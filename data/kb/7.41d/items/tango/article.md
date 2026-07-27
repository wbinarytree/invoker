---
title: Tango
kind: item
patch: 7.41d
card:
  entity: tango
  sentences:
  - text: Tango is a 90-gold consumable with 3 Tooltip Charges; Devour consumes a
      target tree and grants 7.0 Health Regen for a 16.0 Buff Duration.
    marks:
    - gamefile:items/item_tango#cost
    - gamefile:items/item_tango#attribs
    - loc:DOTA_Tooltip_ability_item_tango_Description
  - text: Devour has Unit Target and DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE
      behavior.
    marks:
    - gamefile:items/item_tango#mechanics
  - text: Devour has 165 Cast range.
    marks:
    - gamefile:items/item_tango#mechanics
  - text: Consuming an Ironwood Tree doubles the heal duration.
    marks:
    - loc:DOTA_Tooltip_ability_item_tango_Description
  - text: Devour can target an allied hero to give them one Tango.
    marks:
    - loc:DOTA_Tooltip_ability_item_tango_Description
  - text: Tree Range is %abilitycastrange%.
    marks:
    - loc:DOTA_Tooltip_ability_item_tango_Description
---

# Tango

Tango is a consumable item; Devour grants Health Regen for a Buff Duration, and the item has Tooltip Charges. [gamefile:items/item_tango#cost] [gamefile:items/item_tango#attribs] [loc:DOTA_Tooltip_ability_item_tango_Description]

## Cost

| Item | Cost |
|---|---:|
| Tango | 90 gold |

[gamefile:items/item_tango#cost]

## Stats

| Stat | Value |
|---|---:|
| Buff Duration | 16.0 |
| Health Regen | 7.0 |
| Tooltip Charges | 3 |

[gamefile:items/item_tango#attribs]

## Devour

| Property | Value |
|---|---|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE |
| Cast range | 165 |

[gamefile:items/item_tango#mechanics]

Devour consumes a target tree to grant Health Regen. Consuming an Ironwood Tree doubles the heal duration. It can also target an allied hero to give them one Tango.

| Stat | Value |
|---|---|
| Tree Range | %abilitycastrange% |

[loc:DOTA_Tooltip_ability_item_tango_Description]

*Forage to survive on the battlefield.* [loc:DOTA_Tooltip_ability_item_tango_Lore]