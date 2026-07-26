---
title: Mage Slayer
kind: item
patch: 7.41d
card:
  entity: mage_slayer
  sentences:
  - text: Mage Slayer is a rare 3100-gold item that grants 12 damage, 5.5 health regeneration,
      18% magic resistance, and 2.5 mana regeneration, and carries the passive Mage
      Slayer, which debuffs attacked enemies for 35 damage per second and 40% reduced
      spell damage over 3 seconds.
    marks:
    - gamefile:items/item_mage_slayer#cost
    - gamefile:items/item_mage_slayer#attribs
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: It is built from Perseverance, Cloak, Blades of Attack, and Orb of Venom.
    marks:
    - gamefile:items/item_mage_slayer#components
  - text: The passive applies its debuff when the holder attacks an enemy.
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: The debuff's damage over time is physical damage.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: The debuff can be removed by a dispel.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: The ability is flagged DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES,
      so it does not trigger other on-hit effects.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: 'Lore: it was forged by a secret order in The Third Age of Praxa''cia to
      fell the False King.'
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Lore
---

# Mage Slayer

Mage Slayer is a rare item that grants bonus damage, health regeneration, magic resistance, and mana regeneration, and carries the passive Mage Slayer, which places a debuff on attacked enemies that deals physical damage per second and reduces their spell damage [gamefile:items/item_mage_slayer#cost][gamefile:items/item_mage_slayer#attribs][loc:DOTA_Tooltip_ability_item_mage_slayer_Description].

## Cost and components

| | |
|---|---|
| Cost | 3100 gold |
| Components | Perseverance, Cloak, Blades of Attack, Orb of Venom |

[gamefile:items/item_mage_slayer#cost][gamefile:items/item_mage_slayer#components]

## Bonuses

| Stat | Value |
|---|---|
| Damage | 12 |
| Health regeneration | 5.5 |
| Magic resistance | 18% |
| Mana regeneration | 2.5 |

[gamefile:items/item_mage_slayer#attribs]

## Passive: Mage Slayer

| | |
|---|---|
| DPS | 35 |
| Spell amp debuff | 40% |
| Duration | 3 |

[gamefile:items/item_mage_slayer#attribs]

The passive applies its debuff when the holder attacks an enemy; the debuff deals damage over time and lowers the affected unit's spell damage output for its duration [loc:DOTA_Tooltip_ability_item_mage_slayer_Description]. The damage it deals is physical, and the debuff can be removed by a dispel [gamefile:items/item_mage_slayer#mechanics].

The ability is flagged `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES`, so it does not trigger other on-hit effects [gamefile:items/item_mage_slayer#mechanics].

## Lore

Forged by a secret order in The Third Age of Praxa'cia to fell the False King [loc:DOTA_Tooltip_ability_item_mage_slayer_Lore].