from __future__ import annotations

from invoker.kg import HeroFactFeature, HeroFactProfile, infer_relation
from invoker.kg.vocabulary import (
    CAPABILITIES,
    LIABILITIES,
    RELATION_PATTERNS,
    REQUIREMENTS,
    STATISTICAL_ALIGNMENT,
)


def _feature(type_: str) -> HeroFactFeature:
    return HeroFactFeature(type=type_, evidence=[])


def _profile(
    hero_id: int,
    name: str,
    *,
    capabilities: list[str],
    requirements: list[str] | None = None,
    liabilities: list[str] | None = None,
    targets: list[str] | None = None,
    role_distribution: dict[str, float] | None = None,
) -> HeroFactProfile:
    return HeroFactProfile(
        hero_id=hero_id,
        localized_name=name,
        source_patch="7.41b",
        cohort="pro",
        capabilities=[_feature(t) for t in capabilities],
        requirements=[_feature(t) for t in (requirements or [])],
        liabilities=[_feature(t) for t in (liabilities or [])],
        targets=[_feature(t) for t in (targets or [])],
        role_distribution=role_distribution or {},
        provenance={"prototype": True},
    )


def test_benchmark_vocab_is_small_and_explicit():
    assert "mana_burn" in CAPABILITIES
    assert "mana_dependence" in LIABILITIES
    assert "needs_save" in REQUIREMENTS
    assert "resource_punish" in RELATION_PATTERNS
    assert "aligned" in STATISTICAL_ALIGNMENT
    assert "unobserved" in STATISTICAL_ALIGNMENT


def test_antimage_counters_medusa_via_resource_punish():
    anti_mage = _profile(1, "Anti-Mage", capabilities=["mana_burn", "mobility"])
    medusa = _profile(96, "Medusa", capabilities=[], liabilities=["mana_dependence"])

    relations = infer_relation(anti_mage, medusa)

    assert len(relations) == 1
    rel = relations[0]
    assert rel.relation_kind == "counter"
    assert rel.pattern == "resource_punish"
    assert rel.source_feature == "mana_burn"
    assert rel.target_feature == "mana_dependence"
    assert rel.evidence.statistical == []


def test_slardar_counters_riki_via_vision_exposure():
    slardar = _profile(
        25,
        "Slardar",
        capabilities=["armor_reduction", "vision_reveal", "initiation", "reliable_stun"],
    )
    riki = _profile(48, "Riki", capabilities=["mobility", "silence"], liabilities=["weak_to_reveal"])

    relations = infer_relation(slardar, riki)

    assert any(r.pattern == "vision_exposure" for r in relations)
    rel = next(r for r in relations if r.pattern == "vision_exposure")
    assert rel.relation_kind == "counter"
    assert rel.source_feature == "vision_reveal"
    assert rel.target_feature == "weak_to_reveal"


def test_slardar_synergizes_with_pangolier_via_enabler_payoff():
    slardar = _profile(
        25,
        "Slardar",
        capabilities=["armor_reduction", "vision_reveal", "initiation", "reliable_stun"],
    )
    pangolier = _profile(115, "Pangolier", capabilities=["mobility", "magic_burst", "initiation"])

    relations = infer_relation(slardar, pangolier)

    assert any(r.pattern == "enabler_payoff" for r in relations)
    rel = next(r for r in relations if r.pattern == "enabler_payoff")
    assert rel.relation_kind == "synergy"
    assert rel.source_feature == "armor_reduction"
    assert rel.target_feature == "magic_burst"


def test_oracle_can_cover_needs_save_when_present():
    oracle = _profile(109, "Oracle", capabilities=["save"])
    ally = _profile(999, "Test Core", capabilities=[], requirements=["needs_save"])

    relations = infer_relation(oracle, ally)

    assert len(relations) == 1
    rel = relations[0]
    assert rel.pattern == "save_protection"
    assert rel.relation_kind == "synergy"


def test_underlord_to_pangolier_negative_control_is_empty():
    underlord = _profile(112, "Underlord", capabilities=["wave_clear"])
    pangolier = _profile(115, "Pangolier", capabilities=["mobility", "initiation"])

    relations = infer_relation(underlord, pangolier)

    assert relations == []


def test_oracle_to_nyx_negative_control_is_empty():
    oracle = _profile(109, "Oracle", capabilities=["save"])
    nyx = _profile(88, "Nyx Assassin", capabilities=["reliable_stun", "mobility"])

    relations = infer_relation(oracle, nyx)

    assert relations == []


def test_profile_accepts_targets_and_role_distribution():
    profile = _profile(
        120,
        "Pangolier",
        capabilities=["mobility"],
        targets=["punishes_immobile_backline"],
        role_distribution={"mid": 0.6, "offlane": 0.3, "roamer": 0.1},
    )
    assert [f.type for f in profile.targets] == ["punishes_immobile_backline"]
    assert profile.role_distribution["mid"] == 0.6
