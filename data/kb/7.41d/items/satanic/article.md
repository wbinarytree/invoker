---
title: Satanic
kind: item
patch: 7.41d
card:
  entity: satanic
  sentences:
  - text: Satanic is a 5050-gold artifact granting 25 Damage, 25 Strength, and 30%
      Lifesteal; Unholy Rage increases Lifesteal to a displayed total of 175% for
      its 6.0 duration.
    marks:
    - gamefile:items/item_satanic#cost
    - gamefile:items/item_satanic#attribs
    - loc:DOTA_Tooltip_ability_item_satanic_Description
  - text: Its Unholy Lifesteal Percent is 145.
    marks:
    - gamefile:items/item_satanic#attribs
  - text: Satanic is built from Reaver (2800 gold), Claymore (1350 gold), and Morbid
      Mask (900 gold).
    marks:
    - gamefile:items/item_satanic#components
    - gamefile:items/item_satanic#cost
  - text: Unholy Rage has Immediate, No Target behavior.
    marks:
    - gamefile:items/item_satanic#mechanics
  - text: Unholy Rage has a 30.0 cooldown.
    marks:
    - gamefile:items/item_satanic#mechanics
  - text: Unholy Rage is not dispellable.
    marks:
    - gamefile:items/item_satanic#mechanics
  - text: Unholy Rage has Basic Dispel as its dispel type.
    marks:
    - loc:DOTA_Tooltip_ability_item_satanic_Description
  - text: Passive Lifesteal heals the attacker for a percentage of physical damage
      dealt.
    marks:
    - loc:DOTA_Tooltip_ability_item_satanic_Description
---

# Satanic

Satanic is an artifact that grants Damage, Strength, and Lifesteal and provides the Unholy Rage active. [gamefile:items/item_satanic#cost] [gamefile:items/item_satanic#attribs] [loc:DOTA_Tooltip_ability_item_satanic_Description]

## Stats

| Stat | Value |
|---|---:|
| Damage | 25 |
| Strength | 25 |
| Lifesteal | 30% |
| Unholy Duration | 6.0 |
| Unholy Lifesteal Percent | 145 |
| Unholy Lifesteal Total Tooltip | 175% |

[gamefile:items/item_satanic#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Reaver | 2800 gold |
| Claymore | 1350 gold |
| Morbid Mask | 900 gold |
| **Satanic** | **5050 gold** |

[gamefile:items/item_satanic#components] [gamefile:items/item_satanic#cost]

## Mechanics

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Dispellable | No |
| Cooldown | 30.0 |

[gamefile:items/item_satanic#mechanics]

Unholy Rage increases Lifesteal percentage and has Basic Dispel as its dispel type. [loc:DOTA_Tooltip_ability_item_satanic_Description]

The passive Lifesteal heals the attacker for a percentage of physical damage dealt. [loc:DOTA_Tooltip_ability_item_satanic_Description]

*Immense power at the cost of your soul.* [loc:DOTA_Tooltip_ability_item_satanic_Lore]