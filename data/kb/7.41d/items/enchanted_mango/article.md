---
title: Enchanted Mango
kind: item
patch: 7.41d
card:
  entity: enchanted_mango
  sentences:
  - text: Enchanted Mango is a consumable item costing 65 gold that provides 0.4 Health
      Regeneration and restores 100 mana instantly through Eat Mango.
    marks:
    - gamefile:items/item_enchanted_mango#cost
    - gamefile:items/item_enchanted_mango#attribs
    - loc:DOTA_Tooltip_ability_item_enchanted_mango_Description
  - text: Its build formula is Enchanted Mango (65 gold).
    marks:
    - gamefile:items/item_enchanted_mango#cost
  - text: Eat Mango is immediate and no-target.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: It permits optional unit targeting.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: Its cast range is 400.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: Using it does not resume attacks.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: Using it suppresses the associated consumable.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
---

# Enchanted Mango

Enchanted Mango is a consumable item that provides Health Regeneration and has a Replenish Amount that restores mana through Eat Mango. [gamefile:items/item_enchanted_mango#cost] [gamefile:items/item_enchanted_mango#attribs] [loc:DOTA_Tooltip_ability_item_enchanted_mango_Description]

## Stats

| Stat | Value |
|---|---:|
| Health Regeneration | 0.4 |
| Replenish Amount | 100 |

[gamefile:items/item_enchanted_mango#attribs]

## Use and mechanics

Eat Mango instantly restores mana. [loc:DOTA_Tooltip_ability_item_enchanted_mango_Description]

The use is immediate and no-target, permits optional unit targeting, does not resume attacks, and suppresses the associated consumable. [gamefile:items/item_enchanted_mango#mechanics]

| Stat | Value |
|---|---:|
| Cast range | 400 |

[gamefile:items/item_enchanted_mango#mechanics]

## Components

| Item | Gold cost |
|---|---:|
| Enchanted Mango | 65 gold |

[gamefile:items/item_enchanted_mango#cost]

*The bittersweet flavors of Jidi Isle are irresistible to amphibians.* [loc:DOTA_Tooltip_ability_item_enchanted_mango_Lore]