from __future__ import annotations

from collections.abc import Iterable

from invoker.kg.schemas import (
    HeroFactProfile,
    HeroRelation,
    RelationContext,
    RelationEvidence,
    RelationEvidenceMechanical,
)


def _feature_types(features: Iterable) -> set[str]:
    return {f.type for f in features}


def _make_relation(
    source: HeroFactProfile,
    target: HeroFactProfile,
    *,
    relation_kind: str,
    pattern: str,
    source_feature: str,
    target_feature: str,
    rationale: str,
    confidence: str,
    mechanical_confidence: float,
) -> HeroRelation:
    return HeroRelation(
        relation_id=(
            f"{source.hero_id}->{target.hero_id}:{relation_kind}:{pattern}:{source_feature}"
        ),
        source_patch=source.source_patch,
        cohort=source.cohort,
        from_hero_id=source.hero_id,
        to_hero_id=target.hero_id,
        relation_kind=relation_kind,
        pattern=pattern,
        source_feature=source_feature,
        target_feature=target_feature,
        mechanical_rationale=rationale,
        context=RelationContext(),
        evidence=RelationEvidence(
            mechanical=RelationEvidenceMechanical(
                confidence=mechanical_confidence,
                basis=[
                    f"{source.localized_name}.capabilities includes {source_feature}",
                    (
                        f"{target.localized_name}.capabilities includes {target_feature}"
                        if relation_kind == "synergy"
                        else f"{target.localized_name}.liabilities includes {target_feature}"
                    ),
                ],
            ),
        ),
        confidence=confidence,
    )


def infer_relation(source: HeroFactProfile, target: HeroFactProfile) -> list[HeroRelation]:
    relations: list[HeroRelation] = []
    src_caps = _feature_types(source.capabilities)
    tgt_caps = _feature_types(target.capabilities)
    tgt_reqs = _feature_types(target.requirements)
    tgt_liabs = _feature_types(target.liabilities)

    if "mana_burn" in src_caps and "mana_dependence" in tgt_liabs:
        relations.append(
            _make_relation(
                source,
                target,
                relation_kind="counter",
                pattern="resource_punish",
                source_feature="mana_burn",
                target_feature="mana_dependence",
                rationale="mana burn punishes a hero whose durability or output depends on mana",
                confidence="high",
                mechanical_confidence=0.95,
            )
        )

    if "vision_reveal" in src_caps and "weak_to_reveal" in tgt_liabs:
        relations.append(
            _make_relation(
                source,
                target,
                relation_kind="counter",
                pattern="vision_exposure",
                source_feature="vision_reveal",
                target_feature="weak_to_reveal",
                rationale="persistent reveal punishes invisibility-reliant targets",
                confidence="high",
                mechanical_confidence=0.95,
            )
        )

    if "armor_reduction" in src_caps and "magic_burst" in tgt_caps:
        relations.append(
            _make_relation(
                source,
                target,
                relation_kind="synergy",
                pattern="enabler_payoff",
                source_feature="armor_reduction",
                target_feature="magic_burst",
                rationale="damage amplification or setup creates a payoff window for burst follow-up",
                confidence="med",
                mechanical_confidence=0.65,
            )
        )

    if "save" in src_caps and "needs_save" in tgt_reqs:
        relations.append(
            _make_relation(
                source,
                target,
                relation_kind="synergy",
                pattern="save_protection",
                source_feature="save",
                target_feature="needs_save",
                rationale="defensive protection covers a core ally requirement",
                confidence="med",
                mechanical_confidence=0.8,
            )
        )

    if "reliable_stun" in src_caps and "mobility" in tgt_caps:
        relations.append(
            _make_relation(
                source,
                target,
                relation_kind="counter",
                pattern="mobility_punish",
                source_feature="reliable_stun",
                target_feature="mobility",
                rationale="reliable lockdown punishes heroes whose value depends on movement freedom",
                confidence="med",
                mechanical_confidence=0.7,
            )
        )

    return relations


def infer_relations(profiles: Iterable[HeroFactProfile]) -> list[HeroRelation]:
    profiles = list(profiles)
    out: list[HeroRelation] = []
    for source in profiles:
        for target in profiles:
            if source.hero_id == target.hero_id:
                continue
            out.extend(infer_relation(source, target))
    return out
