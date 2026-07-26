"""Sharded concept-generation driver (batch KB generation spec).

Shell-level orchestration: one `invoker generate-concept --backend codex`
subprocess per entity (fresh codex daemon each), a worker pool for
concurrency, a JSONL manifest per run, and a circuit breaker so an
unattended systematic breakage stops spending instead of running to the
end of the list. Never retries bad output; a transport-class failure
(no article was ever produced — nothing paid) is re-queued exactly once.

Usage:
  uv run python scripts/concept_batch.py --emit-only
  uv run python scripts/concept_batch.py --slugs map,turn_rate,lifesteal
  uv run python scripts/concept_batch.py --concurrency 8
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from invoker.config import Config  # noqa: E402
from invoker.corpus.store import CorpusStore  # noqa: E402
from invoker.paths import corpus_dir, kb_dir, rejected_dir  # noqa: E402

ENTITY_TIMEOUT_S = 15 * 60
STDERR_TAIL_CHARS = 500


def discover(store: CorpusStore, host: str, kb: Path) -> list[str]:
    index = store.load_index(host)
    return [
        slug
        for slug in sorted(index.pages)
        if not (kb / "concepts" / slug / "artifact.json").exists()
    ]


def bucket_for(entity_dir: Path) -> str:
    if not (entity_dir / "artifact.json").exists():
        return "failed"
    completeness = entity_dir / "completeness.json"
    if not completeness.exists():
        return "unguarded"
    missing = json.loads(completeness.read_text()).get("missing", [])
    return "clean" if not missing else "flagged"


class Breaker:
    """3 consecutive failures, or >30% failed after 10 attempts, halts."""

    def __init__(self, consecutive: int, rate: float, min_attempts: int) -> None:
        self._lock = threading.Lock()
        self._consecutive_limit = consecutive
        self._rate_limit = rate
        self._min_attempts = min_attempts
        self._consecutive = 0
        self._attempts = 0
        self._failures = 0
        self.tripped: str | None = None

    def record(self, failed: bool) -> None:
        with self._lock:
            self._attempts += 1
            if failed:
                self._failures += 1
                self._consecutive += 1
            else:
                self._consecutive = 0
            if self._consecutive >= self._consecutive_limit:
                self.tripped = f"{self._consecutive} consecutive failures"
            elif (
                self._attempts >= self._min_attempts
                and self._failures / self._attempts > self._rate_limit
            ):
                self.tripped = (
                    f"failure rate {self._failures}/{self._attempts} "
                    f"exceeds {self._rate_limit:.0%}"
                )


def run_entity(
    slug: str,
    *,
    patch: str,
    host: str,
    kb: Path,
    rejected: Path,
    requeued: bool,
    manifest: Path,
    manifest_lock: threading.Lock,
    breaker: Breaker,
) -> tuple[str, str]:
    """Run one generate-concept subprocess; returns (slug, bucket)."""
    entity_dir = kb / "concepts" / slug
    rejected_entity = rejected / "concepts" / slug
    started = time.monotonic()
    wall_start = time.time()
    started_at = datetime.now(UTC).isoformat()
    cmd = [
        "uv",
        "run",
        "invoker",
        "generate-concept",
        slug,
        "--patch",
        patch,
        "--host",
        host,
        "--backend",
        "codex",
    ]
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=ENTITY_TIMEOUT_S
        )
        exit_code = proc.returncode
        stderr_tail = proc.stderr[-STDERR_TAIL_CHARS:]
    except subprocess.TimeoutExpired as exc:
        exit_code = -1
        stderr_tail = f"timeout after {ENTITY_TIMEOUT_S}s: {exc}"

    bucket = bucket_for(entity_dir)
    # transport-class = nothing was ever paid for: no artifact AND no
    # rejected entry appeared during this attempt
    paid_evidence = rejected_entity.exists() and any(
        p.stat().st_mtime >= wall_start - 5 for p in rejected_entity.iterdir()
    )
    transport_class = bucket == "failed" and not paid_evidence

    line = {
        "slug": slug,
        "started_at": started_at,
        "duration_s": round(time.monotonic() - started, 1),
        "exit_code": exit_code,
        "bucket": bucket,
        "transport_class": transport_class,
        "requeued_attempt": requeued,
        "stderr_tail": stderr_tail,
    }
    with manifest_lock, manifest.open("a") as fh:
        fh.write(json.dumps(line) + "\n")
    breaker.record(bucket == "failed")
    print(f"[{line['duration_s']:7.1f}s] {slug}: {bucket}"
          + (" (transport)" if transport_class else ""))
    return slug, "transport" if transport_class else bucket


def run_pool(
    slugs: list[str], *, concurrency: int, breaker: Breaker, **entity_kwargs
) -> list[str]:
    """Run slugs through the pool with bounded submission (the breaker
    must be able to stop entities that have not been submitted yet);
    returns transport-class failures."""
    transport: list[str] = []
    queue = list(slugs)
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        in_flight = {
            pool.submit(run_entity, slug, **entity_kwargs)
            for slug in queue[:concurrency]
        }
        queue = queue[concurrency:]
        while in_flight:
            done = next(as_completed(in_flight))
            in_flight.remove(done)
            slug, outcome = done.result()
            if outcome == "transport":
                transport.append(slug)
            if queue and not breaker.tripped:
                in_flight.add(pool.submit(run_entity, queue.pop(0), **entity_kwargs))
        if queue:
            print(f"circuit breaker: {breaker.tripped} — "
                  f"{len(queue)} entities not attempted")
    return transport


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--patch", default="7.41d")
    parser.add_argument("--host", default="liquipedia_dota2")
    parser.add_argument("--concurrency", type=int, default=8)
    parser.add_argument("--slugs", help="comma-separated explicit list (pilot mode)")
    parser.add_argument("--emit-only", action="store_true")
    args = parser.parse_args()

    cfg = Config.load()
    store = CorpusStore(corpus_dir(cfg.data_dir))
    kb = kb_dir(cfg.data_dir, args.patch)
    rejected = rejected_dir(cfg.data_dir, args.patch)

    if args.slugs:
        slugs = [s.strip() for s in args.slugs.split(",") if s.strip()]
        pending = [
            s for s in slugs
            if not (kb / "concepts" / s / "artifact.json").exists()
        ]
        skipped = sorted(set(slugs) - set(pending))
        if skipped:
            print(f"skipping existing: {', '.join(skipped)}")
    else:
        pending = discover(store, args.host, kb)

    if args.emit_only:
        for slug in pending:
            print(slug)
        print(f"# {len(pending)} pending", file=sys.stderr)
        return 0

    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    batch_dir = cfg.data_dir / "logs" / "batch"
    batch_dir.mkdir(parents=True, exist_ok=True)
    manifest = batch_dir / f"concepts-{stamp}.jsonl"
    print(f"{len(pending)} entities, concurrency {args.concurrency}, "
          f"manifest {manifest}")

    breaker = Breaker(consecutive=3, rate=0.3, min_attempts=10)
    entity_kwargs = dict(
        patch=args.patch,
        host=args.host,
        kb=kb,
        rejected=rejected,
        manifest=manifest,
        manifest_lock=threading.Lock(),
        breaker=breaker,
    )
    transport = run_pool(
        pending, concurrency=args.concurrency, breaker=breaker,
        requeued=False, **entity_kwargs,
    )
    if transport and not breaker.tripped:
        print(f"re-queueing {len(transport)} transport-class failures once")
        run_pool(
            transport, concurrency=args.concurrency, breaker=breaker,
            requeued=True, **entity_kwargs,
        )

    if breaker.tripped:
        print(f"HALTED: circuit breaker — {breaker.tripped}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
