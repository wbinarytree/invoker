---
title: Mage Slayer
kind: item
patch: 7.41d
card:
  entity: mage_slayer
  sentences:
  - text: Mage Slayer is a rare item costing 3100 gold that grants 12 Damage, 5.5
      Health Regeneration, 18% Magic Resistance, and 2.5 Mana Regeneration, and carries
      a passive that places a debuff on attacked enemies dealing 35 DPS over 3 seconds
      with a 40% spell amp debuff.
    marks:
    - gamefile:items/item_mage_slayer#cost
    - gamefile:items/item_mage_slayer#attribs
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: It is built from Perseverance (1400), Cloak (900), Blades of Attack (450),
      and Orb of Venom (350).
    marks:
    - gamefile:items/item_mage_slayer#components
  - text: Its total cost is 3100 gold.
    marks:
    - gamefile:items/item_mage_slayer#cost
  - text: The passive triggers on the carrier's attacks against enemies, applying
      the debuff for its duration.
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: The damage dealt over that duration is physical.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: The passive is flagged DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES,
      so it does not trigger other on-hit effects.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: The debuff reduces the spell damage the affected enemy deals.
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: The debuff is dispellable.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
---

# Mage Slayer

Mage Slayer is a rare item that grants Damage, Health Regeneration, Magic Resistance, and Mana Regeneration, and carries the passive Mage Slayer, which places a debuff on attacked enemies that deals damage per second and applies a spell amp debuff [gamefile:items/item_mage_slayer#cost][gamefile:items/item_mage_slayer#attribs][loc:DOTA_Tooltip_ability_item_mage_slayer_Description].

## Stats

| Attribute | Value |
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

[gamefile:items/item_mage_slayer#components]

Total cost: 3100 gold [gamefile:items/item_mage_slayer#cost].

## Mechanics

The effect is a passive that triggers on the carrier's attacks against enemies, applying a debuff for its duration [loc:DOTA_Tooltip_ability_item_mage_slayer_Description]. Damage dealt over that duration is physical, and the passive is flagged `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES`, so it does not trigger other on-hit effects [gamefile:items/item_mage_slayer#mechanics]. The debuff reduces the spell damage the affected enemy deals [loc:DOTA_Tooltip_ability_item_mage_slayer_Description], and it is dispellable [gamefile:items/item_mage_slayer#mechanics].

---

*Forged by a secret order in The Third Age of Praxa'cia to fell the False King.* [loc:DOTA_Tooltip_ability_item_mage_slayer_Lore]