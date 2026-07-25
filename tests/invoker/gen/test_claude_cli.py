import json

import pytest
from pydantic import BaseModel

from invoker.gen.claude_cli import ClaudeCliClient
from invoker.gen.client import GenerationError


def cli_payload(
    result: str = "Uphill miss chance is 25%.",
    stop_reason: str = "end_turn",
    is_error: bool = False,
    model: str = "claude-opus-5",
) -> dict:
    return {
        "type": "result",
        "is_error": is_error,
        "result": result,
        "stop_reason": stop_reason,
        "usage": {"input_tokens": 12, "output_tokens": 30},
        "modelUsage": {
            "claude-haiku-4-5-20251001": {
                "outputTokens": 99,
                "canonicalModel": "claude-haiku-4-5",
            },
            model: {"outputTokens": 30, "canonicalModel": model},
        },
    }


def make_client(payload: dict, calls: list | None = None, returncode: int = 0) -> ClaudeCliClient:
    def run(argv: list[str], stdin: str) -> tuple[int, str, str]:
        if calls is not None:
            calls.append((argv, stdin))
        return returncode, json.dumps(payload), ""

    return ClaudeCliClient(run=run)


def generate(client: ClaudeCliClient, **overrides):
    kwargs = dict(
        prompt_name="concept-article",
        prompt_version="1",
        system="You write grounded articles.",
        user_content="Write about evasion.",
    )
    kwargs.update(overrides)
    return client.generate(**kwargs)


def test_generate_builds_headless_command_with_tools_disabled():
    calls: list = []
    generate(make_client(cli_payload(), calls))
    argv, stdin = calls[0]
    assert argv[:4] == ["claude", "-p", "--output-format", "json"]
    assert argv[argv.index("--model") + 1] == "claude-opus-5"
    assert argv[argv.index("--tools") + 1] == ""
    assert argv[argv.index("--system-prompt") + 1] == "You write grounded articles."
    assert stdin == "Write about evasion."


def test_generate_returns_text_and_cli_provenance():
    result = generate(make_client(cli_payload()))
    assert result.text == "Uphill miss chance is 25%."
    prov = result.provenance
    assert prov.transport == "claude-cli"
    assert prov.model == "claude-opus-5"
    assert prov.input_tokens == 12
    assert prov.output_tokens == 30
    assert len(prov.request_sha256) == 64


def test_served_model_matches_requested_not_background_harness_model():
    # haiku has higher outputTokens in the fixture; the requested model must win
    result = generate(make_client(cli_payload()))
    assert result.provenance.model == "claude-opus-5"


def test_missing_requested_model_in_usage_fails_loudly():
    payload = cli_payload()
    del payload["modelUsage"]["claude-opus-5"]
    with pytest.raises(GenerationError, match="not in modelUsage"):
        generate(make_client(payload))


def test_nonzero_exit_raises():
    with pytest.raises(GenerationError, match="exited 1"):
        generate(make_client(cli_payload(), returncode=1))


def test_is_error_payload_raises():
    with pytest.raises(GenerationError, match="reported an error"):
        generate(make_client(cli_payload(is_error=True)))


def test_refusal_and_truncation_raise():
    with pytest.raises(GenerationError, match="refused"):
        generate(make_client(cli_payload(stop_reason="refusal")))
    with pytest.raises(GenerationError, match="max_tokens"):
        generate(make_client(cli_payload(stop_reason="max_tokens")))


def test_non_json_stdout_raises():
    client = ClaudeCliClient(run=lambda argv, stdin: (0, "Execution error", ""))
    with pytest.raises(GenerationError, match="non-JSON"):
        generate(client)


def test_effort_flag_passes_through():
    calls: list = []
    generate(make_client(cli_payload(), calls), effort="medium")
    argv, _ = calls[0]
    assert argv[argv.index("--effort") + 1] == "medium"


class CardStub(BaseModel):
    entity: str
    summary: str


def test_generate_structured_appends_schema_and_validates():
    calls: list = []
    payload = cli_payload(result='{"entity": "evasion", "summary": "Attacks can miss."}')
    client = make_client(payload, calls)
    result = client.generate_structured(
        CardStub,
        prompt_name="card",
        prompt_version="1",
        system="Emit a card.",
        user_content="Card for evasion.",
    )
    assert result.output == CardStub(entity="evasion", summary="Attacks can miss.")
    argv, _ = calls[0]
    system_sent = argv[argv.index("--system-prompt") + 1]
    assert "JSON schema" in system_sent
    assert '"entity"' in system_sent


def test_generate_structured_strips_code_fences():
    payload = cli_payload(result='```json\n{"entity": "evasion", "summary": "ok"}\n```')
    result = make_client(payload).generate_structured(
        CardStub,
        prompt_name="card",
        prompt_version="1",
        system="Emit a card.",
        user_content="Card for evasion.",
    )
    assert result.output.entity == "evasion"


def test_generate_structured_bad_payload_raises_validation_error():
    from pydantic import ValidationError

    payload = cli_payload(result='{"wrong": true}')
    with pytest.raises(ValidationError):
        make_client(payload).generate_structured(
            CardStub,
            prompt_name="card",
            prompt_version="1",
            system="Emit a card.",
            user_content="Card for evasion.",
        )
