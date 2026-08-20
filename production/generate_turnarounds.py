#!/usr/bin/env python3
"""Generate character turnaround stills via the Higgsfield API.

Requires credentials in a local .env (never committed):

    HF_API_KEY_ID=...
    HF_API_KEY_SECRET=...

Usage:
    python production/generate_turnarounds.py                  # Kit turnaround only
    python production/generate_turnarounds.py --character all  # every sheet
    python production/generate_turnarounds.py --character kit --sheet expressions
    python production/generate_turnarounds.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "production"))

import blocks as B  # noqa: E402

API = "https://platform.higgsfield.ai"
MODEL = "higgsfield-ai/soul/standard"

STYLE = (
    "STYLE: painterly 3D animation, hand-painted textures over dimensional forms, visible "
    "brushstroke in the shadows, thick graphic silhouettes, painted volumetric light, rich "
    "saturated color with deep teal shadows and warm amber key light, subtle film grain. "
    "Character sheet on a flat neutral mid-grey background, even three-point studio lighting, "
    "full body visible, consistent scale and consistent eye-line across all views, no cropping. "
    "No text, no labels, no logos, no watermarks."
)

NEGATIVE = (
    "photorealistic, live action, uncanny realistic skin, glossy plastic CGI sheen, "
    "flat lighting, muddy color, extra limbs, extra fingers, deformed hands, warped face, "
    "inconsistent proportions between views, text, labels, watermark, logo, anime, "
    "flat cel shading, cluttered background"
)


def prompt(*parts: str) -> str:
    return "\n\n".join(p.strip() for p in parts if p and p.strip())


JOBS = [
    {
        "id": "kit-turnaround",
        "character": "kit",
        "sheet": "turnaround",
        "aspect_ratio": "16:9",
        "prompt": prompt(
            "Character turnaround sheet, EXACTLY SIX full-body views in a single horizontal row, "
            "all at identical scale and identical eye-line, left to right: 1 front, 2 three-quarter "
            "left, 3 full left profile, 4 three-quarter right, 5 full right profile, 6 rear. Not five "
            "views. Six.",
            B.CHARACTERS["KIT"],
            "CRITICAL LOCKS, identical in every view, matching refs/kit/CANONICAL-turnaround.jpg: "
            "bright saturated yellow hoodie (not mustard), dark grey messenger bag with a single "
            "diagonal strap (left shoulder to right hip), stubby red carpenter's pencil behind the "
            "right ear in ALL views, white laces on both shoes, white crew socks. Same face as the "
            "canonical sheet. Neutral relaxed expression, arms at his sides, standing straight.",
            STYLE,
        ),
    },
    {
        "id": "kit-expressions",
        "character": "kit",
        "sheet": "expressions",
        "aspect_ratio": "16:9",
        "prompt": prompt(
            "Character expression sheet, ten head-and-shoulders portraits of the same boy in a "
            "grid, front-facing, identical lighting and identical scale in every panel.",
            B.CHARACTERS["KIT"],
            "The ten expressions in order: 1 neutral, 2 his default half-grin, 3 mid-sentence and "
            "animated while selling an idea, 4 openly delighted, 5 embarrassed and looking away, "
            "6 defensive with his chin up, 7 caught out and going quiet, 8 furious, 9 crying with "
            "his face screwed up and ugly, 10 quiet resolve looking directly at camera.",
            STYLE,
        ),
    },
    {
        "id": "kit-poses",
        "character": "kit",
        "sheet": "poses",
        "aspect_ratio": "16:9",
        "prompt": prompt(
            "Character pose sheet, six full-body views of the same boy, identical scale, "
            "neutral grey background.",
            B.CHARACTERS["KIT"],
            "Poses: 1 standing relaxed, 2 mid-stride walking, 3 running hard, 4 crouched down "
            "low examining something on the ground, 5 both arms raised in triumph, 6 drawing in "
            "the air with the red carpenter's pencil held like a wand, a glowing amber trail "
            "following the tip.",
            STYLE,
        ),
    },
    {
        "id": "kit-camera-height",
        "character": "kit",
        "sheet": "camera-height",
        "aspect_ratio": "16:9",
        "prompt": prompt(
            "Four views of the same boy, each from a dramatically different camera height, full "
            "body, neutral grey background, identical lighting.",
            B.CHARACTERS["KIT"],
            "CRITICAL LOCKS in every panel, matching refs/kit/CANONICAL-turnaround.jpg: bright "
            "saturated yellow hoodie, dark grey messenger bag with a single diagonal strap, stubby "
            "red carpenter's pencil behind the right ear, white laces, white crew socks. Same face "
            "as the canonical sheet. 1: extreme low angle from ground level looking steeply up at "
            "him, heavily foreshortened, he looms enormous. 2: high angle looking down on him from "
            "above. 3: straight-on eye level. 4: over-the-shoulder from behind his right shoulder.",
            STYLE,
        ),
    },
    {
        "id": "kit-hands",
        "character": "kit",
        "sheet": "hands",
        "aspect_ratio": "16:9",
        "prompt": prompt(
            "Four close-up studies of the same boy's hands, neutral grey background, even lighting. "
            "Warm brown skin, an 11-year-old boy's hands, correct anatomy, exactly five fingers "
            "per hand. 1: holding a stubby flat red carpenter's pencil in a writing grip. 2: mid-air "
            "drawing gesture with the pencil, a glowing amber filament trail curling from the tip. "
            "3: open palm facing up. 4: reaching down toward the ground as if to pick up something "
            "very small.",
            STYLE,
        ),
    },
    {
        "id": "kit-lighting",
        "character": "kit",
        "sheet": "lighting",
        "aspect_ratio": "16:9",
        "prompt": prompt(
            "Six head-and-shoulders portraits of the same boy, identical neutral expression and "
            "identical angle in all six, differing only in lighting.",
            B.CHARACTERS["KIT"],
            "1: warm amber key light from camera left. 2: deep teal rim light from behind, dark "
            "front. 3: single hot orange point light low and close, like a fire or a machine glow. "
            "4: near silhouette against a bright background. 5: flat even neutral light. 6: hard "
            "top light.",
            STYLE,
        ),
    },
    {
        "id": "june-turnaround",
        "character": "june",
        "sheet": "turnaround",
        "aspect_ratio": "16:9",
        "prompt": prompt(
            "Character turnaround sheet, six views in a single horizontal row, all at identical "
            "scale and identical eye-line: front view, three-quarter left, full left profile, "
            "three-quarter right, full right profile, and rear view.",
            B.CHARACTERS["JUNE"],
            "Neutral expression, standing straight, solid arm at her side and wireframe arm held "
            "close to her body. Identical proportions in every view. The hollow left side must "
            "read as genuinely empty in all six views — background visible through the struts.",
            STYLE,
        ),
    },
    {
        "id": "june-empty-side",
        "character": "june",
        "sheet": "empty-side",
        "aspect_ratio": "3:4",
        "prompt": prompt(
            "Single full-body view of the same one-of-a-kind printed girl creature, turned to "
            "three-quarter left so her unfinished side faces camera, backlit hard from behind so "
            "that the hollow wireframe struts of her left arm, shoulder, half-torso and half-leg "
            "read as completely empty open outline with bright background visible through the gaps. "
            "Her solid plum and burnt orange right side falls into shadow. Emphasise that there is "
            "nothing inside the wireframe.",
            B.CHARACTERS["JUNE"],
            STYLE,
        ),
    },
    {
        "id": "colossus-turnaround",
        "character": "colossus",
        "sheet": "turnaround",
        "aspect_ratio": "16:9",
        "prompt": prompt(
            "Character turnaround sheet, five views in a single horizontal row at identical scale "
            "and eye-line: front, three-quarter, full side profile, direct rear, and top-down.",
            B.CHARACTERS["COLOSSUS"],
            "The side profile view must clearly show that he is only a front half. The rear view "
            "looks directly into the open hollow cross-section where the rest of his body should "
            "be. NO hind legs, NO tail, NO back half in any view.",
            STYLE,
        ),
    },
    {
        "id": "benchy-turnaround",
        "character": "benchy",
        "sheet": "turnaround",
        "aspect_ratio": "16:9",
        "prompt": prompt(
            "Character turnaround sheet, five views in a single horizontal row at identical scale "
            "and identical waterline: bow-on front, three-quarter bow, full side profile, "
            "three-quarter stern, direct stern.",
            B.CHARACTERS["BENCHY"],
            STYLE,
        ),
    },
    {
        "id": "tower-turnaround",
        "character": "tower",
        "sheet": "turnaround",
        "aspect_ratio": "3:4",
        "prompt": prompt(
            "Character turnaround sheet, four views in a single horizontal row at identical scale: "
            "front, three-quarter, side profile, rear.",
            B.CHARACTERS["TOWER"],
            "Exactly ten blocks. Crisp at the bottom, melted at the top.",
            STYLE,
        ),
    },
    {
        "id": "finisher-turnaround",
        "character": "finisher",
        "sheet": "turnaround",
        "aspect_ratio": "3:4",
        "prompt": prompt(
            "Character turnaround sheet, five views in a single horizontal row at identical scale "
            "and eye-line: front, three-quarter left, full left profile, three-quarter right, rear.",
            B.CHARACTERS["FINISHER"],
            "His surface is completely smooth and completely untextured. He casts no visible "
            "shadow and light falls on him flatly with no rim highlight.",
            STYLE,
        ),
    },
]


def load_env() -> None:
    path = ROOT / ".env"
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def credentials() -> tuple[str, str]:
    load_env()
    key_id = os.environ.get("HF_API_KEY_ID", "").strip()
    secret = os.environ.get("HF_API_KEY_SECRET", "").strip()
    combo = os.environ.get("HF_KEY", "").strip() or os.environ.get("HF_CREDENTIALS", "").strip()
    if combo and ":" in combo and not (key_id and secret):
        key_id, _, secret = combo.partition(":")
    if not key_id or not secret:
        sys.exit(
            "Missing Higgsfield credentials.\n"
            "Create .env in the repo root with:\n"
            "  HF_API_KEY_ID=...\n"
            "  HF_API_KEY_SECRET=...\n"
            "Get them from https://cloud.higgsfield.ai"
        )
    return key_id, secret


def request(method: str, url: str, key_id: str, secret: str, body: dict | None = None) -> dict:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Key {key_id}:{secret}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) first-layer/0.1",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = resp.read().decode()
            return json.loads(payload) if payload else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        raise SystemExit(f"Higgsfield {exc.code} on {url}\n{detail}") from exc


def submit(job: dict, key_id: str, secret: str) -> str:
    payload = {
        "prompt": job["prompt"],
        "aspect_ratio": job["aspect_ratio"],
        "resolution": "1080p",
        "negative_prompt": NEGATIVE,
    }
    result = request("POST", f"{API}/{MODEL}", key_id, secret, payload)
    request_id = result.get("request_id")
    if not request_id:
        raise SystemExit(f"No request_id in response: {result}")
    return request_id


def poll(request_id: str, key_id: str, secret: str, timeout_s: int = 300) -> dict:
    url = f"{API}/requests/{request_id}/status"
    deadline = time.time() + timeout_s
    delay = 2.0
    while time.time() < deadline:
        status = request("GET", url, key_id, secret)
        state = status.get("status")
        print(f"    {request_id[:8]}… {state}")
        if state in {"completed", "failed", "nsfw", "canceled"}:
            return status
        time.sleep(delay)
        delay = min(delay * 1.5, 8.0)
    raise SystemExit(f"Timed out waiting for {request_id}")


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=120) as resp, dest.open("wb") as fh:
        fh.write(resp.read())


def image_urls(result: dict) -> list[str]:
    urls: list[str] = []
    for image in result.get("images") or []:
        if isinstance(image, dict) and image.get("url"):
            urls.append(image["url"])
        elif isinstance(image, str):
            urls.append(image)
    for job in result.get("jobs") or []:
        nested = ((job.get("results") or {}).get("raw") or {})
        if nested.get("url"):
            urls.append(nested["url"])
    return urls


def run_job(job: dict, key_id: str, secret: str) -> None:
    print(f"\n→ {job['id']}")
    request_id = submit(job, key_id, secret)
    print(f"  queued {request_id}")
    result = poll(request_id, key_id, secret)
    state = result.get("status")
    if state != "completed":
        print(f"  FAILED ({state}): {json.dumps(result)[:500]}")
        return
    urls = image_urls(result)
    if not urls:
        print(f"  completed but no image URL in payload: {json.dumps(result)[:800]}")
        return
    out_dir = ROOT / "refs" / job["character"]
    out_dir.mkdir(parents=True, exist_ok=True)
    for url in urls:
        n = 1
        while True:
            dest = out_dir / f"{job['id']}-{n:02d}.jpg"
            if not dest.exists():
                break
            n += 1
        download(url, dest)
        print(f"  saved {dest.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--character", default="kit", help="kit|june|colossus|benchy|tower|finisher|all")
    parser.add_argument("--sheet", default="turnaround", help="sheet id, comma-separated, or 'all'")
    parser.add_argument("--count", type=int, default=1, help="repeat each selected job this many times")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    sheets = {s.strip() for s in args.sheet.split(",")}
    selected = []
    for job in JOBS:
        if args.character != "all" and job["character"] != args.character:
            continue
        if "all" not in sheets and job["sheet"] not in sheets:
            continue
        selected.append(job)
    if args.count > 1:
        selected = selected * args.count

    if not selected:
        print("No jobs matched. Try --character kit --sheet all")
        return 1

    print(f"{len(selected)} job(s): {', '.join(j['id'] for j in selected)}")
    if args.dry_run:
        for job in selected:
            print(f"\n=== {job['id']} ===\n{job['prompt'][:400]}…")
        return 0

    key_id, secret = credentials()
    for job in selected:
        run_job(job, key_id, secret)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
