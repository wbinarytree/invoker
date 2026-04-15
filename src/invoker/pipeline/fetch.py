from __future__ import annotations

from invoker.config import Config
from invoker.sources.opendota import OpenDotaFetcher
from invoker.sources.stratz import StratzFetcher


async def fetch_all(cfg: Config, patch: str, *, force: bool = False) -> dict:
    cache = cfg.data_dir / "raw"
    od = OpenDotaFetcher(cache, patch)
    strat = StratzFetcher(cache, patch, cfg.stratz_token)
    try:
        heroes = await od.heroes()
        abilities = await od.abilities()
        hero_abilities = await od.hero_abilities_map()
        pro_matches = await od.pro_matches()
        matchups = {h["id"]: await od.matchups(h["id"]) for h in heroes}
        stratz_edges = (
            {h["id"]: await strat.synergies(h["id"]) for h in heroes}
            if strat.available
            else {}
        )
        return {
            "heroes": heroes,
            "abilities": abilities,
            "hero_abilities": hero_abilities,
            "pro_matches": pro_matches,
            "matchups": matchups,
            "stratz_edges": stratz_edges,
        }
    finally:
        await od.close()
        await strat.close()
