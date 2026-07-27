"""Bucket report for a KB batch run (batch KB generation spec) —
concepts and items.

Groups every in-scope entity into clean / flagged / unguarded / failed
from disk state. Concept flags whose cited section anchor is
coverage-allowlisted boilerplate are annotated ("known boilerplate" —
the packet still carries those sections, so the guard may flag them;
see spec). Item flags whose fact is an internal ``item_*`` identifier
are annotated ("identifier" — the guard demands identifiers the prompt
forbids in prose; unresolvable class, see saved review 2026-07-27).
Substantive item flags are printed verbatim so the acceptance pass
reads the report, not 91 artifacts. Markdown to stdout.

Usage: uv run python scripts/concept_report.py [--kind item] [--patch 7.41d]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from concept_batch import item_scope, item_slug  # noqa: E402

from invoker.config import Config  # noqa: E402
from invoker.corpus.store import CorpusStore  # noqa: E402
from invoker.gen.checks import is_allowlisted_anchor  # noqa: E402
from invoker.paths import corpus_dir, kb_dir, rejected_dir  # noqa: E402

IDENTIFIER_FACT = re.compile(r"\bitem_[a-z0-9_]+")


def is_boilerplate_flag(section: str) -> bool:
    return is_allowlisted_anchor(section.rpartition("#")[2])


def annotate_concept(missing: list[dict]) -> tuple[str, list[str]]:
    boilerplate = [m for m in missing if is_boilerplate_flag(m.get("section", ""))]
    note = f"{len(missing)} flags"
    if boilerplate:
        note += f" ({len(boilerplate)} known-boilerplate)"
    if len(boilerplate) == len(missing):
        note += " — boilerplate-only"
    return note, []


def annotate_item(missing: list[dict]) -> tuple[str, list[str]]:
    identifier = [
        m for m in missing if IDENTIFIER_FACT.search(m.get("fact", ""))
    ]
    substantive = [m for m in missing if m not in identifier]
    note = f"{len(missing)} flags"
    if identifier:
        note += f" ({len(identifier)} identifier)"
    if not substantive:
        note += " — identifier-only"
    return note, [
        f"({m.get('section', '')}) {m.get('fact', '')}" for m in substantive
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("concept", "item"), default="concept")
    parser.add_argument("--patch", default="7.41d")
    parser.add_argument("--host", default="liquipedia_dota2")
    args = parser.parse_args()

    cfg = Config.load()
    kb = kb_dir(cfg.data_dir, args.patch)
    rejected = rejected_dir(cfg.data_dir, args.patch)

    if args.kind == "item":
        if cfg.game_data_dir is None:
            print("INVOKER_GAME_DATA_DIR is not configured", file=sys.stderr)
            return 1
        slugs = [item_slug(n) for n in item_scope(cfg.game_data_dir, args.patch)]
        annotate = annotate_item
    else:
        store = CorpusStore(corpus_dir(cfg.data_dir))
        slugs = sorted(store.load_index(args.host).pages)
        annotate = annotate_concept

    buckets: dict[str, list[tuple[str, str, list[str]]]] = {
        "clean": [], "flagged": [], "unguarded": [], "failed": [],
    }
    for slug in slugs:
        entity_dir = kb / f"{args.kind}s" / slug
        # item slugs are internal names (flask, devastator); show the
        # display name the artifact records (Healing Salve, Parasma)
        artifact_file = entity_dir / "artifact.json"
        if args.kind == "item" and artifact_file.exists():
            title = json.loads(artifact_file.read_text()).get("title", "")
            if title and title.lower() != slug.replace("_", " "):
                slug = f"{slug} ({title})"
        if not artifact_file.exists():
            attempts = rejected / f"{args.kind}s" / slug
            note = ""
            if attempts.exists():
                last = sorted(attempts.iterdir())[-1]
                error = (last / "error.txt").read_text().strip()
                note = f"{error[:160]} — rejected output at {last}"
            buckets["failed"].append((slug, note, []))
            continue
        completeness = entity_dir / "completeness.json"
        if not completeness.exists():
            buckets["unguarded"].append((slug, "no completeness.json — re-guard", []))
            continue
        missing = json.loads(completeness.read_text()).get("missing", [])
        if not missing:
            buckets["clean"].append((slug, "", []))
            continue
        note, facts = annotate(missing)
        buckets["flagged"].append((slug, note, facts))

    total = sum(len(v) for v in buckets.values())
    identifier_only = sum(
        1 for _, note, _ in buckets["flagged"] if note.endswith("identifier-only")
    )
    print(f"# {args.kind.capitalize()} batch report — {args.patch}\n")
    summary = f"{total} {args.kind}s: " + ", ".join(
        f"{len(v)} {name}" for name, v in buckets.items())
    if identifier_only:
        summary += f" ({identifier_only} identifier-only)"
    print(summary)
    for name in ("clean", "flagged", "unguarded", "failed"):
        entries = buckets[name]
        if not entries:
            continue
        print(f"\n## {name} ({len(entries)})\n")
        if name == "clean":
            print(", ".join(slug for slug, _, _ in entries))
        else:
            for slug, note, facts in entries:
                print(f"- **{slug}** — {note}" if note else f"- **{slug}**")
                for fact in facts:
                    print(f"  - {fact}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
