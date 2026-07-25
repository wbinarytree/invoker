from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from invoker.gen.client import GenerationProvenance

RUN_REPORT_SCHEMA_VERSION = 1

FailureCode = Literal[
    "resolution-miss",
    "fact-missing",
    "fact-contradicted",
    "trap-triggered",
    "mark-pattern-missing",
    "mark-unresolvable",
    "over-length",
    "answerer-error",
    "judge-error",
]
"""Every failing check is classified so the report implicates the right
layer — the answerer, the KB content, or the case itself."""

FactVerdictLabel = Literal["present", "absent", "contradicted"]


class FactResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    fact: str
    required: bool
    verdict: FactVerdictLabel
    rationale: str


class TrapResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assertion: str
    asserted: bool
    rationale: str


class ExpectedMarkResult(BaseModel):
    """One expected-mark check: which answer marks matched the pattern,
    and whether any of them resolved against its store."""

    model_config = ConfigDict(extra="forbid")

    kind: str
    pattern: str
    matched: list[str] = Field(default_factory=list)
    resolved: str | None = None
    unresolved_reasons: list[str] = Field(default_factory=list)


class CaseResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    case_id: str
    passed: bool
    failures: list[FailureCode]
    answer: str | None = None
    word_count: int | None = None
    max_answer_words: int | None = None
    selected_artifacts: list[str] = Field(default_factory=list)
    changelog_queries: list[str] = Field(default_factory=list)
    facts: list[FactResult] = Field(default_factory=list)
    traps: list[TrapResult] = Field(default_factory=list)
    expected_marks: list[ExpectedMarkResult] = Field(default_factory=list)
    unresolvable_extra_marks: list[str] = Field(default_factory=list)
    """Answer marks outside every expected pattern that failed to resolve.
    Informational — the pass gate covers expected marks only (spec)."""
    error: str | None = None
    answer_provenance: list[GenerationProvenance] = Field(default_factory=list)
    judge_provenance: list[GenerationProvenance] = Field(default_factory=list)


class SkippedCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    case_id: str
    reason: str


class RunReport(BaseModel):
    """One benchmark run: full answers, per-fact judge verdicts with
    rationales, and enough provenance to reproduce or compare runs —
    models, prompt versions, and the exact KB state measured."""

    model_config = ConfigDict(extra="forbid")

    schema_version: int = RUN_REPORT_SCHEMA_VERSION
    run_id: str
    patch: str
    started_at: str
    finished_at: str
    kb_sha256: str
    kb_artifact_count: int
    cases_sha256: str
    """Hash of the case set as run — two reports differing here measured
    different questions, not a different KB."""
    changelog_available: bool
    answerer_model: str
    judge_model: str
    answerer_prompt_version: str
    judge_prompt_version: str
    cases: list[CaseResult]
    skipped: list[SkippedCase] = Field(default_factory=list)
