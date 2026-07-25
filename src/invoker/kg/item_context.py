from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from invoker.kg.ability_context import AttribEntry
from invoker.sources.game_files import GameFilesSource


class ItemConstantsSource(Protocol):
    """Constants surface needed to assemble an item context."""

    def item_records(self) -> dict[str, Any]: ...


class ItemNotFoundError(ValueError):
    pass


@dataclass(frozen=True)
class ItemContext:
    """Source-grounded static context for one item at a given patch."""

    patch: str
    internal_name: str
    name: str
    cost: int | None
    recipe_cost: int | None
    quality: str | None
    behavior: list[str]
    damage_type: str | None
    dispellable: str | None
    description: str | None
    lore: str | None
    attribs: list[AttribEntry]
    components: list[str] | None
    component_names: list[str] | None
    cast_range: str | list[str] | None = None
    mana_cost: str | list[str] | None = None
    cooldown: str | list[str] | None = None


def build_item_context(game_data_dir: Path, item: str, *, patch: str) -> ItemContext:
    """Assemble an ItemContext from game-file snapshot data.

    item: internal name (with or without the item_ prefix) or localized name.
    """
    source = GameFilesSource(game_data_dir, patch)
    return build_item_context_from_source(source, item, patch=patch)


def build_item_context_from_source(
    source: ItemConstantsSource,
    item: str,
    *,
    patch: str,
) -> ItemContext:
    records = source.item_records()
    internal_name, record = _find_item(records, item)
    attribs = [
        AttribEntry(
            header=str(a["header"]),
            value=a.get("value"),
            key=str(a["key"]) if "key" in a else None,
            scepter_bonus=a.get("scepter_bonus"),
            shard_bonus=a.get("shard_bonus"),
            percent=bool(a.get("percent")),
        )
        for a in record.get("attrib", [])
        if isinstance(a, dict) and "header" in a
    ]
    return ItemContext(
        patch=patch,
        internal_name=internal_name,
        name=str(record.get("dname", internal_name)),
        cost=record.get("cost"),
        recipe_cost=record.get("recipe_cost"),
        quality=record.get("quality"),
        behavior=list(record.get("behavior", [])),
        damage_type=record.get("dmg_type") or None,
        dispellable=record.get("dispellable") or None,
        description=record.get("desc") or None,
        lore=record.get("lore") or None,
        attribs=attribs,
        components=record.get("components"),
        component_names=record.get("component_names"),
        cast_range=record.get("cast_range"),
        mana_cost=record.get("mc"),
        cooldown=record.get("cd"),
    )


def _find_item(records: dict[str, Any], item: str) -> tuple[str, dict[str, Any]]:
    token = item.strip().lower()
    for internal_name, record in records.items():
        candidates = {
            internal_name.lower(),
            internal_name.removeprefix("item_").lower(),
            str(record.get("dname", "")).lower(),
        }
        if token in candidates:
            return internal_name, record
    raise ItemNotFoundError(f"item {item!r} not found in game-file snapshot")
