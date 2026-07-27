---
title: Bloodstone
kind: item
patch: 7.41d
card:
  entity: bloodstone
  sentences:
  - text: Bloodstone is an epic 4700-gold item granting 625 Health, 15 Intelligence,
      450 Mana, 20% Spell Lifesteal, 10% Aura Spell Vulnerability in a 1200 Aura Radius,
      and 60% Spell Lifesteal While Active for 5 seconds through Bloodpact.
    marks:
    - gamefile:items/item_bloodstone#cost
    - gamefile:items/item_bloodstone#attribs
    - loc:DOTA_Tooltip_ability_item_bloodstone_Description
  - text: It is built from Veil of Discord (1700 gold) and Soul Booster (3000 gold),
      with Bloodstone listed at 4700 gold.
    marks:
    - gamefile:items/item_bloodstone#components
    - gamefile:items/item_bloodstone#cost
  - text: Its Health Regeneration is 0.
    marks:
    - gamefile:items/item_bloodstone#attribs
  - text: Its Bonus MP Regen is 0.
    marks:
    - gamefile:items/item_bloodstone#attribs
  - text: Its HP Cost is 0.
    marks:
    - gamefile:items/item_bloodstone#attribs
  - text: Its behavior is No Target, Immediate.
    marks:
    - gamefile:items/item_bloodstone#mechanics
  - text: Its mana cost is 0.
    marks:
    - gamefile:items/item_bloodstone#mechanics
  - text: Its cooldown is 35.0.
    marks:
    - gamefile:items/item_bloodstone#mechanics
  - text: Spell Weakness Aura causes enemy units within its radius to take increased
      damage from spells.
    marks:
    - loc:DOTA_Tooltip_ability_item_bloodstone_Description
---

# Bloodstone

Bloodstone is an epic item that provides Health, Health Regeneration, Intelligence, Mana, Bonus MP Regen, Spell Lifesteal, and Spell Lifesteal While Active, with Aura Spell Vulnerability through Spell Weakness Aura and the Bloodpact active. [gamefile:items/item_bloodstone#cost] [gamefile:items/item_bloodstone#attribs] [loc:DOTA_Tooltip_ability_item_bloodstone_Description]

## Components

| Component | Gold cost |
|---|---:|
| Veil of Discord | 1700 gold |
| Soul Booster | 3000 gold |
| **Bloodstone** | **4700 gold** |

[gamefile:items/item_bloodstone#components] [gamefile:items/item_bloodstone#cost]

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

## Mechanics

| Property | Value |
|---|---|
| Behavior | No Target, Immediate |
| Mana cost | 0 |
| Cooldown | 35.0 |

[gamefile:items/item_bloodstone#mechanics]

Bloodpact increases Bloodstone’s Spell Lifesteal for its duration. Spell Weakness Aura causes enemy units within its radius to take increased damage from spells. [loc:DOTA_Tooltip_ability_item_bloodstone_Description]

*The Bloodstone's bright ruby color is unmistakable on the battlefield, as the owner seems to have infinite vitality and spirit.* [loc:DOTA_Tooltip_ability_item_bloodstone_Lore]