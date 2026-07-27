---
title: Observer Ward
kind: item
patch: 7.41d
card:
  entity: ward_observer
  sentences:
  - text: Observer Ward is a consumable item costing 0 gold whose Plant use creates
      an invisible ward with 200 health, Lifetime 360, Duration Minutes Tooltip 6,
      and 1600 ground vision range for the user’s team.
    marks:
    - gamefile:items/item_ward_observer#cost
    - loc:DOTA_Tooltip_ability_item_ward_observer_Description
    - gamefile:items/item_ward_observer#attribs
  - text: Plant has Point Target, AOE, DOTA_ABILITY_BEHAVIOR_OPTIONAL_UNIT_TARGET,
      and DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE behavior.
    marks:
    - gamefile:items/item_ward_observer#mechanics
  - text: Plant has 500 cast range.
    marks:
    - gamefile:items/item_ward_observer#mechanics
  - text: Plant has a 1.0 cooldown.
    marks:
    - gamefile:items/item_ward_observer#mechanics
  - text: Holding Control gives an Observer Ward to an allied hero.
    marks:
    - loc:DOTA_Tooltip_ability_item_ward_observer_Description
  - text: 'Build formula: Observer Ward (0 gold); builds into Observer and Sentry
      Wards.'
    marks:
    - gamefile:items/item_ward_observer#cost
    - gamefile:items/item_ward_observer#components
  - text: A form of half-sentient plant, often cultivated by apprentice wizards.
    marks:
    - loc:DOTA_Tooltip_ability_item_ward_observer_Lore
---

# Observer Ward

Observer Ward is a consumable item whose Plant use creates an invisible Observer Ward that gives ground vision to the user’s team. [gamefile:items/item_ward_observer#cost] [loc:DOTA_Tooltip_ability_item_ward_observer_Description]

## Attributes

| Attribute | Value |
|---|---:|
| Duration Minutes Tooltip | 6 |
| Health | 200 |
| Lifetime | 360 |
| Vision Range Tooltip | 1600 |

[gamefile:items/item_ward_observer#attribs]

## Plant

| Property | Value |
|---|---|
| Behavior | Point Target, AOE, DOTA_ABILITY_BEHAVIOR_OPTIONAL_UNIT_TARGET, DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE |
| Cast range | 500 |
| Cooldown | 1.0 |

[gamefile:items/item_ward_observer#mechanics]

Holding Control gives an Observer Ward to an allied hero. [loc:DOTA_Tooltip_ability_item_ward_observer_Description]

## Components

| Build formula | Gold cost |
|---|---:|
| Observer Ward | 0 gold |
| **Builds into:** Observer and Sentry Wards | 50 gold |

[gamefile:items/item_ward_observer#cost] [gamefile:items/item_ward_observer#components]

*A form of half-sentient plant, often cultivated by apprentice wizards.* [loc:DOTA_Tooltip_ability_item_ward_observer_Lore]