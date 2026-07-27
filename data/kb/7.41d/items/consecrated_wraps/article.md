---
title: Consecrated Wraps
kind: item
patch: 7.41d
card:
  entity: consecrated_wraps
  sentences:
  - text: Consecrated Wraps is an epic 2600-gold item granting 5 All Attributes, 250
      Health, and 12% Magic Resistance; its passive Hallowed periodically gains charges,
      increases movement speed by 15% when a charge is gained, and converts consumed
      charges into an all damage barrier with 120 capacity per stack, Duration 5,
      and Max Barrier Tooltip 360.
    marks:
    - gamefile:items/item_consecrated_wraps#cost
    - gamefile:items/item_consecrated_wraps#attribs
    - loc:DOTA_Tooltip_ability_item_consecrated_wraps_Description
  - text: It is built from Vitality Booster (1000 gold), Shawl (450 gold), Crown (450
      gold), and Recipe (700 gold).
    marks:
    - gamefile:items/item_consecrated_wraps#components
  - text: Taking damage from a player-controlled unit or Roshan consumes all Hallowed
      charges.
    marks:
    - loc:DOTA_Tooltip_ability_item_consecrated_wraps_Description
  - text: The barrier capacity scales with the charges consumed.
    marks:
    - loc:DOTA_Tooltip_ability_item_consecrated_wraps_Description
  - text: Hallowed is passive.
    marks:
    - gamefile:items/item_consecrated_wraps#mechanics
  - text: Hallowed is dispellable.
    marks:
    - gamefile:items/item_consecrated_wraps#mechanics
  - text: Hallowed has a cooldown of 0.
    marks:
    - gamefile:items/item_consecrated_wraps#mechanics
---

# Consecrated Wraps

Consecrated Wraps is an epic item that provides All Attributes, Health, Magic Resistance, and the passive Hallowed. [gamefile:items/item_consecrated_wraps#cost] [gamefile:items/item_consecrated_wraps#attribs] [loc:DOTA_Tooltip_ability_item_consecrated_wraps_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 2600 gold |

[gamefile:items/item_consecrated_wraps#cost]

| Stat | Value |
|---|---:|
| Barrier per Stack | 120 |
| All Attributes | 5 |
| Health | 250 |
| Magic Resistance | 12% |
| Duration | 5 |
| Max Barrier Tooltip | 360 |
| Movement Speed Pct on Stack Gain | 15% |
| Stack Threshold Damage | 0 |

[gamefile:items/item_consecrated_wraps#attribs]

| Property | Value |
|---|---|
| Behavior | Passive |
| Dispellable | Yes |
| Cooldown | 0 |

[gamefile:items/item_consecrated_wraps#mechanics]

## Components

| Component | Cost |
|---|---:|
| Vitality Booster | 1000 gold |
| Shawl | 450 gold |
| Crown | 450 gold |
| Recipe | 700 gold |

[gamefile:items/item_consecrated_wraps#components]

## Hallowed

Hallowed periodically gains charges up to a maximum and increases movement speed whenever a charge is gained. Taking damage from a player-controlled unit or Roshan consumes all charges and grants an all damage barrier whose capacity scales with the charges consumed. [loc:DOTA_Tooltip_ability_item_consecrated_wraps_Description]