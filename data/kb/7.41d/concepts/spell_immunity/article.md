---
title: Spell Immunity
kind: concept
patch: 7.41d
card:
  entity: spell_immunity
  sentences:
  - text: Spell Immunity, formerly magic immunity, is a unit status that prevents
      most single-targeted, area-of-effect, passive, and active abilities from targeting
      the affected unit.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418
  - text: Single-target abilities cannot target a spell-immune unit.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Mechanics
  - text: Area-of-effect abilities ignore a spell-immune unit.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Mechanics
  - text: Ongoing effects may stop affecting a unit when it becomes spell immune.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Mechanics
  - text: Abilities that pierce spell immunity, including most ultimates, can fully
      target and affect the unit.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Mechanics
  - text: A traveling ability projectile has no effect if its target becomes spell
      immune before impact, unless the originating spell pierces immunity.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Mechanics
  - text: Spell immunity does not prevent regular attacks.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Mechanics
  - text: Spell immunity determines whether an ability affects a unit, not the ability’s
      damage type or damage values.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Damage_Interaction
  - text: A 0 damage instance is still registered and may trigger an on-damage effect
      unless flagged as HP Removal.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Damage_Interaction
  - text: Its innate debuff immunity suspends existing debuff effects until spell
      immunity expires.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Debuff_Immunity
  - text: Solar Guardian, Infest, Reflection (Illusion), Grab Ally, Snowball, Omnislash,
      and Swiftslash provide spell immunity as extra protection and also apply Invulnerability.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Sources
  - text: Some non-hero units are permanently spell immune through a passive ability
      or modifier.
    marks:
    - corpus:liquipedia_dota2/spell_immunity@2360418#Non-hero_Units
---

# Spell Immunity

Spell Immunity, formerly known as magic immunity, is a status that prevents most abilities—including single-targeted, area-of-effect, passive, and active abilities—from targeting the affected unit. It is not provided by any ability, but is granted to some units as an extra layer of protection, usually to ward-type units or alongside Invulnerability or Hidden. [corpus:liquipedia_dota2/spell_immunity@2360418]

## Mechanics

Spell immunity is a status effect, also known as a modifier. Most abilities first check whether a unit is spell immune:

- Single-target abilities cannot target it.
- Area-of-effect abilities ignore it.
- Ongoing effects may stop affecting it.
- Abilities that pierce spell immunity, including most ultimates, can fully target and affect it.

An ability usually either fully pierces spell immunity or is fully blocked, although exceptions exist; these can be identified through the interactions list.

If a unit becomes spell immune while an ability projectile is traveling toward it, the projectile has no effect on impact unless its originating spell pierces spell immunity. The same rule applies to most, but not all, delayed effects.

Spell immunity does not prevent regular attacks. Some attack modifiers are blocked, but critical strike, cleave, lifesteal, and most bashes generally pierce it. [corpus:liquipedia_dota2/spell_immunity@2360418#Mechanics]

### Damage interaction

Spell immunity does not itself interact with damage. When an ability pierces spell immunity, its damage is applied normally regardless of damage type; spell immunity governs whether an ability has any effect, not its damage type or damage values.

A 0 damage instance is still registered and may proc an on-damage effect unless flagged as HP Removal.

An ability that does not pierce spell immunity does not attempt to damage a spell-immune unit, regardless of damage type. To damage such a unit, the ability must pierce spell immunity or, for buffs and debuffs, already be affecting the unit. [corpus:liquipedia_dota2/spell_immunity@2360418#Damage_Interaction]

### Dispel

Certain modifiers periodically check for spell immunity and remove themselves when it is detected:

| Hero | Ability | Condition |
|---|---|---|
| Necrophos | Ghost Shroud | — |
| Grimstroke | Phantom's Embrace | — |
| Lion | Mana Drain | — |
| Shadow Shaman | Shackles | vs enemy |
| Primal Beast | Pulverize | — |
| Pugna | Life Drain | vs enemy |

[corpus:liquipedia_dota2/spell_immunity@2360418#Dispel]

### Debuff immunity

Debuff immunity is an innate component of spell immunity. It stops the effects of existing debuffs on the unit, allowing those effects to resume once spell immunity—and therefore debuff immunity—expires. [corpus:liquipedia_dota2/spell_immunity@2360418#Debuff_Immunity]

## Sources

The following abilities provide spell immunity as an extra layer of protection. All also apply Invulnerability. [corpus:liquipedia_dota2/spell_immunity@2360418#Sources]

| Hidden | Hero or unit | Ability | Additional effect |
|---|---|---|---|
| Yes | Dawnbreaker | Solar Guardian | — |
| Yes | Lifestealer | Infest^4 | Basic Dispel on caster |
| Yes | Terrorblade | Reflection (Illusion) | — |
| Yes | Tombstone | Grab Ally | — |
| Yes | Tusk | Snowball | — |
| No | Juggernaut | Omnislash^4 | Basic Dispel on caster |
| No | Juggernaut | Swiftslash^4 | Basic Dispel on caster |

[corpus:liquipedia_dota2/spell_immunity@2360418#Sources]

### Non-hero units

The following units are permanently spell immune through either a passive ability or a modifier. Spell Immunity is a passive ability affecting Self, described as: “This unit does not feel the effects from magical damage sources.” [corpus:liquipedia_dota2/spell_immunity@2360418#Non-hero_Units]

Spell immunity may be represented by a passive ability, status buff, or visual indicator. When represented by a status buff, enemies can inspect the buff and ping the unit’s remaining duration. Some units’ abilities use the other spell-immunity icon. The modifier is `modifier_magic_immune`, with the status “Spell Immune.” [corpus:liquipedia_dota2/spell_immunity@2360418#Non-hero_Units]

| Status-bar icon | Unit type | Unit | Ability |
|---|---|---|---|
| Yes | Unit | Courier | Spell Immunity |
| Yes | Unit | Undying Zombie | Spell Immunity |
| Yes | Ward | Anchor | Spell Immunity |
| Yes | Ward | Fiend's Gate | Spell Immunity |
| Yes | Ward | Ice Spire | Spell Immunity |
| Yes | Ward | Minefield Sign | Spell Immunity |
| Yes | Ward | Plague Ward | Spell Immunity |
| Yes | Ward | Roshan's Banner | Spell Immunity |
| Yes | Ward | Tombstone | Spell Immunity |
| Yes | Ward | Twin Gate | Spell Immunity |
| No | Unit | Beetle | Spell Immunity |
| No | Ward | Healing Ward | Spell Immunity |
| No | Ward | Massive Serpent Ward | Spell Immunity |
| No | Ward | Power Cog | Spell Immunity |
| No | Ward | Phoenix Sun | Spell Immunity |
| No | Ward | Serpent Ward | Spell Immunity |

[corpus:liquipedia_dota2/spell_immunity@2360418#Non-hero_Units]

## Command

The command `dota_create_ability neutral_spell_immunity` adds a passive ability that provides spell immunity. [corpus:liquipedia_dota2/spell_immunity@2360418#Spell_Immunity_Command]