---
title: Healing Salve
kind: item
patch: 7.41d
card:
  entity: flask
  sentences:
  - text: Healing Salve is an item of consumable quality costing 100 gold that grants
      30 Health Regen for 13 seconds, with BREAK ON HERO DAMAGE set to 1.
    marks:
    - gamefile:items/item_flask#cost
    - gamefile:items/item_flask#attribs
  - text: It has 250 cast range.
    marks:
    - gamefile:items/item_flask#mechanics
  - text: It is dispellable.
    marks:
    - gamefile:items/item_flask#mechanics
  - text: Its behavior is Unit Target, Immediate, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK,
      and DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE.
    marks:
    - gamefile:items/item_flask#mechanics
  - text: The effect is lost if the target is attacked by an enemy hero or Roshan.
    marks:
    - loc:DOTA_Tooltip_ability_item_flask_Description
  - text: When cast on an ally, it heals for half the amount per second.
    marks:
    - loc:DOTA_Tooltip_ability_item_flask_Description
---

# Healing Salve

Healing Salve is an item of consumable quality that grants Health Regen. [gamefile:items/item_flask#cost] [gamefile:items/item_flask#attribs]

## Cost

| Item | Cost |
|---|---:|
| Healing Salve | 100 gold |

[gamefile:items/item_flask#cost]

## Stats

| Attribute | Value |
|---|---:|
| BREAK ON HERO DAMAGE | 1 |
| BUFF DURATION | 13 |
| HEALTH REGEN | 30 |

[gamefile:items/item_flask#attribs]

## Mechanics

| Property | Value |
|---|---|
| Behavior | Unit Target, Immediate, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK, DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE |
| Dispellable | Yes |
| Cast range | 250 |

[gamefile:items/item_flask#mechanics]

The effect is lost if the target is attacked by an enemy hero or Roshan. When cast on an ally, it heals for half the amount per second. [loc:DOTA_Tooltip_ability_item_flask_Description]

*A magical salve that can quickly mend even the deepest of wounds.* [loc:DOTA_Tooltip_ability_item_flask_Lore]