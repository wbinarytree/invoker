---
title: Mage Slayer
kind: item
patch: 7.41d
card:
  entity: mage_slayer
  sentences:
  - text: Mage Slayer is a rare item costing 3100 gold that grants 12 damage, 5.5
      health regeneration, 18% magic resistance, and 2.5 mana regeneration, and whose
      holder's attacks apply a debuff dealing 35 damage per second and reducing the
      target's spell damage by 40% for 3 seconds.
    marks:
    - gamefile:items/item_mage_slayer#cost
    - gamefile:items/item_mage_slayer#attribs
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: The debuff is placed on enemies the holder attacks.
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: The debuff's damage is physical.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: The ability is passive and is flagged not to proc other abilities.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: The debuff is dispellable.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: It is built from Perseverance, Cloak, Blades of Attack, and Orb of Venom.
    marks:
    - gamefile:items/item_mage_slayer#components
  - text: Its lore says it was forged by a secret order in The Third Age of Praxa'cia
      to fell the False King.
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Lore
---

# Mage Slayer

Mage Slayer is a rare item costing 3100 gold that grants damage, health regeneration, magic resistance, and mana regeneration, and applies a debuff when its holder attacks that deals damage per second and reduces the target's spell damage [gamefile:items/item_mage_slayer#cost] [gamefile:items/item_mage_slayer#attribs] [loc:DOTA_Tooltip_ability_item_mage_slayer_Description].

## Stats

| Stat | Value |
|---|---|
| Damage | 12 |
| Health regeneration | 5.5 |
| Magic resistance | 18% |
| Mana regeneration | 2.5 |

[gamefile:items/item_mage_slayer#attribs]

## Passive: Mage Slayer

| Property | Value |
|---|---|
| DPS | 35 |
| Duration | 3 |
| Spell amp debuff | 40% |

[gamefile:items/item_mage_slayer#attribs]

The debuff is placed on enemies the holder attacks, dealing damage per second and making them do less spell damage for its duration [loc:DOTA_Tooltip_ability_item_mage_slayer_Description]. Its damage is physical, and the ability is passive and flagged not to proc other abilities. The debuff is dispellable [gamefile:items/item_mage_slayer#mechanics].

## Components

| Component | Gold |
|---|---|
| Perseverance | 1400 |
| Cloak | 900 |
| Blades of Attack | 450 |
| Orb of Venom | 350 |

[gamefile:items/item_mage_slayer#components]

Total: 3100 gold [gamefile:items/item_mage_slayer#cost].

## Lore

Forged by a secret order in The Third Age of Praxa'cia to fell the False King [loc:DOTA_Tooltip_ability_item_mage_slayer_Lore].