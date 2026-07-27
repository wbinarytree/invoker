---
title: Bloodstone
kind: item
patch: 7.41d
card:
  entity: bloodstone
  sentences:
  - text: Bloodstone is a 4700-gold epic item granting 625 Health, 15 Intelligence,
      450 Mana, and 20% Spell Lifesteal; Bloodpact increases Spell Lifesteal to 60%
      with Buff Duration 5, while Spell Weakness Aura applies 10% Aura Spell Vulnerability
      to enemies within 1200.
    marks:
    - gamefile:items/item_bloodstone#cost
    - gamefile:items/item_bloodstone#attribs
    - loc:DOTA_Tooltip_ability_item_bloodstone_Description
  - text: Bloodpact has No Target, Immediate behavior.
    marks:
    - gamefile:items/item_bloodstone#mechanics
  - text: Its cooldown is 35.0.
    marks:
    - gamefile:items/item_bloodstone#mechanics
  - text: 'Build formula: Veil of Discord (1700 gold) + Soul Booster (3000 gold).'
    marks:
    - gamefile:items/item_bloodstone#components
  - text: The Bloodstone's bright ruby color is unmistakable on the battlefield, as
      the owner seems to have infinite vitality and spirit.
    marks:
    - loc:DOTA_Tooltip_ability_item_bloodstone_Lore
---

# Bloodstone

Bloodstone is an epic item that grants Health, Intelligence, Mana, and Spell Lifesteal; its active Bloodpact increases Spell Lifesteal, while its passive Spell Weakness Aura applies Aura Spell Vulnerability to enemy units. [gamefile:items/item_bloodstone#cost] [gamefile:items/item_bloodstone#attribs] [loc:DOTA_Tooltip_ability_item_bloodstone_Description]

## Stats

| Stat | Value |
|---|---:|
| Aura Radius | 1200 |
| Aura Spell Vulnerability | 10% |
| Health | 625 |
| Health Regeneration | 0 |
| Intelligence | 15 |
| Mana | 450 |
| Bonus MP Regen | 0 |
| Buff Duration | 5 |
| HP Cost | 0 |
| Spell Lifesteal | 20% |
| Spell Lifesteal While Active | 60% |

[gamefile:items/item_bloodstone#attribs]

| Property | Value |
|---|---|
| Behavior | No Target, Immediate |
| Cooldown | 35.0 |

[gamefile:items/item_bloodstone#mechanics]

## Abilities

Bloodpact increases Bloodstone’s Spell Lifesteal while active for the buff duration. Spell Weakness Aura causes enemy units within its radius to take increased damage from spells. [loc:DOTA_Tooltip_ability_item_bloodstone_Description]

## Components

| Component | Cost |
|---|---:|
| Veil of Discord | 1700 gold |
| Soul Booster | 3000 gold |
| **Bloodstone** | **4700 gold** |

[gamefile:items/item_bloodstone#components] [gamefile:items/item_bloodstone#cost]

*The Bloodstone's bright ruby color is unmistakable on the battlefield, as the owner seems to have infinite vitality and spirit.* [loc:DOTA_Tooltip_ability_item_bloodstone_Lore]