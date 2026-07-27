---
title: Silver Edge
kind: item
patch: 7.41d
card:
  entity: silver_edge
  sentences:
  - text: Silver Edge is an epic item costing 5700 gold that grants 35 Attack Speed
      and 70 Damage; Shadow Walk costs 75 mana, has a 22.0 cooldown, and gives invisibility
      with Windwalk Duration 17.0 and Windwalk Movement Speed 22%, while an attack
      ending it deals 300 bonus physical damage, disables passive abilities for Backstab
      Duration 5, and caps movement speed at 200.
    marks:
    - gamefile:items/item_silver_edge#cost
    - gamefile:items/item_silver_edge#attribs
    - gamefile:items/item_silver_edge#mechanics
    - loc:DOTA_Tooltip_ability_item_silver_edge_Description
  - text: Its build formula is Shadow Blade (3250 gold), Demon Edge (2200 gold), and
      Recipe (250 gold), with a total cost of 5700 gold.
    marks:
    - gamefile:items/item_silver_edge#components
    - gamefile:items/item_silver_edge#cost
  - text: Shadow Walk is Immediate, No Target, and Usable While Channelling.
    marks:
    - gamefile:items/item_silver_edge#mechanics
  - text: Its Windwalk Fade Time is 0.3.
    marks:
    - gamefile:items/item_silver_edge#attribs
  - text: Its Visibility Radius is 1025.
    marks:
    - gamefile:items/item_silver_edge#attribs
  - text: Shadow Walk’s invisibility ends when its duration expires or the user attacks
      or casts a spell.
    marks:
    - loc:DOTA_Tooltip_ability_item_silver_edge_Description
  - text: While invisible, the user moves faster and can move through units.
    marks:
    - loc:DOTA_Tooltip_ability_item_silver_edge_Description
  - text: Once used to slay an unjust king, only to have the kingdom erupt into civil
      war in the aftermath.
    marks:
    - loc:DOTA_Tooltip_ability_item_silver_edge_Lore
---

# Silver Edge

Silver Edge is an epic item that provides Attack Speed and Damage and has the active ability Shadow Walk. [gamefile:items/item_silver_edge#cost] [gamefile:items/item_silver_edge#attribs] [loc:DOTA_Tooltip_ability_item_silver_edge_Description]

## Components

| Component | Gold cost |
|---|---:|
| Shadow Blade | 3250 gold |
| Demon Edge | 2200 gold |
| Recipe | 250 gold |
| **Total cost** | **5700 gold** |

[gamefile:items/item_silver_edge#components] [gamefile:items/item_silver_edge#cost]

## Stats

| Stat | Value |
|---|---:|
| Backstab Duration | 5 |
| Attack Speed | 35 |
| Damage | 70 |
| Bonus Intellect | 0 |
| Bonus Mana Regen | 0 |
| Bonus Strength | 0 |
| Max Movement Speed | 200 |
| Visibility Radius | 1025 |
| Windwalk Bonus Damage | 300 |
| Windwalk Duration | 17.0 |
| Windwalk Fade Time | 0.3 |
| Windwalk Movement Speed | 22% |

[gamefile:items/item_silver_edge#attribs]

## Shadow Walk

| Property | Value |
|---|---|
| Behavior | Immediate, No Target, Usable While Channelling |
| Mana cost | 75 |
| Cooldown | 22.0 |

[gamefile:items/item_silver_edge#mechanics]

Shadow Walk makes the user invisible until its duration ends or the user attacks or casts a spell. While invisible, the user moves faster and can move through units. An attack that ends the invisibility deals bonus physical damage, disables the target’s passive abilities, and caps the target’s movement speed. [loc:DOTA_Tooltip_ability_item_silver_edge_Description]

*Once used to slay an unjust king, only to have the kingdom erupt into civil war in the aftermath.* [loc:DOTA_Tooltip_ability_item_silver_edge_Lore]