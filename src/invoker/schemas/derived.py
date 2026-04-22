from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from invoker.kg.schemas import FactProvenance, HeroFactFeature


class HeroDerived(BaseModel):
    model_config = ConfigDict(extra="forbid")
    schema_version: int = 2
    generator_version: str
    source_patch: str
    generated_at: str

    hero_id: int
    hero_slug: str | None = None
    localized_name: str

    capabilities: list[HeroFactFeature] = Field(default_factory=list)
    requirements: list[HeroFactFeature] = Field(default_factory=list)
    liabilities: list[HeroFactFeature] = Field(default_factory=list)
    targets: list[HeroFactFeature] = Field(default_factory=list)
    role_distribution: dict[str, float] = Field(default_factory=dict)

    provenance: FactProvenance
