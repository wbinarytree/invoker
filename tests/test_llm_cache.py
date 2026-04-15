from __future__ import annotations

import json
from pathlib import Path

from invoker.llm.cache import CachingLLMClient, _cache_key
from invoker.llm.client import LLMResponse


class CountingClient:
    """Tracks how many times it was called."""

    model_name = "counting"

    def __init__(self, response_text: str = '{"ok": true}') -> None:
        self.calls = 0
        self._text = response_text

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        self.calls += 1
        return LLMResponse(text=self._text, model=self.model_name, prompt_version=prompt_version)


def test_cache_miss_calls_inner(tmp_path: Path) -> None:
    inner = CountingClient()
    client = CachingLLMClient(inner, tmp_path)

    resp = client.complete_json("hello", prompt_version=1)

    assert inner.calls == 1
    assert resp.text == '{"ok": true}'
    assert resp.model == "counting"


def test_cache_hit_skips_inner(tmp_path: Path) -> None:
    inner = CountingClient()
    client = CachingLLMClient(inner, tmp_path)

    first = client.complete_json("hello", prompt_version=1)
    second = client.complete_json("hello", prompt_version=1)

    assert inner.calls == 1  # only called once
    assert first.text == second.text


def test_cache_written_to_disk(tmp_path: Path) -> None:
    inner = CountingClient(response_text='{"result": 42}')
    client = CachingLLMClient(inner, tmp_path)

    client.complete_json("my prompt", prompt_version=2)

    key = _cache_key("counting", 2, "my prompt")
    cache_file = tmp_path / key[:2] / f"{key}.json"
    assert cache_file.exists()
    entry = json.loads(cache_file.read_text())
    assert entry["text"] == '{"result": 42}'
    assert entry["model"] == "counting"
    assert entry["prompt_version"] == 2
    assert "cached_at" in entry


def test_different_prompts_have_different_keys(tmp_path: Path) -> None:
    inner = CountingClient()
    client = CachingLLMClient(inner, tmp_path)

    client.complete_json("prompt A", prompt_version=1)
    client.complete_json("prompt B", prompt_version=1)

    assert inner.calls == 2


def test_different_prompt_versions_have_different_keys(tmp_path: Path) -> None:
    inner = CountingClient()
    client = CachingLLMClient(inner, tmp_path)

    client.complete_json("same prompt", prompt_version=1)
    client.complete_json("same prompt", prompt_version=2)

    assert inner.calls == 2


def test_different_models_have_different_keys(tmp_path: Path) -> None:
    class ModelA:
        model_name = "model-a"

        def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
            return LLMResponse(text='{"a": 1}', model=self.model_name, prompt_version=prompt_version)

    class ModelB:
        model_name = "model-b"

        def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
            return LLMResponse(text='{"b": 2}', model=self.model_name, prompt_version=prompt_version)

    client_a = CachingLLMClient(ModelA(), tmp_path)
    client_b = CachingLLMClient(ModelB(), tmp_path)

    resp_a = client_a.complete_json("same", prompt_version=1)
    resp_b = client_b.complete_json("same", prompt_version=1)

    assert resp_a.text == '{"a": 1}'
    assert resp_b.text == '{"b": 2}'


def test_cache_key_is_deterministic() -> None:
    k1 = _cache_key("model", 1, "prompt")
    k2 = _cache_key("model", 1, "prompt")
    assert k1 == k2


def test_model_name_proxied(tmp_path: Path) -> None:
    inner = CountingClient()
    client = CachingLLMClient(inner, tmp_path)
    assert client.model_name == "counting"
