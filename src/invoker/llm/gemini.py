from __future__ import annotations

import os
import threading
import time
from dataclasses import dataclass

from google import genai
from google.genai import types

from invoker.llm.client import LLMResponse


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
    rpm: int   # requests per minute (free-tier ceiling)
    rpd: int   # requests per day (free-tier ceiling)
    supports_json_mode: bool = True   # response_mime_type="application/json" support
    supports_thinking_config: bool = False  # ThinkingConfig (disable chain-of-thought)

    @property
    def min_interval(self) -> float:
        """Minimum seconds between requests to stay under RPM ceiling."""
        return 60.0 / self.rpm + 0.5  # small buffer above the hard limit


GEMINI_2_5_FLASH = GeminiModelConfig(model="gemini-2.5-flash", rpm=5, rpd=20)
GEMMA_4_31B = GeminiModelConfig(
    model="gemma-4-31b-it",
    rpm=5,
    rpd=100,
    supports_json_mode=False,
    supports_thinking_config=False,  # ThinkingConfig not supported via Google AI API
)

# Known-model registry: looked up by model name in make_model_config().
_KNOWN: dict[str, GeminiModelConfig] = {
    GEMINI_2_5_FLASH.model: GEMINI_2_5_FLASH,
    GEMMA_4_31B.model: GEMMA_4_31B,
}


def make_model_config(model: str, rpm: int, rpd: int) -> GeminiModelConfig:
    """
    Build a GeminiModelConfig from env-var values.
    For known models the capability flags (json_mode, thinking_config) are
    inherited from the registry; unknown models get safe defaults.
    """
    known = _KNOWN.get(model)
    return GeminiModelConfig(
        model=model,
        rpm=rpm,
        rpd=rpd,
        supports_json_mode=known.supports_json_mode if known else True,
        supports_thinking_config=known.supports_thinking_config if known else False,
    )


class GeminiClient:
    # Class-level pacing state shared across all instances (same process = same quota bucket).
    _rpm_lock = threading.Lock()
    _last_call_time: float = 0.0

    def __init__(self, config: GeminiModelConfig = GEMINI_2_5_FLASH) -> None:
        key = os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise RuntimeError("GOOGLE_API_KEY not set")
        self._client = genai.Client(api_key=key)
        self._config = config
        self.model_name = config.model

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
                cfg = types.GenerateContentConfig(temperature=0.0)
                if self._config.supports_json_mode:
                    cfg = types.GenerateContentConfig(
                        temperature=0.0,
                        response_mime_type="application/json",
                    )
                if self._config.supports_thinking_config:
                    cfg = types.GenerateContentConfig(
                        temperature=0.0,
                        thinking_config=types.ThinkingConfig(thinking_budget=0),
                    )

                t0 = time.monotonic()
                _trace(
                    f"generate     model={self.model_name}"
                    f"  prompt_chars={len(prompt)}"
                    + (f"  attempt={attempt}" if attempt else "")
                )
                resp = self._client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                    config=cfg,
                )
                elapsed = time.monotonic() - t0
                text = resp.text or ""
                if not text:
                    # Output text is empty — collect thinking parts as fallback.
                    # Thinking models sometimes put all content in thought=True parts.
                    # Using the thinking text: (a) gets cached so the call isn't repeated,
                    # (b) lets parse_json_response find JSON if the model reasoned to one.
                    try:
                        candidate = resp.candidates[0] if resp.candidates else None
                        parts = candidate.content.parts if candidate else []
                        thinking_parts = [
                            getattr(p, "text", "") or ""
                            for p in parts
                            if getattr(p, "thought", False)
                        ]
                        text = "\n".join(thinking_parts)
                        _trace(
                            f"generate_ok  model={self.model_name}"
                            f"  elapsed={elapsed:.1f}s  response_chars=0"
                            f"  thinking_chars={len(text)}"
                            f"  (using thinking fallback)"
                        )
                    except Exception as diag_exc:
                        _trace(f"thinking_fallback_failed  ({diag_exc})")
                else:
                    _trace(
                        f"generate_ok  model={self.model_name}"
                        f"  elapsed={elapsed:.1f}s  response_chars={len(text)}"
                    )
                if not text:
                    raise RuntimeError(
                        f"Empty response from {self.model_name} after {elapsed:.1f}s"
                    )
                return LLMResponse(
                    text=text, model=self.model_name, prompt_version=prompt_version
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
        raise RuntimeError("unreachable")
