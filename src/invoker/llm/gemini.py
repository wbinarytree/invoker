from __future__ import annotations

import os
import threading
import time
from dataclasses import dataclass

from invoker.llm.client import LLMResponse

try:
    import google.generativeai as genai
except ImportError as e:
    raise RuntimeError("google-generativeai not installed") from e


def _trace(msg: str) -> None:
    print(f"[llm] {msg}", flush=True)


def _is_quota_error(exc: Exception) -> bool:
    name = type(exc).__name__
    msg = str(exc).lower()
    return (
        "resourceexhausted" in name
        or "quota" in msg
        or "429" in msg
        or "rate_limit" in msg
        or "ratelimit" in msg
    )


@dataclass(frozen=True)
class GeminiModelConfig:
    model: str
    rpm: int  # requests per minute (free-tier ceiling)
    rpd: int  # requests per day (free-tier ceiling)

    @property
    def min_interval(self) -> float:
        """Minimum seconds between requests to stay under RPM ceiling."""
        return 60.0 / self.rpm + 0.5  # small buffer above the hard limit


GEMINI_2_5_FLASH = GeminiModelConfig(model="gemini-2.5-flash", rpm=5, rpd=20)
GEMMA_4_31B = GeminiModelConfig(model="gemma-4-31b-it", rpm=5, rpd=100)


class GeminiClient:
    # Class-level pacing state shared across all instances (same process = same quota bucket).
    _rpm_lock = threading.Lock()
    _last_call_time: float = 0.0

    def __init__(self, config: GeminiModelConfig = GEMINI_2_5_FLASH) -> None:
        key = os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise RuntimeError("GOOGLE_API_KEY not set")
        genai.configure(api_key=key)  # pyright: ignore[reportPrivateImportUsage]
        self._config = config
        self.model_name = config.model
        self._model = genai.GenerativeModel(config.model)  # pyright: ignore[reportPrivateImportUsage]

    def _pace(self) -> None:
        """Enforce the RPM ceiling proactively."""
        with GeminiClient._rpm_lock:
            now = time.monotonic()
            gap = now - GeminiClient._last_call_time
            if gap < self._config.min_interval:
                wait = self._config.min_interval - gap
                _trace(f"pacing  sleep={wait:.1f}s  ({self._config.rpm} RPM ceiling)")
                time.sleep(wait)
            GeminiClient._last_call_time = time.monotonic()

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        self._pace()
        max_retries = 3
        delay = 65.0  # start above 60 s to clear the RPM window
        for attempt in range(max_retries + 1):
            try:
                resp = self._model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.0,
                        "response_mime_type": "application/json",
                    },
                )
                return LLMResponse(
                    text=resp.text, model=self.model_name, prompt_version=prompt_version
                )
            except Exception as exc:
                if attempt == max_retries:
                    raise
                if _is_quota_error(exc):
                    _trace(
                        f"quota_error  retry={attempt + 1}/{max_retries}"
                        f"  sleep={delay:.0f}s  ({exc})"
                    )
                    time.sleep(delay)
                    delay *= 2
                else:
                    raise
        raise RuntimeError("unreachable")  # loop always raises or returns
