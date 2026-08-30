#!/usr/bin/env python3
"""Generate Draftlands cold-open first 15s using Quill hero refs.

Uses Higgsfield platform API:
  1) Soul Reference still (identity from hero pack)
  2) Image-to-video (prefers Seedance 2.5 if available; falls back to DoP)

    PYTHONUNBUFFERED=1 python3 -u production/generate_draftlands_cold_open.py

Credentials: HF_API_KEY_ID + HF_API_KEY_SECRET in env or repo-root .env
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "production"))

from hf_io import (  # noqa: E402
    credentials,
    download,
    media_urls,
    next_path,
    poll,
    submit,
    upload_image,
)

SOUL_REF = "higgsfield-ai/soul/reference"
# Prefer Seedance 2.5 per series bible; DoP was the working path on older accounts.
I2V_CANDIDATES = [
    os.environ.get("HF_I2V_MODEL", "").strip(),
    "higgsfield-ai/seedance/2.5",
    "higgsfield-ai/seedance/2.0",
    "bytedance/seedance/v1/pro/image-to-video",
    "higgsfield-ai/dop/standard",
]
I2V_CANDIDATES = [m for m in I2V_CANDIDATES if m]

HERO = ROOT / "assets" / "draftlands" / "hero"
OUT = ROOT / "out" / "draftlands"
KF = OUT / "keyframes"

STYLE = (
    "Painterly hybrid 2D+3D animation, bold visible brushstrokes on face and cloth, "
    "painted textures, cinematic folklore lighting, terracotta and amber-gold Potential dust, "
    "subtle film grain, 16:9 cinematic framing, 24fps feel. No text, no logos, no UI, no subtitles."
)

NEGATIVE = (
    "photorealistic, live action, uncanny realistic human skin, glossy plastic CGI sheen, "
    "anime flat cel, extra fingers, deformed hands, warped face, morphing features, text, "
    "watermark, logo, subtitles, fur hood, snow steppe, wolves, cute little-kid proportions, "
    "rainbow magic beams, HUD, tablet UI, Pixar-smooth CG"
)

STILL_PROMPT = f"""
Cinematic still, 35mm, slight low angle looking up. The SAME mid-teen boy as the reference:
messy dark hair, intense eyes, olive-green worn tunic, brown patched pants, leather satchel strap,
thick off-white bound book held against his chest, white bandage on left wrist, gold-stained fingertips.
He looks UP into a thickening amber haze of glowing dust motes (Potential) as the sky bruises above a
narrow run-down street with wooden scaffolds and slamming shutters. Crowd silhouettes flee the other way.
Serious, dual-audience animation — not cute preschool.

{STYLE}
""".strip()

MOTION_PROMPT = f"""
Fifteen-second cold open. Keep the SAME boy's face and wardrobe locked to the reference image — no morphing.
0-3s: amber dust motes thicken in the air; shutters slam; wind rises; sky darkens with a bruise of light.
3-7s: he looks up harder into the bloom, book clutched, gold fingertips catching light.
7-11s: he opens the book; a thin gold ribbon-line lifts off the page into the air like glowing filament.
11-15s: he runs TOWARD the thickening storm while others flee past him; camera pushes with him; end on his
determined face entering the amber whiteout.
Natural motion only. No dialogue captions. No text.

{STYLE}
""".strip()


def join(*parts: str) -> str:
    return "\n\n".join(p.strip() for p in parts if p and p.strip())


def pick_ref() -> Path:
    preferred = [
        HERO / "var-v4-looking-up.png",
        HERO / "var-v1-three-quarter.png",
        HERO / "var-v2-front.png",
    ]
    for path in preferred:
        if path.exists():
            return path
    raise SystemExit(f"No hero refs found under {HERO}")


def make_still(key_id: str, secret: str, ref: Path) -> Path:
    KF.mkdir(parents=True, exist_ok=True)
    print(f"→ keyframe from {ref.relative_to(ROOT)}", flush=True)
    ref_url = upload_image(ref, key_id, secret)
    request_id = submit(
        SOUL_REF,
        key_id,
        secret,
        {
            "prompt": STILL_PROMPT,
            "image_reference_url": ref_url,
            "aspect_ratio": "16:9",
            "resolution": "1080p",
            "enhance_prompt": False,
            "negative_prompt": NEGATIVE,
        },
    )
    print(f"  queued {request_id}", flush=True)
    result = poll(request_id, key_id, secret, timeout_s=600)
    if result.get("status") != "completed":
        raise SystemExit(f"still failed: {json.dumps(result)[:1200]}")
    urls = media_urls(result)
    if not urls:
        raise SystemExit(f"still had no URL: {json.dumps(result)[:1200]}")
    dest = next_path(KF, "KF-cold-open", ".jpg")
    download(urls[0], dest)
    print(f"  saved {dest.relative_to(ROOT)}", flush=True)
    return dest


def make_clip(key_id: str, secret: str, still: Path) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    image_url = upload_image(still, key_id, secret)
    last_error = None
    for model in I2V_CANDIDATES:
        print(f"→ clip via {model}", flush=True)
        body = {
            "prompt": MOTION_PROMPT,
            "image_url": image_url,
            "enhance_prompt": False,
            "negative_prompt": NEGATIVE,
            "duration": 15,
            "resolution": "1080p",
            "aspect_ratio": "16:9",
        }
        try:
            request_id = submit(model, key_id, secret, body)
        except SystemExit as exc:
            last_error = str(exc)
            print(f"  submit failed for {model}: {last_error[:400]}", flush=True)
            continue
        print(f"  queued {request_id}", flush=True)
        result = poll(request_id, key_id, secret, timeout_s=900)
        status = str(result.get("status") or "")
        if status != "completed":
            last_error = json.dumps(result)[:1200]
            print(f"  {model} status={status}: {last_error[:400]}", flush=True)
            continue
        urls = media_urls(result)
        if not urls:
            last_error = json.dumps(result)[:1200]
            continue
        dest = next_path(OUT, "cold-open-15s", ".mp4")
        download(urls[0], dest)
        meta = {
            "model": model,
            "still": str(still.relative_to(ROOT)),
            "request_id": request_id,
            "output": str(dest.relative_to(ROOT)),
            "prompt_file": "prompts/draftlands/COLD_OPEN_15s.md",
        }
        (OUT / "cold-open-15s-latest.json").write_text(json.dumps(meta, indent=2) + "\n")
        print(f"  saved {dest.relative_to(ROOT)}", flush=True)
        return dest
    raise SystemExit(f"All I2V models failed. Last error:\n{last_error}")


def main() -> int:
    key_id, secret = credentials()
    ref = pick_ref()
    still = make_still(key_id, secret, ref)
    clip = make_clip(key_id, secret, still)
    print(f"\nDONE: {clip}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
