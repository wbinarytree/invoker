from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import ValidationError

from invoker.benchmark.schemas import QACase
from invoker.paths import basic_qa_benchmark_dir


class BenchmarkError(RuntimeError):
    pass


def load_cases(directory: Path | None = None) -> list[QACase]:
    case_dir = directory or basic_qa_benchmark_dir()
    if not case_dir.is_dir():
        raise BenchmarkError(f"benchmark case directory not found: {case_dir}")
    paths = sorted(case_dir.glob("*.yaml"))
    if not paths:
        raise BenchmarkError(f"no benchmark cases found in {case_dir}")

    cases: list[QACase] = []
    seen_ids: set[str] = set()
    for path in paths:
        raw = yaml.safe_load(path.read_text())
        try:
            case = QACase.model_validate(raw)
        except ValidationError as exc:
            raise BenchmarkError(f"invalid benchmark case {path}: {exc}") from exc
        if case.id != path.stem:
            raise BenchmarkError(
                f"{path.name}: case id {case.id!r} must match the file name stem"
            )
        if case.id in seen_ids:
            raise BenchmarkError(f"duplicate benchmark case id: {case.id}")
        seen_ids.add(case.id)
        cases.append(case)
    return cases
