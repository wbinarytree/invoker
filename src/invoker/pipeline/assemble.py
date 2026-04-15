from __future__ import annotations

from datetime import UTC, datetime

from invoker.pipeline.derive import StatisticalEdge
from invoker.pipeline.extract import MechanicalExtraction
from invoker.schemas.derived import (
    HeroDerived,
    MetaBlock,
    MetaHistoryEntry,
    PositionBlock,
    Provenance,
    StatEdge,
    TagSource,
)


def _stat_to_edge(e: StatisticalEdge, reason: str | None, reason_prov: dict | None) -> StatEdge:
    return StatEdge(
        hero_id=e.hero_id,
        score=e.score,
        games=e.games,
        confidence=e.confidence,
        source=e.source,
        reason=reason,
        reason_provenance=reason_prov,
    )


def assemble_hero(
    *,
    hero_id: int,
    localized_name: str,
    internal_name: str,
    source_patch: str,
    generator_version: str,
    liquipedia_roles: list[str],
    mechanical: MechanicalExtraction,
    positions_pro: PositionBlock,
    synergies_pro: list[StatisticalEdge],
    counters_pro: list[StatisticalEdge],
    reasons_by_edge: dict[tuple[str, int], tuple[str, dict]],
    meta_pro: MetaBlock,
    meta_history: list[MetaHistoryEntry],
    statistical_provenance: dict,
    liquipedia_snapshot: str,
) -> HeroDerived:
    def wrap(edges: list[StatisticalEdge], relation: str) -> list[StatEdge]:
        out: list[StatEdge] = []
        for e in edges:
            reason_tuple = reasons_by_edge.get((relation, e.hero_id))
            reason, prov = reason_tuple if reason_tuple else (None, None)
            out.append(_stat_to_edge(e, reason, prov))
        return out

    return HeroDerived(
        schema_version=1,
        generator_version=generator_version,
        source_patch=source_patch,
        generated_at=datetime.now(UTC).isoformat(timespec="seconds"),
        hero_id=hero_id,
        localized_name=localized_name,
        internal_name=internal_name,
        liquipedia_roles=liquipedia_roles,
        functional_tags=mechanical.functional_tags,
        tag_sources=[TagSource(**s.__dict__) for s in mechanical.tag_sources],
        positions={"pro": positions_pro},
        synergies={"pro": wrap(synergies_pro, "synergy")},
        counters={"pro": wrap(counters_pro, "counter")},
        meta={"pro": meta_pro},
        meta_history=meta_history,
        provenance=Provenance(
            mechanical={
                "model": mechanical.model,
                "prompt_version": mechanical.prompt_version,
                "prompt_hash": mechanical.prompt_hash,
                "input_hash": mechanical.input_hash,
                "extracted_at": mechanical.extracted_at,
                "liquipedia_snapshot": liquipedia_snapshot,
            },
            statistical={"pro": statistical_provenance},
        ),
    )
