import json
from datetime import UTC, datetime
from typing import Any

import pytest

from invoker.gen.client import (
    GenerationError,
    GenerationProvenance,
    StructuredResult,
)
from invoker.gen.guard import (
    CompletenessReport,
    GuardResult,
    MissingFact,
    run_guard,
    write_report,
)

VALID_SECTIONS = {
    "corpus:liquipedia_dota2/evasion@1#Talents",
    "gamefile:items/item_mage_slayer#cost",
}


def make_provenance() -> GenerationProvenance:
    return GenerationProvenance(
        model="gpt-5.6-sol",
        transport="codex-app-server",
        prompt_name="completeness-guard",
        prompt_version="1",
        request_sha256="ab" * 32,
        input_tokens=100,
        output_tokens=10,
        stop_reason="completed",
        generated_at=datetime.now(UTC).isoformat(),
    )


class FakeBackend:
    def __init__(self, report: CompletenessReport):
        self.model = "gpt-5.6-sol"
        self.calls: list[dict] = []
        self._report = report

    def generate(self, **kwargs: Any) -> Any:
        raise AssertionError("guard must use generate_structured")

    def generate_structured(self, output_type: Any, **kwargs: Any) -> Any:
        self.calls.append(kwargs)
        return StructuredResult(output=self._report, provenance=make_provenance())


def guard(report: CompletenessReport) -> tuple[GuardResult, FakeBackend]:
    backend = FakeBackend(report)
    result = run_guard(
        backend,
        packet="## [key] text",
        valid_sections=VALID_SECTIONS,
        article="Article body.",
    )
    return result, backend


def test_clean_report_passes_through():
    result, backend = guard(CompletenessReport(missing=[]))
    assert result.report.missing == []
    assert result.provenance.prompt_name == "completeness-guard"
    call = backend.calls[0]
    assert "Packet:" in call["user_content"]
    assert "Article body." in call["user_content"]


def test_bare_concept_key_normalizes_to_mark_key():
    report = CompletenessReport(
        missing=[MissingFact(section="liquipedia_dota2/evasion@1#Talents", fact="ladder")]
    )
    result, _ = guard(report)
    assert result.report.missing[0].section == "corpus:liquipedia_dota2/evasion@1#Talents"


def test_full_mark_key_is_accepted_as_is():
    report = CompletenessReport(
        missing=[MissingFact(section="gamefile:items/item_mage_slayer#cost", fact="3100 gold")]
    )
    result, _ = guard(report)
    assert result.report.missing[0].section == "gamefile:items/item_mage_slayer#cost"


def test_unknown_section_key_refuses_the_report():
    report = CompletenessReport(
        missing=[MissingFact(section="made_up#Section", fact="whatever")]
    )
    with pytest.raises(GenerationError, match="unknown packet section"):
        guard(report)


def make_concept_artifact(tmp_path):
    """A real on-disk concept artifact via the generation pipeline, plus
    the store that can rebuild its packet."""
    from invoker.gen.concepts import generate_concept
    from tests.invoker.corpus.test_sections import make_store
    from tests.invoker.gen.test_concepts import FakeBackend as GenFakeBackend
    from tests.invoker.gen.test_concepts import good_article, good_card

    store = make_store(tmp_path)
    _, artifact_path = generate_concept(
        store,
        GenFakeBackend(good_article(), good_card()),
        host_key="testwiki",
        slug="evasion",
        patch="7.41d",
        kb_dir=tmp_path / "kb" / "7.41d",
    )
    return store, artifact_path


def test_guard_entity_concept_roundtrip_writes_clean_report(tmp_path):
    from invoker.gen.guard import guard_entity

    store, artifact_path = make_concept_artifact(tmp_path)
    backend = FakeBackend(CompletenessReport(missing=[]))
    outcome = guard_entity(
        artifact_path, backend, store=store, game_data_dir=None, host_key="testwiki"
    )
    assert outcome.missing_count == 0
    assert outcome.packet_matches_artifact is True
    payload = json.loads(outcome.report_path.read_text())
    assert payload["missing"] == []
    assert payload["packet_matches_artifact"] is True
    # the guard saw the real packet, not a stub
    assert "Packet:" in backend.calls[0]["user_content"]


def test_guard_entity_concept_without_store_raises(tmp_path):
    from invoker.gen.guard import guard_entity

    _, artifact_path = make_concept_artifact(tmp_path)
    with pytest.raises(GenerationError, match="corpus store"):
        guard_entity(
            artifact_path, FakeBackend(CompletenessReport(missing=[])),
            store=None, game_data_dir=None,
        )


def test_guard_entity_records_packet_drift(tmp_path):
    from invoker.gen.guard import guard_entity

    store, artifact_path = make_concept_artifact(tmp_path)
    raw = json.loads(artifact_path.read_text())
    raw["packet_sha256"] = "0" * 64
    artifact_path.write_text(json.dumps(raw))
    outcome = guard_entity(
        artifact_path, FakeBackend(CompletenessReport(missing=[])),
        store=store, game_data_dir=None, host_key="testwiki",
    )
    assert outcome.packet_matches_artifact is False
    assert json.loads(outcome.report_path.read_text())["packet_matches_artifact"] is False


def test_cli_guard_gate_exits_nonzero_on_flags(tmp_path):
    import typer

    from invoker.cli import _run_guard_gate

    store, artifact_path = make_concept_artifact(tmp_path)
    flagged = FakeBackend(
        CompletenessReport(
            missing=[MissingFact(section="corpus:testwiki/evasion@42", fact="dropped")]
        )
    )
    with pytest.raises(typer.Exit) as excinfo:
        _run_guard_gate(
            artifact_path, flagged, store=store, game_data_dir=None, host_key="testwiki"
        )
    assert excinfo.value.exit_code == 1
    clean = FakeBackend(CompletenessReport(missing=[]))
    _run_guard_gate(artifact_path, clean, store=store, game_data_dir=None, host_key="testwiki")


def test_write_report_records_flags_provenance_and_packet_identity(tmp_path):
    artifact_path = tmp_path / "artifact.json"
    artifact_path.write_text("{}")
    result = GuardResult(
        report=CompletenessReport(
            missing=[MissingFact(section="gamefile:items/item_mage_slayer#cost", fact="3100")]
        ),
        provenance=make_provenance(),
    )
    report_path = write_report(
        artifact_path, result, packet_sha256="cd" * 32, packet_matches_artifact=False
    )
    payload = json.loads(report_path.read_text())
    assert report_path.name == "completeness.json"
    assert payload["schema_version"] == 1
    assert payload["packet_matches_artifact"] is False
    assert payload["packet_sha256"] == "cd" * 32
    assert payload["missing"] == [
        {"section": "gamefile:items/item_mage_slayer#cost", "fact": "3100"}
    ]
    assert payload["guard_provenance"]["transport"] == "codex-app-server"
