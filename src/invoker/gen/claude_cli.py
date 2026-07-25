from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections.abc import Callable
from datetime import UTC, datetime
from typing import TypeVar

from pydantic import BaseModel

from invoker.gen.client import (
    GenerationError,
    GenerationProvenance,
    GenerationResult,
    StructuredResult,
)

CLI_GENERATION_MODEL = "claude-opus-5"
_JSON_FENCE = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$")

T = TypeVar("T", bound=BaseModel)

RunCommand = Callable[[list[str], str], tuple[int, str, str]]
"""(argv, stdin) -> (returncode, stdout, stderr)."""


def _run_subprocess(argv: list[str], stdin: str) -> tuple[int, str, str]:
    completed = subprocess.run(
        argv,
        input=stdin,
        capture_output=True,
        text=True,
        timeout=900,
    )
    return completed.returncode, completed.stdout, completed.stderr


class ClaudeCliClient:
    """Generation backend over `claude -p` (subscription-billed headless runs).

    Same result/provenance surface as the API-backed GenerationClient; the
    transport differs. Tools are disabled and the system prompt fully
    replaces the harness default, so the prompt stays byte-controlled.
    Structured outputs are schema-instructed and validated client-side —
    a bad payload raises instead of degrading (project hard line).
    """

    def __init__(
        self,
        *,
        model: str = CLI_GENERATION_MODEL,
        claude_bin: str = "claude",
        run: RunCommand = _run_subprocess,
    ) -> None:
        self.model = model
        self.claude_bin = claude_bin
        self._run = run

    def generate(
        self,
        *,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
        effort: str | None = None,
    ) -> GenerationResult:
        payload = self._invoke(prompt_name, system, user_content, effort)
        text = str(payload.get("result") or "")
        if not text.strip():
            raise GenerationError(f"{prompt_name}: claude -p returned no text")
        return GenerationResult(
            text=text,
            provenance=self._provenance(payload, prompt_name, prompt_version, system, user_content),
        )

    def generate_structured(
        self,
        output_type: type[T],
        *,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
        effort: str | None = None,
    ) -> StructuredResult[T]:
        schema = json.dumps(output_type.model_json_schema(), sort_keys=True)
        structured_system = (
            f"{system}\n\nRespond with a single JSON object matching this JSON schema, "
            f"with no prose before or after it:\n{schema}"
        )
        payload = self._invoke(prompt_name, structured_system, user_content, effort)
        text = _JSON_FENCE.sub("", str(payload.get("result") or ""))
        output = output_type.model_validate_json(text)
        return StructuredResult(
            output=output,
            provenance=self._provenance(
                payload, prompt_name, prompt_version, structured_system, user_content
            ),
        )

    def _invoke(
        self,
        prompt_name: str,
        system: str,
        user_content: str,
        effort: str | None,
    ) -> dict:
        argv = [
            self.claude_bin,
            "-p",
            "--output-format",
            "json",
            "--model",
            self.model,
            "--tools",
            "",
            "--system-prompt",
            system,
        ]
        if effort is not None:
            argv += ["--effort", effort]
        returncode, stdout, stderr = self._run(argv, user_content)
        if returncode != 0:
            raise GenerationError(
                f"{prompt_name}: claude -p exited {returncode}: {stderr.strip()[:500]}"
            )
        try:
            payload = json.loads(stdout)
        except json.JSONDecodeError as exc:
            raise GenerationError(f"{prompt_name}: claude -p emitted non-JSON output") from exc
        if payload.get("is_error"):
            raise GenerationError(
                f"{prompt_name}: claude -p reported an error: {payload.get('result')}"
            )
        stop_reason = payload.get("stop_reason")
        if stop_reason == "refusal":
            raise GenerationError(f"{prompt_name}: model refused the request")
        if stop_reason == "max_tokens":
            raise GenerationError(f"{prompt_name}: output truncated at max_tokens")
        return payload

    def _provenance(
        self,
        payload: dict,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
    ) -> GenerationProvenance:
        fingerprint = json.dumps(
            {
                "requested_model": self.model,
                "system": system,
                "messages": [{"role": "user", "content": user_content}],
                "prompt": f"{prompt_name}@{prompt_version}",
            },
            sort_keys=True,
        )
        usage = payload.get("usage") or {}
        return GenerationProvenance(
            model=self._served_model(payload, prompt_name),
            transport="claude-cli",
            prompt_name=prompt_name,
            prompt_version=prompt_version,
            request_sha256=hashlib.sha256(fingerprint.encode()).hexdigest(),
            input_tokens=int(usage.get("input_tokens", 0)),
            output_tokens=int(usage.get("output_tokens", 0)),
            stop_reason=str(payload.get("stop_reason")),
            generated_at=datetime.now(UTC).isoformat(),
        )

    def _served_model(self, payload: dict, prompt_name: str) -> str:
        """The requested model's entry in modelUsage confirms what served the
        request. Background harness models (e.g. haiku) also appear there,
        so match on the requested id rather than guessing by usage."""
        model_usage = payload.get("modelUsage") or {}
        for key, value in model_usage.items():
            canonical = value.get("canonicalModel") if isinstance(value, dict) else None
            if key == self.model or canonical == self.model:
                return self.model
        raise GenerationError(
            f"{prompt_name}: requested model {self.model!r} not in modelUsage "
            f"({', '.join(model_usage) or 'empty'}); refusing to record unknown provenance"
        )
