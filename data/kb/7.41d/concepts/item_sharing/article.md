---
title: Item Sharing
kind: concept
patch: 7.41d
card:
  entity: item_sharing
  sentences:
  - text: Item sharing is the ownership system under which almost every item can be
      dropped for another hero or given to an ally, while most items can be used,
      sold, or upgraded only by their purchasing hero and are muted in another hero’s
      inventory.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655
  - text: Completely shareable items include Dust of Appearance (80), Healing Lotus
      (0), Great Healing Lotus (0), Greater Healing Lotus (0), Block of Cheese (2),
      Observer Ward (0), Sentry Ward (50), Observer and Sentry Wards, Smoke of Deceit
      (50), and Tango (Shared).
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable
  - text: A viewed but unselected Neutral Token may be shared, and the receiving ally
      gets a unique set of choices.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable
  - text: Completely shareable Roshan items are Cheese, Aghanim's Blessing - Roshan,
      Refresher Shard, and Roshan's Banner.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Roshan_Items
  - text: Partially shareable items include Bottle (675), Healing Salve (100), Enchanted
      Mango (65), Divine Rapier (5600), Gem of True Sight (900), and Town Portal Scroll
      (100).
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable
  - text: Gem of True Sight drops on death and can be used by enemies.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655
  - text: Divine Rapier is unshareable until the owner’s enemy team picks it up; anyone
      can then use it, but it can be dropped only when its current owner dies.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable
  - text: Tome of Knowledge’s cooldown is bound to its user.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions
  - text: Using an item places every item of the same type in the user’s inventory,
      backpack, and stash on cooldown regardless of ownership or shareability.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions
  - text: A received item is placed on cooldown if that item type would be on cooldown
      for the receiving hero.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions
  - text: An item retains its cooldown when given to a hero who has not used it.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions
  - text: Items merging into an existing stack assume the cooldown of the stack that
      was first in the inventory.
    marks:
    - corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions
---

# Item Sharing

## Ownership and use

Almost every item can be dropped for another hero—including an enemy—to take, or given to an ally. However, most items cannot be shared: the purchasing hero owns the item and is the only hero who can use, sell, or upgrade it. The item is muted in another hero’s inventory. [corpus:liquipedia_dota2/item_sharing@2222655]

Most consumables are completely shareable because they cannot be upgraded and grant only temporary effects. Non-owners can use them, allowing support heroes to purchase items for teammates. Some permanent items are partially shareable: another hero can benefit from their effects while holding them but cannot sell or upgrade them. Divine Rapier and Gem of True Sight drop on death and can be used by enemies. Certain items are disabled on the Animal Courier to prevent abuse. [corpus:liquipedia_dota2/item_sharing@2222655]

## Completely shareable items

| Source listing |
|---|
| Dust of Appearance (80 ) [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |
| Healing Lotus (0 ) [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |
| Great Healing Lotus (0 ) [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |
| Greater Healing Lotus (0 ) [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |
| Block of Cheese (2 ) [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |
| Observer Ward (0 ) [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |
| Sentry Ward (50 ) [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |
| Observer and Sentry Wards [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |
| Smoke of Deceit (50 ) [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |
| Tango (Shared) [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable] |

A Neutral Token may be shared after its holder has viewed the available neutral items, provided they have not selected one. The receiving ally receives their own unique set of choices. [corpus:liquipedia_dota2/item_sharing@2222655#Completely_Shareable]

### Roshan items

| Completely shareable item |
|---|
| Cheese [corpus:liquipedia_dota2/item_sharing@2222655#Roshan_Items] |
| Aghanim's Blessing - Roshan [corpus:liquipedia_dota2/item_sharing@2222655#Roshan_Items] |
| Refresher Shard [corpus:liquipedia_dota2/item_sharing@2222655#Roshan_Items] |
| Roshan's Banner [corpus:liquipedia_dota2/item_sharing@2222655#Roshan_Items] |

## Partially shareable items

| Source listing |
|---|
| Bottle (675 ) [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable] |
| Healing Salve (100 ) [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable] |
| Enchanted Mango (65 ) [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable] |
| Divine Rapier (5600 ) [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable] |
| Gem of True Sight (900 ) [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable] |
| Town Portal Scroll (100 ) [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable] |

A Bottle containing a rune cannot be dropped. [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable]

Healing Salve and Enchanted Mango are shareable when dug up with Trusty Shovel. Buying the same item from a store while carrying a dug-up copy mixes them, allowing both items to be transferred at once. [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable]

Divine Rapier acts as an unshareable item until picked up by the item owner’s enemy team. It can then be used by anyone, but can only be dropped after its current owner dies. [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable]

Town Portal Scroll can be dropped only through the main inventory, which is possible only through Couriers. [corpus:liquipedia_dota2/item_sharing@2222655#Partially_Shareable]

## Cooldown interactions

Tome of Knowledge’s cooldown is bound to its user. Other items follow these rules: [corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions]

- Using an item places every item of the same type in the user’s inventory, backpack, and stash on cooldown, regardless of ownership or shareability. For example, if the user has 2 stacks of Dust of Appearance—one their own and one belonging to a teammate—using either stack puts both on cooldown. [corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions]
- When a hero receives an item type that would be on cooldown for them, the received item is placed on cooldown regardless of ownership or shareability. For example, if the hero has 2 Dust of Appearance, uses 1, and then receives an unused Dust from a teammate, both are on cooldown. [corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions]
- An item retains its cooldown when given to a hero who has not used it. For example, if a teammate has 2 Dust of Appearance, uses one Dust of Appearance, and gives the rest to another hero, it remains on cooldown for that hero. [corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions]
- Items merging into an existing stack assume the cooldown of the stack that was first in the inventory. For example, after buying a stack of Dust of Appearance, giving it to a teammate who uses it, and having that teammate drop it, buying another stack before picking up the first produces a merged stack that is not on cooldown. Picking up the first Dust before buying more instead leaves it on cooldown, and any additional purchased Dust merges with that stack and is also on cooldown. [corpus:liquipedia_dota2/item_sharing@2222655#Cooldown_interactions]