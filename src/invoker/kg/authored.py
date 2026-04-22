from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from invoker.kg.schemas import FactProvenance, FeatureEvidence, HeroFactFeature, HeroFactProfile


def _coerce_feature(raw: dict[str, Any]) -> HeroFactFeature:
    evidence: list[FeatureEvidence] = []
    for item in raw.get("evidence", []) or []:
        if isinstance(item, str):
            evidence.append(FeatureEvidence(text=item))
        else:
            evidence.append(FeatureEvidence.model_validate(item))
    return HeroFactFeature(
        type=raw["type"],
        score=raw.get("score"),
        evidence=evidence,
    )


def _coerce_features(items: list[dict[str, Any]] | None) -> list[HeroFactFeature]:
    return [_coerce_feature(r) for r in (items or [])]


def _coerce_provenance(raw: dict[str, Any]) -> FactProvenance:
    payload = dict(raw)
    for key in ("authored_at", "reviewed_at"):
        if payload.get(key) is not None:
            payload[key] = str(payload[key])
    return FactProvenance.model_validate(payload)


def load_hero_facts(
    path: Path,
    *,
    source_patch: str,
    cohort: str = "pub",
) -> HeroFactProfile:
    """Load a hand-authored hero YAML into a validated HeroFactProfile.

    Authored YAML is patch-invariant; source_patch and cohort are stamped in at
    load time so the derived HeroFactProfile carries the context it was read
    under.
    """
    raw = yaml.safe_load(path.read_text()) or {}
    return HeroFactProfile(
        hero_id=raw["hero_id"],
        hero_slug=raw.get("hero_slug"),
        localized_name=raw["localized_name"],
        source_patch=source_patch,
        cohort=cohort,
        capabilities=_coerce_features(raw.get("capabilities")),
        requirements=_coerce_features(raw.get("requirements")),
        liabilities=_coerce_features(raw.get("liabilities")),
        targets=_coerce_features(raw.get("targets")),
        role_distribution=raw.get("role_distribution") or {},
        provenance=_coerce_provenance(raw["provenance"]),
    )
