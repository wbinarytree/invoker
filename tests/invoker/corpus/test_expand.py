import httpx
import pytest

from invoker.corpus.expand import expand_corpus
from invoker.corpus.mediawiki import MediaWikiClient, MediaWikiError
from invoker.corpus.schemas import CorpusDoc, CorpusHost, CorpusRegistry
from invoker.corpus.store import CorpusStore, page_slug


def make_registry() -> CorpusRegistry:
    return CorpusRegistry(
        schema_version=1,
        hosts={
            "testwiki": CorpusHost(
                api_url="https://example.test/api.php",
                page_base_url="https://example.test/",
                license="CC-BY-SA 3.0",
                max_requests_per_minute=6000,
                max_parse_requests_per_minute=6000,
                pages=["Armor", "Evasion"],
            )
        },
    )


def seed_doc(store: CorpusStore, title: str, revision_id: int) -> None:
    slug = page_slug(title)
    store.write_doc(
        CorpusDoc(
            doc_id=f"testwiki:{slug}@{revision_id}",
            host_key="testwiki",
            requested_title=title,
            resolved_title=title,
            page_id=1,
            revision_id=revision_id,
            revision_timestamp="2026-07-01T00:00:00Z",
            content=f"{title} wikitext {{{{G|some variable}}}}",
            source_url=f"https://example.test/{title}",
            license="CC-BY-SA 3.0",
            retrieved_at="2026-07-25T00:00:00Z",
        )
    )


@pytest.mark.asyncio
async def test_fetch_expanded_html_uses_oldid_and_parse_bucket():
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"parse": {"title": "Evasion", "text": "<p>25%</p>"}})

    client = MediaWikiClient(
        "https://example.test/api.php",
        user_agent="invoker-test/0",
        parse_requests_per_minute=6000,
        transport=httpx.MockTransport(handler),
    )
    try:
        html = await client.fetch_expanded_html(2383969)
    finally:
        await client.close()

    assert html == "<p>25%</p>"
    assert seen[0].url.params["action"] == "parse"
    assert seen[0].url.params["oldid"] == "2383969"


@pytest.mark.asyncio
async def test_fetch_expanded_html_surfaces_api_error():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"error": {"info": "There is no revision with ID 1."}})

    client = MediaWikiClient(
        "https://example.test/api.php",
        user_agent="invoker-test/0",
        parse_requests_per_minute=6000,
        transport=httpx.MockTransport(handler),
    )
    try:
        with pytest.raises(MediaWikiError, match="no revision with ID"):
            await client.fetch_expanded_html(1)
    finally:
        await client.close()


def test_expand_corpus_writes_missing_and_skips_existing(tmp_path):
    store = CorpusStore(tmp_path)
    seed_doc(store, "Armor", 100)
    seed_doc(store, "Evasion", 200)
    store.write_expanded("testwiki", "armor", 100, "<p>already expanded</p>")

    def handler(request: httpx.Request) -> httpx.Response:
        oldid = request.url.params["oldid"]
        return httpx.Response(200, json={"parse": {"text": f"<p>expanded {oldid}</p>"}})

    reports = expand_corpus(
        make_registry(), store, transport=httpx.MockTransport(handler)
    )
    report = reports[0]
    assert report.expanded == ["evasion"]
    assert report.skipped == ["armor"]
    assert report.failed == []
    assert store.expanded_path("testwiki", "evasion", 200).read_text() == "<p>expanded 200</p>"

    second = expand_corpus(make_registry(), store, transport=httpx.MockTransport(handler))
    assert second[0].expanded == []
    assert sorted(second[0].skipped) == ["armor", "evasion"]


def test_expand_corpus_collects_failures_and_continues(tmp_path):
    store = CorpusStore(tmp_path)
    seed_doc(store, "Armor", 100)
    seed_doc(store, "Evasion", 200)

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.params["oldid"] == "100":
            return httpx.Response(500)
        return httpx.Response(200, json={"parse": {"text": "<p>ok</p>"}})

    reports = expand_corpus(
        make_registry(), store, transport=httpx.MockTransport(handler)
    )
    report = reports[0]
    assert report.expanded == ["evasion"]
    assert len(report.failed) == 1
    assert report.failed[0][0] == "armor"


def test_expand_corpus_respects_limit(tmp_path):
    store = CorpusStore(tmp_path)
    seed_doc(store, "Armor", 100)
    seed_doc(store, "Evasion", 200)

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"parse": {"text": "<p>ok</p>"}})

    reports = expand_corpus(
        make_registry(), store, limit=1, transport=httpx.MockTransport(handler)
    )
    assert len(reports[0].expanded) == 1
