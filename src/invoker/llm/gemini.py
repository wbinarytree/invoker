from __future__ import annotations

import os
import threading
import time
from dataclasses import dataclass
from typing import Any, cast

from google import genai
from google.genai import types

from invoker.llm.client import LLMResponse, strip_fences
from invoker.logging import get_logger

logger = get_logger(__name__)


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


def _is_timeout_error(exc: Exception) -> bool:
    return "timeout" in type(exc).__name__.lower()


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
GEMMA_4_31B = GeminiModelConfig(model="gemma-4-31b-it", rpm=15, rpd=1500)


def make_model_config(model: str, rpm: int, rpd: int) -> GeminiModelConfig:
    """Build a GeminiModelConfig from env-var values."""
    return GeminiModelConfig(model=model, rpm=rpm, rpd=rpd)


def _json_config(schema: object | None) -> types.GenerateContentConfig:
    extra = cast(Any, {"response_schema": schema} if schema is not None else {})
    return types.GenerateContentConfig(
        temperature=0.0,
        response_mime_type="application/json",
        **extra,
    )


class GeminiClient:
    # Class-level pacing state shared across all instances (same process = same quota bucket).
    _rpm_lock = threading.Lock()
    _last_call_time: float = 0.0

    def __init__(self, config: GeminiModelConfig = GEMINI_2_5_FLASH) -> None:
        key = os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise RuntimeError("GOOGLE_API_KEY not set")
        self._client = genai.Client(api_key=key, http_options={"timeout": 120_000})
        self._config = config
        self.model_name = config.model

    def _pace(self) -> None:
        """Enforce the RPM ceiling proactively."""
        with GeminiClient._rpm_lock:
            now = time.monotonic()
            gap = now - GeminiClient._last_call_time
            if gap < self._config.min_interval:
                wait = self._config.min_interval - gap
                logger.debug(
                    "Pacing model=%s sleep=%.1fs rpm=%s",
                    self.model_name,
                    wait,
                    self._config.rpm,
                )
                time.sleep(wait)
            GeminiClient._last_call_time = time.monotonic()

    def generate_json(
        self,
        prompt: str,
        *,
        prompt_version: int,
        schema: object | None = None,
        cache_tag: str | None = None,
    ) -> LLMResponse:
        self._pace()
        max_retries = 3
        delay = 65.0  # start above 60 s to clear the RPM window
        for attempt in range(max_retries + 1):
            try:
                cfg = _json_config(schema)

                t0 = time.monotonic()
                logger.info(
                    "Generating JSON model=%s prompt_chars=%s attempt=%s",
                    self.model_name,
                    len(prompt),
                    attempt,
                )
                resp = self._client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                    config=cfg,
                )
                elapsed = time.monotonic() - t0
                text = strip_fences(resp.text or "")
                if text:
                    logger.info(
                        "Generated JSON model=%s elapsed=%.1fs response_chars=%s",
                        self.model_name,
                        elapsed,
                        len(text),
                    )
                else:
                    logger.warning(
                        "Empty response model=%s elapsed=%.1fs",
                        self.model_name,
                        elapsed,
                    )
                return LLMResponse(
                    text=text, model=self.model_name, prompt_version=prompt_version
                )
            except Exception as exc:
                if attempt == max_retries:
                    raise
                if _is_timeout_error(exc):
                    logger.warning(
                        "Timeout model=%s retry=%s/%s sleep=20s error=%s",
                        self.model_name,
                        attempt + 1,
                        max_retries,
                        type(exc).__name__,
                    )
                    time.sleep(20)
                elif _is_quota_error(exc):
                    logger.warning(
                        "Quota error model=%s retry=%s/%s sleep=%ss error=%s",
                        self.model_name,
                        attempt + 1,
                        max_retries,
                        round(delay),
                        exc,
                    )
                    time.sleep(delay)
                    delay *= 2
                else:
                    raise
        raise RuntimeError("unreachable")
