from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


def strip_fences(text: str) -> str:
    """Remove markdown code fences that some models wrap around JSON output."""
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped[stripped.find("\n") + 1:]
    if stripped.endswith("```"):
        stripped = stripped[: stripped.rfind("```")].rstrip()
    return stripped


@dataclass(frozen=True)
class LLMResponse:
    text: str
    model: str
    prompt_version: int


class LLMClient(Protocol):
    model_name: str

    def complete_json(
        self,
        prompt: str,
        *,
        prompt_version: int,
        schema: Any | None = None,
        cache_tag: str | None = None,
    ) -> LLMResponse:
        """
        Call the model with a prompt expected to produce JSON.

        schema: a Pydantic BaseModel class (or generic alias like list[MyModel]).
        When provided and the underlying client supports it, the API enforces
        the schema so the response is always valid JSON matching that shape.
        """
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
