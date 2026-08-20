#!/usr/bin/env python3
"""Generate Seq 01 plates, then SH-001 (chamber still + 5s clip).

    python3 production/generate_seq01.py
    python3 production/generate_seq01.py --plates-only
    python3 production/generate_seq01.py --clip-only --from refs/bedroom/WP-bedroom-chamber-01.jpg
"""

from __future__ import annotations

import argparse
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

SOUL = "higgsfield-ai/soul/standard"
# Seedance v1 is not enabled on this account (model_not_found). DoP is Higgsfield's I2V.
I2V = "higgsfield-ai/dop/standard"
NEGATIVE = B.NEGATIVE_LOCK.removeprefix("NEGATIVE: ").strip()


def still_prompt(*parts: str) -> str:
    return "\n\n".join(p.strip() for p in parts if p and p.strip())


PLATES = [
    {
        "id": "WP-bedroom-night",
        "takes": 2,
        "prompt": still_prompt(
            "Cinematic 21:9 still, wide shot of an empty eleven-year-old boy's bedroom at night. "
            "NO people, NO faces, NO hands, empty wooden chair at the desk. Human scale.",
            B.PLATES["WP-bedroom-night"],
            "A small blank white featureless figurine, about two inches tall, sits half-buried "
            "among the pens in the pen cup. Visible but not centred, not specially lit.",
            "Cool blue moonlight from the WINDOW ON CAMERA LEFT. Hot orange printer glow from "
            "CAMERA RIGHT, low. Two-source lighting only. 21:9 cinematic framing.",
            B.STYLE_LOCK,
        ),
    },
    {
        "id": "WP-bedroom-chamber",
        "takes": 1,
        "prompt": still_prompt(
            "Cinematic 21:9 extreme macro still. First frame of a film. A brass 3D-printer "
            "nozzle hangs in the upper left, beginning to lay one glowing line of molten "
            "material left to right across a textured glass bed. The line is the only bright "
            "thing in frame. Nothing else moves. NO people, NO text, NO UI.",
            B.PLATES["WP-bedroom-chamber"],
            B.STYLE_LOCK,
        ),
    },
    {
        "id": "WP-bedroom-drawer",
        "takes": 1,
        "prompt": still_prompt(
            "Cinematic 21:9 still looking straight down into an open desk drawer. NO people, "
            "NO hands, NO faces.",
            B.PLATES["WP-bedroom-drawer"],
            B.STYLE_LOCK,
        ),
    },
]


def generate_still(job_id: str, prompt: str, key_id: str, secret: str) -> Path:
    print(f"\n→ still {job_id}")
    body = {
        "prompt": prompt,
        "aspect_ratio": "21:9",
        "resolution": "1080p",
        "negative_prompt": NEGATIVE + ", people, person, face, hands, child, boy",
    }
    try:
        request_id = submit(SOUL, key_id, secret, body)
    except SystemExit as exc:
        if "aspect_ratio" in str(exc) or "422" in str(exc):
            print("  21:9 rejected, retrying 16:9")
            body["aspect_ratio"] = "16:9"
            request_id = submit(SOUL, key_id, secret, body)
        else:
            raise
    print(f"  queued {request_id}")
    result = poll(request_id, key_id, secret)
    if result.get("status") != "completed":
        raise SystemExit(f"{job_id} failed: {json.dumps(result)[:800]}")
    urls = media_urls(result)
    if not urls:
        raise SystemExit(f"{job_id} completed with no image URL: {json.dumps(result)[:800]}")
    dest = next_path(ROOT / "refs" / "bedroom", job_id, ".jpg")
    download(urls[0], dest)
    print(f"  saved {dest.relative_to(ROOT)}")
    return dest


def generate_clip(still: Path, key_id: str, secret: str) -> Path:
    still = still if still.is_absolute() else ROOT / still
    print(f"\n→ SH-001 I2V from {still.relative_to(ROOT)}", flush=True)
    image_url = upload_image(still, key_id, secret)
    motion = (
        "Locked-off extreme macro. A brass nozzle slowly lays down one single glowing line "
        "of molten material left to right across a glass print bed. The line cools from "
        "bright amber to solid colour behind the nozzle. Dust motes drift. Nothing else "
        "moves. Shallow depth of field. No camera move."
    )
    request_id = submit(
        I2V,
        key_id,
        secret,
        {
            "prompt": motion,
            "image_url": image_url,
            "enhance_prompt": False,
        },
    )
    print(f"  queued {request_id}")
    result = poll(request_id, key_id, secret, timeout_s=600)
    if result.get("status") != "completed":
        raise SystemExit(f"SH-001 failed: {json.dumps(result)[:800]}")
    urls = media_urls(result)
    if not urls:
        raise SystemExit(f"SH-001 completed with no video URL: {json.dumps(result)[:800]}")
    dest = next_path(ROOT / "out" / "seq-01", "SH-001", ".mp4")
    download(urls[0], dest)
    print(f"  saved {dest.relative_to(ROOT)}")
    return dest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plates-only", action="store_true")
    parser.add_argument("--clip-only", action="store_true")
    parser.add_argument("--from", dest="still_from", default="")
    args = parser.parse_args()

    key_id, secret = credentials()
    chamber: Path | None = Path(args.still_from) if args.still_from else None

    if not args.clip_only:
        for plate in PLATES:
            last = None
            for _ in range(plate["takes"]):
                last = generate_still(plate["id"], plate["prompt"], key_id, secret)
            if plate["id"] == "WP-bedroom-chamber":
                chamber = last

    if args.plates_only:
        return 0

    if chamber is None or not chamber.exists():
        existing = sorted((ROOT / "refs" / "bedroom").glob("WP-bedroom-chamber-*.jpg"))
        if not existing:
            raise SystemExit("No chamber still. Generate plates first.")
        chamber = existing[-1]

    generate_clip(chamber, key_id, secret)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
