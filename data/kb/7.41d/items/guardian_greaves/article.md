---
title: Guardian Greaves
kind: item
patch: 7.41d
card:
  entity: guardian_greaves
  sentences:
  - text: Guardian Greaves is a rare 4450-gold item that grants 5 Armor, 150 Mana,
      50 Movement Speed, and 1.0 Mana Regeneration; Mend restores 325 health and 200
      mana to nearby allies within 1200 radius and applies a Basic Dispel to the caster,
      while Guardian Aura grants allied units 2.5 Health Regen and 1.5 Mana Regen
      within 1200 radius.
    marks:
    - gamefile:items/item_guardian_greaves#cost
    - gamefile:items/item_guardian_greaves#attribs
    - loc:DOTA_Tooltip_ability_item_guardian_greaves_Description
  - text: Guardian Greaves is built from Arcane Boots (1500 gold), Mekansm (1775 gold),
      and a Recipe (1175 gold).
    marks:
    - gamefile:items/item_guardian_greaves#components
    - gamefile:items/item_guardian_greaves#cost
  - text: Mend is an Immediate, No Target active with 0 mana cost and a 45-second
      cooldown.
    marks:
    - gamefile:items/item_guardian_greaves#mechanics
  - text: When the wearer is below 25% health, Guardian Aura’s Health Regen increases
      by 14.5.
    marks:
    - gamefile:items/item_guardian_greaves#attribs
    - loc:DOTA_Tooltip_ability_item_guardian_greaves_Description
  - text: Movement Speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_ability_item_guardian_greaves_Description
---

# Guardian Greaves

Guardian Greaves is a rare item that grants Armor, Mana, Movement Speed, and Mana Regeneration; its Mend active restores health and mana and removes most negative effects from the caster, while Guardian Aura grants Health Regen and Mana Regen to allied units. [gamefile:items/item_guardian_greaves#cost] [gamefile:items/item_guardian_greaves#attribs] [loc:DOTA_Tooltip_ability_item_guardian_greaves_Description]

## Components

| Formula entry | Gold cost |
|---|---:|
| Arcane Boots | 1500 gold |
| Mekansm | 1775 gold |
| Recipe | 1175 gold |
| **Guardian Greaves** | **4450 gold** |

[gamefile:items/item_guardian_greaves#components] [gamefile:items/item_guardian_greaves#cost]

## Stats

| Stat | Value |
|---|---:|
| Aura Bonus Threshold | 25% |
| Aura Health Regen | 2.5 |
| Aura Health Regen Bonus | 14.5 |
| Aura Mana Regen | 1.5 |
| Aura Radius | 1200 |
| Armor | 5 |
| Mana | 150 |
| Movement Speed | 50 |
| Mana Regeneration | 1.0 |
| Max Health Pct Heal Amount | 0 |
| Replenish Health | 325 |
| Replenish Mana | 200 |
| Replenish Radius | 1200 |

[gamefile:items/item_guardian_greaves#attribs]

## Mend

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Mana cost | 0 |
| Cooldown | 45 |

[gamefile:items/item_guardian_greaves#mechanics]

Mend affects nearby allies and applies a Basic Dispel to the caster. [loc:DOTA_Tooltip_ability_item_guardian_greaves_Description]

## Guardian Aura

The aura’s health regeneration increases for the wearer while their health is below its threshold. Movement Speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_ability_item_guardian_greaves_Description]

*One of many holy instruments constructed to honor the Omniscience.* [loc:DOTA_Tooltip_ability_item_guardian_greaves_Lore]