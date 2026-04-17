from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx

from invoker.http.ratelimit import TokenBucket
from invoker.logging import get_logger, log_event


@dataclass
class SourceLimits:
    """Declared rate caps per source. Per-minute is the narrower gate for us."""

    name: str
    per_minute: int
    per_day: int | None = None


OPENDOTA = SourceLimits("opendota", per_minute=60, per_day=3000)
STRATZ = SourceLimits("stratz", per_minute=250, per_day=10_000)

logger = get_logger(__name__)


def _cache_key(method: str, url: str, params: dict[str, Any] | None, body: Any) -> str:
    blob = json.dumps(
        {"m": method, "u": url, "p": params or {}, "b": body}, sort_keys=True
    ).encode()
    return hashlib.sha256(blob).hexdigest()[:16]


class CachedClient:
    """
    httpx-based client with a per-source token bucket and on-disk cache
    keyed on (source, method, url, params, body).
    """

    def __init__(
        self,
        source: SourceLimits,
        cache_root: Path,
        patch: str,
        headers: dict[str, str] | None = None,
        timeout: float = 30.0,
    ) -> None:
        self.source = source
        self.cache_root = cache_root / source.name / patch
        self.cache_root.mkdir(parents=True, exist_ok=True)
        self.bucket = TokenBucket(rate=source.per_minute / 60.0, capacity=source.per_minute)
        self._client = httpx.AsyncClient(headers=headers or {}, timeout=timeout)

    async def close(self) -> None:
        await self._client.aclose()

    async def get(
        self, url: str, params: dict[str, Any] | None = None, *, force: bool = False
    ) -> Any:
        return await self._request("GET", url, params=params, body=None, force=force)

    async def post(self, url: str, body: Any, *, force: bool = False) -> Any:
        return await self._request("POST", url, params=None, body=body, force=force)

    async def _request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None,
        body: Any,
        force: bool,
    ) -> Any:
        key = _cache_key(method, url, params, body)
        cache_path = self.cache_root / f"{key}.json"
        if not force and cache_path.exists():
            log_event(
                logger,
                logging.INFO,
                "source_cache_hit",
                source=self.source.name,
                method=method,
                url=url,
                key=key,
            )
            return json.loads(cache_path.read_text())

        await self.bucket.acquire()
        log_event(
            logger,
            logging.INFO,
            "source_request",
            source=self.source.name,
            method=method,
            url=url,
            key=key,
            force=force,
        )
        r = await self._client.request(method, url, params=params, json=body)
        r.raise_for_status()
        payload = r.json()
        cache_path.write_text(json.dumps(payload, ensure_ascii=False))
        return payload
