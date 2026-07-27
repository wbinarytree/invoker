---
title: Arcane Ring
kind: item
patch: 7.41d
card:
  entity: arcane_ring
  sentences:
  - text: Arcane Ring is a 0-gold item that grants 0 bonus armor and 0 bonus intelligence;
      its Replenish Mana active restores 30 mana plus 3% of the caster’s maximum mana
      to nearby allies within a 1200 radius.
    marks:
    - gamefile:items/item_arcane_ring#cost
    - gamefile:items/item_arcane_ring#attribs
    - loc:DOTA_Tooltip_ability_item_arcane_ring_Description
  - text: Replenish Mana is an immediate, no-target active with a 60.0-second cooldown.
    marks:
    - gamefile:items/item_arcane_ring#mechanics
  - text: “Once a prized heirloom of a minor lord’s house.”
    marks:
    - loc:DOTA_Tooltip_ability_item_arcane_ring_Lore
---

# Arcane Ring

Arcane Ring is an item with Bonus Armor and Bonus Intelligence whose active, Replenish Mana, restores mana to nearby allies. [gamefile:items/item_arcane_ring#attribs] [loc:DOTA_Tooltip_ability_item_arcane_ring_Description]

## Cost

| Item | Cost |
|---|---:|
| Arcane Ring | 0 gold |

[gamefile:items/item_arcane_ring#cost]

## Stats

| Stat | Value |
|---|---:|
| BONUS ARMOR | 0 |
| BONUS INTELLIGENCE | 0 |
| MANA RESTORE | 30 |
| MANA RESTORE PCT | 3% |
| RADIUS | 1200 |

[gamefile:items/item_arcane_ring#attribs]

## Active: Replenish Mana

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Cooldown | 60.0 |

[gamefile:items/item_arcane_ring#mechanics]

Replenish Mana restores a flat amount plus a percentage of the caster’s maximum mana pool to all nearby allies within its radius. [loc:DOTA_Tooltip_ability_item_arcane_ring_Description]

*Once a prized heirloom of a minor lord’s house.* [loc:DOTA_Tooltip_ability_item_arcane_ring_Lore]