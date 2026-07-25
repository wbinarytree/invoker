from __future__ import annotations

import json
import re
from pathlib import Path

from invoker.corpus.schemas import (
    CorpusDoc,
    CorpusIndex,
    CorpusIndexPage,
)

_SLUG_PATTERN = re.compile(r"[^a-z0-9]+")


def page_slug(title: str) -> str:
    slug = _SLUG_PATTERN.sub("_", title.strip().lower()).strip("_")
    if not slug:
        raise ValueError(f"page title produces empty slug: {title!r}")
    return slug


class CorpusStore:
    """Revision-pinned corpus document storage.

    Layout:
        <root>/<host_key>/index.json
        <root>/<host_key>/<page_slug>/<revision_id>.json

    A new revision of a page is a new file; older revisions stay on disk so
    claims citing them remain resolvable after the page moves on.
    """

    def __init__(self, root: Path) -> None:
        self.root = root

    def host_dir(self, host_key: str) -> Path:
        return self.root / host_key

    def index_path(self, host_key: str) -> Path:
        return self.host_dir(host_key) / "index.json"

    def doc_path(self, host_key: str, slug: str, revision_id: int) -> Path:
        return self.host_dir(host_key) / slug / f"{revision_id}.json"

    def load_index(self, host_key: str) -> CorpusIndex:
        path = self.index_path(host_key)
        if not path.exists():
            return CorpusIndex(host_key=host_key)
        return CorpusIndex.model_validate_json(path.read_text())

    def has_revision(self, host_key: str, slug: str, revision_id: int) -> bool:
        return self.doc_path(host_key, slug, revision_id).exists()

    def write_doc(self, doc: CorpusDoc) -> Path:
        slug = page_slug(doc.resolved_title)
        path = self.doc_path(doc.host_key, slug, doc.revision_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(doc.model_dump_json(indent=2))

        index = self.load_index(doc.host_key)
        index.pages[slug] = CorpusIndexPage(
            requested_title=doc.requested_title,
            resolved_title=doc.resolved_title,
            latest_revision_id=doc.revision_id,
            retrieved_at=doc.retrieved_at,
            source_url=doc.source_url,
        )
        index_path = self.index_path(doc.host_key)
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(json.dumps(index.model_dump(), indent=2, sort_keys=True))
        return path
