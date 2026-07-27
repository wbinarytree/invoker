---
title: Glimmer Cape
kind: item
patch: 7.41d
card:
  entity: glimmer_cape
  sentences:
  - text: Glimmer Cape is a rare item costing 2150 gold that provides 20% Magic Resistance
      and whose Glimmer active grants 20 Active Movement Speed, 375 Barrier Block,
      and invisibility for a Duration of 5 after an Initial Fade Delay of 0.5.
    marks:
    - gamefile:items/item_glimmer_cape#cost
    - gamefile:items/item_glimmer_cape#attribs
    - loc:DOTA_Tooltip_ability_item_glimmer_cape_Description
  - text: It is built from Shadow Amulet for 900 gold, Shawl for 450 gold, and a Recipe
      for 800 gold.
    marks:
    - gamefile:items/item_glimmer_cape#components
    - gamefile:items/item_glimmer_cape#cost
  - text: Its Secondary Fade Delay is 0.5.
    marks:
    - gamefile:items/item_glimmer_cape#attribs
  - text: Glimmer has Immediate, Unit Target, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL,
      and DOTA_ABILITY_BEHAVIOR_DONT_RESUME_MOVEMENT behavior.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: Glimmer is dispellable.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: Its cast range is 600.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: Its mana cost is 125.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: Its cooldown is 15.0.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: Glimmer can target the holder or an allied unit.
    marks:
    - loc:DOTA_Tooltip_ability_item_glimmer_cape_Description
  - text: Glimmer can be cast while channeling.
    marks:
    - loc:DOTA_Tooltip_ability_item_glimmer_cape_Description
---

# Glimmer Cape

Glimmer Cape is a rare item with Magic Resistance and the Glimmer active, which grants Active Movement Speed, Barrier Block, and invisibility. [gamefile:items/item_glimmer_cape#cost] [gamefile:items/item_glimmer_cape#attribs] [loc:DOTA_Tooltip_ability_item_glimmer_cape_Description]

## Components

| Component | Gold cost |
|---|---:|
| Shadow Amulet | 900 gold |
| Shawl | 450 gold |
| Recipe | 800 gold |
| **Total cost** | **2150 gold** |

[gamefile:items/item_glimmer_cape#components] [gamefile:items/item_glimmer_cape#cost]

## Stats

| Stat | Value |
|---|---:|
| Active Movement Speed | 20 |
| Barrier Block | 375 |
| Magic Resistance | 20% |
| Duration | 5 |
| Initial Fade Delay | 0.5 |
| Secondary Fade Delay | 0.5 |

[gamefile:items/item_glimmer_cape#attribs]

## Glimmer

| Property | Value |
|---|---|
| Behavior | Immediate, Unit Target, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_MOVEMENT |
| Dispellable | Yes |
| Cast range | 600 |
| Mana cost | 125 |
| Cooldown | 15.0 |

[gamefile:items/item_glimmer_cape#mechanics]

Glimmer can target the holder or an allied unit and can be cast while channeling; after its delay, it grants invisibility and the listed active effects for its duration. [loc:DOTA_Tooltip_ability_item_glimmer_cape_Description]

*The stolen cape of a master illusionist.* [loc:DOTA_Tooltip_ability_item_glimmer_cape_Lore]