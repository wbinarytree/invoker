---
title: Mana Break
kind: concept
patch: 7.41d
card:
  entity: mana_break
  sentences:
  - text: Mana Break is an attack effect that burns a target’s mana and deals additional
      physical damage based on the mana burned; its talent version burns 15/20/25/35/40
      mana per hit and converts 80% of burned mana into damage.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669
    - corpus:liquipedia_dota2/mana_break@2257669#Talents
  - text: It can be gained through items, passive abilities, or talents, and every
      source has the `MODIFIER_PROPERTY_PROCATTACK_FEEDBACK` flag.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669
  - text: Sources apply mana burn first, followed by attack damage and burned mana
      as damage in a single instance.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669
  - text: The general Mana Break damage instance is fully considered by lifesteal
      but not by critical strike or cleave.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669
  - text: Mana-loss manipulation can reduce mana burned without reducing Mana Break’s
      damage, while mana-draining effects restore the same amount even when the target
      loses less mana.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669
  - text: All Mana Break sources stack additively.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669#Stacking
  - text: Listed sources are Anti-Mage, Diffusal Blade, Disperser, Demonic Warrior
      from Book of the Dead, and Demonic Warrior from Underlord.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669#Sources
  - text: The talent’s burned-mana damage is a conditional attack-damage bonus added
      directly to attack damage but not displayed in the HUD.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669#Talents
  - text: This talent bonus is considered by lifesteal and cleave, excluded from critical
      strike, and reducible only by flat reductions such as damage block.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669#Talents
  - text: Percentage-based attack-damage bonuses and reductions do not affect the
      talent bonus.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669#Talents
  - text: Against units with enough mana, the talent effectively increases the hero’s
      and their illusions’ attack damage by 12/16/20/28/32 (6.4/8/8/8/8).
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669#Talents
  - text: The talent does not work against allied or debuff-immune units.
    marks:
    - corpus:liquipedia_dota2/mana_break@2257669#Talents
---

# Mana Break

## Mechanics

Mana Break allows an attacking unit to burn part of its target’s mana and deal additional physical damage based on the mana burned. It can be gained through items, passive abilities, or talents, and every source has the `MODIFIER_PROPERTY_PROCATTACK_FEEDBACK` flag. Sources apply mana burn first, followed by the attack damage and burned mana as damage in a single instance. This damage is fully considered by lifesteal, but not by critical strike or cleave sources. Mana-loss manipulation can reduce the mana burned without reducing Mana Break’s damage; mana-draining effects likewise restore the same amount even when the target loses less mana. [corpus:liquipedia_dota2/mana_break@2257669]

## Stacking

All Mana Break sources stack additively. [corpus:liquipedia_dota2/mana_break@2257669#Stacking]

## Sources

| Source | Ability |
|---|---|
| Anti-Mage | Mana Break [corpus:liquipedia_dota2/mana_break@2257669#Sources] |
| Diffusal Blade | Manabreak [corpus:liquipedia_dota2/mana_break@2257669#Sources] |
| Disperser | Manabreak [corpus:liquipedia_dota2/mana_break@2257669#Sources] |
| Demonic Warrior (Book of the Dead) | Mana Break [corpus:liquipedia_dota2/mana_break@2257669#Sources] |
| Demonic Warrior (Underlord) | Mana Break [corpus:liquipedia_dota2/mana_break@2257669#Sources] |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/mana_break@2257669#Sources] |
| 2a | Requires Aghanim's Scepter. [corpus:liquipedia_dota2/mana_break@2257669#Sources] |
| 2b | Requires Aghanim's Shard. [corpus:liquipedia_dota2/mana_break@2257669#Sources] |

## Talent

| Property | Value |
|---|---|
| Ability | Passive [corpus:liquipedia_dota2/mana_break@2257669#Talents] |
| Affects | Enemies [corpus:liquipedia_dota2/mana_break@2257669#Talents] |
| Damage | Physical [corpus:liquipedia_dota2/mana_break@2257669#Talents] |
| Mana Burned per Hit | 15/20/25/35/40 [corpus:liquipedia_dota2/mana_break@2257669#Talents] |
| Burned Mana as Damage | 80% [corpus:liquipedia_dota2/mana_break@2257669#Talents] |
| Following values exist | 15/20/25/35/40 (8/10/10/10/10) [corpus:liquipedia_dota2/mana_break@2257669#Talents] |

The talent gives the hero’s attacks Mana Break, causing them to burn the target’s mana and deal damage based on the amount burned. Burned mana as damage is a conditional attack-damage bonus. Although this bonus is not displayed in the HUD, it is directly added to the hero’s attack damage. It is not considered by critical strike, but is considered by lifesteal and cleave and can be reduced only by flat reductions, such as damage block. Because it is bonus attack damage, percentage-based attack-damage bonuses and reductions do not affect it. [corpus:liquipedia_dota2/mana_break@2257669#Talents]

Against units with enough mana to burn, it effectively increases the hero’s and their illusions’ attack damage by 12/16/20/28/32 (6.4/8/8/8/8). [corpus:liquipedia_dota2/mana_break@2257669#Talents]

The talent applies mana burn first, then attack damage, then the burned mana as damage. It does not work when attacking allied units, fully stacks with other Mana Break sources, and does not affect debuff-immune units at all. [corpus:liquipedia_dota2/mana_break@2257669#Talents]

In Ability Draft, the talent is available and is not bound to any ability. Its hidden modifier is `modifier_special_bonus_mana_break`. Heroes can have a talent that grants them Mana Break. [corpus:liquipedia_dota2/mana_break@2257669#Talents]