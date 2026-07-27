---
title: Mage Slayer
kind: item
patch: 7.41d
card:
  entity: mage_slayer
  sentences:
  - text: Mage Slayer is a rare 3100-gold item that grants 12 Damage, 5.5 Health Regeneration,
      18% Magic Resistance, and 2.5 Mana Regeneration; its passive makes attacks apply
      a 3-second debuff with 35 DPS and a 40% Spell Amp Debuff.
    marks:
    - gamefile:items/item_mage_slayer#cost
    - gamefile:items/item_mage_slayer#attribs
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: Mage Slayer is built from Perseverance (1400 gold), Cloak (900 gold), Blades
      of Attack (450 gold), and Orb of Venom (350 gold).
    marks:
    - gamefile:items/item_mage_slayer#components
  - text: The debuff's damage is physical.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: The passive is flagged `DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES`,
      so it does not trigger other on-hit effects.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: The debuff reduces the spell damage the affected enemy deals.
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Description
  - text: The debuff is dispellable.
    marks:
    - gamefile:items/item_mage_slayer#mechanics
  - text: Forged by a secret order in The Third Age of Praxa'cia to fell the False
      King.
    marks:
    - loc:DOTA_Tooltip_ability_item_mage_slayer_Lore
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