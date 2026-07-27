---
title: Meteor Hammer
kind: item
patch: 7.41d
card:
  entity: meteor_hammer
  sentences:
  - text: Meteor Hammer is an epic 2850-gold item granting 6 Agility, 24 Intelligence,
      6 Strength, 35 Mana Regen Multiplier, and 10 Spell Amp; its 75-mana, 24-second-cooldown
      active channels for up to 2 seconds, then summons a Magical meteor that impacts
      a 400-radius area for 130 non-building or 90 building damage, stuns for 0.75
      seconds, and applies 50 damage per second for 6 seconds plus a 20% non-building
      slow.
    marks:
    - gamefile:items/item_meteor_hammer#cost
    - gamefile:items/item_meteor_hammer#attribs
    - gamefile:items/item_meteor_hammer#mechanics
    - loc:DOTA_Tooltip_ability_item_meteor_hammer_Description
  - text: Meteor Hammer builds from Kaya (2100 gold), Crown (450 gold), and a Recipe
      (300 gold).
    marks:
    - gamefile:items/item_meteor_hammer#components
    - gamefile:items/item_meteor_hammer#cost
  - text: The active has Point Target, AOE, and Channelled behavior.
    marks:
    - gamefile:items/item_meteor_hammer#mechanics
  - text: Its cast range is 600.
    marks:
    - gamefile:items/item_meteor_hammer#mechanics
  - text: After a successful channel, the meteor lands in .5 seconds.
    marks:
    - gamefile:items/item_meteor_hammer#attribs
    - loc:DOTA_Tooltip_ability_item_meteor_hammer_Description
  - text: Impact deals 130 Magical damage to non-building units and 90 Magical damage
      to buildings.
    marks:
    - gamefile:items/item_meteor_hammer#attribs
    - gamefile:items/item_meteor_hammer#mechanics
  - text: Impact stuns enemies for 0.75 seconds.
    marks:
    - gamefile:items/item_meteor_hammer#attribs
    - loc:DOTA_Tooltip_ability_item_meteor_hammer_Description
  - text: The burn deals 50 damage per second for 6 seconds to enemy units and buildings.
    marks:
    - gamefile:items/item_meteor_hammer#attribs
    - loc:DOTA_Tooltip_ability_item_meteor_hammer_Description
  - text: Burn damage occurs at 1.0-second intervals.
    marks:
    - gamefile:items/item_meteor_hammer#attribs
  - text: Non-building units are slowed by 20% for the burn duration.
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