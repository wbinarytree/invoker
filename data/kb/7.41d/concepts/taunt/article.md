---
title: Taunt
kind: concept
patch: 7.41d
card:
  entity: taunt
  sentences:
  - text: Taunt is a disable that forces one or more units to attack another unit.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389
  - text: It cancels the affected unit’s current order and makes it attack the taunting
      unit.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Mechanics
  - text: It fully cancels attacks against other units, ability casts, and channeling.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Mechanics
  - text: Outside attack range, the unit approaches by regular movement without using
      abilities to close the gap.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Mechanics
  - text: Taunt neither prevents other disables from affecting the unit nor bypasses
      disarms or movement-impairing effects.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Mechanics
  - text: A disarmed taunted unit follows the source to remain within attack range
      and resumes attacking when the disarm expires.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Mechanics
  - text: Orders issued while taunted execute when the taunt ends; without one, the
      unit auto-attacks nearby enemies regardless of its auto-attack settings.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Mechanics
  - text: Fog of War does not make the unit lose track of the taunt source, but unrevealed
      invisibility interrupts its pursuit until the source becomes visible.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Mechanics
  - text: Taunted heroes cannot move items into or within their backpacks, but items
      remain movable among the 6 inventory slots.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Mechanics
  - text: With multiple taunts, the first source normally has priority until its taunt
      expires, after which an active second taunt takes over.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Stacking
  - text: Duel always has priority over other taunts, while taunts have priority over
      fears.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Stacking
  - text: Berserker's Call, Little Friends, Life Break, and Winter's Curse apply taunt
      without silence, while Duel applies it with silence.
    marks:
    - corpus:liquipedia_dota2/taunt@2331389#Sources
---

# Taunt

Taunt is a disable that forces one or more units to attack another unit. [corpus:liquipedia_dota2/taunt@2331389]

## Mechanics

Taunt cancels the affected unit’s current order and makes it attack the taunting unit. It fully cancels attacks against other units, ability casts, and channeling. If outside attack range, the unit approaches the taunt source using only regular movement; it does not use abilities to close the gap. [corpus:liquipedia_dota2/taunt@2331389#Mechanics]

Other disables still affect a taunted unit, and taunt does not bypass disarms or movement-impairing effects. A disarmed taunted unit follows the taunting unit to remain within attack range and resumes attacking when the disarm expires. [corpus:liquipedia_dota2/taunt@2331389#Mechanics]

Orders can be given while taunted and are executed when the taunt ends, similarly to an order being ⇧ Shift-queued while stunned. Without an order, the unit continues auto-attacking nearby enemies regardless of its auto-attack settings until given a new order. A ⇧ Shift-queued order is placed after the auto-attack and executes once the unit stops attacking; therefore, to shift-queue while taunted, the first order must be issued without ⇧ Shift. [corpus:liquipedia_dota2/taunt@2331389#Mechanics]

The Fog of War does not prevent the unit from losing track of the taunting unit, but invisibility does. If the taunting unit becomes invisible without being revealed by True Sight, taunted units immediately stand still when no enemies are nearby or auto-attack an enemy when enemies are nearby. They immediately resume attacking the taunting unit when it becomes visible again. [corpus:liquipedia_dota2/taunt@2331389#Mechanics]

If the unit received an order while taunted or while the taunting unit was invisible, it executes the last order given. Only disabling the unit can prevent execution; the player cannot stop it. After completing the order, the unit remains still, accepts no further orders, and does not resume attacking—even if the taunting unit becomes visible again. This state lasts until the taunt expires. [corpus:liquipedia_dota2/taunt@2331389#Mechanics]

Taunted heroes cannot access their backpacks: items cannot be moved into them, and existing backpack items cannot be moved at all. Items may still be moved freely among the 6 inventory slots. Couriers and allies may still place items into the taunted unit’s backpack. [corpus:liquipedia_dota2/taunt@2331389#Mechanics]

## Stacking

Because a unit cannot attack multiple targets simultaneously, multiple taunts follow priority rules. Generally, the unit attacks the source that taunted it first, then immediately switches to the second source when the first taunt expires if the second remains active. Duel is the exception and always takes priority over other taunts. [corpus:liquipedia_dota2/taunt@2331389#Stacking]

Taunts do not stack with fears and take priority over them. Taunting a feared unit makes it move toward the taunt source. Applying fear to a taunted unit does not make it flee or move toward or away from the fear source. Because fear completely prevents acting, the unit cannot attack the taunting unit and only follows it until able to attack again. If fear remains active when taunt ends, the unit continues or starts moving as soon as the taunt ends. [corpus:liquipedia_dota2/taunt@2331389#Stacking]

Taunt-source priority, from highest to lower, is:

| Priority group |
|---|
| Duel [corpus:liquipedia_dota2/taunt@2331389#Stacking] |
| Berserker's Call / Life Break / Winter's Curse / Little Friends [corpus:liquipedia_dota2/taunt@2331389#Stacking] |

## Sources

### Without silence

| Unit | Ability |
|---|---|
| Axe | Berserker's Call [corpus:liquipedia_dota2/taunt@2331389#Sources] |
| Enchantress | Little Friends [corpus:liquipedia_dota2/taunt@2331389#Sources] |
| Huskar | Life Break<sup>2a</sup> [corpus:liquipedia_dota2/taunt@2331389#Sources] |
| Winter Wyvern | Winter's Curse [corpus:liquipedia_dota2/taunt@2331389#Sources] |

### With silence

| Unit | Ability |
|---|---|
| Legion Commander | Duel [corpus:liquipedia_dota2/taunt@2331389#Sources] |

## Abilities Castable When Taunted

| Unit | Ability |
|---|---|
| Abaddon | Borrowed Time [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Bane | Nightmare End [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Buildings | Glyph of Fortification [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Dazzle | Nothl Projection<sup>2b</sup> [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Elder Titan | Return Astral Spirit [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Elder Titan | Move Astral Spirit [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Lone Druid | Savage Roar<sup>2b</sup> [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Spirit Bear | Savage Roar<sup>2b</sup> [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Morphling | Attribute Shift<sup>2b</sup> [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Roshan | Roar of Retribution [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Rubick | Telekinesis Land<sup>2b, 4</sup> [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Scan | Scan [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Templar Assassin | Refraction<sup>2b</sup> [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Troll Warlord | Battle Trance<sup>1</sup> [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Ursa | Enrage<sup>2a</sup> [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Visage | Stone Form [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Familiar | Stone Form [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| Monkey King | Changing of the Guard [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |

| Marker | Condition |
|---|---|
| 1 | Requires Talent. [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| 2a | Requires Aghanim's Scepter. [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| 2b | Requires Aghanim's Shard. [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| 4 | Ignores Taunt only during Duel. [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |
| 5 | Ignores Taunt only if self-casted Telekinesis. [corpus:liquipedia_dota2/taunt@2331389#Abilities_Castable_When_Taunted] |

## Version History

| Version | Date | Change |
|---|---|---|
| 7.34 | 2023-08-08 | **MOVED:** Little Friends is now unlocked with Aghanim's Scepter. [corpus:liquipedia_dota2/taunt@2331389#Version_History] |
| 7.32 | 2022-08-24 | **ADDED:** new Little Friends ability that uses the Taunt mechanic. [corpus:liquipedia_dota2/taunt@2331389#Version_History] |
| 7.23 | 2019-11-26 | Life Break now uses the Taunt mechanic. [corpus:liquipedia_dota2/taunt@2331389#Version_History] |
| 7.20 | 2018-11-19 | Backpack can no longer be manipulated while taunted. [corpus:liquipedia_dota2/taunt@2331389#Version_History] |
| 6.75 | 2012-10-04 | **ADDED:** new Winter's Curse ability that uses the Taunt mechanic. [corpus:liquipedia_dota2/taunt@2331389#Version_History] |
| 6.73 | 2012-01-12 | **ADDED:** new Duel ability that uses the Taunt mechanic. [corpus:liquipedia_dota2/taunt@2331389#Version_History] |
| 6.00 | 2026-07-25 | **ADDED:** the Taunt mechanic.<br>**ADDED:** new Berserker's Call ability that uses the Taunt mechanic. [corpus:liquipedia_dota2/taunt@2331389#Version_History] |