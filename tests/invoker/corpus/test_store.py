import json

import pytest

from invoker.corpus.schemas import CorpusDoc
from invoker.corpus.store import CorpusStore, page_slug


def make_doc(revision_id: int = 100, title: str = "Attack Speed") -> CorpusDoc:
    slug = page_slug(title)
    return CorpusDoc(
        doc_id=f"liquipedia_dota2:{slug}@{revision_id}",
        host_key="liquipedia_dota2",
        requested_title=title,
        resolved_title=title,
        page_id=7,
        revision_id=revision_id,
        revision_timestamp="2026-07-01T00:00:00Z",
        content="{{Infobox}} wikitext body",
        source_url="https://liquipedia.net/dota2/Attack_Speed",
        license="CC-BY-SA 3.0",
        retrieved_at="2026-07-25T00:00:00Z",
        patch_context="7.41d",
    )


def test_page_slug_normalizes_titles():
    assert page_slug("Attack Speed") == "attack_speed"
    assert page_slug("Pseudo-random Distribution") == "pseudo_random_distribution"
    with pytest.raises(ValueError):
        page_slug("///")


def test_write_doc_creates_revision_pinned_file_and_index(tmp_path):
    store = CorpusStore(tmp_path)
    doc = make_doc()
    path = store.write_doc(doc)

    assert path == tmp_path / "liquipedia_dota2" / "attack_speed" / "100.json"
    assert store.has_revision("liquipedia_dota2", "attack_speed", 100)
    stored = CorpusDoc.model_validate_json(path.read_text())
    assert stored == doc

    index = store.load_index("liquipedia_dota2")
    assert index.pages["attack_speed"].latest_revision_id == 100
    raw_index = json.loads(store.index_path("liquipedia_dota2").read_text())
    assert raw_index["host_key"] == "liquipedia_dota2"


def test_new_revision_keeps_old_file_and_updates_index(tmp_path):
    store = CorpusStore(tmp_path)
    store.write_doc(make_doc(revision_id=100))
    store.write_doc(make_doc(revision_id=101))

    assert store.has_revision("liquipedia_dota2", "attack_speed", 100)
    assert store.has_revision("liquipedia_dota2", "attack_speed", 101)
    index = store.load_index("liquipedia_dota2")
    assert index.pages["attack_speed"].latest_revision_id == 101
