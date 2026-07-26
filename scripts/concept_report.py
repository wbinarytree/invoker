"""Bucket report for a concept batch run (batch KB generation spec).

Groups every in-scope concept into clean / flagged / unguarded / failed
from disk state, annotating guard flags whose cited section anchor is
coverage-allowlisted boilerplate ("known boilerplate" — the packet still
carries those sections, so the guard may flag them; see spec). Markdown
to stdout.

Usage: uv run python scripts/concept_report.py [--patch 7.41d]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from invoker.config import Config  # noqa: E402
from invoker.corpus.store import CorpusStore  # noqa: E402
from invoker.gen.checks import COVERAGE_ALLOWLIST  # noqa: E402
from invoker.paths import corpus_dir, kb_dir, rejected_dir  # noqa: E402


def is_boilerplate_flag(section: str) -> bool:
    return section.rpartition("#")[2] in COVERAGE_ALLOWLIST


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--patch", default="7.41d")
    parser.add_argument("--host", default="liquipedia_dota2")
    args = parser.parse_args()

    cfg = Config.load()
    store = CorpusStore(corpus_dir(cfg.data_dir))
    kb = kb_dir(cfg.data_dir, args.patch)
    rejected = rejected_dir(cfg.data_dir, args.patch)

    buckets: dict[str, list[tuple[str, str]]] = {
        "clean": [], "flagged": [], "unguarded": [], "failed": [],
    }
    for slug in sorted(store.load_index(args.host).pages):
        entity_dir = kb / "concepts" / slug
        if not (entity_dir / "artifact.json").exists():
            attempts = rejected / "concepts" / slug
            note = ""
            if attempts.exists():
                last = sorted(attempts.iterdir())[-1]
                error = (last / "error.txt").read_text().strip()
                note = f"{error[:160]} — rejected output at {last}"
            buckets["failed"].append((slug, note))
            continue
        completeness = entity_dir / "completeness.json"
        if not completeness.exists():
            buckets["unguarded"].append((slug, "no completeness.json — re-guard"))
            continue
        missing = json.loads(completeness.read_text()).get("missing", [])
        if not missing:
            buckets["clean"].append((slug, ""))
            continue
        boilerplate = [m for m in missing if is_boilerplate_flag(m.get("section", ""))]
        substantive = len(missing) - len(boilerplate)
        note = f"{len(missing)} flags"
        if boilerplate:
            note += f" ({len(boilerplate)} known-boilerplate)"
        if substantive == 0:
            note += " — boilerplate-only"
        buckets["flagged"].append((slug, note))

    total = sum(len(v) for v in buckets.values())
    print(f"# Concept batch report — {args.patch}\n")
    print(f"{total} concepts: " + ", ".join(
        f"{len(v)} {name}" for name, v in buckets.items()))
    for name in ("clean", "flagged", "unguarded", "failed"):
        entries = buckets[name]
        if not entries:
            continue
        print(f"\n## {name} ({len(entries)})\n")
        if name == "clean":
            print(", ".join(slug for slug, _ in entries))
        else:
            for slug, note in entries:
                print(f"- **{slug}** — {note}" if note else f"- **{slug}**")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
