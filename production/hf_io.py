"""Shared Higgsfield REST helpers. Credentials come from repo-root .env."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://platform.higgsfield.ai"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) first-layer/0.1"


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
        raise SystemExit("Missing HF_API_KEY_ID / HF_API_KEY_SECRET in .env")
    return key_id, secret


def api_request(method: str, url: str, key_id: str, secret: str, body: dict | None = None) -> dict:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Key {key_id}:{secret}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = resp.read().decode()
            return json.loads(payload) if payload else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        raise SystemExit(f"Higgsfield {exc.code} on {url}\n{detail}") from exc


def submit(model: str, key_id: str, secret: str, body: dict) -> str:
    result = api_request("POST", f"{API}/{model.lstrip('/')}", key_id, secret, body)
    request_id = result.get("request_id")
    if not request_id:
        raise SystemExit(f"No request_id in response: {result}")
    return request_id


def poll(request_id: str, key_id: str, secret: str, timeout_s: int = 420) -> dict:
    import time

    url = f"{API}/requests/{request_id}/status"
    deadline = time.time() + timeout_s
    delay = 2.0
    last = ""
    while time.time() < deadline:
        status = api_request("GET", url, key_id, secret)
        state = str(status.get("status") or "")
        if state != last:
            print(f"    {request_id[:8]}… {state}", flush=True)
            last = state
        if state in {"completed", "failed", "nsfw", "canceled"}:
            return status
        time.sleep(delay)
        delay = min(delay * 1.4, 8.0)
    raise SystemExit(f"Timed out waiting for {request_id}")


def media_urls(result: dict) -> list[str]:
    urls: list[str] = []
    seen: set[str] = set()

    def add(url: object) -> None:
        if isinstance(url, str) and url.startswith("http") and url not in seen:
            seen.add(url)
            urls.append(url)

    for image in result.get("images") or []:
        if isinstance(image, dict):
            add(image.get("url"))
        else:
            add(image)
    for video in result.get("videos") or []:
        if isinstance(video, dict):
            add(video.get("url"))
        else:
            add(video)
    add(result.get("url"))
    video = result.get("video")
    if isinstance(video, dict):
        add(video.get("url"))
    image = result.get("image")
    if isinstance(image, dict):
        add(image.get("url"))
    for job in result.get("jobs") or []:
        nested = job.get("results") or {}
        if isinstance(nested, dict):
            for key in ("raw", "minimax", "video", "image"):
                blob = nested.get(key) or {}
                if isinstance(blob, dict):
                    add(blob.get("url"))
            add(nested.get("url"))
    return urls


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=180) as resp, dest.open("wb") as fh:
        fh.write(resp.read())


def next_path(directory: Path, stem: str, suffix: str) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    n = 1
    while True:
        dest = directory / f"{stem}-{n:02d}{suffix}"
        if not dest.exists():
            return dest
        n += 1


def upload_image(path: Path, key_id: str, secret: str) -> str:
    """Upload a local still and return the public HTTPS URL Seedance can consume."""
    meta = api_request(
        "POST",
        f"{API}/files/generate-upload-url",
        key_id,
        secret,
        {"content_type": "image/jpeg"},
    )
    upload_url = meta["upload_url"]
    headers = dict(meta.get("upload_headers") or {})
    headers.setdefault("Content-Type", "image/jpeg")
    req = urllib.request.Request(upload_url, data=path.read_bytes(), method="PUT", headers=headers)
    with urllib.request.urlopen(req, timeout=120) as resp:
        resp.read()
    public = meta.get("public_url")
    if not public:
        raise SystemExit(f"Upload succeeded but no public_url: {meta}")
    return public
