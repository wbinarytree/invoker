---
title: Mjollnir
kind: item
patch: 7.41d
card:
  entity: mjollnir
  sentences:
  - text: Mjollnir is a 5500-gold artifact item granting 90 Attack Speed and 25 Damage;
      its passive Chain Lightning has a 25% chance to deal 180 magical damage per
      target, while Static Charge has a 20% chance to deal 225 magical damage.
    marks:
    - gamefile:items/item_mjollnir#cost
    - gamefile:items/item_mjollnir#attribs
    - loc:DOTA_Tooltip_ability_item_mjollnir_Description
  - text: 'Build formula: Maelstrom (2950 gold), Hyperstone (2000 gold), and Recipe
      (550 gold).'
    marks:
    - gamefile:items/item_mjollnir#components
  - text: The active has Unit Target behavior.
    marks:
    - gamefile:items/item_mjollnir#mechanics
  - text: It is dispellable.
    marks:
    - gamefile:items/item_mjollnir#mechanics
  - text: Its cast range is 800.
    marks:
    - gamefile:items/item_mjollnir#mechanics
  - text: It costs 50 mana and has a 35.0 cooldown.
    marks:
    - gamefile:items/item_mjollnir#mechanics
  - text: Static Charge places a shield on a target unit that can shock a nearby attacker
      and additional enemies.
    marks:
    - loc:DOTA_Tooltip_ability_item_mjollnir_Description
  - text: Static Charge lasts 15.0 and its shock has a 1.0 cooldown.
    marks:
    - gamefile:items/item_mjollnir#attribs
  - text: Static Charge has primary radius 600, radius 900, secondary radius 900,
      and 4 strikes.
    marks:
    - gamefile:items/item_mjollnir#attribs
  - text: Chain Lightning can trigger on attack, leaps between targets, and its proc
      pierces evasion.
    marks:
    - loc:DOTA_Tooltip_ability_item_mjollnir_Description
  - text: Chain Lightning has a 0.2 cooldown and 0.25 delay.
    marks:
    - gamefile:items/item_mjollnir#attribs
  - text: Chain Lightning has 650 radius and 12 strikes.
    marks:
    - gamefile:items/item_mjollnir#attribs
---

# Mjollnir

Mjollnir is an artifact item that grants Attack Speed and Damage. [gamefile:items/item_mjollnir#cost] [gamefile:items/item_mjollnir#attribs]

## Components

| Build formula | Gold cost |
|---|---:|
| Maelstrom | 2950 gold |
| Hyperstone | 2000 gold |
| Recipe | 550 gold |
| **Mjollnir total cost** | **5500 gold** |

[gamefile:items/item_mjollnir#components] [gamefile:items/item_mjollnir#cost]

## Stats

| Stat | Value |
|---|---:|
| ATTACK SPEED | 90 |
| DAMAGE | 25 |
| CHAIN CHANCE | 25% |
| CHAIN COOLDOWN | 0.2 |
| CHAIN DAMAGE | 180 |
| CHAIN DELAY | 0.25 |
| CHAIN RADIUS | 650 |
| CHAIN STRIKES | 12 |
| ILLUSION MULTIPLIER PCT | 100 |
| MAX CHARGES | 0 |
| STATIC CHANCE | 20% |
| STATIC COOLDOWN | 1.0 |
| STATIC DAMAGE | 225 |
| STATIC DURATION | 15.0 |
| STATIC PRIMARY RADIUS | 600 |
| STATIC RADIUS | 900 |
| STATIC SECONARY RADIUS | 900 |
| STATIC STRIKES | 4 |

[gamefile:items/item_mjollnir#attribs]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Dispellable | Yes |
| Cast range | 800 |
| Mana cost | 50 |
| Cooldown | 35.0 |

[gamefile:items/item_mjollnir#mechanics]

**Static Charge** is an active ability that places a charged shield on a target unit. The shield can release a magical-damage shocking bolt at a nearby attacker and additional enemies. [loc:DOTA_Tooltip_ability_item_mjollnir_Description]

**Chain Lightning** is a passive ability that can trigger on attack, releasing a bolt that leaps between targets and deals magical damage to each. Its proc pierces evasion. [loc:DOTA_Tooltip_ability_item_mjollnir_Description]

*Thor's magical hammer, made for him by the dwarves Brok and Eitri.* [loc:DOTA_Tooltip_ability_item_mjollnir_Lore]