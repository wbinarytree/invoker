from __future__ import annotations

import json
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from invoker.kg.ability_context import AttribEntry, TalentContext
from invoker.kg.hero_context import HeroContextPacket, build_hero_context_from_source
from invoker.kg.hero_stats_context import HeroStatsContext, StatEntry
from invoker.sources.game_files import GameFilesSource

IDENTITY_SCHEMA_VERSION = 1
GAME_RESOURCE_SCHEMA_VERSION = 2
LOCALIZED_RESOURCE_FILENAMES = {
    "heroes": "hero_identity_localization.json",
    "items": "item_identity_localization.json",
    "abilities": "ability_localization.json",
}
GAME_RESOURCE_FILENAMES = {
    "bundle": "bundle.json",
    "heroes": "heroes.json",
    "items": "items.json",
    "index": "index.json",
}


class IdentityExportError(ValueError):
    pass


def export_identity_localization(
    game_data_dir: Path,
    patch: str,
    *,
    locales: Sequence[str] | None = None,
) -> dict[str, Any]:
    patch_dir, snapshot, selected_locales, localizations = _load_export_inputs(
        game_data_dir, patch, locales
    )
    heroes_raw = _read_json(patch_dir / "heroes.json")
    items_raw = _read_json(patch_dir / "items.json")
    neutral_items_raw = _read_json(patch_dir / "neutral_items.json")
    if not isinstance(heroes_raw, dict):
        raise IdentityExportError(f"heroes.json must be an object: {patch_dir}")
    if not isinstance(items_raw, dict):
        raise IdentityExportError(f"items.json must be an object: {patch_dir}")
    if not isinstance(neutral_items_raw, dict):
        raise IdentityExportError(f"neutral_items.json must be an object: {patch_dir}")

    heroes = _hero_identities(heroes_raw, localizations)
    _validate_heroes(heroes)
    alias_collisions = _alias_collisions(heroes)
    items = _item_identities(items_raw, neutral_items_raw, localizations)
    unknowns = _unknowns(heroes, items, selected_locales, alias_collisions)

    return {
        "schema_version": IDENTITY_SCHEMA_VERSION,
        "patch": patch,
        "generated_at": datetime.now(UTC).isoformat(),
        "generated_from": _generated_from(patch, snapshot),
        "locales": list(selected_locales),
        "heroes": heroes,
        "items": items,
        "unknowns": unknowns,
    }


def export_hero_identity_localization(
    game_data_dir: Path,
    patch: str,
    *,
    locales: Sequence[str] | None = None,
) -> dict[str, Any]:
    patch_dir, snapshot, selected_locales, localizations = _load_export_inputs(
        game_data_dir, patch, locales
    )
    heroes_raw = _read_json(patch_dir / "heroes.json")
    if not isinstance(heroes_raw, dict):
        raise IdentityExportError(f"heroes.json must be an object: {patch_dir}")

    heroes = _hero_identities(heroes_raw, localizations)
    _validate_heroes(heroes)
    alias_collisions = _alias_collisions(heroes)
    return {
        **_resource_base(patch, snapshot, selected_locales, resource_type="heroes"),
        "heroes": heroes,
        "unknowns": _hero_unknowns(heroes, selected_locales, alias_collisions),
    }


def export_item_identity_localization(
    game_data_dir: Path,
    patch: str,
    *,
    locales: Sequence[str] | None = None,
) -> dict[str, Any]:
    patch_dir, snapshot, selected_locales, localizations = _load_export_inputs(
        game_data_dir, patch, locales
    )
    items_raw = _read_json(patch_dir / "items.json")
    neutral_items_raw = _read_json(patch_dir / "neutral_items.json")
    if not isinstance(items_raw, dict):
        raise IdentityExportError(f"items.json must be an object: {patch_dir}")
    if not isinstance(neutral_items_raw, dict):
        raise IdentityExportError(f"neutral_items.json must be an object: {patch_dir}")

    items = _item_identities(items_raw, neutral_items_raw, localizations)
    return {
        **_resource_base(patch, snapshot, selected_locales, resource_type="items"),
        "items": items,
        "unknowns": _item_unknowns(items, selected_locales),
    }


def export_ability_localization(
    game_data_dir: Path,
    patch: str,
    *,
    locales: Sequence[str] | None = None,
) -> dict[str, Any]:
    patch_dir, snapshot, selected_locales, localizations = _load_export_inputs(
        game_data_dir, patch, locales
    )
    abilities_raw = _read_json(patch_dir / "abilities.json")
    hero_abilities_raw = _read_json(patch_dir / "hero_abilities.json")
    if not isinstance(abilities_raw, dict):
        raise IdentityExportError(f"abilities.json must be an object: {patch_dir}")
    if not isinstance(hero_abilities_raw, dict):
        raise IdentityExportError(f"hero_abilities.json must be an object: {patch_dir}")

    abilities = _ability_identities(abilities_raw, hero_abilities_raw, localizations)
    return {
        **_resource_base(patch, snapshot, selected_locales, resource_type="abilities"),
        "abilities": abilities,
        "unknowns": _ability_unknowns(abilities, selected_locales),
    }


def export_localized_resources(
    game_data_dir: Path,
    patch: str,
    *,
    locales: Sequence[str] | None = None,
) -> dict[str, dict[str, Any]]:
    return {
        "heroes": export_hero_identity_localization(game_data_dir, patch, locales=locales),
        "items": export_item_identity_localization(game_data_dir, patch, locales=locales),
        "abilities": export_ability_localization(game_data_dir, patch, locales=locales),
    }


def export_game_resource_bundle(
    game_data_dir: Path,
    patch: str,
    *,
    locales: Sequence[str] | None = None,
) -> dict[str, dict[str, Any]]:
    patch_dir, snapshot, selected_locales, localizations = _load_export_inputs(
        game_data_dir, patch, locales
    )
    heroes_raw = _read_json(patch_dir / "heroes.json")
    items_raw = _read_json(patch_dir / "items.json")
    neutral_items_raw = _read_json(patch_dir / "neutral_items.json")
    if not isinstance(heroes_raw, dict):
        raise IdentityExportError(f"heroes.json must be an object: {patch_dir}")
    if not isinstance(items_raw, dict):
        raise IdentityExportError(f"items.json must be an object: {patch_dir}")
    if not isinstance(neutral_items_raw, dict):
        raise IdentityExportError(f"neutral_items.json must be an object: {patch_dir}")

    generated_at = datetime.now(UTC).isoformat()
    heroes = _game_resource_heroes(
        game_data_dir, patch, selected_locales, localizations, heroes_raw
    )
    items = _game_resource_items(items_raw, neutral_items_raw, localizations)
    index = _game_resource_index(heroes, items, selected_locales)
    unknowns = _game_resource_unknowns(heroes, items, selected_locales, index)
    generated_from = _generated_from(patch, snapshot)
    return {
        "bundle": {
            "schema_version": GAME_RESOURCE_SCHEMA_VERSION,
            "patch": patch,
            "generated_at": generated_at,
            "generated_from": generated_from,
            "locales": list(selected_locales),
            "files": {
                "heroes": GAME_RESOURCE_FILENAMES["heroes"],
                "items": GAME_RESOURCE_FILENAMES["items"],
                "index": GAME_RESOURCE_FILENAMES["index"],
            },
            "counts": {
                "heroes": len(heroes),
                "items": len(items),
                "unknowns": len(unknowns),
            },
            "unknowns": unknowns,
        },
        "heroes": {
            "schema_version": GAME_RESOURCE_SCHEMA_VERSION,
            "resource_type": "heroes",
            "patch": patch,
            "generated_at": generated_at,
            "generated_from": generated_from,
            "locales": list(selected_locales),
            "heroes": heroes,
        },
        "items": {
            "schema_version": GAME_RESOURCE_SCHEMA_VERSION,
            "resource_type": "items",
            "patch": patch,
            "generated_at": generated_at,
            "generated_from": generated_from,
            "locales": list(selected_locales),
            "items": items,
        },
        "index": {
            "schema_version": GAME_RESOURCE_SCHEMA_VERSION,
            "resource_type": "index",
            "patch": patch,
            "generated_at": generated_at,
            "locales": list(selected_locales),
            **index,
        },
    }


def hero_lookup_candidates(
    game_data_dir: Path,
    patch: str,
    query: str | int,
    *,
    locales: Sequence[str] | None = None,
) -> list[dict[str, Any]]:
    artifact = export_identity_localization(game_data_dir, patch, locales=locales)
    query_token = _normalize(str(query))
    if not query_token:
        return []
    candidates: list[dict[str, Any]] = []
    for hero in artifact["heroes"]:
        matches = _hero_matches(hero, query_token)
        if not matches:
            continue
        candidate = {
            "hero_id": hero["hero_id"],
            "hero_slug": hero["slug"],
            "internal_name": hero["internal_name"],
            "localized_name": _first_display_name(hero),
            "display_names": hero["display_names"],
            "aliases": hero["aliases"],
            "matches": matches,
        }
        candidates.append(candidate)
    return candidates


def available_locales(game_data_dir: Path, patch: str) -> tuple[str, ...]:
    patch_dir = game_data_dir / patch
    snapshot = _read_snapshot(patch_dir)
    return _selected_locales(patch_dir, snapshot, None)


def _hero_identities(
    heroes_raw: dict[str, Any],
    localizations: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    heroes: list[dict[str, Any]] = []
    for internal_name, raw in sorted(heroes_raw.items()):
        if not isinstance(raw, dict) or not _is_live_hero(raw):
            continue
        display_names: dict[str, str] = {}
        for locale, localization in localizations.items():
            display_name = _localized_hero_name(internal_name, raw, localization, locale=locale)
            if display_name is not None:
                display_names[locale] = display_name
        aliases = {
            locale: locale_aliases
            for locale, localization in localizations.items()
            if (locale_aliases := _hero_aliases(internal_name, localization))
        }
        sources = ["npc_heroes"]
        if display_names or aliases:
            sources.append("localization")
        heroes.append(
            {
                "hero_id": int(str(raw["HeroID"])),
                "internal_name": internal_name,
                "slug": internal_name.removeprefix("npc_dota_hero_"),
                "display_names": display_names,
                "aliases": aliases,
                "sources": sources,
            }
        )
    return sorted(heroes, key=lambda hero: (hero["hero_id"], hero["internal_name"]))


def _item_identities(
    items_raw: dict[str, Any],
    neutral_items_raw: dict[str, Any],
    localizations: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    neutral_names = _neutral_item_names(neutral_items_raw)
    identities: list[dict[str, Any]] = []
    for internal_name, raw in sorted(items_raw.items()):
        if not internal_name.startswith("item_") or not isinstance(raw, dict):
            continue
        display_names = {
            locale: display_name
            for locale, localization in localizations.items()
            if (display_name := _localized_item_name(internal_name, localization)) is not None
        }
        aliases = {
            locale: locale_aliases
            for locale, localization in localizations.items()
            if (locale_aliases := _item_aliases(internal_name, localization))
        }
        entry: dict[str, Any] = {
            "internal_name": internal_name,
            "display_names": display_names,
            "aliases": aliases,
            "is_neutral": internal_name in neutral_names,
            "sources": ["items"],
        }
        descriptions = {
            locale: description
            for locale, localization in localizations.items()
            if (description := _localized_item_description(internal_name, localization)) is not None
        }
        entry["descriptions"] = descriptions
        item_id = _int_or_none(raw.get("ID") or raw.get("ItemID"))
        if item_id is not None:
            entry["item_id"] = item_id
        if display_names or descriptions or aliases:
            entry["sources"].append("localization")
        identities.append(entry)
    return identities


def _ability_identities(
    abilities_raw: dict[str, Any],
    hero_abilities_raw: dict[str, Any],
    localizations: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    owners = _ability_owners(hero_abilities_raw)
    identities: list[dict[str, Any]] = []
    for internal_name in sorted(owners):
        raw = abilities_raw.get(internal_name)
        if not isinstance(raw, dict):
            continue
        display_names = {
            locale: display_name
            for locale, localization in localizations.items()
            if (display_name := _localized_ability_name(internal_name, localization)) is not None
        }
        descriptions = {
            locale: description
            for locale, localization in localizations.items()
            if (
                description := _localized_ability_description(
                    internal_name,
                    raw,
                    localization,
                )
            )
            is not None
        }
        aliases = {
            locale: locale_aliases
            for locale, localization in localizations.items()
            if (locale_aliases := _ability_aliases(internal_name, localization))
        }
        entry: dict[str, Any] = {
            "internal_name": internal_name,
            "display_names": display_names,
            "descriptions": descriptions,
            "aliases": aliases,
            "heroes": sorted(owners[internal_name]),
            "sources": ["abilities", "hero_abilities"],
        }
        ability_id = _int_or_none(raw.get("ID") or raw.get("AbilityID"))
        if ability_id is not None:
            entry["ability_id"] = ability_id
        if display_names or descriptions or aliases:
            entry["sources"].append("localization")
        identities.append(entry)
    return identities


def _ability_owners(hero_abilities_raw: dict[str, Any]) -> dict[str, set[str]]:
    owners: dict[str, set[str]] = {}
    for hero_name, raw in hero_abilities_raw.items():
        if not isinstance(hero_name, str) or not isinstance(raw, dict):
            continue
        for ability_name in _strings(raw.get("abilities")):
            if not ability_name.startswith("item_"):
                owners.setdefault(ability_name, set()).add(hero_name)
        for talent in raw.get("talents") or []:
            if isinstance(talent, dict):
                talent_name = talent.get("name")
                if isinstance(talent_name, str) and talent_name:
                    owners.setdefault(talent_name, set()).add(hero_name)
    return owners


def _strings(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str) and item]


def _game_resource_heroes(
    game_data_dir: Path,
    patch: str,
    locales: tuple[str, ...],
    localizations: dict[str, dict[str, Any]],
    heroes_raw: dict[str, Any],
) -> list[dict[str, Any]]:
    base_locale = "english" if "english" in locales else locales[0]
    sources = {locale: GameFilesSource(game_data_dir, patch, locale=locale) for locale in locales}
    base_source = sources[base_locale]
    identities = {
        hero["internal_name"]: hero for hero in _hero_identities(heroes_raw, localizations)
    }
    heroes: list[dict[str, Any]] = []
    for hero in base_source.heroes():
        internal_name = str(hero["name"])
        identity = identities.get(internal_name)
        if identity is None:
            continue
        contexts = {
            locale: build_hero_context_from_source(source, internal_name, patch=patch)
            for locale, source in sources.items()
        }
        base_context = contexts[base_locale]
        heroes.append(
            {
                "hero_id": int(identity["hero_id"]),
                "internal_name": internal_name,
                "slug": identity["slug"],
                "display_names": identity["display_names"],
                "aliases": identity["aliases"],
                "primary_attr": base_context.hero.primary_attr,
                "attack_type": base_context.hero.attack_type,
                "roles": base_context.hero.roles,
                "stats": _stats_to_dict(base_context.stats),
                "abilities": _hero_abilities_to_resource(base_context, contexts),
                "talents": _hero_talents_to_resource(base_context, contexts),
                "sources": ["npc_heroes", "hero_abilities", "abilities", "localization"],
            }
        )
    return sorted(heroes, key=lambda entry: (entry["hero_id"], entry["internal_name"]))


def _hero_abilities_to_resource(
    base_context: HeroContextPacket,
    contexts: dict[str, HeroContextPacket],
) -> list[dict[str, Any]]:
    localized = {
        locale: {ability.internal_name: ability for ability in context.abilities}
        for locale, context in contexts.items()
    }
    abilities: list[dict[str, Any]] = []
    for ability in base_context.abilities:
        if ability.internal_name.startswith("item_"):
            continue
        display_names = {
            locale: locale_ability.name
            for locale, abilities_by_name in localized.items()
            if (locale_ability := abilities_by_name.get(ability.internal_name)) is not None
            and locale_ability.name
        }
        descriptions = {
            locale: locale_ability.description
            for locale, abilities_by_name in localized.items()
            if (locale_ability := abilities_by_name.get(ability.internal_name)) is not None
            and locale_ability.description
        }
        payload = {
            "internal_name": ability.internal_name,
            "display_names": display_names,
            "descriptions": descriptions,
            "source": ability.source,
            "behavior": ability.behavior,
            "damage_type": ability.damage_type,
            "pierces_debuff_immunity": ability.pierces_debuff_immunity,
            "dispellable": ability.dispellable,
            "attribs": [_attrib_to_resource(attrib) for attrib in ability.attribs],
            "cast_range": ability.cast_range,
            "timing": ability.timing,
            "mana_cost": ability.mana_cost,
            "cooldown": ability.cooldown,
            "sources": ["hero_abilities", "abilities", "localization"],
        }
        abilities.append(_drop_none(payload))
    return abilities


def _hero_talents_to_resource(
    base_context: HeroContextPacket,
    contexts: dict[str, HeroContextPacket],
) -> list[dict[str, Any]]:
    localized = {
        locale: {talent.internal_name: talent for talent in context.talents}
        for locale, context in contexts.items()
    }
    talents: list[dict[str, Any]] = []
    for talent in base_context.talents:
        display_names = {
            locale: locale_talent.name
            for locale, talents_by_name in localized.items()
            if (locale_talent := talents_by_name.get(talent.internal_name)) is not None
            and locale_talent.name
        }
        talents.append(
            {
                "internal_name": talent.internal_name,
                "level": talent.level,
                "hero_level": _talent_hero_level(talent),
                "display_names": display_names,
                "value_sources": ["AbilityValues"],
                "sources": ["hero_abilities", "abilities", "localization"],
            }
        )
    return talents


def _game_resource_items(
    items_raw: dict[str, Any],
    neutral_items_raw: dict[str, Any],
    localizations: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    neutral_metadata = _neutral_item_metadata(neutral_items_raw)
    items: list[dict[str, Any]] = []
    for internal_name, raw in sorted(items_raw.items()):
        if not internal_name.startswith("item_") or not isinstance(raw, dict):
            continue
        display_names = {
            locale: display_name
            for locale, localization in localizations.items()
            if (display_name := _localized_item_name(internal_name, localization)) is not None
        }
        descriptions = {
            locale: description
            for locale, localization in localizations.items()
            if (description := _localized_item_description(internal_name, localization)) is not None
        }
        aliases = {
            locale: locale_aliases
            for locale, localization in localizations.items()
            if (locale_aliases := _item_aliases(internal_name, localization))
        }
        is_recipe = raw.get("ItemRecipe") == "1" or internal_name.startswith("item_recipe_")
        item: dict[str, Any] = {
            "internal_name": internal_name,
            "display_names": display_names,
            "aliases": aliases,
            "descriptions": descriptions,
            "is_neutral": internal_name in neutral_metadata,
            "is_recipe": is_recipe,
            "cost": _int_or_none(raw.get("ItemCost")),
            "stats": _ability_values_to_resource(raw.get("AbilityValues")),
            "ability": _item_ability_to_resource(raw),
            "sources": ["items", "localization"],
        }
        item_id = _int_or_none(raw.get("ID") or raw.get("ItemID"))
        if item_id is not None:
            item["item_id"] = item_id
        if is_recipe:
            item["recipe"] = _recipe_to_resource(raw)
        if internal_name in neutral_metadata:
            item["neutral"] = neutral_metadata[internal_name]
            item["sources"].append("neutral_items")
        items.append(_drop_none(item))
    return items


def _game_resource_index(
    heroes: list[dict[str, Any]],
    items: list[dict[str, Any]],
    locales: tuple[str, ...],
) -> dict[str, Any]:
    return {
        "heroes": _entity_index(
            heroes,
            id_field="hero_id",
            slug_field="slug",
            target_field="internal_name",
            locales=locales,
        ),
        "items": _entity_index(
            items,
            id_field="item_id",
            slug_field=None,
            target_field="internal_name",
            locales=locales,
        ),
    }


def _entity_index(
    records: list[dict[str, Any]],
    *,
    id_field: str,
    slug_field: str | None,
    target_field: str,
    locales: tuple[str, ...],
) -> dict[str, Any]:
    by_id: dict[str, str] = {}
    by_internal_name: dict[str, str] = {}
    by_slug: dict[str, str] = {}
    by_display_name: dict[str, dict[str, list[str]]] = {locale: {} for locale in locales}
    by_alias: dict[str, dict[str, list[str]]] = {locale: {} for locale in locales}
    for record in records:
        target = str(record[target_field])
        if id_field in record:
            by_id[str(record[id_field])] = target
        by_internal_name[target] = target
        if slug_field is not None and record.get(slug_field):
            by_slug[str(record[slug_field])] = target
        for locale, value in record.get("display_names", {}).items():
            _index_token(by_display_name.setdefault(locale, {}), value, target)
        for locale, aliases in record.get("aliases", {}).items():
            for alias in aliases:
                _index_token(by_alias.setdefault(locale, {}), alias, target)
    index: dict[str, Any] = {
        "by_id": by_id,
        "by_internal_name": by_internal_name,
        "by_display_name": by_display_name,
        "by_alias": by_alias,
    }
    if slug_field is not None:
        index["by_slug"] = by_slug
    return index


def _index_token(index: dict[str, list[str]], value: str, target: str) -> None:
    token = _normalize(value)
    if not token:
        return
    targets = index.setdefault(token, [])
    if target not in targets:
        targets.append(target)


def _game_resource_unknowns(
    heroes: list[dict[str, Any]],
    items: list[dict[str, Any]],
    locales: tuple[str, ...],
    index: dict[str, Any],
) -> list[dict[str, Any]]:
    unknowns: list[dict[str, Any]] = []
    for hero in heroes:
        _append_missing_locales(
            unknowns, "hero_display_name", hero["internal_name"], hero["display_names"], locales
        )
        for ability in hero["abilities"]:
            _append_missing_locales(
                unknowns,
                "base_ability_display_name",
                ability["internal_name"],
                ability["display_names"],
                locales,
            )
            _append_missing_locales(
                unknowns,
                "base_ability_description",
                ability["internal_name"],
                ability["descriptions"],
                locales,
            )
        for talent in hero["talents"]:
            _append_missing_locales(
                unknowns,
                "talent_display_name",
                talent["internal_name"],
                talent["display_names"],
                locales,
            )
    for item in items:
        _append_missing_locales(
            unknowns, "item_display_name", item["internal_name"], item["display_names"], locales
        )
        if not item.get("is_recipe"):
            _append_missing_locales(
                unknowns,
                "item_description",
                item["internal_name"],
                item["descriptions"],
                locales,
            )
    unknowns.extend(_index_collisions("hero_alias_collision", index["heroes"]["by_alias"]))
    unknowns.extend(_index_collisions("item_alias_collision", index["items"]["by_alias"]))
    return unknowns


def _append_missing_locales(
    unknowns: list[dict[str, Any]],
    kind: str,
    internal_name: str,
    values: dict[str, Any],
    locales: tuple[str, ...],
) -> None:
    missing = [locale for locale in locales if locale not in values]
    if missing:
        unknowns.append(
            {
                "kind": kind,
                "internal_name": internal_name,
                "missing_locales": missing,
            }
        )


def _index_collisions(kind: str, by_alias: dict[str, dict[str, list[str]]]) -> list[dict[str, Any]]:
    collisions: list[dict[str, Any]] = []
    for locale, aliases in by_alias.items():
        for token, targets in aliases.items():
            if len(targets) > 1:
                collisions.append(
                    {
                        "kind": kind,
                        "locale": locale,
                        "normalized_alias": token,
                        "internal_names": sorted(targets),
                    }
                )
    return collisions


def _stats_to_dict(stats: HeroStatsContext) -> dict[str, Any]:
    payload: dict[str, Any] = {}
    for name in (
        "base_str",
        "base_agi",
        "base_int",
        "str_gain",
        "agi_gain",
        "int_gain",
        "base_armor",
        "attack_range",
        "move_speed",
    ):
        entry = _stat_entry_to_dict(getattr(stats, name))
        if entry is not None:
            payload[name] = entry
    return payload


def _stat_entry_to_dict(entry: StatEntry | None) -> dict[str, Any] | None:
    if entry is None:
        return None
    return {"value": entry.value, "percentile": entry.percentile, "band": entry.band}


def _attrib_to_resource(attrib: AttribEntry) -> dict[str, Any]:
    payload: dict[str, Any] = {"header": attrib.header, "value": attrib.value}
    if attrib.key is not None:
        payload["key"] = attrib.key
    return payload


def _talent_hero_level(talent: TalentContext) -> int | None:
    return {1: 10, 2: 15, 3: 20, 4: 25}.get(talent.level)


def _ability_values_to_resource(values: Any) -> list[dict[str, Any]]:
    if not isinstance(values, dict):
        return []
    rows: list[dict[str, Any]] = []
    for key, raw in values.items():
        value: Any
        if isinstance(raw, dict):
            if "value" not in raw:
                continue
            value = raw["value"]
        else:
            value = raw
        rows.append(
            {
                "key": str(key),
                "header": _label_from_key(str(key)).upper() + ":",
                "value": _levels(value),
            }
        )
    return rows


def _ability_value_replacements(values: Any) -> dict[str, str]:
    if not isinstance(values, dict):
        return {}
    replacements: dict[str, str] = {}
    for field_name, raw in values.items():
        if isinstance(raw, dict):
            if "value" not in raw:
                continue
            value = raw["value"]
        else:
            value = raw
        replacements[str(field_name)] = _template_value(value)
    return replacements


def _resolve_percent_template(template: str, replacements: dict[str, str]) -> str:
    rendered = template
    for key, value in replacements.items():
        rendered = rendered.replace(f"%{key}%", value)
    return _collapse_replaced_percent_escape(rendered)


def _template_value(value: Any) -> str:
    if not isinstance(value, str):
        return str(value)
    parts = value.split()
    return "/".join(parts) if len(parts) > 1 else value


def _collapse_replaced_percent_escape(value: str) -> str:
    chars: list[str] = []
    index = 0
    while index < len(value):
        if (
            value.startswith("%%", index)
            and chars
            and (chars[-1].isdigit() or chars[-1] in {"+", "-", "."})
        ):
            chars.append("%")
            index += 2
            continue
        chars.append(value[index])
        index += 1
    return "".join(chars)


def _item_ability_to_resource(raw: dict[str, Any]) -> dict[str, Any]:
    ability = {
        "behavior": _raw_behavior(raw.get("AbilityBehavior")),
        "cast_range": _levels(raw["AbilityCastRange"]) if "AbilityCastRange" in raw else None,
        "cast_point": _levels(raw["AbilityCastPoint"]) if "AbilityCastPoint" in raw else None,
        "mana_cost": _levels(raw["AbilityManaCost"]) if "AbilityManaCost" in raw else None,
        "cooldown": _levels(raw["AbilityCooldown"]) if "AbilityCooldown" in raw else None,
        "shared_cooldown": raw.get("AbilitySharedCooldown"),
        "values": _ability_values_to_resource(raw.get("AbilityValues")),
    }
    return _drop_none(ability)


def _raw_behavior(value: Any) -> list[str]:
    if not isinstance(value, str) or not value:
        return []
    return [part.strip() for part in value.split("|") if part.strip()]


def _recipe_to_resource(raw: dict[str, Any]) -> dict[str, Any]:
    requirements: list[dict[str, Any]] = []
    raw_requirements = raw.get("ItemRequirements")
    if isinstance(raw_requirements, dict):
        for slot, components in sorted(raw_requirements.items()):
            if isinstance(components, str):
                requirements.append(
                    {
                        "slot": str(slot),
                        "components": [
                            component.strip()
                            for component in components.split(";")
                            if component.strip()
                        ],
                    }
                )
    return _drop_none(
        {
            "result": raw.get("ItemResult"),
            "requirements": requirements,
        }
    )


def _neutral_item_metadata(raw: dict[str, Any]) -> dict[str, dict[str, Any]]:
    metadata: dict[str, dict[str, Any]] = {}
    tiers = raw.get("neutral_tiers")
    if not isinstance(tiers, dict):
        return metadata
    for tier, tier_data in tiers.items():
        if not isinstance(tier_data, dict):
            continue
        items = tier_data.get("items")
        if not isinstance(items, dict):
            continue
        for item_name in items:
            if isinstance(item_name, str):
                metadata[item_name] = _drop_none(
                    {
                        "tier": _int_or_none(tier),
                        "start_time": tier_data.get("start_time"),
                        "craft_cost": _int_or_none(tier_data.get("craft_cost")),
                        "recraft_cost": _int_or_none(tier_data.get("recraft_cost")),
                    }
                )
    return metadata


def _drop_none(payload: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in payload.items() if value is not None}


def _hero_matches(hero: dict[str, Any], query_token: str) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for field, value in (
        ("hero_id", str(hero["hero_id"])),
        ("internal_name", hero["internal_name"]),
        ("slug", hero["slug"]),
    ):
        if _normalize(value) == query_token:
            matches.append({"field": field, "value": value, "source": "npc_heroes"})
    for locale, value in hero.get("display_names", {}).items():
        if _normalize(value) == query_token:
            matches.append(
                {
                    "field": "display_name",
                    "locale": locale,
                    "value": value,
                    "source": "localization",
                }
            )
    for locale, aliases in hero.get("aliases", {}).items():
        for alias in aliases:
            if _normalize(alias) == query_token:
                matches.append(
                    {
                        "field": "alias",
                        "locale": locale,
                        "value": alias,
                        "source": "localization",
                    }
                )
    return matches


def _validate_heroes(heroes: list[dict[str, Any]]) -> None:
    _fail_duplicates(heroes, "hero_id", "duplicate hero ids")
    _fail_duplicates(heroes, "internal_name", "duplicate hero internal names")


def _alias_collisions(heroes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    owners: dict[tuple[str, str], set[str]] = {}
    for hero in heroes:
        for locale, aliases in hero.get("aliases", {}).items():
            for alias in aliases:
                owners.setdefault((locale, _normalize(alias)), set()).add(hero["internal_name"])
    return [
        {
            "kind": "hero_alias_collision",
            "locale": locale,
            "normalized_alias": token,
            "internal_names": sorted(internal_names),
        }
        for (locale, token), internal_names in sorted(owners.items())
        if token and len(internal_names) > 1
    ]


def _fail_duplicates(entries: list[dict[str, Any]], field: str, message: str) -> None:
    seen: dict[Any, int] = {}
    for entry in entries:
        value = entry.get(field)
        seen[value] = seen.get(value, 0) + 1
    duplicates = sorted(value for value, count in seen.items() if count > 1)
    if duplicates:
        raise IdentityExportError(f"{message}: {duplicates}")


def _unknowns(
    heroes: list[dict[str, Any]],
    items: list[dict[str, Any]],
    locales: tuple[str, ...],
    alias_collisions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    unknowns: list[dict[str, Any]] = _hero_unknowns(heroes, locales, alias_collisions)
    unknowns.extend(_item_unknowns(items, locales))
    return unknowns


def _hero_unknowns(
    heroes: list[dict[str, Any]],
    locales: tuple[str, ...],
    alias_collisions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    unknowns: list[dict[str, Any]] = list(alias_collisions)
    for hero in heroes:
        missing = [locale for locale in locales if locale not in hero["display_names"]]
        if missing:
            unknowns.append(
                {
                    "kind": "hero_display_name",
                    "internal_name": hero["internal_name"],
                    "missing_locales": missing,
                }
            )
    return unknowns


def _item_unknowns(
    items: list[dict[str, Any]],
    locales: tuple[str, ...],
) -> list[dict[str, Any]]:
    unknowns: list[dict[str, Any]] = []
    for item in items:
        missing = [locale for locale in locales if locale not in item["display_names"]]
        if missing:
            unknowns.append(
                {
                    "kind": "item_display_name",
                    "internal_name": item["internal_name"],
                    "missing_locales": missing,
                }
            )
        missing_descriptions = [locale for locale in locales if locale not in item["descriptions"]]
        if missing_descriptions:
            unknowns.append(
                {
                    "kind": "item_description",
                    "internal_name": item["internal_name"],
                    "missing_locales": missing_descriptions,
                }
            )
    return unknowns


def _ability_unknowns(
    abilities: list[dict[str, Any]],
    locales: tuple[str, ...],
) -> list[dict[str, Any]]:
    unknowns: list[dict[str, Any]] = []
    for ability in abilities:
        missing = [locale for locale in locales if locale not in ability["display_names"]]
        if missing:
            unknowns.append(
                {
                    "kind": "ability_display_name",
                    "internal_name": ability["internal_name"],
                    "missing_locales": missing,
                }
            )
        missing_descriptions = [
            locale for locale in locales if locale not in ability["descriptions"]
        ]
        if missing_descriptions:
            unknowns.append(
                {
                    "kind": "ability_description",
                    "internal_name": ability["internal_name"],
                    "missing_locales": missing_descriptions,
                }
            )
    return unknowns


def _load_export_inputs(
    game_data_dir: Path,
    patch: str,
    locales: Sequence[str] | None,
) -> tuple[Path, dict[str, Any], tuple[str, ...], dict[str, dict[str, Any]]]:
    patch_dir = game_data_dir / patch
    snapshot = _read_snapshot(patch_dir)
    selected_locales = _selected_locales(patch_dir, snapshot, locales)
    localizations = {
        locale: _read_json(patch_dir / "localization" / f"{locale}.json")
        for locale in selected_locales
    }
    return patch_dir, snapshot, selected_locales, localizations


def _resource_base(
    patch: str,
    snapshot: dict[str, Any],
    selected_locales: tuple[str, ...],
    *,
    resource_type: str,
) -> dict[str, Any]:
    return {
        "schema_version": IDENTITY_SCHEMA_VERSION,
        "resource_type": resource_type,
        "patch": patch,
        "generated_at": datetime.now(UTC).isoformat(),
        "generated_from": _generated_from(patch, snapshot),
        "locales": list(selected_locales),
    }


def _generated_from(patch: str, snapshot: dict[str, Any]) -> dict[str, Any]:
    return {
        "source": "invoker game-file snapshot",
        "source_patch": patch,
        "source_snapshot": {
            "kind": "invoker_snapshot",
            "metadata": _sanitized_snapshot_metadata(snapshot),
        },
    }


def _selected_locales(
    patch_dir: Path,
    snapshot: dict[str, Any],
    locales: Sequence[str] | None,
) -> tuple[str, ...]:
    if locales is not None:
        selected = list(locales)
    elif isinstance(snapshot.get("locales"), list):
        selected = [locale for locale in snapshot["locales"] if isinstance(locale, str)]
    elif isinstance(snapshot.get("locale"), str):
        selected = [snapshot["locale"]]
    else:
        selected = sorted(path.stem for path in (patch_dir / "localization").glob("*.json"))
    cleaned: list[str] = []
    for locale in selected:
        value = str(locale).strip()
        if not value:
            raise IdentityExportError("locale names must not be empty")
        if value not in cleaned:
            cleaned.append(value)
    if not cleaned:
        raise IdentityExportError(f"no localization files are available for {patch_dir}")
    for locale in cleaned:
        path = patch_dir / "localization" / f"{locale}.json"
        if not path.exists():
            raise IdentityExportError(f"missing localization file for locale={locale}: {path}")
    return tuple(cleaned)


def _sanitized_snapshot_metadata(snapshot: dict[str, Any]) -> dict[str, Any]:
    allowed = {
        "schema_version",
        "patch",
        "source",
        "source_format",
        "generated_at",
        "locale",
        "locales",
        "source_files",
        "files",
    }
    metadata = {key: snapshot[key] for key in allowed if key in snapshot}
    if "source" in metadata:
        metadata["source"] = "dota2npc extraction"
    return metadata


def _read_snapshot(patch_dir: Path) -> dict[str, Any]:
    raw = _read_json(patch_dir / "snapshot.json")
    if not isinstance(raw, dict):
        raise IdentityExportError(f"snapshot.json must be an object: {patch_dir}")
    return raw


def _read_json(path: Path) -> Any:
    if not path.exists():
        raise IdentityExportError(f"missing game snapshot file: {path}")
    return json.loads(path.read_text())


def _is_live_hero(raw: dict[str, Any]) -> bool:
    hero_id = raw.get("HeroID")
    enabled = raw.get("Enabled", "1")
    return hero_id not in (None, "", "0") and enabled != "0"


def _localized_hero_name(
    internal_name: str,
    raw: dict[str, Any],
    localization: dict[str, Any],
    *,
    locale: str,
) -> str | None:
    for key in (
        f"{internal_name}:n",
        f"DOTA_Tooltip_Hero_{internal_name}",
        f"dota_tooltip_hero_{internal_name}",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return value
    if locale == "english":
        value = localization.get(f"{internal_name}__en:n")
        if isinstance(value, str) and value:
            return value
        guide_name = raw.get("workshop_guide_name")
        return guide_name if isinstance(guide_name, str) and guide_name else None
    return None


def _hero_aliases(internal_name: str, localization: dict[str, Any]) -> list[str]:
    return _split_aliases(localization.get(f"{internal_name}__name_alias"))


def _localized_item_name(internal_name: str, localization: dict[str, Any]) -> str | None:
    for key in (
        f"DOTA_Tooltip_Ability_{internal_name}:n",
        f"DOTA_Tooltip_ability_{internal_name}:n",
        f"DOTA_Tooltip_ability_{internal_name}",
        f"DOTA_Tooltip_Ability_{internal_name}",
        f"DOTA_Tooltip_Item_{internal_name}",
        f"dota_tooltip_ability_{internal_name}",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _localized_item_description(internal_name: str, localization: dict[str, Any]) -> str | None:
    for key in (
        f"DOTA_Tooltip_ability_{internal_name}_Description",
        f"DOTA_Tooltip_Ability_{internal_name}_Description",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _item_aliases(internal_name: str, localization: dict[str, Any]) -> list[str]:
    return _dedupe(
        [
            *_split_aliases(localization.get(f"{internal_name}__name_alias")),
            *_split_aliases(localization.get(f"DOTA_SearchAlias_Ability_{internal_name}")),
        ]
    )


def _localized_ability_name(internal_name: str, localization: dict[str, Any]) -> str | None:
    for key in (
        f"DOTA_Tooltip_ability_{internal_name}",
        f"DOTA_Tooltip_Ability_{internal_name}",
        f"DOTA_Tooltip_Ability_{internal_name}:n",
        f"DOTA_Tooltip_ability_{internal_name}:n",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _localized_ability_description(
    internal_name: str,
    raw: dict[str, Any],
    localization: dict[str, Any],
) -> str | None:
    replacements = _ability_value_replacements(raw.get("AbilityValues"))
    for key in (
        f"DOTA_Tooltip_ability_{internal_name}_Description",
        f"DOTA_Tooltip_Ability_{internal_name}_Description",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return _resolve_percent_template(value, replacements)
    return None


def _ability_aliases(internal_name: str, localization: dict[str, Any]) -> list[str]:
    return _dedupe(
        [
            *_split_aliases(localization.get(f"{internal_name}__name_alias")),
            *_split_aliases(localization.get(f"DOTA_SearchAlias_Ability_{internal_name}")),
        ]
    )


def _split_aliases(raw: Any) -> list[str]:
    if not isinstance(raw, str):
        return []
    aliases: list[str] = []
    for token in raw.split(";"):
        alias = token.strip()
        if alias and alias not in aliases:
            aliases.append(alias)
    return aliases


def _dedupe(values: list[str]) -> list[str]:
    deduped: list[str] = []
    for value in values:
        if value and value not in deduped:
            deduped.append(value)
    return deduped


def _neutral_item_names(raw: dict[str, Any]) -> set[str]:
    names: set[str] = set()

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if isinstance(key, str) and key.startswith("item_"):
                    names.add(key)
                visit(child)
        elif isinstance(value, str) and value.startswith("item_"):
            names.add(value)

    visit(raw)
    return names


def _first_display_name(hero: dict[str, Any]) -> str | None:
    display_names = hero.get("display_names") or {}
    if not isinstance(display_names, dict):
        return None
    for locale in ("english", *sorted(display_names)):
        value = display_names.get(locale)
        if isinstance(value, str):
            return value
    return None


def _int_or_none(value: Any) -> int | None:
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return None


def _label_from_key(key: str) -> str:
    return key.replace("_", " ")


def _levels(value: Any) -> str | list[str]:
    if not isinstance(value, str):
        return str(value)
    parts = value.split()
    return parts if len(parts) > 1 else value


def _normalize(value: str) -> str:
    return "".join(char for char in value.casefold() if char.isalnum())
