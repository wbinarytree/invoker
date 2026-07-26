---
title: Lifesteal
kind: concept
patch: 7.41d
card:
  entity: lifesteal
  sentences:
  - text: Lifesteal heals an attacking unit for a percentage of its physical attack
      damage dealt; percentage-based item lifesteal heals for 40% of its usual value
      against creeps.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Definition
    - corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal
  - text: Regular lifesteal does not heal from magical attack damage or spell damage
      of any damage type.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal
  - text: Percentage-based sources stack additively after each source’s creep multiplier
      and before lifesteal amplification.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal
  - text: Lifesteal-manipulation sources stack multiplicatively.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal
  - text: A killing attack calculates healing from the full damage the target would
      have received, not its remaining health.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal
  - text: Most incoming damage-manipulation effects on the attacked target do not
      change lifesteal healing.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal
  - text: Lifesteal healing has no upper limit.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal
  - text: Clones, illusions, and creep-heroes count as heroes for item lifesteal,
      while Roshan counts as a creep.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal
  - text: Instant attacks against secondary targets can heal when attack modifiers
      work with the instant-attack source.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal
  - text: Spell lifesteal heals a hero for a percentage of the actual spell damage
      it deals.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Spell_Lifesteal
  - text: Spell-lifesteal healing from a killing blow is capped by the target’s remaining
      health and does not apply to pure spell damage.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Spell_Lifesteal
  - text: Open Wounds pseudo-lifesteal heals from physical, magical, and pure damage
      to its target without a creep penalty.
    marks:
    - corpus:liquipedia_dota2/lifesteal@2393558#Pseudo-Lifesteal
---

# Lifesteal

Lifesteal heals an attacking unit while it damages an enemy. Units can gain percentage-based lifesteal from abilities, items, or talents; Morbid Mask is one example. [corpus:liquipedia_dota2/lifesteal@2393558]

## Definition

| Mechanic | Definition | Example |
|---|---|---|
| Lifesteal | Heals the attacking unit while damaging an enemy with the unit’s physical attack damage. It does not heal from magical attack damage. An instant attack heals if attack modifiers can affect it. | Lifesteal |
| Pseudo-Lifesteal | Conditionally heals the unit using lifesteal and follows all properties of the mechanic. | Bodyguard |
| Lifesteal Manipulation | Manipulates the healing values of lifesteal sources. | Sange |
| Spell Lifesteal | Heals the unit while damaging an enemy with spell damage, or heals the attacking unit from its magical attack damage. | Voodoo Mask |

[corpus:liquipedia_dota2/lifesteal@2393558#Definition]

### Total Lifesteal

Percentage-based lifesteal from items, abilities, and talents stacks independently and additively after each source’s creep lifesteal multiplier. All sources are summed before lifesteal amplification is applied as a multiplier; all lifesteal-manipulation sources stack multiplicatively. [corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal]

Healing equals a percentage of the total physical attack damage dealt to the attacked unit. If an attack exceeds the target’s current health and kills it, healing uses the damage the target would have received had it survived. Critical strikes therefore produce more healing, and certain attack modifiers work conditionally with lifesteal. [corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal]

Lifesteal does not heal from magical attack damage such as Monkey King Bar procs, or from spell damage of any damage type; only physical attack damage qualifies. Instant attacks against secondary targets can heal if attack modifiers work with the instant-attack source. [corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal]

Most damage-manipulation effects on the attacked target, such as Flesh Golem or Aeon Disk, do not alter lifesteal healing. An illusion’s lifesteal heal is based on its outgoing damage manipulation—its total attack damage—but an attacked illusion’s incoming damage manipulation does not affect the attacker’s heal. Lifesteal healing has no upper limit. [corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal]

Percentage-based item lifesteal heals for **40%** of its usual value against creeps. Attacks against clones, illusions, and creep-heroes are treated as attacks against heroes; attacks against Roshan are treated as attacks against creeps. [corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal]

Calculation sequence:

```text
Total Lifesteal
± Lifesteal Sources
× Creep Lifesteal Multiplier
+ Shared Lifesteal Sources
× Creep Lifesteal Multiplier
× Source Lifesteal Amplification
× Wielder Lifesteal Amplification
```

[corpus:liquipedia_dota2/lifesteal@2393558#Total_Lifesteal]

### Lifesteal Manipulation

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |

[corpus:liquipedia_dota2/lifesteal@2393558#Lifesteal_Manipulation]

### Equations

```text
Total Heal = Total Attack Damage Dealt × Total Lifesteal-%based

Total Lifesteal =
Self Lifesteal Amplification
× Πi=1n(Lifesteal-%based × Creep Multiplier)i
+ Πi=1n(Source Lifesteal Amplification × Shared Lifesteal-%based × Creep Multiplier)i
```

[corpus:liquipedia_dota2/lifesteal@2393558#Equations]

### Conditional Attack Damage Bonuses

These abilities grant direct attack-damage bonuses under specific circumstances. The bonuses are not displayed in the HUD and are not restricted to physical damage, but count as attack damage because they are dealt in the same instance as the unit’s attack damage. Only physical conditional attack-damage bonuses increase lifesteal healing. [corpus:liquipedia_dota2/lifesteal@2393558#Conditional_Attack_Damage_Bonus]

## Sources

Most lifesteal sources treat creep-heroes as heroes and Roshan as a creep. [corpus:liquipedia_dota2/lifesteal@2393558#Sources]

### Lifesteal Sources

| Hero or unit | Ability | Marker or condition |
|---|---|---|
| Bloodseeker | Sanguivore | Own Kill; 4 |
| Broodmother | Spider’s Milk | — |
| Broodmother | Insatiable Hunger | — |
| Chaos Knight | Chaos Strike | — |
| Dawnbreaker | Luminosity | Self |
| Doom | Scorched Earth | 2b |
| Juggernaut | Blade Dance | 1 |
| Kez | Kazurai Katana | 2b |
| Legion Commander | Moment of Courage | — |
| Lone Druid | Spirit Link | — |
| Lycan | Wolf Bite | Self |
| Marci | Bodyguard | 5 |
| Meepo | Ransack | 4 |
| Monkey King | Jingu Mastery | — |
| Troll Warlord | Battle Trance | 6 |
| Wraith King | Vampiric Spirit | — |

[corpus:liquipedia_dota2/lifesteal@2393558#Sources]

### Sources Without a Creep Penalty

| Hero or unit | Ability | Condition |
|---|---|---|
| Ancient Prowler Acolyte | Prowler Aura | — |
| Lifestealer | Feast | — |
| Lifestealer | Open Wounds | — |
| Lycan | Wolf Bite | Shared |

[corpus:liquipedia_dota2/lifesteal@2393558#Sources]

| Marker | Meaning |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |
| 4 | Considers creep-heroes as creeps and Spirit Bear as a hero. |
| 5 | Does not restore health from overkill damage. |
| 6 | Cannot lifesteal from creep-heroes, including Spirit Bear. |

[corpus:liquipedia_dota2/lifesteal@2393558#Sources]

### Items

| Item | Source |
|---|---|
| Mask of Madness | Lifesteal |
| Morbid Mask | Lifesteal |
| Satanic | Lifesteal |
| Satanic | Unholy Rage |
| Vampiric Enchantment | Lifesteal |
| Vladmir’s Offering | Vladmir’s Aura |

[corpus:liquipedia_dota2/lifesteal@2393558#Items]

### Talents

| Ability | Type | Affects | Lifesteal |
|---|---|---|---|
| Lifesteal | Passive | Self | Varies |

The talent grants the hero attack lifesteal, healing it based on the attack damage dealt. It stacks additively with other lifesteal sources and cannot lifesteal from wards, buildings, or allied units. [corpus:liquipedia_dota2/lifesteal@2393558#Talents]

| Existing lifesteal value |
|---:|
| 8% |
| 10% |
| 12% |
| 15% |
| 18% |
| 20% |
| 25% |
| 30% |
| 35% |
| 40% |
| 100% |

Self-illusions cannot use this lifesteal despite its particles remaining visible. [corpus:liquipedia_dota2/lifesteal@2393558#Talents]

| Talent bonus | Value |
|---|---:|
| Lifesteal | 12% |

[corpus:liquipedia_dota2/lifesteal@2393558#Talents]

## Pseudo-Lifesteal

Pseudo-lifesteal sources work differently and conditionally, with mechanics unique to each source. [corpus:liquipedia_dota2/lifesteal@2393558#Pseudo-Lifesteal]

| Source | Behavior |
|---|---|
| Lifestealer — Open Wounds | Heals for physical, magical, and pure damage dealt to the debuffed target. It is not affected by the creep penalty. |
| Lycan — Wolf Bite | Grants regular and shared lifesteal to both the caster and target. The shared lifesteal is not affected by the creep penalty. |

[corpus:liquipedia_dota2/lifesteal@2393558#Pseudo-Lifesteal]

## Spell Lifesteal

Spell lifesteal heals a hero from spell damage it deals. Like attack lifesteal, it is calculated as a percentage of the actual damage done. Unlike attack lifesteal, it does not heal from overkill damage: if spell damage exceeds the target’s current health and kills it, healing is based on the target’s remaining health. Spell lifesteal does not interact with pure spell-damage sources. [corpus:liquipedia_dota2/lifesteal@2393558#Spell_Lifesteal]

## Gallery

| Particle type |
|---|
| Regular lifesteal particles |
| Spell lifesteal particles |

[corpus:liquipedia_dota2/lifesteal@2393558#Gallery]

## Recent Changes

### 7.38 — 2025-02-19

Individual abilities no longer had special lifesteal rules for different situations such as heroes versus creeps or illusions and different damage types; lifesteal mechanics became consistent across every ability:

- Lifesteal applies to physical attack damage and is reduced by **40%** when damaging non-heroes.
- Spell Lifesteal applies to physical spell damage and magical damage from spells or attacks, and is reduced by **80%** when damaging non-heroes.
- Neither Lifesteal nor Spell Lifesteal applies to pure damage.
- Holding **Alt** while viewing an item that provides Lifesteal or Spell Lifesteal shows its percentages for attacks versus spells and creeps versus heroes.

The following sources and targets provide no lifesteal:

| Excluded source or target |
|---|
| Attacks that do not proc attack modifiers |
| Attack damage against wards, buildings, or couriers |
| Spell damage against illusions, wards, buildings, or couriers |
| Reflected damage |
| Spells that remove health instead of dealing direct damage |
| Any damage dealt to self or allies |

A small number of abilities do not use Lifesteal or Spell Lifesteal but still heal and can benefit from Lifesteal Amp:

| Ability | Healing behavior |
|---|---|
| Lifestealer — Open Wounds | Heals attackers for a percentage of damage done. |
| Lifestealer — Feast | Heals for a percentage of the target’s maximum health. |
| Meepo — Ransack | Heals all Meepos a flat amount for each strike. |

[corpus:liquipedia_dota2/lifesteal@2393558#Recent_Changes]

### 7.33c — 2023-05-13

Item lifesteal against creeps increased from **50%** to **60%**. [corpus:liquipedia_dota2/lifesteal@2393558#Recent_Changes]

### 7.32 — 2022-08-24

Item lifesteal against creeps decreased from **100%** to **50%**. [corpus:liquipedia_dota2/lifesteal@2393558#Recent_Changes]