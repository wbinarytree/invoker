---
title: Black King Bar
kind: item
patch: 7.41d
card:
  entity: black_king_bar
  sentences:
  - text: Black King Bar is an epic 4050-gold item that grants 24 damage and 10 strength;
      Avatar lasts 9/8/7 seconds, applies a Basic Dispel, grants 60% magic resistance
      and immunity to reflected and pure damage, and makes negative effects from enemy
      spells have no effect.
    marks:
    - gamefile:items/item_black_king_bar#cost
    - gamefile:items/item_black_king_bar#attribs
    - loc:DOTA_Tooltip_ability_item_black_king_bar_Description
  - text: Its build formula is Mithril Hammer (1600 gold), Ogre Axe (1000 gold), and
      Recipe (1450 gold).
    marks:
    - gamefile:items/item_black_king_bar#components
    - gamefile:items/item_black_king_bar#cost
  - text: Avatar has Immediate, No Target behavior.
    marks:
    - gamefile:items/item_black_king_bar#mechanics
  - text: Activation costs 50 mana.
    marks:
    - gamefile:items/item_black_king_bar#mechanics
  - text: Its cooldown is 95.
    marks:
    - gamefile:items/item_black_king_bar#mechanics
  - text: A powerful staff imbued with the strength of giants.
    marks:
    - loc:DOTA_Tooltip_ability_item_black_king_bar_Lore
---

# Black King Bar

Black King Bar is an epic item that grants Damage and Strength and provides Avatar, an active that applies a Basic Dispel, grants Magic Resistance and immunity to reflected and pure damage, and makes negative effects from enemy spells have no effect for its duration. [gamefile:items/item_black_king_bar#cost] [gamefile:items/item_black_king_bar#attribs] [loc:DOTA_Tooltip_ability_item_black_king_bar_Description]

## Build formula

| Component | Gold cost |
|---|---:|
| Mithril Hammer | 1600 gold |
| Ogre Axe | 1000 gold |
| Recipe | 1450 gold |
| **Black King Bar** | **4050 gold** |

[gamefile:items/item_black_king_bar#components] [gamefile:items/item_black_king_bar#cost]

## Stats

| Stat | Value |
|---|---:|
| DAMAGE | 24 |
| STRENGTH | 10 |
| DURATION / Avatar duration (s) | 9/8/7 |
| MAX LEVEL | 3 |
| MODEL SCALE | 30 |
| SPELL REDUCE / Avatar magic resistance | 60% |

[gamefile:items/item_black_king_bar#attribs] [loc:DOTA_Tooltip_ability_item_black_king_bar_Description]

## Activation

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Mana cost | 50 |
| Cooldown | 95 |

[gamefile:items/item_black_king_bar#mechanics]

Avatar’s dispel type is Basic Dispel. [loc:DOTA_Tooltip_ability_item_black_king_bar_Description]

*A powerful staff imbued with the strength of giants.* [loc:DOTA_Tooltip_ability_item_black_king_bar_Lore]