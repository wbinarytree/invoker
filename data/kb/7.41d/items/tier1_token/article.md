---
title: Tier 1 Token
kind: item
patch: 7.41d
card:
  entity: tier1_token
  sentences:
  - text: Tier 1 Token is an item with No Target behavior whose activation redeems
      a Tier 1 Neutral Item.
    marks:
    - gamefile:items/item_tier1_token#mechanics
    - loc:DOTA_Tooltip_ability_item_tier1_token_Description
  - text: The resulting neutral item isn't shareable.
    marks:
    - loc:DOTA_Tooltip_ability_item_tier1_token_Description
  - text: A hero can only redeem a single token per tier.
    marks:
    - loc:DOTA_Tooltip_ability_item_tier1_token_Description
---

# Tier 1 Token

Tier 1 Token is an item with No Target behavior whose activation redeems a Tier 1 Neutral Item. [gamefile:items/item_tier1_token#cost] [gamefile:items/item_tier1_token#mechanics] [loc:DOTA_Tooltip_ability_item_tier1_token_Description]

## Mechanics

| Property | Value |
|---|---|
| Behavior | No Target |

[gamefile:items/item_tier1_token#mechanics]

The resulting neutral item isn't shareable, and a hero can only redeem a single token per tier. [loc:DOTA_Tooltip_ability_item_tier1_token_Description]