import json

import httpx
import pytest

from invoker.http.client import SharedOpenDotaCachedClient


@pytest.mark.asyncio
async def test_shared_opendota_cache_writes_envelope_and_reuses_data(tmp_path):
    calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        assert request.url.path == "/api/proMatches"
        return httpx.Response(200, json=[{"match_id": 1}])

    client = SharedOpenDotaCachedClient(
        tmp_path,
        fetched_by="invoker@test",
        source_patch="7.41b",
    )
    await client._client.aclose()
    client._client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    try:
        first = await client.get("https://api.opendota.com/api/proMatches")
        second = await client.get("https://api.opendota.com/api/proMatches")
    finally:
        await client.close()

    assert first == [{"match_id": 1}]
    assert second == first
    assert calls == 1

    cache_file = tmp_path / "opendota" / "responses" / "proMatches.json"
    assert cache_file.exists()
    envelope = json.loads(cache_file.read_text())
    assert envelope["meta"]["endpoint"] == "/proMatches"
    assert envelope["meta"]["params"] == {}
    assert envelope["meta"]["schema_version"] == 1
    assert envelope["meta"]["fetched_by"] == "invoker@test"
    assert envelope["meta"]["source_patch"] == "7.41b"
    assert envelope["data"] == [{"match_id": 1}]


@pytest.mark.asyncio
async def test_shared_opendota_cache_uses_oracle_param_filename(tmp_path):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=[{"match_id": 2}])

    client = SharedOpenDotaCachedClient(
        tmp_path,
        fetched_by="invoker@test",
        source_patch=None,
    )
    await client._client.aclose()
    client._client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    try:
        rows = await client.get(
            "https://api.opendota.com/api/proMatches",
            params={"less_than_match_id": 42},
        )
    finally:
        await client.close()

    assert rows == [{"match_id": 2}]
    cache_file = (
        tmp_path
        / "opendota"
        / "responses"
        / "proMatches__less_than_match_id=42.json"
    )
    assert cache_file.exists()


@pytest.mark.asyncio
async def test_shared_opendota_cache_force_refetches(tmp_path):
    calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(200, json={"call": calls})

    client = SharedOpenDotaCachedClient(
        tmp_path,
        fetched_by="invoker@test",
        source_patch=None,
    )
    await client._client.aclose()
    client._client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    try:
        first = await client.get("https://api.opendota.com/api/teams/123/matches")
        second = await client.get("https://api.opendota.com/api/teams/123/matches", force=True)
    finally:
        await client.close()

    assert first == {"call": 1}
    assert second == {"call": 2}
    assert calls == 2
