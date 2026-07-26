---
title: Health Regeneration
kind: concept
patch: 7.41d
card:
  entity: health_regeneration
  sentences:
  - text: Health regeneration is the health a unit regains each second; it is displayed
      as a small number with a `+` beside the health bar, is applied in fixed `0.1-second`
      intervals, has no cap, and grants heroes `+0.1HP` per strength point.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984
  - text: Total health regeneration is defined as Base Health Regeneration + (`0.1
      × Strength`) ± Flat Bonus Health Regeneration Values ± % Bonus Current/Max Health
      Regeneration Values × (`1 ± % Restoration Manipulation Multiplier`).
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984
  - text: Most units have set, unit-specific base health regeneration.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Base_Health_Regeneration
  - text: Listed hero health-regeneration values are `-0.25`, `0`, `0.2`, `0.25`,
      `0.5`, `0.66`, `0.75`, `1`, `1.25`, `1.5`, `2`, `2.5`, and `3`.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Heroes
  - text: Listed creep base-regeneration endpoints are `0` for Undying Zombie, Skeleton
      Warrior, and Wraith King Skeleton and `20` for Tormentor and Roshan.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Creeps
  - text: Summoned wards have no base health regeneration.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Summons
  - text: Most regeneration changes are flat bonuses, while others scale with health
      or attributes.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Modifying_Health_Regeneration
  - text: The listed ability bonuses count as health regeneration rather than healing.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Abilities
  - text: The Health Regeneration talent grants a varying flat health-regeneration
      bonus.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Talents
  - text: The item tables cover passive traits only and exclude bonuses from item
      abilities such as Regeneration Aura.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Items
  - text: Health-regeneration manipulation is capped at `100%`.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Health_Regen_Manipulation
  - text: Version `7.27` changed health-regeneration manipulation to stack multiplicatively
      instead of additively.
    marks:
    - corpus:liquipedia_dota2/health_regeneration@2330984#Recent_Changes
---

# Health Regeneration

Health regeneration determines how much health a unit regains each second and appears as a small number with a `+` sign to the right of the unit’s health bar. Heroes gain bonus health regeneration from strength; each strength point grants `+0.1HP`.

Regeneration occurs in `0.1-second` intervals. This interval cannot be changed, and health regeneration has no cap. Health regeneration manipulation can increase or reduce regeneration, with the modified value shown on the HUD.

| Attribute | Bonus Health Regeneration |
|---|---:|
| Strength | +0.1HP |

Total health regeneration is defined as:

```text
Base Health Regeneration
+ (0.1 × Strength)
± Flat Bonus Health Regeneration Values
± % Bonus Current/Max Health Regeneration Values
× (1 ± % Restoration Manipulation Multiplier)
```

[corpus:liquipedia_dota2/health_regeneration@2330984]

## Base Health Regeneration

Most units have set base health regeneration that differs between units. [corpus:liquipedia_dota2/health_regeneration@2330984#Base_Health_Regeneration]

### Heroes

| Health Regeneration |
|---:|
| -0.25 |
| 0 |
| 0.2 |
| 0.25 |
| 0.5 |
| 0.66 |
| 0.75 |
| 1 |
| 1.25 |
| 1.5 |
| 2 |
| 2.5 |
| 3 [corpus:liquipedia_dota2/health_regeneration@2330984#Heroes] |

### Creeps

| Unit | Health Regeneration |
|---|---:|
| Undying Zombie, Skeleton Warrior, Wraith King Skeleton | 0 |
| Forged Spirit | 0.25 |
| Ghost, Minor Imp, Ancient Ice Shaman, Pollywog, Boglet, Croaker, Marshmage Apprentice, Marshmage, Kobold, Kobold Soldier, Kobold Foreman, Hill Troll Berserker, Hill Troll Priest, Vhoul Assassin, Fell Spirit, Harpy Scout, Harpy Stormcrafter, Centaur Courser, Giant Wolf, Alpha Wolf, Satyr Banisher, Satyr Mindstealer, Ogre Bruiser, Ogre Frostmage, Mud Golem, Hellbear, Wildwing, Wildwing Ripper, Hill Troll, Dark Troll Summoner, Ancient Black Drake, Ancient Rock Golem, Ancient Rumblehide, Ancient Thunderhide, Shard Golem, Ancient Prowler Acolyte, Ancient Prowler Shaman, Lycan Wolf | 0.5 |
| Centaur Conqueror, Satyr Tormenter, Hellbear Smasher | 1 |
| Ancient Granite Golem, Raptor, Razorback | 1.5 |
| Ancient Frostbitten Golem, Ancient Croaker, Ancient Marshmage, Ancient Black Dragon, Spiderling | 2 |
| Warpine Raider, Zealot, Treant | 2.5 |
| Eidolon | 4 |
| Demonic Archer, Demonic Warrior | 5 |
| Tormentor, Roshan | 20 [corpus:liquipedia_dota2/health_regeneration@2330984#Creeps] |

### Summons

Summoned wards have no base health regeneration. Other summoned units have the following base regeneration:

| Unit | Health Regeneration |
|---|---:|
| Astral Spirit, Familiar | 0 |
| Earth, Storm, Fire | 2/4/6/8 |
| Warlock Golem | 25/50/75 [corpus:liquipedia_dota2/health_regeneration@2330984#Summons] |

## Modifying Health Regeneration

Abilities and items can change how quickly a unit regenerates health. Most add a flat bonus, while others scale with factors such as health or attributes. Bonuses may be permanently passive, conditionally activated, or brief but strong. [corpus:liquipedia_dota2/health_regeneration@2330984#Modifying_Health_Regeneration]

### Abilities

The following abilities grant health-regeneration bonuses and are not considered healing:

| Source | Ability | Requirement |
|---|---|---|
| Alchemist | Berserk Potion | — |
| Alchemist | Chemical Rage | — |
| Broodmother | Spin Web | — |
| Chen | Divine Favor | — |
| Dragon Knight | Dragon Blood | — |
| Huskar | Berserker's Blood | — |
| Invoker | Quas | — |
| Io | Tether | — |
| Io | Overcharge | — |
| Juggernaut | Healing Ward | — |
| Legion Commander | Press the Attack | — |
| Legion Commander | Duel<sup>3</sup> | — |
| Lich | Frost Shield | — |
| Lifestealer | Infest | — |
| Lycan | Feral Impulse | — |
| Mars | Arena of Blood<sup>1</sup> | Requires talent |
| Meepo | Dig | — |
| Naga Siren | Song of the Siren<sup>2b</sup> | Requires Aghanim's Shard |
| Necrophos | Heartstopper Aura | — |
| Necrophos | Reaper's Scythe | — |
| Nyx Assassin | Burrow | — |
| Omniknight | Repel | — |
| Omniknight | Guardian Angel<sup>2a</sup> | Requires Aghanim's Scepter |
| Pudge | Dismember<sup>2b</sup> | Requires Aghanim's Shard |
| Slardar | Guardian Sprint | — |
| Slark | Depth Shroud | — |
| Slark | Shadow Dance | — |
| Timbersaw | Reactive Armor | — |
| Familiar | Stone Form | — |
| Visage | Gravekeeper's Cloak<sup>2b</sup> | Requires Aghanim's Shard |
| Aegis of the Immortal | Reincarnation | — |
| Bottle | Regenerate | — |
| Guardian Greaves | Guardian Aura | — |
| Headdress | Regeneration Aura | — |
| Healing Salve | Salve | — |
| Helm of the Dominator | Dominate | — |
| Helm of the Overlord | Dominate | — |
| Holy Locket | Regeneration Aura | — |
| Mekansm | Mekansm Aura | — |
| Pipe of Insight | Insight Aura | — |
| Runes | Regeneration | — |
| Spirit Vessel | Soul Release | — |
| Tango | Devour | — |
| Tranquil Boots | Break | — |
| Urn of Shadows | Soul Release | — |
| Flagbearer Creep | Inspiration Aura | — |
| Satyr Tormenter | Unholy Aura | — |
| Buildings | Tower Protection | — |
| Fountain | Rejuvenation Aura | — [corpus:liquipedia_dota2/health_regeneration@2330984#Abilities] |

### Talents

The Health Regeneration talent ability is passive, affects self, grants a varying flat health-regeneration bonus, and uses a hidden modifier.

| Property | Value |
|---|---|
| Ability | Passive |
| Affects | Self |
| Health Regen Bonus | Varies |
| Effect | Grants the hero a flat health-regeneration bonus |
| Values | 4/5/6/7/8/10/12/14/15/16/20/25/30/35/40/50/80 |
| Modifier | Hidden modifier |

The hero-talent table uses left and right columns for Levels 10, 15, 20, and 25:

| Bonus | Listed Values |
|---|---|
| Health Regen | +3/+4/+25/+25 [corpus:liquipedia_dota2/health_regeneration@2330984#Talents] |

### Items

The tables account only for passive item traits and exclude bonuses from item abilities such as Regeneration Aura.

#### Flat-Rate and Strength Regeneration

These items provide regeneration through a combination of flat-rate regeneration and strength:

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Boots of Bearing | 18.8 | 4225 | 224.73 |
| Bracer | 1.25 | 505 | 404 |
| Helm of the Dominator | 6.6 | 2550 | 386.36 |
| Helm of the Overlord | 9.1 | 5650 | 620.88 |
| Khanda | 7.8 | 5600 | 717.95 |
| Linken's Sphere | 8.1 | 4800 | 592.59 |
| Phylactery | 6.1 | 2600 | 426.23 [corpus:liquipedia_dota2/health_regeneration@2330984#Items] |

Values exclude portions from active abilities and auras. [corpus:liquipedia_dota2/health_regeneration@2330984#Items]

#### Flat-Rate Regeneration

These items grant a flat health-regeneration bonus to the hero that has them equipped:

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Armlet of Mordiggian | 5 | 2500 | 500 |
| Battle Fury | 7.5 | 3900 | 520 |
| Brawny Enchantment | 0 | N/A | N/A |
| Crimson Guard | 12 | 3725 | 310.42 |
| Enchanted Mango | 0.4 | 65 | 162.5 |
| Headdress | 0.5 | 425 | 850 |
| Heaven's Halberd | 6.5 | 3400 | 523.08 |
| Helm of Iron Will | 4 | 975 | 243.75 |
| Lotus Orb | 6.5 | 3850 | 592.31 |
| Mage Slayer | 5.5 | 3100 | 563.64 |
| Nimble Enchantment | -0.22 | N/A | N/A |
| Perseverance | 5.5 | 1400 | 254.55 |
| Pipe of Insight | 14 | 3725 | 266.07 |
| Refresher Orb | 14 | 5000 | 357.14 |
| Refresher Shard | 12 | N/A | N/A |
| Ring of Health | 4.5 | 700 | 155.56 |
| Ring of Regen | 1.25 | 175 | 140 |
| Ring of Tarrasque | 12 | 1700 | 141.67 |
| Tranquil Boots | 14 | 900 | 64.29 |
| Vanguard | 4.5 | 1700 | 377.78 |
| Vital Enchantment | 2.25 | N/A | N/A [corpus:liquipedia_dota2/health_regeneration@2330984#Items] |

Values exclude portions from active abilities and auras. [corpus:liquipedia_dota2/health_regeneration@2330984#Items]

#### Strength Regeneration

These items increase the hero’s health regeneration through their provided strength:

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Abyssal Blade | 2.6 | 6250 | 2403.85 |
| Aghanim's Scepter | 1 | 4200 | 4200 |
| Belt of Strength | 0.6 | 450 | 750 |
| Black King Bar | 1 | 4050 | 4050 |
| Circlet | 0.2 | 155 | 775 |
| Consecrated Wraps | 0.5 | 2600 | 5200 |
| Crella's Crozier | 0.6 | 4800 | 8000 |
| Crown | 0.4 | 450 | 1125 |
| Diadem | 0.6 | 1000 | 1666.67 |
| Dragon Lance | 1 | 1900 | 1900 |
| Drum of Endurance | 0.8 | 1625 | 2031.25 |
| Echo Sabre | 1.5 | 2700 | 1800 |
| Essence Distiller | 0.3 | 1775 | 5916.67 |
| Ethereal Blade | 2.4 | 5200 | 2166.67 |
| Eye of Skadi | 3.5 | 5900 | 1685.71 |
| Gauntlets of Strength | 0.3 | 140 | 466.67 |
| Ghost Scepter | 0.5 | 1500 | 3000 |
| Harpoon | 2.5 | 4700 | 1880 |
| Heart of Tarrasque | 4 | 5100 | 1275 |
| Holy Locket | 0.7 | 2250 | 3214.29 |
| Hurricane Pike | 1.5 | 4450 | 2966.67 |
| Hydra's Breath | 1.5 | 5900 | 3933.33 |
| Iron Branch | 0.1 | 55 | 550 |
| Kaya and Sange | 1.6 | 4200 | 2625 |
| Magic Wand | 0.3 | 460 | 1533.33 |
| Manta Style | 1 | 4650 | 4650 |
| Meteor Hammer | 0.6 | 2850 | 4750 |
| Null Talisman | 0.2 | 505 | 2525 |
| Ogre Axe | 1 | 1000 | 1000 |
| Overwhelming Blink | 2.5 | 6800 | 2720 |
| Power Treads (Strength) | 1 | 1400 | 1400 |
| Reaver | 2.5 | 2800 | 1120 |
| Sange | 1.6 | 2100 | 1312.5 |
| Sange and Yasha | 1.6 | 4200 | 2625 |
| Satanic | 2.5 | 5050 | 2020 |
| Skull Basher | 1 | 2875 | 2875 |
| Soul Ring | 0.6 | 805 | 1341.67 |
| Spirit Vessel | 1 | 2725 | 2725 |
| Ultimate Orb | 1.5 | 2800 | 1866.67 |
| Urn of Shadows | 0.2 | 825 | 4125 |
| Wraith Band | 0.2 | 505 | 2525 [corpus:liquipedia_dota2/health_regeneration@2330984#Items] |

Values exclude portions from active abilities and auras. [corpus:liquipedia_dota2/health_regeneration@2330984#Items]

## Health Regeneration Manipulation

Health regeneration manipulation is any amplification or reduction applied to health regeneration.

### Manipulation Sources

| Source | Ability |
|---|---|
| Chen | Divine Favor |
| Dark Willow | Pixie Dust |
| Mars | Dauntless |
| Night Stalker | Heart of Darkness |
| Omniknight | Guardian Angel<sup>2a</sup> |

### Decrease Sources

| Source | Ability |
|---|---|
| Necrophos | Heartstopper Aura<sup>1</sup> |
| Venomancer | Poison Sting<sup>1</sup> |
| Vhoul Assassin | Envenomed Weapon |

`1` Requires talent. `2a` Requires Aghanim's Scepter. Capped at `100%`. [corpus:liquipedia_dota2/health_regeneration@2330984#Health_Regen_Manipulation]

## Recent Changes

| Version | Date | Description |
|---|---|---|
| 7.33 | 2023-04-20 | Reduced hero base health from 200 to 120.<br>Increased health bonus per strength from 20 to 22.<br>ADDED special health bars to display hero attacks to destroy for ward-type units. |
| 7.27 | 2020-06-28 | The following mechanics now stack multiplicatively instead of additively:<br>• Heal manipulation<br>• Health regen manipulation<br>• Lifesteal manipulation<br>• Spell lifesteal manipulation |
| 7.26a | 2020-04-21 | Fixed the following mechanics to not allow negative heal, health regeneration, and lifesteal values:<br>• Heal manipulation<br>• Health regen manipulation<br>• Lifesteal manipulation [corpus:liquipedia_dota2/health_regeneration@2330984#Recent_Changes] |