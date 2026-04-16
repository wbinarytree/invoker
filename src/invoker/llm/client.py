from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class LLMResponse:
    text: str
    model: str
    prompt_version: int


def parse_json_response(text: str) -> Any:
    """
    Parse JSON from a model response that may include chain-of-thought reasoning.

    Tries direct parse first (fast path for models that return pure JSON).
    On failure, scans for the last outermost { or [ and parses from there —
    handles models that prefix the JSON with reasoning text.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Find the first opening brace/bracket and try from there.
    # Reasoning preamble precedes the JSON, so the first { or [ is the start.
    for char in ("{", "["):
        idx = text.find(char)
        if idx != -1:
            try:
                return json.loads(text[idx:])
            except json.JSONDecodeError:
                pass

    raise ValueError(f"No valid JSON found in response (length={len(text)})")


class LLMClient(Protocol):
    model_name: str

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        """Call the model with a prompt expected to produce JSON. Returns raw text."""
        ...


def make_client(kind: str, config: object | None = None) -> LLMClient:
    if kind == "gemini":
        from invoker.llm.gemini import GEMINI_2_5_FLASH, GeminiClient, GeminiModelConfig

        resolved = config if isinstance(config, GeminiModelConfig) else GEMINI_2_5_FLASH
        return GeminiClient(config=resolved)
    if kind == "manual":
        from invoker.llm.manual import ManualClient

        return ManualClient()
    raise ValueError(f"unknown LLM client kind: {kind}")
