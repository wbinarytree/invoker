---
title: Book of Shadows
kind: item
patch: 7.41d
card:
  entity: book_of_shadows
  sentences:
  - text: Book of Shadows is a 0-gold item with 0 Bonus All Stats and 400 Night Vision
      whose Shadows active applies a Basic Dispel and makes the target untargetable
      by the caster's enemies, silenced, muted, and disarmed for 4 seconds; Shadows
      has 700 cast range and an 8.0-second cooldown.
    marks:
    - gamefile:items/item_book_of_shadows#cost
    - gamefile:items/item_book_of_shadows#attribs
    - gamefile:items/item_book_of_shadows#mechanics
    - loc:DOTA_Tooltip_ability_item_book_of_shadows_Description
  - text: Shadows has Unit Target behavior.
    marks:
    - gamefile:items/item_book_of_shadows#mechanics
  - text: Shadows can target an enemy, an ally, or the caster.
    marks:
    - loc:DOTA_Tooltip_ability_item_book_of_shadows_Description
---

# Book of Shadows

Book of Shadows is an item with Bonus All Stats and Night Vision whose Shadows active applies a Basic Dispel and inflicts silence, mute, disarm, and enemy untargetability. [gamefile:items/item_book_of_shadows#attribs] [loc:DOTA_Tooltip_ability_item_book_of_shadows_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Book of Shadows | 0 |

[gamefile:items/item_book_of_shadows#cost]

## Stats

| Stat | Value |
|---|---:|
| Bonus All Stats | 0 |
| Duration | 4 |
| Night Vision | 400 |

[gamefile:items/item_book_of_shadows#attribs]

## Shadows

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Cast range | 700 |
| Cooldown | 8.0 |

[gamefile:items/item_book_of_shadows#mechanics]

Shadows can target an enemy, ally, or the caster. The target becomes untargetable by enemies of the caster while silenced, muted, and disarmed. Its Dispel Type is Basic Dispel. [loc:DOTA_Tooltip_ability_item_book_of_shadows_Description]

*An impossible tome filled with unreadable prose of unknowable thoughts.* [loc:DOTA_Tooltip_ability_item_book_of_shadows_Lore]