---
title: Ring of Basilius
kind: item
patch: 7.41d
card:
  entity: ring_of_basilius
  sentences:
  - text: Ring of Basilius is a rare 425-gold item that provides 0.25 Mana Regeneration
      and passively grants allies 1.0 Aura Mana Regen within a 1200 radius through
      Basilius Aura.
    marks:
    - gamefile:items/item_ring_of_basilius#cost
    - gamefile:items/item_ring_of_basilius#attribs
    - loc:DOTA_Tooltip_ability_item_ring_of_basilius_Description
  - text: It is built from Sage's Mask (175 gold) and a Recipe (250 gold).
    marks:
    - gamefile:items/item_ring_of_basilius#components
  - text: It builds into Arcane Boots and Vladmir's Offering.
    marks:
    - gamefile:items/item_ring_of_basilius#components
  - text: “Ring given as a reward to the greatest mages.”
    marks:
    - loc:DOTA_Tooltip_ability_item_ring_of_basilius_Lore
---

# Ring of Basilius

Ring of Basilius is a rare item that provides Mana Regeneration and grants Aura Mana Regen to allies through the passive Basilius Aura. [gamefile:items/item_ring_of_basilius#cost] [gamefile:items/item_ring_of_basilius#attribs] [loc:DOTA_Tooltip_ability_item_ring_of_basilius_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 425 gold |

[gamefile:items/item_ring_of_basilius#cost]

| Stat | Value |
|---|---:|
| Aura Mana Regen | 1.0 |
| Aura Radius | 1200 |
| Mana Regeneration | 0.25 |

[gamefile:items/item_ring_of_basilius#attribs]

| Property | Value |
|---|---:|
| Behavior | Passive |
| Cast range | 1200 |

[gamefile:items/item_ring_of_basilius#mechanics]

## Components

| Role | Item | Gold cost |
|---|---|---:|
| Component | Sage's Mask | 175 gold |
| Component | Recipe | 250 gold |
| Builds into | Arcane Boots | 1500 gold |
| Builds into | Vladmir's Offering | 2200 gold |

[gamefile:items/item_ring_of_basilius#components]

*Ring given as a reward to the greatest mages.* [loc:DOTA_Tooltip_ability_item_ring_of_basilius_Lore]