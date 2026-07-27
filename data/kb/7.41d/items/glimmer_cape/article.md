---
title: Glimmer Cape
kind: item
patch: 7.41d
card:
  entity: glimmer_cape
  sentences:
  - text: Glimmer Cape is a rare 2150-gold item with Magic Resistance whose active
      Glimmer grants invisibility, 20 Active Movement Speed, 20% Magic Resistance,
      and a 375-magic-damage barrier for 5 seconds, with a 0.5-second Initial Fade
      Delay and 0.5 Secondary Fade Delay.
    marks:
    - gamefile:items/item_glimmer_cape#cost
    - gamefile:items/item_glimmer_cape#attribs
    - loc:DOTA_Tooltip_ability_item_glimmer_cape_Description
  - text: It is built from Shadow Amulet for 900 gold, Shawl for 450 gold, and a Recipe
      costing 800 gold.
    marks:
    - gamefile:items/item_glimmer_cape#components
  - text: Glimmer can be applied to the user or a target allied unit.
    marks:
    - loc:DOTA_Tooltip_ability_item_glimmer_cape_Description
  - text: Glimmer has 600 cast range.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: Glimmer costs 125 mana.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: Glimmer has a 15.0 cooldown.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: Its behavior is Immediate and Unit Target.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: It is usable while channelling.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: It does not resume movement.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: It is dispellable.
    marks:
    - gamefile:items/item_glimmer_cape#mechanics
  - text: The stolen cape of a master illusionist.
    marks:
    - loc:DOTA_Tooltip_ability_item_glimmer_cape_Lore
---

# Glimmer Cape

Glimmer Cape is a rare item with Magic Resistance whose active Glimmer grants invisibility, Active Movement Speed, and a magic damage barrier. [gamefile:items/item_glimmer_cape#cost] [gamefile:items/item_glimmer_cape#attribs] [loc:DOTA_Tooltip_ability_item_glimmer_cape_Description]

## Components

| Component | Gold cost |
|---|---:|
| Shadow Amulet | 900 gold |
| Shawl | 450 gold |
| Recipe | 800 gold |
| **Glimmer Cape** | **2150 gold** |

[gamefile:items/item_glimmer_cape#components] [gamefile:items/item_glimmer_cape#cost]

## Glimmer

| Stat | Value |
|---|---:|
| Active Movement Speed | 20 |
| Barrier Block | 375 magic damage |
| Magic Resistance | 20% |
| Duration | 5 seconds |
| Initial Fade Delay | 0.5 seconds |
| Secondary Fade Delay | 0.5 |

[gamefile:items/item_glimmer_cape#attribs] [loc:DOTA_Tooltip_ability_item_glimmer_cape_Description]

Glimmer can be applied to the user or a target allied unit; invisibility begins after a delay, while the barrier absorbs magic damage. [loc:DOTA_Tooltip_ability_item_glimmer_cape_Description]

| Use stat | Value |
|---|---:|
| Cast range | 600 |
| Mana cost | 125 |
| Cooldown | 15.0 |

[gamefile:items/item_glimmer_cape#mechanics]

Its behavior is Immediate and Unit Target; it is usable while channelling, does not resume movement, and is dispellable. [gamefile:items/item_glimmer_cape#mechanics]

*The stolen cape of a master illusionist.* [loc:DOTA_Tooltip_ability_item_glimmer_cape_Lore]