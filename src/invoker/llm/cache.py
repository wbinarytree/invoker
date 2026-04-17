from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

from invoker.llm.client import LLMClient, LLMResponse


def _cache_key(model: str, prompt_version: int, prompt: str) -> str:
    blob = f"{model}:{prompt_version}:{prompt}".encode()
    return hashlib.sha256(blob).hexdigest()


def _now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def _trace(msg: str) -> None:
    print(f"[llm] {msg}", flush=True)


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

    def _path(self, key: str) -> Path:
        return self._cache_dir / key[:2] / f"{key}.json"

    def _read(self, key: str) -> LLMResponse | None:
        p = self._path(key)
        if not p.exists():
            return None
        entry = json.loads(p.read_text())
        return LLMResponse(
            text=entry["text"],
            model=entry["model"],
            prompt_version=entry["prompt_version"],
        )

    def _write(self, key: str, response: LLMResponse) -> None:
        p = self._path(key)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            json.dumps(
                {
                    "text": response.text,
                    "model": response.model,
                    "prompt_version": response.prompt_version,
                    "cached_at": _now_iso(),
                },
                indent=2,
            )
        )

    def complete_json(self, prompt: str, *, prompt_version: int, schema: object | None = None) -> LLMResponse:
        key = _cache_key(self.model_name, prompt_version, prompt)
        cached = self._read(key)
        if cached is not None:
            _trace(f"cache_hit   key={key[:12]}  model={self.model_name}")
            return cached
        _trace(f"request     key={key[:12]}  model={self.model_name}")
        response = self._inner.complete_json(prompt, prompt_version=prompt_version, schema=schema)
        self._write(key, response)
        return response
