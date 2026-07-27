---
title: Martyr's Plate
kind: item
patch: 7.41d
card:
  entity: martyrs_plate
  sentences:
  - text: Martyr's Plate is a 0-gold item that provides 7 Health Regeneration and
      25% Magic Resistance, and its Martyrdom active redirects 25% of all magic damage
      dealt to allied heroes within a 900 Aura Radius toward the user for 10 seconds.
    marks:
    - gamefile:items/item_martyrs_plate#cost
    - gamefile:items/item_martyrs_plate#attribs
    - loc:DOTA_Tooltip_ability_item_martyrs_plate_Description
  - text: Martyrdom is immediate, requires no target, and has a 40-second Cooldown.
    marks:
    - gamefile:items/item_martyrs_plate#mechanics
  - text: The build formula is Martyr's Plate (0 gold).
    marks:
    - gamefile:items/item_martyrs_plate#cost
---

# Martyr's Plate

Martyr's Plate is an item that provides Health Regeneration and Magic Resistance and grants Martyrdom, an active with Aura Radius, Damage Redirection, and Duration. [gamefile:items/item_martyrs_plate#attribs] [loc:DOTA_Tooltip_ability_item_martyrs_plate_Description]

## Stats

| Stat | Value |
|---|---:|
| Aura Radius | 900 |
| Damage Redirection | 25% |
| Duration | 10 |
| Health Regeneration | 7 |
| Magic Resistance | 25% |

[gamefile:items/item_martyrs_plate#attribs]

## Martyrdom

Martyrdom is immediate and requires no target. [gamefile:items/item_martyrs_plate#mechanics]

It redirects a portion of all magic damage dealt to allied heroes within its radius toward the user for its duration. [loc:DOTA_Tooltip_ability_item_martyrs_plate_Description]

| Stat | Value |
|---|---:|
| Cooldown | 40 |

[gamefile:items/item_martyrs_plate#mechanics]

## Components

| Entry | Gold cost |
|---|---:|
| Martyr's Plate | 0 gold |

[gamefile:items/item_martyrs_plate#cost]