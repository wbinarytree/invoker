from pathlib import Path

import yaml

from invoker.kg.vocabulary_review import (
    iter_vocabulary_gap_contexts,
    iter_vocabulary_review_contexts,
    record_vocabulary_gap_review,
    record_vocabulary_review,
    render_vocabulary_revision_prompt,
)


def _hero_payload() -> dict:
    return {
        "hero_id": 999,
        "hero_slug": "testhero",
        "localized_name": "Test Hero",
        "capabilities": [
            {
                "type": "mobility",
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


def test_review_context_includes_usage_and_rules(tmp_path: Path):
    root = tmp_path / "authored"
    root.mkdir()
    root.joinpath("testhero.yaml").write_text(yaml.safe_dump(_hero_payload(), sort_keys=False))

    contexts = iter_vocabulary_review_contexts(
        tmp_path,
        bucket="capabilities",
        term="mobility",
    )

    assert len(contexts) == 1
    assert contexts[0].used_by == ["testhero"]
    assert contexts[0].consumed_by_rules == ["mobility_punish"]


def test_record_vocabulary_review_writes_yaml_and_log(tmp_path: Path):
    context = iter_vocabulary_review_contexts(
        tmp_path,
        bucket="capabilities",
        term="mobility",
    )[0]

    record = record_vocabulary_review(
        tmp_path,
        context,
        desired_action="revise",
        human_suggestion="Keep this for blink and dash style repositioning only.",
    )

    review_path = tmp_path / "authored" / "vocab-review.yaml"
    log_path = tmp_path / "authored" / "vocab-review-log.jsonl"
    review = yaml.safe_load(review_path.read_text())

    assert record.desired_action == "revise"
    assert review["reviews"]["capabilities"]["mobility"]["desired_action"] == "revise"
    assert "blink and dash" in review["reviews"]["capabilities"]["mobility"]["human_suggestion"]
    assert '"term": "mobility"' in log_path.read_text()


def test_render_vocabulary_revision_prompt_includes_review_notes(tmp_path: Path):
    context = iter_vocabulary_review_contexts(
        tmp_path,
        bucket="capabilities",
        term="mobility",
    )[0]
    record_vocabulary_review(
        tmp_path,
        context,
        desired_action="revise",
        human_suggestion="Do not use this for generic movement speed.",
    )

    prompt, version = render_vocabulary_revision_prompt(tmp_path, bucket="capabilities")

    assert version >= 1
    assert "Return JSON only." in prompt
    assert "Vocabulary context:" in prompt
    assert "Do not use this for generic movement speed." in prompt
    assert "mobility_punish" in prompt
    assert '"bucket": "capabilities"' in prompt


def test_render_vocabulary_revision_prompt_can_include_reviewed_only(tmp_path: Path):
    context = iter_vocabulary_review_contexts(
        tmp_path,
        bucket="capabilities",
        term="mobility",
    )[0]
    record_vocabulary_review(
        tmp_path,
        context,
        desired_action="keep",
        human_suggestion="This term is still useful.",
    )

    prompt, _ = render_vocabulary_revision_prompt(tmp_path, reviewed_only=True)

    assert '"term": "mobility"' in prompt
    assert '"term": "mana_burn"' not in prompt


def test_record_vocabulary_gap_review_writes_yaml_and_log(tmp_path: Path):
    root = tmp_path / "authored"
    root.mkdir()
    root.joinpath("vocab-gaps.yaml").write_text(
        yaml.safe_dump(
            {
                "gaps": [
                    {
                        "hero_slug": "pangolier",
                        "localized_name": "Pangolier",
                        "bucket": "capabilities",
                        "concept": "attack speed reduction",
                        "why_needed": "the current vocabulary has no attack speed term",
                        "evidence": "Lucky Shot can slow enemy attack speed",
                        "candidate_term": "attack_speed_reduction",
                        "status": "proposed",
                    }
                ]
            },
            sort_keys=False,
        )
    )
    context = iter_vocabulary_gap_contexts(
        tmp_path,
        bucket="capabilities",
        candidate_term="attack_speed_reduction",
    )[0]

    record = record_vocabulary_gap_review(
        tmp_path,
        context,
        desired_action="promote",
        human_suggestion="Promote this because Phoenix has the same mechanic.",
    )

    review_path = tmp_path / "authored" / "vocab-gap-review.yaml"
    log_path = tmp_path / "authored" / "vocab-gap-review-log.jsonl"
    review = yaml.safe_load(review_path.read_text())

    assert record.desired_action == "promote"
    assert review["reviews"][context.gap_key]["candidate_term"] == "attack_speed_reduction"
    assert "Phoenix" in review["reviews"][context.gap_key]["human_suggestion"]
    assert '"candidate_term": "attack_speed_reduction"' in log_path.read_text()


def test_render_vocabulary_revision_prompt_separates_reviewed_and_unreviewed_gaps(
    tmp_path: Path,
):
    root = tmp_path / "authored"
    root.mkdir()
    root.joinpath("vocab-gaps.yaml").write_text(
        yaml.safe_dump(
            {
                "gaps": [
                    {
                        "hero_slug": "pangolier",
                        "localized_name": "Pangolier",
                        "bucket": "capabilities",
                        "concept": "attack speed reduction",
                        "why_needed": "missing attack speed concept",
                        "evidence": "Lucky Shot can slow enemy attack speed",
                        "candidate_term": "attack_speed_reduction",
                        "status": "proposed",
                    },
                    {
                        "hero_slug": "riki",
                        "localized_name": "Riki",
                        "bucket": "capabilities",
                        "concept": "permanent invisibility",
                        "why_needed": "missing stealth concept",
                        "evidence": "Cloak and Dagger makes Riki invisible",
                        "candidate_term": "stealth",
                        "status": "proposed",
                    },
                ]
            },
            sort_keys=False,
        )
    )
    context = iter_vocabulary_gap_contexts(
        tmp_path,
        bucket="capabilities",
        candidate_term="attack_speed_reduction",
    )[0]
    record_vocabulary_gap_review(
        tmp_path,
        context,
        desired_action="promote",
        human_suggestion="Promote narrowly.",
    )

    prompt, _ = render_vocabulary_revision_prompt(tmp_path, bucket="capabilities")

    assert '"reviewed_vocabulary_gaps"' in prompt
    assert '"unreviewed_vocabulary_gaps"' in prompt
    assert '"candidate_term": "attack_speed_reduction"' in prompt
    assert '"candidate_term": "stealth"' in prompt
