from __future__ import annotations

from pathlib import Path

from invoker.kg import (
    FactProvenance,
    HeroFactFeature,
    HeroFactProfile,
    RelationsReader,
    infer_relations,
    write_relations,
)
from invoker.kg.reader import RelationsFile
from invoker.kg.schemas import (
    HeroRelation,
    RelationContext,
    RelationEvidence,
    RelationEvidenceMechanical,
)


def _feature(type_: str) -> HeroFactFeature:
    return HeroFactFeature(type=type_, evidence=[])


def _profile(
    hero_id: int,
    name: str,
    *,
    capabilities: list[str] | None = None,
    requirements: list[str] | None = None,
    liabilities: list[str] | None = None,
) -> HeroFactProfile:
    return HeroFactProfile(
        hero_id=hero_id,
        hero_slug=name.lower(),
        localized_name=name,
        source_patch="7.41b",
        cohort="pro",
        capabilities=[_feature(t) for t in (capabilities or [])],
        requirements=[_feature(t) for t in (requirements or [])],
        liabilities=[_feature(t) for t in (liabilities or [])],
        targets=[],
        role_distribution={},
        provenance=FactProvenance(
            authored_by="human",
            authored_at="2026-04-22",
            assist_model=None,
        ),
    )


def _sample_relations() -> list[HeroRelation]:
    anti_mage = _profile(1, "Anti-Mage", capabilities=["mana_burn"])
    medusa = _profile(96, "Medusa", liabilities=["mana_dependence"])
    slardar = _profile(
        25,
        "Slardar",
        capabilities=["armor_reduction", "vision_reveal", "reliable_stun"],
    )
    riki = _profile(48, "Riki", capabilities=["mobility"], liabilities=["weak_to_reveal"])
    pangolier = _profile(120, "Pangolier", capabilities=["magic_burst", "mobility"])
    return infer_relations([anti_mage, medusa, slardar, riki, pangolier])


def test_relations_from_returns_only_outbound():
    rels = _sample_relations()
    reader = RelationsReader(rels)
    out = reader.relations_from(1)
    assert out
    assert all(r.from_hero_id == 1 for r in out)


def test_relations_to_returns_only_inbound():
    rels = _sample_relations()
    reader = RelationsReader(rels)
    out = reader.relations_to(96)
    assert out
    assert all(r.to_hero_id == 96 for r in out)


def test_relations_for_dedupes_by_relation_id():
    rels = _sample_relations()
    reader = RelationsReader(rels)
    out = reader.relations_for(25)
    ids = [r.relation_id for r in out]
    assert len(ids) == len(set(ids))
    assert all(r.from_hero_id == 25 or r.to_hero_id == 25 for r in out)


def test_relations_between_covers_both_directions():
    rels = _sample_relations()
    reader = RelationsReader(rels)
    ab = reader.relations_between(25, 120)
    ba = reader.relations_between(120, 25)
    assert sorted(r.relation_id for r in ab) == sorted(r.relation_id for r in ba)
    assert ab


def test_synergies_with_filters_kind():
    rels = _sample_relations()
    reader = RelationsReader(rels)
    out = reader.synergies_with(25)
    assert out
    assert all(r.relation_kind == "synergy" for r in out)


def test_counters_of_returns_inbound_counters():
    rels = _sample_relations()
    reader = RelationsReader(rels)
    out = reader.counters_of(96)
    assert out
    for r in out:
        assert r.to_hero_id == 96
        assert r.relation_kind == "counter"


def test_countered_by_returns_outbound_counters():
    rels = _sample_relations()
    reader = RelationsReader(rels)
    out = reader.countered_by(1)
    assert out
    for r in out:
        assert r.from_hero_id == 1
        assert r.relation_kind == "counter"


def test_relations_by_pattern_filters():
    rels = _sample_relations()
    reader = RelationsReader(rels)
    out = reader.relations_by_pattern("resource_punish")
    assert out
    assert all(r.pattern == "resource_punish" for r in out)


def test_write_and_load_roundtrips(tmp_path: Path):
    rels = _sample_relations()
    path = tmp_path / "relations.json"
    write_relations(
        path,
        rels,
        source_patch="7.41b",
        generated_at="2026-04-22T00:00:00Z",
    )
    reader = RelationsReader.load(path)
    assert len(reader.all()) == len(rels)
    assert {r.relation_id for r in reader.all()} == {r.relation_id for r in rels}


def test_relations_file_rejects_unknown_fields():
    rel = HeroRelation(
        relation_id="1->2:counter:resource_punish:mana_burn",
        source_patch="7.41b",
        cohort="pro",
        from_hero_id=1,
        to_hero_id=2,
        relation_kind="counter",
        pattern="resource_punish",
        source_feature="mana_burn",
        target_feature="mana_dependence",
        mechanical_rationale="x",
        context=RelationContext(),
        evidence=RelationEvidence(
            mechanical=RelationEvidenceMechanical(confidence=0.9, basis=[])
        ),
        confidence="high",
    )
    file = RelationsFile(
        schema_version=2,
        source_patch="7.41b",
        generated_at="2026-04-22T00:00:00Z",
        relations=[rel],
    )
    assert file.schema_version == 2
    assert len(file.relations) == 1
