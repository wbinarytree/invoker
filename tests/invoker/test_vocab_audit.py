from pathlib import Path

import yaml

from invoker.kg.vocab_audit import format_vocab_audit, run_vocab_audit
from invoker.kg.vocabulary import CAPABILITIES, RELATION_PATTERNS, load_vocabulary


def _hero_payload(term: str = "mobility") -> dict:
    return {
        "hero_id": 999,
        "hero_slug": "testhero",
        "localized_name": "Test Hero",
        "capabilities": [
            {
                "type": term,
                "score": 0.8,
                "evidence": ["test evidence"],
            }
        ],
        "requirements": [],
        "liabilities": [],
        "targets": [],
        "role_distribution": {},
        "provenance": {
            "authored_by": "human",
            "authored_at": "2026-04-25",
            "assist_model": None,
        },
    }


def test_vocabulary_exports_live_terms_from_yaml():
    raw = load_vocabulary()

    assert "mobility" in CAPABILITIES
    assert "setup_followup" in RELATION_PATTERNS
    assert raw["capabilities"]["mobility"]["status"] == "accepted"


def test_vocab_audit_passes_without_blocking_errors(tmp_path: Path):
    root = tmp_path / "authored"
    root.mkdir()
    root.joinpath("testhero.yaml").write_text(yaml.safe_dump(_hero_payload(), sort_keys=False))

    audit = run_vocab_audit(tmp_path)

    assert audit.passed is True
    assert audit.unknown_authored_terms == []
    assert "capabilities" in audit.terms_without_rule


def test_vocab_audit_reports_unknown_authored_terms(tmp_path: Path):
    root = tmp_path / "authored"
    root.mkdir()
    root.joinpath("testhero.yaml").write_text(
        yaml.safe_dump(_hero_payload("not_real"), sort_keys=False)
    )

    audit = run_vocab_audit(tmp_path)
    text = format_vocab_audit(audit)

    assert audit.passed is False
    assert audit.unknown_authored_terms[0].term == "not_real"
    assert "testhero.capabilities.not_real" in text
