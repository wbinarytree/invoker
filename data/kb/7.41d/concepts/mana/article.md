---
title: Mana
kind: concept
patch: 7.41d
card:
  entity: mana
  sentences:
  - text: Mana (MP, or mana points) is the magic-power pool units spend on most active
      and some passive abilities; every hero has an unalterable 75MP base pool that
      sets a 75MP floor for maximum mana and gains 12MP per intelligence point.
    marks:
    - corpus:liquipedia_dota2/mana@2365137
  - text: Total hero mana is defined as `Base Mana + (12 × Intelligence) ± Flat Bonus
      Mana Values × % Bonus Current/Max Mana Values`.
    marks:
    - corpus:liquipedia_dota2/mana@2365137
  - text: The HUD’s blue mana bar shows current and maximum mana, with visible values
      rounded up from decimal totals.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#HUD_Mana_bar
  - text: Mana regeneration is the mana regained each second and appears with a `+`
      sign at the right of the mana bar.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#Mana_Regeneration
  - text: Restoration increases current mana only up to maximum mana; bursts apply
      once, while restoration over time uses multiple instances.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#Restoring_Mana
  - text: Burning removes mana and deals damage based on the amount removed, draining
      transfers stolen mana, and simple removal has no additional effect.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#Removing_Mana
  - text: Setting mana directly is neither restoration nor removal and cannot exceed
      maximum mana.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#Setting_Mana
  - text: Apart from intelligence and raw item bonuses, very few abilities alter maximum
      mana.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#Maximum_Mana_Affecting_Abilities
  - text: Equipped items can add maximum mana through intelligence, a flat bonus,
      or both while preserving the current mana percentage.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#Items
  - text: Mana restore manipulation amplifies or reduces mana restoration from every
      classified mana-restoring ability.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#Mana_Restore_Manipulation
  - text: Mana-loss manipulation reduces ability costs and mana removed, burned, or
      drained, with multiple reductions stacking multiplicatively.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#Mana_Loss_Manipulation
  - text: On-restore effects trigger from restoration and regeneration but not from
      other mana gains such as setting mana.
    marks:
    - corpus:liquipedia_dota2/mana@2365137#On-restore_Effects
---

# Mana

## Overview

Mana, or MP—short for mana points—represents a unit’s magic power. It is the cost for most active abilities and some passive abilities. Every hero has an unalterable base mana pool of 75MP, so a hero’s maximum mana cannot fall below 75MP. Most non-hero units have a set mana pool only when they possess mana-requiring abilities, with a few exceptions; these set values cannot be altered.

Each intelligence point increases a hero’s mana by 12MP. Because every hero has intelligence growth per level, heroes gain mana as they level. Base intelligence cannot fall below 1, although negative bonus intelligence can produce 0 intelligence.

Total hero mana is defined as:

```text
Base Mana
+ (12 × Intelligence)
± Flat Bonus Mana Values
× % Bonus Current/Max Mana Values
```

[corpus:liquipedia_dota2/mana@2365137]

## Display

A unit’s mana is displayed in the HUD and, for some units, may also appear in the game world. Mana uses a blue bar, while the number on the right shows mana regeneration. [corpus:liquipedia_dota2/mana@2365137#Display]

### HUD mana bar

The selected unit’s mana appears in the HUD as a blue bar at the bottom of the screen. At the center of the bar, the left number is current mana and the right number is maximum mana. Actual total mana uses decimals, but the HUD always rounds the visible values up.

Mana regeneration is visible on every unit’s HUD mana bar. Although only one decimal is displayed, the underlying value uses more decimals and is rounded up for display. Enemy heroes’ and creep-heroes’ mana bars are not visible above their heads. [corpus:liquipedia_dota2/mana@2365137#HUD_Mana_bar]

### Over-head mana bar

Heroes and creep-heroes have a mana bar directly above their heads, below the health bar. A creep-hero receives this bar even when it has no mana pool; other units have no overhead mana bar.

There is only one type of mana bar. Mana bars have no lines like health bars and do not differ from one another. [corpus:liquipedia_dota2/mana@2365137#Over-head_Mana_bar]

## Modifying mana

Some heroes, neutral creeps, summoned units, and items have abilities that affect units’ current or maximum mana pools. [corpus:liquipedia_dota2/mana@2365137#Modifying_Mana]

### Restoring mana

Restoring mana increases a unit’s current mana, analogously to healing health, but cannot raise it beyond maximum mana. A burst restore supplies mana in one instance, while a restore over time divides the amount among multiple instances.

Restoration is independent of regeneration ticks, and its intervals can vary. Restored mana is not included in the regeneration number displayed on the mana bar.

| Mana-restoring source |
|---|
| Bane – Fiend's Grip |
| Invoker – E.M.P. |
| Io – Tether |
| Keeper of the Light – Chakra Magic |
| Lich – Sinister Gaze |
| Lion – Mana Drain |
| Medusa – Mystic Snake |
| Medusa – Cold Blooded |
| Outworld Destroyer – Essence Flux |
| Phoenix – Supernova |
| Pudge – Meat Hook |
| Pugna – Life Drain |
| Silencer – Glaives of Wisdom |
| Slark – Pounce |
| Slark – Essence Shift |
| Storm Spirit – Ball Lightning |
| Arcane Boots – Replenish |
| Arcane Ring – Replenish Mana |
| Bloodstone – Bloodpact |
| Cheese – Fondue |
| Enchanted Mango – Eat Mango |
| Eternal Shroud – Shroud |
| Guardian Greaves – Mend |
| Holy Locket – Energy Charge |
| Magic Stick – Energy Charge |
| Magic Wand – Energy Charge |
| Soul Ring – Sacrifice |
| Runes – Water |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/mana@2365137#Restoring_Mana]

### Removing mana

Most active abilities, some passive abilities, and item abilities require mana. Their mana cost appears at the bottom-left corner of the ability’s HUD icon and again in the bottom-left corner of its description. Most abilities have a fixed mana cost, but some costs are dynamic, including costs based on the mana pool or paid over time.

For offensive mana loss, *burning* removes mana and causes damage based on the amount removed; *draining* steals mana and transfers it to another unit; and simple *removal* removes mana without other effects.

| Mana-removing source |
|---|
| Bane – Fiend's Grip |
| Clockwerk – Power Cogs |
| Invoker – E.M.P. |
| Leshrac – Pulse Nova |
| Lich – Sinister Gaze |
| Lion – Mana Drain |
| Medusa – Mana Shield |
| Night Stalker – Hunter in the Night2b |
| Nyx Assassin – Vendetta |
| Satyr Mindstealer – Mana Burn |
| Storm Spirit – Ball Lightning |
| Winter Wyvern – Arctic Burn2a |
| Witch Doctor – Voodoo Restoration |
| Harpy Scout – Take Off |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/mana@2365137#Removing_Mana]

### Setting mana

Mana can be directly set to specified values rather than restored or removed. Such changes are not registered as restoration or removal and are ignored by effects that react to restored or removed mana. Setting mana cannot raise it beyond the unit’s maximum mana.

| Mana-setting source |
|---|
| Chen – Holy Persuasion |
| Soul Ring – Sacrifice |
| Timbersaw – Chakram |
| Timbersaw – Second Chakram |
| Weaver – Time Lapse |

[corpus:liquipedia_dota2/mana@2365137#Setting_Mana]

### Maximum-mana-affecting abilities

Apart from intelligence and raw item bonuses, very few abilities alter maximum mana. Intelligence-affecting sources are excluded from this list.

| Source | Values | Effect |
|---|---|---|
| Eye of the Vizier | Max Mana: -15% | Reduces the wielder’s maximum mana. |
| Null Talisman | Max Mana: 3% | — |
| Outworld Destroyer – Astral Imprisonment | Max Mana Stolen: 16%/18%/20%/22%<br>Duration: 30/40/50/60 | Steals part of the target hero’s maximum mana for the duration without increasing or reducing current mana. |
| Soul Ring – Sacrifice | Temporary Mana Bonus: 170<br>Duration: 10 | If the added mana would exceed the user’s current mana pool, maximum mana is temporarily increased by the exceeding amount. |

[corpus:liquipedia_dota2/mana@2365137#Maximum_Mana_Affecting_Abilities]

### Items

Many equipped items increase their owner’s maximum mana through intelligence, a flat bonus, or both. In each case, the current mana percentage remains unchanged. These effects are limited to the equipped item’s owner. [corpus:liquipedia_dota2/mana@2365137#Items]

#### Flat-rate and intelligence mana

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Aghanim's Scepter | 295 | 4200 | 14.24 |
| Bloodstone | 630 | 4700 | 7.46 |
| Crella's Crozier | 522 | 4800 | 9.2 |
| Essence Distiller | 186 | 1775 | 9.54 |
| Gleipnir | 344 | 4650 | 13.52 |
| Khanda | 546 | 5600 | 10.26 |
| Null Talisman | Expression error: Unexpected < operator. | 505 | Expression error: Unexpected < operator. |

Values do not include portions from actives or auras. [corpus:liquipedia_dota2/mana@2365137#Items]

#### Flat-rate mana

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Aeon Disk | 300 | 3000 | 10 |
| Aether Lens | 300 | 2275 | 7.58 |
| Arcane Boots | 125 | 1500 | 12 |
| Energy Booster | 250 | 800 | 3.2 |
| Greedy Enchantment | 0.8 | N/A | N/A |
| Guardian Greaves | 150 | 4450 | 29.67 |
| Lotus Orb | 250 | 3850 | 15.4 |
| Octarine Core | 450 | 4900 | 10.89 |
| Pavise | 175 | 1350 | 7.71 |
| Point Booster | 175 | 1200 | 6.86 |
| Quickened Enchantment | 0 | N/A | N/A |
| Solar Crest | 200 | 2575 | 12.88 |
| Soul Booster | 425 | 3000 | 7.06 |
| Wizard Hat | 125 | 250 | 2 |

Values do not include portions from actives or auras. [corpus:liquipedia_dota2/mana@2365137#Items]

#### Intelligence mana

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Arcane Blink | 300 | 6800 | 22.67 |
| Bloodthorn | 300 | 6400 | 21.33 |
| Bracer | 24 | 505 | 21.04 |
| Circlet | 24 | 155 | 6.46 |
| Consecrated Wraps | 60 | 2600 | 43.33 |
| Crown | 48 | 450 | 9.38 |
| Crude Enchantment | Expression error: Unexpected < operator. | N/A | N/A |
| Diadem | 72 | 1000 | 13.89 |
| Diffusal Blade | 120 | 2500 | 20.83 |
| Disperser | 120 | 6100 | 50.83 |
| Ethereal Blade | 288 | 5200 | 18.06 |
| Eul's Scepter of Divinity | 120 | 2600 | 21.67 |
| Eye of Skadi | 420 | 5900 | 14.05 |
| Force Staff | 120 | 2200 | 18.33 |
| Ghost Scepter | 60 | 1500 | 25 |
| Harpoon | 120 | 4700 | 39.17 |
| Helm of the Dominator | 72 | 2550 | 35.42 |
| Helm of the Overlord | 252 | 5650 | 22.42 |
| Holy Locket | 84 | 2250 | 26.79 |
| Hurricane Pike | 180 | 4450 | 24.72 |
| Iron Branch | 12 | 55 | 4.58 |
| Kaya | 192 | 2100 | 10.94 |
| Kaya and Sange | 192 | 4200 | 21.88 |
| Linken's Sphere | 192 | 4800 | 25 |
| Magic Wand | 36 | 460 | 12.78 |
| Manta Style | 120 | 4650 | 38.75 |
| Mantle of Intelligence | 36 | 140 | 3.89 |
| Meteor Hammer | 288 | 2850 | 9.9 |
| Mystic Staff | 300 | 2800 | 9.33 |
| Oblivion Staff | 120 | 1625 | 13.54 |
| Orchid Malevolence | 144 | 3275 | 22.74 |
| Parasma | 480 | 5975 | 12.45 |
| Phylactery | 72 | 2600 | 36.11 |
| Power Treads (Intelligence) | 120 | 1400 | 11.67 |
| Robe of the Magi | 72 | 450 | 6.25 |
| Rod of Atos | 144 | 2250 | 15.63 |
| Scythe of Vyse | 360 | 5200 | 14.44 |
| Spirit Vessel | 120 | 2725 | 22.71 |
| Staff of Wizardry | 120 | 1000 | 8.33 |
| Ultimate Orb | 180 | 2800 | 15.56 |
| Urn of Shadows | 24 | 825 | 34.38 |
| Veil of Discord | 120 | 1700 | 14.17 |
| Wind Waker | 420 | 6800 | 16.19 |
| Witch Blade | 144 | 2775 | 19.27 |
| Wraith Band | 24 | 505 | 21.04 |
| Yasha and Kaya | 192 | 4200 | 21.88 |

Values do not include portions from actives or auras. [corpus:liquipedia_dota2/mana@2365137#Items]

### Maximum-mana talents

The Mana ability is passive, affects self, and has a varying Mana Bonus. It increases maximum mana while preserving the current mana percentage and uses a hidden modifier.

| Existing Mana Bonus values |
|---|
| 100/125/150/175/200/225/250/275/300/350/400/500/600/700/800/1000 |

Heroes can have a talent granting a flat mana bonus. The listed talent entry is:

| Bonus | Value |
|---|---:|
| Mana | +200 |

[corpus:liquipedia_dota2/mana@2365137#Talents]

## Mana restore manipulation

Mana restore manipulation is any amplification or reduction applied to mana restoration. It affects every ability listed as a mana-restoring ability.

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/mana@2365137#Mana_Restore_Manipulation]

## Mana loss manipulation

Mana loss manipulation reduces mana lost through ability costs or through mana removed, burned, or drained by abilities. Multiple mana-loss manipulations stack multiplicatively.

It does not affect mana regeneration, including negative mana-regeneration values. It also does not affect mana changes caused by gaining or losing intelligence: current mana percentages remain equal when intelligence changes, regardless of mana-loss reduction. Mana-setting effects are likewise unaffected.

Extra effects based on mana loss are not reduced. Mana Break abilities still deal full damage despite burning less mana, and mana-draining effects restore the same amount despite making their targets lose less mana. Mana-loss reduction is nevertheless applied before an ability is cast, so effects such as Nether Ward deal reduced damage.

| Mana-loss-manipulation source |
|---|
| Runes – Arcane |
| Kaya and Sange – Mana Loss Reduction |

[corpus:liquipedia_dota2/mana@2365137#Mana_Loss_Manipulation]

### Mana-loss-reduction talents

Manacost/Manaloss Reduction is passive, affects self, and has a varying Mana Loss Reduction. It grants both mana-cost and mana-loss reduction and uses a hidden modifier.

| Existing values |
|---|
| 8%/9%/11% |

Heroes can have a talent granting mana-loss reduction. The listed talent entry is:

| Bonus | Value |
|---|---:|
| Mana Reduction | +10% |

[corpus:liquipedia_dota2/mana@2365137#Talents_2]

## On-restore effects

Some abilities react when a unit has mana restored or regenerates mana. Only mana classified as restoration and mana obtained through regeneration trigger on-restore effects; mana gained by other methods, including setting mana, does not.

| Ability | Effect |
|---|---|
| Io – Tether | Whenever the caster has mana restored or regenerates mana, restores the tethered ally’s mana by a percentage of the restoration and regeneration received by the caster. |

[corpus:liquipedia_dota2/mana@2365137#On-restore_Effects]

## Abilities modified by mana

### Based on maximum mana

| Ability |
|---|
| Aegis of the Immortal – Reincarnation |
| Anti-Mage – Mana Break |
| Bane – Fiend's Grip |
| Fountain – Rejuvenation Aura |
| Medusa – Mystic Snake |
| Medusa – Cold Blooded |
| Night Stalker – Hunter in the Night2b |
| Nyx Assassin – Burrow |
| Outworld Destroyer – Essence Flux |
| Runes – Regeneration |
| Winter Wyvern – Arctic Burn2a |

| Marker | Requirement |
|---|---|
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

These abilities have effects based on maximum mana. [corpus:liquipedia_dota2/mana@2365137#Abilities_Modified_by_Mana]

### Based on current mana

Illusions’ current health and mana depend on the current health and mana of the units on which they are based. Besides illusions, the following abilities have effects based on current mana:

| Ability |
|---|
| Lich – Sinister Gaze |
| Ogre Magi – Unrefined Fireblast |
| Outworld Destroyer – Arcane Orb |

[corpus:liquipedia_dota2/mana@2365137#Abilities_Modified_by_Mana]

### Other mana-based effects

| Ability | Values | Effect |
|---|---|---|
| Anti-Mage – Mana Void | Damage per Missing Mana: 0.3 | Damages the target and an area around it based on how much mana the target is missing. |
| Outworld Destroyer – Sanity's Eclipse | Mana Difference Damage Multiplier: ( ) | Damages everyone within the area based on the mana difference between the caster and the enemy heroes hit. |
| Pugna – Nether Ward | Damage per Used Mana: (<br>Bonus Mana: 98%) | Damages any nearby enemy that spends mana in any way. |

[corpus:liquipedia_dota2/mana@2365137#Abilities_Modified_by_Mana]

## Mana regeneration

Mana regeneration determines how much mana a unit regains each second. It is displayed as a small number with a `+` sign on the right side of the unit’s mana bar. [corpus:liquipedia_dota2/mana@2365137#Mana_Regeneration]

## Recent changes

| Version | Date | Description |
|---|---|---|
| 7.31b | 2022-02-28 | Mana cost reduction now stacks multiplicatively. |
| 7.26a | 2020-04-21 | Fixed mana restore manipulation and mana regen manipulation, to not allow negative mana restore and mana regeneration. |
| 7.22 | 2019-05-24 | Heroes can now have non-standard base mana regeneration values. |

[corpus:liquipedia_dota2/mana@2365137#Recent_Changes]