from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from invoker.kg.vocabulary import FEATURE_BUCKETS, LIVE_STATUS, VOCABULARY_PATH, load_vocabulary
from invoker.llm.client import strip_fences
from invoker.paths import (
    authored_dir,
    vocab_gap_review_file,
    vocab_proposals_file,
    vocabulary_notes_file,
)

PROPOSAL_ACTIONS = frozenset({"add", "revise", "rename", "merge", "split", "remove", "defer"})
REVIEW_STATUSES = frozenset({"pending", "accepted", "rejected", "deferred"})
PROMOTABLE_ACTIONS = frozenset({"add", "revise", "rename", "split"})
VOCABULARY_NOTES_PATH = vocabulary_notes_file()


class VocabularyProposalError(ValueError):
    pass


@dataclass(frozen=True)
class ParseVocabularyProposalsResult:
    source_response_path: Path
    proposals_path: Path
    parsed_count: int
    added_count: int
    updated_count: int


@dataclass(frozen=True)
class ReviewVocabularyProposalResult:
    proposal_id: str
    review_status: str
    proposal_path: Path


@dataclass(frozen=True)
class AmendVocabularyProposalResult:
    old_proposal_id: str
    new_proposal_id: str
    proposal_path: Path


@dataclass(frozen=True)
class PromoteVocabularyResult:
    vocabulary_path: Path
    proposals_path: Path
    notes_path: Path
    promoted_ids: list[str]
    promoted_terms: list[str]
    warnings: list[str]


def _now() -> str:
    return datetime.now(UTC).isoformat()


def _load_yaml_mapping(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    raw = yaml.safe_load(path.read_text()) or {}
    if not isinstance(raw, dict):
        return {}
    return raw


def _write_yaml(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=False))


def _candidate_payloads(text: str) -> list[str]:
    stripped = text.strip()
    candidates = [stripped, strip_fences(stripped)]
    candidates.extend(
        block.strip()
        for block in re.findall(
            r"```(?:json)?\s*(.*?)```",
            text,
            flags=re.DOTALL | re.IGNORECASE,
        )
    )

    seen: set[str] = set()
    out: list[str] = []
    for candidate in candidates:
        if candidate and candidate not in seen:
            seen.add(candidate)
            out.append(candidate)
    return out


def _coerce_response_payload(text: str) -> dict[str, Any]:
    for candidate in _candidate_payloads(text):
        try:
            payload = json.loads(candidate)
        except json.JSONDecodeError:
            try:
                payload = yaml.safe_load(candidate) or {}
            except yaml.YAMLError:
                continue
        if isinstance(payload, dict):
            return payload
    raise VocabularyProposalError("LLM response must parse to a JSON object")


def _clean_term(term: object) -> str:
    if not isinstance(term, str) or not term.strip():
        raise VocabularyProposalError("proposal term must be a non-empty string")
    cleaned = term.strip()
    if not re.fullmatch(r"[a-z][a-z0-9_]*", cleaned):
        raise VocabularyProposalError(f"proposal term must be snake_case: {cleaned}")
    return cleaned


def _clean_bucket(bucket: object) -> str:
    if bucket not in FEATURE_BUCKETS and bucket != "relation_patterns":
        raise VocabularyProposalError(
            f"proposal bucket must be one of {sorted(FEATURE_BUCKETS + ('relation_patterns',))}"
        )
    return str(bucket)


def _clean_action(action: object) -> str:
    if action not in PROPOSAL_ACTIONS:
        raise VocabularyProposalError(f"proposal action must be one of {sorted(PROPOSAL_ACTIONS)}")
    return str(action)


def _as_string_list(value: object) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise VocabularyProposalError("proposal list fields must be arrays")
    return [str(item) for item in value if str(item).strip()]


def _as_mapping_list(value: object) -> list[dict[str, Any]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise VocabularyProposalError("proposal object-list fields must be arrays")
    return [item for item in value if isinstance(item, dict)]


def _proposal_id(source_response_path: Path, bucket: str, term: str, action: str) -> str:
    return f"{source_response_path.stem}:{bucket}:{term}:{action}"


def _proposal_source_path(proposal: dict[str, Any]) -> Path:
    source = proposal.get("source_response_path")
    if isinstance(source, str) and source:
        return Path(source)
    proposal_id = str(proposal.get("proposal_id", "manual:unknown:unknown:unknown"))
    return Path(proposal_id.split(":", maxsplit=1)[0])


def _normalize_proposal(raw: dict[str, Any], source_response_path: Path) -> dict[str, Any]:
    bucket = _clean_bucket(raw.get("bucket"))
    term = _clean_term(raw.get("term"))
    action = _clean_action(raw.get("action"))
    normalized: dict[str, Any] = {
        "proposal_id": _proposal_id(source_response_path, bucket, term, action),
        "bucket": bucket,
        "term": term,
        "action": action,
        "review_status": "pending",
        "source_response_path": str(source_response_path),
        "parsed_at": _now(),
        "definition": str(raw.get("definition") or ""),
        "include_when": _as_string_list(raw.get("include_when")),
        "exclude_when": _as_string_list(raw.get("exclude_when")),
        "examples": _as_mapping_list(raw.get("examples")),
        "enabled_rules": _as_mapping_list(raw.get("enabled_rules")),
        "rationale": str(raw.get("rationale") or ""),
        "llm_status": str(raw.get("status") or ""),
    }
    if raw.get("renames") is not None:
        normalized["renames"] = _clean_term(raw.get("renames"))
    if raw.get("merge_into") is not None:
        normalized["merge_into"] = _clean_term(raw.get("merge_into"))
    if raw.get("split_into") is not None:
        normalized["split_into"] = _as_string_list(raw.get("split_into"))
    return normalized


def _proposal_records(data_dir: Path) -> list[dict[str, Any]]:
    raw = _load_yaml_mapping(vocab_proposals_file(data_dir))
    proposals = raw.get("proposals", [])
    if not isinstance(proposals, list):
        return []
    return [proposal for proposal in proposals if isinstance(proposal, dict)]


def parse_vocabulary_proposals(
    data_dir: Path,
    source_response_path: Path,
) -> ParseVocabularyProposalsResult:
    """Parse one manual LLM response into the persistent proposal inbox."""

    payload = _coerce_response_payload(source_response_path.read_text())
    if payload.get("schema_version") != 1:
        raise VocabularyProposalError("vocabulary proposal response schema_version must be 1")
    raw_proposals = payload.get("proposals", [])
    if not isinstance(raw_proposals, list):
        raise VocabularyProposalError("vocabulary proposal response must contain proposals array")

    parsed = [
        _normalize_proposal(item, source_response_path)
        for item in raw_proposals
        if isinstance(item, dict)
    ]
    proposals_path = vocab_proposals_file(data_dir)
    raw = _load_yaml_mapping(proposals_path)
    raw.setdefault("schema_version", 1)
    proposals = raw.setdefault("proposals", [])
    if not isinstance(proposals, list):
        proposals = []
        raw["proposals"] = proposals

    existing_by_id = {
        proposal.get("proposal_id"): proposal
        for proposal in proposals
        if isinstance(proposal, dict) and isinstance(proposal.get("proposal_id"), str)
    }
    added = 0
    updated = 0
    for proposal in parsed:
        existing = existing_by_id.get(proposal["proposal_id"])
        if existing is None:
            proposals.append(proposal)
            added += 1
            continue
        review_fields = {
            key: existing[key]
            for key in ("review_status", "reviewed_at", "reviewer", "human_note", "promoted_at")
            if key in existing
        }
        existing.clear()
        existing.update(proposal)
        existing.update(review_fields)
        updated += 1

    rounds = raw.setdefault("parse_rounds", [])
    if isinstance(rounds, list):
        rounds.append(
            {
                "source_response_path": str(source_response_path),
                "parsed_at": _now(),
                "proposal_count": len(parsed),
                "added_count": added,
                "updated_count": updated,
            }
        )
    _write_yaml(proposals_path, raw)
    return ParseVocabularyProposalsResult(
        source_response_path=source_response_path,
        proposals_path=proposals_path,
        parsed_count=len(parsed),
        added_count=added,
        updated_count=updated,
    )


def iter_vocabulary_proposals(
    data_dir: Path,
    *,
    bucket: str | None = None,
    term: str | None = None,
    review_status: str | None = None,
    proposal_id: str | None = None,
) -> list[dict[str, Any]]:
    proposals = _proposal_records(data_dir)
    out: list[dict[str, Any]] = []
    for proposal in proposals:
        if bucket is not None and proposal.get("bucket") != bucket:
            continue
        if term is not None and proposal.get("term") != term:
            continue
        if review_status is not None and proposal.get("review_status") != review_status:
            continue
        if proposal_id is not None and proposal.get("proposal_id") != proposal_id:
            continue
        out.append(proposal)
    return out


def _live_vocab_entries(bucket: str) -> dict[str, Any]:
    vocabulary = load_vocabulary(VOCABULARY_PATH)
    raw_entries = vocabulary.get(bucket, {})
    if not isinstance(raw_entries, dict):
        return {}
    return {
        term: metadata
        for term, metadata in raw_entries.items()
        if isinstance(term, str)
        and isinstance(metadata, dict)
        and metadata.get("status") == LIVE_STATUS
    }


def _accepted_review_errors(proposal: dict[str, Any]) -> list[str]:
    """Return proposal/action mismatches that should block human acceptance."""

    bucket = str(proposal.get("bucket", ""))
    term = str(proposal.get("term", ""))
    action = str(proposal.get("action", ""))
    live_entries = _live_vocab_entries(bucket)
    if action == "revise" and term not in live_entries:
        return [
            f"cannot accept revise for missing live term {bucket}.{term}; "
            "amend the proposal to action=add, or reject/defer it"
        ]
    if action == "add" and term in live_entries:
        return [
            f"cannot accept add for existing live term {bucket}.{term}; "
            "amend the proposal to action=revise, or reject/defer it"
        ]
    if action == "rename" and term in live_entries:
        return [
            f"cannot accept rename to existing live term {bucket}.{term}; "
            "choose a different term, or reject/defer it"
        ]
    return []


def _validate_review_decision(proposal: dict[str, Any], review_status: str) -> None:
    if review_status != "accepted":
        return
    errors = _accepted_review_errors(proposal)
    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise VocabularyProposalError(f"cannot accept vocabulary proposal:\n{details}")


def review_vocabulary_proposal(
    data_dir: Path,
    proposal_id: str,
    *,
    review_status: str,
    human_note: str = "",
) -> ReviewVocabularyProposalResult:
    """Record a human decision on one proposal without deleting proposal history."""

    if review_status not in REVIEW_STATUSES - {"pending"}:
        raise VocabularyProposalError(
            f"review_status must be one of {sorted(REVIEW_STATUSES - {'pending'})}"
        )
    proposals_path = vocab_proposals_file(data_dir)
    raw = _load_yaml_mapping(proposals_path)
    proposals = raw.get("proposals", [])
    if not isinstance(proposals, list):
        raise VocabularyProposalError(f"{proposals_path} has no proposal list")
    for proposal in proposals:
        if isinstance(proposal, dict) and proposal.get("proposal_id") == proposal_id:
            _validate_review_decision(proposal, review_status)
            proposal["review_status"] = review_status
            proposal["reviewed_at"] = _now()
            proposal["reviewer"] = "human"
            proposal["human_note"] = human_note.strip()
            _write_yaml(proposals_path, raw)
            return ReviewVocabularyProposalResult(proposal_id, review_status, proposals_path)
    raise VocabularyProposalError(f"unknown proposal_id: {proposal_id}")


def amend_vocabulary_proposal(
    data_dir: Path,
    proposal_id: str,
    *,
    action: str | None = None,
    term: str | None = None,
    review_status: str | None = None,
    human_note: str | None = None,
) -> AmendVocabularyProposalResult:
    """Amend one proposal when the LLM chose the wrong action or term name."""

    proposals_path = vocab_proposals_file(data_dir)
    raw = _load_yaml_mapping(proposals_path)
    proposals = raw.get("proposals", [])
    if not isinstance(proposals, list):
        raise VocabularyProposalError(f"{proposals_path} has no proposal list")

    for proposal in proposals:
        if not isinstance(proposal, dict) or proposal.get("proposal_id") != proposal_id:
            continue
        old_proposal_id = str(proposal["proposal_id"])
        if action is not None:
            proposal["action"] = _clean_action(action)
        if term is not None:
            proposal["term"] = _clean_term(term)
        if review_status is not None:
            if review_status not in REVIEW_STATUSES:
                raise VocabularyProposalError(
                    f"review_status must be one of {sorted(REVIEW_STATUSES)}"
                )
            proposal["review_status"] = review_status
        _validate_review_decision(proposal, str(proposal.get("review_status", "")))
        if human_note is not None:
            proposal["human_note"] = human_note.strip()
        proposal["amended_at"] = _now()
        source_path = _proposal_source_path(proposal)
        proposal["proposal_id"] = _proposal_id(
            source_path,
            str(proposal["bucket"]),
            str(proposal["term"]),
            str(proposal["action"]),
        )
        _write_yaml(proposals_path, raw)
        return AmendVocabularyProposalResult(
            old_proposal_id=old_proposal_id,
            new_proposal_id=str(proposal["proposal_id"]),
            proposal_path=proposals_path,
        )
    raise VocabularyProposalError(f"unknown proposal_id: {proposal_id}")


def _authored_hero_slugs(data_dir: Path) -> set[str]:
    root = authored_dir(data_dir)
    if not root.exists():
        return set()
    slugs: set[str] = set()
    for path in root.glob("*.yaml"):
        if path.name.startswith("vocab-") or path.name.endswith(".draft.yaml"):
            continue
        raw = _load_yaml_mapping(path)
        slugs.add(str(raw.get("hero_slug") or path.stem))
    return slugs


def _authored_term_usage(data_dir: Path) -> set[tuple[str, str]]:
    used: set[tuple[str, str]] = set()
    root = authored_dir(data_dir)
    if not root.exists():
        return used
    for path in root.glob("*.yaml"):
        if path.name.startswith("vocab-") or path.name.endswith(".draft.yaml"):
            continue
        raw = _load_yaml_mapping(path)
        for bucket in FEATURE_BUCKETS:
            items = raw.get(bucket, [])
            if not isinstance(items, list):
                continue
            for item in items:
                if isinstance(item, dict) and isinstance(item.get("type"), str):
                    used.add((bucket, item["type"]))
    return used


def _gap_grounding(data_dir: Path, proposal: dict[str, Any]) -> list[str]:
    raw = _load_yaml_mapping(vocab_gap_review_file(data_dir))
    reviews = raw.get("reviews", {})
    if not isinstance(reviews, dict):
        return []

    candidates = {str(proposal.get("term", ""))}
    for key in ("renames", "merge_into"):
        if proposal.get(key):
            candidates.add(str(proposal[key]))
    examples = proposal.get("examples", [])
    example_heroes = {
        str(example.get("hero_slug"))
        for example in examples
        if isinstance(example, dict) and example.get("hero_slug")
    }

    grounded: list[str] = []
    for review in reviews.values():
        if not isinstance(review, dict):
            continue
        if review.get("bucket") != proposal.get("bucket"):
            continue
        if review.get("candidate_term") in candidates or review.get("hero_slug") in example_heroes:
            grounded.append(str(review.get("hero_slug") or review.get("gap_key") or "unknown"))
    return sorted(set(grounded))


def _split_parent_grounding(data_dir: Path, proposal: dict[str, Any]) -> list[str]:
    """Return grounding inherited from accepted split proposals that name this term."""

    bucket = proposal.get("bucket")
    term = proposal.get("term")
    grounded: set[str] = set()
    for parent in _proposal_records(data_dir):
        if parent is proposal:
            continue
        if parent.get("review_status") != "accepted":
            continue
        if parent.get("action") != "split" or parent.get("bucket") != bucket:
            continue
        split_into = parent.get("split_into", [])
        if not isinstance(split_into, list) or term not in split_into:
            continue
        grounded.update(_direct_proposal_grounding(data_dir, parent))
    return sorted(grounded)


def _direct_proposal_grounding(data_dir: Path, proposal: dict[str, Any]) -> list[str]:
    bucket = str(proposal.get("bucket"))
    term = str(proposal.get("term"))
    authored_usage = _authored_term_usage(data_dir)
    if (bucket, term) in authored_usage:
        return [term]

    hero_slugs = _authored_hero_slugs(data_dir)
    example_heroes = [
        str(example.get("hero_slug"))
        for example in proposal.get("examples", [])
        if isinstance(example, dict) and example.get("hero_slug") in hero_slugs
    ]
    grounded = sorted(set(example_heroes) | set(_gap_grounding(data_dir, proposal)))
    return grounded


def _proposal_grounding(data_dir: Path, proposal: dict[str, Any]) -> list[str]:
    direct = _direct_proposal_grounding(data_dir, proposal)
    if direct:
        return direct
    return _split_parent_grounding(data_dir, proposal)


def _metadata_from_proposal(proposal: dict[str, Any], *, introduced_in: str) -> dict[str, Any]:
    metadata = {
        "definition": str(proposal.get("definition") or ""),
        "include_when": _as_string_list(proposal.get("include_when")),
        "exclude_when": _as_string_list(proposal.get("exclude_when")),
        "examples": _as_mapping_list(proposal.get("examples")),
        "status": "accepted",
        "introduced_in": introduced_in,
    }
    return metadata


def _note_line(proposal: dict[str, Any], introduced_in: str) -> str:
    rationale = str(proposal.get("human_note") or proposal.get("rationale") or "").strip()
    suffix = f" - {rationale}" if rationale else ""
    return (
        f"- {introduced_in}: `{proposal.get('bucket')}.{proposal.get('term')}` "
        f"{proposal.get('action')} from `{proposal.get('proposal_id')}`.{suffix}"
    )


def promote_vocabulary(
    data_dir: Path,
    *,
    bucket: str | None = None,
    term: str | None = None,
    proposal_id: str | None = None,
    max_terms: int = 10,
    dry_run: bool = False,
) -> PromoteVocabularyResult:
    """Apply accepted vocabulary proposals to the canonical metadata artifact."""

    selected = iter_vocabulary_proposals(
        data_dir,
        bucket=bucket,
        term=term,
        proposal_id=proposal_id,
        review_status="accepted",
    )
    selected = [proposal for proposal in selected if proposal.get("action") in PROMOTABLE_ACTIONS]
    if not selected:
        raise VocabularyProposalError("no accepted promotable vocabulary proposals matched")

    new_terms = [
        proposal
        for proposal in selected
        if proposal.get("action") in {"add", "rename", "split"}
    ]
    warnings: list[str] = []
    if len(new_terms) > max_terms:
        warnings.append(
            f"{len(new_terms)} new terms selected; "
            f"review carefully before promoting more than {max_terms}"
        )

    vocabulary = load_vocabulary(VOCABULARY_PATH)
    introduced_in = datetime.now(UTC).date().isoformat()
    errors: list[str] = []
    for proposal in selected:
        proposal_bucket = str(proposal["bucket"])
        proposal_term = str(proposal["term"])
        grounding = _proposal_grounding(data_dir, proposal)
        if not grounding:
            errors.append(
                f"{proposal['proposal_id']}: not grounded by authored hero usage, "
                "reviewed gaps, or examples tied to authored heroes"
            )
        if proposal_bucket not in vocabulary or not isinstance(vocabulary[proposal_bucket], dict):
            errors.append(f"{proposal['proposal_id']}: unknown bucket {proposal_bucket}")
            continue
        bucket_entries = vocabulary[proposal_bucket]
        if proposal["action"] == "add" and proposal_term in bucket_entries:
            errors.append(
                f"{proposal['proposal_id']}: {proposal_bucket}.{proposal_term} already exists"
            )
        if proposal["action"] == "revise" and proposal_term not in bucket_entries:
            errors.append(
                f"{proposal['proposal_id']}: cannot revise missing term "
                f"{proposal_bucket}.{proposal_term}"
            )
    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise VocabularyProposalError(f"cannot promote vocabulary proposals:\n{details}")

    promoted_terms: list[str] = []
    promoted_ids: list[str] = []
    note_lines: list[str] = []

    for proposal in selected:
        proposal_bucket = str(proposal["bucket"])
        proposal_term = str(proposal["term"])
        bucket_entries = vocabulary[proposal_bucket]

        if proposal["action"] == "revise":
            bucket_entries[proposal_term].update(
                _metadata_from_proposal(proposal, introduced_in=introduced_in)
            )
        elif proposal["action"] == "rename":
            old_term = str(proposal.get("renames") or "")
            if old_term and old_term in bucket_entries:
                bucket_entries[old_term]["status"] = "deprecated"
                bucket_entries[old_term]["replaced_by"] = proposal_term
            bucket_entries[proposal_term] = _metadata_from_proposal(
                proposal,
                introduced_in=introduced_in,
            )
        elif proposal["action"] == "split":
            if proposal_term in bucket_entries:
                bucket_entries[proposal_term].update(
                    _metadata_from_proposal(proposal, introduced_in=introduced_in)
                )
            else:
                bucket_entries[proposal_term] = _metadata_from_proposal(
                    proposal,
                    introduced_in=introduced_in,
                )
        elif proposal["action"] == "add":
            bucket_entries[proposal_term] = _metadata_from_proposal(
                proposal,
                introduced_in=introduced_in,
            )
        promoted_ids.append(str(proposal["proposal_id"]))
        promoted_terms.append(f"{proposal_bucket}.{proposal_term}")
        note_lines.append(_note_line(proposal, introduced_in))

    proposals_path = vocab_proposals_file(data_dir)
    raw_proposals = _load_yaml_mapping(proposals_path)
    proposals = raw_proposals.get("proposals", [])
    if not isinstance(proposals, list):
        proposals = []
    if not dry_run:
        _write_yaml(VOCABULARY_PATH, vocabulary)
        for proposal in proposals:
            if isinstance(proposal, dict) and proposal.get("proposal_id") in promoted_ids:
                proposal["review_status"] = "promoted"
                proposal["promoted_at"] = _now()
        _write_yaml(proposals_path, raw_proposals)
        VOCABULARY_NOTES_PATH.parent.mkdir(parents=True, exist_ok=True)
        if not VOCABULARY_NOTES_PATH.exists():
            VOCABULARY_NOTES_PATH.write_text("# KG Vocabulary Notes\n\n")
        with VOCABULARY_NOTES_PATH.open("a") as fh:
            if note_lines:
                fh.write("\n".join(note_lines) + "\n")

    return PromoteVocabularyResult(
        vocabulary_path=VOCABULARY_PATH,
        proposals_path=proposals_path,
        notes_path=VOCABULARY_NOTES_PATH,
        promoted_ids=promoted_ids,
        promoted_terms=promoted_terms,
        warnings=warnings,
    )
