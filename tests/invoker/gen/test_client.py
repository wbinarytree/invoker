import httpx
import pytest
from anthropic import Anthropic, DefaultHttpxClient
from pydantic import BaseModel, ValidationError

from invoker.gen.client import (
    GENERATION_MODEL,
    GenerationClient,
    GenerationError,
)


def make_client(response_json: dict, captured: list | None = None) -> GenerationClient:
    def handler(request: httpx.Request) -> httpx.Response:
        if captured is not None:
            captured.append(request)
        return httpx.Response(200, json=response_json)

    api = Anthropic(
        api_key="test-key",
        http_client=DefaultHttpxClient(transport=httpx.MockTransport(handler)),
    )
    return GenerationClient(client=api)


def message_json(
    text: str = "Uphill miss chance is 25%.",
    stop_reason: str = "end_turn",
    model: str = "claude-opus-5",
) -> dict:
    return {
        "id": "msg_test",
        "type": "message",
        "role": "assistant",
        "model": model,
        "content": [{"type": "text", "text": text}],
        "stop_reason": stop_reason,
        "stop_sequence": None,
        "usage": {"input_tokens": 100, "output_tokens": 25},
    }


def generate(client: GenerationClient, **overrides):
    kwargs: dict = dict(
        prompt_name="concept-article",
        prompt_version="1",
        system="You write grounded articles.",
        user_content="Write about evasion.",
    )
    kwargs.update(overrides)
    return client.generate(**kwargs)


def test_generate_returns_text_and_provenance():
    client = make_client(message_json())
    result = generate(client)
    assert result.text == "Uphill miss chance is 25%."
    prov = result.provenance
    assert prov.model == "claude-opus-5"
    assert prov.prompt_name == "concept-article"
    assert prov.prompt_version == "1"
    assert prov.input_tokens == 100
    assert prov.output_tokens == 25
    assert prov.stop_reason == "end_turn"
    assert len(prov.request_sha256) == 64


def test_provenance_model_comes_from_response_not_request():
    client = make_client(message_json(model="claude-opus-4-8"))
    result = generate(client)
    assert result.provenance.model == "claude-opus-4-8"


def test_request_hash_stable_for_identical_calls_and_sensitive_to_content():
    a = generate(make_client(message_json())).provenance.request_sha256
    b = generate(make_client(message_json())).provenance.request_sha256
    c = generate(make_client(message_json()), user_content="Write about armor.")
    assert a == b
    assert a != c.provenance.request_sha256


def test_refusal_raises():
    client = make_client(message_json(text="", stop_reason="refusal"))
    with pytest.raises(GenerationError, match="refused"):
        generate(client)


def test_truncation_raises():
    client = make_client(message_json(stop_reason="max_tokens"))
    with pytest.raises(GenerationError, match="max_tokens"):
        generate(client)


def test_empty_output_raises():
    client = make_client(message_json(text="   "))
    with pytest.raises(GenerationError, match="no text"):
        generate(client)


def test_default_model_is_pinned_opus_5():
    captured: list[httpx.Request] = []
    client = make_client(message_json(), captured)
    generate(client)
    import json

    body = json.loads(captured[0].content)
    assert body["model"] == GENERATION_MODEL == "claude-opus-5"
    assert body["max_tokens"] == 16000
    assert "temperature" not in body


def test_effort_passes_through_output_config():
    captured: list[httpx.Request] = []
    client = make_client(message_json(), captured)
    generate(client, effort="medium")
    import json

    body = json.loads(captured[0].content)
    assert body["output_config"] == {"effort": "medium"}


class CardStub(BaseModel):
    entity: str
    summary: str


def test_generate_structured_parses_and_carries_provenance():
    payload = '{"entity": "evasion", "summary": "Attacks can miss."}'
    client = make_client(message_json(text=payload))
    result = client.generate_structured(
        CardStub,
        prompt_name="card",
        prompt_version="1",
        system="Emit a card.",
        user_content="Card for evasion.",
    )
    assert result.output == CardStub(entity="evasion", summary="Attacks can miss.")
    assert result.provenance.prompt_name == "card"


def test_generate_structured_invalid_payload_raises():
    client = make_client(message_json(text='{"wrong_field": true}'))
    with pytest.raises(ValidationError):
        client.generate_structured(
            CardStub,
            prompt_name="card",
            prompt_version="1",
            system="Emit a card.",
            user_content="Card for evasion.",
        )
