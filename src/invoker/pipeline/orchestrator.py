from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from invoker.graph import build_graph, cache_graph
from invoker.llm import LLMClient, PendingManualResponseError
from invoker.logging import get_logger
from invoker.paths import hero_file
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
from invoker.pipeline.writer import read_hero, write_hero
from invoker.schemas.derived import (
    HeroDerived,
    MetaBlock,
    MetaHistoryEntry,
    PositionBlock,
    StatEdge,
)

logger = get_logger(__name__)


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
    pending_manual_paths: list[Path] | None = None


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


def extract_hero(
    data_dir: Path,
    patch: str,
    generator_version: str,
    bundle: HeroRawBundle,
    client: LLMClient,
) -> HeroResult:
    """
    Pass 1: extract mechanical tags, compute statistical edges, write the hero
    file with no reasons. Idempotent when the LLM client is cache-hot.
    """
    logger.info(
        "Extract start hero_id=%s hero_name=%s",
        bundle.hero_id,
        bundle.localized_name,
    )
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
    except PendingManualResponseError as exc:
        logger.info(
            "Extract pending manual response hero_id=%s hero_name=%s prompt=%s",
            bundle.hero_id,
            bundle.localized_name,
            exc.prompt_path,
        )
        return HeroResult(
            hero_id=bundle.hero_id,
            success=False,
            failure_reason="pending_manual",
            pending_manual_paths=[exc.prompt_path],
        )
    except Exception as exc:
        logger.exception(
            "Extract failed hero_id=%s hero_name=%s",
            bundle.hero_id,
            bundle.localized_name,
        )
        return HeroResult(hero_id=bundle.hero_id, success=False, failure_reason=str(exc))
    logger.info(
        "Extract done hero_id=%s hero_name=%s tags=%s",
        bundle.hero_id,
        bundle.localized_name,
        mech.functional_tags,
    )

    synergies, counters = merge_matchups(
        bundle.stratz_edges, bundle.opendota_matchups, hero_id=bundle.hero_id
    )

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
        reasons_by_edge={},
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
    logger.info(
        "Hero written (extract pass) hero_id=%s hero_name=%s",
        bundle.hero_id,
        bundle.localized_name,
    )

    return HeroResult(hero_id=bundle.hero_id, success=True)


def _select_reason_candidates(hero: HeroDerived, max_edges: int) -> list[tuple[StatEdge, str]]:
    """
    Candidates come from the written hero's synergies/counters, already sorted
    by |score| desc, filtered to med/high confidence, capped at max_edges per
    relation. Counter list excludes heroes already chosen as synergies so the
    batch never contains duplicate hero_b_ids.
    """
    syn = [e for e in hero.synergies.get("pro", []) if e.confidence in ("med", "high")][:max_edges]
    syn_ids = {e.hero_id for e in syn}
    ctr = [
        e
        for e in hero.counters.get("pro", [])
        if e.confidence in ("med", "high") and e.hero_id not in syn_ids
    ][:max_edges]
    return [(e, "synergy") for e in syn] + [(e, "counter") for e in ctr]


def _apply_reasons(
    hero: HeroDerived,
    reasons: dict[tuple[str, int], tuple[str, dict]],
) -> HeroDerived:
    """Return a new HeroDerived with reasons merged into synergies/counters."""

    def merge(edges: list[StatEdge], relation: str) -> list[StatEdge]:
        out: list[StatEdge] = []
        for e in edges:
            pair = reasons.get((relation, e.hero_id))
            if pair is None:
                out.append(e)
                continue
            reason, prov = pair
            out.append(e.model_copy(update={"reason": reason, "reason_provenance": prov}))
        return out

    synergies = {b: merge(v, "synergy") for b, v in hero.synergies.items()}
    counters = {b: merge(v, "counter") for b, v in hero.counters.items()}
    return hero.model_copy(update={"synergies": synergies, "counters": counters})


def reason_hero(
    data_dir: Path,
    patch: str,
    hero_id: int,
    client: LLMClient,
    *,
    max_edges: int = 5,
    hero_names: dict[int, str] | None = None,
) -> HeroResult:
    """
    Pass 2: read the written hero, run the reason batch against the current
    pool of hero facts on disk, and rewrite the hero with reasons attached.

    Skips the batch cleanly when no candidate has hero_b tags (`tagged == 0`)
    so hero B pools that have not been extracted yet do not waste quota.
    """
    try:
        hero = read_hero(data_dir, patch, hero_id)
    except FileNotFoundError:
        return HeroResult(
            hero_id=hero_id,
            success=False,
            failure_reason="hero_file_missing",
        )

    pairs = _select_reason_candidates(hero, max_edges=max_edges)
    if not pairs:
        logger.info(
            "Reason batch skipped hero_id=%s (no med/high candidates)",
            hero_id,
        )
        return HeroResult(hero_id=hero_id, success=True)

    edge_inputs: list[EdgeReasonInput] = []
    for edge, relation in pairs:
        hero_b_name, hero_b_tags = _try_load_hero_context(data_dir, patch, edge.hero_id, hero_names)
        edge_inputs.append(
            EdgeReasonInput(
                hero_b_id=edge.hero_id,
                hero_b_name=hero_b_name,
                hero_b_tags=hero_b_tags,
                relation=relation,
                score=edge.score or 0.0,
                games=edge.games,
            )
        )

    tagged = sum(1 for ei in edge_inputs if ei.hero_b_tags)
    if tagged == 0:
        logger.info(
            "Reason batch skipped hero_id=%s (0/%d hero_b have tags)",
            hero_id,
            len(edge_inputs),
        )
        return HeroResult(hero_id=hero_id, success=True)

    logger.info(
        "Reason batch start hero_id=%s synergies=%s counters=%s tagged=%d/%d",
        hero_id,
        sum(1 for _, r in pairs if r == "synergy"),
        sum(1 for _, r in pairs if r == "counter"),
        tagged,
        len(edge_inputs),
    )

    batch_inp = BatchReasonInput(
        hero_a_name=hero.localized_name,
        hero_a_tags=hero.functional_tags,
        edges=edge_inputs,
    )
    pending_reason_prompt: Path | None = None
    try:
        outputs = generate_reasons_batch(batch_inp, client)
    except PendingManualResponseError as exc:
        logger.info(
            "Reason batch pending manual response hero_id=%s prompt=%s",
            hero_id,
            exc.prompt_path,
        )
        pending_reason_prompt = exc.prompt_path
        outputs = []
    except Exception:
        logger.exception("Reason batch failed hero_id=%s", hero_id)
        outputs = []

    reasons: dict[tuple[str, int], tuple[str, dict]] = {}
    reasons_written = 0
    reasons_skipped = 0
    inp_by_id = {ei.hero_b_id: ei for ei in edge_inputs}
    for out in outputs:
        ei = inp_by_id.get(out.hero_b_id)
        if ei is None:
            continue
        try:
            validate_grounding(out.reason, hero.functional_tags, ei.hero_b_tags)
        except Exception as exc:
            logger.warning(
                "Reason skipped relation=%s hero_id=%s other_hero_id=%s error=%s",
                ei.relation,
                hero_id,
                out.hero_b_id,
                exc,
            )
            reasons_skipped += 1
            continue
        reasons[(ei.relation, out.hero_b_id)] = (
            out.reason,
            {"model": out.model, "prompt_version": out.prompt_version},
        )
        reasons_written += 1

    if reasons:
        updated = _apply_reasons(hero, reasons)
        write_hero(data_dir, patch, updated)
        write_summary(data_dir, updated, "pro")

    logger.info(
        "Reason batch done hero_id=%s reasons_written=%s reasons_skipped=%s",
        hero_id,
        reasons_written,
        reasons_skipped,
    )

    return HeroResult(
        hero_id=hero_id,
        success=True,
        reasons_written=reasons_written,
        reasons_skipped=reasons_skipped,
        pending_manual_paths=[pending_reason_prompt] if pending_reason_prompt else None,
    )


ProgressCallback = Callable[["HeroRawBundle", HeroResult], None]


def _merge_pass_results(hero_id: int, extract: HeroResult, reason: HeroResult) -> HeroResult:
    pending: list[Path] = []
    if extract.pending_manual_paths:
        pending.extend(extract.pending_manual_paths)
    if reason.pending_manual_paths:
        pending.extend(reason.pending_manual_paths)
    return HeroResult(
        hero_id=hero_id,
        success=reason.success,
        reasons_written=reason.reasons_written,
        reasons_skipped=reason.reasons_skipped,
        failure_reason=reason.failure_reason,
        pending_manual_paths=pending or None,
    )


def run_bootstrap(
    data_dir: Path,
    patch: str,
    generator_version: str,
    bundles: list[HeroRawBundle],
    client: LLMClient,
    *,
    max_reason_edges: int = 5,
    skip_reasons: bool = False,
    hero_names: dict[int, str] | None = None,
    on_extract: ProgressCallback | None = None,
    on_reason: ProgressCallback | None = None,
) -> list[HeroResult]:
    """
    Drive the two-pass bootstrap across a roster. Pass 1 extracts every hero's
    tags before pass 2 runs so cross-hero reasons can see hero_b tags on disk.

    Returned list preserves `bundles` order. `on_extract` / `on_reason` fire
    per hero with the bundle and the merged HeroResult for that phase — use
    them for CLI progress output; neither is required.
    """
    extract_results: dict[int, HeroResult] = {}
    for bundle in bundles:
        result = extract_hero(data_dir, patch, generator_version, bundle, client)
        extract_results[bundle.hero_id] = result
        if on_extract is not None:
            on_extract(bundle, result)

    if skip_reasons:
        return [extract_results[b.hero_id] for b in bundles]

    merged_results: list[HeroResult] = []
    for bundle in bundles:
        extract = extract_results[bundle.hero_id]
        if not extract.success:
            merged_results.append(extract)
            continue
        reason = reason_hero(
            data_dir,
            patch,
            bundle.hero_id,
            client,
            max_edges=max_reason_edges,
            hero_names=hero_names,
        )
        merged = _merge_pass_results(bundle.hero_id, extract, reason)
        if on_reason is not None:
            on_reason(bundle, merged)
        merged_results.append(merged)
    return merged_results


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
