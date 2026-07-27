---
title: Ring of Aquila
kind: item
patch: 7.41d
card:
  entity: ring_of_aquila
  sentences:
  - text: Ring of Aquila is an item that grants 9 Agility, 3 Damage, 3 Intelligence,
      and 3 Strength, while Aquila Aura grants nearby allies 2 Armor and 1 Mana Regeneration
      in a 1200 radius.
    marks:
    - gamefile:items/item_ring_of_aquila#attribs
    - loc:DOTA_Tooltip_ability_item_ring_of_aquila_Description
  - text: Its behavior is Immediate, No Target, Toggle.
    marks:
    - gamefile:items/item_ring_of_aquila#mechanics
  - text: Its cast range is 1200.
    marks:
    - gamefile:items/item_ring_of_aquila#mechanics
  - text: Aquila Aura is passive.
    marks:
    - loc:DOTA_Tooltip_ability_item_ring_of_aquila_Description
  - text: Deactivating Aquila Aura stops it from affecting non-hero units.
    marks:
    - loc:DOTA_Tooltip_ability_item_ring_of_aquila_Description
---

# Ring of Aquila

Ring of Aquila is an item that grants Agility, Damage, Intelligence, and Strength and provides Aquila Aura, which grants Armor and Mana Regeneration to nearby allies. [gamefile:items/item_ring_of_aquila#cost] [gamefile:items/item_ring_of_aquila#attribs] [loc:DOTA_Tooltip_ability_item_ring_of_aquila_Description]

## Stats

| Stat | Value |
|---|---:|
| Aura Bonus Armor | 2 |
| Aura Mana Regen | 1 |
| Aura Radius | 1200 |
| Agility | 9 |
| Damage | 3 |
| Intelligence | 3 |
| Strength | 3 |

[gamefile:items/item_ring_of_aquila#attribs]

## Mechanics

| Property | Value |
|---|---|
| Behavior | Immediate, No Target, Toggle |
| Cast range | 1200 |

[gamefile:items/item_ring_of_aquila#mechanics]

Aquila Aura is passive. Deactivating the aura stops it from affecting non-hero units. [loc:DOTA_Tooltip_ability_item_ring_of_aquila_Description]

*The ring of the fallen Warlord Aquila continues to support armies in battle.* [loc:DOTA_Tooltip_ability_item_ring_of_aquila_Lore]