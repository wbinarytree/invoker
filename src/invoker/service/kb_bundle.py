"""KB consumer-bundle export: `kb/<patch>/` trees inside a resource bundle.

Spec: docs/specs/2026-07-27-kb-exposure-service-and-bundle.md. The exported
tree is the data contract downstream consumers (phylactery) vendor; the
KnowledgeService ladder reads the same layout. Every artifact is loaded
through its sha binding before it is copied, so a drifted article fails the
export instead of shipping.
"""

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path

from invoker.corpus.registry import load_registry
from invoker.gen.artifacts import kb_fingerprint, load_entity_article

KB_INDEX_SCHEMA_VERSION = 1
KB_SOURCES_SCHEMA_VERSION = 1

# KB layout grammar: entity-class directory -> artifact kind. heroes/ joins
# when the hero generator lands.
KB_CLASS_KINDS = {"concepts": "concept", "items": "item"}
KB_KIND_CLASSES = {kind: class_dir for class_dir, kind in KB_CLASS_KINDS.items()}


class KbExportError(RuntimeError):
    """The KB tree cannot be exported as-is; nothing usable was written."""


@dataclass(frozen=True)
class _ScannedEntity:
    kind: str
    slug: str
    title: str
    identity_line: str
    entity_dir: Path
    article_file: str


@dataclass(frozen=True)
class KbExportReport:
    patch: str
    out_dir: Path
    kb_sha256: str
    counts: dict[str, int]


def _scan_kb(kb_source_dir: Path, patch: str) -> list[_ScannedEntity]:
    if not kb_source_dir.is_dir():
        raise KbExportError(f"KB directory does not exist: {kb_source_dir}")
    entities: list[_ScannedEntity] = []
    for class_dir in sorted(path for path in kb_source_dir.iterdir() if path.is_dir()):
        kind = KB_CLASS_KINDS.get(class_dir.name)
        if kind is None:
            raise KbExportError(
                f"KB entity class {class_dir.name!r} has no export support yet; "
                "extend KB_CLASS_KINDS and the index shape"
            )
        for entity_dir in sorted(path for path in class_dir.iterdir() if path.is_dir()):
            artifact, _body = load_entity_article(entity_dir / "artifact.json")
            if artifact.kind != kind:
                raise KbExportError(
                    f"{entity_dir}: artifact kind {artifact.kind!r} does not match "
                    f"its class directory {class_dir.name!r}"
                )
            if artifact.patch != patch:
                raise KbExportError(
                    f"{entity_dir}: artifact patch {artifact.patch!r} does not match "
                    f"the export patch {patch!r}"
                )
            entities.append(
                _ScannedEntity(
                    kind=kind,
                    slug=artifact.slug,
                    title=artifact.title,
                    identity_line=artifact.card.sentences[0].text,
                    entity_dir=entity_dir,
                    article_file=artifact.article_file,
                )
            )
    if not entities:
        raise KbExportError(f"KB directory has no artifacts: {kb_source_dir}")
    return entities


def build_kb_index(kb_source_dir: Path, patch: str) -> dict:
    """The consumer catalog: one entry per entity plus the KB content
    fingerprint, so a consumer can tell "KB changed" without diffing trees.
    Identity lines are the card's first sentence — the same summary the
    answerer index serves for select. Deliberately no timestamp: an export
    over an unchanged KB is byte-stable."""
    return _index_payload(_scan_kb(kb_source_dir, patch), kb_source_dir, patch)


def _index_payload(
    entities: list[_ScannedEntity], kb_source_dir: Path, patch: str
) -> dict:
    sha, count = kb_fingerprint(kb_source_dir)
    return {
        "schema_version": KB_INDEX_SCHEMA_VERSION,
        "patch": patch,
        "kb_sha256": sha,
        "artifact_count": count,
        "entries": [
            {
                "id": f"{entity.kind}/{entity.slug}",
                "kind": entity.kind,
                "slug": entity.slug,
                "title": entity.title,
                "identity_line": entity.identity_line,
            }
            for entity in entities
        ],
    }


def build_kb_sources(registry_path: Path | None = None) -> dict:
    """Corpus host metadata a consumer needs to render `corpus:` marks as
    pinned live links (`<page_base_url>index.php?oldid=<rev>#<anchor>`) with
    license attribution. Citations stay pointers — never page content."""
    registry = load_registry(registry_path)
    return {
        "schema_version": KB_SOURCES_SCHEMA_VERSION,
        "hosts": {
            key: {"page_base_url": host.page_base_url, "license": host.license}
            for key, host in sorted(registry.hosts.items())
        },
    }


def export_kb_bundle(
    kb_source_dir: Path,
    patch: str,
    bundle_root: Path,
    *,
    registry_path: Path | None = None,
) -> KbExportReport:
    """Write `kb/<patch>/` into a resource bundle root and record the patch
    in `bundle.json`. The target patch tree is replaced wholesale — it is
    derived output owned by this export."""
    entities = _scan_kb(kb_source_dir, patch)
    index = _index_payload(entities, kb_source_dir, patch)
    sources = build_kb_sources(registry_path)

    target = bundle_root / "kb" / patch
    if target.exists():
        shutil.rmtree(target)
    counts: dict[str, int] = {}
    for entity in entities:
        entity_target = target / KB_KIND_CLASSES[entity.kind] / entity.slug
        entity_target.mkdir(parents=True)
        for name in (entity.article_file, "artifact.json"):
            shutil.copyfile(entity.entity_dir / name, entity_target / name)
        counts[entity.kind] = counts.get(entity.kind, 0) + 1
    (target / "index.json").write_text(json.dumps(index, indent=2) + "\n")
    (target / "sources.json").write_text(json.dumps(sources, indent=2) + "\n")
    _record_kb_patch(bundle_root, patch)
    return KbExportReport(
        patch=patch,
        out_dir=target,
        kb_sha256=index["kb_sha256"],
        counts=counts,
    )


def _record_kb_patch(bundle_root: Path, patch: str) -> None:
    from invoker.service.core import BUNDLE_SCHEMA_VERSION

    path = bundle_root / "bundle.json"
    raw: dict = {}
    if path.exists():
        loaded = json.loads(path.read_text())
        if not isinstance(loaded, dict):
            raise KbExportError(f"bundle metadata must be a JSON object: {path}")
        raw = loaded
    schema = raw.get("schema_version")
    if schema is not None and not (
        isinstance(schema, int) and schema <= BUNDLE_SCHEMA_VERSION
    ):
        raise KbExportError(
            f"bundle metadata has unsupported schema_version={schema!r}: {path}"
        )
    raw["schema_version"] = BUNDLE_SCHEMA_VERSION
    for key in ("patches", "kb_patches"):
        values = {value for value in raw.get(key) or [] if isinstance(value, str)}
        values.add(patch)
        raw[key] = sorted(values)
    path.write_text(json.dumps(raw, indent=2) + "\n")
