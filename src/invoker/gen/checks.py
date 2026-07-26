"""Mechanical faithfulness checks over the general ``[kind:KEY]`` mark
grammar (``invoker.marks``), shared by every generator (concepts, items):
marks must resolve against the context packet's keyed sections, every
packet section must be cited by the article (lossless compression —
boilerplate anchors exempt), and every number must appear in the text of
the section(s) it cites. Checking is against the packet only — never
live sources.
"""

from __future__ import annotations

import re

from invoker.gen.client import GenerationError
from invoker.marks import MARK_PATTERN, Mark, strip_marks

NUMBER_PATTERN = re.compile(r"\d+(?:\.\d+)?")

COVERAGE_ALLOWLIST = frozenset({"References"})
"""Section anchors exempt from coverage: wiki reference/footnote lists
carry no load-bearing facts (spec: generation completeness gates)."""


def extract_marks(text: str) -> list[str]:
    """Distinct ``kind:key`` mark strings, in first-use order."""
    seen: dict[str, None] = {}
    for match in MARK_PATTERN.finditer(text):
        seen.setdefault(str(Mark(kind=match.group(1), key=match.group(2))))
    return list(seen)


def check_marks(used: list[str], valid: set[str], what: str, slug: str) -> None:
    unknown = [mark for mark in used if mark not in valid]
    if unknown:
        raise GenerationError(
            f"{slug}: {what} cites marks not in the context packet: {', '.join(sorted(unknown))}"
        )
    if not used:
        raise GenerationError(f"{slug}: {what} contains no citation marks")


def check_coverage(cited: list[str], valid: set[str], what: str, slug: str) -> None:
    """Every packet section must be cited — the article is a lossless
    compression, so an uncited section is dropped content. Anchors in
    ``COVERAGE_ALLOWLIST`` are boilerplate and exempt."""
    cited_set = set(cited)
    missing = sorted(
        mark
        for mark in valid
        if mark not in cited_set and mark.partition("#")[2] not in COVERAGE_ALLOWLIST
    )
    if missing:
        raise GenerationError(
            f"{slug}: {what} does not cite packet sections: {', '.join(missing)}"
        )


def article_segments(text: str) -> list[tuple[str, list[str]]]:
    """Split text at citation marks: the text preceding a run of
    consecutive marks is attributed to those marks' sections. An uncited
    tail (if any) carries an empty mark list."""
    segments: list[tuple[str, list[str]]] = []
    matches = list(MARK_PATTERN.finditer(text))
    position = 0
    index = 0
    while index < len(matches):
        match = matches[index]
        marks = [f"{match.group(1)}:{match.group(2)}"]
        end = match.end()
        follower = index + 1
        while follower < len(matches) and not text[end : matches[follower].start()].strip():
            marks.append(f"{matches[follower].group(1)}:{matches[follower].group(2)}")
            end = matches[follower].end()
            follower += 1
        segments.append((text[position : match.start()], marks))
        position = end
        index = follower
    tail = text[position:]
    if tail.strip():
        segments.append((tail, []))
    return segments


def check_numbers(text: str, source_text: str, what: str, slug: str) -> None:
    """Every number in generated text must literally appear in the cited
    source. Marks are stripped first — keys carry digits of their own."""
    stripped = strip_marks(text)
    missing = sorted(
        number for number in set(NUMBER_PATTERN.findall(stripped)) if number not in source_text
    )
    if missing:
        raise GenerationError(
            f"{slug}: {what} contains numbers not found in the cited source: {', '.join(missing)}"
        )


def check_article_numbers(text: str, text_by_mark: dict[str, str], slug: str) -> None:
    """Numbers in each cited segment must appear in that segment's own
    cited sections; uncited text is checked against all sections."""
    all_sections = "\n".join(text_by_mark.values())
    for segment_text, marks in article_segments(text):
        if marks:
            source = "\n".join(text_by_mark.get(mark, "") for mark in marks)
            what = f"article segment citing {', '.join(marks)}"
        else:
            source = all_sections
            what = "uncited article text"
        check_numbers(segment_text, source, what, slug)
