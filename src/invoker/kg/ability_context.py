from __future__ import annotations

from dataclasses import dataclass
from typing import Any

_NOISY_HEADER_PATTERNS = ("SCEPTER", "SHARD")


@dataclass(frozen=True)
class AttribEntry:
    header: str
    value: str | list[str]
    key: str | None = None


@dataclass(frozen=True)
class AbilityContext:
    internal_name: str
    name: str
    source: str  # "base_ability" | "innate"
    behavior: list[str]
    damage_type: str | None
    pierces_debuff_immunity: bool | None
    dispellable: str | None
    description: str | None
    attribs: list[AttribEntry]
    cast_range: str | list[str] | None = None
    timing: dict[str, str | list[str]] | None = None
    mana_cost: str | list[str] | None = None
    cooldown: str | list[str] | None = None


@dataclass(frozen=True)
class TalentContext:
    internal_name: str
    name: str
    level: int  # tier 1–4 (hero levels 10 / 15 / 20 / 25)


def build_ability_contexts(
    hero_internal_name: str,
    abilities_map: dict[str, Any],
    hero_abilities_map: dict[str, Any],
) -> tuple[list[AbilityContext], list[TalentContext]]:
    hero_data = hero_abilities_map.get(hero_internal_name, {})

    abilities: list[AbilityContext] = []
    for ability_name in hero_data.get("abilities", []):
        if ability_name == "generic_hidden":
            continue
        raw = abilities_map.get(ability_name)
        if not isinstance(raw, dict):
            continue
        ability = _build_ability(ability_name, raw)
        if ability.source != "innate" and "Hidden" in ability.behavior:
            continue
        abilities.append(ability)

    talents: list[TalentContext] = []
    for entry in hero_data.get("talents", []):
        talent_name = entry.get("name", "")
        raw = abilities_map.get(talent_name)
        if not isinstance(raw, dict):
            continue
        talents.append(
            TalentContext(
                internal_name=talent_name,
                name=str(raw.get("dname", talent_name)),
                level=int(entry.get("level", 0)),
            )
        )

    return abilities, talents


def _is_noisy_header(header: str) -> bool:
    upper = header.upper()
    if upper.endswith("TOOLTIP:") or "TOOLTIP" in upper:
        return True
    return any(pat in upper for pat in _NOISY_HEADER_PATTERNS)


def _build_ability(internal_name: str, raw: dict[str, Any]) -> AbilityContext:
    behavior_raw = raw.get("behavior")
    if isinstance(behavior_raw, list):
        behavior = [str(b) for b in behavior_raw]
    elif behavior_raw is not None:
        behavior = [str(behavior_raw)]
    else:
        behavior = []

    bkb = raw.get("bkbpierce")
    if bkb == "Yes":
        pierces: bool | None = True
    elif bkb == "No":
        pierces = False
    else:
        pierces = None

    attribs = [
        AttribEntry(
            header=str(a["header"]),
            value=_to_str_or_list(a["value"]),
            key=str(a["key"]) if "key" in a else None,
        )
        for a in raw.get("attrib", [])
        if isinstance(a, dict)
        and "header" in a
        and "value" in a
        and not _is_noisy_header(str(a["header"]))
    ]

    return AbilityContext(
        internal_name=internal_name,
        name=raw.get("dname", internal_name),
        source="innate" if raw.get("is_innate") else "base_ability",
        behavior=behavior,
        damage_type=raw.get("dmg_type") or None,
        pierces_debuff_immunity=pierces,
        dispellable=raw.get("dispellable") or None,
        description=raw.get("desc") or None,
        attribs=attribs,
        cast_range=_to_str_or_list(raw["cast_range"]) if "cast_range" in raw else None,
        timing=_timing(raw.get("timing")),
        mana_cost=_to_str_or_list(raw["mc"]) if "mc" in raw else None,
        cooldown=_to_str_or_list(raw["cd"]) if "cd" in raw else None,
    )


def _to_str_or_list(v: Any) -> str | list[str]:
    if isinstance(v, list):
        return [str(x) for x in v]
    return str(v)


def _timing(raw: Any) -> dict[str, str | list[str]] | None:
    if not isinstance(raw, dict):
        return None
    timing = {str(key): _to_str_or_list(value) for key, value in raw.items()}
    return timing or None
