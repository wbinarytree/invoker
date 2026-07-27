---
title: Town Portal Scroll
kind: item
patch: 7.41d
card:
  entity: tpscroll
  sentences:
  - text: Town Portal Scroll is a consumable item costing 100 gold that provides Teleport,
      a Point Target, Channelled ability with a Tooltip Channel Time of 3.0, 75 mana
      cost, and 80.0 cooldown that teleports the user to a target friendly building.
    marks:
    - gamefile:items/item_tpscroll#cost
    - loc:DOTA_Tooltip_ability_item_tpscroll_Description
    - gamefile:items/item_tpscroll#attribs
    - gamefile:items/item_tpscroll#mechanics
  - text: Teleport has a Maximum Distance of 800.
    marks:
    - gamefile:items/item_tpscroll#attribs
  - text: Teleport has a Minimum Distance of 70.
    marks:
    - gamefile:items/item_tpscroll#attribs
  - text: Its Vision Radius is 200.
    marks:
    - gamefile:items/item_tpscroll#attribs
  - text: Its Cast range is 0.
    marks:
    - gamefile:items/item_tpscroll#mechanics
  - text: Double-clicking Teleport sends the user to their team’s base fountain.
    marks:
    - loc:DOTA_Tooltip_ability_item_tpscroll_Description
---

# Town Portal Scroll

Town Portal Scroll is a consumable item that provides Teleport, a Point Target, Channelled ability. [gamefile:items/item_tpscroll#cost] [loc:DOTA_Tooltip_ability_item_tpscroll_Description] [gamefile:items/item_tpscroll#mechanics]

## Cost

| Item | Gold cost |
|---|---:|
| Town Portal Scroll | 100 |

[gamefile:items/item_tpscroll#cost]

## Stats

| Stat | Value |
|---|---|
| Maximum Distance | 800 |
| Minimum Distance | 70 |
| Tooltip Channel Time | 3.0 |
| Vision Radius | 200 |

[gamefile:items/item_tpscroll#attribs]

| Stat | Value |
|---|---|
| Behavior | Point Target, Channelled, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK, DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_CHANNEL, DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES |
| Cast range | 0 |
| Mana cost | 75 |
| Cooldown | 80.0 |

[gamefile:items/item_tpscroll#mechanics]

## Teleport

After channeling, Teleport teleports the user to a target friendly building. Double-clicking teleports the user to their team’s base fountain. [loc:DOTA_Tooltip_ability_item_tpscroll_Description]

*What a hero truly needs.* [loc:DOTA_Tooltip_ability_item_tpscroll_Lore]