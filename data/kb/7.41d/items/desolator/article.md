---
title: Desolator
kind: item
patch: 7.41d
card:
  entity: desolator
  sentences:
  - text: Desolator is a 3500-gold artifact item with 55 Damage whose Corruption applies
      -6 armor for 7.0 seconds and whose Soul Stealer grants 1 Bonus Damage per Assist
      or 2 Bonus Damage per Kill, capped at 30.
    marks:
    - gamefile:items/item_desolator#cost
    - gamefile:items/item_desolator#attribs
    - loc:DOTA_Tooltip_ability_item_desolator_Description
  - text: It is built from a Mithril Hammer (1600 gold), a Mithril Hammer (1600 gold),
      and an Orb of Blight (300 gold).
    marks:
    - gamefile:items/item_desolator#components
  - text: Soul Stealer grants Desolator damage whenever an enemy hero dies while affected
      by Corruption, subject to a maximum.
    marks:
    - loc:DOTA_Tooltip_ability_item_desolator_Description
  - text: Its behavior is Passive.
    marks:
    - gamefile:items/item_desolator#mechanics
  - text: It is dispellable.
    marks:
    - gamefile:items/item_desolator#mechanics
  - text: Its lore reads, “A wicked weapon, used in torturing political criminals.”
    marks:
    - loc:DOTA_Tooltip_ability_item_desolator_Lore
---

# Desolator

Desolator is an artifact item that grants Damage, Bonus Damage per Assist, and Bonus Damage per Kill; its Corruption and Soul Stealer passives apply Corruption Armor for a Corruption Duration and are limited by Max Damage. [gamefile:items/item_desolator#cost] [gamefile:items/item_desolator#attribs] [loc:DOTA_Tooltip_ability_item_desolator_Description]

## Stats

| Stat | Value |
|---|---:|
| Damage | 55 |
| Bonus Damage per Assist | 1 |
| Bonus Damage per Kill | 2 |
| Corruption Armor | -6 |
| Corruption Duration | 7.0 |
| Max Damage | 30 |

[gamefile:items/item_desolator#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Mithril Hammer | 1600 |
| Mithril Hammer | 1600 |
| Orb of Blight | 300 |
| **Desolator** | **3500** |

[gamefile:items/item_desolator#components] [gamefile:items/item_desolator#cost]

## Mechanics

Corruption causes attacks to reduce the target’s armor for a duration. Soul Stealer grants Desolator damage whenever an enemy hero dies while affected by Corruption, subject to a maximum. [loc:DOTA_Tooltip_ability_item_desolator_Description]

Its behavior is Passive, and it is dispellable. [gamefile:items/item_desolator#mechanics]

*A wicked weapon, used in torturing political criminals.* [loc:DOTA_Tooltip_ability_item_desolator_Lore]