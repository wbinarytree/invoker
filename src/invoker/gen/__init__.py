"""Batch generation pipeline (S1-S5 of the grounded encyclopedia).

LLM calls live behind GenerationClient with provenance pinned on every
result. Nothing in this package may be imported from the bootstrap or
query path — generation is a separate, rebuildable batch stage.
"""

from invoker.gen.claude_cli import CLI_GENERATION_MODEL, ClaudeCliClient
from invoker.gen.client import (
    GENERATION_MODEL,
    GenerationClient,
    GenerationError,
    GenerationProvenance,
    GenerationResult,
    StructuredResult,
)

__all__ = [
    "CLI_GENERATION_MODEL",
    "ClaudeCliClient",
    "GENERATION_MODEL",
    "GenerationClient",
    "GenerationError",
    "GenerationProvenance",
    "GenerationResult",
    "StructuredResult",
]
