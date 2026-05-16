from __future__ import annotations

import json
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

IDENTITY_SCHEMA_VERSION = 1


class IdentityExportError(ValueError):
    pass


def export_identity_localization(
    game_data_dir: Path,
    patch: str,
    *,
    locales: Sequence[str] | None = None,
) -> dict[str, Any]:
    patch_dir = game_data_dir / patch
    snapshot = _read_snapshot(patch_dir)
    selected_locales = _selected_locales(patch_dir, snapshot, locales)
    localizations = {
        locale: _read_json(patch_dir / "localization" / f"{locale}.json")
        for locale in selected_locales
    }
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
        "generated_from": {
            "source": "invoker game-file snapshot",
            "source_patch": patch,
            "source_snapshot": {
                "kind": "invoker_snapshot",
                "metadata": _sanitized_snapshot_metadata(snapshot),
            },
        },
        "locales": list(selected_locales),
        "heroes": heroes,
        "items": items,
        "unknowns": unknowns,
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
            display_name = _localized_hero_name(
                internal_name, raw, localization, locale=locale
            )
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
        item_id = _int_or_none(raw.get("ID") or raw.get("ItemID"))
        if item_id is not None:
            entry["item_id"] = item_id
        if display_names or aliases:
            entry["sources"].append("localization")
        identities.append(entry)
    return identities


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
    return unknowns


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
        f"DOTA_Tooltip_ability_{internal_name}",
        f"DOTA_Tooltip_Ability_{internal_name}",
        f"DOTA_Tooltip_Item_{internal_name}",
        f"dota_tooltip_ability_{internal_name}",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _item_aliases(internal_name: str, localization: dict[str, Any]) -> list[str]:
    return _split_aliases(localization.get(f"{internal_name}__name_alias"))


def _split_aliases(raw: Any) -> list[str]:
    if not isinstance(raw, str):
        return []
    aliases: list[str] = []
    for token in raw.split(";"):
        alias = token.strip()
        if alias and alias not in aliases:
            aliases.append(alias)
    return aliases


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


def _normalize(value: str) -> str:
    return "".join(char for char in value.casefold() if char.isalnum())
