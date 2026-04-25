from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

VOCABULARY_PATH = Path(__file__).with_name("vocabulary.yaml")
FEATURE_BUCKETS = ("capabilities", "requirements", "liabilities", "targets")
VOCABULARY_BUCKETS = FEATURE_BUCKETS + ("relation_patterns", "statistical_alignment")
LIVE_STATUS = "accepted"


class VocabularyError(ValueError):
    """Raised when the vocabulary metadata file cannot provide live term sets."""

    pass


def load_vocabulary(path: Path = VOCABULARY_PATH) -> dict[str, Any]:
    """Load and minimally validate the reviewable vocabulary metadata artifact."""

    raw = yaml.safe_load(path.read_text()) or {}
    if not isinstance(raw, dict):
        raise VocabularyError(f"{path} must parse to a YAML mapping")
    for bucket in VOCABULARY_BUCKETS:
        if bucket not in raw:
            raise VocabularyError(f"{path} missing vocabulary bucket {bucket!r}")
        if not isinstance(raw[bucket], dict):
            raise VocabularyError(f"{path} bucket {bucket!r} must be a mapping")
    return raw


def live_terms(bucket: str, *, path: Path = VOCABULARY_PATH) -> frozenset[str]:
    """Return accepted term keys for one vocabulary bucket."""

    raw = load_vocabulary(path)
    entries = raw[bucket]
    terms: set[str] = set()
    for term, metadata in entries.items():
        if not isinstance(term, str) or not term:
            raise VocabularyError(f"{path} bucket {bucket!r} contains an invalid term key")
        if not isinstance(metadata, dict):
            raise VocabularyError(f"{path} entry {bucket}.{term} must be a mapping")
        if metadata.get("status") == LIVE_STATUS:
            terms.add(term)
    return frozenset(terms)


CAPABILITIES = live_terms("capabilities")
REQUIREMENTS = live_terms("requirements")
LIABILITIES = live_terms("liabilities")
TARGETS = live_terms("targets")
RELATION_PATTERNS = live_terms("relation_patterns")
STATISTICAL_ALIGNMENT = live_terms("statistical_alignment")
