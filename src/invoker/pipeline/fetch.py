from __future__ import annotations

from invoker.config import Config
from invoker.logging import get_logger
from invoker.sources.opendota import OpenDotaFetcher
from invoker.sources.stratz import StratzFetcher

logger = get_logger(__name__)


def _apply_filter(heroes: list[dict], hero_filter: set[str] | None) -> list[dict]:
    """Return only heroes matching the filter (by name or numeric id string)."""
    if hero_filter is None:
        return heroes
    normalised = {t.lower() for t in hero_filter}
    return [
        h
        for h in heroes
        if h.get("localized_name", "").lower() in normalised
        or str(h.get("id", "")) in normalised
    ]


async def fetch_all(
    cfg: Config,
    patch: str,
    *,
    hero_filter: set[str] | None = None,
) -> dict:
    """
    Fetch raw data for the given patch.

    hero_filter: set of name or numeric-id strings to restrict per-hero calls.
    None means fetch all heroes (production behaviour).
    """
    cache = cfg.data_dir / "raw"
    od = OpenDotaFetcher(cache, patch)
    strat = StratzFetcher(cache, patch, cfg.stratz_token)
    try:
        logger.info(
            "Fetch start patch=%s hero_filter=%s stratz_available=%s",
            patch,
            sorted(hero_filter) if hero_filter else None,
            strat.available,
        )
        all_heroes = await od.heroes()
        abilities = await od.abilities()
        hero_abilities = await od.hero_abilities_map()
        pro_matches = await od.pro_matches()

        heroes = _apply_filter(all_heroes, hero_filter)
        hero_names = {h["id"]: h["localized_name"] for h in all_heroes}

        matchups = {h["id"]: await od.matchups(h["id"]) for h in heroes}
        stratz_edges = (
            {h["id"]: await strat.synergies(h["id"]) for h in heroes}
            if strat.available
            else {}
        )
        logger.info(
            "Fetch done patch=%s roster_heroes=%s selected_heroes=%s stratz_heroes=%s",
            patch,
            len(all_heroes),
            len(heroes),
            len(stratz_edges),
        )
        return {
            "heroes": heroes,
            "hero_names": hero_names,
            "abilities": abilities,
            "hero_abilities": hero_abilities,
            "pro_matches": pro_matches,
            "matchups": matchups,
            "stratz_edges": stratz_edges,
        }
    finally:
        await od.close()
        await strat.close()
