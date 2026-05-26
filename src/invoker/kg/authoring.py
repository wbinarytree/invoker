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
from invoker.kg.ability_context import AbilityContext, AttribEntry, TalentContext
from invoker.kg.hero_context import HeroContextPacket, HeroIdentityContext, build_hero_context
from invoker.kg.hero_stats_context import HeroStatsContext, StatEntry
from invoker.kg.mechanism_primer import MechanismPrimerContext, load_active_mechanism_primer
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
    hero: HeroIdentityContext,
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
                "hero_id": hero.hero_id,
                "hero_slug": hero.hero_slug,
                "localized_name": hero.localized_name,
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
            if "examples" in entry:
                entry["examples"] = _trim_examples(entry["examples"])
            entry["term"] = term
            packet[bucket].append(entry)
        packet[bucket].sort(key=lambda entry: entry["term"])

    return json.dumps(packet, indent=2, sort_keys=True)


def _trim_examples(raw: Any) -> list[str]:
    if not isinstance(raw, list):
        return []
    slugs: list[str] = []
    for item in raw:
        if isinstance(item, dict) and isinstance(item.get("hero_slug"), str):
            slug = item["hero_slug"].strip()
            if slug and slug not in slugs:
                slugs.append(slug)
    return slugs


def _stat_entry_to_dict(entry: StatEntry | None) -> dict[str, Any] | None:
    if entry is None:
        return None
    return {"value": entry.value, "percentile": entry.percentile, "band": entry.band}


def _stats_to_json(stats: HeroStatsContext) -> str:
    payload = {
        name: _stat_entry_to_dict(getattr(stats, name))
        for name in (
            "base_str",
            "base_agi",
            "base_int",
            "str_gain",
            "agi_gain",
            "int_gain",
            "base_armor",
            "base_attack_min",
            "base_attack_max",
            "attack_range",
            "move_speed",
        )
        if _stat_entry_to_dict(getattr(stats, name)) is not None
    }
    return json.dumps(payload, indent=2, sort_keys=True)


def _attrib_to_dict(attrib: AttribEntry) -> dict[str, Any]:
    payload: dict[str, Any] = {"header": attrib.header, "value": attrib.value}
    if attrib.key is not None:
        payload["key"] = attrib.key
    return payload


def _ability_to_dict(ability: AbilityContext) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "name": ability.name,
        "source": ability.source,
        "description": ability.description,
    }
    if ability.behavior:
        payload["behavior"] = ability.behavior
    if ability.damage_type:
        payload["damage_type"] = ability.damage_type
    if ability.pierces_debuff_immunity is not None:
        payload["pierces_debuff_immunity"] = ability.pierces_debuff_immunity
    if ability.dispellable:
        payload["dispellable"] = ability.dispellable
    if ability.attribs:
        payload["attribs"] = [_attrib_to_dict(a) for a in ability.attribs]
    if ability.cast_range is not None:
        payload["cast_range"] = ability.cast_range
    if ability.timing:
        payload["timing"] = ability.timing
    if ability.mana_cost is not None:
        payload["mana_cost"] = ability.mana_cost
    if ability.cooldown is not None:
        payload["cooldown"] = ability.cooldown
    return payload


def _abilities_to_json(abilities: list[AbilityContext]) -> str:
    return json.dumps([_ability_to_dict(a) for a in abilities], indent=2, sort_keys=True)


def _talents_to_json(talents: list[TalentContext]) -> str:
    payload = sorted(
        ({"name": t.name, "level": t.level} for t in talents),
        key=lambda t: (t["level"], t["name"]),
    )
    return json.dumps(payload, indent=2, sort_keys=True)


def _mechanism_primer_to_json(primer: MechanismPrimerContext) -> str:
    return json.dumps(
        {"patch": primer.patch, "mechanics": primer.mechanics},
        indent=2,
        sort_keys=True,
    )


def render_draft_facts_prompt(packet: HeroContextPacket) -> tuple[str, int]:
    prompt = load("draft_fact_profile")
    primer = load_active_mechanism_primer()
    rendered = prompt.render(
        HERO_ID=str(packet.hero.hero_id),
        HERO_NAME=packet.hero.localized_name,
        HERO_SLUG=packet.hero.hero_slug,
        PRIMARY_ATTR=packet.hero.primary_attr or "unknown",
        ATTACK_TYPE=packet.hero.attack_type or "unknown",
        ROLES=", ".join(packet.hero.roles) or "Unknown",
        PATCH=packet.patch,
        VOCABULARY_CONTEXT_JSON=_prompt_vocabulary_context(),
        STATS_JSON=_stats_to_json(packet.stats),
        MECHANISM_PRIMER_JSON=_mechanism_primer_to_json(primer),
        ABILITIES_JSON=_abilities_to_json(packet.abilities),
        TALENTS_JSON=_talents_to_json(packet.talents),
    )
    return rendered, prompt.version


def draft_facts(
    data_dir: Path,
    game_data_dir: Path,
    hero: str,
    *,
    patch: str = AUTHORING_PATCH,
) -> DraftFactsResult:
    packet = asyncio.run(build_hero_context(game_data_dir, hero, patch=patch))
    prompt_text, prompt_version = render_draft_facts_prompt(packet)
    client = ManualClient(
        inbox=data_dir / "raw" / "manual_prompts",
        outbox=data_dir / "raw" / "manual_responses",
    )
    cache_tag = f"draft-facts/{packet.hero.hero_slug}"
    try:
        response = client.generate_json(
            prompt_text,
            prompt_version=prompt_version,
            cache_tag=cache_tag,
        )
    except PendingManualResponseError as exc:
        return DraftFactsResult(
            hero_slug=packet.hero.hero_slug,
            prompt_path=exc.prompt_path,
            response_path=exc.response_path,
            pending=True,
        )

    raw = _coerce_response_payload(response.text)
    raw.setdefault("hero_id", packet.hero.hero_id)
    raw.setdefault("hero_slug", packet.hero.hero_slug)
    raw.setdefault("localized_name", packet.hero.localized_name)
    raw.setdefault("capabilities", [])
    raw.setdefault("requirements", [])
    raw.setdefault("liabilities", [])
    raw.setdefault("targets", [])
    raw.setdefault("role_distribution", {})
    gaps = _coerce_vocabulary_gaps(raw.pop("vocabulary_gaps", []), hero=packet.hero)
    validate_authored_payload(raw)
    gaps_path = record_vocabulary_gaps(data_dir, gaps)

    destination = authored_dir(data_dir) / f"{packet.hero.hero_slug}.yaml"
    if destination.exists():
        destination = _draft_path_for(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(yaml.safe_dump(raw, sort_keys=False, allow_unicode=False))
    return DraftFactsResult(
        hero_slug=packet.hero.hero_slug,
        prompt_path=client._paths(prompt_text, cache_tag)[0],
        response_path=client._paths(prompt_text, cache_tag)[1],
        authored_path=destination,
        gaps_path=gaps_path,
        gap_count=len(gaps),
        pending=False,
    )
