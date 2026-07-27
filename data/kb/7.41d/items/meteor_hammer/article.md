---
title: Meteor Hammer
kind: item
patch: 7.41d
card:
  entity: meteor_hammer
  sentences:
  - text: Meteor Hammer is an epic item costing 2850 gold that grants 6 Agility, 24
      Intelligence, 6 Strength, 35 Mana Regen Multiplier, and 10 Spell Amp, and provides
      a 75-mana active with a 24-second cooldown that channels for 2 seconds before
      a 400-radius magical meteor strike.
    marks:
    - gamefile:items/item_meteor_hammer#cost
    - gamefile:items/item_meteor_hammer#attribs
    - gamefile:items/item_meteor_hammer#mechanics
    - loc:DOTA_Tooltip_ability_item_meteor_hammer_Description
  - text: It is built from Kaya (2100 gold), Crown (450 gold), and a Recipe (300 gold).
    marks:
    - gamefile:items/item_meteor_hammer#components
    - gamefile:items/item_meteor_hammer#cost
  - text: The active has Point Target, AOE, Channelled behavior and 600 cast range.
    marks:
    - gamefile:items/item_meteor_hammer#mechanics
  - text: After a successful channel, the meteor lands after .5 seconds.
    marks:
    - gamefile:items/item_meteor_hammer#attribs
    - loc:DOTA_Tooltip_ability_item_meteor_hammer_Description
  - text: Impact deals 130 magical damage to non-building units and 90 magical damage
      to buildings, stunning enemies for 0.75 seconds.
    marks:
    - gamefile:items/item_meteor_hammer#attribs
    - gamefile:items/item_meteor_hammer#mechanics
    - loc:DOTA_Tooltip_ability_item_meteor_hammer_Description
  - text: The burn deals 50 damage per second to buildings and non-building units
      for 6 seconds at 1.0-second intervals.
    marks:
    - gamefile:items/item_meteor_hammer#attribs
    - loc:DOTA_Tooltip_ability_item_meteor_hammer_Description
  - text: Non-building units are slowed by 20% for the 6-second burn duration.
    marks:
    - gamefile:items/item_meteor_hammer#attribs
    - loc:DOTA_Tooltip_ability_item_meteor_hammer_Description
---

# Meteor Hammer

Meteor Hammer is an epic item that grants Agility, Intelligence, Strength, Mana Regen Multiplier, and Spell Amp, and provides the Meteor Hammer active. [gamefile:items/item_meteor_hammer#cost] [gamefile:items/item_meteor_hammer#attribs] [loc:DOTA_Tooltip_ability_item_meteor_hammer_Description]

## Components

| Component | Gold cost |
|---|---:|
| Kaya | 2100 gold |
| Crown | 450 gold |
| Recipe | 300 gold |
| **Meteor Hammer** | **2850 gold** |

[gamefile:items/item_meteor_hammer#components] [gamefile:items/item_meteor_hammer#cost]

## Stats

| Stat | Value |
|---|---:|
| AGILITY | 6 |
| INTELLIGENCE | 24 |
| STRENGTH | 6 |
| BURN DPS BUILDINGS / Building Over Time Damage | 50 |
| BURN DPS UNITS / Non-Building Over Time Damage | 50 |
| BURN DURATION | 6 |
| BURN INTERVAL | 1.0 |
| BURN SLOW | 20% |
| ENEMY PARTICLES VISIBLE | 0 |
| IMPACT DAMAGE BUILDINGS / Building Impact Damage | 90 |
| IMPACT DAMAGE UNITS / Non-Building Impact Damage | 130 |
| IMPACT RADIUS | 400 |
| LAND TIME / Landing Time | .5 |
| MANA REGEN MULTIPLIER | 35 |
| MAX DURATION / Channel Duration | 2 |
| SPELL AMP | 10 |
| STUN DURATION | 0.75 |

[gamefile:items/item_meteor_hammer#attribs] [loc:DOTA_Tooltip_ability_item_meteor_hammer_Description]

## Active

| Property | Value |
|---|---:|
| Behavior | Point Target, AOE, Channelled |
| Damage type | Magical |
| Cast range | 600 |
| Mana cost | 75 |
| Cooldown | 24 |

[gamefile:items/item_meteor_hammer#mechanics]

After a successful channel, the active summons a meteor that strikes an area, stuns enemies, and deals impact damage. It then deals damage over time to enemy units and buildings; non-building units are also slowed for the burn duration. [loc:DOTA_Tooltip_ability_item_meteor_hammer_Description]