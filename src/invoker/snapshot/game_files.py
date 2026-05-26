from __future__ import annotations

import json
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from invoker.snapshot.kv import parse_kv1_file


class SnapshotError(ValueError):
    pass


@dataclass(frozen=True)
class SnapshotResult:
    patch_dir: Path
    hero_count: int
    ability_count: int
    item_count: int
    neutral_item_count: int
    locales: tuple[str, ...]


def snapshot_game_files(
    source: Path,
    out_dir: Path,
    patch: str,
    *,
    localization: Path | None = None,
    locale: str = "english",
    locales: Sequence[str] | None = None,
) -> SnapshotResult:
    """Translate pre-extracted Dota NPC KV files into the JSON snapshot contract."""
    npc_dir = _resolve_npc_dir(source)
    selected_locales = _selected_locales(locale=locale, locales=locales)
    if localization is not None and len(selected_locales) != 1:
        raise SnapshotError("--localization can only be used with one --locale value")
    heroes_raw = _root(parse_kv1_file(npc_dir / "npc_heroes.txt"), "DOTAHeroes")
    abilities_raw = _load_abilities(npc_dir)
    ability_ids = _load_ability_ids(npc_dir)
    _merge_source_ids(abilities_raw, ability_ids)
    items_raw = _load_optional_root(npc_dir / "items.txt", "DOTAAbilities")
    neutral_items_raw = _load_optional_root(npc_dir / "neutral_items.txt", "neutral_items")
    localizations: dict[str, dict[str, str]] = {}
    localization_sources: dict[str, list[Path]] = {}
    for selected_locale in selected_locales:
        if localization is not None:
            files = [localization]
        else:
            files = _discover_localization_files(source, npc_dir, selected_locale)
        localization_sources[selected_locale] = files
        localizations[selected_locale] = _load_localization_files(files)

    heroes = {
        name: block
        for name, block in heroes_raw.items()
        if name.startswith("npc_dota_hero_")
        and name != "npc_dota_hero_base"
        and isinstance(block, dict)
    }
    hero_abilities = {name: _extract_hero_abilities(block) for name, block in heroes.items()}
    items = {
        name: block
        for name, block in items_raw.items()
        if name.startswith("item_") and isinstance(block, dict)
    }
    _merge_source_ids(items, ability_ids)

    patch_dir = out_dir / patch
    localization_dir = patch_dir / "localization"
    localization_dir.mkdir(parents=True, exist_ok=True)

    _write_json(patch_dir / "heroes.json", heroes)
    _write_json(patch_dir / "abilities.json", abilities_raw)
    _write_json(patch_dir / "hero_abilities.json", hero_abilities)
    _write_json(patch_dir / "items.json", items)
    _write_json(patch_dir / "neutral_items.json", neutral_items_raw)
    for selected_locale, localization_raw in localizations.items():
        _write_json(localization_dir / f"{selected_locale}.json", localization_raw)
    _write_json(
        patch_dir / "snapshot.json",
        {
            "schema_version": 1,
            "patch": patch,
            "source": "dota2npc extraction",
            "source_format": "pre-extracted-vpk-kv1",
            "generated_at": datetime.now(UTC).isoformat(),
            "locale": selected_locales[0],
            "locales": list(selected_locales),
            "source_files": _source_files(source, npc_dir, localization_sources),
            "localization_sources": {
                selected_locale: [_safe_source_path(source, path) for path in files]
                for selected_locale, files in localization_sources.items()
            },
            "files": {
                "heroes": "heroes.json",
                "abilities": "abilities.json",
                "hero_abilities": "hero_abilities.json",
                "items": "items.json",
                "neutral_items": "neutral_items.json",
                "localization": {
                    selected_locale: f"localization/{selected_locale}.json"
                    for selected_locale in selected_locales
                },
            },
        },
    )

    return SnapshotResult(
        patch_dir=patch_dir,
        hero_count=len(heroes),
        ability_count=len(abilities_raw),
        item_count=len(items),
        neutral_item_count=len(neutral_items_raw),
        locales=selected_locales,
    )


def _selected_locales(*, locale: str, locales: Sequence[str] | None) -> tuple[str, ...]:
    raw = list(locales) if locales is not None else [locale]
    selected: list[str] = []
    for value in raw:
        cleaned = str(value).strip()
        if not cleaned:
            raise SnapshotError("locale names must not be empty")
        if cleaned not in selected:
            selected.append(cleaned)
    return tuple(selected)


def _resolve_npc_dir(source: Path) -> Path:
    if (source / "npc_heroes.txt").exists():
        return source
    if (source / "npc" / "npc_heroes.txt").exists():
        return source / "npc"
    raise SnapshotError(f"{source} does not contain npc_heroes.txt or npc/npc_heroes.txt")


def _load_abilities(npc_dir: Path) -> dict[str, Any]:
    abilities = _root(parse_kv1_file(npc_dir / "npc_abilities.txt"), "DOTAAbilities")
    hero_dir = npc_dir / "heroes"
    if hero_dir.exists():
        for path in sorted(hero_dir.glob("npc_dota_hero_*.txt")):
            abilities.update(_root(parse_kv1_file(path), "DOTAAbilities"))
    return {
        name: block
        for name, block in abilities.items()
        if name != "Version" and isinstance(block, dict)
    }


def _load_ability_ids(npc_dir: Path) -> dict[str, str]:
    path = npc_dir / "npc_ability_ids.txt"
    if not path.exists():
        return {}
    root = _root(parse_kv1_file(path), "DOTAAbilityIDs")
    ids: dict[str, str] = {}
    for section_name in ("UnitAbilities", "ItemAbilities"):
        section = root.get(section_name)
        if isinstance(section, dict):
            _collect_ability_ids(section, ids)
    return ids


def _collect_ability_ids(block: dict[str, Any], ids: dict[str, str]) -> None:
    for key, value in block.items():
        if isinstance(value, str):
            ids[str(key)] = value
        elif isinstance(value, dict):
            _collect_ability_ids(value, ids)


def _merge_source_ids(records: dict[str, Any], ability_ids: dict[str, str]) -> None:
    for name, block in records.items():
        if not isinstance(block, dict) or "ID" in block:
            continue
        source_id = ability_ids.get(name)
        if source_id is not None:
            block["ID"] = source_id


def _load_optional_root(path: Path, root_key: str) -> dict[str, Any]:
    if not path.exists():
        return {}
    return _root(parse_kv1_file(path), root_key)


def _discover_localization_files(source: Path, npc_dir: Path, locale: str) -> list[Path]:
    roots = [
        source / "resource" / "localization",
        npc_dir.parent / "resource" / "localization",
    ]
    names = [
        f"abilities_{locale}.txt",
        f"items_{locale}.txt",
        f"dota_{locale}.txt",
    ]
    paths: list[Path] = []
    for root in roots:
        for name in names:
            path = root / name
            if path.exists() and path not in paths:
                paths.append(path)
    return paths


def _source_files(
    source: Path,
    npc_dir: Path,
    localization_sources: dict[str, list[Path]],
) -> dict[str, Any]:
    files: dict[str, Any] = {
        "heroes": _safe_source_path(source, npc_dir / "npc_heroes.txt"),
        "abilities": [_safe_source_path(source, path) for path in _ability_source_paths(npc_dir)],
    }
    ability_ids_path = npc_dir / "npc_ability_ids.txt"
    if ability_ids_path.exists():
        files["ability_ids"] = _safe_source_path(source, ability_ids_path)
    for name in ("items.txt", "neutral_items.txt"):
        path = npc_dir / name
        if path.exists():
            files[name.removesuffix(".txt")] = _safe_source_path(source, path)
    files["localization"] = {
        locale: [_safe_source_path(source, path) for path in paths]
        for locale, paths in localization_sources.items()
    }
    return files


def _ability_source_paths(npc_dir: Path) -> list[Path]:
    paths = [npc_dir / "npc_abilities.txt"]
    hero_dir = npc_dir / "heroes"
    if hero_dir.exists():
        paths.extend(sorted(hero_dir.glob("npc_dota_hero_*.txt")))
    return [path for path in paths if path.exists()]


def _safe_source_path(source: Path, path: Path) -> str:
    for root in (source, source / "npc", source.parent):
        try:
            return path.relative_to(root).as_posix()
        except ValueError:
            continue
    return path.name


def _load_localization_files(paths: list[Path]) -> dict[str, str]:
    tokens: dict[str, str] = {}
    for path in paths:
        tokens.update(_load_localization(path))
    return tokens


def _load_localization(path: Path) -> dict[str, str]:
    parsed = parse_kv1_file(path)
    root = next(iter(parsed.values())) if len(parsed) == 1 else parsed
    if isinstance(root, dict) and "Tokens" in root and isinstance(root["Tokens"], dict):
        root = root["Tokens"]
    if not isinstance(root, dict):
        raise SnapshotError(f"{path} does not contain a KV localization object")
    return {str(k): str(v) for k, v in root.items() if isinstance(v, str)}


def _root(parsed: dict[str, Any], root_key: str) -> dict[str, Any]:
    root = parsed.get(root_key)
    if not isinstance(root, dict):
        raise SnapshotError(f"missing KV root {root_key!r}")
    return root


def _extract_hero_abilities(hero: dict[str, Any]) -> dict[str, Any]:
    talent_start = _int_or_default(hero.get("AbilityTalentStart"), 10)
    abilities: list[str] = []
    talents: list[dict[str, Any]] = []
    for key, value in sorted(hero.items(), key=lambda item: _ability_sort_key(item[0])):
        if not key.startswith("Ability") or key == "AbilityTalentStart":
            continue
        index = _ability_index(key)
        if index is None or not isinstance(value, str) or not value:
            continue
        if index >= talent_start or value.startswith("special_bonus_"):
            level = ((max(index, talent_start) - talent_start) // 2) + 1
            talents.append({"name": value, "level": level})
        else:
            abilities.append(value)
    return {"abilities": abilities, "talents": talents}


def _ability_sort_key(key: str) -> tuple[int, str]:
    index = _ability_index(key)
    return (index if index is not None else 10_000, key)


def _ability_index(key: str) -> int | None:
    suffix = key.removeprefix("Ability")
    if not suffix.isdigit():
        return None
    return int(suffix)


def _int_or_default(value: Any, default: int) -> int:
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return default


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
