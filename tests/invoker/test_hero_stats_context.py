import pytest

from invoker.kg.hero_stats_context import (
    HeroStatsContext,
    StatEntry,
    _assign_band,
    compute_hero_stats_context,
)


def _roster(overrides: dict | None = None) -> dict:
    """Five-hero synthetic roster for band/percentile tests."""
    base = {
        f"npc_dota_hero_{i}": {
            "base_str": float(i * 10),
            "base_agi": float(i * 5),
            "base_int": float(i * 8),
            "str_gain": float(i),
            "agi_gain": float(i * 0.5),
            "int_gain": float(i * 0.8),
            "base_armor": float(i),
            "base_attack_min": float(20 + i),
            "base_attack_max": float(25 + i),
            "base_attack_speed": float(95 + i),
            "base_attack_time": float(1.4 + i / 10),
            "attack_animation_point": float(i / 10),
            "attack_acquisition_range": float(500 + i * 50),
            "attack_range": float(i * 100),
            "move_speed": float(300 + i * 10),
            "primary_attr": "str",
            "attack_type": "Melee",
        }
        for i in range(1, 6)
    }
    if overrides:
        base.update(overrides)
    return base


@pytest.mark.parametrize(
    "percentile,expected_band",
    [
        (0.0, "very_low"),
        (0.19, "very_low"),
        (0.2, "low"),
        (0.39, "low"),
        (0.4, "average"),
        (0.59, "average"),
        (0.6, "high"),
        (0.79, "high"),
        (0.8, "very_high"),
        (1.0, "very_high"),
    ],
)
def test_assign_band(percentile, expected_band):
    assert _assign_band(percentile) == expected_band


def test_compute_hero_stats_context_returns_correct_type():
    roster = _roster()
    result = compute_hero_stats_context("npc_dota_hero_3", roster)
    assert isinstance(result, HeroStatsContext)
    assert isinstance(result.base_str, StatEntry)
    assert result.base_str.value == 30.0
    assert result.base_attack_min is not None
    assert result.base_attack_min.value == 23.0
    assert result.base_attack_max is not None
    assert result.base_attack_max.value == 28.0
    assert result.base_attack_speed is not None
    assert result.base_attack_speed.value == 98.0
    assert result.base_attack_time is not None
    assert result.base_attack_time.value == 1.7
    assert result.attack_animation_point is not None
    assert result.attack_animation_point.value == 0.3
    assert result.attack_acquisition_range is not None
    assert result.attack_acquisition_range.value == 650.0
    assert result.primary_attr == "str"
    assert result.attack_type == "Melee"


def test_compute_hero_stats_context_percentile_ordering():
    roster = _roster()
    low = compute_hero_stats_context("npc_dota_hero_1", roster)
    high = compute_hero_stats_context("npc_dota_hero_5", roster)
    assert low.base_str is not None and high.base_str is not None
    assert low.base_str.percentile < high.base_str.percentile


def test_compute_hero_stats_context_band_very_high():
    roster = _roster()
    result = compute_hero_stats_context("npc_dota_hero_5", roster)
    assert result.base_str is not None
    assert result.base_str.band == "very_high"


def test_compute_hero_stats_context_band_very_low():
    roster = _roster()
    result = compute_hero_stats_context("npc_dota_hero_1", roster)
    assert result.base_str is not None
    assert result.base_str.band == "very_low"


def test_compute_hero_stats_context_missing_stat_returns_none():
    roster = {
        "npc_dota_hero_a": {"base_str": 20.0, "primary_attr": "str", "attack_type": "Melee"},
        "npc_dota_hero_b": {"base_str": 25.0, "primary_attr": "agi", "attack_type": "Ranged"},
    }
    result = compute_hero_stats_context("npc_dota_hero_a", roster)
    assert result.base_str is not None
    assert result.base_agi is None
    assert result.move_speed is None


def test_compute_hero_stats_context_unknown_hero_returns_empty():
    roster = _roster()
    result = compute_hero_stats_context("npc_dota_hero_unknown", roster)
    assert result.base_str is None
    assert result.primary_attr == ""
