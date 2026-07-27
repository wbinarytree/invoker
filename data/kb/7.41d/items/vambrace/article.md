---
title: Vambrace
kind: item
patch: 7.41d
card:
  entity: vambrace
  sentences:
  - text: Vambrace is a common 0-gold item granting 15 Bonus Attack Speed, 10 Bonus
      Magic Resistance, 10 Bonus Primary Stat, 4 Bonus Secondary Stat, and 8 Bonus
      Spell Amp; Switch Attributes selects Strength, Agility, or Intelligence to receive
      the primary-stat bonus while the other two receive the secondary-stat bonus.
    marks:
    - gamefile:items/item_vambrace#cost
    - gamefile:items/item_vambrace#attribs
    - loc:DOTA_Tooltip_ability_item_vambrace_Description
  - text: Switch Attributes has Immediate, No Target behavior.
    marks:
    - gamefile:items/item_vambrace#mechanics
---

# Vambrace

Vambrace is a common item [gamefile:items/item_vambrace#cost] with Bonus Attack Speed, Bonus Magic Resistance, Bonus Primary Stat, Bonus Secondary Stat, and Bonus Spell Amp [gamefile:items/item_vambrace#attribs], plus the Switch Attributes active. [loc:DOTA_Tooltip_ability_item_vambrace_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Vambrace | 0 gold |

[gamefile:items/item_vambrace#cost]

## Stats

| Stat | Value |
|---|---:|
| Bonus Attack Speed | 15 |
| Bonus Magic Resistance | 10 |
| Bonus Primary Stat | 10 |
| Bonus Secondary Stat | 4 |
| Bonus Spell Amp | 8 |

[gamefile:items/item_vambrace#attribs]

## Switch Attributes

Switch Attributes has Immediate, No Target behavior. [gamefile:items/item_vambrace#mechanics]

Activating it switches the active attribute between Strength, Agility, and Intelligence. The selected attribute receives Bonus Primary Stat, while the other two receive Bonus Secondary Stat. [loc:DOTA_Tooltip_ability_item_vambrace_Description] [gamefile:items/item_vambrace#attribs]

*The coveted treasure that divided the heirs of Queen Raiya upon her death, resulting in the eventual downfall of her kingdom.* [loc:DOTA_Tooltip_ability_item_vambrace_Lore]