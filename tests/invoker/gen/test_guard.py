import json
from datetime import UTC, datetime

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

    def generate(self, **kwargs):
        raise AssertionError("guard must use generate_structured")

    def generate_structured(self, output_type, **kwargs):
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
