from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class PositionBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")
    weights: dict[str, float]
    games: int
    window_days: int


class StatEdge(BaseModel):
    model_config = ConfigDict(extra="forbid")
    hero_id: int
    score: float | None
    games: int
    confidence: str
    source: str
    reason: str | None = None
    reason_provenance: dict | None = None


class MetaBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")
    contest_rate: float
    win_rate: float
    tier: str
    games: int


class MetaHistoryEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")
    patch: str
    bracket: str
    contest_rate: float
    win_rate: float
    tier: str


class TagSource(BaseModel):
    model_config = ConfigDict(extra="forbid")
    tag: str
    ability: str
    evidence: str


class Provenance(BaseModel):
    model_config = ConfigDict(extra="forbid")
    mechanical: dict
    statistical: dict


class HeroDerived(BaseModel):
    model_config = ConfigDict(extra="forbid")
    schema_version: int
    generator_version: str
    source_patch: str
    generated_at: str

    hero_id: int
    localized_name: str
    internal_name: str
    liquipedia_roles: list[str]

    functional_tags: list[str]
    tag_sources: list[TagSource]

    positions: dict[str, PositionBlock]
    synergies: dict[str, list[StatEdge]]
    counters: dict[str, list[StatEdge]]
    meta: dict[str, MetaBlock]
    meta_history: list[MetaHistoryEntry]

    provenance: Provenance
