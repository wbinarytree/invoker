---
title: Urn of Shadows
kind: item
patch: 7.41d
card:
  entity: urn_of_shadows
  sentences:
  - text: Urn of Shadows is a rare 825-gold item that grants 2 All Attributes, 2 Armor,
      and 1.25 Mana Regeneration; its Soul Release active provides 30 health regeneration
      to allies or deals 25 damage per second to enemies for 8.0 seconds.
    marks:
    - gamefile:items/item_urn_of_shadows#cost
    - gamefile:items/item_urn_of_shadows#attribs
    - loc:DOTA_Tooltip_ability_item_urn_of_shadows_Description
  - text: Soul Release is Unit Target and has DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES.
    marks:
    - gamefile:items/item_urn_of_shadows#mechanics
  - text: Soul Release has 750 cast range.
    marks:
    - gamefile:items/item_urn_of_shadows#mechanics
  - text: Soul Release has a 10.0-second cooldown.
    marks:
    - gamefile:items/item_urn_of_shadows#mechanics
  - text: Soul Release is dispellable.
    marks:
    - gamefile:items/item_urn_of_shadows#mechanics
  - text: The item starts with 2 charges.
    marks:
    - gamefile:items/item_urn_of_shadows#attribs
  - text: It gains 1 additional charge whenever an enemy hero dies within 1500 range.
    marks:
    - gamefile:items/item_urn_of_shadows#attribs
    - loc:DOTA_Tooltip_ability_item_urn_of_shadows_Description
  - text: It is built from Sage's Mask for 175 gold, Ring of Protection for 175 gold,
      Circlet for 155 gold, and a Recipe for 320 gold; it builds into Essence Distiller
      and Spirit Vessel.
    marks:
    - gamefile:items/item_urn_of_shadows#components
---

Urn of Shadows is a rare item that grants All Attributes, Armor, and Mana Regeneration and has the Soul Release active. [gamefile:items/item_urn_of_shadows#cost] [gamefile:items/item_urn_of_shadows#attribs] [loc:DOTA_Tooltip_ability_item_urn_of_shadows_Description]

## Cost

| Stat | Value |
|---|---:|
| Cost | 825 gold |

[gamefile:items/item_urn_of_shadows#cost]

## Stats

| Stat | Value |
|---|---:|
| ALL ATTRIBUTES | 2 |
| ARMOR | 2 |
| DURATION | 8.0 |
| MANA REGENERATION | 1.25 |
| SOUL ADDITIONAL CHARGES | 1 |
| SOUL DAMAGE AMOUNT | 25 |
| SOUL HEAL AMOUNT | 30 |
| SOUL INITIAL CHARGE | 2 |
| SOUL RADIUS | 1500 |

[gamefile:items/item_urn_of_shadows#attribs]

## Soul Release

| Property | Value |
|---|---|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES |
| Dispellable | Yes |
| Cast range | 750 |
| Cooldown | 10.0 |

[gamefile:items/item_urn_of_shadows#mechanics]

Soul Release provides health regeneration to allied targets and deals damage per second to enemy targets. Its effect has a fixed duration, and the item gains charges whenever an enemy hero dies within range. [loc:DOTA_Tooltip_ability_item_urn_of_shadows_Description]

## Components

| Role | Item | Gold cost |
|---|---|---:|
| Component | Sage's Mask | 175 gold |
| Component | Ring of Protection | 175 gold |
| Component | Circlet | 155 gold |
| Recipe | Recipe | 320 gold |
| Builds into | Essence Distiller | 1775 gold |
| Builds into | Spirit Vessel | 2725 gold |

[gamefile:items/item_urn_of_shadows#components]

*Contains the ashes of powerful demons.* [loc:DOTA_Tooltip_ability_item_urn_of_shadows_Lore]