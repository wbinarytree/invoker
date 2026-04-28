from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from invoker.graph import build_graph, cache_graph
from invoker.kg import (
    HeroFactProfile,
    RelationsReader,
    infer_relations,
    load_hero_facts,
    write_relations,
)
from invoker.paths import authored_dir, hero_file, relations_file
from invoker.pipeline.manifest import build_manifest, write_manifest
from invoker.pipeline.summarize import write_summary
from invoker.pipeline.validators import ValidationContext, validate_hero
from invoker.pipeline.writer import write_hero
from invoker.schemas.derived import HeroDerived


@dataclass
class HeroResult:
    hero_id: int
    success: bool
    hero_slug: str | None = None
    failure_reason: str | None = None


def _now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def _to_derived(
    profile: HeroFactProfile,
    *,
    generator_version: str,
    generated_at: str,
) -> HeroDerived:
    return HeroDerived(
        generator_version=generator_version,
        source_patch=profile.source_patch,
        generated_at=generated_at,
        hero_id=profile.hero_id,
        hero_slug=profile.hero_slug,
        localized_name=profile.localized_name,
        capabilities=profile.capabilities,
        requirements=profile.requirements,
        liabilities=profile.liabilities,
        targets=profile.targets,
        role_distribution=profile.role_distribution,
        provenance=profile.provenance,
    )


def _is_canonical_authored_file(path: Path) -> bool:
    return (
        path.suffix == ".yaml"
        and not path.name.endswith(".draft.yaml")
        and not path.name.startswith("vocab-")
    )


def discover_authored_files(data_dir: Path, heroes: set[str] | None = None) -> list[Path]:
    root = authored_dir(data_dir)
    files = [path for path in sorted(root.glob("*.yaml")) if _is_canonical_authored_file(path)]
    if heroes is None:
        return files

    wanted = {token.strip().lower() for token in heroes if token.strip()}
    selected: list[Path] = []
    for path in files:
        profile = load_hero_facts(path, source_patch="__filter__", cohort="pub")
        tokens = {path.stem.lower(), profile.localized_name.lower(), str(profile.hero_id)}
        if tokens & wanted:
            selected.append(path)
    return selected


def load_profiles(
    data_dir: Path,
    patch: str,
    *,
    cohort: str = "pub",
    heroes: set[str] | None = None,
) -> list[HeroFactProfile]:
    return [
        load_hero_facts(path, source_patch=patch, cohort=cohort)
        for path in discover_authored_files(data_dir, heroes)
    ]


def finalize_patch(
    data_dir: Path,
    patch: str,
    hero_ids: list[int],
    *,
    complete: bool,
) -> None:
    manifest = build_manifest(data_dir, patch, hero_ids, complete=complete)
    write_manifest(data_dir, manifest)
    graph = build_graph(data_dir, patch, hero_ids)
    cache_graph(data_dir, patch, graph)


def run_bootstrap(
    data_dir: Path,
    patch: str,
    generator_version: str,
    *,
    heroes: set[str] | None = None,
    cohort: str = "pub",
) -> list[HeroResult]:
    profiles = load_profiles(data_dir, patch, cohort=cohort, heroes=heroes)
    if not profiles:
        raise FileNotFoundError(f"no authored hero YAML files found under {authored_dir(data_dir)}")

    generated_at = _now_iso()
    roster_ids = {profile.hero_id for profile in profiles}
    written_ids: list[int] = []
    results: list[HeroResult] = []

    for profile in profiles:
        hero = _to_derived(profile, generator_version=generator_version, generated_at=generated_at)
        validate_hero(hero, ValidationContext(roster_hero_ids=roster_ids))
        write_hero(data_dir, patch, hero)
        written_ids.append(hero.hero_id)
        results.append(HeroResult(hero_id=hero.hero_id, hero_slug=hero.hero_slug, success=True))

    relations = infer_relations(profiles)
    write_relations(
        relations_file(data_dir, patch),
        relations,
        source_patch=patch,
        generated_at=generated_at,
    )

    reader = RelationsReader(relations)
    for hero_id in written_ids:
        hero = HeroDerived.model_validate_json(hero_file(data_dir, patch, hero_id).read_text())
        write_summary(data_dir, hero, reader)

    finalize_patch(data_dir, patch, written_ids, complete=heroes is None)
    return results
