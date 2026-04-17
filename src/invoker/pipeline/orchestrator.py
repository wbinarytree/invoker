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
    BatchReasonInput,
    EdgeReasonInput,
    generate_reasons_batch,
    validate_grounding,
)
from invoker.pipeline.summarize import write_summary
from invoker.pipeline.validators import ValidationContext, validate_hero
from invoker.paths import hero_file
from invoker.pipeline.writer import read_hero, write_hero
from invoker.schemas.derived import MetaBlock, MetaHistoryEntry, PositionBlock


def _trace(msg: str) -> None:
    print(f"[pipeline] {msg}", flush=True)


@dataclass
class HeroRawBundle:
    hero_id: int
    localized_name: str
    internal_name: str
    roles: list[str]
    abilities: list[dict]
    stratz_edges: list[dict] | None
    opendota_matchups: list[dict] | None
    position_counts: dict[str, int]
    total_pro_games: int
    window_days: int
    contest_rate: float
    win_rate: float
    meta_history: list[MetaHistoryEntry]


@dataclass
class HeroResult:
    hero_id: int
    success: bool
    reasons_written: int = 0
    reasons_skipped: int = 0
    failure_reason: str | None = None


def _try_load_hero_context(
    data_dir: Path,
    patch: str,
    hero_id: int,
    hero_names: dict[int, str] | None = None,
) -> tuple[str, list[str]]:
    """
    Return (localized_name, functional_tags) for an already-written hero.
    Falls back to the roster name map (if provided) or a placeholder.
    """
    try:
        b = read_hero(data_dir, patch, hero_id)
        return b.localized_name, b.functional_tags
    except Exception:
        name = (hero_names or {}).get(hero_id, f"hero_{hero_id}")
        return name, []


def run_for_hero(
    data_dir: Path,
    patch: str,
    generator_version: str,
    bundle: HeroRawBundle,
    client: LLMClient,
    max_edges: int = 5,
    hero_names: dict[int, str] | None = None,
) -> HeroResult:
    hero_label = f"hero={bundle.hero_id} ({bundle.localized_name})"

    # --- Extraction ---
    _trace(f"extract  start   {hero_label}")
    try:
        mech = extract_mechanical(
            HeroExtractionInput(
                hero_id=bundle.hero_id,
                hero_name=bundle.localized_name,
                roles=bundle.roles,
                abilities=bundle.abilities,
            ),
            client,
        )
    except Exception as exc:
        _trace(f"extract  failed  {hero_label}  ({exc})")
        return HeroResult(hero_id=bundle.hero_id, success=False, failure_reason=str(exc))
    _trace(f"extract  done    {hero_label}  tags={mech.functional_tags}")

    # --- Stat edges ---
    synergies, counters = merge_matchups(
        bundle.stratz_edges, bundle.opendota_matchups, hero_id=bundle.hero_id
    )

    # --- Reason generation (single batch call) ---
    reasons: dict[tuple[str, int], tuple[str, dict]] = {}
    reasons_written = 0
    reasons_skipped = 0

    # Cap to top max_edges per relation (lists already sorted by |score| desc).
    candidate_syn = [e for e in synergies if e.confidence in ("med", "high")][:max_edges]
    syn_ids = {e.hero_id for e in candidate_syn}
    # Exclude heroes already in candidate_syn to avoid duplicate hero_b_ids in the batch.
    candidate_ctr = [
        e for e in counters if e.confidence in ("med", "high") and e.hero_id not in syn_ids
    ][:max_edges]
    candidates = candidate_syn + candidate_ctr

    if candidates:
        _trace(
            f"reason   batch   hero={bundle.hero_id}"
            f"  syn={len(candidate_syn)}  ctr={len(candidate_ctr)}"
        )
        edge_inputs: list[EdgeReasonInput] = []
        for e in candidates:
            relation = "synergy" if e.hero_id in syn_ids else "counter"  # syn_ids already disjoint from ctr
            hero_b_name, hero_b_tags = _try_load_hero_context(data_dir, patch, e.hero_id, hero_names)
            edge_inputs.append(
                EdgeReasonInput(
                    hero_b_id=e.hero_id,
                    hero_b_name=hero_b_name,
                    hero_b_tags=hero_b_tags,
                    relation=relation,
                    score=e.score or 0.0,
                    games=e.games,
                )
            )

        batch_inp = BatchReasonInput(
            hero_a_name=bundle.localized_name,
            hero_a_tags=mech.functional_tags,
            edges=edge_inputs,
        )
        try:
            outputs = generate_reasons_batch(batch_inp, client)
        except Exception as exc:
            _trace(f"reason   batch_failed  hero={bundle.hero_id}  ({exc})")
            outputs = []

        # Build a lookup from hero_b_id to (EdgeReasonInput, EdgeReasonOutput).
        inp_by_id = {ei.hero_b_id: ei for ei in edge_inputs}
        for out in outputs:
            ei = inp_by_id.get(out.hero_b_id)
            if ei is None:
                continue
            relation = ei.relation
            try:
                validate_grounding(out.reason, mech.functional_tags, ei.hero_b_tags)
            except Exception as exc:
                _trace(
                    f"reason   skip    {relation}  {bundle.hero_id}→{out.hero_b_id}  ({exc})"
                )
                reasons_skipped += 1
                continue
            reasons[(relation, out.hero_b_id)] = (
                out.reason,
                {"model": out.model, "prompt_version": out.prompt_version},
            )
            reasons_written += 1

        _trace(
            f"reason   done    hero={bundle.hero_id}"
            f"  written={reasons_written}  skipped={reasons_skipped}"
        )

    # --- Assemble and write ---
    hero = assemble_hero(
        hero_id=bundle.hero_id,
        localized_name=bundle.localized_name,
        internal_name=bundle.internal_name,
        source_patch=patch,
        generator_version=generator_version,
        roles=bundle.roles,
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
    )

    write_hero(data_dir, patch, hero)
    write_summary(data_dir, hero, "pro")
    _trace(f"written  {hero_label}  reasons={reasons_written}  skipped={reasons_skipped}")

    return HeroResult(
        hero_id=bundle.hero_id,
        success=True,
        reasons_written=reasons_written,
        reasons_skipped=reasons_skipped,
    )


def finalize_patch(
    data_dir: Path,
    patch: str,
    hero_ids: list[int],
    *,
    complete: bool = True,
) -> None:
    ctx = ValidationContext(roster_hero_ids=set(hero_ids), partial=not complete)
    written_ids = [hid for hid in hero_ids if hero_file(data_dir, patch, hid).exists()]
    for hid in written_ids:
        validate_hero(read_hero(data_dir, patch, hid), ctx)

    m = build_manifest(data_dir, patch, hero_ids, ["pro"], complete=complete)
    write_manifest(data_dir, m)

    g = build_graph(data_dir, patch, written_ids)
    cache_graph(data_dir, patch, g)
