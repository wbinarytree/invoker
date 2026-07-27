---
title: Consecrated Wraps
kind: item
patch: 7.41d
card:
  entity: consecrated_wraps
  sentences:
  - text: Consecrated Wraps is a 2600-gold epic item granting 5 All Attributes, 250
      Health, and 12% Magic Resistance; its Hallowed passive periodically gains charges
      and consumes them after damage from a player-controlled unit or Roshan to grant
      a scaling all damage barrier with 120 Barrier per Stack and a 360 Max Barrier
      Tooltip.
    marks:
    - gamefile:items/item_consecrated_wraps#cost
    - gamefile:items/item_consecrated_wraps#attribs
    - loc:DOTA_Tooltip_ability_item_consecrated_wraps_Description
  - text: Whenever Hallowed gains a charge, movement speed increases by 15%.
    marks:
    - gamefile:items/item_consecrated_wraps#attribs
    - loc:DOTA_Tooltip_ability_item_consecrated_wraps_Description
  - text: Hallowed's Duration is 5.
    marks:
    - gamefile:items/item_consecrated_wraps#attribs
  - text: Its Stack Threshold Damage is 0.
    marks:
    - gamefile:items/item_consecrated_wraps#attribs
  - text: Hallowed is dispellable.
    marks:
    - gamefile:items/item_consecrated_wraps#mechanics
  - text: Hallowed has a cooldown of 0.
    marks:
    - gamefile:items/item_consecrated_wraps#mechanics
  - text: It is built from Vitality Booster (1000 gold), Shawl (450 gold), Crown (450
      gold), and a Recipe (700 gold).
    marks:
    - gamefile:items/item_consecrated_wraps#components
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