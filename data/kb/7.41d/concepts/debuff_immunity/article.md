---
title: Debuff Immunity
kind: concept
patch: 7.41d
card:
  entity: debuff_immunity
  sentences:
  - text: Debuff immunity is a modifier that suspends most debuff effects without
      removing them or blocking their placement, grants source-dependent magic resistance
      and 100% resistance to pure and reflected damage, and protects mana from removal.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Damage
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Mana
  - text: Most debuff effects temporarily cease while immunity lasts, but debuffs
      that pierce immunity continue functioning normally.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Debuffs
  - text: Prevented effects include stun, sleep, silence, mute, break, disarm, blind,
      fear, taunt, root, leash, slows, and general stat reductions.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Debuffs
  - text: Positive debuff effects may still apply, such as Savage Roar’s movement-speed
      increase.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Debuffs
  - text: The inherent magic-resistance increase depends on the source ability.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Damage
  - text: Its 100% resistance to pure and reflected damage causes those damage types
      to deal 0 damage.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Damage
  - text: A 0 damage instance remains registered and may trigger on-damage effects
      unless flagged as HP Removal.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Damage
  - text: Abilities that pierce debuff immunity completely ignore its granted damage
      resistances.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Damage
  - text: Physical damage does not interact with debuff immunity, regardless of whether
      its ability pierces immunity.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Damage
  - text: Only ability costs can reduce mana during immunity unless the mana-removing
      ability pierces immunity.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Mana
  - text: Except for Curse of the Oldgrowth, immunity does not prevent True Sight,
      shared vision, or exposure.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#True_Sight_and_Vision
  - text: Gaining debuff immunity does not dispel debuffs, although some granting
      abilities independently apply a dispel.
    marks:
    - corpus:liquipedia_dota2/debuff_immunity@2381690#Dispel
---

# Debuff Immunity

Debuff immunity is a modifier that stops most debuff effects without dispelling the debuffs or preventing them from being placed. It also grants resistance against magical damage, immunity against pure and reflected damage, and protection against mana loss. [corpus:liquipedia_dota2/debuff_immunity@2381690]

## Mechanics

The mechanics illustration shows Visage under the effect of Black King Bar. [corpus:liquipedia_dota2/debuff_immunity@2381690#Mechanics]

### Debuffs

Debuff immunity is a status effect. Most debuffs check whether the unit has this status; if present, their effects temporarily cease until the unit is no longer debuff immune. Some debuffs, commonly those placed by ultimate abilities, pierce debuff immunity and continue functioning normally. A debuff usually either fully pierces debuff immunity or is fully blocked, though exceptions exist. Ability description boxes indicate whether a debuff pierces immunity directly below the ability name, with a compiled list in the interactions tab. [corpus:liquipedia_dota2/debuff_immunity@2381690#Debuffs]

Debuff immunity protects against negative debuff effects, but positive effects may still apply, such as Savage Roar increasing movement speed. Functional effects that merely use the target as their source of origin continue: Thunder Strike keeps striking, and Ion Shell keeps dealing damage around the unit. Triggered debuff effects can still trigger, including Last Word, Cinder Brew, and Soul Burn, but the triggered effect is itself subject to debuff immunity. Debuffs may also continue applying buffs or debuffs to other units; Penitence still grants attacking enemies attack speed. [corpus:liquipedia_dota2/debuff_immunity@2381690#Debuffs]

Debuff immunity prevents the following status effects:

| Status effect | Behavior |
|---|---|
| Stun/Sleep | Prevented |
| Silence/Mute/Break | Prevented |
| Disarm/Blind | Prevented |
| Cyclone | The unit stays on the ground |
| Hex | The unit’s model does not change |
| Forced Movement | The movement is immediately interrupted in most cases |
| Fear/Taunt | Prevented |
| Root/Leash | Prevented |
| Ethereal/Attack immunity | Prevented |
| Slows | Prevented |
| General stats reductions — movement Speed/Turn Rate | Prevented |
| General stats reductions — Attack Speed/Projectile Speed | Prevented |
| General stats reductions — Attack Damage/Spell Damage | Prevented |
| General stats reductions — Magic Resistance/Status Resistance/Armor | Prevented |
| General stats reductions — Attack Range/Cast Range | Prevented |
| General stats reductions — Attack Animation/Cast Animation | Prevented |
| General stats reductions — Strength/Agility/Intelligence | Prevented |
| General stats reductions — Health/Health Regen/Heal | Prevented |
| General stats reductions — Mana/Mana Regen/Mana Restore | Prevented |
| General stats reductions — Lifesteal/Spell Lifesteal | Prevented |
| General stats reductions — vision | Prevented |

[corpus:liquipedia_dota2/debuff_immunity@2381690#Debuffs]

### Damage

Debuff immunity inherently grants increased magic resistance, with the amount depending on the source ability. It also grants 100% resistance against pure and reflected damage, causing them to deal 0 damage. A 0 damage instance is still registered and may proc on-damage effects unless flagged as HP Removal. [corpus:liquipedia_dota2/debuff_immunity@2381690#Damage]

These resistances apply only against abilities that do not pierce debuff immunity. An ability that pierces debuff immunity and deals magical, pure, or reflected damage completely ignores the granted resistances; magical damage is dealt as though the immunity’s magic-resistance bonus were absent. Physical damage does not interact with debuff immunity, regardless of whether the ability pierces it. [corpus:liquipedia_dota2/debuff_immunity@2381690#Damage]

### Mana

Debuff immunity prevents abilities from draining, burning, or otherwise removing the unit’s mana, so only ability costs can reduce its mana unless the ability pierces debuff immunity. [corpus:liquipedia_dota2/debuff_immunity@2381690#Mana]

### True Sight and Vision

Except for Curse of the Oldgrowth, debuff immunity does not prevent abilities from revealing the unit with True Sight or shared vision, or from exposing it, even when the applying ability does not pierce debuff immunity. [corpus:liquipedia_dota2/debuff_immunity@2381690#True_Sight_and_Vision]

### Dispel

Gaining debuff immunity does not dispel any debuffs. Some abilities that provide debuff immunity independently apply a form of dispel as part of the ability. [corpus:liquipedia_dota2/debuff_immunity@2381690#Dispel]

## Sources

The following abilities grant debuff immunity and a magic-resistance bonus:

| Category | Source | Requirement |
|---|---|---|
| Debuff Immunity Sources with Basic Dispel | Black King Bar – Avatar | |
| Debuff Immunity Sources with Basic Dispel | Elder Titan – Astral Spirit | Requires Aghanim’s Scepter |
| Debuff Immunity Sources with Basic Dispel | Huskar – Life Break | |
| Debuff Immunity Sources with Basic Dispel | Juggernaut – Blade Fury | |
| Debuff Immunity Sources with Basic Dispel | Lifestealer – Rage | |
| Debuff Immunity Sources with Basic Dispel | Pangolier – Rolling Thunder | |
| Debuff Immunity Sources without Basic Dispel | Dawnbreaker – Starbreaker | Requires Aghanim’s Shard |
| Debuff Immunity Sources without Basic Dispel | Chen – Hand of God | Requires Aghanim’s Scepter |
| Debuff Immunity Sources without Basic Dispel | Lion – Mana Drain | Requires Aghanim’s Shard |
| Debuff Immunity Sources without Basic Dispel | Omniknight – Repel | |
| Debuff Immunity Sources without Basic Dispel | Pangolier – Roll Up | |
| Debuff Immunity Sources without Basic Dispel | Ringmaster – Tame the Beasts | Requires talent |
| Passive Debuff Immunity | Grimstroke – Dark Portrait (Illusion) | |

[corpus:liquipedia_dota2/debuff_immunity@2381690#Sources]