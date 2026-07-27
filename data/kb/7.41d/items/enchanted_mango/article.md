---
title: Enchanted Mango
kind: item
patch: 7.41d
card:
  entity: enchanted_mango
  sentences:
  - text: Enchanted Mango is a 65-gold consumable item that provides 0.4 Health Regeneration
      and instantly restores 100 mana through Eat Mango.
    marks:
    - gamefile:items/item_enchanted_mango#cost
    - gamefile:items/item_enchanted_mango#attribs
    - loc:DOTA_Tooltip_ability_item_enchanted_mango_Description
  - text: Eat Mango has 400 Cast range.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: The use is immediate.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: The use is no-target.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: Optional unit targeting is permitted.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: The use does not resume attacks.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: The use suppresses the associated consumable.
    marks:
    - gamefile:items/item_enchanted_mango#mechanics
  - text: 'Build formula: Enchanted Mango (65 gold).'
    marks:
    - gamefile:items/item_enchanted_mango#cost
  - text: The bittersweet flavors of Jidi Isle are irresistible to amphibians.
    marks:
    - loc:DOTA_Tooltip_ability_item_enchanted_mango_Lore
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