---
title: Fusion Rune
kind: item
patch: 7.41d
card:
  entity: fusion_rune
  sentences:
  - text: Fusion Rune is a 0-gold consumable item that targets a unit within 250 range
      and grants the bonuses of every Power Rune for 50 seconds, with a 120.0-second
      cooldown.
    marks:
    - gamefile:items/item_fusion_rune#cost
    - loc:DOTA_Tooltip_ability_item_fusion_rune_Description
    - gamefile:items/item_fusion_rune#attribs
    - gamefile:items/item_fusion_rune#mechanics
  - text: Its cast is Immediate and has DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK and
      DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE.
    marks:
    - gamefile:items/item_fusion_rune#mechanics
  - text: Each use consumes a charge.
    marks:
    - loc:DOTA_Tooltip_ability_item_fusion_rune_Description
---

# Fusion Rune

Fusion Rune is a consumable item that grants its target the bonuses of every Power Rune. [gamefile:items/item_fusion_rune#cost] [loc:DOTA_Tooltip_ability_item_fusion_rune_Description]

## Stats

| Stat | Value |
|---|---:|
| DURATION | 50 |

[gamefile:items/item_fusion_rune#attribs]

| Casting stat | Value |
|---|---|
| Behavior | Unit Target, Immediate, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK, DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE |
| Cast range | 250 |
| Cooldown | 120.0 |

[gamefile:items/item_fusion_rune#mechanics]

## Cost

| Item | Gold cost |
|---|---:|
| Fusion Rune | 0 |

[gamefile:items/item_fusion_rune#cost]

## Effect

Use: Consume. Each use consumes a charge. [loc:DOTA_Tooltip_ability_item_fusion_rune_Description]