---
title: Mekansm
kind: item
patch: 7.41d
card:
  entity: mekansm
  sentences:
  - text: Mekansm is a rare 1775-gold item that provides 5 Armor and restores 250
      health to allied units within a 1200 radius, while its aura grants 2.5 health
      regeneration within a 1200 radius.
    marks:
    - gamefile:items/item_mekansm#cost
    - gamefile:items/item_mekansm#attribs
    - loc:DOTA_Tooltip_ability_item_mekansm_Description
  - text: Restore has Immediate, No Target behavior.
    marks:
    - gamefile:items/item_mekansm#mechanics
  - text: Restore has 1200 cast range.
    marks:
    - gamefile:items/item_mekansm#mechanics
  - text: Restore costs 100 mana.
    marks:
    - gamefile:items/item_mekansm#mechanics
  - text: Restore has a 50.0 cooldown.
    marks:
    - gamefile:items/item_mekansm#mechanics
  - text: Mekansm is built from Headdress for 425 gold, Chainmail for 500 gold, and
      a Recipe for 850 gold.
    marks:
    - gamefile:items/item_mekansm#components
  - text: Mekansm builds into Guardian Greaves.
    marks:
    - gamefile:items/item_mekansm#components
---

# Mekansm

Mekansm is a rare item with Armor, Aura Health Regen, Aura Radius, Heal Amount, and Heal Radius. [gamefile:items/item_mekansm#cost] [gamefile:items/item_mekansm#attribs]

## Stats

| Stat | Value |
|---|---:|
| Aura Health Regen | 2.5 |
| Aura Radius | 1200 |
| Armor | 5 |
| Heal Amount | 250 |
| Heal Radius | 1200 |

[gamefile:items/item_mekansm#attribs]

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Cast range | 1200 |
| Mana cost | 100 |
| Cooldown | 50.0 |

[gamefile:items/item_mekansm#mechanics]

Restore restores health to allied units in its radius. Mekansm Aura passively grants health regeneration to allied units in its radius. [loc:DOTA_Tooltip_ability_item_mekansm_Description]

## Cost and Components

| Item | Gold cost |
|---|---:|
| Mekansm | 1775 gold |

[gamefile:items/item_mekansm#cost]

| Component | Gold cost |
|---|---:|
| Headdress | 425 gold |
| Chainmail | 500 gold |
| Recipe | 850 gold |

[gamefile:items/item_mekansm#components]

**Builds into:** Guardian Greaves — 4450 gold. [gamefile:items/item_mekansm#components]

*A glowing jewel formed out of assorted parts that somehow fit together perfectly.* [loc:DOTA_Tooltip_ability_item_mekansm_Lore]