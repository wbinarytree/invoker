from invoker.pipeline.derive import (
    confidence_for,
    merge_matchups,
    meta_tier,
    position_weights,
)


def test_confidence_bucketing():
    assert confidence_for(0) == "none"
    assert confidence_for(5) == "low"
    assert confidence_for(20) == "med"
    assert confidence_for(100) == "high"


def test_position_weights_floor_and_normalize():
    w = position_weights({"1": 0, "2": 40, "3": 40, "4": 1, "5": 1})
    assert w["2"] > 0.4
    assert w["3"] > 0.4
    assert w["4"] == 0.0
    assert w["5"] == 0.0
    assert abs(sum(w.values()) - 1.0) < 0.01


def test_meta_tier_thresholds():
    assert meta_tier(0.6, 0.55) == "first_phase_priority"
    assert meta_tier(0.30, 0.52) == "high_priority"
    assert meta_tier(0.15, 0.50) == "situational"
    assert meta_tier(0.05, 0.50) == "niche"


def test_merge_matchups_prefers_stratz():
    stratz = [{"heroId1": 28, "heroId2": 120, "synergy": 0.08, "matchCount": 50}]
    od = [{"hero_id": 120, "games_played": 100, "wins": 52}]
    syn, cnt = merge_matchups(stratz, od, hero_id=28)
    assert syn and syn[0].hero_id == 120
    assert syn[0].source == "stratz"
    assert syn[0].score == 0.08
    assert not cnt


def test_merge_matchups_falls_back_to_opendota():
    syn, cnt = merge_matchups(None, [{"hero_id": 120, "games_played": 100, "wins": 40}], hero_id=28)
    assert not syn
    assert cnt and cnt[0].source == "opendota"
    assert cnt[0].score == -0.1
