from __future__ import annotations

import hashlib
from pathlib import Path

from invoker.llm.client import LLMResponse


class ManualClient:
    """
    File-based LLM loop for rate-limit emergencies and spot-checks.

    Writes each prompt to data/raw/manual_prompts/<hash>.md.
    Reads the response from data/raw/manual_responses/<hash>.txt.
    Raises if response is missing so you know to go paste it into ChatGPT/Claude.ai.
    """

    model_name = "manual"

    def __init__(self, inbox: Path | None = None, outbox: Path | None = None) -> None:
        self.inbox = inbox or Path("data/raw/manual_prompts")
        self.outbox = outbox or Path("data/raw/manual_responses")
        self.inbox.mkdir(parents=True, exist_ok=True)
        self.outbox.mkdir(parents=True, exist_ok=True)

    def complete_json(self, prompt: str, *, prompt_version: int, schema: object | None = None, cache_tag: str | None = None) -> LLMResponse:
        h = hashlib.sha256(prompt.encode()).hexdigest()[:12]
        prompt_path = self.inbox / f"{h}.md"
        response_path = self.outbox / f"{h}.txt"
        if not prompt_path.exists():
            prompt_path.write_text(prompt)
        if not response_path.exists():
            raise FileNotFoundError(
                f"Manual response missing. Paste the JSON output for:\n  {prompt_path}\n"
                f"into:\n  {response_path}"
            )
        return LLMResponse(
            text=response_path.read_text(),
            model="manual",
            prompt_version=prompt_version,
        )
