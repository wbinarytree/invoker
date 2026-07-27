---
title: Divine Rapier
kind: item
patch: 7.41d
card:
  entity: rapier
  sentences:
  - text: Divine Rapier is a 5600-gold epic item whose Transmute toggle switches between
      25% bonus spell amplification and 250 bonus attack damage.
    marks:
    - gamefile:items/item_rapier#cost
    - loc:DOTA_Tooltip_ability_item_rapier_Description
    - gamefile:items/item_rapier#mechanics
    - gamefile:items/item_rapier#attribs
  - text: Its build formula is Sacred Relic (3400 gold) + Demon Edge (2200 gold) =
      Divine Rapier (5600 gold).
    marks:
    - gamefile:items/item_rapier#components
    - gamefile:items/item_rapier#cost
  - text: Its DAMAGE stat is 100.
    marks:
    - gamefile:items/item_rapier#attribs
  - text: The item has a cooldown of 6.
    marks:
    - gamefile:items/item_rapier#mechanics
  - text: Everlasting causes Divine Rapier to drop on death.
    marks:
    - loc:DOTA_Tooltip_ability_item_rapier_Description
  - text: Everlasting prevents Divine Rapier from being destroyed.
    marks:
    - loc:DOTA_Tooltip_ability_item_rapier_Description
  - text: If an ally of its owner picks it up, it remains unusable until returned
      to the owner.
    marks:
    - loc:DOTA_Tooltip_ability_item_rapier_Description
  - text: If an enemy picks it up and is killed, it becomes immediately usable by
      anybody.
    marks:
    - loc:DOTA_Tooltip_ability_item_rapier_Description
  - text: A dropped Divine Rapier cannot be picked up by a courier.
    marks:
    - loc:DOTA_Tooltip_ability_item_rapier_Description
---

# Divine Rapier

Divine Rapier is an epic item that grants either bonus spell amplification or bonus attack damage. [gamefile:items/item_rapier#cost] [loc:DOTA_Tooltip_ability_item_rapier_Description]

## Components

| Component | Gold cost |
|---|---:|
| Sacred Relic | 3400 gold |
| Demon Edge | 2200 gold |
| **Divine Rapier** | **5600 gold** |

[gamefile:items/item_rapier#components] [gamefile:items/item_rapier#cost]

## Stats

| Stat | Value |
|---|---:|
| BONUS DAMAGE | 250 |
| DAMAGE | 100 |
| BONUS SPELL AMP | 25% |

[gamefile:items/item_rapier#attribs]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Toggle |
| Cooldown | 6 |

[gamefile:items/item_rapier#mechanics]

Transmute switches between the bonus spell amplification and bonus attack damage modes. Everlasting causes Divine Rapier to drop on death and prevents it from being destroyed. If an ally of its owner picks it up, it remains unusable until returned to the owner; if an enemy picks it up and is killed, it becomes immediately usable by anybody. A dropped Divine Rapier cannot be picked up by a courier. [loc:DOTA_Tooltip_ability_item_rapier_Description]

*So powerful, it cannot have a single owner.* [loc:DOTA_Tooltip_ability_item_rapier_Lore]