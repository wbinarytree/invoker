---
title: Damage Block
kind: concept
patch: 7.41d
card:
  entity: damage_block
  sentences:
  - text: Damage Block is a mechanic that typically reduces incoming damage by a flat
      amount and has four categories ordered by proc timing.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270
    - corpus:liquipedia_dota2/damage_block@2379270#Overview
  - text: Damage Block can block damage with the HP Removal flag.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Overview
  - text: Mana Shield Damage Block blocks all damage types before every other form
      of damage manipulation.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Mana_Shield_Damage_Block
  - text: Physical Damage Block reduces physical damage from attacks and cleave, except
      attacks from ward-type units.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Physical_Damage_Block
  - text: Damage Block (Melee) gives melee heroes a 50% chance to block 16 physical
      attack damage.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Melee_Damage_Block
  - text: Magical Damage Block reduces magical spell damage before all other damage
      manipulation except Mana Shield, so higher magic resistance yields less actual
      reduction.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Magical_Damage_Block
  - text: Universal Damage Block reduces all three damage types after almost every
      other source of damage manipulation.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Universal_Damage_Block
  - text: When multiple sources in one category activate, only the highest block value
      reduces damage.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Stacking
  - text: Sources from different categories block damage sequentially and independently.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Stacking
  - text: All side effects from simultaneously activated same-category sources occur
      even though only the highest block value reduces damage.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Side_Effects
  - text: Two Vanguards, each with a 60% proc chance, give Damage Block an 84% probability
      of proccing when Huskar is attacked.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Examples
  - text: Reducing damage to 0 prevents some on-damage effects, but effects that react
      to 0 damage can still proc.
    marks:
    - corpus:liquipedia_dota2/damage_block@2379270#Preventing_on-damage_effects
---

# Damage Block

Damage Block is a mechanic that reduces incoming damage, typically by a flat amount. [corpus:liquipedia_dota2/damage_block@2379270]

## Overview

Unlike Damage Manipulation, Damage Block always reduces rather than increases incoming damage and can block damage with the HP Removal flag. Four categories exist, ordered below by when they proc. [corpus:liquipedia_dota2/damage_block@2379270#Overview]

| Category |
|---|
| Mana Shield Damage Block [corpus:liquipedia_dota2/damage_block@2379270#Mana_Shield_Damage_Block] |
| Physical Damage Block [corpus:liquipedia_dota2/damage_block@2379270#Physical_Damage_Block] |
| Magical Damage Block [corpus:liquipedia_dota2/damage_block@2379270#Magical_Damage_Block] |
| Universal Damage Block [corpus:liquipedia_dota2/damage_block@2379270#Universal_Damage_Block] |

## Mana Shield Damage Block

Mana Shield Damage Block is driven by `MODIFIER_PROPERTY_TOTAL_CONSTANT_BLOCK_UNAVOIDABLE_PRE_ARMOR`. It blocks damage of all types before every other form of damage manipulation. Its block value is variable and adapts to the incoming damage instance’s value. [corpus:liquipedia_dota2/damage_block@2379270#Mana_Shield_Damage_Block]

## Physical Damage Block

Physical Damage Block is driven by `MODIFIER_PROPERTY_PHYSICAL_CONSTANT_BLOCK`. It reduces physical damage from attacks and cleave, except damage dealt by attacks from ward-type units. It normally offers no protection against spells, with only a few exceptions.

It triggers after Mana Shield but before all other damage manipulation. Consequently, higher armor results in less actual reduction from the block. Its effectiveness is meaningful only in relation to the attacker’s damage.

On a proc, an ocher-colored negative `-x` number with a shield icon appears on the unit and shows the exact amount blocked. In the Vanguard example, Axe blocks physical attack damage and the ochre number displays the total blocked amount. Chance-based Physical Damage Block uses pseudo-random distribution. [corpus:liquipedia_dota2/damage_block@2379270#Physical_Damage_Block]

### Melee Damage Block

| Name | Classification | Affects | Proc Chance | Damage Blocked |
|---|---|---|---:|---:|
| Damage Block (Melee) | Ability; Passive | Heroes | 50% | 16 |

Damage Block (Melee) grants melee heroes a chance to block a flat amount of physical attack damage from incoming attacks. [corpus:liquipedia_dota2/damage_block@2379270#Melee_Damage_Block]

#### Details

The proc chance is determined upon attack-projectile impact and uses pseudo-random distribution (`+30.21%` and `P(4) = 100%`). [corpus:liquipedia_dota2/damage_block@2379270#Details]

#### Other sources

| Constant Physical Damage Block Source | Proc Chance | Blocked Damage | Other values |
|---|---:|---:|---|
| Crimson Guard – Damage Block | 60% | 75 / 50 | — |
| Crimson Guard – Guard | 100% | 70/45 | Strength as Blocked Damage Bonus: 2%; Duration: 7; buff is applied to all allied heroes within 1200 radius of the caster |
| Tidehunter – Kraken Shell | 100% | 15/35/55/75 | — |
| Vanguard – Damage Block | 60% | 50 / 25 | — [corpus:liquipedia_dota2/damage_block@2379270#Other_Sources] |

#### Blocked spell damage

The following abilities’ damage is blocked when it is physical and sourced to attack.

| Physical Spell Damage Blocked |
|---|
| Blade Mail – Damage Return |
| Nyx Assassin – Spiked Carapace |
| Spectre – Dispersion |
| Luna – Moon Glaives |
| Silencer – Glaives of Wisdom 2b |
| Storm Spirit – Overload 1 [corpus:liquipedia_dota2/damage_block@2379270#Blocked_Spell_Damage] |

#### Attack damage not blocked

Only the set damage from the following attacks is not blocked.

| Attack damage setting |
|---|
| Pangolier – Swashbuckle |
| Pangolier – Shield Crash2a |
| Snapfire – Lil' Shredder [corpus:liquipedia_dota2/damage_block@2379270#Not_Blocked_Attack_Damage] |

## Magical Damage Block

Magical Damage Block is driven by `MODIFIER_PROPERTY_MAGICAL_CONSTANT_BLOCK` and reduces magical damage taken from spells. It triggers after Mana Shield but before all other damage manipulation, so higher magic resistance results in less actual reduction.

On a proc, a cyan-colored number appears on the unit and shows the exact amount blocked. In the Infused Raindrops example, Axe blocks magical damage from Shadow Poison and the cyan number displays the total blocked amount.

| Constant Magical Damage Block Source |
|---|
| Dandelion Amulet – Magical Damage Block |
| Infused Raindrops – Magical Damage Block [corpus:liquipedia_dota2/damage_block@2379270#Magical_Damage_Block] |

## Universal Damage Block

Universal Damage Block is driven by `MODIFIER_PROPERTY_TOTAL_CONSTANT_BLOCK`. It reduces damage of all three types and triggers after almost every other source of damage manipulation. An on-damage effect therefore procs directly afterward. [corpus:liquipedia_dota2/damage_block@2379270#Universal_Damage_Block]

### Sources

| Universal Damage Block Source |
|---|
| Aeon Disk – Combo Breaker |
| Pudge – Meat Shield |
| Ogre Magi – Fire Shield |
| Visage – Gravekeeper's Cloak |
| Kunkka – Ghostship |

#### Aeon Disk — Combo Breaker

| Condition | Damage Absorb |
|---|---|
| HP≥70% | Blocks damage partially so that the wielder remains with 70% health |
| HP<70% | Blocks all damage |

This effect occurs immediately before Combo Breaker activates and is distinct from the activated Combo Breaker damage reduction. [corpus:liquipedia_dota2/damage_block@2379270#Sources]

## Stacking

When multiple sources within the same Damage Block category activate, only the source with the highest block value supplies the actual blocked damage; the others cannot reduce it further. Sources from different categories block damage sequentially and independently. Stacking multiple sources from the same category is therefore inadvisable. [corpus:liquipedia_dota2/damage_block@2379270#Stacking]

### Side effects

Many Damage Block sources have negative side effects that occur when blocking damage. If multiple sources in the same category activate simultaneously, all their side effects activate even though only the source with the highest block value reduces the damage.

| Event | Source | Side effect |
|---|---|---|
| One magical damage instance | Infused Raindrops | Goes on cooldown |
| One magical damage instance | Dandelion Amulet | Goes on cooldown |
| One attack | Fire Shield | Can lose a stack |
| One attack | Gravekeeper's Cloak | Can lose a stack |
| One attack | Ghostship | Can cause rum hangover |

These side effects provide another reason why stacking multiple Damage Block sources from the same category can be inadvisable. [corpus:liquipedia_dota2/damage_block@2379270#Side_Effects]

### Chance-based blocking

Physical Damage Block proc chances work independently. For multiple Damage Block sources with the same value, the probability of any block proccing is:

`% Block = 1 - ∏ᵢ₌₁ⁿ(1 - Damage Block Sources i)` [corpus:liquipedia_dota2/damage_block@2379270#Chance-based_blocking]

#### Examples

**Example 1.** Huskar has two Vanguards in his inventory. The probability that one procs when he is attacked is:

```text
Block Chance
= 1 - (1 - 0.6) × (1 - 0.6)
= 1 - 0.16
= 0.84
```

Because Vanguard has a Damage Block proc chance of 60%, Damage Block has an 84% probability of proccing when Huskar is attacked. [corpus:liquipedia_dota2/damage_block@2379270#Examples]

**Example 2.** Warlock is affected by Guard and has one Vanguard in his inventory.

| Source | Proc Chance | Damage Block |
|---|---:|---|
| Guard from Crimson Guard | 100% | 70/45 damage blocked |
| Vanguard | 60% | Damage blocked on a ranged hero like Warlock |

Guard procs on every hit and has a greater blocked-damage value than Vanguard. Vanguard therefore has no effect on the blocked damage, whether it procs or not. [corpus:liquipedia_dota2/damage_block@2379270#Examples]

## Preventing on-damage effects

Many abilities react when a unit receives damage. Fully negating the damage prevents some from proccing, but effects that react to `0` damage can still proc after the triggering damage is negated.

The following do not react when damage is fully negated and reduced to `0`:

| Ability or effect |
|---|
| Aegis of the Immortal – Expire Restore |
| Ancient Black Dragon – Splash Attack¹ |
| Blink Dagger – Blink |
| Bloodthorn – Soul Rend |
| Bottle – Regenerate |
| Bristleback – Bristleback² |
| Clarity – Replenish |
| Healing Salve – Salve |
| Lifesteal – All sources |
| Lifestealer – Open Wounds |
| Mjollnir – Static Charge |
| Monkey King – Tree Dance |
| Orchid Malevolence – Soul Burn |
| Pugna – Life Drain |
| Runes – Regeneration |
| Spell lifesteal – All sources |
| Spirit Vessel – Soul Release |
| Templar Assassin – Psi Blades¹ |
| Tidehunter – Kraken Shell² |
| Urn of Shadows – Soul Release |
| Visage – Soul Assumption² |

¹ These work when Aphotic Shield negates the damage.  
² These abilities have damage counters that do not work when the damage is negated. [corpus:liquipedia_dota2/damage_block@2379270#Preventing_on-damage_effects]

The following still react to fully negated damage:

| Ability or effect |
|---|
| Bane – Nightmare |
| Batrider – Sticky Napalm |
| Battle Fury – Cleave |
| Blade Mail – Damage Return |
| Chen – Divine Favor |
| Death Prophet – Exorcism |
| Dragon Knight – Elder Dragon Form (splash damage) |
| Elder Titan – Echo Stomp |
| Invoker – Ghost Walk |
| Kunkka – Tidebringer |
| Lifestealer – Feast |
| Lone Druid – Summon Spirit Bear |
| Magnus – Empower |
| Spectre – Dispersion¹ |
| Spirit Bear – Return |
| Sven – Great Cleave |
| Tiny – Tree Grab |
| Tiny – Tree Throw |
| Viper – Corrosive Skin |
| Warlock – Fatal Bonds¹ |

¹ Dispersion’s damage and Fatal Bonds’ damage spread are fully unaffected by every form of reduction except magic resistance and armor. [corpus:liquipedia_dota2/damage_block@2379270#Preventing_on-damage_effects]

## Recent Changes

| Version | Date | Description |
|---|---|---|
| 7.39 | 2025-05-21 | **ADDED** Poor Man's Shield as a **TIER 2** neutral item. |
| 7.28 | 2020-12-17 | **REMOVED** Poor Man's Shield. |
| 7.23c | 2019-12-06 | **Damage Block:** Now works against player-controlled units again. Now follows the same stacking rules as other Damage Block sources instead of fully stacking with all of them. Reduced proc chance from 100% to 50%. Increased blocked damage from 8 to 16. [corpus:liquipedia_dota2/damage_block@2379270#Recent_Changes] |