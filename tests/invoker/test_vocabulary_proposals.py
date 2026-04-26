import json
from pathlib import Path

import yaml

import invoker.kg.vocabulary_proposals as proposals
from invoker.kg.vocabulary_proposals import (
    amend_vocabulary_proposal,
    parse_vocabulary_proposals,
    promote_vocabulary,
    review_vocabulary_proposal,
)


def _response_payload() -> dict:
    return {
        "schema_version": 1,
        "proposals": [
            {
                "bucket": "capabilities",
                "term": "attack_speed_reduction",
                "action": "add",
                "definition": "Reduces enemy attack speed through a hero-owned mechanic.",
                "include_when": ["The hero directly applies attack speed reduction."],
                "exclude_when": ["The effect comes primarily from purchased items."],
                "examples": [
                    {
                        "hero_slug": "pangolier",
                        "evidence": "Lucky Shot can reduce enemy attack speed.",
                    }
                ],
                "enabled_rules": [],
                "rationale": "Reviewed gaps support this term.",
                "status": "proposed",
            }
        ],
    }


def _split_response_payload() -> dict:
    return {
        "schema_version": 1,
        "proposals": [
            {
                "bucket": "capabilities",
                "term": "damage_amp",
                "action": "split",
                "definition": "Increases damage through hero-owned mechanics.",
                "include_when": [],
                "exclude_when": [],
                "examples": [
                    {
                        "hero_slug": "largo",
                        "evidence": "Largo has a reviewed damage amplification gap.",
                    }
                ],
                "enabled_rules": [],
                "split_into": ["physical_damage_amp"],
                "rationale": "Damage amplification should be split by damage type.",
                "status": "proposed",
            },
            {
                "bucket": "capabilities",
                "term": "physical_damage_amp",
                "action": "add",
                "definition": "Increases physical damage through hero-owned mechanics.",
                "include_when": [],
                "exclude_when": [],
                "examples": [],
                "enabled_rules": [],
                "rationale": "Child term of a grounded split.",
                "status": "proposed",
            },
        ],
    }


def _vocabulary_payload() -> dict:
    return {
        "schema_version": 1,
        "capabilities": {
            "mobility": {
                "definition": "Moves.",
                "include_when": [],
                "exclude_when": [],
                "examples": [],
                "status": "accepted",
                "introduced_in": "stage2",
            }
        },
        "requirements": {},
        "liabilities": {},
        "targets": {},
        "relation_patterns": {},
        "statistical_alignment": {},
    }


def _write_grounding_files(tmp_path: Path) -> None:
    root = tmp_path / "authored"
    root.mkdir(exist_ok=True)
    root.joinpath("pangolier.yaml").write_text(
        yaml.safe_dump(
            {
                "hero_id": 120,
                "hero_slug": "pangolier",
                "localized_name": "Pangolier",
                "capabilities": [{"type": "mobility", "score": 0.8}],
                "requirements": [],
                "liabilities": [],
                "targets": [],
                "role_distribution": {},
                "provenance": {},
            },
            sort_keys=False,
        )
    )
    root.joinpath("vocab-gap-review.yaml").write_text(
        yaml.safe_dump(
            {
                "schema_version": 1,
                "reviews": {
                    "pangolier|capabilities|attack speed reduction|attack_speed_reduction": {
                        "gap_key": (
                            "pangolier|capabilities|attack speed reduction|"
                            "attack_speed_reduction"
                        ),
                        "hero_slug": "pangolier",
                        "bucket": "capabilities",
                        "candidate_term": "attack_speed_reduction",
                        "desired_action": "promote",
                    },
                    "largo|capabilities|ally damage amplification|damage_amp": {
                        "gap_key": "largo|capabilities|ally damage amplification|damage_amp",
                        "hero_slug": "largo",
                        "bucket": "capabilities",
                        "candidate_term": "damage_amp",
                        "desired_action": "rename",
                    }
                },
            },
            sort_keys=False,
        )
    )


def test_parse_vocabulary_proposals_writes_inbox(tmp_path: Path):
    response_path = tmp_path / "response.txt"
    response_path.write_text(json.dumps(_response_payload()))

    result = parse_vocabulary_proposals(tmp_path, response_path)

    raw = yaml.safe_load(result.proposals_path.read_text())
    assert result.parsed_count == 1
    assert result.added_count == 1
    assert raw["proposals"][0]["term"] == "attack_speed_reduction"
    assert raw["proposals"][0]["review_status"] == "pending"


def test_parse_vocabulary_proposals_preserves_human_review(monkeypatch, tmp_path: Path):
    response_path = tmp_path / "response.txt"
    response_path.write_text(json.dumps(_response_payload()))
    vocabulary_path = tmp_path / "vocabulary.yaml"
    vocabulary_path.write_text(yaml.safe_dump(_vocabulary_payload(), sort_keys=False))
    monkeypatch.setattr(proposals, "VOCABULARY_PATH", vocabulary_path)
    parse_vocabulary_proposals(tmp_path, response_path)
    proposal_id = yaml.safe_load(
        (tmp_path / "authored" / "vocab-proposals.yaml").read_text()
    )["proposals"][0]["proposal_id"]
    review_vocabulary_proposal(
        tmp_path,
        proposal_id,
        review_status="accepted",
        human_note="Promote after review.",
    )

    result = parse_vocabulary_proposals(tmp_path, response_path)

    raw = yaml.safe_load(result.proposals_path.read_text())
    assert result.updated_count == 1
    assert raw["proposals"][0]["review_status"] == "accepted"
    assert raw["proposals"][0]["human_note"] == "Promote after review."


def test_promote_vocabulary_updates_vocab_notes_and_proposal_status(
    monkeypatch,
    tmp_path: Path,
):
    response_path = tmp_path / "response.txt"
    response_path.write_text(json.dumps(_response_payload()))
    vocabulary_path = tmp_path / "vocabulary.yaml"
    notes_path = tmp_path / "kg-vocabulary-notes.md"
    vocabulary_path.write_text(yaml.safe_dump(_vocabulary_payload(), sort_keys=False))
    monkeypatch.setattr(proposals, "VOCABULARY_PATH", vocabulary_path)
    monkeypatch.setattr(proposals, "VOCABULARY_NOTES_PATH", notes_path)
    _write_grounding_files(tmp_path)

    parse_result = parse_vocabulary_proposals(tmp_path, response_path)
    proposal_id = yaml.safe_load(parse_result.proposals_path.read_text())["proposals"][0][
        "proposal_id"
    ]
    review_vocabulary_proposal(tmp_path, proposal_id, review_status="accepted")

    result = promote_vocabulary(tmp_path)

    vocabulary = yaml.safe_load(vocabulary_path.read_text())
    inbox = yaml.safe_load(parse_result.proposals_path.read_text())
    assert "attack_speed_reduction" in vocabulary["capabilities"]
    assert vocabulary["capabilities"]["attack_speed_reduction"]["status"] == "accepted"
    assert inbox["proposals"][0]["review_status"] == "promoted"
    assert "capabilities.attack_speed_reduction" in notes_path.read_text()
    assert result.promoted_terms == ["capabilities.attack_speed_reduction"]


def test_promote_vocabulary_refuses_ungrounded_terms(monkeypatch, tmp_path: Path):
    response_path = tmp_path / "response.txt"
    response_path.write_text(json.dumps(_response_payload()))
    vocabulary_path = tmp_path / "vocabulary.yaml"
    vocabulary_path.write_text(yaml.safe_dump(_vocabulary_payload(), sort_keys=False))
    monkeypatch.setattr(proposals, "VOCABULARY_PATH", vocabulary_path)

    parse_result = parse_vocabulary_proposals(tmp_path, response_path)
    proposal_id = yaml.safe_load(parse_result.proposals_path.read_text())["proposals"][0][
        "proposal_id"
    ]
    review_vocabulary_proposal(tmp_path, proposal_id, review_status="accepted")

    try:
        promote_vocabulary(tmp_path)
    except proposals.VocabularyProposalError as exc:
        assert "not grounded" in str(exc)
    else:
        raise AssertionError("expected ungrounded proposal to fail promotion")


def test_promote_vocabulary_reports_all_preflight_errors(monkeypatch, tmp_path: Path):
    response_path = tmp_path / "response.txt"
    response_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "proposals": [
                    {
                        "bucket": "capabilities",
                        "term": "missing_existing_term",
                        "action": "revise",
                        "definition": "Should fail because revise requires a live term.",
                        "include_when": [],
                        "exclude_when": [],
                        "examples": [{"hero_slug": "pangolier", "evidence": "grounded"}],
                        "enabled_rules": [],
                        "rationale": "",
                        "status": "proposed",
                    },
                    {
                        "bucket": "capabilities",
                        "term": "floating_term",
                        "action": "add",
                        "definition": "Should fail because it is ungrounded.",
                        "include_when": [],
                        "exclude_when": [],
                        "examples": [],
                        "enabled_rules": [],
                        "rationale": "",
                        "status": "proposed",
                    },
                ],
            }
        )
    )
    vocabulary_path = tmp_path / "vocabulary.yaml"
    vocabulary_path.write_text(yaml.safe_dump(_vocabulary_payload(), sort_keys=False))
    monkeypatch.setattr(proposals, "VOCABULARY_PATH", vocabulary_path)
    _write_grounding_files(tmp_path)

    parse_result = parse_vocabulary_proposals(tmp_path, response_path)
    inbox = yaml.safe_load(parse_result.proposals_path.read_text())
    for proposal in inbox["proposals"]:
        proposal["review_status"] = "accepted"
    parse_result.proposals_path.write_text(yaml.safe_dump(inbox, sort_keys=False))

    try:
        promote_vocabulary(tmp_path)
    except proposals.VocabularyProposalError as exc:
        message = str(exc)
        assert "missing_existing_term" in message
        assert "floating_term" in message
    else:
        raise AssertionError("expected preflight errors")


def test_amend_vocabulary_proposal_updates_action_and_id(tmp_path: Path):
    response_path = tmp_path / "response.txt"
    response_path.write_text(json.dumps(_response_payload()))
    parse_result = parse_vocabulary_proposals(tmp_path, response_path)
    old_id = yaml.safe_load(parse_result.proposals_path.read_text())["proposals"][0][
        "proposal_id"
    ]

    result = amend_vocabulary_proposal(
        tmp_path,
        old_id,
        action="defer",
        review_status="deferred",
        human_note="Corrected after review.",
    )

    raw = yaml.safe_load(parse_result.proposals_path.read_text())
    assert result.old_proposal_id == old_id
    assert result.new_proposal_id.endswith(":capabilities:attack_speed_reduction:defer")
    assert raw["proposals"][0]["proposal_id"] == result.new_proposal_id
    assert raw["proposals"][0]["action"] == "defer"
    assert raw["proposals"][0]["review_status"] == "deferred"
    assert raw["proposals"][0]["human_note"] == "Corrected after review."


def test_review_vocabulary_proposal_blocks_impossible_revise_acceptance(
    monkeypatch,
    tmp_path: Path,
):
    response_path = tmp_path / "response.txt"
    payload = _response_payload()
    payload["proposals"][0]["action"] = "revise"
    response_path.write_text(json.dumps(payload))
    vocabulary_path = tmp_path / "vocabulary.yaml"
    vocabulary_path.write_text(yaml.safe_dump(_vocabulary_payload(), sort_keys=False))
    monkeypatch.setattr(proposals, "VOCABULARY_PATH", vocabulary_path)

    parse_result = parse_vocabulary_proposals(tmp_path, response_path)
    proposal_id = yaml.safe_load(parse_result.proposals_path.read_text())["proposals"][0][
        "proposal_id"
    ]

    try:
        review_vocabulary_proposal(tmp_path, proposal_id, review_status="accepted")
    except proposals.VocabularyProposalError as exc:
        assert "cannot accept revise for missing live term" in str(exc)
    else:
        raise AssertionError("expected impossible revise acceptance to fail")


def test_promote_vocabulary_allows_child_term_from_grounded_split(
    monkeypatch,
    tmp_path: Path,
):
    response_path = tmp_path / "response.txt"
    response_path.write_text(json.dumps(_split_response_payload()))
    vocabulary_path = tmp_path / "vocabulary.yaml"
    notes_path = tmp_path / "kg-vocabulary-notes.md"
    vocabulary_path.write_text(yaml.safe_dump(_vocabulary_payload(), sort_keys=False))
    monkeypatch.setattr(proposals, "VOCABULARY_PATH", vocabulary_path)
    monkeypatch.setattr(proposals, "VOCABULARY_NOTES_PATH", notes_path)
    _write_grounding_files(tmp_path)

    parse_result = parse_vocabulary_proposals(tmp_path, response_path)
    inbox = yaml.safe_load(parse_result.proposals_path.read_text())
    for proposal in inbox["proposals"]:
        review_vocabulary_proposal(
            tmp_path,
            proposal["proposal_id"],
            review_status="accepted",
        )

    result = promote_vocabulary(tmp_path)

    vocabulary = yaml.safe_load(vocabulary_path.read_text())
    assert "damage_amp" in vocabulary["capabilities"]
    assert "physical_damage_amp" in vocabulary["capabilities"]
    assert "capabilities.physical_damage_amp" in result.promoted_terms


def test_promote_vocabulary_dry_run_does_not_write(monkeypatch, tmp_path: Path):
    response_path = tmp_path / "response.txt"
    response_path.write_text(json.dumps(_response_payload()))
    vocabulary_path = tmp_path / "vocabulary.yaml"
    notes_path = tmp_path / "kg-vocabulary-notes.md"
    vocabulary_path.write_text(yaml.safe_dump(_vocabulary_payload(), sort_keys=False))
    monkeypatch.setattr(proposals, "VOCABULARY_PATH", vocabulary_path)
    monkeypatch.setattr(proposals, "VOCABULARY_NOTES_PATH", notes_path)
    _write_grounding_files(tmp_path)

    parse_result = parse_vocabulary_proposals(tmp_path, response_path)
    proposal_id = yaml.safe_load(parse_result.proposals_path.read_text())["proposals"][0][
        "proposal_id"
    ]
    review_vocabulary_proposal(tmp_path, proposal_id, review_status="accepted")
    vocabulary_before = vocabulary_path.read_text()

    result = promote_vocabulary(tmp_path, dry_run=True)

    assert result.promoted_terms == ["capabilities.attack_speed_reduction"]
    assert result.promoted_ids == [proposal_id]
    assert vocabulary_path.read_text() == vocabulary_before
    assert not notes_path.exists()
    inbox = yaml.safe_load(parse_result.proposals_path.read_text())
    assert inbox["proposals"][0]["review_status"] == "accepted"
    assert "promoted_at" not in inbox["proposals"][0]


def test_promote_vocabulary_warns_when_new_terms_exceed_max_terms(
    monkeypatch,
    tmp_path: Path,
):
    response_path = tmp_path / "response.txt"
    response_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "proposals": [
                    {
                        "bucket": "capabilities",
                        "term": term,
                        "action": "add",
                        "definition": f"Definition for {term}.",
                        "include_when": [],
                        "exclude_when": [],
                        "examples": [
                            {"hero_slug": "pangolier", "evidence": f"Pangolier needs {term}."},
                        ],
                        "enabled_rules": [],
                        "rationale": "",
                        "status": "proposed",
                    }
                    for term in ("term_alpha", "term_beta", "term_gamma")
                ],
            }
        )
    )
    vocabulary_path = tmp_path / "vocabulary.yaml"
    vocabulary_path.write_text(yaml.safe_dump(_vocabulary_payload(), sort_keys=False))
    monkeypatch.setattr(proposals, "VOCABULARY_PATH", vocabulary_path)
    _write_grounding_files(tmp_path)

    parse_result = parse_vocabulary_proposals(tmp_path, response_path)
    inbox = yaml.safe_load(parse_result.proposals_path.read_text())
    for proposal in inbox["proposals"]:
        review_vocabulary_proposal(
            tmp_path,
            proposal["proposal_id"],
            review_status="accepted",
        )

    result = promote_vocabulary(tmp_path, max_terms=2, dry_run=True)

    assert len(result.warnings) == 1
    assert "3 new terms selected" in result.warnings[0]
    assert "more than 2" in result.warnings[0]


def test_promote_vocabulary_no_warning_when_under_max_terms(monkeypatch, tmp_path: Path):
    response_path = tmp_path / "response.txt"
    response_path.write_text(json.dumps(_response_payload()))
    vocabulary_path = tmp_path / "vocabulary.yaml"
    vocabulary_path.write_text(yaml.safe_dump(_vocabulary_payload(), sort_keys=False))
    monkeypatch.setattr(proposals, "VOCABULARY_PATH", vocabulary_path)
    _write_grounding_files(tmp_path)

    parse_result = parse_vocabulary_proposals(tmp_path, response_path)
    proposal_id = yaml.safe_load(parse_result.proposals_path.read_text())["proposals"][0][
        "proposal_id"
    ]
    review_vocabulary_proposal(tmp_path, proposal_id, review_status="accepted")

    result = promote_vocabulary(tmp_path, max_terms=10, dry_run=True)

    assert result.warnings == []
