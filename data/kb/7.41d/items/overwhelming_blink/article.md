---
title: Overwhelming Blink
kind: item
patch: 7.41d
card:
  entity: overwhelming_blink
  sentences:
  - text: Overwhelming Blink is a component-quality item costing 6800 gold that grants
      25 Strength; its active teleports the user up to 1200 range, deals magical damage
      in an 800 radius, and applies 50% Movement Slow and 50 Attack Slow for 6 seconds.
    marks:
    - gamefile:items/item_overwhelming_blink#cost
    - gamefile:items/item_overwhelming_blink#attribs
    - gamefile:items/item_overwhelming_blink#mechanics
    - loc:DOTA_Tooltip_ability_item_overwhelming_blink_Description
  - text: The active has a 0 mana cost.
    marks:
    - gamefile:items/item_overwhelming_blink#mechanics
  - text: The active has a 15.0-second cooldown.
    marks:
    - gamefile:items/item_overwhelming_blink#mechanics
  - text: Blink Range Clamp is 960.
    marks:
    - gamefile:items/item_overwhelming_blink#attribs
  - text: After teleportation, immediate damage is 100 plus 50% of Strength.
    marks:
    - gamefile:items/item_overwhelming_blink#attribs
    - loc:DOTA_Tooltip_ability_item_overwhelming_blink_Description
  - text: Additional damage over time is 100% of Strength.
    marks:
    - gamefile:items/item_overwhelming_blink#attribs
    - loc:DOTA_Tooltip_ability_item_overwhelming_blink_Description
  - text: Damage from an enemy hero or Roshan prevents use for the 3.0-second Blink
      Damage Cooldown.
    marks:
    - gamefile:items/item_overwhelming_blink#attribs
    - loc:DOTA_Tooltip_ability_item_overwhelming_blink_Description
  - text: 'Build formula: Blink Dagger (2250 gold) + Reaver (2800 gold) + Recipe (1750
      gold).'
    marks:
    - gamefile:items/item_overwhelming_blink#components
---

# Overwhelming Blink

Overwhelming Blink is a component-quality item that grants Strength and provides the active Overwhelming Blink, which teleports the user, deals magical damage, and applies Movement Slow and Attack Slow. [gamefile:items/item_overwhelming_blink#cost] [gamefile:items/item_overwhelming_blink#attribs] [gamefile:items/item_overwhelming_blink#mechanics] [loc:DOTA_Tooltip_ability_item_overwhelming_blink_Description]

## Stats

| Stat | Value |
|---|---:|
| ATTACK SLOW | 50 |
| BLINK DAMAGE COOLDOWN | 3.0 |
| BLINK RANGE | 1200 |
| BLINK RANGE CLAMP | 960 |
| STRENGTH | 25 |
| DAMAGE BASE | 100 |
| DAMAGE PCT INSTANT | 50% |
| DAMAGE PCT OVER TIME | 100% |
| DURATION | 6 |
| MOVEMENT SLOW | 50% |
| RADIUS | 800 |

[gamefile:items/item_overwhelming_blink#attribs]

## Overwhelming Blink

| Property | Value |
|---|---|
| Behavior | Point Target, DOTA_ABILITY_BEHAVIOR_DIRECTIONAL, DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES, DOTA_ABILITY_BEHAVIOR_OVERSHOOT |
| Damage type | Magical |
| Cast range | 1200 |
| Mana cost | 0 |
| Cooldown | 15.0 |

[gamefile:items/item_overwhelming_blink#mechanics]

The active teleports the user to a target point. After teleportation, enemies in the area take immediate Strength-based damage and additional damage over time, while their movement speed and attack speed are slowed for the effect duration. It cannot be used during Blink Damage Cooldown after the user takes damage from an enemy hero or Roshan. [loc:DOTA_Tooltip_ability_item_overwhelming_blink_Description]

## Components

| Component | Gold cost |
|---|---:|
| Blink Dagger | 2250 gold |
| Reaver | 2800 gold |
| Recipe | 1750 gold |
| **Overwhelming Blink** | **6800 gold** |

[gamefile:items/item_overwhelming_blink#components] [gamefile:items/item_overwhelming_blink#cost]

*A horrifying dagger forged in the chaos maw and nigh untouchable by mortal hands.* [loc:DOTA_Tooltip_ability_item_overwhelming_blink_Lore]