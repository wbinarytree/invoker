from __future__ import annotations

from typing import Literal, Protocol

from pydantic import BaseModel, ConfigDict

from invoker.benchmark.answerer import BenchmarkAnswer
from invoker.benchmark.marks import MarkResolver
from invoker.benchmark.report import (
    CaseResult,
    ExpectedMarkResult,
    FactResult,
    FailureCode,
    TrapResult,
)
from invoker.benchmark.schemas import QACase
from invoker.gen.client import GenerationError, GenerationProvenance
from invoker.gen.concepts import GenerationBackend
from invoker.marks import Mark, count_words

JUDGE_PROMPT_VERSION = "1"

FACT_JUDGE_SYSTEM_PROMPT = """You judge whether an answer states an expected fact.

Verdicts:
- "present": the answer states every element of the fact, in any wording.
- "contradicted": the answer asserts something incompatible with the fact \
(a different number for the same quantity is a contradiction).
- "absent": the answer neither states nor contradicts the fact. Stating \
only some elements of a multi-part fact, without contradicting any, is \
"absent".

Rules:
- Judge only against the answer text; bring no outside knowledge of the game.
- Inline marks like [corpus:...] are citations, not content; ignore them.
- rationale: one sentence naming the deciding element."""

TRAP_JUDGE_SYSTEM_PROMPT = """You judge whether an answer asserts a specific claim.

- asserted=true: the answer states or clearly implies the claim.
- asserted=false: the answer does not make the claim. Explicitly denying \
the claim is not asserting it; not mentioning it is not asserting it.

Rules:
- Judge only against the answer text; bring no outside knowledge of the game.
- Inline marks like [corpus:...] are citations, not content; ignore them.
- rationale: one sentence naming the deciding element."""


class FactVerdict(BaseModel):
    model_config = ConfigDict(extra="forbid")

    verdict: Literal["present", "absent", "contradicted"]
    rationale: str


class TrapVerdict(BaseModel):
    model_config = ConfigDict(extra="forbid")

    asserted: bool
    rationale: str


class JudgeProtocol(Protocol):
    """Judgments return their provenance alongside the verdict so the
    report records which model actually served every judge call — a
    served-by substitution must never go unrecorded."""

    def fact(self, answer_text: str, fact: str) -> tuple[FactVerdict, GenerationProvenance]: ...

    def trap(
        self, answer_text: str, assertion: str
    ) -> tuple[TrapVerdict, GenerationProvenance]: ...


class Judge:
    """One binary judgment per call. The judge sees the answer and the
    single fact or assertion — never the sources and never the other gold
    fields (cheap-verifier discipline: "does this paragraph state X" is
    the easy, checkable task)."""

    def __init__(self, backend: GenerationBackend) -> None:
        self._backend = backend

    def fact(self, answer_text: str, fact: str) -> tuple[FactVerdict, GenerationProvenance]:
        result = self._backend.generate_structured(
            FactVerdict,
            prompt_name="qa-judge-fact",
            prompt_version=JUDGE_PROMPT_VERSION,
            system=FACT_JUDGE_SYSTEM_PROMPT,
            user_content=f"Answer:\n{answer_text}\n\nExpected fact: {fact}",
        )
        return result.output, result.provenance

    def trap(self, answer_text: str, assertion: str) -> tuple[TrapVerdict, GenerationProvenance]:
        result = self._backend.generate_structured(
            TrapVerdict,
            prompt_name="qa-judge-trap",
            prompt_version=JUDGE_PROMPT_VERSION,
            system=TRAP_JUDGE_SYSTEM_PROMPT,
            user_content=f"Answer:\n{answer_text}\n\nClaim: {assertion}",
        )
        return result.output, result.provenance


def score_case(
    case: QACase,
    answer: BenchmarkAnswer,
    judge: JudgeProtocol,
    resolver: MarkResolver,
) -> CaseResult:
    """Score one answered case. Pass semantics (spec): every required fact
    present, nothing contradicted (optional facts included), no trap
    asserted, every expected mark matched by at least one resolvable mark,
    and the word bound respected."""
    if answer.text is None:
        return CaseResult(
            case_id=case.id,
            passed=False,
            failures=["resolution-miss"],
            max_answer_words=case.max_answer_words,
            answer_provenance=answer.provenance,
        )

    failures: list[FailureCode] = []
    facts, traps, judge_provenance, judge_error = _judge_answer(case, answer.text, judge)
    if judge_error is not None:
        failures.append("judge-error")
    if any(fact.required and fact.verdict == "absent" for fact in facts):
        failures.append("fact-missing")
    if any(fact.verdict == "contradicted" for fact in facts):
        failures.append("fact-contradicted")
    if any(trap.asserted for trap in traps):
        failures.append("trap-triggered")

    mark_results, mark_failures, extra_unresolvable = _check_marks(case, answer, resolver)
    failures.extend(mark_failures)

    word_count = count_words(answer.text)
    if case.max_answer_words is not None and word_count > case.max_answer_words:
        failures.append("over-length")

    failures = list(dict.fromkeys(failures))
    return CaseResult(
        case_id=case.id,
        passed=not failures,
        failures=failures,
        answer=answer.text,
        word_count=word_count,
        max_answer_words=case.max_answer_words,
        selected_artifacts=answer.selected_artifacts,
        changelog_queries=answer.changelog_queries,
        facts=facts,
        traps=traps,
        expected_marks=mark_results,
        unresolvable_extra_marks=extra_unresolvable,
        error=judge_error,
        answer_provenance=answer.provenance,
        judge_provenance=judge_provenance,
    )


def _judge_answer(
    case: QACase,
    answer_text: str,
    judge: JudgeProtocol,
) -> tuple[list[FactResult], list[TrapResult], list[GenerationProvenance], str | None]:
    """Judge every fact and trap. A judge failure stops further judging and
    is surfaced as-is — partial verdicts are kept, nothing is retried."""
    facts: list[FactResult] = []
    traps: list[TrapResult] = []
    provenance: list[GenerationProvenance] = []
    try:
        for expected in case.expected_facts:
            verdict, call_provenance = judge.fact(answer_text, expected.fact)
            provenance.append(call_provenance)
            facts.append(
                FactResult(
                    fact=expected.fact,
                    required=expected.required,
                    verdict=verdict.verdict,
                    rationale=verdict.rationale,
                )
            )
        for forbidden in case.forbidden_assertions:
            verdict, call_provenance = judge.trap(answer_text, forbidden.assertion)
            provenance.append(call_provenance)
            traps.append(
                TrapResult(
                    assertion=forbidden.assertion,
                    asserted=verdict.asserted,
                    rationale=verdict.rationale,
                )
            )
    except GenerationError as exc:
        return facts, traps, provenance, str(exc)
    return facts, traps, provenance, None


def _check_marks(
    case: QACase,
    answer: BenchmarkAnswer,
    resolver: MarkResolver,
) -> tuple[list[ExpectedMarkResult], list[FailureCode], list[str]]:
    results: list[ExpectedMarkResult] = []
    failures: list[FailureCode] = []
    resolutions = {mark: resolver.resolve(mark) for mark in answer.marks}
    matched_by_any_pattern: set[Mark] = set()
    for expected in case.expected_marks:
        candidates = [
            mark
            for mark in answer.marks
            if mark.kind == expected.kind and expected.pattern in mark.key
        ]
        matched_by_any_pattern.update(candidates)
        resolved = next((mark for mark in candidates if resolutions[mark].ok), None)
        results.append(
            ExpectedMarkResult(
                kind=expected.kind,
                pattern=expected.pattern,
                matched=[str(mark) for mark in candidates],
                resolved=str(resolved) if resolved else None,
                unresolved_reasons=[
                    f"{mark}: {resolutions[mark].reason}"
                    for mark in candidates
                    if not resolutions[mark].ok
                ],
            )
        )
        if not candidates:
            failures.append("mark-pattern-missing")
        elif resolved is None:
            failures.append("mark-unresolvable")
    extra_unresolvable = [
        f"{mark}: {resolution.reason}"
        for mark, resolution in resolutions.items()
        if not resolution.ok and mark not in matched_by_any_pattern
    ]
    return results, failures, extra_unresolvable
