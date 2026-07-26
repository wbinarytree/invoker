import json

import pytest
from pydantic import BaseModel

from invoker.gen.client import GenerationError
from invoker.gen.codex import CodexClient, strict_output_schema

THREAD_ID = "thread-1"
TURN_ID = "turn-1"


class FakeAppServer:
    """Scripted daemon: each request the client sends is answered by
    `respond`, which returns the messages (response + notifications) the
    server would emit. Lines queue in order; receive drains them."""

    def __init__(self, respond):
        self.sent: list[dict] = []
        self.closed = False
        self.respond = respond
        self._out: list[str] = []

    def send_line(self, line: str) -> None:
        request = json.loads(line)
        self.sent.append(request)
        for msg in self.respond(request):
            self._out.append(json.dumps(msg))

    def receive_line(self, timeout: float) -> str:
        if not self._out:
            raise AssertionError("client waited for a line the script never emitted")
        return self._out.pop(0)

    def close(self) -> None:
        self.closed = True


def usage_notification(input_tokens: int = 1000, output_tokens: int = 50) -> dict:
    return {
        "jsonrpc": "2.0",
        "method": "thread/tokenUsage/updated",
        "params": {
            "threadId": THREAD_ID,
            "turnId": TURN_ID,
            "tokenUsage": {
                "last": {
                    "totalTokens": input_tokens + output_tokens,
                    "inputTokens": input_tokens,
                    "cachedInputTokens": 0,
                    "outputTokens": output_tokens,
                    "reasoningOutputTokens": 10,
                },
                "total": {},
            },
        },
    }


def agent_message(text: str) -> dict:
    return {
        "jsonrpc": "2.0",
        "method": "item/completed",
        "params": {
            "threadId": THREAD_ID,
            "turnId": TURN_ID,
            "completedAtMs": 0,
            "item": {"type": "agentMessage", "id": "msg-1", "text": text},
        },
    }


def turn_completed(status: str = "completed", error: dict | None = None) -> dict:
    return {
        "jsonrpc": "2.0",
        "method": "turn/completed",
        "params": {
            "threadId": THREAD_ID,
            "turn": {"id": TURN_ID, "items": [], "status": status, "error": error},
        },
    }


def scripted_server(
    turn_messages: list[dict] | None = None,
    thread_model: str = "gpt-5.6-sol",
) -> FakeAppServer:
    if turn_messages is None:
        turn_messages = [
            usage_notification(),
            agent_message("Uphill miss chance is 25%."),
            turn_completed(),
        ]

    def respond(request: dict) -> list[dict]:
        response = {"jsonrpc": "2.0", "id": request["id"]}
        if request["method"] == "initialize":
            return [{**response, "result": {"userAgent": "codex/0.145.0"}}]
        if request["method"] == "thread/start":
            return [
                {**response, "result": {"thread": {"id": THREAD_ID}, "model": thread_model}}
            ]
        if request["method"] == "turn/start":
            return [
                {**response, "result": {"turn": {"id": TURN_ID, "status": "inProgress"}}},
                *turn_messages,
            ]
        raise AssertionError(f"unscripted method {request['method']}")

    return FakeAppServer(respond)


def make_client(server: FakeAppServer, model: str = "gpt-5.6-sol") -> CodexClient:
    return CodexClient(model=model, spawn=lambda: server)


def generate(client: CodexClient, **overrides):
    kwargs = dict(
        prompt_name="concept-article",
        prompt_version="1",
        system="You write grounded articles.",
        user_content="Write about evasion.",
    )
    kwargs.update(overrides)
    return client.generate(**kwargs)


def sent_by_method(server: FakeAppServer, method: str) -> dict:
    matches = [msg for msg in server.sent if msg["method"] == method]
    assert len(matches) == 1, f"expected one {method}, saw {len(matches)}"
    return matches[0]


def test_generate_starts_locked_down_ephemeral_thread():
    server = scripted_server()
    generate(make_client(server))
    params = sent_by_method(server, "thread/start")["params"]
    assert params["ephemeral"] is True
    assert params["model"] == "gpt-5.6-sol"
    assert params["baseInstructions"] == "You write grounded articles."
    assert params["approvalPolicy"] == "never"
    assert params["sandbox"] == "read-only"
    assert params["config"] == {"mcp_servers": {}}
    turn = sent_by_method(server, "turn/start")["params"]
    assert turn["input"] == [{"type": "text", "text": "Write about evasion."}]
    assert "outputSchema" not in turn


def test_generate_returns_text_and_reported_usage():
    result = generate(make_client(scripted_server()))
    assert result.text == "Uphill miss chance is 25%."
    prov = result.provenance
    assert prov.transport == "codex-app-server"
    assert prov.model == "gpt-5.6-sol"
    assert prov.input_tokens == 1000
    assert prov.output_tokens == 50
    assert prov.stop_reason == "completed"
    assert len(prov.request_sha256) == 64


def test_missing_usage_notification_records_null_not_zero():
    server = scripted_server(turn_messages=[agent_message("Answer."), turn_completed()])
    prov = generate(make_client(server)).provenance
    assert prov.input_tokens is None
    assert prov.output_tokens is None


def test_daemon_and_initialize_are_reused_across_calls():
    server = scripted_server()
    client = make_client(server)
    generate(client)
    server.respond = scripted_server().respond  # rescript for the second turn
    generate(client)
    assert len([m for m in server.sent if m["method"] == "initialize"]) == 1
    assert len([m for m in server.sent if m["method"] == "thread/start"]) == 2


def test_failed_turn_surfaces_error_and_tears_down_daemon():
    server = scripted_server(
        turn_messages=[turn_completed(status="failed", error={"message": "status 400"})]
    )
    with pytest.raises(GenerationError, match="failed: status 400"):
        generate(make_client(server))
    assert server.closed


def test_model_substitution_is_refused():
    server = scripted_server(thread_model="gpt-5.5")
    with pytest.raises(GenerationError, match="resolved to 'gpt-5.5'"):
        generate(make_client(server))


def test_reroute_notification_is_refused():
    reroute = {
        "jsonrpc": "2.0",
        "method": "model/rerouted",
        "params": {
            "threadId": THREAD_ID,
            "turnId": TURN_ID,
            "fromModel": "gpt-5.6-sol",
            "toModel": "gpt-5.5",
            "reason": "highRiskCyberActivity",
        },
    }
    server = scripted_server(turn_messages=[reroute, turn_completed()])
    with pytest.raises(GenerationError, match="rerouted"):
        generate(make_client(server))


def test_server_request_mid_turn_is_a_contract_violation():
    approval = {
        "jsonrpc": "2.0",
        "id": 99,
        "method": "execCommandApproval",
        "params": {"threadId": THREAD_ID},
    }
    server = scripted_server(turn_messages=[approval, turn_completed()])
    with pytest.raises(GenerationError, match="no-tools contract"):
        generate(make_client(server))


def test_empty_agent_message_raises():
    server = scripted_server(turn_messages=[turn_completed()])
    with pytest.raises(GenerationError, match="no text"):
        generate(make_client(server))


def test_jsonrpc_error_response_raises():
    def respond(request: dict) -> list[dict]:
        return [
            {"jsonrpc": "2.0", "id": request["id"], "error": {"code": -1, "message": "bad params"}}
        ]

    with pytest.raises(GenerationError, match="bad params"):
        generate(make_client(FakeAppServer(respond)))


class CardStub(BaseModel):
    entity: str
    summary: str


def structured(client: CodexClient):
    return client.generate_structured(
        CardStub,
        prompt_name="card",
        prompt_version="1",
        system="Emit a card.",
        user_content="Card for evasion.",
    )


def test_generate_structured_sends_output_schema_and_validates():
    server = scripted_server(
        turn_messages=[
            usage_notification(),
            agent_message('{"entity": "evasion", "summary": "Attacks can miss."}'),
            turn_completed(),
        ]
    )
    result = structured(make_client(server))
    assert result.output == CardStub(entity="evasion", summary="Attacks can miss.")
    turn = sent_by_method(server, "turn/start")["params"]
    assert turn["outputSchema"] == strict_output_schema(CardStub.model_json_schema())
    # the schema constrains server-side; the system prompt stays byte-identical
    assert sent_by_method(server, "thread/start")["params"]["baseInstructions"] == "Emit a card."


def test_strict_output_schema_closes_objects_and_requires_all_fields():
    class Inner(BaseModel):
        note: str = "n/a"

    class Outer(BaseModel):
        name: str
        inner: Inner

    schema = strict_output_schema(Outer.model_json_schema())
    assert schema["additionalProperties"] is False
    assert schema["required"] == ["inner", "name"]
    inner = schema["$defs"]["Inner"]
    assert inner["additionalProperties"] is False
    assert inner["required"] == ["note"]  # defaulted field still demanded of the model


def test_generate_structured_bad_payload_raises_generation_error():
    server = scripted_server(turn_messages=[agent_message('{"wrong": true}'), turn_completed()])
    with pytest.raises(GenerationError, match="does not validate as CardStub"):
        structured(make_client(server))


def test_structured_schema_changes_request_fingerprint():
    plain = generate(make_client(scripted_server()))

    server = scripted_server(
        turn_messages=[agent_message('{"entity": "e", "summary": "s"}'), turn_completed()]
    )
    schema_result = make_client(server).generate_structured(
        CardStub,
        prompt_name="concept-article",
        prompt_version="1",
        system="You write grounded articles.",
        user_content="Write about evasion.",
    )
    assert plain.provenance.request_sha256 != schema_result.provenance.request_sha256


def test_effort_passes_through_on_turn_start():
    server = scripted_server()
    generate(make_client(server), effort="xhigh")
    assert sent_by_method(server, "turn/start")["params"]["effort"] == "xhigh"
