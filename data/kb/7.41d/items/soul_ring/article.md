---
title: Soul Ring
kind: item
patch: 7.41d
card:
  entity: soul_ring
  sentences:
  - text: Soul Ring is a common 805-gold item that grants 2 Armor and 6 Strength;
      its active ability, Sacrifice, consumes health to grant 170 mana for 10 seconds.
    marks:
    - gamefile:items/item_soul_ring#cost
    - gamefile:items/item_soul_ring#attribs
    - loc:DOTA_Tooltip_ability_item_soul_ring_Description
  - text: Its build formula is Ring of Protection (175 gold) + Gauntlets of Strength
      (140 gold) + Gauntlets of Strength (140 gold) + Recipe (350 gold).
    marks:
    - gamefile:items/item_soul_ring#components
  - text: Sacrifice has No Target, Immediate behavior.
    marks:
    - gamefile:items/item_soul_ring#mechanics
  - text: Sacrifice has a 30.0 cooldown.
    marks:
    - gamefile:items/item_soul_ring#mechanics
  - text: Mana that cannot fit in the mana pool creates a buffer that is used before
      the mana pool.
    marks:
    - loc:DOTA_Tooltip_ability_item_soul_ring_Description
  - text: A ring that feeds on the souls of those who wear it.
    marks:
    - loc:DOTA_Tooltip_ability_item_soul_ring_Lore
---

# Soul Ring

Soul Ring is a common item [gamefile:items/item_soul_ring#cost] that grants Armor and Strength [gamefile:items/item_soul_ring#attribs] and provides Sacrifice, an active ability that consumes health to temporarily gain mana. [loc:DOTA_Tooltip_ability_item_soul_ring_Description]

## Statistics

| Stat | Value |
|---|---:|
| Armor | 2 |
| Strength | 6 |
| Duration | 10 |
| Mana Gain | 170 |

[gamefile:items/item_soul_ring#attribs]

## Components

| Component | Cost |
|---|---:|
| Ring of Protection | 175 gold |
| Gauntlets of Strength | 140 gold |
| Gauntlets of Strength | 140 gold |
| Recipe | 350 gold |
| **Soul Ring** | **805 gold** |

[gamefile:items/item_soul_ring#components] [gamefile:items/item_soul_ring#cost]

## Sacrifice

| Property | Value |
|---|---|
| Behavior | No Target, Immediate |
| Cooldown | 30.0 |

[gamefile:items/item_soul_ring#mechanics]

Mana that cannot fit in the mana pool creates a buffer that is used before the mana pool. [loc:DOTA_Tooltip_ability_item_soul_ring_Description]

*A ring that feeds on the souls of those who wear it.* [loc:DOTA_Tooltip_ability_item_soul_ring_Lore]