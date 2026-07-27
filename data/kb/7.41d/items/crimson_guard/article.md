---
title: Crimson Guard
kind: item
patch: 7.41d
card:
  entity: crimson_guard
  sentences:
  - text: Crimson Guard is an epic item costing 3725 gold that grants 6 Armor, 250
      Health, and 12 Health Regeneration; its active Guard gives nearby allied heroes
      and buildings a 100% block chance against each incoming attack, with a fixed
      block component of 70, a caster-maximum-health component of 2.0%, and DURATION
      7, while passive Damage Block has a 60% chance to block 75 damage for melee
      heroes or 50 for ranged heroes.
    marks:
    - gamefile:items/item_crimson_guard#cost
    - gamefile:items/item_crimson_guard#attribs
    - loc:DOTA_Tooltip_ability_item_crimson_guard_Description
  - text: Its BLOCK PENALTY RANGED is 25.
    marks:
    - gamefile:items/item_crimson_guard#attribs
  - text: Its BONUS AOE RADIUS is 1200.
    marks:
    - gamefile:items/item_crimson_guard#attribs
  - text: 'Build formula: Vanguard (1700 gold) + Helm of Iron Will (975 gold) + Recipe
      (1050 gold).'
    marks:
    - gamefile:items/item_crimson_guard#components
  - text: Guard is Immediate and No Target.
    marks:
    - gamefile:items/item_crimson_guard#mechanics
  - text: Guard is not dispellable.
    marks:
    - gamefile:items/item_crimson_guard#mechanics
  - text: Guard has Cast range 1200.
    marks:
    - gamefile:items/item_crimson_guard#mechanics
  - text: Guard has Mana cost 75.
    marks:
    - gamefile:items/item_crimson_guard#mechanics
  - text: Guard has Cooldown 40.0.
    marks:
    - gamefile:items/item_crimson_guard#mechanics
  - text: A cuirass originally built to protect against the dreaded Year Beast.
    marks:
    - loc:DOTA_Tooltip_ability_item_crimson_guard_Lore
---

# Crimson Guard

Crimson Guard is an epic item that grants Armor, Health, and Health Regeneration and provides the active Guard and passive Damage Block. [gamefile:items/item_crimson_guard#cost] [gamefile:items/item_crimson_guard#attribs] [loc:DOTA_Tooltip_ability_item_crimson_guard_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 3725 gold |

[gamefile:items/item_crimson_guard#cost]

| Stat | Value |
|---|---:|
| BLOCK CHANCE | 60% |
| BLOCK CHANCE ACTIVE | 100% |
| BLOCK DAMAGE ACTIVE | 70 |
| BLOCK DAMAGE MELEE | 75 |
| BLOCK DAMAGE RANGED | 50 |
| BLOCK PENALTY RANGED | 25 |
| BONUS AOE RADIUS | 1200 |
| ARMOR | 6 |
| HEALTH | 250 |
| HEALTH REGENERATION | 12 |
| DURATION | 7 |
| MAX HP PCT | 2.0% |

[gamefile:items/item_crimson_guard#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Vanguard | 1700 gold |
| Helm of Iron Will | 975 gold |
| Recipe | 1050 gold |

[gamefile:items/item_crimson_guard#components]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Immediate, No Target |
| Dispellable | No |
| Cast range | 1200 |
| Mana cost | 75 |
| Cooldown | 40.0 |

[gamefile:items/item_crimson_guard#mechanics]

Guard grants nearby allied heroes and buildings damage block against each incoming attack; its block amount combines a fixed component with a percentage of the caster’s maximum health. Damage Block gives melee and ranged heroes a chance to block incoming attack damage, with different block amounts for each. [loc:DOTA_Tooltip_ability_item_crimson_guard_Description]

*A cuirass originally built to protect against the dreaded Year Beast.* [loc:DOTA_Tooltip_ability_item_crimson_guard_Lore]