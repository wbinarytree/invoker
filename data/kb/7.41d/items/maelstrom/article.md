---
title: Maelstrom
kind: item
patch: 7.41d
card:
  entity: maelstrom
  sentences:
  - text: Maelstrom is a 2950-gold artifact item that grants 25 Attack Speed and 25
      Damage and passively has a 25% chance on attack to release Chain Lightning with
      110 magical damage, 4 strikes, a 650 radius, 0.25 delay, and a 0.2 cooldown.
    marks:
    - gamefile:items/item_maelstrom#cost
    - gamefile:items/item_maelstrom#attribs
    - gamefile:items/item_maelstrom#mechanics
    - loc:DOTA_Tooltip_ability_item_maelstrom_Description
  - text: Its Illusion Multiplier Pct is 100.
    marks:
    - gamefile:items/item_maelstrom#attribs
  - text: The Chain Lightning bolt leaps between targets and deals magical damage
      to each.
    marks:
    - loc:DOTA_Tooltip_ability_item_maelstrom_Description
  - text: Its proc pierces evasion.
    marks:
    - loc:DOTA_Tooltip_ability_item_maelstrom_Description
  - text: Its build formula is Mithril Hammer for 1600 gold, Javelin for 900 gold,
      and Gloves of Haste for 450 gold; it builds into Mjollnir.
    marks:
    - gamefile:items/item_maelstrom#components
  - text: “A hammer forged for the gods themselves, Maelstrom allows its user to harness
      the power of lightning.”
    marks:
    - loc:DOTA_Tooltip_ability_item_maelstrom_Lore
---

# Maelstrom

Maelstrom is an artifact item [gamefile:items/item_maelstrom#cost] that grants Attack Speed and Damage [gamefile:items/item_maelstrom#attribs] and has the passive Chain Lightning effect. [loc:DOTA_Tooltip_ability_item_maelstrom_Description]

## Cost

| Property | Value |
|---|---:|
| Cost | 2950 gold |

[gamefile:items/item_maelstrom#cost]

## Stats

| Stat | Value |
|---|---:|
| Attack Speed | 25 |
| Damage | 25 |
| Chain Chance | 25% |
| Chain Cooldown | 0.2 |
| Chain Damage | 110 |
| Chain Delay | 0.25 |
| Chain Radius | 650 |
| Chain Strikes | 4 |
| Illusion Multiplier Pct | 100 |

[gamefile:items/item_maelstrom#attribs]

## Components

| Build formula | Gold cost |
|---|---:|
| Mithril Hammer | 1600 gold |
| Javelin | 900 gold |
| Gloves of Haste | 450 gold |
| **Builds into: Mjollnir** | **5500 gold** |

[gamefile:items/item_maelstrom#components]

## Mechanics

Chain Lightning is passive. [gamefile:items/item_maelstrom#mechanics]

It can trigger on attack, releasing a bolt of electricity that leaps between targets within its radius and deals magical damage to each. Its proc pierces evasion. [loc:DOTA_Tooltip_ability_item_maelstrom_Description]

*A hammer forged for the gods themselves, Maelstrom allows its user to harness the power of lightning.* [loc:DOTA_Tooltip_ability_item_maelstrom_Lore]