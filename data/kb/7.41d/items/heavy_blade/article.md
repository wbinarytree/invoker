---
title: Witchbane
kind: item
patch: 7.41d
card:
  entity: heavy_blade
  sentences:
  - text: 'Witchbane is a 0-gold item with Attack Speed, Damage, and Radius attributes:
      it grants 0 Attack Speed, its Subjugate passive makes attacks deal bonus magical
      damage equal to 4% of the target''s Max Mana, and its Cleanse active applies
      a Basic Dispel to all enemies and allies in a 300-radius area.'
    marks:
    - gamefile:items/item_heavy_blade#cost
    - gamefile:items/item_heavy_blade#attribs
    - loc:DOTA_Tooltip_Ability_item_heavy_blade_Description
  - text: Cleanse has Point Target, AOE behavior.
    marks:
    - gamefile:items/item_heavy_blade#mechanics
  - text: Cleanse has 700 cast range.
    marks:
    - gamefile:items/item_heavy_blade#mechanics
  - text: Cleanse costs 50 mana.
    marks:
    - gamefile:items/item_heavy_blade#mechanics
  - text: Cleanse has a 40-second cooldown.
    marks:
    - gamefile:items/item_heavy_blade#mechanics
---

# Witchbane

Witchbane is an item with the Attack Speed, Damage, and Radius attributes, the Cleanse active, and the Subjugate passive. [gamefile:items/item_heavy_blade#attribs] [loc:DOTA_Tooltip_Ability_item_heavy_blade_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Witchbane | 0 |

[gamefile:items/item_heavy_blade#cost]

## Stats

| Stat | Value |
|---|---:|
| ATTACK SPEED | 0 |
| DAMAGE — target's Max Mana as bonus magical damage | 4% |
| RADIUS — Cleanse area | 300 |

[gamefile:items/item_heavy_blade#attribs] [loc:DOTA_Tooltip_Ability_item_heavy_blade_Description]

| Cast property | Value |
|---|---:|
| Behavior | Point Target, AOE |
| Cast range | 700 |
| Mana cost | 50 |
| Cooldown | 40 |

[gamefile:items/item_heavy_blade#mechanics]

## Effects

**Cleanse** dispels all enemies and allies in its area. It applies a Basic Dispel. [loc:DOTA_Tooltip_Ability_item_heavy_blade_Description]

**Subjugate** causes attacks to deal bonus magical damage based on the target's Max Mana. [loc:DOTA_Tooltip_Ability_item_heavy_blade_Description]

*With ready access to test subjects, untold cruelties have been dreamed up and loosed upon the world from within the walls of the Tyler Estate.* [loc:DOTA_Tooltip_Ability_item_heavy_blade_Lore]