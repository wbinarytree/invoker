---
title: Cloak
kind: item
patch: 7.41d
card:
  entity: cloak
  sentences:
  - text: Cloak is a component item costing 900 gold that grants 18 bonus magical
      armor and 18% magic resistance.
    marks:
    - gamefile:items/item_cloak#cost
    - gamefile:items/item_cloak#attribs
  - text: Its build formula is Cloak (900 gold).
    marks:
    - gamefile:items/item_cloak#cost
  - text: It builds into Eternal Shroud, Mage Slayer, and Pipe of Insight.
    marks:
    - gamefile:items/item_cloak#components
  - text: Cloak has passive behavior.
    marks:
    - gamefile:items/item_cloak#mechanics
---

# Cloak

Cloak is a component item that grants bonus magical armor and magic resistance. [gamefile:items/item_cloak#cost] [gamefile:items/item_cloak#attribs]

## Stats

| Stat | Value |
|---|---:|
| Bonus Magical Armor | 18 |
| Magic Resistance | 18% |

[gamefile:items/item_cloak#attribs]

## Components

| Item | Gold cost |
|---|---:|
| Cloak | 900 gold |

[gamefile:items/item_cloak#cost]

| Builds into | Gold cost |
|---|---:|
| Eternal Shroud | 3900 gold |
| Mage Slayer | 3100 gold |
| Pipe of Insight | 3725 gold |

[gamefile:items/item_cloak#components]

## Mechanics

Cloak has passive behavior. [gamefile:items/item_cloak#mechanics]

*A cloak made of a magical material that works to dispel any magic cast on it.* [loc:DOTA_Tooltip_ability_item_cloak_Lore]