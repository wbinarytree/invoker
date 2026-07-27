---
title: Eye of Skadi
kind: item
patch: 7.41d
card:
  entity: skadi
  sentences:
  - text: Eye of Skadi is a 5900-gold artifact granting 35 All Attributes; its passive
      Cold Attack lasts 3.0 seconds, applies movement-speed modifiers of -25% to melee
      enemies and -50% to ranged enemies, applies attack-speed modifiers of -20% to
      melee enemies and -20 to ranged enemies, and reduces Health Restoration by 50%.
    marks:
    - gamefile:items/item_skadi#cost
    - gamefile:items/item_skadi#attribs
    - gamefile:items/item_skadi#mechanics
    - loc:DOTA_Tooltip_ability_item_skadi_Description
  - text: Attacks apply Cold Attack.
    marks:
    - loc:DOTA_Tooltip_ability_item_skadi_Description
  - text: It is built from Ultimate Orb (2800 gold), Ultimate Orb (2800 gold), and
      Orb of Frost (300 gold).
    marks:
    - gamefile:items/item_skadi#components
---

# Eye of Skadi

Eye of Skadi is an artifact that grants All Attributes and has the passive Cold Attack effect, which lowers enemy movement speed, attack speed, and Health Restoration. [gamefile:items/item_skadi#cost] [gamefile:items/item_skadi#attribs] [loc:DOTA_Tooltip_ability_item_skadi_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 5900 gold |

[gamefile:items/item_skadi#cost]

| Stat | Value |
|---|---:|
| ALL ATTRIBUTES | 35 |
| HEALTH | 0 |
| MANA | 0 |
| COLD ATTACK SLOW MELEE | -20% |
| COLD ATTACK SLOW RANGED | -20 |
| COLD DURATION | 3.0 |
| COLD SLOW MELEE | -25% |
| COLD SLOW RANGED | -50% |
| RESTORATION REDUCTION | 50% |

[gamefile:items/item_skadi#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Ultimate Orb | 2800 gold |
| Ultimate Orb | 2800 gold |
| Orb of Frost | 300 gold |

[gamefile:items/item_skadi#components]

## Mechanics

Eye of Skadi has passive behavior. [gamefile:items/item_skadi#mechanics]

Attacks apply Cold Attack. Its movement-speed reduction depends on whether the enemy is melee or ranged, and it also lowers the enemy’s attack speed and Health Restoration. [loc:DOTA_Tooltip_ability_item_skadi_Description]

*Extremely rare artifact, guarded by the azure dragons.* [loc:DOTA_Tooltip_ability_item_skadi_Lore]