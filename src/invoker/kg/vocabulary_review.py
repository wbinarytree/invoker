from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from invoker.kg.infer import RULE_FEATURE_REFERENCES
from invoker.kg.vocab_audit import run_vocab_audit
from invoker.kg.vocabulary import VOCABULARY_BUCKETS, load_vocabulary
from invoker.llm.manual import ManualClient, PendingManualResponseError
from invoker.paths import (
    authored_dir,
    vocab_gap_review_file,
    vocab_gap_review_log_file,
    vocab_gaps_file,
    vocab_review_file,
    vocab_review_log_file,
)
from invoker.prompts import load

REVIEW_ACTIONS = frozenset({"keep", "revise", "rename", "merge", "split", "remove", "defer"})
GAP_REVIEW_ACTIONS = frozenset({"promote", "merge", "rename", "reject", "defer"})


@dataclass(frozen=True)
class VocabularyTermContext:
    """Human-facing review context for one vocabulary term."""

    bucket: str
    term: str
    metadata: dict[str, Any]
    used_by: list[str]
    consumed_by_rules: list[str]
    reviewed: bool


@dataclass(frozen=True)
class VocabularyReviewRecord:
    """One human review note captured outside the canonical vocabulary artifact."""

    bucket: str
    term: str
    desired_action: str
    human_suggestion: str
    reviewed_at: str
    current_status: str
    used_by: list[str]
    consumed_by_rules: list[str]


@dataclass(frozen=True)
class VocabularyGapContext:
    """Human-facing review context for one unresolved vocabulary gap."""

    gap_key: str
    hero_slug: str
    localized_name: str
    bucket: str
    concept: str
    candidate_term: str
    why_needed: str
    evidence: str
    status: str
    reviewed: bool


@dataclass(frozen=True)
class VocabularyGapReviewRecord:
    """One human review note for a proposed or missing vocabulary concept."""

    gap_key: str
    hero_slug: str
    bucket: str
    concept: str
    candidate_term: str
    desired_action: str
    human_suggestion: str
    reviewed_at: str
    gap_status: str


@dataclass(frozen=True)
class VocabularyPromptResult:
    """Paths for the manual LLM prompt handoff."""

    prompt_path: Path
    response_path: Path
    pending: bool


def _load_yaml_mapping(path: Path) -> dict[str, Any]:
    """Load a YAML mapping, returning an empty mapping when the file is absent."""

    if not path.exists():
        return {}
    raw = yaml.safe_load(path.read_text()) or {}
    if not isinstance(raw, dict):
        return {}
    return raw


def _authored_fact_files(data_dir: Path) -> list[Path]:
    """List canonical authored hero YAML files that can consume vocabulary terms."""

    root = authored_dir(data_dir)
    if not root.exists():
        return []
    return [
        path
        for path in sorted(root.glob("*.yaml"))
        if not path.name.endswith(".draft.yaml") and not path.name.startswith("vocab-")
    ]


def _usage_by_term(data_dir: Path) -> dict[tuple[str, str], set[str]]:
    """Map each authored feature term to the hero slugs that currently use it."""

    usage: dict[tuple[str, str], set[str]] = {}
    for path in _authored_fact_files(data_dir):
        raw = _load_yaml_mapping(path)
        hero_slug = str(raw.get("hero_slug") or path.stem)
        for bucket in ("capabilities", "requirements", "liabilities", "targets"):
            items = raw.get(bucket, [])
            if not isinstance(items, list):
                continue
            for item in items:
                if not isinstance(item, dict):
                    continue
                term = item.get("type")
                if isinstance(term, str) and term:
                    usage.setdefault((bucket, term), set()).add(hero_slug)
    return usage


def _rules_by_term() -> dict[tuple[str, str], set[str]]:
    """Map each vocabulary feature or relation pattern to rule patterns using it."""

    rules: dict[tuple[str, str], set[str]] = {}
    for ref in RULE_FEATURE_REFERENCES:
        rules.setdefault((ref.source_bucket, ref.source_feature), set()).add(ref.pattern)
        rules.setdefault((ref.target_bucket, ref.target_feature), set()).add(ref.pattern)
        rules.setdefault(("relation_patterns", ref.pattern), set()).add(ref.pattern)
    return rules


def _review_lookup(data_dir: Path) -> dict[tuple[str, str], dict[str, Any]]:
    """Index existing review records by bucket and term for resume behavior."""

    raw = _load_yaml_mapping(vocab_review_file(data_dir))
    reviews = raw.get("reviews", {})
    if not isinstance(reviews, dict):
        return {}

    out: dict[tuple[str, str], dict[str, Any]] = {}
    for bucket, terms in reviews.items():
        if not isinstance(bucket, str) or not isinstance(terms, dict):
            continue
        for term, record in terms.items():
            if isinstance(term, str) and isinstance(record, dict):
                out[(bucket, term)] = record
    return out


def _gap_key(gap: dict[str, Any]) -> str:
    """Build a stable key for a vocabulary gap captured from authored hero review."""

    parts = [
        str(gap.get("hero_slug", "")),
        str(gap.get("bucket", "")),
        str(gap.get("concept", "")),
        str(gap.get("candidate_term", "")),
    ]
    return "|".join(parts)


def _gap_review_lookup(data_dir: Path) -> dict[str, dict[str, Any]]:
    """Index existing vocabulary-gap review records by stable gap key."""

    raw = _load_yaml_mapping(vocab_gap_review_file(data_dir))
    reviews = raw.get("reviews", {})
    if not isinstance(reviews, dict):
        return {}
    return {key: value for key, value in reviews.items() if isinstance(value, dict)}


def iter_vocabulary_gap_contexts(
    data_dir: Path,
    *,
    bucket: str | None = None,
    candidate_term: str | None = None,
    include_reviewed: bool = False,
) -> list[VocabularyGapContext]:
    """Return review contexts for unresolved vocabulary gaps, optionally narrowed."""

    reviews = _gap_review_lookup(data_dir)
    contexts: list[VocabularyGapContext] = []
    for gap in _gap_records(data_dir, bucket=bucket):
        if candidate_term is not None and gap.get("candidate_term") != candidate_term:
            continue
        gap_key = _gap_key(gap)
        reviewed = gap_key in reviews
        if reviewed and not include_reviewed:
            continue
        contexts.append(
            VocabularyGapContext(
                gap_key=gap_key,
                hero_slug=str(gap.get("hero_slug", "")),
                localized_name=str(gap.get("localized_name", "")),
                bucket=str(gap.get("bucket", "")),
                concept=str(gap.get("concept", "")),
                candidate_term=str(gap.get("candidate_term", "")),
                why_needed=str(gap.get("why_needed", "")),
                evidence=str(gap.get("evidence", "")),
                status=str(gap.get("status", "")),
                reviewed=reviewed,
            )
        )
    return contexts


def iter_vocabulary_review_contexts(
    data_dir: Path,
    *,
    bucket: str | None = None,
    term: str | None = None,
    include_reviewed: bool = False,
) -> list[VocabularyTermContext]:
    """Return review contexts for live vocabulary terms, optionally narrowed."""

    vocabulary = load_vocabulary()
    usage = _usage_by_term(data_dir)
    rules = _rules_by_term()
    reviewed = _review_lookup(data_dir)
    contexts: list[VocabularyTermContext] = []

    for bucket_name in VOCABULARY_BUCKETS:
        if bucket is not None and bucket_name != bucket:
            continue
        entries = vocabulary[bucket_name]
        for term_name, metadata in entries.items():
            if term is not None and term_name != term:
                continue
            is_reviewed = (bucket_name, term_name) in reviewed
            if is_reviewed and not include_reviewed:
                continue
            contexts.append(
                VocabularyTermContext(
                    bucket=bucket_name,
                    term=term_name,
                    metadata=metadata,
                    used_by=sorted(usage.get((bucket_name, term_name), set())),
                    consumed_by_rules=sorted(rules.get((bucket_name, term_name), set())),
                    reviewed=is_reviewed,
                )
            )
    return contexts


def _serialize_context(context: VocabularyTermContext) -> dict[str, Any]:
    """Convert a review context into the compact packet used by LLM prompts."""

    metadata = context.metadata
    packet: dict[str, Any] = {
        "bucket": context.bucket,
        "term": context.term,
        "status": metadata.get("status"),
        "definition": metadata.get("definition", ""),
        "include_when": metadata.get("include_when", []),
        "exclude_when": metadata.get("exclude_when", []),
        "examples": metadata.get("examples", []),
        "used_by": context.used_by,
        "consumed_by_rules": context.consumed_by_rules,
    }
    if metadata.get("introduced_in") is not None:
        packet["introduced_in"] = metadata["introduced_in"]
    return packet


def _review_record_payload(record: VocabularyReviewRecord) -> dict[str, Any]:
    """Convert one review record to the YAML/JSONL persistence shape."""

    return {
        "bucket": record.bucket,
        "term": record.term,
        "reviewed_at": record.reviewed_at,
        "reviewer": "human",
        "current_status": record.current_status,
        "desired_action": record.desired_action,
        "human_suggestion": record.human_suggestion,
        "used_by": record.used_by,
        "consumed_by_rules": record.consumed_by_rules,
    }


def record_vocabulary_review(
    data_dir: Path,
    context: VocabularyTermContext,
    *,
    desired_action: str,
    human_suggestion: str,
) -> VocabularyReviewRecord:
    """Persist one human vocabulary note to YAML and append-only JSONL."""

    if desired_action not in REVIEW_ACTIONS:
        raise ValueError(f"desired_action must be one of {sorted(REVIEW_ACTIONS)}")
    record = VocabularyReviewRecord(
        bucket=context.bucket,
        term=context.term,
        desired_action=desired_action,
        human_suggestion=human_suggestion.strip(),
        reviewed_at=datetime.now(UTC).isoformat(),
        current_status=str(context.metadata.get("status", "")),
        used_by=context.used_by,
        consumed_by_rules=context.consumed_by_rules,
    )
    payload = _review_record_payload(record)

    review_path = vocab_review_file(data_dir)
    raw = _load_yaml_mapping(review_path)
    raw.setdefault("schema_version", 1)
    reviews = raw.setdefault("reviews", {})
    if not isinstance(reviews, dict):
        reviews = {}
        raw["reviews"] = reviews
    bucket_reviews = reviews.setdefault(context.bucket, {})
    if not isinstance(bucket_reviews, dict):
        bucket_reviews = {}
        reviews[context.bucket] = bucket_reviews
    bucket_reviews[context.term] = payload

    review_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.write_text(yaml.safe_dump(raw, sort_keys=False, allow_unicode=False))

    log_path = vocab_review_log_file(data_dir)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a") as fh:
        fh.write(json.dumps(payload, sort_keys=True) + "\n")

    return record


def _gap_review_record_payload(record: VocabularyGapReviewRecord) -> dict[str, Any]:
    """Convert one gap review record to the YAML/JSONL persistence shape."""

    return {
        "gap_key": record.gap_key,
        "hero_slug": record.hero_slug,
        "bucket": record.bucket,
        "concept": record.concept,
        "candidate_term": record.candidate_term,
        "reviewed_at": record.reviewed_at,
        "reviewer": "human",
        "gap_status": record.gap_status,
        "desired_action": record.desired_action,
        "human_suggestion": record.human_suggestion,
    }


def record_vocabulary_gap_review(
    data_dir: Path,
    context: VocabularyGapContext,
    *,
    desired_action: str,
    human_suggestion: str,
) -> VocabularyGapReviewRecord:
    """Persist one human note for a vocabulary gap proposal."""

    if desired_action not in GAP_REVIEW_ACTIONS:
        raise ValueError(f"desired_action must be one of {sorted(GAP_REVIEW_ACTIONS)}")
    record = VocabularyGapReviewRecord(
        gap_key=context.gap_key,
        hero_slug=context.hero_slug,
        bucket=context.bucket,
        concept=context.concept,
        candidate_term=context.candidate_term,
        desired_action=desired_action,
        human_suggestion=human_suggestion.strip(),
        reviewed_at=datetime.now(UTC).isoformat(),
        gap_status=context.status,
    )
    payload = _gap_review_record_payload(record)

    review_path = vocab_gap_review_file(data_dir)
    raw = _load_yaml_mapping(review_path)
    raw.setdefault("schema_version", 1)
    reviews = raw.setdefault("reviews", {})
    if not isinstance(reviews, dict):
        reviews = {}
        raw["reviews"] = reviews
    reviews[context.gap_key] = payload

    review_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.write_text(yaml.safe_dump(raw, sort_keys=False, allow_unicode=False))

    log_path = vocab_gap_review_log_file(data_dir)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a") as fh:
        fh.write(json.dumps(payload, sort_keys=True) + "\n")

    return record


def _review_records_for_terms(
    data_dir: Path,
    contexts: list[VocabularyTermContext],
) -> list[dict[str, Any]]:
    """Return persisted human review records matching the selected prompt scope."""

    selected = {(context.bucket, context.term) for context in contexts}
    return [
        record
        for key, record in _review_lookup(data_dir).items()
        if key in selected
    ]


def _gap_review_records_for_bucket(
    data_dir: Path,
    *,
    bucket: str | None = None,
) -> list[dict[str, Any]]:
    """Return persisted gap review records matching the selected prompt bucket."""

    records = _gap_review_lookup(data_dir).values()
    return [
        record
        for record in records
        if bucket is None or record.get("bucket") == bucket
    ]


def _gap_records(data_dir: Path, *, bucket: str | None = None) -> list[dict[str, Any]]:
    """Return vocabulary gaps relevant to the selected bucket."""

    raw = _load_yaml_mapping(vocab_gaps_file(data_dir))
    gaps = raw.get("gaps", [])
    if not isinstance(gaps, list):
        return []
    out: list[dict[str, Any]] = []
    for item in gaps:
        if not isinstance(item, dict):
            continue
        if bucket is not None and item.get("bucket") != bucket:
            continue
        out.append(item)
    return out


def _unreviewed_gap_records(data_dir: Path, *, bucket: str | None = None) -> list[dict[str, Any]]:
    """Return gap records that do not yet have human review notes."""

    reviewed = set(_gap_review_lookup(data_dir))
    return [gap for gap in _gap_records(data_dir, bucket=bucket) if _gap_key(gap) not in reviewed]


def _audit_summary(data_dir: Path, *, bucket: str | None = None) -> dict[str, Any]:
    """Compress audit output to the fields the LLM needs for vocabulary revision."""

    audit = run_vocab_audit(data_dir)

    def _filter_bucket_map(values: dict[str, list[str]]) -> dict[str, list[str]]:
        if bucket is None:
            return values
        return {bucket: values.get(bucket, [])} if values.get(bucket) else {}

    return {
        "passed": audit.passed,
        "authored_files": audit.authored_files,
        "open_vocabulary_gap_count": audit.vocabulary_gap_count,
        "unknown_authored_terms": [
            {
                "file": use.path.name,
                "hero_slug": use.hero_slug,
                "bucket": use.bucket,
                "term": use.term,
            }
            for use in audit.unknown_authored_terms
            if bucket is None or use.bucket == bucket
        ],
        "rule_errors": [
            {
                "pattern": error.pattern,
                "bucket": error.bucket,
                "term": error.term,
                "reason": error.reason,
            }
            for error in audit.rule_errors
            if bucket is None or error.bucket == bucket
        ],
        "unused_live_terms": _filter_bucket_map(audit.unused_live_terms),
        "terms_without_rule": _filter_bucket_map(audit.terms_without_rule),
        "relation_patterns_without_rule": (
            audit.relation_patterns_without_rule
            if bucket in {None, "relation_patterns"}
            else []
        ),
    }


def render_vocabulary_revision_prompt(
    data_dir: Path,
    *,
    bucket: str | None = None,
    term: str | None = None,
    reviewed_only: bool = False,
) -> tuple[str, int]:
    """Compose a compact JSON-output LLM prompt from selected vocabulary review context."""

    prompt = load("revise_vocabulary")
    contexts = iter_vocabulary_review_contexts(
        data_dir,
        bucket=bucket,
        term=term,
        include_reviewed=True,
    )
    if reviewed_only:
        contexts = [context for context in contexts if context.reviewed]

    context_packet = {
        "scope": {
            "bucket": bucket,
            "term": term,
            "reviewed_only": reviewed_only,
        },
        "audit_summary": _audit_summary(data_dir, bucket=bucket),
        "terms": [_serialize_context(context) for context in contexts],
        "human_reviews": _review_records_for_terms(data_dir, contexts),
        "reviewed_vocabulary_gaps": _gap_review_records_for_bucket(data_dir, bucket=bucket),
        "unreviewed_vocabulary_gaps": _unreviewed_gap_records(data_dir, bucket=bucket),
    }
    context_json = json.dumps(context_packet, indent=2, sort_keys=True)

    rendered = prompt.render(
        VOCABULARY_CONTEXT_JSON=context_json,
    )
    return rendered, prompt.version


def write_vocabulary_revision_prompt(
    data_dir: Path,
    *,
    bucket: str | None = None,
    term: str | None = None,
    reviewed_only: bool = False,
) -> VocabularyPromptResult:
    """Write the composed vocabulary prompt into the manual LLM handoff directories."""

    prompt_text, prompt_version = render_vocabulary_revision_prompt(
        data_dir,
        bucket=bucket,
        term=term,
        reviewed_only=reviewed_only,
    )
    client = ManualClient(
        inbox=data_dir / "raw" / "manual_prompts",
        outbox=data_dir / "raw" / "manual_responses",
    )
    scope = ["revise-vocabulary"]
    if bucket is not None:
        scope.append(bucket)
    if term is not None:
        scope.append(term)
    cache_tag = "/".join(scope)
    try:
        client.generate_json(
            prompt_text,
            prompt_version=prompt_version,
            cache_tag=cache_tag,
        )
    except PendingManualResponseError as exc:
        return VocabularyPromptResult(
            prompt_path=exc.prompt_path,
            response_path=exc.response_path,
            pending=True,
        )

    prompt_path, response_path = client._paths(prompt_text, cache_tag)
    return VocabularyPromptResult(
        prompt_path=prompt_path,
        response_path=response_path,
        pending=False,
    )
