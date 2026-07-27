---
title: Infused Raindrops
kind: item
patch: 7.41d
card:
  entity: infused_raindrop
  sentences:
  - text: Infused Raindrops is a 225-gold component item that starts with 6 charges,
      provides 0.8 mana regeneration, and blocks 120 magic damage from an instance
      above the 75-damage threshold.
    marks:
    - gamefile:items/item_infused_raindrop#cost
    - gamefile:items/item_infused_raindrop#attribs
    - loc:DOTA_Tooltip_ability_item_infused_raindrop_Description
  - text: Its behavior is passive.
    marks:
    - gamefile:items/item_infused_raindrop#mechanics
  - text: The effect has a 7.0-second cooldown.
    marks:
    - gamefile:items/item_infused_raindrop#mechanics
  - text: Each qualifying block consumes a charge.
    marks:
    - loc:DOTA_Tooltip_ability_item_infused_raindrop_Description
  - text: The item disappears when all charges are gone.
    marks:
    - loc:DOTA_Tooltip_ability_item_infused_raindrop_Description
  - text: “Elemental protection from magical assaults.”
    marks:
    - loc:DOTA_Tooltip_ability_item_infused_raindrop_Lore
---

# Infused Raindrops

Infused Raindrops is a component item that provides Magic Damage Block and Mana Regeneration. [gamefile:items/item_infused_raindrop#cost] [gamefile:items/item_infused_raindrop#attribs]

## Cost

| Item | Gold cost |
|---|---:|
| Infused Raindrops | 225 |

[gamefile:items/item_infused_raindrop#cost]

## Stats

| Stat | Value |
|---|---:|
| Initial Charges | 6 |
| Magic Damage Block | 120 |
| Mana Regeneration | 0.8 |
| Min Damage | 75 |

[gamefile:items/item_infused_raindrop#attribs]

| Property | Value |
|---|---:|
| Behavior | Passive |
| Cooldown | 7.0 |

[gamefile:items/item_infused_raindrop#mechanics]

## Mechanics

Magical Damage Block consumes a charge to block magic damage from an instance above the minimum-damage threshold. The item disappears when all charges are gone. [loc:DOTA_Tooltip_ability_item_infused_raindrop_Description]

*Elemental protection from magical assaults.* [loc:DOTA_Tooltip_ability_item_infused_raindrop_Lore]