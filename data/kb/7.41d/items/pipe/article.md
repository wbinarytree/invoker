---
title: Pipe of Insight
kind: item
patch: 7.41d
card:
  entity: pipe
  sentences:
  - text: Pipe of Insight is a rare 3725-gold item granting 14 Health Regeneration
      and 20% Magic Resistance; its active Barrier provides nearby allies a 425 magic-damage
      barrier for 8.0 seconds within 1200 radius, while its passive Insight Aura provides
      allied units 8% Magic Resistance within 1200 radius.
    marks:
    - gamefile:items/item_pipe#cost
    - gamefile:items/item_pipe#attribs
    - loc:DOTA_Tooltip_ability_item_pipe_Description
  - text: Barrier has Immediate, No Target behavior.
    marks:
    - gamefile:items/item_pipe#mechanics
  - text: Barrier has 1200 cast range.
    marks:
    - gamefile:items/item_pipe#mechanics
  - text: Barrier costs 150 mana.
    marks:
    - gamefile:items/item_pipe#mechanics
  - text: Barrier has a 60.0-second cooldown.
    marks:
    - gamefile:items/item_pipe#mechanics
  - text: The barrier block for creeps is 425.
    marks:
    - gamefile:items/item_pipe#attribs
  - text: The build formula is Ring of Tarrasque (1700 gold), Cloak (900 gold), Shawl
      (450 gold), and Recipe (675 gold).
    marks:
    - gamefile:items/item_pipe#components
---

# Pipe of Insight

Pipe of Insight is a rare item that grants Health Regeneration and Magic Resistance, with the active Barrier and passive Insight Aura. [gamefile:items/item_pipe#cost] [gamefile:items/item_pipe#attribs] [loc:DOTA_Tooltip_ability_item_pipe_Description]

## Overview

| Property | Value |
|---|---:|
| Quality | rare |
| Cost | 3725 gold |

[gamefile:items/item_pipe#cost]

## Attributes

| Attribute | Value |
|---|---:|
| ADD NOSTACK DEBUFF | 1 |
| AURA HEALTH REGEN | 0 |
| AURA RADIUS | 1200 |
| BARRIER BLOCK | 425 |
| BARRIER BLOCK CREEP | 425 |
| BARRIER DURATION | 8.0 |
| BARRIER RADIUS | 1200 |
| BONUS ALL STATS | 0 |
| HEALTH REGENERATION | 14 |
| MAGIC RESISTANCE | 20% |
| MAGIC RESISTANCE AURA | 8% |

[gamefile:items/item_pipe#attribs]

## Barrier and Insight Aura

Barrier gives all nearby allies a magic damage barrier. Insight Aura gives allied units magic resistance. [loc:DOTA_Tooltip_ability_item_pipe_Description]

| Property | Value |
|---|---:|
| Behavior | Immediate, No Target |
| Cast range | 1200 |
| Mana cost | 150 |
| Cooldown | 60.0 |

[gamefile:items/item_pipe#mechanics]

## Components

| Component | Gold cost |
|---|---:|
| Ring of Tarrasque | 1700 gold |
| Cloak | 900 gold |
| Shawl | 450 gold |
| Recipe | 675 gold |

[gamefile:items/item_pipe#components]

*A powerful artifact of mysterious origin, it creates barriers against magical forces.* [loc:DOTA_Tooltip_ability_item_pipe_Lore]