import pytest

from invoker.llm.manual import ManualClient, PendingManualResponseError


def test_manual_client_writes_prompt_and_raises_pending(tmp_path):
    client = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    with pytest.raises(PendingManualResponseError) as exc_info:
        client.generate_json("hello", prompt_version=1, cache_tag="extract/Slardar")
    err = exc_info.value
    assert err.prompt_path.exists()
    assert err.response_path.exists()
    assert err.response_path.suffix == ".json"
    assert err.response_path.read_text() == ""
    assert "extract/Slardar" in str(err)
    assert err.prompt_path.is_relative_to(tmp_path / "in" / "extract" / "Slardar")


def test_manual_client_roundtrip(tmp_path):
    client = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    try:
        client.generate_json("hello", prompt_version=1, cache_tag="extract/Axe")
    except PendingManualResponseError as err:
        err.response_path.parent.mkdir(parents=True, exist_ok=True)
        err.response_path.write_text('{"ok": true}')
    resp = client.generate_json("hello", prompt_version=1, cache_tag="extract/Axe")
    assert resp.text == '{"ok": true}'


def test_manual_client_prompt_header_records_context(tmp_path):
    client = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    try:
        client.generate_json("body text", prompt_version=7, cache_tag="reason/Axe")
    except PendingManualResponseError as err:
        content = err.prompt_path.read_text()
    assert "cache_tag: reason/Axe" in content
    assert "prompt_version: 7" in content
    assert "body text" in content


def test_manual_client_without_tag_still_works(tmp_path):
    client = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    with pytest.raises(PendingManualResponseError) as exc_info:
        client.generate_json("untagged", prompt_version=1)
    assert exc_info.value.prompt_path.parent == tmp_path / "in"
