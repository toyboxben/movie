#!/usr/bin/env python3
"""Generate SH-001, SH-002, SH-003 as a continuity test.

    python3 -u production/generate_first3.py
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
OUT = ROOT / "out" / "seq-01"
KF = ROOT / "out" / "seq-01" / "keyframes"


def p(*parts: str) -> str:
    return "\n\n".join(x.strip() for x in parts if x and x.strip())


def kit_urls() -> dict:
    manifest = json.loads((ROOT / "refs" / "kit" / "manifest.json").read_text())
    return manifest["urls"]


def run_still(name: str, body: dict, key_id: str, secret: str) -> Path:
    print(f"\n→ keyframe {name}", flush=True)
    request_id = submit(SOUL_REF, key_id, secret, body)
    print(f"  queued {request_id}", flush=True)
    result = poll(request_id, key_id, secret)
    if result.get("status") != "completed":
        raise SystemExit(f"{name} still failed: {json.dumps(result)[:800]}")
    urls = media_urls(result)
    if not urls:
        raise SystemExit(f"{name} still had no URL: {json.dumps(result)[:800]}")
    dest = next_path(KF, name, ".jpg")
    download(urls[0], dest)
    print(f"  saved {dest.relative_to(ROOT)}", flush=True)
    return dest


def run_clip(name: str, still: Path, motion: str, key_id: str, secret: str, end: Path | None = None) -> Path:
    still = still if still.is_absolute() else ROOT / still
    print(f"\n→ clip {name} from {still.relative_to(ROOT)}", flush=True)
    body = {
        "prompt": motion,
        "image_url": upload_image(still, key_id, secret),
        "enhance_prompt": False,
    }
    if end is not None:
        end = end if end.is_absolute() else ROOT / end
        body["end_image_url"] = upload_image(end, key_id, secret)
        print(f"  last frame {end.relative_to(ROOT)}", flush=True)
    request_id = submit(I2V, key_id, secret, body)
    print(f"  queued {request_id}", flush=True)
    result = poll(request_id, key_id, secret, timeout_s=600)
    if result.get("status") != "completed":
        raise SystemExit(f"{name} clip failed: {json.dumps(result)[:800]}")
    urls = media_urls(result)
    if not urls:
        raise SystemExit(f"{name} clip had no URL: {json.dumps(result)[:800]}")
    dest = next_path(OUT, name, ".mp4")
    download(urls[0], dest)
    print(f"  saved {dest.relative_to(ROOT)}", flush=True)
    return dest


def main() -> int:
    key_id, secret = credentials()
    urls = kit_urls()
    chamber = ROOT / "refs" / "bedroom" / "WP-bedroom-chamber-01.jpg"
    if not chamber.exists():
        raise SystemExit("Missing chamber plate. Generate plates first.")

    room = (
        "The room MUST match the locked bedroom: wooden desk, cube 3D printer with a hot "
        "orange chamber glow CAMERA RIGHT, cool blue moonlight through a window CAMERA LEFT, "
        "pinned unfinished robot sketches on the wall, a crowded pen cup, a small blank white "
        "figurine half-buried in the pens, teal cargo-short kid in a yellow hoodie. Painterly "
        "3D animation, Arcane-like, 16:9 cinematic still. No text, no logos, no UI labels."
    )

    # SH-002 landing: Kit in the room. Identity from the frozen front still.
    kf002 = run_still(
        "KF-002",
        {
            "prompt": p(
                "Cinematic still, 35mm, eye level. The SAME 11-year-old Black boy as the "
                "reference image, hunched at a desk, absorbed in a computer screen, working. "
                "Bright yellow hoodie, teal cargo shorts, red high-tops with white laces, "
                "dark grey messenger bag, thick red marker tucked behind his right ear. "
                "Face, hair, and clothes must match the reference exactly. He is not looking "
                "at camera.",
                B.PLATES["WP-bedroom-night"],
                room,
                B.STYLE_LOCK,
            ),
            "image_reference_url": urls["refs/kit/views/02-three-quarter-left.jpg"],
            "aspect_ratio": "16:9",
            "resolution": "1080p",
            "enhance_prompt": False,
        },
        key_id,
        secret,
    )

    # SH-003: over-shoulder, same kid, same room.
    kf003 = run_still(
        "KF-003",
        {
            "prompt": p(
                "Cinematic still, 50mm over-the-shoulder. Camera behind the SAME 11-year-old "
                "Black boy's right shoulder. Yellow hoodie fills the left foreground. He is "
                "looking at a computer screen showing a detailed robot dog 3D model, solid "
                "with a faint wireframe overlay, rotating. NO readable text, NO UI, NO logos "
                "on the screen. Screen glow on his shoulder. Thick red marker behind the "
                "right ear if the ear is visible.",
                B.PLATES["WP-bedroom-night"],
                room,
                B.STYLE_LOCK,
            ),
            "image_reference_url": urls["refs/kit/views/05-rear.jpg"],
            "aspect_ratio": "16:9",
            "resolution": "1080p",
            "enhance_prompt": False,
        },
        key_id,
        secret,
    )

    run_clip(
        "SH-001",
        chamber,
        "Locked-off extreme macro. A brass nozzle slowly lays down one single glowing line "
        "of molten material left to right across a glass print bed. The line cools from "
        "bright amber to solid colour behind the nozzle. Dust motes drift. Nothing else "
        "moves. No camera move.",
        key_id,
        secret,
    )
    run_clip(
        "SH-002",
        kf002,
        "Slow cinematic pull out from a medium shot of the boy at the desk to a wider view "
        "of the whole bedroom. He stays hunched, working, barely moving. Printer glows "
        "orange on the right, window moonlight on the left. Dust in the air. Smooth slow "
        "camera move only.",
        key_id,
        secret,
    )
    run_clip(
        "SH-003",
        kf003,
        "Locked-off over-the-shoulder. The robot dog model on the screen rotates slowly. "
        "The boy is still. Screen light flickers faintly on his yellow hoodie. No camera "
        "move. No text appears on the screen.",
        key_id,
        secret,
    )
    print("\nDone. Keyframes in out/seq-01/keyframes/, clips in out/seq-01/", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
