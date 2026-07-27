---
title: Refresher Orb
kind: item
patch: 7.41d
card:
  entity: refresher
  sentences:
  - text: Refresher Orb is a rare 5000-gold item that grants 14 Health Regeneration
      and 7.0 Mana Regeneration; its Reset Cooldowns active costs 325 mana, has a
      180 cooldown, and resets the cooldowns of all your abilities.
    marks:
    - gamefile:items/item_refresher#cost
    - gamefile:items/item_refresher#attribs
    - loc:DOTA_Tooltip_ability_item_refresher_Description
  - text: It is built from Ring of Tarrasque (1700 gold), Tiara of Selemene (1700
      gold), and a Recipe (1600 gold).
    marks:
    - gamefile:items/item_refresher#components
  - text: Reset Cooldowns is a No Target active with DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL
      behavior.
    marks:
    - gamefile:items/item_refresher#mechanics
  - text: Reset Cooldowns shares a cooldown with Refresher Shard.
    marks:
    - loc:DOTA_Tooltip_ability_item_refresher_Description
  - text: Its cooldown progresses only while Refresher Orb is in the hero’s main inventory.
    marks:
    - loc:DOTA_Tooltip_ability_item_refresher_Description
  - text: A powerful artifact created for wizards.
    marks:
    - loc:DOTA_Tooltip_ability_item_refresher_Lore
---

# Refresher Orb

Refresher Orb is a rare item that grants Health Regeneration and Mana Regeneration and provides the active ability Reset Cooldowns. [gamefile:items/item_refresher#cost] [gamefile:items/item_refresher#attribs] [loc:DOTA_Tooltip_ability_item_refresher_Description]

## Attributes

| Stat | Value |
|---|---:|
| DAMAGE | 0 |
| HEALTH REGENERATION | 14 |
| MANA REGENERATION | 7.0 |
| COOLDOWN DURATION / Cooldown | 180 |
| MAX LEVEL | 1 |
| REFRESH ITEMS | 0 |
| Mana cost | 325 |

[gamefile:items/item_refresher#attribs] [gamefile:items/item_refresher#mechanics]

## Components

| Entry | Gold cost |
|---|---:|
| Ring of Tarrasque | 1700 gold |
| Tiara of Selemene | 1700 gold |
| Recipe | 1600 gold |
| Refresher Orb | 5000 gold |

[gamefile:items/item_refresher#components] [gamefile:items/item_refresher#cost]

## Mechanics

Reset Cooldowns is a No Target active with `DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL` behavior. [gamefile:items/item_refresher#mechanics]

It resets the cooldowns of all your abilities and shares a cooldown with Refresher Shard. Its cooldown progresses only while it is in the hero’s main inventory. [loc:DOTA_Tooltip_ability_item_refresher_Description]

*A powerful artifact created for wizards.* [loc:DOTA_Tooltip_ability_item_refresher_Lore]