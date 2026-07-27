---
title: Clarity
kind: item
patch: 7.41d
card:
  entity: clarity
  sentences:
  - text: Clarity is a consumable item costing 60 gold whose Replenish use grants
      a target within 250 cast range 6 Mana Regen for a Buff Duration of 25.
    marks:
    - gamefile:items/item_clarity#cost
    - gamefile:items/item_clarity#attribs
    - gamefile:items/item_clarity#mechanics
    - loc:DOTA_Tooltip_ability_item_clarity_Description
  - text: The effect is lost if an enemy hero or Roshan attacks the affected unit.
    marks:
    - loc:DOTA_Tooltip_ability_item_clarity_Description
  - text: The effect is dispellable.
    marks:
    - gamefile:items/item_clarity#mechanics
  - text: “Clear water that enhances the ability to meditate.”
    marks:
    - loc:DOTA_Tooltip_ability_item_clarity_Lore
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