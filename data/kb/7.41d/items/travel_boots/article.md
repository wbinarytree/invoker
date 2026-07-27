---
title: Boots of Travel
kind: item
patch: 7.41d
card:
  entity: travel_boots
  sentences:
  - text: Boots of Travel is a common item costing 2500 gold that provides 90 Movement
      Speed, 800 Maximum Distance, 40 TP Cooldown, and 200 Vision Radius, and upgrades
      Town Portal Scroll.
    marks:
    - gamefile:items/item_travel_boots#cost
    - gamefile:items/item_travel_boots#attribs
    - loc:DOTA_Tooltip_ability_item_travel_boots_Description
  - text: It is built from Boots of Speed (500 gold) and a Recipe (2000 gold), and
      builds into Boots of Travel 2.
    marks:
    - gamefile:items/item_travel_boots#components
  - text: Its behavior is Passive.
    marks:
    - gamefile:items/item_travel_boots#mechanics
  - text: The upgraded Town Portal Scroll can target units.
    marks:
    - loc:DOTA_Tooltip_ability_item_travel_boots_Description
  - text: The upgrade reduces Town Portal Scroll's cooldown.
    marks:
    - loc:DOTA_Tooltip_ability_item_travel_boots_Description
  - text: Using the upgraded Town Portal Scroll does not consume a charge.
    marks:
    - loc:DOTA_Tooltip_ability_item_travel_boots_Description
  - text: Movement Speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_ability_item_travel_boots_Description
---

# Boots of Travel

Boots of Travel is a common item that provides Movement Speed, Maximum Distance, TP Cooldown, and Vision Radius, and upgrades Town Portal Scroll. [gamefile:items/item_travel_boots#cost] [gamefile:items/item_travel_boots#attribs] [loc:DOTA_Tooltip_ability_item_travel_boots_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 2500 gold |

[gamefile:items/item_travel_boots#cost]

| Stat | Value |
|---|---:|
| Movement Speed | 90 |
| Maximum Distance | 800 |
| TP Cooldown | 40 |
| Vision Radius | 200 |

[gamefile:items/item_travel_boots#attribs]

## Components

| Type | Item | Gold cost |
|---|---|---:|
| Component | Boots of Speed | 500 gold |
| Recipe | Recipe | 2000 gold |
| Builds into | Boots of Travel 2 | 4500 gold |

[gamefile:items/item_travel_boots#components]

## Mechanics

Its behavior is Passive. [gamefile:items/item_travel_boots#mechanics]

It upgrades Town Portal Scroll, allowing it to target units, reducing its cooldown, and preventing charge consumption on use. Movement Speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_ability_item_travel_boots_Description]

*Winged boots that grant omnipresence.* [loc:DOTA_Tooltip_ability_item_travel_boots_Lore]