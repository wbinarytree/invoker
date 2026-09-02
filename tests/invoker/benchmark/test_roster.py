import json
from datetime import date

import pytest

from invoker.benchmark.roster import RosterError, build_roster, load_roster, write_roster
from invoker.patches import PatchWindow

HEROES = [
    {"id": i, "name": f"npc_dota_hero_h{i:02d}", "localized_name": f"Hero {i}"}
    for i in range(1, 21)
] + [
    # Slug sorts before every h* slug while the id sorts after: exercises pair normalization.
    {"id": 21, "name": "npc_dota_hero_aardvark", "localized_name": "Aardvark"},
]
# 2026-06-09T00:00:00Z, inside the 7.41d-style window below.
T0 = 1780963200


def _match(match_id, radiant, dire, *, start=T0, series=100, league=5, patch=60):
    picks_bans = []
    order = 0
    for team, side in ((0, radiant), (1, dire)):
        for hero_id in side:
            picks_bans.append({"is_pick": True, "hero_id": hero_id, "team": team, "order": order})
            order += 1
        picks_bans.append({"is_pick": False, "hero_id": 99, "team": team, "order": order})
        order += 1
    return {
        "match_id": match_id,
        "start_time": start,
        "leagueid": league,
        "league": {"name": "Test League"},
        "series_id": series,
        "series_type": 2,
        "radiant_team": {"name": "Radiant Org"},
        "dire_team": {"name": "Dire Org"},
        "patch": patch,
        "picks_bans": picks_bans,
    }


WINDOWS = [
    PatchWindow(patch="7.41c", start_date=date(2026, 5, 6), end_date_exclusive=date(2026, 6, 4)),
    PatchWindow(patch="7.41d", start_date=date(2026, 6, 4), end_date_exclusive=None),
]


def _build(matches, **kwargs):
    return build_roster(
        matches,
        HEROES,
        kb_patch="7.41d",
        label="test",
        hero_identity_source="game_files:7.41d",
        windows=WINDOWS,
        **kwargs,
    )


def test_roster_and_pairs_from_two_games():
    game_a = _match(1, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    game_b = _match(2, [1, 2, 3, 11, 12], [6, 13, 14, 15, 16], start=T0 + 3600)
    roster = _build([game_b, game_a])  # order-independent

    assert [m.match_id for m in roster.matches] == [1, 2]
    assert roster.matches[0].radiant_picks == ["h01", "h02", "h03", "h04", "h05"]
    assert roster.sampling_frame.teams == ["Dire Org", "Radiant Org"]
    assert roster.sampling_frame.series_id == 100

    heroes = {h.slug: h for h in roster.heroes}
    assert len(heroes) == 16
    assert heroes["h01"].picks == 2 and heroes["h01"].games == [1, 2]
    assert heroes["h11"].picks == 1 and heroes["h11"].display_name == "Hero 11"

    pairs = {(p.a, p.b): p for p in roster.pairs}
    assert pairs[("h01", "h02")].ally_games == [1, 2]
    assert pairs[("h01", "h02")].enemy_games == []
    assert pairs[("h01", "h06")].enemy_games == [1, 2]
    assert pairs[("h01", "h11")].ally_games == [2]
    assert ("h04", "h11") not in pairs  # never shared a game
    # ally: 20 per game, 3 shared (h01-h02-h03 on radiant both games) -> 37
    # enemy: 25 per game, 3 shared (h01/h02/h03 vs h06 both games) -> 47
    assert len(roster.pairs) == 84
    assert all(p.a < p.b for p in roster.pairs)


def test_pair_slugs_are_ordered_lexically_even_when_hero_ids_are_not():
    roster = _build([_match(1, [21, 1, 2, 3, 4], [6, 7, 8, 9, 10])])
    pair = next(p for p in roster.pairs if "aardvark" in (p.a, p.b))
    assert (pair.a, pair.b) == ("aardvark", "h01")
    assert (pair.a_hero_id, pair.b_hero_id) == (21, 1)
    assert pair.ally_games == [1]
    enemy = next(p for p in roster.pairs if p.a == "aardvark" and p.b == "h06")
    assert enemy.enemy_games == [1]


def test_fingerprint_is_stable_across_rebuilds_and_ignores_provenance():
    game = _match(1, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    first = _build([game])
    second = _build([game])
    assert first.fingerprint == second.fingerprint
    assert first.provenance.generator_version == "1"
    assert first.provenance.source_patch == "7.41d"
    changed = _build([_match(1, [1, 2, 3, 4, 5], [6, 7, 8, 9, 11])])
    assert changed.fingerprint != first.fingerprint


def test_patch_check_flags_games_outside_kb_patch():
    inside = _match(1, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    # 2026-05-20, inside the 7.41c-style window
    outside = _match(2, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], start=T0 - 20 * 86400)
    roster = _build([inside])
    assert roster.patch_check.all_in_kb_patch is True
    assert roster.patch_check.kb_window_open_ended is True
    assert roster.patch_check.match_windows == {"1": "7.41d"}
    assert roster.matches[0].opendota_patch_id == 60

    roster = _build([inside, outside])
    assert roster.patch_check.all_in_kb_patch is False
    assert roster.patch_check.match_windows["2"] == "7.41c"


@pytest.mark.parametrize(
    ("mutate", "message"),
    [
        (lambda m: m.__setitem__("series_id", 101), "disagree on series_id"),
        (lambda m: m["picks_bans"].pop(0), "has 4 picks"),
        (lambda m: m["picks_bans"][0].__setitem__("hero_id", 999), "not in the game snapshot"),
        (lambda m: m.__setitem__("picks_bans", []), "no picks_bans"),
        (lambda m: m["picks_bans"][1].__setitem__("hero_id", 1), "picks a hero twice"),
        (lambda m: m["picks_bans"][6].__setitem__("hero_id", 1), "on both sides"),
        (lambda m: m.__setitem__("match_id", 1), "duplicate match ids"),
    ],
)
def test_inconsistent_payloads_fail_loudly(mutate, message):
    good = _match(1, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    bad = _match(2, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], start=T0 + 60)
    mutate(bad)
    with pytest.raises(RosterError, match=message):
        _build([good, bad])


def test_write_and_load_round_trip(tmp_path):
    roster = _build([_match(1, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10])])
    path = write_roster(roster, tmp_path / "rosters" / "test.json")
    loaded = load_roster(path)
    assert loaded == roster
    with pytest.raises(RosterError, match="not found"):
        load_roster(tmp_path / "missing.json")
    tampered = json.loads(path.read_text())
    tampered["heroes"][0]["picks"] = 99
    path.write_text(json.dumps(tampered))
    with pytest.raises(RosterError, match="fingerprint mismatch"):
        load_roster(path)


def test_kb_patch_without_a_window_fails():
    with pytest.raises(RosterError, match="has no window"):
        build_roster(
            [_match(1, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10])],
            HEROES,
            kb_patch="7.99",
            label="test",
            hero_identity_source="game_files:7.99",
            windows=WINDOWS,
        )
