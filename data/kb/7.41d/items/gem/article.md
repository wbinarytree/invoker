---
title: Gem of True Sight
kind: item
patch: 7.41d
card:
  entity: gem
  sentences:
  - text: Gem of True Sight is a 900-gold component item whose active Reveal grants
      True Sight in a 300-radius area for 4 seconds and whose passive True Sight has
      900 radius.
    marks:
    - gamefile:items/item_gem#cost
    - gamefile:items/item_gem#attribs
    - loc:DOTA_Tooltip_ability_item_gem_Description
  - text: Reveal has Point Target, AOE behavior.
    marks:
    - gamefile:items/item_gem#mechanics
  - text: Reveal has 300 cast range.
    marks:
    - gamefile:items/item_gem#mechanics
  - text: Reveal has a 12-second cooldown.
    marks:
    - gamefile:items/item_gem#mechanics
  - text: Reveal exposes wards and units even in Fog of War.
    marks:
    - loc:DOTA_Tooltip_ability_item_gem_Description
  - text: Passive True Sight lets allied vision within range of the carrier see invisible
      units and wards.
    marks:
    - loc:DOTA_Tooltip_ability_item_gem_Description
  - text: Everlasting causes the item to drop when its carrier dies.
    marks:
    - loc:DOTA_Tooltip_ability_item_gem_Description
  - text: Everlasting prevents the item from being destroyed.
    marks:
    - loc:DOTA_Tooltip_ability_item_gem_Description
---

# Gem of True Sight

Gem of True Sight is a component item with the active Reveal and the passives True Sight and Everlasting. [gamefile:items/item_gem#cost] [loc:DOTA_Tooltip_ability_item_gem_Description]

## Cost

| Item | Gold |
|---|---:|
| Gem of True Sight | 900 |

[gamefile:items/item_gem#cost]

## Stats

| Stat | Value |
|---|---:|
| Active Radius | 300 |
| Duration | 4 |
| Radius | 900 |

[gamefile:items/item_gem#attribs]

| Stat | Value |
|---|---|
| Behavior | Point Target, AOE |
| Cast range | 300 |
| Cooldown | 12 |

[gamefile:items/item_gem#mechanics]

## Mechanics

Reveal grants True Sight in its area, revealing wards and units even in Fog of War. Passive True Sight allows any allied vision within range of the carrier to see invisible units and wards. Everlasting causes the item to be dropped on death and prevents it from being destroyed. [loc:DOTA_Tooltip_ability_item_gem_Description]

> Not one thrall creature of the depths,  
> Nor spirit bound in drowning's keep,  
> Nor Maelrawn the Tentacular,  
> Shall rest till seas, gem comes to sleep.  
> [loc:DOTA_Tooltip_ability_item_gem_Lore]