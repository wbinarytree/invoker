from invoker.pipeline.summarize import summarize
from invoker.schemas.derived import (
    HeroDerived,
    MetaBlock,
    PositionBlock,
    Provenance,
    StatEdge,
    TagSource,
)


def _hero() -> HeroDerived:
    return HeroDerived(
        schema_version=1,
        generator_version="invoker@0.1.0",
        source_patch="7.41b",
        generated_at="2026-04-14T00:00:00Z",
        hero_id=28,
        localized_name="Slardar",
        internal_name="npc_dota_hero_slardar",
        liquipedia_roles=["Initiator"],
        functional_tags=["armor_reduction", "single_target_disable"],
        tag_sources=[
            TagSource(tag="armor_reduction", ability="Corrosive Haze", evidence="-20 armor"),
            TagSource(
                tag="single_target_disable", ability="Slithereen Crush", evidence="1.5s stun"
            ),
        ],
        positions={"pro": PositionBlock(weights={"3": 1.0}, games=34, window_days=90)},
        synergies={
            "pro": [
                StatEdge(
                    hero_id=120,
                    score=0.08,
                    games=50,
                    confidence="high",
                    source="stratz",
                    reason="armor reduction helps physical",
                )
            ]
        },
        counters={
            "pro": [
                StatEdge(
                    hero_id=96,
                    score=-0.07,
                    games=34,
                    confidence="med",
                    source="opendota",
                    reason="armor reduction does not overcome innate armor",
                )
            ]
        },
        meta={"pro": MetaBlock(contest_rate=0.12, win_rate=0.51, tier="situational", games=34)},
        meta_history=[],
        provenance=Provenance(mechanical={"model": "fake"}, statistical={}),
    )


def test_summary_contains_all_sections():
    s = summarize(_hero(), "pro")
    assert "Slardar" in s
    assert "armor_reduction" in s
    assert "h120" in s
    assert "h96" in s
    assert "tier: situational" in s
