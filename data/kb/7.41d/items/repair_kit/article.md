---
title: Repair Kit
kind: item
patch: 7.41d
card:
  entity: repair_kit
  sentences:
  - text: Repair Kit is a 0-gold consumable whose Building Repair targets a building
      within 600 range, restores 40% health over a Duration of 30, grants 10 Armor
      Bonus for the same period, provides 25 Health Regeneration, and has a 60.0 cooldown.
    marks:
    - gamefile:items/item_repair_kit#cost
    - gamefile:items/item_repair_kit#attribs
    - loc:DOTA_Tooltip_ability_item_repair_kit_Description
    - gamefile:items/item_repair_kit#mechanics
  - text: Building Repair's Behavior is Unit Target, Immediate, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK,
      and DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE.
    marks:
    - gamefile:items/item_repair_kit#mechanics
---

# Repair Kit

Repair Kit is a consumable item with Armor Bonus, Duration, Heal Percent, and Health Regeneration. [gamefile:items/item_repair_kit#cost] [gamefile:items/item_repair_kit#attribs]

## Cost

| Item | Cost |
|---|---:|
| Repair Kit | 0 gold |

[gamefile:items/item_repair_kit#cost]

## Stats

| Stat | Value |
|---|---:|
| Armor Bonus | 10 |
| Duration | 30 |
| Heal Percent | 40% |
| Health Regeneration | 25 |

[gamefile:items/item_repair_kit#attribs]

## Building Repair

Building Repair targets a building, restores part of its health over time, and grants armor for the same period. [loc:DOTA_Tooltip_ability_item_repair_kit_Description]

| Property | Value |
|---|---|
| Behavior | Unit Target, Immediate, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK, DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE |
| Cast range | 600 |
| Cooldown | 60.0 |

[gamefile:items/item_repair_kit#mechanics]