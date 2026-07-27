---
title: Arcane Blink
kind: item
patch: 7.41d
card:
  entity: arcane_blink
  sentences:
  - text: Arcane Blink is a component-quality 6800-gold item that grants 25 Intelligence;
      its 0-mana-cost active teleports the user to a target point within 1400 cast
      range, restores 250 health and 100 mana, and has a 9.0 cooldown.
    marks:
    - gamefile:items/item_arcane_blink#cost
    - gamefile:items/item_arcane_blink#attribs
    - gamefile:items/item_arcane_blink#mechanics
    - loc:DOTA_Tooltip_ability_item_arcane_blink_Description
  - text: Its build formula is Blink Dagger (2250 gold) + Mystic Staff (2800 gold)
      + Recipe (1750 gold).
    marks:
    - gamefile:items/item_arcane_blink#components
  - text: Its Blink Range is 1400.
    marks:
    - gamefile:items/item_arcane_blink#attribs
  - text: Its Blink Range Clamp is 1120.
    marks:
    - gamefile:items/item_arcane_blink#attribs
  - text: It cannot be used for 3.0 after the user takes damage from an enemy hero
      or Roshan.
    marks:
    - gamefile:items/item_arcane_blink#attribs
    - loc:DOTA_Tooltip_ability_item_arcane_blink_Description
  - text: The active is point-targeted and directional.
    marks:
    - gamefile:items/item_arcane_blink#mechanics
  - text: The active supports overshoot behavior.
    marks:
    - gamefile:items/item_arcane_blink#mechanics
  - text: Roots disable the active.
    marks:
    - gamefile:items/item_arcane_blink#mechanics
---

# Arcane Blink

Arcane Blink is a component-quality item [gamefile:items/item_arcane_blink#cost] that grants Intelligence [gamefile:items/item_arcane_blink#attribs] and provides the Arcane Blink active, which teleports its user to a target point and restores health and mana. [loc:DOTA_Tooltip_ability_item_arcane_blink_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 6800 gold |

[gamefile:items/item_arcane_blink#cost]

| Stat | Value |
|---|---:|
| Blink Damage Cooldown | 3.0 |
| Blink Range | 1400 |
| Blink Range Clamp | 1120 |
| Intelligence | 25 |
| Debuff Amp | 0 |
| Duration | 0 |
| Heal Amount | 250 |
| Mana Amount | 100 |

[gamefile:items/item_arcane_blink#attribs]

| Active stat | Value |
|---|---:|
| Cast range | 1400 |
| Mana cost | 0 |
| Cooldown | 9.0 |

[gamefile:items/item_arcane_blink#mechanics]

## Components

| Component | Gold cost |
|---|---:|
| Blink Dagger | 2250 gold |
| Mystic Staff | 2800 gold |
| Recipe | 1750 gold |

[gamefile:items/item_arcane_blink#components]

## Mechanics

Arcane Blink is point-targeted and directional, supports overshoot behavior, and is disabled by roots. [gamefile:items/item_arcane_blink#mechanics]

After teleportation, it restores health and mana. It cannot be used after taking damage from an enemy hero or Roshan until its damage cooldown expires. [loc:DOTA_Tooltip_ability_item_arcane_blink_Description]

*A revitalizing tool to help bear the weight of arcane expenditure.* [loc:DOTA_Tooltip_ability_item_arcane_blink_Lore]