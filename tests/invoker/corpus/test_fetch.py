import httpx
import pytest

from invoker.corpus.fetch import CorpusFetchError, fetch_corpus, source_page_url
from invoker.corpus.registry import load_registry
from invoker.corpus.schemas import CorpusDoc, CorpusHost, CorpusRegistry
from invoker.corpus.store import CorpusStore


def make_registry() -> CorpusRegistry:
    return CorpusRegistry(
        schema_version=1,
        hosts={
            "testwiki": CorpusHost(
                api_url="https://example.test/api.php",
                page_base_url="https://example.test/",
                license="CC-BY-SA 3.0",
                max_requests_per_minute=6000,
                pages=["Armor", "Ghost Page"],
            )
        },
    )


def make_transport(revid: int) -> httpx.MockTransport:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "query": {
                    "pages": [
                        {
                            "pageid": 1,
                            "ns": 0,
                            "title": "Armor",
                            "revisions": [
                                {
                                    "revid": revid,
                                    "timestamp": "2026-07-01T00:00:00Z",
                                    "slots": {"main": {"content": "armor wikitext"}},
                                }
                            ],
                        },
                        {"ns": 0, "title": "Ghost Page", "missing": True},
                    ]
                }
            },
        )

    return httpx.MockTransport(handler)


def test_fetch_corpus_writes_docs_and_reports_missing(tmp_path):
    store = CorpusStore(tmp_path)
    reports = fetch_corpus(
        make_registry(),
        store,
        patch_context="7.41d",
        transport=make_transport(100),
    )

    assert len(reports) == 1
    report = reports[0]
    assert report.fetched == ["armor"]
    assert report.unchanged == []
    assert report.missing == ["Ghost Page (missing)"]

    doc_path = store.doc_path("testwiki", "armor", 100)
    doc = CorpusDoc.model_validate_json(doc_path.read_text())
    assert doc.doc_id == "testwiki:armor@100"
    assert doc.patch_context == "7.41d"
    assert doc.source_url == "https://example.test/Armor"
    assert doc.license == "CC-BY-SA 3.0"


def test_fetch_corpus_skips_known_revisions_and_writes_new_ones(tmp_path):
    store = CorpusStore(tmp_path)
    registry = make_registry()

    fetch_corpus(registry, store, transport=make_transport(100))
    second = fetch_corpus(registry, store, transport=make_transport(100))
    assert second[0].fetched == []
    assert second[0].unchanged == ["armor"]

    third = fetch_corpus(registry, store, transport=make_transport(101))
    assert third[0].fetched == ["armor"]
    assert store.has_revision("testwiki", "armor", 100)
    assert store.has_revision("testwiki", "armor", 101)
    assert store.load_index("testwiki").pages["armor"].latest_revision_id == 101


def test_fetch_corpus_unknown_host_fails_loudly(tmp_path):
    with pytest.raises(CorpusFetchError, match="unknown corpus host"):
        fetch_corpus(make_registry(), CorpusStore(tmp_path), only_host="nope")


def test_source_page_url_quotes_spaces():
    assert (
        source_page_url("https://liquipedia.net/dota2/", "Pseudo-random Distribution")
        == "https://liquipedia.net/dota2/Pseudo-random_Distribution"
    )


def test_packaged_registry_is_fetchable_shape():
    registry = load_registry()
    host = registry.hosts["liquipedia_dota2"]
    assert source_page_url(host.page_base_url, host.pages[0]).startswith(
        "https://liquipedia.net/dota2/"
    )
