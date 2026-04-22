from __future__ import annotations

CAPABILITIES = frozenset(
    {
        "mana_burn",
        "initiation",
        "reliable_stun",
        "mobility",
        "vision_reveal",
        "armor_reduction",
        "magic_burst",
        "wave_clear",
        "save",
        "silence",
    }
)

REQUIREMENTS = frozenset(
    {
        "needs_frontline",
        "needs_damage_followup",
        "needs_save",
        "needs_lockdown",
    }
)

LIABILITIES = frozenset(
    {
        "mana_dependence",
        "weak_to_reveal",
        "weak_to_gap_close",
        "weak_to_kiting",
        "greedy",
        "low_waveclear",
    }
)

RELATION_PATTERNS = frozenset(
    {
        "resource_punish",
        "enabler_payoff",
        "setup_followup",
        "save_protection",
        "vision_exposure",
        "mobility_punish",
    }
)

STATISTICAL_ALIGNMENT = frozenset(
    {
        "aligned",
        "weakly_aligned",
        "unobserved",
        "contradicted",
    }
)
