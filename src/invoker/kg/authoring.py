from __future__ import annotations

import asyncio
import json
import re
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from invoker.kg import HeroFactProfile, infer_relations, load_hero_facts
from invoker.kg.vocabulary import (
    CAPABILITIES,
    LIABILITIES,
    REQUIREMENTS,
    TARGETS,
    load_vocabulary,
)
from invoker.llm.client import strip_fences
from invoker.llm.manual import ManualClient, PendingManualResponseError
from invoker.paths import authored_dir, vocab_gaps_file
from invoker.prompts import load
from invoker.sources.opendota import OpenDotaFetcher

AUTHORING_PATCH = "authoring"
AUTHORED_FACT_KEYS = frozenset(
    {
        "hero_id",
        "hero_slug",
        "localized_name",
        "capabilities",
        "requirements",
        "liabilities",
        "targets",
        "role_distribution",
        "provenance",
    }
)
GAP_BUCKETS = frozenset({"capabilities", "requirements", "liabilities", "targets"})


class AuthoredFactsValidationError(ValueError):
    pass


@dataclass(frozen=True)
class HeroPromptContext:
    hero_id: int
    hero_slug: str
    localized_name: str
    internal_name: str
    roles: list[str]
    abilities: list[dict[str, str]]


@dataclass(frozen=True)
class DraftFactsResult:
    hero_slug: str
    prompt_path: Path
    response_path: Path
    authored_path: Path | None = None
    gaps_path: Path | None = None
    gap_count: int = 0
    pending: bool = False


@dataclass(frozen=True)
class PromoteDraftResult:
    hero_slug: str
    authored_path: Path
    draft_path: Path
    backup_path: Path | None = None
    draft_deleted: bool = False


def _normalize_slug(name: str) -> str:
    return name.lower().replace(" ", "_").replace("-", "_")


def _candidate_payloads(text: str) -> list[str]:
    stripped = text.strip()
    candidates: list[str] = [stripped, strip_fences(stripped)]
    fenced_blocks = re.findall(
        r"```(?:yaml|yml|json)?\s*(.*?)```",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    for block in fenced_blocks:
        candidates.append(block.strip())

    seen: set[str] = set()
    ordered: list[str] = []
    for candidate in candidates:
        normalized = candidate.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        ordered.append(normalized)
    return ordered


def _coerce_response_payload(text: str) -> dict[str, Any]:
    for candidate in _candidate_payloads(text):
        try:
            payload = yaml.safe_load(candidate) or {}
        except yaml.YAMLError:
            continue
        if isinstance(payload, dict):
            return payload
    raise AuthoredFactsValidationError("manual response must parse to a YAML or JSON mapping")


def _select_bucket_vocab(bucket: str) -> frozenset[str]:
    if bucket == "capabilities":
        return CAPABILITIES
    if bucket == "requirements":
        return REQUIREMENTS
    if bucket == "liabilities":
        return LIABILITIES
    if bucket == "targets":
        return TARGETS
    raise AssertionError(f"unknown bucket {bucket}")


def resolve_authored_file(data_dir: Path, hero: str) -> Path:
    root = authored_dir(data_dir)
    token = hero.strip().lower()
    path = root / f"{token}.yaml"
    if path.exists():
        return path

    for candidate in sorted(root.glob("*.yaml")):
        if _is_draft_path(candidate):
            continue
        profile = load_hero_facts(candidate, source_patch=AUTHORING_PATCH)
        if token in {
            candidate.stem.lower(),
            str(profile.hero_id),
            profile.localized_name.lower(),
            (profile.hero_slug or "").lower(),
        }:
            return candidate
    raise FileNotFoundError(f"no authored hero file found for {hero!r} under {root}")


def validate_authored_payload(raw: dict[str, Any]) -> None:
    extra = sorted(set(raw) - AUTHORED_FACT_KEYS)
    if extra:
        raise AuthoredFactsValidationError(f"unknown top-level keys: {extra}")

    required_top_level = {
        "hero_id",
        "hero_slug",
        "localized_name",
        "capabilities",
        "requirements",
        "liabilities",
        "targets",
        "provenance",
    }
    missing = sorted(key for key in required_top_level if key not in raw)
    if missing:
        raise AuthoredFactsValidationError(f"missing required keys: {missing}")

    if not isinstance(raw["provenance"], dict):
        raise AuthoredFactsValidationError("provenance must be a mapping")

    for key in ("authored_by", "authored_at"):
        if not raw["provenance"].get(key):
            raise AuthoredFactsValidationError(f"provenance.{key} is required")

    for bucket in ("capabilities", "requirements", "liabilities", "targets"):
        items = raw.get(bucket)
        if not isinstance(items, list):
            raise AuthoredFactsValidationError(f"{bucket} must be a list")
        allowed = _select_bucket_vocab(bucket)
        seen: set[str] = set()
        for item in items:
            if not isinstance(item, dict):
                raise AuthoredFactsValidationError(f"{bucket} entries must be mappings")
            feature_type = item.get("type")
            if not isinstance(feature_type, str) or not feature_type:
                raise AuthoredFactsValidationError(f"{bucket} entries must include non-empty type")
            if feature_type not in allowed:
                raise AuthoredFactsValidationError(
                    f"{bucket}.{feature_type} is not in the live vocabulary"
                )
            if feature_type in seen:
                raise AuthoredFactsValidationError(f"{bucket} contains duplicate {feature_type}")
            seen.add(feature_type)
            score = item.get("score")
            if score is not None and not isinstance(score, (int, float)):
                raise AuthoredFactsValidationError(f"{bucket}.{feature_type} score must be numeric")
            if score is not None and not 0.0 <= float(score) <= 1.0:
                raise AuthoredFactsValidationError(
                    f"{bucket}.{feature_type} score must be between 0.0 and 1.0"
                )
            evidence = item.get("evidence", [])
            if evidence is None:
                evidence = []
            if not isinstance(evidence, list):
                raise AuthoredFactsValidationError(
                    f"{bucket}.{feature_type} evidence must be a list when present"
                )
            if bucket in {"capabilities", "liabilities", "targets"} and not evidence:
                raise AuthoredFactsValidationError(
                    f"{bucket}.{feature_type} requires at least one evidence item"
                )

    role_distribution = raw.get("role_distribution", {})
    if role_distribution is None:
        role_distribution = {}
    if not isinstance(role_distribution, dict):
        raise AuthoredFactsValidationError("role_distribution must be a mapping")
    total = 0.0
    for role, weight in role_distribution.items():
        if not isinstance(weight, (int, float)) or not 0.0 <= float(weight) <= 1.0:
            raise AuthoredFactsValidationError(
                f"role_distribution[{role}] must be between 0.0 and 1.0"
            )
        total += float(weight)
    if total > 1.001:
        raise AuthoredFactsValidationError("role_distribution must sum to at most 1.0")


def _coerce_gap_text(gap: dict[str, Any], key: str) -> str:
    value = gap.get(key)
    if value is None:
        return ""
    if not isinstance(value, str):
        raise AuthoredFactsValidationError(f"vocabulary_gaps.{key} must be a string")
    return value.strip()


def _coerce_vocabulary_gaps(
    raw: Any,
    *,
    context: HeroPromptContext,
) -> list[dict[str, Any]]:
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise AuthoredFactsValidationError("vocabulary_gaps must be a list when present")

    gaps: list[dict[str, Any]] = []
    for item in raw:
        if not isinstance(item, dict):
            raise AuthoredFactsValidationError("vocabulary_gaps entries must be mappings")
        bucket = _coerce_gap_text(item, "bucket")
        if bucket not in GAP_BUCKETS:
            raise AuthoredFactsValidationError(
                f"vocabulary_gaps.bucket must be one of {sorted(GAP_BUCKETS)}"
            )
        concept = _coerce_gap_text(item, "concept")
        why_needed = _coerce_gap_text(item, "why_needed")
        if not concept or not why_needed:
            raise AuthoredFactsValidationError(
                "vocabulary_gaps entries require concept and why_needed"
            )
        gaps.append(
            {
                "hero_id": context.hero_id,
                "hero_slug": context.hero_slug,
                "localized_name": context.localized_name,
                "bucket": bucket,
                "concept": concept,
                "why_needed": why_needed,
                "evidence": _coerce_gap_text(item, "evidence")
                or _coerce_gap_text(item, "example_evidence"),
                "candidate_term": _coerce_gap_text(item, "candidate_term"),
                "status": "proposed",
            }
        )
    return gaps


def record_vocabulary_gaps(data_dir: Path, gaps: list[dict[str, Any]]) -> Path | None:
    if not gaps:
        return None

    path = vocab_gaps_file(data_dir)
    raw = yaml.safe_load(path.read_text()) or {} if path.exists() else {}
    if isinstance(raw, list):
        existing = raw
    elif isinstance(raw, dict):
        existing = raw.get("gaps", [])
    else:
        existing = []
    if not isinstance(existing, list):
        existing = []

    by_key: dict[tuple[str, str, str], dict[str, Any]] = {}
    for item in existing:
        if not isinstance(item, dict):
            continue
        key = (
            str(item.get("hero_slug", "")),
            str(item.get("bucket", "")),
            str(item.get("concept", "")),
        )
        by_key[key] = item
    for gap in gaps:
        key = (gap["hero_slug"], gap["bucket"], gap["concept"])
        by_key[key] = gap

    payload = {
        "gaps": sorted(
            by_key.values(),
            key=lambda g: (
                str(g.get("hero_slug", "")),
                str(g.get("bucket", "")),
                str(g.get("concept", "")),
            ),
        )
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=False))
    return path


def validate_authored_file(path: Path) -> HeroFactProfile:
    raw = yaml.safe_load(path.read_text()) or {}
    if not isinstance(raw, dict):
        raise AuthoredFactsValidationError("authored file must parse to a YAML mapping")
    validate_authored_payload(raw)
    return load_hero_facts(path, source_patch=AUTHORING_PATCH)


def _backup_path_for(path: Path) -> Path:
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    backup_dir = path.parent / ".backups"
    return backup_dir / f"{path.stem}.{stamp}{path.suffix}"


def _draft_path_for(authored_path: Path) -> Path:
    return authored_path.with_name(f"{authored_path.stem}.draft{authored_path.suffix}")


def _is_draft_path(path: Path) -> bool:
    return path.name.endswith(".draft.yaml")


def promote_authored_draft(
    data_dir: Path,
    hero: str,
    *,
    delete_draft: bool = False,
) -> PromoteDraftResult:
    authored_path = resolve_authored_file(data_dir, hero)
    draft_path = _draft_path_for(authored_path)
    if not draft_path.exists():
        raise FileNotFoundError(f"no draft file found at {draft_path}")

    draft_profile = validate_authored_file(draft_path)
    backup_path: Path | None = None
    if authored_path.exists():
        backup_path = _backup_path_for(authored_path)
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(authored_path, backup_path)

    shutil.copy2(draft_path, authored_path)
    if delete_draft:
        draft_path.unlink()

    return PromoteDraftResult(
        hero_slug=draft_profile.hero_slug or authored_path.stem,
        authored_path=authored_path,
        draft_path=draft_path,
        backup_path=backup_path,
        draft_deleted=delete_draft,
    )


def authored_profiles(data_dir: Path, *, include_drafts: bool = False) -> list[HeroFactProfile]:
    profiles: list[HeroFactProfile] = []
    for path in sorted(authored_dir(data_dir).glob("*.yaml")):
        if not include_drafts and _is_draft_path(path):
            continue
        try:
            profiles.append(validate_authored_file(path))
        except Exception:
            continue
    return profiles


def _hero_label(hero_id: int, names_by_id: dict[int, str]) -> str:
    name = names_by_id.get(hero_id)
    if name:
        return f"{name} ({hero_id})"
    return str(hero_id)


def format_relations_for_hero(data_dir: Path, hero: str) -> str:
    target_path = resolve_authored_file(data_dir, hero)
    target = validate_authored_file(target_path)
    profiles = authored_profiles(data_dir)
    names_by_id = {profile.hero_id: profile.localized_name for profile in profiles}
    relations = infer_relations(profiles)

    outbound = [rel for rel in relations if rel.from_hero_id == target.hero_id]
    inbound = [rel for rel in relations if rel.to_hero_id == target.hero_id]

    lines = [f"# Relations for {target.localized_name}", ""]
    if not outbound and not inbound:
        lines.append("No relations inferred from the current authored corpus.")
        return "\n".join(lines) + "\n"

    if outbound:
        lines.append("## Outbound")
        for rel in outbound:
            lines.append(
                f"- {rel.relation_kind} -> {_hero_label(rel.to_hero_id, names_by_id)} "
                f"[{rel.pattern}] {rel.source_feature} -> {rel.target_feature}: "
                f"{rel.mechanical_rationale}"
            )
        lines.append("")
    if inbound:
        lines.append("## Inbound")
        for rel in inbound:
            lines.append(
                f"- {_hero_label(rel.from_hero_id, names_by_id)} -> {rel.relation_kind} "
                f"[{rel.pattern}] {rel.source_feature} -> {rel.target_feature}: "
                f"{rel.mechanical_rationale}"
            )
        lines.append("")
    return "\n".join(lines)


def _hero_matches(token: str, hero: dict[str, Any]) -> bool:
    localized = str(hero.get("localized_name", ""))
    internal = str(hero.get("name", ""))
    hero_id = str(hero.get("id", ""))
    slug = internal.removeprefix("npc_dota_hero_")
    return token in {
        localized.lower(),
        internal.lower(),
        slug.lower(),
        hero_id.lower(),
    }


def _prompt_vocabulary_context() -> str:
    vocabulary = load_vocabulary()
    packet: dict[str, list[dict[str, Any]]] = {}

    for bucket in ("capabilities", "requirements", "liabilities", "targets"):
        entries = vocabulary[bucket]
        packet[bucket] = []
        for term, metadata in entries.items():
            if not isinstance(metadata, dict) or metadata.get("status") != "accepted":
                continue
            entry = {
                key: value
                for key, value in metadata.items()
                if key not in {"status", "introduced_in"}
            }
            entry["term"] = term
            packet[bucket].append(entry)
        packet[bucket].sort(key=lambda entry: entry["term"])

    return json.dumps(packet, indent=2, sort_keys=True)


def _select_hero(
    heroes: list[dict[str, Any]],
    hero_abilities: dict[str, Any],
    abilities: dict[str, Any],
    hero: str,
) -> HeroPromptContext:
    token = hero.strip().lower()
    selected = next((item for item in heroes if _hero_matches(token, item)), None)
    if selected is None:
        raise FileNotFoundError(f"hero {hero!r} not found in OpenDota roster")

    internal_name = selected["name"]
    hero_slug = internal_name.removeprefix("npc_dota_hero_")
    mapping = hero_abilities.get(internal_name, {})
    ability_names = mapping.get("abilities", [])
    resolved_abilities: list[dict[str, str]] = []
    for ability_name in ability_names:
        payload = abilities.get(ability_name)
        if not payload:
            continue
        name = payload.get("dname") or ""
        desc = payload.get("desc") or ""
        if not name or not desc:
            continue
        resolved_abilities.append({"name": name, "text": desc})

    return HeroPromptContext(
        hero_id=selected["id"],
        hero_slug=hero_slug,
        localized_name=selected["localized_name"],
        internal_name=internal_name,
        roles=selected.get("roles", []),
        abilities=resolved_abilities,
    )


async def fetch_prompt_context(
    data_dir: Path,
    hero: str,
    *,
    patch: str = AUTHORING_PATCH,
) -> HeroPromptContext:
    fetcher = OpenDotaFetcher(data_dir / "raw", patch)
    try:
        heroes = await fetcher.heroes()
        hero_abilities = await fetcher.hero_abilities_map()
        abilities = await fetcher.abilities()
        return _select_hero(heroes, hero_abilities, abilities, hero)
    finally:
        await fetcher.close()


def render_draft_facts_prompt(context: HeroPromptContext) -> tuple[str, int]:
    prompt = load("draft_fact_profile")
    ability_context = json.dumps(
        [
            {"name": ability["name"], "description": ability["text"]}
            for ability in context.abilities
        ],
        indent=2,
        sort_keys=True,
    )
    rendered = prompt.render(
        HERO_ID=str(context.hero_id),
        HERO_NAME=context.localized_name,
        HERO_SLUG=context.hero_slug,
        ROLES=", ".join(context.roles) or "Unknown",
        ABILITIES_JSON=ability_context,
        VOCABULARY_CONTEXT_JSON=_prompt_vocabulary_context(),
    )
    return rendered, prompt.version


def draft_facts(
    data_dir: Path,
    hero: str,
    *,
    patch: str = AUTHORING_PATCH,
) -> DraftFactsResult:
    context = asyncio.run(fetch_prompt_context(data_dir, hero, patch=patch))
    prompt_text, prompt_version = render_draft_facts_prompt(context)
    client = ManualClient(
        inbox=data_dir / "raw" / "manual_prompts",
        outbox=data_dir / "raw" / "manual_responses",
    )
    cache_tag = f"draft-facts/{context.hero_slug}"
    try:
        response = client.generate_json(
            prompt_text,
            prompt_version=prompt_version,
            cache_tag=cache_tag,
        )
    except PendingManualResponseError as exc:
        return DraftFactsResult(
            hero_slug=context.hero_slug,
            prompt_path=exc.prompt_path,
            response_path=exc.response_path,
            pending=True,
        )

    raw = _coerce_response_payload(response.text)
    raw.setdefault("hero_id", context.hero_id)
    raw.setdefault("hero_slug", context.hero_slug)
    raw.setdefault("localized_name", context.localized_name)
    raw.setdefault("capabilities", [])
    raw.setdefault("requirements", [])
    raw.setdefault("liabilities", [])
    raw.setdefault("targets", [])
    raw.setdefault("role_distribution", {})
    gaps = _coerce_vocabulary_gaps(raw.pop("vocabulary_gaps", []), context=context)
    validate_authored_payload(raw)
    gaps_path = record_vocabulary_gaps(data_dir, gaps)

    destination = authored_dir(data_dir) / f"{context.hero_slug}.yaml"
    if destination.exists():
        destination = _draft_path_for(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(yaml.safe_dump(raw, sort_keys=False, allow_unicode=False))
    return DraftFactsResult(
        hero_slug=context.hero_slug,
        prompt_path=client._paths(prompt_text, cache_tag)[0],
        response_path=client._paths(prompt_text, cache_tag)[1],
        authored_path=destination,
        gaps_path=gaps_path,
        gap_count=len(gaps),
        pending=False,
    )
