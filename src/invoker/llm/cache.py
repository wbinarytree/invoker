from __future__ import annotations

import hashlib
import json
import logging
from datetime import UTC, datetime
from pathlib import Path

from invoker.llm.client import LLMClient, LLMResponse, strip_fences
from invoker.logging import get_logger, log_event


def _cache_key(model: str, prompt_version: int, prompt: str) -> str:
    blob = f"{model}:{prompt_version}:{prompt}".encode()
    return hashlib.sha256(blob).hexdigest()


def _now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


logger = get_logger(__name__)


class CachingLLMClient:
    """
    Wraps any LLMClient with an on-disk response cache.

    Cache key: sha256(model + ":" + prompt_version + ":" + rendered_prompt).
    Cache layout: <cache_dir>/<key[:2]>/<key>.json
    On hit the inner client is never called — no quota burned, no pacing wait.
    """

    def __init__(self, inner: LLMClient, cache_dir: Path) -> None:
        self._inner = inner
        self._cache_dir = cache_dir
        self.model_name = inner.model_name

    def _path(self, key: str, tag: str | None = None) -> Path:
        base = self._cache_dir / tag if tag else self._cache_dir
        return base / key[:2] / f"{key}.json"

    def _read(self, key: str, tag: str | None = None) -> LLMResponse | None:
        p = self._path(key, tag)
        if not p.exists():
            return None
        entry = json.loads(p.read_text())
        return LLMResponse(
            text=strip_fences(entry["text"]),
            model=entry["model"],
            prompt_version=entry["prompt_version"],
        )

    def _write(
        self,
        key: str,
        response: LLMResponse,
        tag: str | None = None,
        prompt: str = "",
    ) -> None:
        p = self._path(key, tag)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            json.dumps(
                {
                    "text": response.text,
                    "model": response.model,
                    "prompt_version": response.prompt_version,
                    "cached_at": _now_iso(),
                    "prompt": prompt,
                },
                indent=2,
            )
        )

    def generate_json(
        self,
        prompt: str,
        *,
        prompt_version: int,
        schema: object | None = None,
        cache_tag: str | None = None,
    ) -> LLMResponse:
        key = _cache_key(self.model_name, prompt_version, prompt)
        cached = self._read(key, cache_tag)
        if cached is not None:
            log_event(
                logger,
                logging.INFO,
                "cache_hit",
                key=key[:12],
                model=self.model_name,
                cache_tag=cache_tag,
            )
            return cached
        log_event(
            logger,
            logging.INFO,
            "request",
            key=key[:12],
            model=self.model_name,
            cache_tag=cache_tag,
        )
        response = self._inner.generate_json(
            prompt,
            prompt_version=prompt_version,
            schema=schema,
        )
        self._write(key, response, cache_tag, prompt)
        return response
