from __future__ import annotations

import os

from invoker.llm.client import LLMResponse

try:
    import google.generativeai as genai
except ImportError as e:
    raise RuntimeError("google-generativeai not installed") from e


class GeminiClient:
    def __init__(self, model: str = "gemini-2.5-flash") -> None:
        key = os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise RuntimeError("GOOGLE_API_KEY not set")
        # google.generativeai re-exports these at runtime but omits them from __all__.
        genai.configure(api_key=key)  # pyright: ignore[reportPrivateImportUsage]
        self.model_name = model
        self._model = genai.GenerativeModel(model)  # pyright: ignore[reportPrivateImportUsage]

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        resp = self._model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.0,
                "response_mime_type": "application/json",
            },
        )
        return LLMResponse(text=resp.text, model=self.model_name, prompt_version=prompt_version)
