from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

from invoker.gen.client import GenerationError, GenerationProvenance

ENTITY_ARTIFACT_SCHEMA_VERSION = 3


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

    On disk the entity is a SKILL.md-style markdown file (`article_file`):
    YAML frontmatter carrying title/kind/patch and the card, then the
    article body — the card is readable and distinguishable at a glance.
    `artifact.json` holds everything else (citations, hashes, provenance)
    and deliberately not the card, so each fact has one home.
    `article_sha256` binds the whole markdown file (frontmatter included) —
    consumers must verify it and refuse a drifted file. `citations` lists
    every distinct article mark; all marks resolve against the context
    packet or generation fails — never against live sources.
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


def kb_fingerprint(kb_dir: Path) -> tuple[str, int]:
    """Content hash over every file in the KB archive plus the artifact
    count — the record of exactly which KB state a report or export saw."""
    digest = hashlib.sha256()
    count = 0
    if kb_dir.is_dir():
        for path in sorted(kb_dir.rglob("*")):
            if path.is_file():
                digest.update(str(path.relative_to(kb_dir)).encode())
                digest.update(path.read_bytes())
                if path.name == "artifact.json":
                    count += 1
    return digest.hexdigest(), count


def persist_rejected(
    rejected_dir: Path | None,
    *,
    kind: str,
    slug: str,
    article_text: str,
    card: EntityCard | None,
    error: Exception,
) -> Path | None:
    """Persist paid-for output that will not become an artifact — the
    article (and card, when one exists) plus the error text — so an abort
    never discards what the tokens bought. Returns the directory written,
    or None when persistence is off (no rejected_dir)."""
    if rejected_dir is None:
        return None
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S.%f")
    target = rejected_dir / kind / slug / stamp
    target.mkdir(parents=True, exist_ok=True)
    (target / "article.md").write_text(article_text)
    if card is not None:
        (target / "card.json").write_text(card.model_dump_json(indent=2))
    (target / "error.txt").write_text(f"{type(error).__name__}: {error}\n")
    return target


def article_file_text(*, title: str, kind: str, patch: str, card: EntityCard, body: str) -> str:
    """Compose the on-disk markdown: frontmatter (identity + card) + body."""
    front = yaml.safe_dump(
        {
            "title": title,
            "kind": kind,
            "patch": patch,
            "card": card.model_dump(),
        },
        sort_keys=False,
        allow_unicode=True,
    )
    return f"---\n{front}---\n\n{body}"


def _parse_article_file(text: str, slug: str) -> tuple[dict[str, Any], EntityCard, str]:
    if not text.startswith("---\n"):
        raise GenerationError(f"{slug}: article file has no frontmatter; regenerate")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise GenerationError(f"{slug}: article frontmatter is unterminated; regenerate")
    meta = yaml.safe_load(text[4 : end + 1])
    if not isinstance(meta, dict) or "card" not in meta:
        raise GenerationError(f"{slug}: article frontmatter carries no card; regenerate")
    card = EntityCard.model_validate(meta["card"])
    body = text[end + len("\n---\n") :].lstrip("\n")
    return meta, card, body


def write_entity_artifact(entity_dir: Path, artifact: EntityArtifact, file_text: str) -> Path:
    """Write the artifact pair: article_file (frontmatter + body, the text
    `article_sha256` was computed over) and artifact.json without the card."""
    entity_dir.mkdir(parents=True, exist_ok=True)
    (entity_dir / artifact.article_file).write_text(file_text)
    path = entity_dir / "artifact.json"
    path.write_text(artifact.model_dump_json(indent=2, exclude={"card"}))
    return path


def load_entity_article(artifact_path: Path) -> tuple[EntityArtifact, str]:
    """Load an artifact and its article body, verifying the sha binding.

    A hand-edited or drifted article file fails loudly — artifacts are
    regenerated, never patched in place."""
    payload = json.loads(artifact_path.read_text())
    slug = str(payload.get("slug", artifact_path.parent.name))
    if payload.get("schema_version") != ENTITY_ARTIFACT_SCHEMA_VERSION:
        raise GenerationError(
            f"{slug}: artifact schema {payload.get('schema_version')} != "
            f"{ENTITY_ARTIFACT_SCHEMA_VERSION}; regenerate"
        )
    file_text = (artifact_path.parent / str(payload["article_file"])).read_text()
    digest = hashlib.sha256(file_text.encode()).hexdigest()
    if digest != payload["article_sha256"]:
        raise GenerationError(
            f"{slug}: article file drifted from its artifact (sha mismatch); regenerate"
        )
    meta, card, body = _parse_article_file(file_text, slug)
    for field in ("title", "kind", "patch"):
        if meta.get(field) != payload.get(field):
            raise GenerationError(
                f"{slug}: frontmatter {field} {meta.get(field)!r} does not match "
                f"artifact.json {payload.get(field)!r}; regenerate"
            )
    artifact = EntityArtifact.model_validate({**payload, "card": card})
    return artifact, body
