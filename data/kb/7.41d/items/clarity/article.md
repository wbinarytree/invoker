---
title: Clarity
kind: item
patch: 7.41d
card:
  entity: clarity
  sentences:
  - text: Clarity is a 60-gold consumable that targets a unit within 250 cast range
      and grants 6 Mana Regen for 25 seconds.
    marks:
    - gamefile:items/item_clarity#cost
    - gamefile:items/item_clarity#attribs
    - gamefile:items/item_clarity#mechanics
  - text: Replenish ends if the affected unit is attacked by an enemy hero or Roshan.
    marks:
    - loc:DOTA_Tooltip_ability_item_clarity_Description
  - text: The effect is dispellable.
    marks:
    - gamefile:items/item_clarity#mechanics
---

# Clarity

Clarity is a consumable item that grants Mana Regen. [gamefile:items/item_clarity#cost] [gamefile:items/item_clarity#attribs]

## Stats

| Stat | Value |
|---|---:|
| Cost | 60 gold |
| Buff Duration | 25 |
| Mana Regen | 6 |
| Cast Range | 250 |

[gamefile:items/item_clarity#cost] [gamefile:items/item_clarity#attribs] [gamefile:items/item_clarity#mechanics]

## Mechanics

Its use, Replenish, applies Mana Regen to the target for the Buff Duration. If the affected unit is attacked by an enemy hero or Roshan, the effect is lost. [loc:DOTA_Tooltip_ability_item_clarity_Description]

Its behavior is Unit Target, Immediate, `DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK`, and `DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE`. The effect is dispellable. [gamefile:items/item_clarity#mechanics]

*Clear water that enhances the ability to meditate.* [loc:DOTA_Tooltip_ability_item_clarity_Lore]