from __future__ import annotations

from dataclasses import dataclass

from invoker.schemas.derived import HeroDerived


class ValidationError(Exception):
    pass


@dataclass
class ValidationContext:
    roster_hero_ids: set[int]


def validate_hero(hero: HeroDerived, ctx: ValidationContext) -> None:
    _validate_id_integrity(hero, ctx)
    _validate_feature_uniqueness(hero)
    _validate_feature_scores(hero)
    _validate_role_distribution(hero)
    _validate_provenance(hero)


def _validate_id_integrity(hero: HeroDerived, ctx: ValidationContext) -> None:
    if hero.hero_id not in ctx.roster_hero_ids:
        raise ValidationError(f"hero_id {hero.hero_id} not in current roster")


def _validate_feature_uniqueness(hero: HeroDerived) -> None:
    for bucket_name in ("capabilities", "requirements", "liabilities", "targets"):
        features = getattr(hero, bucket_name)
        names = [feature.type for feature in features]
        if len(names) != len(set(names)):
            raise ValidationError(f"hero {hero.hero_id}: duplicate {bucket_name}")


def _validate_feature_scores(hero: HeroDerived) -> None:
    for bucket_name in ("capabilities", "requirements", "liabilities", "targets"):
        for feature in getattr(hero, bucket_name):
            if feature.score is not None and not 0.0 <= feature.score <= 1.0:
                raise ValidationError(
                    f"hero {hero.hero_id}: {bucket_name}.{feature.type} score out of range"
                )


def _validate_role_distribution(hero: HeroDerived) -> None:
    total = 0.0
    for role, weight in hero.role_distribution.items():
        if not 0.0 <= weight <= 1.0:
            raise ValidationError(f"hero {hero.hero_id}: role_distribution[{role}] out of range")
        total += weight
    if total > 1.001:
        raise ValidationError(f"hero {hero.hero_id}: role_distribution sums to > 1")


def _validate_provenance(hero: HeroDerived) -> None:
    if not hero.provenance.authored_by:
        raise ValidationError(f"hero {hero.hero_id}: provenance.authored_by missing")
    if not hero.provenance.authored_at:
        raise ValidationError(f"hero {hero.hero_id}: provenance.authored_at missing")
