---
title: Mjollnir
kind: item
patch: 7.41d
card:
  entity: mjollnir
  sentences:
  - text: Mjollnir is a 5500-gold artifact item that grants 90 attack speed and 25
      damage, gives attacks a 25% Chain Lightning chance for 180 magical damage across
      12 strikes, and provides Static Charge, whose shield has a 20% chance to release
      4 bolts for 225 magical damage.
    marks:
    - gamefile:items/item_mjollnir#cost
    - gamefile:items/item_mjollnir#attribs
    - loc:DOTA_Tooltip_ability_item_mjollnir_Description
  - text: Its build formula is Maelstrom for 2950 gold, Hyperstone for 2000 gold,
      and a Recipe for 550 gold, totaling 5500 gold.
    marks:
    - gamefile:items/item_mjollnir#components
    - gamefile:items/item_mjollnir#cost
  - text: Chain Lightning has a 0.2 cooldown, 0.25 delay, and 650 radius.
    marks:
    - gamefile:items/item_mjollnir#attribs
  - text: Static Charge has a 1.0 cooldown, 15.0 duration, 600 primary radius, 900
      radius, and 900 secondary radius.
    marks:
    - gamefile:items/item_mjollnir#attribs
  - text: Static Charge has Unit Target behavior.
    marks:
    - gamefile:items/item_mjollnir#mechanics
  - text: Static Charge is dispellable.
    marks:
    - gamefile:items/item_mjollnir#mechanics
  - text: Static Charge has 800 cast range, 50 mana cost, and a 35.0 cooldown.
    marks:
    - gamefile:items/item_mjollnir#mechanics
  - text: Static Charge places a charged shield on a target unit that can release
      a magical-damage bolt at a nearby attacker and additional enemies.
    marks:
    - loc:DOTA_Tooltip_ability_item_mjollnir_Description
  - text: Chain Lightning can trigger on attack, releasing a bolt that leaps between
      targets and deals magical damage to each.
    marks:
    - loc:DOTA_Tooltip_ability_item_mjollnir_Description
  - text: Chain Lightning's proc pierces evasion.
    marks:
    - loc:DOTA_Tooltip_ability_item_mjollnir_Description
  - text: Thor's magical hammer, made for him by the dwarves Brok and Eitri.
    marks:
    - loc:DOTA_Tooltip_ability_item_mjollnir_Lore
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