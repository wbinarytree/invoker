"""Unit tests for the batch driver's pure decision logic — the breaker
and bucket classification stand between an unattended fleet run and
six-figure token spend."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))

from concept_batch import Breaker, bucket_for, is_transport_class


def make_breaker() -> Breaker:
    return Breaker(consecutive=3, rate=0.3, min_attempts=10)


def test_breaker_trips_on_consecutive_failures():
    breaker = make_breaker()
    for _ in range(2):
        breaker.record(failed=True)
    assert breaker.tripped is None
    breaker.record(failed=True)
    assert breaker.tripped == "3 consecutive failures"


def test_breaker_success_resets_the_consecutive_count():
    breaker = make_breaker()
    for _ in range(2):
        breaker.record(failed=True)
    breaker.record(failed=False)
    for _ in range(2):
        breaker.record(failed=True)
    assert breaker.tripped is None


def test_breaker_rate_trip_waits_for_min_attempts():
    breaker = make_breaker()
    # 2 failures in 4 attempts is 50% — but below min_attempts, no trip
    for failed in (True, False, True, False):
        breaker.record(failed=failed)
    assert breaker.tripped is None
    # alternate up to 10 attempts: 5/10 = 50% > 30% trips on the boundary
    for failed in (True, False, True, False, True, False):
        breaker.record(failed=failed)
    assert breaker.tripped is not None
    assert "exceeds 30%" in breaker.tripped


def test_bucket_for_disk_states(tmp_path):
    assert bucket_for(tmp_path / "absent") == "failed"

    unguarded = tmp_path / "unguarded"
    unguarded.mkdir()
    (unguarded / "artifact.json").write_text("{}")
    assert bucket_for(unguarded) == "unguarded"

    clean = tmp_path / "clean"
    clean.mkdir()
    (clean / "artifact.json").write_text("{}")
    (clean / "completeness.json").write_text(json.dumps({"missing": []}))
    assert bucket_for(clean) == "clean"

    flagged = tmp_path / "flagged"
    flagged.mkdir()
    (flagged / "artifact.json").write_text("{}")
    (flagged / "completeness.json").write_text(
        json.dumps({"missing": [{"section": "s", "fact": "f"}]})
    )
    assert bucket_for(flagged) == "flagged"


def test_transport_class_requires_unpaid_failure():
    assert is_transport_class("failed", paid_evidence=False, timed_out=False)
    # a rejected entry means the tokens were spent — never re-queue
    assert not is_transport_class("failed", paid_evidence=True, timed_out=False)
    # a timeout kill 15 minutes in likely interrupted a paid call whose
    # reject was never written — the double-pay window from the review
    assert not is_transport_class("failed", paid_evidence=False, timed_out=True)
    assert not is_transport_class("flagged", paid_evidence=False, timed_out=False)
