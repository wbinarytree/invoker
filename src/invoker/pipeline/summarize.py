from __future__ import annotations

from pathlib import Path

from invoker.kg.reader import RelationsReader
from invoker.paths import summary_file
from invoker.schemas.derived import HeroDerived


def _format_bucket(name: str, features: list) -> str | None:
    if not features:
        return None
    body = ", ".join(
        feature.type if feature.score is None else f"{feature.type} ({feature.score:.1f})"
        for feature in features
    )
    return f"- {name}: {body}"


def summarize(hero: HeroDerived, relations: RelationsReader) -> str:
    lines = [f"# {hero.localized_name}", ""]
    for bucket_name in ("capabilities", "requirements", "liabilities", "targets"):
        line = _format_bucket(bucket_name.capitalize(), getattr(hero, bucket_name))
        if line:
            lines.append(line)

    if hero.role_distribution:
        roles = ", ".join(f"{role}={weight:.2f}" for role, weight in hero.role_distribution.items())
        lines.append(f"- Role distribution: {roles}")

    lines.append("")
    synergies = relations.synergies_with(hero.hero_id)[:5]
    counters = [
        rel for rel in relations.relations_for(hero.hero_id) if rel.relation_kind == "counter"
    ][:5]

    if synergies:
        lines.append("## Synergies")
        for rel in synergies:
            lines.append(f"- {rel.relation_id}: {rel.mechanical_rationale}")
        lines.append("")

    if counters:
        lines.append("## Counters")
        for rel in counters:
            lines.append(f"- {rel.relation_id}: {rel.mechanical_rationale}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_summary(data_dir: Path, hero: HeroDerived, relations: RelationsReader) -> Path:
    path = summary_file(data_dir, hero.source_patch, hero.hero_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(summarize(hero, relations))
    return path
