from __future__ import annotations

from pathlib import Path

from invoker.paths import summary_file
from invoker.schemas.derived import HeroDerived


def summarize(hero: HeroDerived, bracket: str) -> str:
    pos = hero.positions.get(bracket)
    pos_label = (
        "-".join(p for p, w in (pos.weights.items() if pos else {}) if w > 0) if pos else "unknown"
    )
    tags = ", ".join(hero.functional_tags)
    syns = [e for e in hero.synergies.get(bracket, []) if e.confidence in ("med", "high")][:3]
    cnts = [e for e in hero.counters.get(bracket, []) if e.confidence in ("med", "high")][:3]
    meta = hero.meta.get(bracket)

    history_line = ""
    if hero.meta_history:
        recent = [m for m in hero.meta_history if m.bracket == bracket][-3:]
        if len(recent) >= 2 and recent[0].tier != recent[-1].tier:
            history_line = f" [was {recent[0].tier} in {recent[0].patch}]"

    primary_tag = hero.functional_tags[0] if hero.functional_tags else "n/a"
    lines = [
        f"{hero.localized_name} [pos{pos_label} — {primary_tag}]",
        f"Functions: {tags}",
    ]
    if syns:
        lines.append(
            f"{bracket.capitalize()} synergies ({hero.source_patch}, med+): "
            + "; ".join(
                f"h{e.hero_id} {e.score:+.2f} ({e.games}g)" + (f" — {e.reason}" if e.reason else "")
                for e in syns
            )
        )
    if cnts:
        lines.append(
            f"{bracket.capitalize()} counters ({hero.source_patch}, med+): "
            + "; ".join(
                f"h{e.hero_id} {e.score:+.2f} ({e.games}g)" + (f" — {e.reason}" if e.reason else "")
                for e in cnts
            )
        )
    if meta:
        lines.append(
            f"{bracket.capitalize()} meta ({hero.source_patch}): "
            f"contest {meta.contest_rate:.0%}, win {meta.win_rate:.0%}, "
            f"tier: {meta.tier}{history_line}"
        )
    return "\n".join(lines) + "\n"


def write_summary(data_dir: Path, hero: HeroDerived, bracket: str) -> Path:
    path = summary_file(data_dir, hero.source_patch, bracket, hero.hero_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(summarize(hero, bracket))
    return path
