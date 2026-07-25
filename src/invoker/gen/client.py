from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Generic, TypeVar

import anthropic
from pydantic import BaseModel

GENERATION_MODEL = "claude-opus-5"

T = TypeVar("T", bound=BaseModel)


class GenerationError(RuntimeError):
    """A generation call did not produce a usable artifact. Never retried
    silently — the pipeline surfaces the failure (project hard line)."""


class GenerationProvenance(BaseModel):
    """Request-level provenance pinned to every generated artifact.

    `model` is taken from the response, not the request, so a served-by
    substitution can never go unrecorded. `request_sha256` fingerprints the
    exact prompt bytes; the generator layer adds patch + context packet
    hash + citations on top (spec: artifact shapes).
    """

    model: str
    transport: str  # "api" | "claude-cli"
    prompt_name: str
    prompt_version: str
    request_sha256: str
    input_tokens: int
    output_tokens: int
    stop_reason: str
    generated_at: str


@dataclass(frozen=True)
class GenerationResult:
    text: str
    provenance: GenerationProvenance


@dataclass(frozen=True)
class StructuredResult(Generic[T]):
    output: T
    provenance: GenerationProvenance


class GenerationClient:
    """Synchronous generation client for the batch pipeline.

    Model is fixed at construction and recorded per call. Auth resolves
    through the SDK (ANTHROPIC_API_KEY or an `ant auth login` profile);
    pass `client` explicitly only for tests.
    """

    def __init__(
        self,
        *,
        model: str = GENERATION_MODEL,
        client: anthropic.Anthropic | None = None,
    ) -> None:
        self.model = model
        self._client = client or anthropic.Anthropic()

    def generate(
        self,
        *,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
        max_tokens: int = 16000,
        effort: str | None = None,
    ) -> GenerationResult:
        """One prose-generation call. Raises GenerationError on refusal,
        truncation, or empty output."""
        kwargs = self._request_kwargs(system, user_content, max_tokens, effort)
        response = self._client.messages.create(**kwargs)
        self._check_stop(response.stop_reason, prompt_name)
        text = "".join(block.text for block in response.content if block.type == "text")
        if not text.strip():
            raise GenerationError(f"{prompt_name}: model returned no text")
        return GenerationResult(
            text=text,
            provenance=self._provenance(response, prompt_name, prompt_version, kwargs),
        )

    def generate_structured(
        self,
        output_type: type[T],
        *,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
        max_tokens: int = 16000,
        effort: str | None = None,
    ) -> StructuredResult[T]:
        """One schema-constrained call. The response is validated against
        `output_type`; validation failure raises rather than degrading."""
        kwargs = self._request_kwargs(system, user_content, max_tokens, effort)
        response = self._client.messages.parse(output_format=output_type, **kwargs)
        self._check_stop(response.stop_reason, prompt_name)
        parsed = response.parsed_output
        if parsed is None:
            raise GenerationError(
                f"{prompt_name}: response did not parse into {output_type.__name__}"
            )
        return StructuredResult(
            output=parsed,
            provenance=self._provenance(response, prompt_name, prompt_version, kwargs),
        )

    def _request_kwargs(
        self,
        system: str,
        user_content: str,
        max_tokens: int,
        effort: str | None,
    ) -> dict:
        kwargs: dict = {
            "model": self.model,
            "max_tokens": max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": user_content}],
        }
        if effort is not None:
            kwargs["output_config"] = {"effort": effort}
        return kwargs

    @staticmethod
    def _check_stop(stop_reason: str | None, prompt_name: str) -> None:
        if stop_reason == "refusal":
            raise GenerationError(f"{prompt_name}: model refused the request")
        if stop_reason == "max_tokens":
            raise GenerationError(f"{prompt_name}: output truncated at max_tokens; raise the limit")

    def _provenance(
        self,
        response: anthropic.types.Message,
        prompt_name: str,
        prompt_version: str,
        request_kwargs: dict,
    ) -> GenerationProvenance:
        fingerprint = json.dumps(
            {
                "requested_model": request_kwargs["model"],
                "system": request_kwargs["system"],
                "messages": request_kwargs["messages"],
                "prompt": f"{prompt_name}@{prompt_version}",
            },
            sort_keys=True,
        )
        return GenerationProvenance(
            model=response.model,
            transport="api",
            prompt_name=prompt_name,
            prompt_version=prompt_version,
            request_sha256=hashlib.sha256(fingerprint.encode()).hexdigest(),
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            stop_reason=str(response.stop_reason),
            generated_at=datetime.now(UTC).isoformat(),
        )
