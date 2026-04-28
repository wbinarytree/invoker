from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

from invoker.kg.ability_context import AbilityContext, TalentContext, build_ability_contexts
from invoker.kg.hero_stats_context import HeroStatsContext, compute_hero_stats_context
from invoker.sources.game_files import GameFilesSource


class HeroConstantsSource(Protocol):
    """Constants surface needed to assemble a hero authoring packet."""

    def heroes(self) -> list[dict[str, Any]]: ...

    def hero_stats(self) -> dict[str, Any]: ...

    def abilities(self) -> dict[str, Any]: ...

    def hero_abilities_map(self) -> dict[str, Any]: ...


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
    """

    patch: str
    hero: HeroIdentityContext
    stats: HeroStatsContext
    abilities: list[AbilityContext] = field(default_factory=list)
    talents: list[TalentContext] = field(default_factory=list)


async def build_hero_context(
    game_data_dir: Path,
    hero: str,
    *,
    patch: str,
) -> HeroContextPacket:
    """
    Assemble a HeroContextPacket from game-file snapshot data.
    hero: internal name, slug, localized name, or numeric id.
    """
    source = GameFilesSource(game_data_dir, patch)
    return build_hero_context_from_source(source, hero, patch=patch)


def build_hero_context_from_source(
    source: HeroConstantsSource,
    hero: str,
    *,
    patch: str,
) -> HeroContextPacket:
    """Assemble a HeroContextPacket from an already-constructed constants source."""
    heroes_list = source.heroes()
    raw_stats = source.hero_stats()
    raw_abilities = source.abilities()
    raw_hero_abilities = source.hero_abilities_map()
    hero_stats_map = {v["name"]: v for v in raw_stats.values() if "name" in v}
    hero_record = _find_hero(heroes_list, hero)
    internal_name = hero_record["name"]
    stats = compute_hero_stats_context(internal_name, hero_stats_map)
    abilities, talents = build_ability_contexts(
        internal_name, raw_abilities, raw_hero_abilities
    )
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
        abilities=abilities,
        talents=talents,
    )


class HeroNotFoundError(ValueError):
    pass


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
    raise HeroNotFoundError(f"hero {hero!r} not found in game-file snapshot roster")
