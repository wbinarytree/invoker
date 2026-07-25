from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, model_validator

CORPUS_DOC_SCHEMA_VERSION = 1
CORPUS_INDEX_SCHEMA_VERSION = 1


class CorpusDoc(BaseModel):
    """One fetched wiki page pinned to a specific revision."""

    model_config = ConfigDict(extra="forbid")

    schema_version: int = CORPUS_DOC_SCHEMA_VERSION
    doc_id: str
    host_key: str
    requested_title: str
    resolved_title: str
    page_id: int
    revision_id: int
    revision_timestamp: str
    content_format: str = "wikitext"
    content: str
    source_url: str
    license: str
    retrieved_at: str
    patch_context: str | None = None


class OmittedPage(BaseModel):
    """A page deliberately not fetched. The reason is mandatory: omissions
    must stay auditable, not silent."""

    model_config = ConfigDict(extra="forbid")

    title: str
    reason: str = Field(min_length=1)


class OmitRule(BaseModel):
    """A whole class of pages deliberately not fetched, matched by title
    prefix (e.g. Liquipedia's `Archive:` namespace). Same auditability rule:
    the reason is mandatory."""

    model_config = ConfigDict(extra="forbid")

    prefix: str = Field(min_length=1)
    reason: str = Field(min_length=1)


class CorpusHost(BaseModel):
    """One MediaWiki host plus the curated page list to fetch from it."""

    model_config = ConfigDict(extra="forbid")

    api_url: str
    page_base_url: str
    license: str
    max_requests_per_minute: int = Field(default=20, gt=0)
    # action=parse is the expensive API mode; Liquipedia asks ~1 call / 30s.
    max_parse_requests_per_minute: int = Field(default=2, gt=0)
    pages: list[str] = Field(min_length=1)
    coverage_categories: list[str] = Field(default_factory=list)
    omit: list[OmittedPage] = Field(default_factory=list)
    omit_prefixes: list[OmitRule] = Field(default_factory=list)

    @model_validator(mode="after")
    def _pages_and_omit_disjoint(self) -> CorpusHost:
        overlap = {page.title for page in self.omit} & set(self.pages)
        if overlap:
            raise ValueError(f"titles listed in both pages and omit: {sorted(overlap)}")
        return self


class CorpusRegistry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: int
    hosts: dict[str, CorpusHost] = Field(min_length=1)


class CorpusIndexPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    requested_title: str
    resolved_title: str
    latest_revision_id: int
    retrieved_at: str
    source_url: str


class CorpusIndex(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: int = CORPUS_INDEX_SCHEMA_VERSION
    host_key: str
    pages: dict[str, CorpusIndexPage] = Field(default_factory=dict)
