from __future__ import annotations

import hashlib
from pathlib import Path

from invoker.llm.client import LLMResponse


class PendingManualResponseError(LookupError):
    """
    Raised when a manual prompt has been written but no response file exists yet.

    Carries the concrete paths so the CLI can print paste instructions instead of
    a stack trace.
    """

    def __init__(self, prompt_path: Path, response_path: Path, cache_tag: str | None) -> None:
        self.prompt_path = prompt_path
        self.response_path = response_path
        self.cache_tag = cache_tag
        super().__init__(
            f"Manual response missing for {cache_tag or 'unknown stage'}. "
            f"Paste the JSON output for {prompt_path} into {response_path}."
        )


class ManualClient:
    """
    File-based LLM loop for rate-limit emergencies and spot-checks.

    Writes each prompt to data/raw/manual_prompts/<tag>/<hash>.md (tag from the
    caller's cache_tag, e.g. "extract/Slardar"). Reads the response from
    data/raw/manual_responses/<tag>/<hash>.txt. Raises PendingManualResponseError
    when the response file is missing.
    """

    model_name = "manual"

    def __init__(self, inbox: Path | None = None, outbox: Path | None = None) -> None:
        self.inbox = inbox or Path("data/raw/manual_prompts")
        self.outbox = outbox or Path("data/raw/manual_responses")
        self.inbox.mkdir(parents=True, exist_ok=True)
        self.outbox.mkdir(parents=True, exist_ok=True)

    def _paths(self, prompt: str, cache_tag: str | None) -> tuple[Path, Path]:
        h = hashlib.sha256(prompt.encode()).hexdigest()[:12]
        in_dir = self.inbox / cache_tag if cache_tag else self.inbox
        out_dir = self.outbox / cache_tag if cache_tag else self.outbox
        return in_dir / f"{h}.md", out_dir / f"{h}.txt"

    def generate_json(
        self,
        prompt: str,
        *,
        prompt_version: int,
        schema: object | None = None,
        cache_tag: str | None = None,
    ) -> LLMResponse:
        prompt_path, response_path = self._paths(prompt, cache_tag)
        if not prompt_path.exists():
            prompt_path.parent.mkdir(parents=True, exist_ok=True)
            header = f"<!-- cache_tag: {cache_tag or ''} prompt_version: {prompt_version} -->\n"
            prompt_path.write_text(header + prompt)
        if not response_path.exists():
            response_path.parent.mkdir(parents=True, exist_ok=True)
            raise PendingManualResponseError(prompt_path, response_path, cache_tag)
        return LLMResponse(
            text=response_path.read_text(),
            model="manual",
            prompt_version=prompt_version,
        )
