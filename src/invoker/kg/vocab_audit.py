from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from invoker.kg.infer import RULE_FEATURE_REFERENCES
from invoker.kg.vocabulary import (
    CAPABILITIES,
    FEATURE_BUCKETS,
    LIABILITIES,
    RELATION_PATTERNS,
    REQUIREMENTS,
    TARGETS,
)
from invoker.paths import authored_dir, vocab_gaps_file


@dataclass(frozen=True)
class AuthoredTermUse:
    """One observed authored fact term in a canonical hero YAML file."""

    path: Path
    hero_slug: str
    bucket: str
    term: str


@dataclass(frozen=True)
class RuleVocabularyError:
    """A rule reference that cannot be satisfied by the live vocabulary."""

    pattern: str
    bucket: str
    term: str
    reason: str


@dataclass(frozen=True)
class VocabularyAudit:
    """Combined audit result for authored facts, live vocabulary, and rule references."""

    authored_files: int
    vocabulary_gap_count: int
    unknown_authored_terms: list[AuthoredTermUse] = field(default_factory=list)
    unused_live_terms: dict[str, list[str]] = field(default_factory=dict)
    terms_without_rule: dict[str, list[str]] = field(default_factory=dict)
    rule_errors: list[RuleVocabularyError] = field(default_factory=list)
    relation_patterns_without_rule: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        """Return true when the audit found no blocking vocabulary errors."""

        return not self.unknown_authored_terms and not self.rule_errors


def _allowed_terms() -> dict[str, frozenset[str]]:
    """Map authored fact buckets to their live accepted term sets."""

    return {
        "capabilities": CAPABILITIES,
        "requirements": REQUIREMENTS,
        "liabilities": LIABILITIES,
        "targets": TARGETS,
    }


def _authored_fact_files(data_dir: Path) -> list[Path]:
    """List canonical authored hero YAML files, excluding drafts and review inboxes."""

    root = authored_dir(data_dir)
    if not root.exists():
        return []
    return [
        path
        for path in sorted(root.glob("*.yaml"))
        if not path.name.endswith(".draft.yaml") and not path.name.startswith("vocab-")
    ]


def _load_mapping(path: Path) -> dict[str, Any]:
    """Load a YAML mapping, treating non-mapping payloads as empty for audit purposes."""

    raw = yaml.safe_load(path.read_text()) or {}
    if not isinstance(raw, dict):
        return {}
    return raw


def _read_authored_terms(
    data_dir: Path,
) -> tuple[list[AuthoredTermUse], list[AuthoredTermUse], int]:
    """Collect authored term usage and separate terms outside live vocabulary."""

    allowed = _allowed_terms()
    used: list[AuthoredTermUse] = []
    unknown: list[AuthoredTermUse] = []
    files = _authored_fact_files(data_dir)
    for path in files:
        raw = _load_mapping(path)
        hero_slug = str(raw.get("hero_slug") or path.stem)
        for bucket in FEATURE_BUCKETS:
            items = raw.get(bucket, [])
            if not isinstance(items, list):
                continue
            for item in items:
                if not isinstance(item, dict):
                    continue
                term = item.get("type")
                if not isinstance(term, str) or not term:
                    continue
                use = AuthoredTermUse(path=path, hero_slug=hero_slug, bucket=bucket, term=term)
                used.append(use)
                if term not in allowed[bucket]:
                    unknown.append(use)
    return used, unknown, len(files)


def _read_vocab_gap_count(data_dir: Path) -> int:
    """Count unresolved vocabulary-gap inbox entries from Stage 3 authoring."""

    path = vocab_gaps_file(data_dir)
    if not path.exists():
        return 0
    raw = _load_mapping(path)
    gaps = raw.get("gaps", [])
    if not isinstance(gaps, list):
        return 0
    return sum(1 for item in gaps if isinstance(item, dict) and item.get("status") != "accepted")


def _rule_audit() -> tuple[dict[str, set[str]], list[RuleVocabularyError], list[str]]:
    """Check that deterministic rules only reference live features and patterns."""

    allowed = _allowed_terms()
    referenced: dict[str, set[str]] = {bucket: set() for bucket in FEATURE_BUCKETS}
    used_patterns: set[str] = set()
    errors: list[RuleVocabularyError] = []

    for ref in RULE_FEATURE_REFERENCES:
        referenced[ref.source_bucket].add(ref.source_feature)
        referenced[ref.target_bucket].add(ref.target_feature)
        used_patterns.add(ref.pattern)
        if ref.source_feature not in allowed[ref.source_bucket]:
            errors.append(
                RuleVocabularyError(
                    pattern=ref.pattern,
                    bucket=ref.source_bucket,
                    term=ref.source_feature,
                    reason="source feature is not live vocabulary",
                )
            )
        if ref.target_feature not in allowed[ref.target_bucket]:
            errors.append(
                RuleVocabularyError(
                    pattern=ref.pattern,
                    bucket=ref.target_bucket,
                    term=ref.target_feature,
                    reason="target feature is not live vocabulary",
                )
            )
        if ref.pattern not in RELATION_PATTERNS:
            errors.append(
                RuleVocabularyError(
                    pattern=ref.pattern,
                    bucket="relation_patterns",
                    term=ref.pattern,
                    reason="rule pattern is not live vocabulary",
                )
            )

    unused_patterns = sorted(RELATION_PATTERNS - used_patterns)
    return referenced, errors, unused_patterns


def run_vocab_audit(data_dir: Path) -> VocabularyAudit:
    """Run the Stage 4 vocabulary guardrail against the current local corpus."""

    used, unknown, authored_count = _read_authored_terms(data_dir)
    used_by_bucket = {
        bucket: {use.term for use in used if use.bucket == bucket} for bucket in FEATURE_BUCKETS
    }
    allowed = _allowed_terms()
    referenced, rule_errors, unused_patterns = _rule_audit()

    unused_live_terms = {
        bucket: sorted(terms - used_by_bucket[bucket])
        for bucket, terms in allowed.items()
        if terms - used_by_bucket[bucket]
    }
    terms_without_rule = {
        bucket: sorted(terms - referenced[bucket])
        for bucket, terms in allowed.items()
        if terms - referenced[bucket]
    }

    return VocabularyAudit(
        authored_files=authored_count,
        vocabulary_gap_count=_read_vocab_gap_count(data_dir),
        unknown_authored_terms=unknown,
        unused_live_terms=unused_live_terms,
        terms_without_rule=terms_without_rule,
        rule_errors=rule_errors,
        relation_patterns_without_rule=unused_patterns,
    )


def format_vocab_audit(audit: VocabularyAudit) -> str:
    """Render a human-readable audit report for the CLI."""

    lines = [
        "# Vocabulary Audit",
        "",
        f"Authored hero files: {audit.authored_files}",
        f"Open vocabulary gaps: {audit.vocabulary_gap_count}",
        f"Status: {'pass' if audit.passed else 'fail'}",
        "",
    ]

    if audit.unknown_authored_terms:
        lines.append("## Unknown Authored Terms")
        for use in audit.unknown_authored_terms:
            lines.append(f"- {use.path.name}: {use.hero_slug}.{use.bucket}.{use.term}")
        lines.append("")

    if audit.rule_errors:
        lines.append("## Rule Vocabulary Errors")
        for error in audit.rule_errors:
            lines.append(f"- {error.pattern}: {error.bucket}.{error.term} ({error.reason})")
        lines.append("")

    if audit.unused_live_terms:
        lines.append("## Unused Live Terms")
        for bucket, terms in audit.unused_live_terms.items():
            lines.append(f"- {bucket}: {', '.join(terms)}")
        lines.append("")

    if audit.terms_without_rule:
        lines.append("## Terms With No Consuming Rule")
        for bucket, terms in audit.terms_without_rule.items():
            lines.append(f"- {bucket}: {', '.join(terms)}")
        lines.append("")

    if audit.relation_patterns_without_rule:
        lines.append("## Relation Patterns With No Rule")
        lines.append(f"- {', '.join(audit.relation_patterns_without_rule)}")
        lines.append("")

    if audit.passed:
        lines.append("No blocking vocabulary errors found.")
    return "\n".join(lines) + "\n"
