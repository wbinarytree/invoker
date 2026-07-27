---
title: Tome of Aghanim
kind: item
patch: 7.41d
card:
  entity: tome_of_aghanim
  sentences:
  - text: Tome of Aghanim is a 0-gold item whose Consume ability targets an allied
      unit and grants it the Aghanim's Scepter buff for 3 minutes.
    marks:
    - gamefile:items/item_tome_of_aghanim#cost
    - loc:DOTA_Tooltip_ability_item_tome_of_aghanim_Description
    - gamefile:items/item_tome_of_aghanim#attribs
  - text: Its build formula is Tome of Aghanim (0 gold).
    marks:
    - gamefile:items/item_tome_of_aghanim#cost
  - text: Its behavior is Unit Target, Immediate, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK,
      and DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE.
    marks:
    - gamefile:items/item_tome_of_aghanim#mechanics
  - text: Its cast range is 250.
    marks:
    - gamefile:items/item_tome_of_aghanim#mechanics
---

# Tome of Aghanim

Tome of Aghanim is an item that temporarily grants an allied target the Aghanim's Scepter buff. [gamefile:items/item_tome_of_aghanim#cost] [loc:DOTA_Tooltip_ability_item_tome_of_aghanim_Description]

## Stats

| Stat | Value |
|---|---:|
| Duration Minutes | 3 |

[gamefile:items/item_tome_of_aghanim#attribs]

| Property | Value |
|---|---|
| Behavior | Unit Target, Immediate, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK, DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE |
| Cast range | 250 |

[gamefile:items/item_tome_of_aghanim#mechanics]

## Components

| Item | Gold cost |
|---|---:|
| Tome of Aghanim | 0 |

[gamefile:items/item_tome_of_aghanim#cost]

## Use

**Consume** targets an allied unit and temporarily grants it the Aghanim's Scepter buff. [loc:DOTA_Tooltip_ability_item_tome_of_aghanim_Description]