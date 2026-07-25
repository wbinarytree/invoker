from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from invoker.gen.client import GenerationProvenance

CONCEPT_ARTIFACT_SCHEMA_VERSION = 1


class CardSentence(BaseModel):
    """One card sentence; every sentence carries at least one source mark
    (compression with pointers back — never marks-free prose)."""

    model_config = ConfigDict(extra="forbid")

    text: str
    marks: list[str] = Field(min_length=1)


class ConceptCard(BaseModel):
    model_config = ConfigDict(extra="forbid")

    entity: str
    sentences: list[CardSentence] = Field(min_length=1)


class ConceptArtifact(BaseModel):
    """One generated concept: article (evidence trail) + card (serving tier).

    `citations` lists every distinct mark used; all of them resolve against
    the context packet or generation fails — never against live sources.
    """

    model_config = ConfigDict(extra="forbid")

    schema_version: int = CONCEPT_ARTIFACT_SCHEMA_VERSION
    kind: str = "concept"
    slug: str
    title: str
    patch: str
    article_markdown: str
    card: ConceptCard
    citations: list[str]
    packet_sha256: str
    article_provenance: GenerationProvenance
    card_provenance: GenerationProvenance
