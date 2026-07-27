---
title: Mana Regeneration
kind: concept
patch: 7.41d
card:
  entity: mana_regeneration
  sentences:
  - text: Mana regeneration determines how much mana a unit regains each second; it
      occurs at fixed 0.1-second intervals, each intelligence point adds 0.05MP, and
      it has no cap.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534
  - text: The HUD displays mana regeneration as a small number with a + sign to the
      right of the mana bar.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534
  - text: Most units with mana pools have unit-specific base regeneration, but most
      heroes and some non-hero units have none.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Base_Mana_Regeneration
  - text: The hero base-regeneration table lists -1, 0, 0.25, 0.3, 0.4, 0.5, and 0.75.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Heroes
  - text: The creep table assigns 1.5 to Ancient Granite Golem, 3 to Harpy Stormcrafter,
      and 4 to Forged Spirit.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Creeps
  - text: Storm and Fire summons have 1.5 regeneration, while Earth has 2.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Summons
  - text: Abilities and items usually add flat regeneration, although some bonuses
      scale with mana or attributes.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Modifying_Mana_Regeneration
  - text: Flat mana-regeneration talents are passive self-effects with listed values
      of 1/1.25/1.5/1.75/2/2.5/3/4/5/6/8/10/14.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Talents
  - text: Item tables include only passive traits and exclude regeneration supplied
      by item abilities, actives, or auras.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Items
  - text: Scythe of Vyse has a listed regeneration value of 10, an item cost of 5200,
      and a cost/value point of 520.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Items
  - text: Mana regen manipulation is amplification or reduction applied to mana regeneration.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Mana_Regen_Manipulation
  - text: Mana Regen Amplification is a passive self-effect with a listed value of
      10%, but no hero has the talent.
    marks:
    - corpus:liquipedia_dota2/mana_regeneration@2244534#Talents_2
---

# Mana Regeneration

## Overview

Mana regeneration determines how much mana a unit regains each second. The HUD displays it as a small number with a `+` sign to the right of the unit’s mana bar. Heroes gain mana regeneration from intelligence, with each intelligence point increasing mana regeneration by `0.05MP`. Regeneration occurs at fixed `0.1`-second intervals, cannot have its interval changed, and has no cap. Mana restore manipulation affects mana regeneration, and the HUD displays increased or reduced values. [corpus:liquipedia_dota2/mana_regeneration@2244534]

| Attribute | Bonus Mana Regeneration |
|---|---:|
| Intelligence | +0.05MP |

[corpus:liquipedia_dota2/mana_regeneration@2244534]

## Base Mana Regeneration

Most units with a mana pool have a set base mana regeneration that differs by unit. Most heroes and some non-hero units have no base mana regeneration. [corpus:liquipedia_dota2/mana_regeneration@2244534#Base_Mana_Regeneration]

### Heroes

| Hero | Magic Regeneration |
|---|---:|
|  | -1 |
|  | 0 |
|  | 0.25 |
|  | 0.3 |
|  | 0.4 |
|  | 0.5 |
|  | 0.75 |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Heroes]

### Creeps

| Unit | Magic Regeneration |
|---|---:|
| Ghost, Warpine Raider, Ancient Frostbitten Golem, Ancient Ice Shaman, Pollywog, Boglet, Croaker, Ancient Croaker, Marshmage Apprentice, Marshmage, Ancient Marshmage, Kobold, Kobold Soldier, Kobold Foreman, Hill Troll Berserker, Hill Troll Priest, Vhoul Assassin, Fell Spirit, Harpy Scout, Centaur Courser, Centaur Conqueror, Giant Wolf, Alpha Wolf, Satyr Banisher, Satyr Mindstealer, Ogre Bruiser, Ogre Frostmage, Mud Golem, Satyr Tormenter, Hellbear, Hellbear Smasher, Wildwing, Wildwing Ripper, Hill Troll, Dark Troll Summoner, Ancient Black Drake, Ancient Black Dragon, Ancient Rock Golem, Ancient Rumblehide, Ancient Thunderhide, Shard Golem, Ancient Prowler Acolyte, Ancient Prowler Shaman | 1 |
| Ancient Granite Golem | 1.5 |
| Harpy Stormcrafter | 3 |
| Forged Spirit | 4 |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Creeps]

### Summons

Summons without a mana pool also have no mana regeneration. All other summons have the following regeneration: [corpus:liquipedia_dota2/mana_regeneration@2244534#Summons]

| Unit | Magic Regeneration |
|---|---:|
| Storm, Fire | 1.5 |
| Earth | 2 |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Summons]

## Modifying Mana Regeneration

As with health regeneration, abilities and items can change how quickly a unit regenerates mana. Most add a flat bonus, while some increase regeneration based on factors such as mana or attributes. Bonuses may be permanent passives, conditionally activated effects, or short effects that provide a strong bonus. [corpus:liquipedia_dota2/mana_regeneration@2244534#Modifying_Mana_Regeneration]

### Abilities

The following abilities affect a unit’s mana regeneration: [corpus:liquipedia_dota2/mana_regeneration@2244534#Ability]

| Source | Ability |
|---|---|
| Crystal Maiden | Arcane Aura |
| Fountain | Rejuvenation Aura |
| Necrophos | Heartstopper Aura |
| Nyx Assassin | Burrow |
| Satyr Mindstealer | Mana Aura |
| Aegis of the Immortal | Reincarnation Expire Regeneration |
| Arcane Boots | Basilius Aura |
| Clarity | Replenish |
| Bottle | Regenerate |
| Guardian Greaves | Guardian Aura |
| Runes | Regeneration |
| Ring of Aquila | Aquila Aura |
| Ring of Basilius | Basilius Aura |
| Veil of Discord | Basilius Aura |
| Vladmir's Offering | Vladmir's Aura |
| Helm of the Overlord | Vladmir's Aura |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Ability]

### Flat Mana-Regeneration Talent

Mana Regeneration is a passive ability affecting self. It grants the hero a flat mana-regeneration bonus, with `Mana Regen Bonus: Varies`, and has a hidden modifier. [corpus:liquipedia_dota2/mana_regeneration@2244534#Talents]

| Property | Value |
|---|---|
| Listed values | 1/1.25/1.5/1.75/2/2.5/3/4/5/6/8/10/14 |
| Modifier | ? Hidden modifier |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Talents]

Heroes with the talent are listed using Level 10, Level 15, Level 20, and Level 25 headings, each divided into Left and Right. [corpus:liquipedia_dota2/mana_regeneration@2244534#Talents]

| Bonus | Listed entries |
|---|---|
| Mana Regen | +1.5 / +1.75 / +1.5 / +1.75 / +1.5 / +1.5 / +1.75 / +1.5 / +1.5 / +1.5 / +1.5 / +1.5 |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Talents]

### Items

The item tables account only for passive traits and exclude bonuses from item abilities, such as Basilius Aura. Values likewise exclude portions from actives or auras. [corpus:liquipedia_dota2/mana_regeneration@2244534#Items]

#### Flat-Rate and Intelligence Mana Regeneration

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Bloodthorn | 5.25 | 6400 | 1219.05 |
| Essence Distiller | 1.9 | 1775 | 934.21 |
| Eul's Scepter of Divinity | 3 | 2600 | 866.67 |
| Harpoon | 2.5 | 4700 | 1880 |
| Khanda | 3.4 | 5600 | 1647.06 |
| Linken's Sphere | 5.05 | 4800 | 950.5 |
| Null Talisman | 1.25 | 505 | 404 |
| Oblivion Staff | 1.75 | 1625 | 928.57 |
| Orchid Malevolence | 3.1 | 3275 | 1056.45 |
| Parasma | 3.5 | 5975 | 1707.14 |
| Phylactery | 2.55 | 2600 | 1019.61 |
| Scythe of Vyse | 10 | 5200 | 520 |
| Spirit Vessel | 2.25 | 2725 | 1211.11 |
| Urn of Shadows | 1.35 | 825 | 611.11 |
| Wind Waker | 4.75 | 6800 | 1431.58 |
| Witch Blade | 2.1 | 2775 | 1321.43 |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Items]

#### Flat-Rate Mana Regeneration

These items grant a flat mana-regeneration bonus to the hero carrying them. [corpus:liquipedia_dota2/mana_regeneration@2244534#Items]

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Aether Lens | 2.5 | 2275 | 910 |
| Arcane Boots | 0.25 | 1500 | 6000 |
| Battle Fury | 2.75 | 3900 | 1418.18 |
| Echo Sabre | 1.75 | 2700 | 1542.86 |
| Falcon Blade | 1.8 | 1125 | 625 |
| Guardian Greaves | 1 | 4450 | 4450 |
| Infused Raindrops | 0.8 | 225 | 281.25 |
| Keen-Eyed Enchantment | 0.33 | N/A | N/A |
| Lotus Orb | 4 | 3850 | 962.5 |
| Mage Slayer | 2.5 | 3100 | 1240 |
| Mystical Enchantment | 0.07 | N/A | N/A |
| Octarine Core | 6 | 4900 | 816.67 |
| Perseverance | 2.25 | 1400 | 622.22 |
| Refresher Orb | 7 | 5000 | 714.29 |
| Refresher Shard | 6 | N/A | N/A |
| Ring of Basilius | 0.5 | 425 | 850 |
| Sage's Mask | 0.7 | 175 | 250 |
| Tiara of Selemene | 6 | 1700 | 283.33 |
| Vladmir's Offering | 0.75 | 2200 | 2933.33 |
| Void Stone | 1.75 | 700 | 400 |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Items]

#### Intelligence Mana Regeneration

These items increase the hero’s mana regeneration through the intelligence they provide. [corpus:liquipedia_dota2/mana_regeneration@2244534#Items]

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Aghanim's Scepter | 0.5 | 4200 | 8400 |
| Arcane Blink | 1.25 | 6800 | 5440 |
| Bloodstone | 0.75 | 4700 | 6266.67 |
| Bracer | 0.1 | 505 | 5050 |
| Circlet | 0.1 | 155 | 1550 |
| Consecrated Wraps | 0.25 | 2600 | 10400 |
| Crella's Crozier | 0.3 | 4800 | 16000 |
| Crown | 0.2 | 450 | 2250 |
| Crude Enchantment | Expression error: Unexpected < operator. | N/A | N/A |
| Diadem | 0.3 | 1000 | 3333.33 |
| Diffusal Blade | 0.5 | 2500 | 5000 |
| Disperser | 0.5 | 6100 | 12200 |
| Ethereal Blade | 1.2 | 5200 | 4333.33 |
| Eye of Skadi | 1.75 | 5900 | 3371.43 |
| Force Staff | 0.5 | 2200 | 4400 |
| Ghost Scepter | 0.25 | 1500 | 6000 |
| Gleipnir | 0.6 | 4650 | 7750 |
| Helm of the Dominator | 0.3 | 2550 | 8500 |
| Helm of the Overlord | 1.05 | 5650 | 5380.95 |
| Holy Locket | 0.35 | 2250 | 6428.57 |
| Hurricane Pike | 0.75 | 4450 | 5933.33 |
| Iron Branch | 0.05 | 55 | 1100 |
| Kaya | 0.8 | 2100 | 2625 |
| Kaya and Sange | 0.8 | 4200 | 5250 |
| Magic Wand | 0.15 | 460 | 3066.67 |
| Manta Style | 0.5 | 4650 | 9300 |
| Mantle of Intelligence | 0.15 | 140 | 933.33 |
| Meteor Hammer | 1.2 | 2850 | 2375 |
| Mystic Staff | 1.25 | 2800 | 2240 |
| Power Treads (Intelligence) | 0.5 | 1400 | 2800 |
| Robe of the Magi | 0.3 | 450 | 1500 |
| Rod of Atos | 0.6 | 2250 | 3750 |
| Staff of Wizardry | 0.5 | 1000 | 2000 |
| Ultimate Orb | 0.75 | 2800 | 3733.33 |
| Veil of Discord | 0.5 | 1700 | 3400 |
| Wraith Band | 0.1 | 505 | 5050 |
| Yasha and Kaya | 0.8 | 4200 | 5250 |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Items]

## Mana Regen Manipulation

Mana regen manipulation is any amplification or reduction applied to mana regeneration. Its main article is Restoration Manipulation. [corpus:liquipedia_dota2/mana_regeneration@2244534#Mana_Regen_Manipulation]

| Source | Effect |
|---|---|
| Crystal Maiden | Blueheart Floe |
| Meteor Hammer | Mana Regen Amp |
| Kaya | Mana Regen Amp |
| Kaya and Sange | Mana Regen Amp |
| Necrophos | Ghost Shroud |
| Necrophos | Ghost Shroud 3 |
| Yasha and Kaya | Mana Regen Amp |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Mana_Regen_Manipulation]

| Note | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Mana_Regen_Manipulation]

### Mana Regen Amplification Talent

Mana Regen Amplification is a passive ability affecting self. It grants the hero mana regen amplification, lists `Mana Regen Amplification: Varies`, has the listed value `10%`, and uses a hidden modifier. No hero has this talent. [corpus:liquipedia_dota2/mana_regeneration@2244534#Talents_2]

| Property | Value |
|---|---|
| Ability | Mana Regen Amplification |
| Type | Passive |
| Affects | Self |
| Mana Regen Amplification | Varies |
| Listed values | 10% |
| Modifier | ? Hidden modifier |

[corpus:liquipedia_dota2/mana_regeneration@2244534#Talents_2]

## Recent Changes

Recent changes are recorded in **Mana/Changelogs**. [corpus:liquipedia_dota2/mana_regeneration@2244534#Recent_Changes]