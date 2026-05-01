import json
import shutil
from pathlib import Path

import pytest

from invoker.service import KnowledgeService, KnowledgeServiceError
from invoker.service.http import handle_http_request
from invoker.service.mcp import KnowledgeMCPAdapter

FIXTURE_GAME_SNAPSHOT = Path(__file__).resolve().parents[2] / "fixtures" / "game_snapshot" / "7.41b"


def _write_bundle(
    tmp_path: Path,
    *,
    teams: list[dict] | None = None,
    registry_teams: list[dict] | None = None,
) -> Path:
    bundle = tmp_path / "bundle"
    game_patch_dir = bundle / "game_constants" / "7.41b"
    shutil.copytree(FIXTURE_GAME_SNAPSHOT, game_patch_dir)
    bundle.mkdir(exist_ok=True)
    (bundle / "bundle.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "default_patch": "7.41b",
                "patches": ["7.41b"],
                "generated_at": "2026-05-01T00:00:00Z",
            },
            indent=2,
        )
    )
    if registry_teams is not None:
        registry = bundle / "authored" / "teams.yaml"
        registry.parent.mkdir(parents=True)
        registry.write_text(_teams_yaml(registry_teams))
    if teams is not None:
        teams_dir = bundle / "derived" / "7.41b" / "teams"
        teams_dir.mkdir(parents=True)
        profiles = []
        for team in teams:
            team_id = team["team_id"]
            roster_hash = team.get("roster_hash", f"hash-{team_id}")
            profile_path = teams_dir / str(team_id) / roster_hash / "profile.json"
            profile_path.parent.mkdir(parents=True)
            profile = _profile(team_id=team_id, name=team["name"], roster_hash=roster_hash)
            profile["team"]["observed_names"] = team.get(
                "observed_names", [{"name": team["name"], "count": 1}]
            )
            profile["team"]["aliases"] = team.get("aliases", [])
            if "players" in team:
                profile["roster"]["players"] = team["players"]
                profile["players"] = [
                    {
                        "account_id": player["account_id"],
                        "personaname": player.get("personaname"),
                        "games": 1,
                        "wins": 1,
                        "hero_pool": [
                            {
                                "hero_id": 73,
                                "localized_name": "Alchemist",
                                "games": 1,
                                "wins": 1,
                                "win_match_ids": [1],
                                "loss_match_ids": [],
                            }
                        ],
                    }
                    for player in team["players"]
                ]
            profile_path.write_text(json.dumps(profile, indent=2))
            profiles.append(
                {
                    "team_id": team_id,
                    "team_name": team["name"],
                    "roster_hash": roster_hash,
                    "patch": "7.41b",
                    "match_count": 1,
                    "hero_count": 1,
                    "path": f"{team_id}/{roster_hash}/profile.json",
                }
            )
        (teams_dir / "index.json").write_text(
            json.dumps({"schema_version": 1, "profiles": profiles}, indent=2)
        )
    return bundle


def _teams_yaml(teams: list[dict]) -> str:
    lines = ["schema_version: 1", "teams:"]
    for team in teams:
        lines.extend(
            [
                f"  - team_id: {team['team_id']}",
                f"    name: {team['name']}",
                "    aliases:",
            ]
        )
        aliases = team.get("aliases") or []
        if aliases:
            lines.extend(f"      - {alias}" for alias in aliases)
        else:
            lines.append("      []")
        lines.append("    players:")
        for player in team.get("players") or []:
            lines.extend(
                [
                    f"      - account_id: {player['account_id']}",
                    f"        name: {player['name']}",
                    f"        position: {player['position']}",
                ]
            )
    return "\n".join(lines) + "\n"


def _profile(*, team_id: int, name: str, roster_hash: str) -> dict:
    return {
        "schema_version": 1,
        "team": {
            "team_id": team_id,
            "name": name,
            "tag": "EX",
            "name_source": "registry",
            "observed_names": [{"name": name, "count": 1}],
            "aliases": [],
        },
        "scope": {"match_count": 1, "contributing_match_count": 1},
        "roster": {
            "roster_hash": roster_hash,
            "players": [
                {
                    "account_id": 10,
                    "personaname": "Carry",
                    "games": 1,
                    "primary_position": 1,
                    "position_source": "authored",
                }
            ],
            "stand_ins": [
                {
                    "account_id": 99,
                    "personaname": "Standin",
                    "games": 1,
                    "match_ids": [2],
                }
            ],
            "canonical_source": "authored_registry",
        },
        "hero_pool": [
            {
                "hero_id": 73,
                "localized_name": "Alchemist",
                "games": 1,
                "wins": 1,
                "positions": [{"position": 1, "games": 1}],
                "players": [{"account_id": 10, "personaname": "Carry", "games": 1}],
                "win_match_ids": [1],
                "loss_match_ids": [],
            }
        ],
        "players": [
            {
                "account_id": 10,
                "personaname": "Carry",
                "games": 1,
                "wins": 1,
                "hero_pool": [
                    {
                        "hero_id": 73,
                        "localized_name": "Alchemist",
                        "games": 1,
                        "wins": 1,
                        "win_match_ids": [1],
                        "loss_match_ids": [],
                    }
                ],
            }
        ],
        "observed_patch_windows": [{"patch": "7.41b", "match_count": 1}],
        "tournaments": [{"leagueid": 1, "league_name": "Fixture League"}],
        "source": {
            "fetched_at": "2026-05-01T00:00:00Z",
            "missing_match_detail_count": 0,
            "match_roster_classifications": [],
        },
    }


def test_hero_constants_are_backed_by_bundled_game_files(tmp_path):
    service = KnowledgeService(_write_bundle(tmp_path, teams=[]))

    response = service.get_hero_constants("Alchemist")

    assert response["service_schema_version"] == 1
    assert response["kind"] == "hero_constants"
    assert response["patch"] == "7.41b"
    assert response["source"]["artifact"] == "game_constants"
    assert response["source"]["schema_version"] == 1
    assert response["data"]["hero"]["localized_name"] == "Alchemist"
    assert response["data"]["stats"]["base_str"]["value"] == 23.0
    assert any(
        ability["name"] == "Acid Spray" for ability in response["data"]["abilities"]
    )


def test_team_queries_match_profile_and_do_not_expose_roster_hash(tmp_path):
    service = KnowledgeService(
        _write_bundle(tmp_path, teams=[{"team_id": 123, "name": "Example Team"}])
    )

    roster = service.get_team_roster("Example Team")
    hero_pool = service.get_team_hero_pool(123)
    player_pool = service.get_team_player_hero_pool("Example Team", "Carry")
    profile = service.get_team_profile(123)

    assert roster["data"]["team"]["team_id"] == 123
    assert roster["data"]["roster"]["players"][0]["account_id"] == 10
    assert hero_pool["data"]["hero_pool"][0]["hero_id"] == 73
    assert player_pool["data"]["hero_pool"][0]["localized_name"] == "Alchemist"
    assert "roster_hash" not in json.dumps(profile)


def test_resolution_returns_candidates_instead_of_guessing_ambiguous_names(tmp_path):
    bundle = _write_bundle(
        tmp_path,
        teams=[
            {"team_id": 123, "name": "Example Team"},
            {"team_id": 456, "name": "Example Team"},
        ],
    )
    service = KnowledgeService(bundle)

    resolution = service.resolve_team("Example Team")

    assert [candidate["team_id"] for candidate in resolution["data"]["candidates"]] == [
        123,
        456,
    ]
    with pytest.raises(KnowledgeServiceError, match="ambiguous"):
        service.get_team_profile("Example Team")


def test_player_resolution_returns_candidates_instead_of_guessing(tmp_path):
    bundle = _write_bundle(
        tmp_path,
        teams=[
            {
                "team_id": 123,
                "name": "Example Team",
                "players": [
                    {"account_id": 10, "personaname": "Same Name"},
                    {"account_id": 11, "personaname": "Same Name"},
                ],
            }
        ],
    )
    service = KnowledgeService(bundle)

    resolution = service.resolve_player("Same Name", team=123)

    assert [candidate["account_id"] for candidate in resolution["data"]["candidates"]] == [
        10,
        11,
    ]
    with pytest.raises(KnowledgeServiceError, match="ambiguous"):
        service.get_team_player_hero_pool(123, "Same Name")


def test_team_registry_enriches_alias_and_player_resolution(tmp_path):
    bundle = _write_bundle(
        tmp_path,
        teams=[
            {
                "team_id": 123,
                "name": "Observed Name",
                "players": [{"account_id": 10, "personaname": None}],
            }
        ],
        registry_teams=[
            {
                "team_id": 123,
                "name": "Registry Team",
                "aliases": ["RT"],
                "players": [{"account_id": 10, "name": "Registry Carry", "position": 1}],
            }
        ],
    )
    service = KnowledgeService(bundle)

    roster = service.get_team_roster("RT")
    player = service.get_team_player_hero_pool("Registry Team", "Registry Carry")

    assert roster["data"]["team"]["name"] == "Registry Team"
    assert roster["data"]["team"]["aliases"] == ["RT"]
    assert roster["data"]["roster"]["players"][0]["registry_name"] == "Registry Carry"
    assert roster["data"]["roster"]["players"][0]["registry_position"] == 1
    assert player["data"]["player"]["registry_name"] == "Registry Carry"


def test_missing_team_profile_error_includes_build_command(tmp_path):
    service = KnowledgeService(_write_bundle(tmp_path, teams=[]))

    with pytest.raises(KnowledgeServiceError, match="build-team-profile") as exc:
        service.get_team_profile(999)

    assert exc.value.code == "team_profile_not_found"


def test_http_and_mcp_adapters_return_equivalent_payloads(tmp_path):
    service = KnowledgeService(
        _write_bundle(tmp_path, teams=[{"team_id": 123, "name": "Example Team"}])
    )
    mcp = KnowledgeMCPAdapter(service)

    status, http_payload = handle_http_request(
        service,
        method="POST",
        path="/get_team_roster",
        body=json.dumps({"team": "Example Team"}).encode(),
    )
    mcp_payload = mcp.call_tool("get_team_roster", {"team": "Example Team"})

    assert status == 200
    assert http_payload == mcp_payload
    assert mcp.list_tools()[0]["name"] == "list_bundle_patches"
