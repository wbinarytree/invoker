from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class FeatureEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str


class HeroFactFeature(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    score: float | None = None
    evidence: list[FeatureEvidence] = Field(default_factory=list)


class HeroFactProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")
    hero_id: int
    localized_name: str
    source_patch: str
    cohort: str
    capabilities: list[HeroFactFeature] = Field(default_factory=list)
    requirements: list[HeroFactFeature] = Field(default_factory=list)
    liabilities: list[HeroFactFeature] = Field(default_factory=list)
    targets: list[HeroFactFeature] = Field(default_factory=list)
    role_distribution: dict[str, float] = Field(default_factory=dict)
    provenance: dict = Field(default_factory=dict)


class RelationContext(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source_roles: list[str] = Field(default_factory=list)
    target_roles: list[str] = Field(default_factory=list)
    lane_context: str | None = None
    phase_context: str | None = None
    archetype_context: list[str] = Field(default_factory=list)


class RelationEvidenceMechanical(BaseModel):
    model_config = ConfigDict(extra="forbid")
    confidence: float
    basis: list[str] = Field(default_factory=list)


class RelationEvidenceStatistical(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str
    score: float | None = None
    games: int | None = None
    alignment: str


class RelationEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")
    mechanical: RelationEvidenceMechanical
    statistical: list[RelationEvidenceStatistical] = Field(default_factory=list)


class HeroRelation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    relation_id: str
    source_patch: str
    cohort: str
    from_hero_id: int
    to_hero_id: int
    relation_kind: str
    pattern: str
    source_feature: str
    target_feature: str
    mechanical_rationale: str
    context: RelationContext = Field(default_factory=RelationContext)
    evidence: RelationEvidence
    confidence: str
