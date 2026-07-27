---
title: Lotus Orb
kind: item
patch: 7.41d
card:
  entity: lotus_orb
  sentences:
  - text: Lotus Orb is an epic item costing 3850 gold that grants 10 Armor, 6.5 Health
      Regeneration, 250 Mana, and 4.0 Mana Regeneration, and its Echo Shell active
      applies a shield to a target unit for an Active Duration of 5 that re-casts
      most targeted spells back to their caster while the shielded unit still takes
      damage from the spell.
    marks:
    - gamefile:items/item_lotus_orb#cost
    - gamefile:items/item_lotus_orb#attribs
    - loc:DOTA_Tooltip_ability_item_lotus_orb_Description
  - text: Lotus Orb's build formula is Perseverance (1400 gold) + Platemail (1400
      gold) + Energy Booster (800 gold) + Recipe (250 gold).
    marks:
    - gamefile:items/item_lotus_orb#components
    - gamefile:items/item_lotus_orb#cost
  - text: Echo Shell has Unit Target behavior.
    marks:
    - gamefile:items/item_lotus_orb#mechanics
  - text: Echo Shell has 900 cast range.
    marks:
    - gamefile:items/item_lotus_orb#mechanics
  - text: Echo Shell costs 175 Mana.
    marks:
    - gamefile:items/item_lotus_orb#mechanics
  - text: Echo Shell has a 15.0 cooldown.
    marks:
    - gamefile:items/item_lotus_orb#mechanics
  - text: Echo Shell's dispel type is Basic Dispel.
    marks:
    - loc:DOTA_Tooltip_ability_item_lotus_orb_Description
  - text: The jewel at its center still reflects a pale image of its creator.
    marks:
    - loc:DOTA_Tooltip_ability_item_lotus_orb_Lore
---

# Lotus Orb

Lotus Orb is an epic item that grants Armor, Health Regeneration, Mana, and Mana Regeneration and provides the Echo Shell active ability. [gamefile:items/item_lotus_orb#cost] [gamefile:items/item_lotus_orb#attribs] [loc:DOTA_Tooltip_ability_item_lotus_orb_Description]

## Components

| Component | Gold cost |
|---|---:|
| Perseverance | 1400 gold |
| Platemail | 1400 gold |
| Energy Booster | 800 gold |
| Recipe | 250 gold |
| **Lotus Orb** | **3850 gold** |

[gamefile:items/item_lotus_orb#components] [gamefile:items/item_lotus_orb#cost]

## Stats

| Stat | Value |
|---|---:|
| Active Duration | 5 |
| Armor | 10 |
| Health Regeneration | 6.5 |
| Mana | 250 |
| Mana Regeneration | 4.0 |

[gamefile:items/item_lotus_orb#attribs]

## Echo Shell

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Cast range | 900 |
| Mana cost | 175 |
| Cooldown | 15.0 |

[gamefile:items/item_lotus_orb#mechanics]

Echo Shell applies a shield to the target unit that re-casts most targeted spells back to their caster. The shielded unit still takes damage from the spell. Its dispel type is Basic Dispel. [loc:DOTA_Tooltip_ability_item_lotus_orb_Description]

*The jewel at its center still reflects a pale image of its creator.* [loc:DOTA_Tooltip_ability_item_lotus_orb_Lore]