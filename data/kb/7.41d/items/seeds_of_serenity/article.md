---
title: Seeds of Serenity
kind: item
patch: 7.41d
card:
  entity: seeds_of_serenity
  sentences:
  - text: Seeds of Serenity is a 0-gold item with the point-targeted, area-of-effect
      active Verdurous Dale, which gives allied units within its 400 radius health
      regeneration based on AURA HEALTH REGEN 8 and 25% of the caster’s health regeneration
      for DURATION 8.
    marks:
    - gamefile:items/item_seeds_of_serenity#cost
    - gamefile:items/item_seeds_of_serenity#mechanics
    - gamefile:items/item_seeds_of_serenity#attribs
    - loc:DOTA_Tooltip_Ability_item_seeds_of_serenity_Description
  - text: The build formula is Seeds of Serenity (0 gold).
    marks:
    - gamefile:items/item_seeds_of_serenity#cost
  - text: BONUS HEALTH is 0.
    marks:
    - gamefile:items/item_seeds_of_serenity#attribs
  - text: BONUS HEALTH REGEN is 0.
    marks:
    - gamefile:items/item_seeds_of_serenity#attribs
  - text: Verdurous Dale has a cast range of 350.
    marks:
    - gamefile:items/item_seeds_of_serenity#mechanics
  - text: Verdurous Dale has a cooldown of 35.0.
    marks:
    - gamefile:items/item_seeds_of_serenity#mechanics
  - text: Verdurous Dale targets the ground.
    marks:
    - loc:DOTA_Tooltip_Ability_item_seeds_of_serenity_Description
  - text: The caster’s health regeneration contribution is fixed at the time of casting.
    marks:
    - loc:DOTA_Tooltip_Ability_item_seeds_of_serenity_Description
  - text: An evergreen sprout treasured by the woodkin and highly coveted by interlopers
      and their like.
    marks:
    - loc:DOTA_Tooltip_Ability_item_seeds_of_serenity_Lore
---

# Seeds of Serenity

Seeds of Serenity is an item with the point-targeted, area-of-effect active Verdurous Dale, which provides health regeneration to allied units within its area. [gamefile:items/item_seeds_of_serenity#mechanics] [loc:DOTA_Tooltip_Ability_item_seeds_of_serenity_Description]

## Components

| Item | Gold cost |
|---|---:|
| Seeds of Serenity | 0 gold |

[gamefile:items/item_seeds_of_serenity#cost]

## Stats

| Stat | Value |
|---|---:|
| AURA HEALTH REGEN | 8 |
| AURA HEALTH REGEN PCT | 25% |
| BONUS HEALTH | 0 |
| BONUS HEALTH REGEN | 0 |
| DURATION | 8 |
| RADIUS | 400 |

[gamefile:items/item_seeds_of_serenity#attribs]

## Verdurous Dale

| Property | Value |
|---|---|
| Behavior | Point Target, AOE |
| Cast range | 350 |
| Cooldown | 35.0 |

[gamefile:items/item_seeds_of_serenity#mechanics]

Verdurous Dale targets the ground. Allied units receive health regeneration while within the area, calculated from the aura health regeneration and a percentage of the caster’s health regeneration at the time of casting. [loc:DOTA_Tooltip_Ability_item_seeds_of_serenity_Description]

*An evergreen sprout treasured by the woodkin and highly coveted by interlopers and their like.* [loc:DOTA_Tooltip_Ability_item_seeds_of_serenity_Lore]