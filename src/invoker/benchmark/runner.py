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
from invoker.gen.artifacts import kb_fingerprint
from invoker.gen.client import GenerationError
from invoker.gen.concepts import GenerationBackend


def cases_fingerprint(cases: list[QACase]) -> str:
    """Content hash of the case set as run, id-sorted — lets two reports
    reveal that a case itself changed between them."""
    digest = hashlib.sha256()
    for case in sorted(cases, key=lambda c: c.id):
        digest.update(case.model_dump_json().encode())
    return digest.hexdigest()




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
    game_data_dir: Path | None = None,
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
    resolver = MarkResolver(
        corpus_store=corpus_store,
        changelog=changelog,
        game_data_dir=game_data_dir,
        patch=patch,
    )

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
    # microseconds keep two back-to-back runs from sharing a report dir
    run_id = started.strftime("%Y%m%d-%H%M%S-%f")
    report = RunReport(
        run_id=run_id,
        patch=patch,
        started_at=started.isoformat(),
        finished_at=finished.isoformat(),
        kb_sha256=kb_sha256,
        kb_artifact_count=artifact_count,
        cases_sha256=cases_fingerprint(cases),
        changelog_available=changelog is not None,
        answerer_model=answer_backend.model,
        judge_model=judge_backend.model,
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
