from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel, ConfigDict

from invoker.corpus.sections import load_sections
from invoker.corpus.store import CorpusStore
from invoker.gen.artifacts import load_entity_article
from invoker.gen.client import GenerationError, GenerationProvenance
from invoker.gen.concepts import GenerationBackend, build_packet
from invoker.gen.items import build_item_packet
from invoker.kg.item_context import build_item_context

GUARD_PROMPT_VERSION = "1"
GUARD_SCHEMA_VERSION = 1
REPORT_FILENAME = "completeness.json"

GUARD_SYSTEM = """You audit compression completeness for a grounded encyclopedia.

You receive a source packet (sections, each headed by [key]) and an article
generated from it. The article is meant to compress the packet without losing
load-bearing content. List every load-bearing fact that is present in the
packet but absent from the article.

Load-bearing: exact values, enumerations (lists of items, abilities, talents,
sources with their numbers), interaction rules, conditions and exceptions.
Not load-bearing: prose style, ordering, phrasing, section structure,
reference/citation boilerplate, wiki housekeeping.

For each missing fact, copy the packet section key it comes from into
`section` exactly as it appears between the brackets. Judge only absence —
do not assess correctness, style, or add outside knowledge. Report nothing
when the article carries every load-bearing fact."""


class MissingFact(BaseModel):
    model_config = ConfigDict(extra="forbid")

    section: str
    fact: str


class CompletenessReport(BaseModel):
    """Flat by design: absence is a checkable claim (each flag cites a
    packet section), importance is not — the guard never ranks (spec:
    completeness gates)."""

    model_config = ConfigDict(extra="forbid")

    missing: list[MissingFact]


@dataclass(frozen=True)
class GuardResult:
    report: CompletenessReport
    provenance: GenerationProvenance


def run_guard(
    backend: GenerationBackend,
    *,
    packet: str,
    valid_sections: set[str],
    article: str,
    effort: str | None = None,
) -> GuardResult:
    """One fresh-session completeness call over (packet, article).

    Every flag must name a real packet section — concept packets render
    keys without their `corpus:` prefix, so both spellings are accepted
    and flags are normalized to the prefixed mark key. An unknown key
    means the guard's own output is unusable and raises (surfaced,
    never repaired)."""
    result = backend.generate_structured(
        CompletenessReport,
        prompt_name="completeness-guard",
        prompt_version=GUARD_PROMPT_VERSION,
        system=GUARD_SYSTEM,
        user_content=f"Packet:\n\n{packet}\n\n---\n\nArticle:\n\n{article}",
        effort=effort,
    )
    normalized: list[MissingFact] = []
    for flag in result.output.missing:
        key = _normalize_section(flag.section, valid_sections)
        if key is None:
            raise GenerationError(
                f"completeness-guard: flag cites unknown packet section "
                f"{flag.section!r}; refusing an uncheckable report"
            )
        normalized.append(MissingFact(section=key, fact=flag.fact))
    return GuardResult(
        report=CompletenessReport(missing=normalized),
        provenance=result.provenance,
    )


def _normalize_section(section: str, valid_sections: set[str]) -> str | None:
    if section in valid_sections:
        return section
    prefixed = f"corpus:{section}"
    if prefixed in valid_sections:
        return prefixed
    return None


@dataclass(frozen=True)
class GuardOutcome:
    report_path: Path
    missing_count: int
    packet_matches_artifact: bool


def guard_entity(
    artifact_path: Path,
    backend: GenerationBackend,
    *,
    store: CorpusStore | None,
    game_data_dir: Path | None,
    host_key: str = "liquipedia_dota2",
    effort: str | None = None,
) -> GuardOutcome:
    """Guard one written artifact: rebuild its packet from today's
    substrate, run the compression guard, write completeness.json.

    Works for a just-generated artifact (packet sha matches) and for
    re-guarding an old one (a drifted substrate is recorded, not
    hidden)."""
    artifact, article = load_entity_article(artifact_path)
    if artifact.kind == "concept":
        if store is None:
            raise GenerationError(f"{artifact_path}: guarding a concept needs the corpus store")
        sections = load_sections(store, host_key, artifact.slug)
        packet, text_by_mark, packet_sha256 = build_packet(sections)
    elif artifact.kind == "item":
        if game_data_dir is None:
            raise GenerationError(
                f"{artifact_path}: guarding an item needs INVOKER_GAME_DATA_DIR"
            )
        try:
            context = build_item_context(game_data_dir, artifact.slug, patch=artifact.patch)
        except (KeyError, ValueError) as exc:
            raise GenerationError(f"{artifact_path}: {exc}") from exc
        packet, text_by_mark, packet_sha256 = build_item_packet(context)
    else:
        raise GenerationError(
            f"{artifact_path}: no packet builder for kind {artifact.kind!r}"
        )
    result = run_guard(
        backend,
        packet=packet,
        valid_sections=set(text_by_mark),
        article=article,
        effort=effort,
    )
    report_path = write_report(
        artifact_path,
        result,
        packet_sha256=packet_sha256,
        packet_matches_artifact=packet_sha256 == artifact.packet_sha256,
    )
    return GuardOutcome(
        report_path=report_path,
        missing_count=len(result.report.missing),
        packet_matches_artifact=packet_sha256 == artifact.packet_sha256,
    )


def write_report(
    artifact_path: Path,
    result: GuardResult,
    *,
    packet_sha256: str,
    packet_matches_artifact: bool,
) -> Path:
    """Write completeness.json next to the artifact. `packet_sha256` is
    the packet the guard actually saw; when re-guarding an old artifact
    against drifted substrate it may differ from the artifact's recorded
    packet hash — the flag records which world the verdict is about."""
    report_path = artifact_path.parent / REPORT_FILENAME
    payload = {
        "schema_version": GUARD_SCHEMA_VERSION,
        "artifact_file": artifact_path.name,
        "packet_sha256": packet_sha256,
        "packet_matches_artifact": packet_matches_artifact,
        "missing": [flag.model_dump() for flag in result.report.missing],
        "guard_provenance": result.provenance.model_dump(),
    }
    report_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    return report_path
