from __future__ import annotations

from invoker.pipeline.orchestrator import HeroRawBundle


def _resolve_abilities(
    hero_internal: str,
    hero_abilities_map: dict,
    abilities_dict: dict,
) -> list[dict]:
    """Return list of {name, text} dicts for a hero's non-trivial abilities."""
    entry = hero_abilities_map.get(hero_internal, {})
    ability_names: list[str] = entry.get("abilities", [])
    out: list[dict] = []
    for ab_name in ability_names:
        ab = abilities_dict.get(ab_name)
        if not ab:
            continue
        dname = ab.get("dname") or ""
        desc = ab.get("desc") or ""
        if not dname or not desc:
            continue
        out.append({"name": dname, "text": desc})
    return out


def build_bundles(raw: dict, patch: str) -> list[HeroRawBundle]:
    """
    Convert fetch_all output into HeroRawBundle objects ready for run_for_hero.

    Meta stats (position_counts, contest_rate, win_rate) are zeroed — no source
    exists yet without fetching individual match details. Explicit zeros are used
    rather than omitting the fields (null is correct when data is missing).
    """
    heroes: list[dict] = raw["heroes"]
    abilities_dict: dict = raw["abilities"]
    hero_abilities_map: dict = raw["hero_abilities"]
    matchups: dict[int, list[dict]] = raw.get("matchups", {})
    stratz_edges: dict[int, list[dict]] = raw.get("stratz_edges", {})

    bundles: list[HeroRawBundle] = []
    for h in heroes:
        hero_id: int = h["id"]
        internal_name: str = h["name"]  # e.g. npc_dota_hero_pangolier

        abilities = _resolve_abilities(internal_name, hero_abilities_map, abilities_dict)

        bundles.append(
            HeroRawBundle(
                hero_id=hero_id,
                localized_name=h["localized_name"],
                internal_name=internal_name,
                roles=h.get("roles", []),
                abilities=abilities,
                stratz_edges=stratz_edges.get(hero_id) or None,
                opendota_matchups=matchups.get(hero_id) or None,
                position_counts={},
                total_pro_games=0,
                window_days=0,
                contest_rate=0.0,
                win_rate=0.0,
                meta_history=[],
            )
        )
    return bundles
