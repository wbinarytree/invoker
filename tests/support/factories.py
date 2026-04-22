from invoker.kg.schemas import (
    FactProvenance,
    HeroFactFeature,
    HeroRelation,
    RelationContext,
    RelationEvidence,
    RelationEvidenceMechanical,
)
from invoker.schemas.derived import HeroDerived


def _feature(type_: str, score: float | None = None) -> HeroFactFeature:
    return HeroFactFeature(type=type_, score=score, evidence=[])


def make_hero() -> HeroDerived:
    return HeroDerived(
        generator_version="invoker@0.1.0",
        source_patch="7.41b",
        generated_at="2026-04-22T00:00:00Z",
        hero_id=28,
        hero_slug="slardar",
        localized_name="Slardar",
        capabilities=[_feature("armor_reduction", 0.9), _feature("reliable_stun", 0.8)],
        requirements=[],
        liabilities=[],
        targets=[],
        role_distribution={"offlane": 0.9, "roamer": 0.1},
        provenance=FactProvenance(
            authored_by="human",
            authored_at="2026-04-22",
            assist_model=None,
        ),
    )


def make_relation() -> HeroRelation:
    return HeroRelation(
        relation_id="28->120:synergy:enabler_payoff:armor_reduction",
        source_patch="7.41b",
        cohort="pub",
        from_hero_id=28,
        to_hero_id=120,
        relation_kind="synergy",
        pattern="enabler_payoff",
        source_feature="armor_reduction",
        target_feature="magic_burst",
        mechanical_rationale=(
            "damage amplification or setup creates a payoff window "
            "for burst follow-up"
        ),
        context=RelationContext(),
        evidence=RelationEvidence(
            mechanical=RelationEvidenceMechanical(confidence=0.65, basis=["x", "y"])
        ),
        confidence="med",
    )
