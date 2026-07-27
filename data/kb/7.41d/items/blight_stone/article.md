---
title: Orb of Blight
kind: item
patch: 7.41d
card:
  entity: blight_stone
  sentences:
  - text: Orb of Blight is a 300-gold component whose passive Lesser Corruption applies
      -2 Corruption Armor for 3.0 seconds.
    marks:
    - gamefile:items/item_blight_stone#cost
    - gamefile:items/item_blight_stone#attribs
    - loc:DOTA_Tooltip_Ability_item_blight_stone_Description
  - text: It builds into Desolator, Medallion Of Courage, and Orb of Corrosion.
    marks:
    - gamefile:items/item_blight_stone#components
  - text: Attacks apply the armor reduction to their target.
    marks:
    - gamefile:items/item_blight_stone#mechanics
  - text: Lesser Corruption is dispellable.
    marks:
    - gamefile:items/item_blight_stone#mechanics
---

# Orb of Blight

Orb of Blight is a component whose Lesser Corruption passive applies Corruption Armor and Corruption Duration. [gamefile:items/item_blight_stone#cost] [gamefile:items/item_blight_stone#attribs] [loc:DOTA_Tooltip_Ability_item_blight_stone_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 300 gold |
| Corruption Armor | -2 |
| Corruption Duration | 3.0 |

[gamefile:items/item_blight_stone#cost] [gamefile:items/item_blight_stone#attribs]

## Components

| Builds into | Gold cost |
|---|---:|
| Desolator | 3500 gold |
| Medallion Of Courage | 0 gold |
| Orb of Corrosion | 1050 gold |

[gamefile:items/item_blight_stone#components]

## Mechanics

Attacks apply the armor reduction to their target. Lesser Corruption is passive and dispellable. [loc:DOTA_Tooltip_Ability_item_blight_stone_Description] [gamefile:items/item_blight_stone#mechanics]

*An unnerving stone unearthed beneath the Fields of Endless Carnage.* [loc:DOTA_Tooltip_Ability_item_blight_stone_Lore]