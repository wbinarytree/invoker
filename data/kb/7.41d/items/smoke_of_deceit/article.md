---
title: Smoke of Deceit
kind: item
patch: 7.41d
card:
  entity: smoke_of_deceit
  sentences:
  - text: Smoke of Deceit is a 50-gold consumable whose Disguise grants invisibility
      and 15% bonus movement speed for 45.0 seconds to the caster and allied player-controlled
      units within a 1200 application radius.
    marks:
    - gamefile:items/item_smoke_of_deceit#cost
    - gamefile:items/item_smoke_of_deceit#attribs
    - loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Description
  - text: Its cooldown is 1.0.
    marks:
    - gamefile:items/item_smoke_of_deceit#mechanics
  - text: The second cast cooldown is 2.0.
    marks:
    - gamefile:items/item_smoke_of_deceit#attribs
  - text: While the caster remains disguised, allies entering the 300 secondary application
      radius also receive the buff.
    marks:
    - gamefile:items/item_smoke_of_deceit#attribs
    - loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Description
  - text: Each smoke can be applied only once to allies.
    marks:
    - loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Description
  - text: Attacking or moving within 1025 radius of an enemy hero or tower breaks
      the invisibility.
    marks:
    - gamefile:items/item_smoke_of_deceit#attribs
    - loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Description
  - text: The invisibility is immune to True Sight.
    marks:
    - loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Description
  - text: Smoke of Deceit can be used from the backpack.
    marks:
    - loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Description
  - text: It has no cooldown when moved into the main inventory.
    marks:
    - loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Description
  - text: The charlatan wizard Myrddin's only true contribution to the arcane arts.
    marks:
    - loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Lore
---

# Smoke of Deceit

Smoke of Deceit is a consumable item whose Disguise grants invisibility and bonus movement speed. [gamefile:items/item_smoke_of_deceit#cost] [loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 50 gold |

[gamefile:items/item_smoke_of_deceit#cost]

| Stat | Value |
|---|---:|
| Application radius | 1200 |
| Bonus movement speed | 15% |
| Duration | 45.0 |
| Second cast cooldown | 2.0 |
| Secondary application radius | 300 |
| Visibility radius | 1025 |

[gamefile:items/item_smoke_of_deceit#attribs]

| Property | Value |
|---|---|
| Behavior | No Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Cast range | 1200 |
| Cooldown | 1.0 |

[gamefile:items/item_smoke_of_deceit#mechanics]

## Disguise

Disguise affects the caster and all allied player-controlled units within the application radius. While the caster remains disguised, allies entering the secondary application radius also receive the buff; each smoke can only be applied once to allies. Attacking or moving within the visibility radius of an enemy hero or tower breaks the invisibility. The invisibility is immune to True Sight. Smoke of Deceit can be used from the backpack and has no cooldown when moved into the main inventory. [loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Description]

*The charlatan wizard Myrddin's only true contribution to the arcane arts.* [loc:DOTA_Tooltip_ability_item_smoke_of_deceit_Lore]