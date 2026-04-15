from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from invoker.graph import build_graph, cache_graph
from invoker.llm import LLMClient
from invoker.pipeline.assemble import assemble_hero
from invoker.pipeline.derive import merge_matchups, meta_tier, position_weights
from invoker.pipeline.extract import HeroExtractionInput, extract_mechanical
from invoker.pipeline.manifest import build_manifest, write_manifest
from invoker.pipeline.reason import (
    ReasonInput,
    generate_counter_reason,
    generate_synergy_reason,
    validate_grounding,
)
from invoker.pipeline.summarize import write_summary
from invoker.pipeline.validators import ValidationContext, validate_hero
from invoker.pipeline.writer import write_hero
from invoker.schemas.derived import MetaBlock, MetaHistoryEntry, PositionBlock


@dataclass
class HeroRawBundle:
    hero_id: int
    localized_name: str
    internal_name: str
    liquipedia_roles: list[str]
    abilities: list[dict]
    stratz_edges: list[dict] | None
    opendota_matchups: list[dict] | None
    position_counts: dict[str, int]
    total_pro_games: int
    window_days: int
    contest_rate: float
    win_rate: float
    meta_history: list[MetaHistoryEntry]
    liquipedia_snapshot: str


def run_for_hero(
    data_dir: Path,
    patch: str,
    generator_version: str,
    bundle: HeroRawBundle,
    client: LLMClient,
) -> None:
    mech = extract_mechanical(
        HeroExtractionInput(
            hero_id=bundle.hero_id,
            hero_name=bundle.localized_name,
            liquipedia_roles=bundle.liquipedia_roles,
            abilities=bundle.abilities,
        ),
        client,
    )

    synergies, counters = merge_matchups(
        bundle.stratz_edges, bundle.opendota_matchups, hero_id=bundle.hero_id
    )

    reasons: dict[tuple[str, int], tuple[str, dict]] = {}
    syn_ids = {e.hero_id for e in synergies}
    for e in synergies + counters:
        if e.confidence not in ("med", "high"):
            continue
        relation = "synergy" if e.hero_id in syn_ids else "counter"
        inp = ReasonInput(
            hero_a_id=bundle.hero_id,
            hero_a_name=bundle.localized_name,
            hero_a_tags=mech.functional_tags,
            hero_b_id=e.hero_id,
            hero_b_name=f"hero_{e.hero_id}",
            hero_b_tags=[],
            score=e.score or 0.0,
            games=e.games,
        )
        gen = generate_synergy_reason if relation == "synergy" else generate_counter_reason
        out = gen(inp, client)
        try:
            validate_grounding(out.reason, mech.functional_tags, [])
        except Exception:
            continue
        reasons[(relation, e.hero_id)] = (
            out.reason,
            {"model": out.model, "prompt_version": out.prompt_version},
        )

    hero = assemble_hero(
        hero_id=bundle.hero_id,
        localized_name=bundle.localized_name,
        internal_name=bundle.internal_name,
        source_patch=patch,
        generator_version=generator_version,
        liquipedia_roles=bundle.liquipedia_roles,
        mechanical=mech,
        positions_pro=PositionBlock(
            weights=position_weights(bundle.position_counts),
            games=bundle.total_pro_games,
            window_days=bundle.window_days,
        ),
        synergies_pro=synergies,
        counters_pro=counters,
        reasons_by_edge=reasons,
        meta_pro=MetaBlock(
            contest_rate=bundle.contest_rate,
            win_rate=bundle.win_rate,
            tier=meta_tier(bundle.contest_rate, bundle.win_rate),
            games=bundle.total_pro_games,
        ),
        meta_history=bundle.meta_history,
        statistical_provenance={"window_days": bundle.window_days},
        liquipedia_snapshot=bundle.liquipedia_snapshot,
    )

    write_hero(data_dir, patch, hero)
    write_summary(data_dir, hero, "pro")


def finalize_patch(
    data_dir: Path,
    patch: str,
    hero_ids: list[int],
    *,
    complete: bool = True,
) -> None:
    from invoker.paths import hero_file
    from invoker.pipeline.writer import read_hero

    ctx = ValidationContext(roster_hero_ids=set(hero_ids))
    written_ids = [hid for hid in hero_ids if hero_file(data_dir, patch, hid).exists()]
    for hid in written_ids:
        validate_hero(read_hero(data_dir, patch, hid), ctx)

    m = build_manifest(data_dir, patch, hero_ids, ["pro"], complete=complete)
    write_manifest(data_dir, m)

    g = build_graph(data_dir, patch, written_ids)
    cache_graph(data_dir, patch, g)
