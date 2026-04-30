from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlencode, urlparse
from uuid import uuid4

import httpx

from invoker.http.ratelimit import TokenBucket
from invoker.logging import get_logger


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


def _endpoint_path(url: str) -> str:
    path = urlparse(url).path
    if path.startswith("/api/"):
        return path.removeprefix("/api")
    if path == "/api":
        return "/"
    return path or "/"


def _cache_slug(method: str, endpoint: str) -> str:
    cleaned = endpoint.strip("/").replace("/", "_") or "root"
    return f"{method.lower()}_{cleaned}"


def _write_json_atomic(path: Path, payload: Any) -> None:
    tmp_path = path.with_name(f".{path.name}.{os.getpid()}.{uuid4().hex}.tmp")
    tmp_path.write_text(json.dumps(payload, ensure_ascii=False))
    tmp_path.replace(path)


def _shared_response_cache_path(
    responses_dir: Path,
    endpoint: str,
    params: dict[str, Any] | None,
) -> Path:
    clean_endpoint = endpoint.strip("/").replace("/", "_") or "root"
    if not params:
        return responses_dir / f"{clean_endpoint}.json"

    query = urlencode(sorted((k, str(v)) for k, v in params.items()), doseq=True)
    safe_query = "".join(c if c.isalnum() or c in "-_=&" else "_" for c in query)
    return responses_dir / f"{clean_endpoint}__{safe_query}.json"


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
            logger.debug(
                "Source cache hit source=%s method=%s key=%s url=%s",
                self.source.name,
                method,
                key,
                url,
            )
            return json.loads(cache_path.read_text())

        await self.bucket.acquire()
        logger.info(
            "Source request source=%s method=%s key=%s force=%s url=%s",
            self.source.name,
            method,
            key,
            force,
            url,
        )
        r = await self._client.request(method, url, params=params, json=body)
        r.raise_for_status()
        payload = r.json()
        cache_path.write_text(json.dumps(payload, ensure_ascii=False))
        return payload


class SharedOpenDotaCachedClient:
    """
    OpenDota client using the shared Dota agents cache envelope.

    Files are written under $CACHE_DIR/opendota/responses and callers receive
    the raw API payload stored in the envelope's data field.
    """

    def __init__(
        self,
        cache_root: Path,
        *,
        fetched_by: str,
        source_patch: str | None,
        headers: dict[str, str] | None = None,
        timeout: float = 30.0,
    ) -> None:
        self.source = OPENDOTA
        self.cache_root = cache_root / self.source.name / "responses"
        self.cache_root.mkdir(parents=True, exist_ok=True)
        self.fetched_by = fetched_by
        self.source_patch = source_patch
        self.bucket = TokenBucket(
            rate=self.source.per_minute / 60.0,
            capacity=self.source.per_minute,
        )
        self._client = httpx.AsyncClient(headers=headers or {}, timeout=timeout)

    async def close(self) -> None:
        await self._client.aclose()

    async def get(
        self, url: str, params: dict[str, Any] | None = None, *, force: bool = False
    ) -> Any:
        return await self._request("GET", url, params=params, body=None, force=force)

    async def post(self, url: str, body: Any, *, force: bool = False) -> Any:
        return await self._request("POST", url, params=None, body=body, force=force)

    def _cache_path(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None,
        body: Any,
    ) -> Path:
        endpoint = _endpoint_path(url)
        if method != "GET" or body is not None:
            key = _cache_key(method, url, params, body)
            return self.cache_root / f"{_cache_slug(method, endpoint)}_{key}.json"
        return _shared_response_cache_path(self.cache_root, endpoint, params)

    def _read_envelope(self, path: Path) -> Any:
        envelope = json.loads(path.read_text())
        if not isinstance(envelope, dict):
            raise ValueError(f"cache envelope is not an object: {path}")
        meta = envelope.get("meta")
        if not isinstance(meta, dict):
            raise ValueError(f"cache envelope missing meta: {path}")
        if meta.get("schema_version") != 1:
            raise ValueError(f"unsupported cache schema_version in {path}")
        if "data" not in envelope:
            raise ValueError(f"cache envelope missing data: {path}")
        return envelope["data"]

    def _build_envelope(
        self,
        endpoint: str,
        params: dict[str, Any] | None,
        data: Any,
    ) -> dict[str, Any]:
        meta: dict[str, Any] = {
            "endpoint": endpoint,
            "params": params or {},
            "fetched_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
            "schema_version": 1,
            "fetched_by": self.fetched_by,
        }
        if self.source_patch is not None:
            meta["source_patch"] = self.source_patch
        return {"meta": meta, "data": data}

    async def _request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None,
        body: Any,
        force: bool,
    ) -> Any:
        endpoint = _endpoint_path(url)
        cache_path = self._cache_path(method, url, params, body)
        if not force and cache_path.exists():
            logger.debug(
                "Shared OpenDota cache hit method=%s endpoint=%s path=%s",
                method,
                endpoint,
                cache_path,
            )
            return self._read_envelope(cache_path)

        await self.bucket.acquire()
        logger.info(
            "OpenDota request method=%s endpoint=%s force=%s",
            method,
            endpoint,
            force,
        )
        r = await self._client.request(method, url, params=params, json=body)
        r.raise_for_status()
        payload = r.json()
        _write_json_atomic(cache_path, self._build_envelope(endpoint, params, payload))
        return payload
