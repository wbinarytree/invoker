---
title: Mage Slayer
kind: item
patch: 7.41d
card:
  entity: mage_slayer
  sentences:
  - text: Mage Slayer is a rare item costing 3100 gold that grants 12 damage, 5.5
      health regeneration, 18% magic resistance, and 2.5 mana regeneration, and whose
      passive debuffs attacked enemies for 3 seconds, dealing 35 damage per second
      and reducing their spell damage by 40%.
    marks:
    - gamefile:items/item_mage_slayer#cost
    - gamefile:items/item_mage_slayer#attribs
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: It is built from Perseverance (1400), Cloak (900), Blades of Attack (450),
      and Orb of Venom (350), totaling 3100 gold with no recipe.
    marks:
    - gamefile:items/item_mage_slayer#components
    - gamefile:items/item_mage_slayer#cost
  - text: The debuff is applied whenever the holder attacks an enemy.
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: The ability is passive and flagged `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES`,
      so it does not trigger other abilities.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: Its damage is physical.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: The debuff is dispellable.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: In lore it was forged by a secret order in The Third Age of Praxa'cia to
      fell the False King.
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Lore
---

# Mage Slayer

Mage Slayer is a rare item that grants bonus damage, health regeneration, magic resistance, and mana regeneration, and whose passive places a debuff on attacked enemies that deals physical damage per second and reduces their spell damage [gamefile:items/item_mage_slayer#cost][gamefile:items/item_mage_slayer#attribs][loc:DOTA_Tooltip_ability_item_mage_slayer_Description].

## Stats

| Stat | Value |
|---|---|
| Damage | 12 |
| Health Regeneration | 5.5 |
| Magic Resistance | 18% |
| Mana Regeneration | 2.5 |
| DPS | 35 |
| Duration | 3 |
| Spell Amp Debuff | 40% |

[gamefile:items/item_mage_slayer#attribs]

## Components

| Component | Gold |
|---|---|
| Perseverance | 1400 |
| Cloak | 900 |
| Blades of Attack | 450 |
| Orb of Venom | 350 |
| **Total** | **3100** |

[gamefile:items/item_mage_slayer#components][gamefile:items/item_mage_slayer#cost]

## Behavior

The Mage Slayer passive applies its debuff whenever the holder attacks an enemy; the debuff deals damage per second and lowers the target's spell damage for its duration [loc:DOTA_Tooltip_ability_item_mage_slayer_Description]. The ability is passive and flagged `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES`, so it does not trigger other abilities. Its damage is physical, and the debuff is dispellable [gamefile:items/item_mage_slayer#mechanics].

## Lore

Forged by a secret order in The Third Age of Praxa'cia to fell the False King [loc:DOTA_Tooltip_ability_item_mage_slayer_Lore].