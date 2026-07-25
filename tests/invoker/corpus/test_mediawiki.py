import httpx
import pytest

from invoker.corpus.mediawiki import MediaWikiClient, MediaWikiError


def query_response() -> dict:
    return {
        "query": {
            "normalized": [{"from": "attack speed", "to": "Attack speed"}],
            "redirects": [{"from": "Attack speed", "to": "Attack Speed"}],
            "pages": [
                {
                    "pageid": 7,
                    "ns": 0,
                    "title": "Attack Speed",
                    "revisions": [
                        {
                            "revid": 100,
                            "parentid": 99,
                            "timestamp": "2026-07-01T00:00:00Z",
                            "slots": {"main": {"content": "attack speed wikitext"}},
                        }
                    ],
                },
                {"ns": 0, "title": "Ghost Page", "missing": True},
                {"pageid": 9, "ns": 0, "title": "Empty Page", "revisions": []},
            ],
        }
    }


@pytest.mark.asyncio
async def test_fetch_revisions_parses_redirects_missing_and_content():
    seen_requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen_requests.append(request)
        return httpx.Response(200, json=query_response())

    client = MediaWikiClient(
        "https://liquipedia.net/dota2/api.php",
        user_agent="invoker-test/0",
        transport=httpx.MockTransport(handler),
    )
    try:
        revisions, missing = await client.fetch_revisions(
            ["attack speed", "Ghost Page", "Empty Page"]
        )
    finally:
        await client.close()

    assert len(seen_requests) == 1
    request = seen_requests[0]
    assert request.headers["user-agent"] == "invoker-test/0"
    assert request.url.params["titles"] == "attack speed|Ghost Page|Empty Page"
    assert request.url.params["redirects"] == "1"

    assert len(revisions) == 1
    revision = revisions[0]
    assert revision.requested_title == "attack speed"
    assert revision.resolved_title == "Attack Speed"
    assert revision.revision_id == 100
    assert revision.content == "attack speed wikitext"

    reasons = {page.requested_title: page.reason for page in missing}
    assert reasons == {"Ghost Page": "missing", "Empty Page": "no_revision"}


@pytest.mark.asyncio
async def test_fetch_revisions_batches_large_title_lists():
    calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(200, json={"query": {"pages": []}})

    client = MediaWikiClient(
        "https://example.test/api.php",
        user_agent="invoker-test/0",
        requests_per_minute=6000,
        transport=httpx.MockTransport(handler),
    )
    try:
        await client.fetch_revisions([f"Page {i}" for i in range(45)])
    finally:
        await client.close()
    assert calls == 3


@pytest.mark.asyncio
async def test_unexpected_response_shape_raises():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"nope": True})

    client = MediaWikiClient(
        "https://example.test/api.php",
        user_agent="invoker-test/0",
        transport=httpx.MockTransport(handler),
    )
    try:
        with pytest.raises(MediaWikiError, match="unexpected MediaWiki response"):
            await client.fetch_revisions(["Mechanics"])
    finally:
        await client.close()
