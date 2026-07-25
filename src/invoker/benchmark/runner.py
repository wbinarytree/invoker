from __future__ import annotations

import hashlib
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from invoker.benchmark.answerer import ANSWERER_PROMPT_VERSION, Answerer, load_kb_entries
from invoker.benchmark.marks import MarkResolver
from invoker.benchmark.report import CaseResult, RunReport, SkippedCase
from invoker.benchmark.schemas import QACase
from invoker.benchmark.scorer import JUDGE_PROMPT_VERSION, Judge, score_case
from invoker.corpus.store import CorpusStore
from invoker.gen.client import GenerationError
from invoker.gen.concepts import GenerationBackend


def kb_fingerprint(kb_dir: Path) -> tuple[str, int]:
    """Content hash over every file in the KB archive plus the artifact
    count — the run report's record of exactly which KB state was measured."""
    digest = hashlib.sha256()
    count = 0
    if kb_dir.is_dir():
        for path in sorted(kb_dir.rglob("*")):
            if path.is_file():
                digest.update(str(path.relative_to(kb_dir)).encode())
                digest.update(path.read_bytes())
                if path.name == "artifact.json":
                    count += 1
    return digest.hexdigest(), count


def run_benchmark(
    *,
    cases: list[QACase],
    patch: str,
    kb_dir: Path,
    corpus_store: CorpusStore | None,
    changelog: dict[str, Any] | None,
    answer_backend: GenerationBackend,
    judge_backend: GenerationBackend,
    out_dir: Path,
    on_result: Callable[[CaseResult], None] | None = None,
) -> tuple[RunReport, Path]:
    """Answer and score every case targeting `patch`; cases pinned to other
    patches are recorded as skipped. An answerer failure fails that case
    (`answerer-error`) and the run moves on — one broken case never hides
    the others' results. Writes the report under `out_dir/<run_id>/`."""
    started = datetime.now(UTC)
    entries = load_kb_entries(kb_dir)
    kb_sha256, artifact_count = kb_fingerprint(kb_dir)
    answerer = Answerer(answer_backend, entries, changelog)
    judge = Judge(judge_backend)
    resolver = MarkResolver(corpus_store=corpus_store, changelog=changelog)

    results: list[CaseResult] = []
    skipped: list[SkippedCase] = []
    for case in cases:
        if case.patch != patch:
            skipped.append(
                SkippedCase(
                    case_id=case.id,
                    reason=f"case targets patch {case.patch}, run is {patch}",
                )
            )
            continue
        try:
            answer = answerer.answer(case.question)
        except GenerationError as exc:
            result = CaseResult(
                case_id=case.id,
                passed=False,
                failures=["answerer-error"],
                max_answer_words=case.max_answer_words,
                error=str(exc),
            )
        else:
            result = score_case(case, answer, judge, resolver)
        results.append(result)
        if on_result is not None:
            on_result(result)

    finished = datetime.now(UTC)
    run_id = started.strftime("%Y%m%d-%H%M%S")
    report = RunReport(
        run_id=run_id,
        patch=patch,
        started_at=started.isoformat(),
        finished_at=finished.isoformat(),
        kb_sha256=kb_sha256,
        kb_artifact_count=artifact_count,
        changelog_available=changelog is not None,
        answerer_model=getattr(answer_backend, "model", "unknown"),
        judge_model=getattr(judge_backend, "model", "unknown"),
        answerer_prompt_version=ANSWERER_PROMPT_VERSION,
        judge_prompt_version=JUDGE_PROMPT_VERSION,
        cases=results,
        skipped=skipped,
    )
    report_dir = out_dir / run_id
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "report.json"
    report_path.write_text(report.model_dump_json(indent=2))
    return report, report_path
