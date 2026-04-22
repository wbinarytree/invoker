from __future__ import annotations

import json
from collections import defaultdict
from collections.abc import Iterable
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field

from invoker.kg.schemas import HeroRelation


class RelationsFile(BaseModel):
    model_config = ConfigDict(extra="forbid")
    schema_version: int = 2
    source_patch: str
    generated_at: str
    relations: list[HeroRelation] = Field(default_factory=list)


class RelationsReader:
    """In-memory index over a relations.json file.

    Relations are directional records: from_hero_id → to_hero_id. A single
    pair typically produces several records (one per rule that fired).
    """

    def __init__(self, relations: Iterable[HeroRelation]) -> None:
        self._relations: list[HeroRelation] = list(relations)
        self._by_from: dict[int, list[HeroRelation]] = defaultdict(list)
        self._by_to: dict[int, list[HeroRelation]] = defaultdict(list)
        self._by_pattern: dict[str, list[HeroRelation]] = defaultdict(list)
        for r in self._relations:
            self._by_from[r.from_hero_id].append(r)
            self._by_to[r.to_hero_id].append(r)
            self._by_pattern[r.pattern].append(r)

    @classmethod
    def load(cls, path: Path) -> RelationsReader:
        file = RelationsFile.model_validate_json(path.read_text())
        return cls(file.relations)

    def all(self) -> list[HeroRelation]:
        return list(self._relations)

    def relations_from(self, hero_id: int) -> list[HeroRelation]:
        return list(self._by_from.get(hero_id, []))

    def relations_to(self, hero_id: int) -> list[HeroRelation]:
        return list(self._by_to.get(hero_id, []))

    def relations_for(self, hero_id: int) -> list[HeroRelation]:
        seen: dict[str, HeroRelation] = {}
        for r in self._by_from.get(hero_id, []):
            seen[r.relation_id] = r
        for r in self._by_to.get(hero_id, []):
            seen[r.relation_id] = r
        return list(seen.values())

    def relations_between(self, a: int, b: int) -> list[HeroRelation]:
        out: list[HeroRelation] = []
        for r in self._by_from.get(a, []):
            if r.to_hero_id == b:
                out.append(r)
        for r in self._by_from.get(b, []):
            if r.to_hero_id == a:
                out.append(r)
        return out

    def synergies_with(self, hero_id: int) -> list[HeroRelation]:
        return [r for r in self.relations_for(hero_id) if r.relation_kind == "synergy"]

    def counters_of(self, hero_id: int) -> list[HeroRelation]:
        return [r for r in self._by_to.get(hero_id, []) if r.relation_kind == "counter"]

    def countered_by(self, hero_id: int) -> list[HeroRelation]:
        return [r for r in self._by_from.get(hero_id, []) if r.relation_kind == "counter"]

    def relations_by_pattern(self, pattern: str) -> list[HeroRelation]:
        return list(self._by_pattern.get(pattern, []))


def write_relations(
    path: Path,
    relations: Iterable[HeroRelation],
    *,
    source_patch: str,
    generated_at: str,
    schema_version: int = 2,
) -> None:
    file = RelationsFile(
        schema_version=schema_version,
        source_patch=source_patch,
        generated_at=generated_at,
        relations=list(relations),
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(file.model_dump(mode="json"), indent=2, sort_keys=False))
