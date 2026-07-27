---
title: Sentry Ward
kind: item
patch: 7.41d
card:
  entity: ward_sentry
  sentences:
  - text: Sentry Ward is a 50-gold consumable whose Plant use creates an invisible
      watcher with 200 Health and a 420 lifetime that provides 1050-range True Sight
      within existing allied vision, has 0 Vision Range, and grants no ground vision.
    marks:
    - gamefile:items/item_ward_sentry#cost
    - loc:DOTA_Tooltip_ability_item_ward_sentry_Description
    - gamefile:items/item_ward_sentry#attribs
  - text: The build formula is Sentry Ward (50 gold) into Observer and Sentry Wards.
    marks:
    - gamefile:items/item_ward_sentry#cost
    - gamefile:items/item_ward_sentry#components
  - text: Its Duration Minutes Tooltip is 7.
    marks:
    - gamefile:items/item_ward_sentry#attribs
  - text: Its behavior is Point Target, AOE, DOTA_ABILITY_BEHAVIOR_OPTIONAL_UNIT_TARGET,
      and DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE.
    marks:
    - gamefile:items/item_ward_sentry#mechanics
  - text: Its cast range is 500.
    marks:
    - gamefile:items/item_ward_sentry#mechanics
  - text: Its cooldown is 1.0.
    marks:
    - gamefile:items/item_ward_sentry#mechanics
  - text: True Sight reveals invisible enemy units and wards within existing allied
      vision.
    marks:
    - loc:DOTA_Tooltip_ability_item_ward_sentry_Description
  - text: Holding Control gives the Sentry Ward to an allied hero.
    marks:
    - loc:DOTA_Tooltip_ability_item_ward_sentry_Description
---

# Sentry Ward

Sentry Ward is a consumable item whose Plant use creates an invisible watcher that provides True Sight to existing allied vision and grants no ground vision. [gamefile:items/item_ward_sentry#cost] [loc:DOTA_Tooltip_ability_item_ward_sentry_Description]

## Cost and build

| Entry | Gold cost |
|---|---:|
| Sentry Ward | 50 gold |
| Builds into: Observer and Sentry Wards | 50 gold |

[gamefile:items/item_ward_sentry#cost] [gamefile:items/item_ward_sentry#components]

## Attributes

| Stat | Value |
|---|---:|
| Duration Minutes Tooltip | 7 |
| Health | 200 |
| Lifetime | 420 |
| True Sight Range | 1050 |
| Vision Range | 0 |

[gamefile:items/item_ward_sentry#attribs]

## Mechanics

| Stat | Value |
|---|---|
| Behavior | Point Target, AOE, DOTA_ABILITY_BEHAVIOR_OPTIONAL_UNIT_TARGET, DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE |
| Cast range | 500 |
| Cooldown | 1.0 |

[gamefile:items/item_ward_sentry#mechanics]

True Sight allows invisible enemy units and wards within existing allied vision to be seen. Holding Control gives the Sentry Ward to an allied hero. [loc:DOTA_Tooltip_ability_item_ward_sentry_Description]

*Originally grown in the garden of a fearful king.* [loc:DOTA_Tooltip_ability_item_ward_sentry_Lore]