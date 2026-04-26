from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from invoker.kg.hero_stats_context import HeroStatsContext, compute_hero_stats_context
from invoker.sources.opendota import OpenDotaFetcher


@dataclass(frozen=True)
class HeroIdentityContext:
    hero_id: int
    hero_slug: str
    localized_name: str
    primary_attr: str
    attack_type: str
    roles: list[str]


@dataclass(frozen=True)
class HeroContextPacket:
    """Composable static context for one hero at a given patch.

    Separates context assembly from prompt rendering so the same packet
    can be consumed by multiple callers without re-fetching source data.
    abilities and talents are not yet populated.
    """

    patch: str
    hero: HeroIdentityContext
    stats: HeroStatsContext
    abilities: list[Any] = field(default_factory=list)
    talents: list[Any] = field(default_factory=list)


async def build_hero_context(
    data_dir: Path,
    hero: str,
    *,
    patch: str,
) -> HeroContextPacket:
    """
    Assemble a HeroContextPacket from OpenDota source data.
    hero: internal name, slug, localized name, or numeric id.
    """
    fetcher = OpenDotaFetcher(data_dir / "raw", patch)
    try:
        heroes_list = await fetcher.heroes()
        raw_stats = await fetcher.hero_stats()
        # /api/constants/heroes is keyed by numeric id; remap to internal name
        hero_stats_map = {v["name"]: v for v in raw_stats.values() if "name" in v}
        hero_record = _find_hero(heroes_list, hero)
        internal_name = hero_record["name"]
        stats = compute_hero_stats_context(internal_name, hero_stats_map)
        identity = HeroIdentityContext(
            hero_id=hero_record["id"],
            hero_slug=internal_name.removeprefix("npc_dota_hero_"),
            localized_name=hero_record["localized_name"],
            primary_attr=str(hero_record.get("primary_attr", "")),
            attack_type=str(hero_record.get("attack_type", "")),
            roles=list(hero_record.get("roles", [])),
        )
        return HeroContextPacket(
            patch=patch,
            hero=identity,
            stats=stats,
        )
    finally:
        await fetcher.close()


def _find_hero(heroes: list[dict[str, Any]], hero: str) -> dict[str, Any]:
    token = hero.strip().lower()
    for h in heroes:
        slug = h.get("name", "").removeprefix("npc_dota_hero_")
        candidates = {
            slug.lower(),
            h.get("localized_name", "").lower(),
            str(h.get("id", "")),
            h.get("name", "").lower(),
        }
        if token in candidates:
            return h
    raise FileNotFoundError(f"hero {hero!r} not found in OpenDota roster")
