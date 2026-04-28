from __future__ import annotations

import contextlib
from dataclasses import dataclass
from typing import Any

_TRACKED_STATS = [
    "base_str",
    "base_agi",
    "base_int",
    "str_gain",
    "agi_gain",
    "int_gain",
    "base_armor",
    "attack_range",
    "move_speed",
]

# Quintile boundaries: [0.2, 0.4, 0.6, 0.8] → five even bands.
_BANDS = [
    (0.2, "very_low"),
    (0.4, "low"),
    (0.6, "average"),
    (0.8, "high"),
    (float("inf"), "very_high"),
]


def _assign_band(percentile: float) -> str:
    for cutoff, name in _BANDS:
        if percentile < cutoff:
            return name
    return "very_high"


@dataclass(frozen=True)
class StatEntry:
    value: float
    percentile: float
    band: str


@dataclass(frozen=True)
class HeroStatsContext:
    base_str: StatEntry | None
    base_agi: StatEntry | None
    base_int: StatEntry | None
    str_gain: StatEntry | None
    agi_gain: StatEntry | None
    int_gain: StatEntry | None
    base_armor: StatEntry | None
    attack_range: StatEntry | None
    move_speed: StatEntry | None
    primary_attr: str
    attack_type: str


def compute_hero_stats_context(
    hero_internal_name: str,
    all_heroes: dict[str, Any],
) -> HeroStatsContext:
    """
    Compute a HeroStatsContext for one hero relative to all heroes.

    all_heroes: constants-shaped hero stats keyed by internal hero name.
    Percentile is computed across the full roster for each stat independently.
    """
    hero = all_heroes.get(hero_internal_name, {})

    stat_values: dict[str, list[float]] = {stat: [] for stat in _TRACKED_STATS}
    for h in all_heroes.values():
        for stat in _TRACKED_STATS:
            raw = h.get(stat)
            if raw is not None:
                with contextlib.suppress(TypeError, ValueError):
                    stat_values[stat].append(float(raw))

    def make_entry(stat: str) -> StatEntry | None:
        raw = hero.get(stat)
        if raw is None:
            return None
        try:
            value = float(raw)
        except (TypeError, ValueError):
            return None
        roster = stat_values[stat]
        if not roster:
            return StatEntry(value=value, percentile=0.5, band="average")
        below = sum(1 for v in roster if v < value)
        equal = sum(1 for v in roster if v == value)
        percentile = round((below + 0.5 * equal) / len(roster), 2)
        return StatEntry(value=value, percentile=percentile, band=_assign_band(percentile))

    return HeroStatsContext(
        base_str=make_entry("base_str"),
        base_agi=make_entry("base_agi"),
        base_int=make_entry("base_int"),
        str_gain=make_entry("str_gain"),
        agi_gain=make_entry("agi_gain"),
        int_gain=make_entry("int_gain"),
        base_armor=make_entry("base_armor"),
        attack_range=make_entry("attack_range"),
        move_speed=make_entry("move_speed"),
        primary_attr=str(hero.get("primary_attr", "")),
        attack_type=str(hero.get("attack_type", "")),
    )
