from __future__ import annotations

import base64
import json
from typing import Any

from fastapi import FastAPI, Request
import zstandard as zstd

app = FastAPI(title="Thryve Webhook", version="0.1.0")


def _decompress_zstd(payload: bytes) -> bytes:
    decompressor = zstd.ZstdDecompressor()
    return decompressor.decompress(payload)


def _decode_payload(raw_body: bytes, content_encoding: str) -> bytes:
    if content_encoding != "zstd" or not raw_body:
        return raw_body

    try:
        return _decompress_zstd(raw_body)
    except zstd.ZstdError:
        pass

    try:
        decoded = base64.b64decode(raw_body, validate=True)
        return _decompress_zstd(decoded)
    except Exception:
        return raw_body


@app.post("/webhooks/thryve")
async def thryve_webhook(request: Request) -> dict[str, Any]:
    raw_body = await request.body()
    content_encoding = request.headers.get("content-encoding", "").lower()
    decoded_body = _decode_payload(raw_body, content_encoding)
    text_body = decoded_body.decode("utf-8", errors="replace") if decoded_body else ""

    payload: Any | None = None
    if decoded_body:
        try:
            payload = json.loads(text_body)
        except Exception:
            payload = {"raw": text_body}

    if payload is None:
        payload = {}

    print("Thryve webhook received:", payload)
    return {"status": "ok"}
