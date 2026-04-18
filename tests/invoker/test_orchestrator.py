import json
from pathlib import Path

from invoker.kb import KnowledgeBase
from invoker.llm.client import LLMResponse
from invoker.pipeline.orchestrator import (
    HeroRawBundle,
    extract_hero,
    finalize_patch,
    reason_hero,
)


class ScriptedClient:
    """LLM that returns preset outputs based on prompt content."""

    model_name = "scripted"

    def generate_json(
        self,
        prompt: str,
        *,
        prompt_version: int,
        schema: object | None = None,
        cache_tag: str | None = None,
    ) -> LLMResponse:
        if "functional_tags" in prompt:
            return LLMResponse(
                text=json.dumps(
                    {
                        "functional_tags": [
                            "armor_reduction",
                            "single_target_disable",
                            "initiation",
                        ],
                        "tag_sources": [
                            {
                                "tag": "armor_reduction",
                                "ability": "Corrosive Haze",
                                "evidence": "reduces armor",
                            },
                            {
                                "tag": "single_target_disable",
                                "ability": "Slithereen Crush",
                                "evidence": "stuns 1.6s",
                            },
                            {
                                "tag": "initiation",
                                "ability": "Slithereen Crush",
                                "evidence": "blink-in AoE stun",
                            },
                        ],
                    }
                ),
                model="scripted",
                prompt_version=prompt_version,
            )
        # Batch reason prompt: extract hero_b_ids and return one reason per edge.
        import re

        ids = [int(m) for m in re.findall(r"hero_b_id=(\d+)", prompt)]
        return LLMResponse(
            text=json.dumps(
                [
                    {
                        "hero_b_id": hid,
                        "reason": (
                            f"Armor reduction amplifies single_target_disable against {hid}."
                        ),
                    }
                    for hid in ids
                ]
            ),
            model="scripted",
            prompt_version=prompt_version,
        )


def _slardar_bundle() -> HeroRawBundle:
    return HeroRawBundle(
        hero_id=28,
        localized_name="Slardar",
        internal_name="npc_dota_hero_slardar",
        roles=["Initiator", "Disabler"],
        abilities=[
            {"name": "Slithereen Crush", "text": "AoE stun with armor reduction"},
            {"name": "Corrosive Haze", "text": "Armor reduction debuff"},
        ],
        stratz_edges=[{"heroId1": 28, "heroId2": 120, "synergy": 0.08, "matchCount": 50}],
        opendota_matchups=[{"hero_id": 96, "games_played": 34, "wins": 12}],
        position_counts={"1": 0, "2": 0, "3": 34, "4": 0, "5": 0},
        total_pro_games=34,
        window_days=90,
        contest_rate=0.12,
        win_rate=0.51,
        meta_history=[],
    )


def _stub_bundle(hero_id: int, name: str) -> HeroRawBundle:
    """Minimal bundle for a hero_b target. Abilities need only satisfy the
    extract prompt shape; the scripted client returns the same tags regardless."""
    return HeroRawBundle(
        hero_id=hero_id,
        localized_name=name,
        internal_name=f"npc_dota_hero_{name.lower()}",
        roles=["Carry"],
        abilities=[{"name": "Placeholder", "text": "does damage"}],
        stratz_edges=None,
        opendota_matchups=None,
        position_counts={"1": 34, "2": 0, "3": 0, "4": 0, "5": 0},
        total_pro_games=34,
        window_days=90,
        contest_rate=0.05,
        win_rate=0.50,
        meta_history=[],
    )


def _preseed_hero_with_tags(tmp_path: Path, hero_id: int, name: str, tags: list[str]) -> None:
    """Write a minimal hero file so reason_hero sees B-side tags without going
    through extraction. Used by tests that exercise the reason pass in isolation."""
    from invoker.pipeline.writer import write_hero
    from invoker.schemas.derived import (
        HeroDerived,
        MetaBlock,
        PositionBlock,
        Provenance,
        TagSource,
    )

    hero = HeroDerived(
        schema_version=1,
        generator_version="invoker@test",
        source_patch="7.41b",
        generated_at="2026-04-18T00:00:00Z",
        hero_id=hero_id,
        localized_name=name,
        internal_name=f"npc_dota_hero_{name.lower()}",
        roles=["Carry"],
        functional_tags=tags,
        tag_sources=[TagSource(tag=t, ability="n/a", evidence="seed") for t in tags],
        positions={"pro": PositionBlock(weights={"1": 1.0}, games=10, window_days=90)},
        synergies={"pro": []},
        counters={"pro": []},
        meta={"pro": MetaBlock(contest_rate=0.0, win_rate=0.5, tier="niche", games=10)},
        meta_history=[],
        provenance=Provenance(mechanical={"model": "seed"}, statistical={"pro": {}}),
    )
    write_hero(tmp_path, "7.41b", hero)


def test_two_pass_flow_produces_valid_hero_with_reasons(tmp_path: Path):
    """Pass 1 extracts A + B; pass 2 reasons over A and sees B's tags."""
    client = ScriptedClient()
    bundles = [_slardar_bundle(), _stub_bundle(120, "DragonKnight"), _stub_bundle(96, "Mirana")]

    for b in bundles:
        r = extract_hero(tmp_path, "7.41b", "invoker@test", b, client)
        assert r.success

    r = reason_hero(tmp_path, "7.41b", 28, client)
    assert r.success
    assert r.reasons_written >= 1

    finalize_patch(tmp_path, "7.41b", [28, 120, 96], complete=True)

    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    h = kb.hero(28)
    assert h.localized_name == "Slardar"
    assert "armor_reduction" in h.functional_tags
    assert len(h.synergies["pro"]) == 1
    assert h.synergies["pro"][0].reason is not None


def test_manual_client_extract_returns_pending(tmp_path: Path):
    from invoker.llm import CachingLLMClient
    from invoker.llm.manual import ManualClient

    inner = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    client = CachingLLMClient(inner, tmp_path / "cache")

    result = extract_hero(tmp_path, "7.41b", "invoker@test", _slardar_bundle(), client)

    assert result.success is False
    assert result.failure_reason == "pending_manual"
    assert result.pending_manual_paths is not None
    prompt = result.pending_manual_paths[0]
    assert prompt.exists()
    assert "extract/Slardar" in str(prompt)


def test_manual_client_resumes_across_both_passes(tmp_path: Path):
    """
    Full manual-mode resume contract, exercised one pass at a time:
      1. pass 1 writes an extract prompt and aborts.
      2. after the extract response is filled, pass 1 succeeds; pass 2 then
         writes a reason prompt and aborts.
      3. after the reason response is filled, pass 2 succeeds with reasons.
    """
    import json

    from invoker.llm import CachingLLMClient
    from invoker.llm.manual import ManualClient

    inner = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    client = CachingLLMClient(inner, tmp_path / "cache")
    bundle = _slardar_bundle()

    # Pre-seed hero_b files so pass 2 has tags to ground against.
    _preseed_hero_with_tags(tmp_path, 120, "DragonKnight", ["physical_carry"])
    _preseed_hero_with_tags(tmp_path, 96, "Centaur", ["physical_carry"])

    # Round 1: pass 1 pending.
    r1 = extract_hero(tmp_path, "7.41b", "invoker@test", bundle, client)
    assert r1.success is False
    assert r1.failure_reason == "pending_manual"
    extract_prompt = r1.pending_manual_paths[0]

    def _write_response(prompt_path: Path, payload: object) -> None:
        response_path = (tmp_path / "out" / prompt_path.relative_to(tmp_path / "in")).with_suffix(
            ".txt"
        )
        response_path.parent.mkdir(parents=True, exist_ok=True)
        response_path.write_text(json.dumps(payload))

    _write_response(
        extract_prompt,
        {
            "functional_tags": ["armor_reduction"],
            "tag_sources": [
                {
                    "tag": "armor_reduction",
                    "ability": "Corrosive Haze",
                    "evidence": "reduces armor",
                }
            ],
        },
    )

    # Round 2: pass 1 succeeds (cache miss → disk response). Pass 2 pending.
    r2_ext = extract_hero(tmp_path, "7.41b", "invoker@test", bundle, client)
    assert r2_ext.success is True
    r2_rsn = reason_hero(tmp_path, "7.41b", bundle.hero_id, client)
    assert r2_rsn.success is True
    assert r2_rsn.pending_manual_paths is not None
    reason_prompt = r2_rsn.pending_manual_paths[0]
    assert "reason/Slardar" in str(reason_prompt)
    assert r2_rsn.reasons_written == 0  # prompt written, not yet answered

    _write_response(
        reason_prompt,
        [
            {"hero_b_id": 120, "reason": "armor_reduction amplifies carries."},
            {"hero_b_id": 96, "reason": "armor_reduction shreds this matchup."},
        ],
    )

    # Round 3: pass 2 succeeds.
    r3_rsn = reason_hero(tmp_path, "7.41b", bundle.hero_id, client)
    assert r3_rsn.success is True
    assert r3_rsn.reasons_written == 2
    assert r3_rsn.pending_manual_paths is None


def test_max_reason_edges_caps_candidates(tmp_path: Path):
    bundle = _slardar_bundle()
    bundle.opendota_matchups = None
    bundle.stratz_edges = [
        {"heroId1": 28, "heroId2": hid, "synergy": 0.1 - 0.001 * i, "matchCount": 50}
        for i, hid in enumerate([120, 121, 122, 123, 124, 125, 126])
    ]
    for hid in (120, 121, 122, 123, 124, 125, 126):
        _preseed_hero_with_tags(tmp_path, hid, f"hero{hid}", ["physical_carry"])

    class CountingClient(ScriptedClient):
        def __init__(self) -> None:
            self.batch_edge_count = 0

        def generate_json(self, prompt, **kwargs):
            if "hero_b_id" in prompt:
                import re

                self.batch_edge_count = len(re.findall(r"hero_b_id=", prompt))
            return super().generate_json(prompt, **kwargs)

    client = CountingClient()
    assert extract_hero(tmp_path, "7.41b", "invoker@test", bundle, client).success
    reason_hero(tmp_path, "7.41b", bundle.hero_id, client, max_edges=3)
    assert client.batch_edge_count == 3


# ---------------------------------------------------------------------------
# Two-pass contract — explicit coverage for extract_hero / reason_hero split.
# ---------------------------------------------------------------------------


def test_extract_hero_writes_tags_without_reasons(tmp_path: Path):
    """Pass 1 must never call the reason prompt."""

    class CountingClient(ScriptedClient):
        def __init__(self) -> None:
            self.extract_calls = 0
            self.reason_calls = 0

        def generate_json(self, prompt, **kwargs):
            if "functional_tags" in prompt:
                self.extract_calls += 1
            else:
                self.reason_calls += 1
            return super().generate_json(prompt, **kwargs)

    client = CountingClient()
    r = extract_hero(tmp_path, "7.41b", "invoker@test", _slardar_bundle(), client)
    assert r.success
    assert client.extract_calls == 1
    assert client.reason_calls == 0

    # Hero file is on disk with tags and stat edges but no reasons.
    from invoker.pipeline.writer import read_hero

    hero = read_hero(tmp_path, "7.41b", 28)
    assert hero.functional_tags
    assert hero.synergies["pro"]
    for edge in hero.synergies["pro"] + hero.counters["pro"]:
        assert edge.reason is None
        assert edge.reason_provenance is None


def test_reason_hero_skips_when_no_hero_b_has_tags(tmp_path: Path):
    """The `tagged == 0` guard must short-circuit before the batch fires."""

    class CountingClient(ScriptedClient):
        def __init__(self) -> None:
            self.reason_calls = 0

        def generate_json(self, prompt, **kwargs):
            if "functional_tags" not in prompt:
                self.reason_calls += 1
            return super().generate_json(prompt, **kwargs)

    client = CountingClient()
    # Only Slardar is extracted; hero_b (120, 96) tag coverage is empty.
    assert extract_hero(tmp_path, "7.41b", "invoker@test", _slardar_bundle(), client).success

    r = reason_hero(tmp_path, "7.41b", 28, client)
    assert r.success  # clean skip, not a failure
    assert r.reasons_written == 0
    assert r.reasons_skipped == 0
    assert client.reason_calls == 0

    from invoker.pipeline.writer import read_hero

    hero = read_hero(tmp_path, "7.41b", 28)
    for edge in hero.synergies["pro"] + hero.counters["pro"]:
        assert edge.reason is None


def test_reason_hero_runs_when_any_hero_b_has_tags(tmp_path: Path):
    """If at least one hero_b has tags, the batch runs and reasons land."""
    client = ScriptedClient()
    assert extract_hero(tmp_path, "7.41b", "invoker@test", _slardar_bundle(), client).success
    # Only hero 120 has tags; 96 does not.
    _preseed_hero_with_tags(tmp_path, 120, "DragonKnight", ["physical_carry"])

    r = reason_hero(tmp_path, "7.41b", 28, client)
    assert r.success
    assert r.reasons_written >= 1  # at least the 120 edge gets a reason

    from invoker.pipeline.writer import read_hero

    hero = read_hero(tmp_path, "7.41b", 28)
    by_id = {e.hero_id: e for e in hero.synergies["pro"] + hero.counters["pro"]}
    assert by_id[120].reason is not None


def test_reason_hero_missing_hero_file_returns_failure(tmp_path: Path):
    r = reason_hero(tmp_path, "7.41b", 999, ScriptedClient())
    assert not r.success
    assert r.failure_reason == "hero_file_missing"


def test_two_pass_ordering_unblocks_cross_hero_reasons(tmp_path: Path):
    """
    The canonical motivation: running all pass 1s before any pass 2 lets
    Slardar's reason batch see hero 120's tags, which is impossible if extract
    and reason are interleaved per hero.
    """
    client = ScriptedClient()
    bundles = [
        _slardar_bundle(),
        _stub_bundle(120, "DragonKnight"),
        _stub_bundle(96, "Mirana"),
    ]

    # Pass 1: extract all.
    for b in bundles:
        assert extract_hero(tmp_path, "7.41b", "invoker@test", b, client).success

    # Pass 2: reason over all. Slardar sees 120 + 96 tags.
    r = reason_hero(tmp_path, "7.41b", 28, client)
    assert r.reasons_written == 2  # synergy 120 + counter 96

    from invoker.pipeline.writer import read_hero

    hero = read_hero(tmp_path, "7.41b", 28)
    assert all(e.reason for e in hero.synergies["pro"])
    assert all(e.reason for e in hero.counters["pro"])


def test_reason_hero_is_idempotent_under_caching(tmp_path: Path):
    """Re-running reason_hero with a cache-hot client should not re-hit the LLM."""
    from invoker.llm import CachingLLMClient

    class CountingScripted(ScriptedClient):
        def __init__(self) -> None:
            self.calls = 0

        def generate_json(self, prompt, **kwargs):
            self.calls += 1
            return super().generate_json(prompt, **kwargs)

    inner = CountingScripted()
    client = CachingLLMClient(inner, tmp_path / "cache")

    for b in [_slardar_bundle(), _stub_bundle(120, "DragonKnight"), _stub_bundle(96, "Mirana")]:
        extract_hero(tmp_path, "7.41b", "invoker@test", b, client)
    reason_hero(tmp_path, "7.41b", 28, client)
    first_calls = inner.calls

    # Second reason pass: every prompt is cache-hot.
    reason_hero(tmp_path, "7.41b", 28, client)
    assert inner.calls == first_calls
