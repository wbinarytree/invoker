"""Inline source-mark grammar shared by generation and benchmarking.

A mark is `[kind:KEY]` inline in generated text — the traceability unit of
the whole KB (marks-not-verdicts). Generators emit and check them;
the benchmark parses and resolves them. Resolvers live with the benchmark
(`invoker.benchmark.marks`); this module is only the grammar.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

MARK_KINDS = ("gamefile", "loc", "corpus", "changelog", "stats", "human")

MARK_PATTERN = re.compile(rf"\[({'|'.join(MARK_KINDS)}):([^\]\s]+)\]")


@dataclass(frozen=True)
class Mark:
    kind: str
    key: str

    def __str__(self) -> str:
        return f"{self.kind}:{self.key}"


def parse_marks(text: str) -> list[Mark]:
    """Distinct inline source marks, in first-use order."""
    seen: dict[Mark, None] = {}
    for match in MARK_PATTERN.finditer(text):
        seen.setdefault(Mark(kind=match.group(1), key=match.group(2)))
    return list(seen)


def strip_marks(text: str) -> str:
    return MARK_PATTERN.sub("", text)


def count_words(text: str) -> int:
    """Prose word count with mark tokens excluded — concision bounds
    target prose, and mark density must not penalize citation discipline."""
    return len(strip_marks(text).split())
