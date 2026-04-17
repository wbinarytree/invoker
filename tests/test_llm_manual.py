import pytest

from invoker.llm.manual import ManualClient


def test_manual_client_writes_prompt_and_raises(tmp_path):
    client = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    with pytest.raises(FileNotFoundError):
        client.generate_json("hello", prompt_version=1)
    assert any((tmp_path / "in").iterdir()), "prompt should be written"


def test_manual_client_roundtrip(tmp_path):
    client = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    try:
        client.generate_json("hello", prompt_version=1)
    except FileNotFoundError as e:
        msg = str(e)
        assert "Paste the JSON output for" in msg
    import hashlib

    h = hashlib.sha256(b"hello").hexdigest()[:12]
    (tmp_path / "out" / f"{h}.txt").write_text('{"ok": true}')
    resp = client.generate_json("hello", prompt_version=1)
    assert resp.text == '{"ok": true}'
