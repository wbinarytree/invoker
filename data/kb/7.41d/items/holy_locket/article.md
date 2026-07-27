---
title: Holy Locket
kind: item
patch: 7.41d
card:
  entity: holy_locket
  sentences:
  - text: Holy Locket is a rare 2250-gold item whose Energy Charge targets an allied
      unit, holds up to 25 charges, restores 17 health and 15 mana per charge, and
      provides 15% Incoming Heal Increase Active for an Active Buff Duration of 4.0,
      while Holy Blessing increases heals provided by 10%.
    marks:
    - gamefile:items/item_holy_locket#cost
    - gamefile:items/item_holy_locket#attribs
    - loc:DOTA_Tooltip_ability_item_holy_locket_Description
  - text: Its build formula is Magic Wand (460 gold) + Crown (450 gold) + Recipe (1340
      gold).
    marks:
    - gamefile:items/item_holy_locket#components
  - text: It grants 7 All Attributes, 0 Bonus Health, and 0 Bonus Mana.
    marks:
    - gamefile:items/item_holy_locket#attribs
  - text: It automatically gains charges on its Charge Gain Timer of 10 and whenever
      a visible enemy within its Charge Radius of 1200 uses an ability.
    marks:
    - gamefile:items/item_holy_locket#attribs
    - loc:DOTA_Tooltip_ability_item_holy_locket_Description
  - text: Its use behavior is Unit Target, Immediate, and DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK,
      with 600 cast range and 0.0 cooldown.
    marks:
    - gamefile:items/item_holy_locket#mechanics
  - text: Its Use Cooldown stat is 13.
    marks:
    - gamefile:items/item_holy_locket#attribs
  - text: A prized relic long thought lost forever in a failed crusade.
    marks:
    - loc:DOTA_Tooltip_ability_item_holy_locket_Lore
---

# Holy Locket

Holy Locket is a rare item with All Attributes, Bonus Health, Bonus Mana, Energy Charge, and Holy Blessing, affecting incoming Heal Amplification, health restoration, mana restoration, and heals you provide. [gamefile:items/item_holy_locket#cost] [gamefile:items/item_holy_locket#attribs] [loc:DOTA_Tooltip_ability_item_holy_locket_Description]

## Components

| Component | Gold cost |
|---|---:|
| Magic Wand | 460 gold |
| Crown | 450 gold |
| Recipe | 1340 gold |
| **Holy Locket** | **2250 gold** |

[gamefile:items/item_holy_locket#components] [gamefile:items/item_holy_locket#cost]

## Stats

| Stat | Value |
|---|---:|
| Active Buff Duration | 4.0 |
| All Attributes | 7 |
| Bonus Health | 0 |
| Bonus Mana | 0 |
| Charge Gain Timer | 10 |
| Charge Radius | 1200 |
| Heal Increase Passive | 10% |
| Health Restore per Charge | 17 |
| Incoming Heal Increase Active | 15% |
| Mana Restore per Charge | 15 |
| Max Charges | 25 |
| Use Cooldown | 13 |

[gamefile:items/item_holy_locket#attribs]

| Use property | Value |
|---|---|
| Behavior | Unit Target, Immediate, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Cast range | 600 |
| Cooldown | 0.0 |

[gamefile:items/item_holy_locket#mechanics]

## Effects

**Energy Charge** targets an allied unit, increases its incoming Heal Amplification for the active duration, and instantly restores health and mana for each stored charge. Holy Locket automatically gains charges on its charge timer and whenever a visible enemy within its charge radius uses an ability. [loc:DOTA_Tooltip_ability_item_holy_locket_Description]

**Holy Blessing** amplifies heals provided by the holder. [loc:DOTA_Tooltip_ability_item_holy_locket_Description]

*A prized relic long thought lost forever in a failed crusade.* [loc:DOTA_Tooltip_ability_item_holy_locket_Lore]