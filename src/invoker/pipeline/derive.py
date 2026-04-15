from __future__ import annotations

from dataclasses import dataclass

CONFIDENCE_BUCKETS = [
    (40, "high"),
    (10, "med"),
    (1, "low"),
    (0, "none"),
]


def confidence_for(games: int) -> str:
    for threshold, label in CONFIDENCE_BUCKETS:
        if games >= threshold:
            return label
    return "none"


@dataclass
class PositionStats:
    weights: dict[str, float]
    games: int
    window_days: int


def position_weights(counts_per_position: dict[str, int], floor: float = 0.03) -> dict[str, float]:
    total = sum(counts_per_position.values())
    if total == 0:
        return {str(p): 0.0 for p in range(1, 6)}
    raw = {str(p): counts_per_position.get(str(p), 0) / total for p in range(1, 6)}
    above_floor = {k: v for k, v in raw.items() if v >= floor}
    floored = sum(raw[k] for k in raw if k not in above_floor)
    if above_floor:
        rescale = 1.0 / (1.0 - floored if 1.0 - floored > 0 else 1.0)
        weights = {k: (v * rescale if k in above_floor else 0.0) for k, v in raw.items()}
        s = sum(weights.values()) or 1.0
        weights = {k: round(v / s, 3) for k, v in weights.items()}
    else:
        weights = {k: round(v, 3) for k, v in raw.items()}
    return weights


@dataclass
class MetaTier:
    contest_rate: float
    win_rate: float
    tier: str
    games: int


def meta_tier(contest_rate: float, win_rate: float) -> str:
    if contest_rate >= 0.5:
        return "first_phase_priority"
    if contest_rate >= 0.25:
        return "high_priority"
    if contest_rate >= 0.10:
        return "situational"
    return "niche"


@dataclass
class StatisticalEdge:
    hero_id: int
    score: float | None
    games: int
    confidence: str
    source: str
    reason: str | None = None


def merge_matchups(
    stratz_edges: list[dict] | None,
    opendota_matchups: list[dict] | None,
    *,
    hero_id: int,
) -> tuple[list[StatisticalEdge], list[StatisticalEdge]]:
    """
    Merge synergy and counter data. Preference order:
      - synergies: prefer STRATZ (signed advantage). If absent, fall back to OpenDota matchup
        win-rate delta against average.
      - counters: symmetric — negative advantage becomes a counter.
    Result: (synergies, counters) — each a list of StatisticalEdge.
    """
    synergies: dict[int, StatisticalEdge] = {}
    counters: dict[int, StatisticalEdge] = {}

    if stratz_edges:
        for edge in stratz_edges:
            other = edge["heroId2"] if edge["heroId1"] == hero_id else edge["heroId1"]
            games = int(edge["matchCount"])
            score = float(edge["synergy"])
            target = synergies if score >= 0 else counters
            target[other] = StatisticalEdge(
                hero_id=other,
                score=score,
                games=games,
                confidence=confidence_for(games),
                source="stratz",
            )

    if opendota_matchups:
        for m in opendota_matchups:
            other = int(m["hero_id"])
            if other in synergies or other in counters:
                continue
            games = int(m["games_played"])
            if games == 0:
                continue
            wr = m["wins"] / games
            score = round(wr - 0.5, 3)
            target = synergies if score >= 0 else counters
            target[other] = StatisticalEdge(
                hero_id=other,
                score=score,
                games=games,
                confidence=confidence_for(games),
                source="opendota",
            )

    return (
        sorted(synergies.values(), key=lambda e: abs(e.score or 0), reverse=True),
        sorted(counters.values(), key=lambda e: abs(e.score or 0), reverse=True),
    )
