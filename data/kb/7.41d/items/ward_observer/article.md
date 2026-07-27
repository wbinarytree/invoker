---
title: Observer Ward
kind: item
patch: 7.41d
card:
  entity: ward_observer
  sentences:
  - text: Observer Ward is a 0-gold consumable whose Plant use creates an invisible
      Observer Ward that grants the user’s team ground vision with 1600 vision range
      for 6 minutes.
    marks:
    - gamefile:items/item_ward_observer#cost
    - loc:DOTA_Tooltip_ability_item_ward_observer_Description
    - gamefile:items/item_ward_observer#attribs
  - text: The ward has 200 health.
    marks:
    - gamefile:items/item_ward_observer#attribs
  - text: Plant is Point Target and AOE, with optional unit targeting and associated-consumable
      suppression.
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