#!/usr/bin/env python3
"""Split Kit's canonical sheets into single-view stills and upload them.

Seedance needs one composed frame per clip, not a 5-across turnaround sheet.
These crops are the identity pack: use the matching angle as the character
reference when generating a shot keyframe, then I2V that keyframe.

    python production/prepare_kit_refs.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "production"))

from hf_io import credentials, upload_image  # noqa: E402

KIT = ROOT / "refs" / "kit"
VIEWS = KIT / "views"


def slice_row(src: Path, names: list[str], inset: float = 0.02) -> list[Path]:
    im = Image.open(src)
    w, h = im.size
    n = len(names)
    col = w / n
    pad = int(col * inset)
    VIEWS.mkdir(parents=True, exist_ok=True)
    out = []
    for i, name in enumerate(names):
        left = int(i * col) + pad
        right = int((i + 1) * col) - pad
        crop = im.crop((left, 0, right, h))
        dest = VIEWS / f"{name}.jpg"
        crop.convert("RGB").save(dest, quality=95)
        out.append(dest)
        print(f"  crop {dest.relative_to(ROOT)}  {crop.size}")
    return out


def main() -> int:
    print("Splitting canonical Kit sheets into single views")
    files = []
    files += slice_row(
        KIT / "CANONICAL-turnaround.jpg",
        ["01-front", "02-three-quarter-left", "03-three-quarter-right", "04-profile-right", "05-rear"],
    )
    files += slice_row(
        KIT / "kit-camera-height-01.jpg",
        ["06-low-angle", "07-front-worried", "08-front-worried-b", "09-rear-alt"],
    )

    print("\nUploading to Higgsfield so Seedance can take public URLs")
    key_id, secret = credentials()
    urls = {}
    for path in [KIT / "CANONICAL-turnaround.jpg", *files]:
        url = upload_image(path, key_id, secret)
        rel = str(path.relative_to(ROOT))
        urls[rel] = url
        print(f"  {rel}")

    manifest = {
        "character": "kit",
        "canonical_sheet": "refs/kit/CANONICAL-turnaround.jpg",
        "identity": "Use these stills as image references. Do not text-to-video Kit.",
        "views": {
            "front": "refs/kit/views/01-front.jpg",
            "three_quarter": "refs/kit/views/02-three-quarter-left.jpg",
            "three_quarter_right": "refs/kit/views/03-three-quarter-right.jpg",
            "profile": "refs/kit/views/04-profile-right.jpg",
            "rear": "refs/kit/views/05-rear.jpg",
            "low_angle": "refs/kit/views/06-low-angle.jpg",
        },
        "height_default": {
            "toy": "low_angle",
            "ground": "low_angle",
            "eye": "front",
            "high": "front",
            "n/a": "front",
        },
        "urls": urls,
    }
    dest = KIT / "manifest.json"
    dest.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"\n  wrote {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
