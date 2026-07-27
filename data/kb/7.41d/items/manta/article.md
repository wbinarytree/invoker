---
title: Manta Style
kind: item
patch: 7.41d
card:
  entity: manta
  sentences:
  - text: Manta Style is an epic item costing 4650 gold that grants 26 Agility, 15
      Attack Speed, 10 Intelligence, 10% Movement Speed, and 10 Strength and provides
      Mirror Image, which creates 2 images of the hero with an illusion duration of
      18.
    marks:
    - gamefile:items/item_manta#cost
    - gamefile:items/item_manta#attribs
    - loc:DOTA_Tooltip_ability_item_manta_Description
  - text: It is built from Yasha for 2100 gold, Diadem for 1000 gold, and a Recipe
      for 1550 gold.
    marks:
    - gamefile:items/item_manta#components
  - text: The images deal 33% outgoing melee damage or 28% outgoing ranged damage.
    marks:
    - gamefile:items/item_manta#attribs
  - text: The images take 300% incoming damage.
    marks:
    - gamefile:items/item_manta#attribs
  - text: Mirror Image has an invulnerability duration of 0.1.
    marks:
    - gamefile:items/item_manta#attribs
  - text: The images have a vision radius of 1000.
    marks:
    - gamefile:items/item_manta#attribs
  - text: Mirror Image has No Target and DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK
      behavior.
    marks:
    - gamefile:items/item_manta#mechanics
  - text: Mirror Image costs 125 mana.
    marks:
    - gamefile:items/item_manta#mechanics
  - text: Mirror Image has a 34.0 cooldown.
    marks:
    - gamefile:items/item_manta#mechanics
  - text: Mirror Image has a Basic Dispel dispel type.
    marks:
    - loc:DOTA_Tooltip_ability_item_manta_Description
  - text: “An axe made of reflective materials that causes confusion amongst enemy
      ranks.”
    marks:
    - loc:DOTA_Tooltip_ability_item_manta_Lore
---

# Manta Style

Manta Style is an epic item that grants Agility, Attack Speed, Intelligence, Movement Speed, and Strength and provides the Mirror Image active. [gamefile:items/item_manta#cost] [gamefile:items/item_manta#attribs] [loc:DOTA_Tooltip_ability_item_manta_Description]

## Stats

| Stat | Value |
|---|---:|
| AGILITY | 26 |
| ATTACK SPEED | 15 |
| INTELLIGENCE | 10 |
| MOVEMENT SPEED | 10% |
| STRENGTH | 10 |
| ILLUSION DURATION | 18 |
| IMAGES COUNT | 2 |
| IMAGES DO DAMAGE PERCENT MELEE | -67 |
| IMAGES DO DAMAGE PERCENT RANGED | -72 |
| IMAGES TAKE DAMAGE PERCENT | 200 |
| INVULN DURATION | 0.1 |
| TOOLTIP DAMAGE INCOMING TOTAL PCT | 300% |
| TOOLTIP DAMAGE OUTGOING MELEE | 33% |
| TOOLTIP DAMAGE OUTGOING RANGED | 28% |
| VISION RADIUS | 1000 |

[gamefile:items/item_manta#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Yasha | 2100 gold |
| Diadem | 1000 gold |
| Recipe | 1550 gold |
| **Manta Style** | **4650 gold** |

[gamefile:items/item_manta#components] [gamefile:items/item_manta#cost]

## Mirror Image

| Property | Value |
|---|---|
| Behavior | No Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Mana cost | 125 |
| Cooldown | 34.0 |

[gamefile:items/item_manta#mechanics]

Mirror Image creates images of the hero. Its Dispel Type is Basic Dispel. [loc:DOTA_Tooltip_ability_item_manta_Description]

*An axe made of reflective materials that causes confusion amongst enemy ranks.* [loc:DOTA_Tooltip_ability_item_manta_Lore]