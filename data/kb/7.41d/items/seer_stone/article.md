---
title: Seer Stone
kind: item
patch: 7.41d
card:
  entity: seer_stone
  sentences:
  - text: Seer Stone is a 0-gold item that provides 350 Cast Range, 10 Mana Regeneration,
      and 350 Vision Bonus and grants Reveal, an active ability that reveals an 800-radius
      area for 6 seconds.
    marks:
    - gamefile:items/item_seer_stone#cost
    - gamefile:items/item_seer_stone#attribs
    - loc:DOTA_Tooltip_ability_item_seer_stone_Description
  - text: Reveal has Point Target, AOE, Immediate behavior.
    marks:
    - gamefile:items/item_seer_stone#mechanics
  - text: Reveal has 0 cast range.
    marks:
    - gamefile:items/item_seer_stone#mechanics
  - text: Reveal has a 60-second cooldown.
    marks:
    - gamefile:items/item_seer_stone#mechanics
  - text: 'The build formula is Seer Stone cost: 0 gold.'
    marks:
    - gamefile:items/item_seer_stone#cost
  - text: The curious creation of a wizard who professed to hail from another time.
    marks:
    - loc:DOTA_Tooltip_ability_item_seer_stone_Lore
---

# Seer Stone

Seer Stone is an item that provides Cast Range, Mana Regeneration, and Vision Bonus and grants the active ability Reveal. [gamefile:items/item_seer_stone#attribs] [loc:DOTA_Tooltip_ability_item_seer_stone_Description]

## Stats

| Stat | Value |
|---|---:|
| Cast Range | 350 |
| Duration | 6 |
| Mana Regeneration | 10 |
| Radius | 800 |
| Vision Bonus | 350 |

[gamefile:items/item_seer_stone#attribs]

## Reveal

Reveal targets and reveals an area of the map. [loc:DOTA_Tooltip_ability_item_seer_stone_Description]

| Property | Value |
|---|---|
| Behavior | Point Target, AOE, Immediate |
| Cast range | 0 |
| Cooldown | 60 |

[gamefile:items/item_seer_stone#mechanics]

## Components

| Build formula | Gold cost |
|---|---:|
| Seer Stone cost | 0 gold |

[gamefile:items/item_seer_stone#cost]

*The curious creation of a wizard who professed to hail from another time.* [loc:DOTA_Tooltip_ability_item_seer_stone_Lore]