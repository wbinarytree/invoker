from __future__ import annotations

import json
from functools import cached_property
from pathlib import Path

from invoker.graph import load_graph
from invoker.paths import manifest_file, summary_file
from invoker.pipeline.writer import read_hero
from invoker.schemas.derived import HeroDerived


class KnowledgeBase:
    def __init__(self, patch: str, bracket: str = "pro", *, data_dir: Path | None = None) -> None:
        from invoker.config import Config

        cfg = Config.load()
        self.patch = patch
        self.bracket = bracket
        self.data_dir = data_dir or cfg.data_dir
        self._heroes: dict[int, HeroDerived] = {}

    @cached_property
    def _manifest(self) -> dict:
        return json.loads(manifest_file(self.data_dir, self.patch).read_text())

    @cached_property
    def _graph(self):
        return load_graph(self.data_dir, self.patch)

    def patches(self) -> list[str]:
        root = self.data_dir / "derived"
        return sorted(p.name for p in root.iterdir() if p.is_dir()) if root.exists() else []

    def brackets(self) -> list[str]:
        for entry in self._manifest.get("heroes", []):
            return entry.get("brackets", [])
        return []

    def hero(self, key: int | str) -> HeroDerived:
        if isinstance(key, str):
            return self._by_name(key)
        if key not in self._heroes:
            self._heroes[key] = read_hero(self.data_dir, self.patch, key)
        return self._heroes[key]

    def _by_name(self, name: str) -> HeroDerived:
        for entry in self._manifest.get("heroes", []):
            h = self.hero(entry["hero_id"])
            if h.localized_name.lower() == name.lower():
                return h
        raise KeyError(f"hero not found: {name}")

    def synergies(self, key: int | str, *, min_confidence: str = "med") -> list:
        order = ["none", "low", "med", "high"]
        cutoff = order.index(min_confidence)
        return [
            e
            for e in self.hero(key).synergies.get(self.bracket, [])
            if order.index(e.confidence) >= cutoff
        ]

    def counters(self, key: int | str, *, min_confidence: str = "med") -> list:
        order = ["none", "low", "med", "high"]
        cutoff = order.index(min_confidence)
        return [
            e
            for e in self.hero(key).counters.get(self.bracket, [])
            if order.index(e.confidence) >= cutoff
        ]

    def neighbors(self, key: int | str, *, relation: str = "synergy", top_k: int = 5) -> list:
        h = self.hero(key)
        edges = (h.synergies if relation == "synergy" else h.counters).get(self.bracket, [])
        return edges[:top_k]

    def summary(self, key: int | str) -> str:
        hid = self.hero(key).hero_id
        return summary_file(self.data_dir, self.patch, self.bracket, hid).read_text()

    def by_tag(self, tag: str) -> list[HeroDerived]:
        results: list[HeroDerived] = []
        for entry in self._manifest.get("heroes", []):
            h = self.hero(entry["hero_id"])
            if tag in h.functional_tags:
                results.append(h)
        return results
