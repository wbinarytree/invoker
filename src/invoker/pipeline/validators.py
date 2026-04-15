from __future__ import annotations

from dataclasses import dataclass

from invoker.pipeline.derive import confidence_for
from invoker.schemas.derived import HeroDerived
from invoker.taxonomy import load_taxonomy


class ValidationError(Exception):
    pass


@dataclass
class ValidationContext:
    roster_hero_ids: set[int]


def validate_hero(hero: HeroDerived, ctx: ValidationContext) -> None:
    _validate_tag_taxonomy(hero)
    _validate_tag_source_completeness(hero)
    _validate_reason_grounding(hero)
    _validate_statistical_sanity(hero)
    _validate_id_integrity(hero, ctx)
    _validate_bracket_consistency(hero)


def _validate_tag_taxonomy(h: HeroDerived) -> None:
    tax = load_taxonomy()
    unknown = [t for t in h.functional_tags if not tax.has(t)]
    if unknown:
        raise ValidationError(f"hero {h.hero_id}: tags not in taxonomy: {unknown}")


def _validate_tag_source_completeness(h: HeroDerived) -> None:
    cited = {s.tag for s in h.tag_sources}
    missing = [t for t in h.functional_tags if t not in cited]
    if missing:
        raise ValidationError(f"hero {h.hero_id}: tags missing tag_sources: {missing}")


def _validate_reason_grounding(h: HeroDerived) -> None:
    for kind, edges in (("synergies", h.synergies), ("counters", h.counters)):
        for br, lst in edges.items():
            for e in lst:
                if e.reason is None:
                    continue
                text = e.reason.lower().replace("_", " ")
                hero_tags = set(h.functional_tags)
                grounded = any(tag in text or tag.replace("_", " ") in text for tag in hero_tags)
                if not grounded:
                    raise ValidationError(
                        f"hero {h.hero_id} {kind}[{br}] vs {e.hero_id}: "
                        "reason not grounded in any tag"
                    )


def _validate_statistical_sanity(h: HeroDerived) -> None:
    for dct in (h.synergies, h.counters):
        for lst in dct.values():
            for e in lst:
                if e.games < 0:
                    raise ValidationError(f"hero {h.hero_id}: negative games")
                if (e.score is None) != (e.games == 0):
                    raise ValidationError(
                        f"hero {h.hero_id}: score/games mismatch — score={e.score}, games={e.games}"
                    )
                expected = confidence_for(e.games)
                if e.confidence != expected:
                    raise ValidationError(
                        f"hero {h.hero_id}: confidence {e.confidence} "
                        f"expected {expected} for {e.games} games"
                    )


def _validate_id_integrity(h: HeroDerived, ctx: ValidationContext) -> None:
    if h.hero_id not in ctx.roster_hero_ids:
        raise ValidationError(f"hero_id {h.hero_id} not in current roster")
    for dct in (h.synergies, h.counters):
        for lst in dct.values():
            for e in lst:
                if e.hero_id not in ctx.roster_hero_ids:
                    raise ValidationError(
                        f"hero {h.hero_id}: edge references unknown hero {e.hero_id}"
                    )


def _validate_bracket_consistency(h: HeroDerived) -> None:
    for br, block in h.positions.items():
        if block.window_days <= 0:
            raise ValidationError(f"positions[{br}]: window_days must be > 0")
    for br, block in h.meta.items():
        if block.games < 0:
            raise ValidationError(f"meta[{br}]: games negative")
