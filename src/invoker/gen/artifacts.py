from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from invoker.gen.client import GenerationProvenance

ENTITY_ARTIFACT_SCHEMA_VERSION = 2


class CardSentence(BaseModel):
    """One card sentence; every sentence carries at least one source mark
    (compression with pointers back — never marks-free prose)."""

    model_config = ConfigDict(extra="forbid")

    text: str
    marks: list[str] = Field(min_length=1)


class EntityCard(BaseModel):
    model_config = ConfigDict(extra="forbid")

    entity: str
    sentences: list[CardSentence] = Field(min_length=1)


class EntityArtifact(BaseModel):
    """One generated entity (concept, item, hero): article (evidence
    trail) + card (serving tier).

    The article lives in a sibling markdown file (`article_file`) so the
    human-skim gate and archive diffs stay readable; `article_sha256` binds
    the two — consumers must verify it and refuse a drifted article.
    `citations` lists every distinct mark used; all of them resolve against
    the context packet or generation fails — never against live sources.
    """

    model_config = ConfigDict(extra="forbid")

    schema_version: int = ENTITY_ARTIFACT_SCHEMA_VERSION
    kind: Literal["concept", "item", "hero"]
    slug: str
    title: str
    patch: str
    article_file: str
    article_sha256: str
    card: EntityCard
    citations: list[str]
    packet_sha256: str
    article_provenance: GenerationProvenance
    card_provenance: GenerationProvenance
