from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class LLMResponse:
    text: str
    model: str
    prompt_version: int


class LLMClient(Protocol):
    model_name: str

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        """Call the model with a prompt expected to produce JSON. Returns raw text."""
        ...


def make_client(kind: str, model: str | None = None) -> LLMClient:
    if kind == "gemini":
        from invoker.llm.gemini import GEMINI_2_5_FLASH, GeminiClient

        return GeminiClient(config=GEMINI_2_5_FLASH)
    if kind == "manual":
        from invoker.llm.manual import ManualClient

        return ManualClient()
    raise ValueError(f"unknown LLM client kind: {kind}")
