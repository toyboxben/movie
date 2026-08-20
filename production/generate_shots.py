#!/usr/bin/env python3
"""Generate Seq 01 shots 001–003 as a continuity test.

Uses Soul Reference for Kit keyframes (identity from the frozen still pack)
and Higgsfield DoP for image-to-video (Seedance is not on this API account).

    PYTHONUNBUFFERED=1 python3 production/generate_shots.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "production"))

import blocks as B  # noqa: E402
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
I2V = "higgsfield-ai/dop/standard"
NEGATIVE = B.NEGATIVE_LOCK.removeprefix("NEGATIVE: ").strip()
MANIFEST = json.loads((ROOT / "refs" / "kit" / "manifest.json").read_text())
KIT_URLS = MANIFEST["urls"]


def join(*parts: str) -> str:
    return "\n\n".join(p.strip() for p in parts if p and p.strip())


def soul_still(name: str, prompt: str, ref_url: str, key_id: str, secret: str) -> Path:
    print(f"\n→ keyframe {name}", flush=True)
    request_id = submit(
        SOUL_REF,
        key_id,
        secret,
        {
            "prompt": prompt,
            "image_reference_url": ref_url,
            "aspect_ratio": "16:9",
            "resolution": "1080p",
            "enhance_prompt": False,
        },
    )
    print(f"  queued {request_id}", flush=True)
    result = poll(request_id, key_id, secret)
    if result.get("status") != "completed":
        raise SystemExit(f"{name} still failed: {json.dumps(result)[:800]}")
    urls = media_urls(result)
    if not urls:
        raise SystemExit(f"{name} still had no URL: {json.dumps(result)[:800]}")
    dest = next_path(ROOT / "out" / "seq-01", name, ".jpg")
    download(urls[0], dest)
    print(f"  saved {dest.relative_to(ROOT)}", flush=True)
    return dest


def i2v(name: str, still: Path, motion: str, key_id: str, secret: str, end: Path | None = None) -> Path:
    print(f"\n→ clip {name} from {still.relative_to(ROOT)}", flush=True)
    body = {
        "prompt": motion,
        "image_url": upload_image(still, key_id, secret),
        "enhance_prompt": False,
    }
    if end is not None:
        body["end_image_url"] = upload_image(end, key_id, secret)
    request_id = submit(I2V, key_id, secret, body)
    print(f"  queued {request_id}", flush=True)
    result = poll(request_id, key_id, secret, timeout_s=600)
    if result.get("status") != "completed":
        raise SystemExit(f"{name} clip failed: {json.dumps(result)[:800]}")
    urls = media_urls(result)
    if not urls:
        raise SystemExit(f"{name} clip had no URL: {json.dumps(result)[:800]}")
    dest = next_path(ROOT / "out" / "seq-01", name, ".mp4")
    download(urls[0], dest)
    print(f"  saved {dest.relative_to(ROOT)}", flush=True)
    return dest


KF002 = join(
    "Cinematic still, 35mm, eye level. The SAME boy as the reference image, face and "
    "wardrobe locked: bright yellow hoodie, teal cargo shorts, red high-tops with white "
    "laces, dark grey messenger bag, thick red marker behind the right ear. He is hunched "
    "at a wooden desk at night, absorbed in a screen, slightly from the side/three-quarter. "
    "He is 11. Smooth painterly skin, no 3D-print ring lines.",
    B.PLATES["WP-bedroom-night"],
    "A small blank white featureless figurine sits half-buried among the pens in the pen cup, "
    "visible but not centred. Cool blue moonlight camera-left, hot orange printer glow "
    "camera-right. No text, no logos, no UI.",
    B.STYLE_LOCK,
)

KF003 = join(
    "Cinematic still, 50mm, locked off, over-the-shoulder. Camera behind the SAME boy's "
    "right shoulder looking at a computer screen. Yellow hoodie shoulder and dark curly "
    "hair fill the left foreground, out of focus. On the screen: a detailed robot dog 3D "
    "model rotating, wireframe over solid, NO readable text, NO UI, NO logos. Screen glow "
    "on his shoulder. Face mostly unseen. Wardrobe locked to the reference.",
    B.PLATES["WP-bedroom-night"],
    "Cool blue moonlight camera-left, hot orange printer glow camera-right. No text.",
    B.STYLE_LOCK,
)


def main() -> int:
    key_id, secret = credentials()

    kf002 = soul_still(
        "KF-002",
        KF002,
        KIT_URLS["refs/kit/views/02-three-quarter-left.jpg"],
        key_id,
        secret,
    )
    kf003 = soul_still(
        "KF-003",
        KF003,
        KIT_URLS["refs/kit/views/05-rear.jpg"],
        key_id,
        secret,
    )

    i2v(
        "SH-002",
        kf002,
        "Slow pull out at eye level. The boy stays hunched at the desk, absorbed, small "
        "natural movements only. The room around him is revealed. Printer chamber glows "
        "orange on the right. Cool moonlight from the left. No morphing of the face.",
        key_id,
        secret,
    )
    i2v(
        "SH-003",
        kf003,
        "Locked-off over-the-shoulder. The robot dog model on the screen rotates slowly. "
        "The boy is still. Screen light flickers faintly. No camera move. No text.",
        key_id,
        secret,
    )
    print("\nDone. Clips in out/seq-01/", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
