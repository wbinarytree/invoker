---
title: Attack Damage
kind: concept
patch: 7.41d
card:
  entity: attack_damage
  sentences:
  - text: Attack damage is the amount a unit is shown to deal with a regular attack;
      total attack damage is Main Attack Damage plus Bonus Attack Damage, and primary-attribute
      scaling is +1 per point for Strength, Agility, or Intelligence and +0.45 for
      Universal.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047
    - corpus:liquipedia_dota2/attack_damage@2401047#Main_Attack_Damage
  - text: Main Attack Damage is the white statistic consisting of Base Attack Damage
      plus damage granted by the hero’s primary attribute.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Main_Attack_Damage
  - text: Base Attack Damage is an unchanging minimum–maximum range from which a random
      value is chosen for each attack.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Base_Attack_Damage
  - text: Bonus Attack Damage is the green, plus-sign statistic increased by grants
      such as the +9 Damage from Blades of Attack.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Bonus_Attack_Damage
  - text: Illusions benefit only from Main Attack Damage even though their HUD displays
      Bonus Attack Damage.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Bonus_Attack_Damage
  - text: Attack damage against a unit type equals Total Attack Damage × Attack Class
      × Damage Manipulation.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Attack_Class_Definition
  - text: There are 3 attack classes, while a unit without a class ability deals 100%
      damage before armor and other damage manipulation.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Attack_Classes
  - text: Runty attacks use a 0.75 factor against heroes and a 0.7 factor against
      Reinforced units.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Runty
  - text: Piercing attacks use factors of 0.5 against heroes, 1.5 against creeps,
      and 0.35 against Reinforced units.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Piercing
  - text: Reinforced units take damage from heroes, illusions, and summoned units
      at factors of 0.5, 0.6, and 0.9, respectively.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Reinforced
  - text: Instant Attacks use regular attack-damage values as ability damage without
      the regular attack animation or attack-speed timing.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Instant_Attacks
  - text: Conditional Attack Damage Bonuses are undisplayed direct bonuses dealt in
      the same damage instance as the unit’s attack damage.
    marks:
    - corpus:liquipedia_dota2/attack_damage@2401047#Conditional_Attack_Damage_Bonus
---

# Attack Damage

Attack damage is the amount of damage a unit is shown to deal with a regular attack. A unit’s total attack damage is the sum of its Main Attack Damage and Bonus Attack Damage. Many effects can modify attack damage, which passes through multiple steps to determine how much damage an attack actually deals. [corpus:liquipedia_dota2/attack_damage@2401047]

## Total Attack Damage

A level 1 Sniper with Blades of Attack has base attack damage that varies by 6; Main Attack Damage is displayed in white and Bonus Attack Damage in green. Total attack damage is synonymous with the health a target immediately loses as a direct result of an attack. Some on-hit effects unaffected by critical strike are still considered attack damage, while others are not. [corpus:liquipedia_dota2/attack_damage@2401047#Total_Attack_Damage]

Total Attack Damage can be defined as:

| Order |
|---|
| Base and Main Value |
| ± Base Attack Damage Values (× Multiplier) |
| × % Bonus Attack Damage Multiplier |
| ± Flat Bonus Attack Damage Values |
| × Critical Strike Multiplier |
| ± Instant Attack Damage Bonus (× Multiplier) |
| ± × Conditional Bonuses |
| − Damage Block |
| × Attack Class Multiplier |
| × Damage Manipulation |

The following abilities reduce the affected unit’s damage before Damage Block is applied:

| Total Attack Damage Reducing Source |
|---|
| Bane – Enfeeble |
| Dragon Knight – Breathe Fire |
| Giant Wolf – Intimidate |
| Hoodwink – Acorn Shot³ |
| Phantom Assassin – Stifling Dagger³ |
| Riki – Tricks of the Trade |
| Vengeful Spirit – Wave of Terror |

1 Requires talent.  
2a Requires Aghanim’s Scepter.  
2b Requires Aghanim’s Shard.  
3 Main attack damage is reduced only for the instant attack, so only the ability can use it. [corpus:liquipedia_dota2/attack_damage@2401047#Total_Attack_Damage_Sources]

## Main Attack Damage

Main Attack Damage is the white damage value in a hero’s statistics. It consists of Base Attack Damage plus damage granted by the hero’s primary attribute. It can be increased only by raising the primary attribute or by a few specific abilities. Attribute points can be acquired by leveling up or through items, abilities, and talents that grant bonus attributes.

### Scaling attributes

| Primary Attribute | Main Attack Damage/Point |
|---|---:|
| Strength | +1 |
| Agility | +1 |
| Intelligence | +1 |
| Universal | +0.45 |

Main Attack Damage is defined as:

`Main Attack Damage = ((Base Attack Damage + Σ Primary Attribute) × (1 + Bonus Modifiers1) × (1 + Bonus Modifiers2) × … × (1 + Bonus Modifiersn))` [corpus:liquipedia_dota2/attack_damage@2401047#Main_Attack_Damage]

### General increasing sources

The following sources manipulate a hero’s primary attribute and therefore increase Main Attack Damage:

| Source | Value and behavior |
|---|---|
| Attributes – Attribute Bonus | All Attribute Bonus: 2/4/6/8/10/12/14. If all ability points are spent on their respective levels, Attribute Bonus levels automatically at levels 17/19/21/22/23/24/26. |
| Power Treads – Switch Attribute | Selected Attribute Bonus: 10. Passively grants a bonus to the currently selected attribute. Casting switches Strength ➜ Intelligence, Intelligence ➜ Agility, and Agility ➜ Strength. |

[corpus:liquipedia_dota2/attack_damage@2401047#Main_Attack_Damage_Sources]

### Strength

#### Bonus Strength items

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Abyssal Blade | 26 | 6250 | 240.38 |
| Aghanim's Scepter | 10 | 4200 | 420 |
| Belt of Strength | 6 | 450 | 75 |
| Black King Bar | 10 | 4050 | 405 |
| Boots of Bearing | 8 | 4225 | 528.13 |
| Bracer | 5 | 505 | 101 |
| Circlet | 2 | 155 | 77.5 |
| Consecrated Wraps | 5 | 2600 | 520 |
| Crella's Crozier | 6 | 4800 | 800 |
| Crown | 4 | 450 | 112.5 |
| Diadem | 6 | 1000 | 166.67 |
| Dragon Lance | 10 | 1900 | 190 |
| Drum of Endurance | 8 | 1625 | 203.13 |
| Echo Sabre | 15 | 2700 | 180 |
| Essence Distiller | 3 | 1775 | 591.67 |
| Ethereal Blade | 24 | 5200 | 216.67 |
| Eye of Skadi | 35 | 5900 | 168.57 |
| Gauntlets of Strength | 3 | 140 | 46.67 |
| Ghost Scepter | 5 | 1500 | 300 |
| Harpoon | 25 | 4700 | 188 |
| Heart of Tarrasque | 40 | 5100 | 127.5 |
| Helm of the Dominator | 6 | 2550 | 425 |
| Helm of the Overlord | 21 | 5650 | 269.05 |
| Holy Locket | 7 | 2250 | 321.43 |
| Hurricane Pike | 15 | 4450 | 296.67 |
| Hydra's Breath | 15 | 5900 | 393.33 |
| Iron Branch | 1 | 55 | 55 |
| Kaya and Sange | 16 | 4200 | 262.5 |
| Khanda | 8 | 5600 | 700 |
| Linken's Sphere | 16 | 4800 | 300 |
| Magic Wand | 3 | 460 | 153.33 |
| Manta Style | 10 | 4650 | 465 |
| Meteor Hammer | 6 | 2850 | 475 |
| Null Talisman | 2 | 505 | 252.5 |
| Ogre Axe | 10 | 1000 | 100 |
| Overwhelming Blink | 25 | 6800 | 272 |
| Phylactery | 6 | 2600 | 433.33 |
| Power Treads (Strength) | 10 | 1400 | 140 |
| Reaver | 25 | 2800 | 112 |
| Sange | 16 | 2100 | 131.25 |
| Sange and Yasha | 16 | 4200 | 262.5 |
| Satanic | 25 | 5050 | 202 |
| Skull Basher | 10 | 2875 | 287.5 |
| Soul Ring | 6 | 805 | 134.17 |
| Spirit Vessel | 10 | 2725 | 272.5 |
| Ultimate Orb | 15 | 2800 | 186.67 |
| Urn of Shadows | 2 | 825 | 412.5 |
| Wraith Band | 2 | 505 | 252.5 |

Values do not include portions from actives or auras.

#### Strength-increasing sources

| Source |
|---|
| Attributes – Attribute Bonus |
| Alchemist – Aghanim's Scepter Synth |
| Evolved Enchantment – Primary Attribute Bonus |
| Armlet of Mordiggian – Unholy Strength |
| Centaur Warrunner – Double Edge²ᵇ |
| Magnus – Reverse Polarity¹ |
| Power Treads – Switch Attribute |
| Omniknight – Heavenly Grace |
| Pudge – Flesh Heap |
| Undying – Decay |
| Undying – Flesh Golem |
| Invoker – Quas |
| Morphling – Adaptive Strike (Strength) |
| Morphling – Morph²ᵃ |
| Slark – Essence Shift |

1 Requires talent.  
2a Requires Aghanim’s Scepter.  
2b Requires Aghanim’s Shard. [corpus:liquipedia_dota2/attack_damage@2401047#Strength]

### Agility

#### Bonus Agility items

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Aghanim's Scepter | 10 | 4200 | 420 |
| Band of Elvenskin | 6 | 450 | 75 |
| Blade of Alacrity | 10 | 1000 | 100 |
| Bracer | 2 | 505 | 252.5 |
| Butterfly | 35 | 5450 | 155.71 |
| Circlet | 2 | 155 | 77.5 |
| Consecrated Wraps | 5 | 2600 | 520 |
| Crella's Crozier | 6 | 4800 | 800 |
| Crown | 4 | 450 | 112.5 |
| Diadem | 6 | 1000 | 166.67 |
| Diffusal Blade | 15 | 2500 | 166.67 |
| Disperser | 40 | 6100 | 152.5 |
| Dragon Lance | 15 | 1900 | 126.67 |
| Eaglesong | 25 | 2800 | 112 |
| Essence Distiller | 3 | 1775 | 591.67 |
| Ethereal Blade | 24 | 5200 | 216.67 |
| Eye of Skadi | 35 | 5900 | 168.57 |
| Ghost Scepter | 5 | 1500 | 300 |
| Harpoon | 10 | 4700 | 470 |
| Helm of the Dominator | 6 | 2550 | 425 |
| Helm of the Overlord | 21 | 5650 | 269.05 |
| Holy Locket | 7 | 2250 | 321.43 |
| Hurricane Pike | 20 | 4450 | 222.5 |
| Hydra's Breath | 30 | 5900 | 196.67 |
| Iron Branch | 1 | 55 | 55 |
| Khanda | 8 | 5600 | 700 |
| Linken's Sphere | 16 | 4800 | 300 |
| Magic Wand | 3 | 460 | 153.33 |
| Manta Style | 26 | 4650 | 178.85 |
| Meteor Hammer | 6 | 2850 | 475 |
| Null Talisman | 2 | 505 | 252.5 |
| Orb of Corrosion | 7 | 1050 | 150 |
| Phylactery | 6 | 2600 | 433.33 |
| Power Treads (Agility) | 10 | 1400 | 140 |
| Sange and Yasha | 16 | 4200 | 262.5 |
| Slippers of Agility | 3 | 140 | 46.67 |
| Specialist's Array | 15 | 2550 | 170 |
| Spirit Vessel | 10 | 2725 | 272.5 |
| Swift Blink | 25 | 6800 | 272 |
| Ultimate Orb | 15 | 2800 | 186.67 |
| Urn of Shadows | 2 | 825 | 412.5 |
| Wraith Band | 5 | 505 | 101 |
| Yasha | 16 | 2100 | 131.25 |
| Yasha and Kaya | 16 | 4200 | 262.5 |

Values do not include portions from actives or auras.

#### Agility-increasing sources

| Source |
|---|
| Attributes – Attribute Bonus |
| Alchemist – Aghanim's Scepter Synth |
| Evolved Enchantment – Primary Attribute Bonus |
| Drow Ranger – Precision Aura |
| Magnus – Reverse Polarity¹ |
| Riki – Tricks of the Trade |
| Slark – Essence Shift |
| Power Treads – Switch Attribute |
| Phantom Lancer – Phantom Rush |
| Morphling – Morph²ᵃ |
| Invoker – Wex |

1 Requires talent.  
2a Requires Aghanim’s Scepter.  
2b Requires Aghanim’s Shard. [corpus:liquipedia_dota2/attack_damage@2401047#Agility]

### Intelligence

#### Bonus Intelligence items

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Aghanim's Scepter | 10 | 4200 | 420 |
| Arcane Blink | 25 | 6800 | 272 |
| Bloodstone | 15 | 4700 | 313.33 |
| Bloodthorn | 25 | 6400 | 256 |
| Bracer | 2 | 505 | 252.5 |
| Circlet | 2 | 155 | 77.5 |
| Consecrated Wraps | 5 | 2600 | 520 |
| Crella's Crozier | 6 | 4800 | 800 |
| Crown | 4 | 450 | 112.5 |
| Crude Enchantment | Expression error: Unexpected < operator. | N/A | N/A |
| Diadem | 6 | 1000 | 166.67 |
| Diffusal Blade | 10 | 2500 | 250 |
| Disperser | 10 | 6100 | 610 |
| Essence Distiller | 3 | 1775 | 591.67 |
| Ethereal Blade | 24 | 5200 | 216.67 |
| Eul's Scepter of Divinity | 10 | 2600 | 260 |
| Eye of Skadi | 35 | 5900 | 168.57 |
| Force Staff | 10 | 2200 | 220 |
| Ghost Scepter | 5 | 1500 | 300 |
| Gleipnir | 12 | 4650 | 387.5 |
| Harpoon | 10 | 4700 | 470 |
| Helm of the Dominator | 6 | 2550 | 425 |
| Helm of the Overlord | 21 | 5650 | 269.05 |
| Holy Locket | 7 | 2250 | 321.43 |
| Hurricane Pike | 15 | 4450 | 296.67 |
| Iron Branch | 1 | 55 | 55 |
| Kaya | 16 | 2100 | 131.25 |
| Kaya and Sange | 16 | 4200 | 262.5 |
| Khanda | 8 | 5600 | 700 |
| Linken's Sphere | 16 | 4800 | 300 |
| Magic Wand | 3 | 460 | 153.33 |
| Manta Style | 10 | 4650 | 465 |
| Mantle of Intelligence | 3 | 140 | 46.67 |
| Meteor Hammer | 24 | 2850 | 118.75 |
| Mystic Staff | 25 | 2800 | 112 |
| Null Talisman | 5 | 505 | 101 |
| Oblivion Staff | 10 | 1625 | 162.5 |
| Orchid Malevolence | 12 | 3275 | 272.92 |
| Parasma | 40 | 5975 | 149.38 |
| Phylactery | 6 | 2600 | 433.33 |
| Power Treads (Intelligence) | 10 | 1400 | 140 |
| Robe of the Magi | 6 | 450 | 75 |
| Rod of Atos | 12 | 2250 | 187.5 |
| Scythe of Vyse | 30 | 5200 | 173.33 |
| Spirit Vessel | 10 | 2725 | 272.5 |
| Staff of Wizardry | 10 | 1000 | 100 |
| Ultimate Orb | 15 | 2800 | 186.67 |
| Urn of Shadows | 2 | 825 | 412.5 |
| Veil of Discord | 10 | 1700 | 170 |
| Wind Waker | 35 | 6800 | 194.29 |
| Witch Blade | 12 | 2775 | 231.25 |
| Wraith Band | 2 | 505 | 252.5 |
| Yasha and Kaya | 16 | 4200 | 262.5 |

Values do not include portions from actives or auras.

#### Intelligence-increasing sources

| Source |
|---|
| Attributes – Attribute Bonus |
| Alchemist – Aghanim's Scepter Synth |
| Evolved Enchantment – Primary Attribute Bonus |
| Invoker – Exort |
| Power Treads – Switch Attribute |
| Magnus – Reverse Polarity¹ |
| Silencer – Glaives of Wisdom |
| Skywrath Mage – Shield of the Scion |
| Morphling – Morph²ᵃ |

1 Requires talent.  
2a Requires Aghanim’s Scepter.  
2b Requires Aghanim’s Shard. [corpus:liquipedia_dota2/attack_damage@2401047#Intelligence]

### Universal

#### Damage from all-attribute items

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Aghanim's Scepter | 13.5 | 4200 | 311.11 |
| Bracer | 4.05 | 505 | 124.69 |
| Circlet | 2.7 | 155 | 57.41 |
| Consecrated Wraps | 6.75 | 2600 | 385.19 |
| Crella's Crozier | 8.1 | 4800 | 592.59 |
| Crown | 5.4 | 450 | 83.33 |
| Diadem | 8.1 | 1000 | 123.46 |
| Essence Distiller | 4.05 | 1775 | 438.27 |
| Ethereal Blade | 32.4 | 5200 | 160.49 |
| Evolved Enchantment | 32.4 | N/A | N/A |
| Eye of Skadi | 47.25 | 5900 | 124.87 |
| Ghost Scepter | 6.75 | 1500 | 222.22 |
| Harpoon | 20.25 | 4700 | 232.1 |
| Helm of the Dominator | 8.1 | 2550 | 314.81 |
| Helm of the Overlord | 28.35 | 5650 | 199.29 |
| Holy Locket | 9.45 | 2250 | 238.1 |
| Hurricane Pike | 22.5 | 4450 | 197.78 |
| Iron Branch | 1.35 | 55 | 40.74 |
| Khanda | 10.8 | 5600 | 518.52 |
| Linken's Sphere | 21.6 | 4800 | 222.22 |
| Magic Wand | 4.05 | 460 | 113.58 |
| Manta Style | 20.7 | 4650 | 224.64 |
| Meteor Hammer | 16.2 | 2850 | 175.93 |
| Null Talisman | 4.05 | 505 | 124.69 |
| Phylactery | 8.1 | 2600 | 320.99 |
| Spirit Vessel | 13.5 | 2725 | 201.85 |
| Ultimate Orb | 20.25 | 2800 | 138.27 |
| Urn of Shadows | 2.7 | 825 | 305.56 |
| Wraith Band | 4.05 | 505 | 124.69 |

Values do not include portions from actives or auras.

| Related talent pages |
|---|
| Strength Talents |
| Agility Talents |
| Intelligence Talents |
| All Attributes Talents |

[corpus:liquipedia_dota2/attack_damage@2401047#Universal]

### Reducing sources

Some abilities reduce Main Attack Damage by percentages, while others manipulate the hero’s primary attribute and therefore reduce Main Attack Damage:

| Main Attack Damage Reducing Source |
|---|
| Lycan – Howl |
| Medusa – Split Shot |
| Morphling – Attribute Shift (Strength Gain) |
| Rubick – Fade Bolt |
| Silencer – Glaives of Wisdom |
| Slark – Essence Shift |
| Tidehunter – Anchor Smash |
| Timbersaw – Whirling Death |
| Underlord – Atrophy Aura |
| Undying – Decay |
| Windranger – Focus Fire |

1 Requires talent.  
2a Requires Aghanim’s Scepter.  
2b Requires Aghanim’s Shard. [corpus:liquipedia_dota2/attack_damage@2401047#Reducing_Sources]

## Base Attack Damage

Base Attack Damage is the part of Main Attack Damage that remains the same throughout a game. It consists of minimum and maximum values; whenever an attack is issued, a random value between them is chosen to help determine its damage.

Chaos Knight’s Base Attack Damage ranges between 32 – 52. This range of 20 always remains part of his attack calculations, regardless of his attributes or Bonus Attack Damage.

| Base Attack Damage Increasing Source |
|---|
| Arc Warden – Magnetic Field (Disorder) |
| Terrorblade – Metamorphosis |
| Tiny – Tree Grab |
| Tiny – Grow |
| Vengeful Spirit – Wave of Terror¹ |

1 Requires talent. [corpus:liquipedia_dota2/attack_damage@2401047#Base_Attack_Damage]

### Talents

The Base Attack Damage talent is passive, affects self, and has a Base Attack Damage Bonus that varies. It grants the hero a base attack damage bonus and is therefore affected by percentage-based damage-increasing and damage-reducing effects.

| Existing values |
|---|
| 15/20/25/30/40/45/50/100 |

It uses a hidden modifier. The talent table contains:

| Bonus | Level 10 Left | Level 10 Right | Level 15 Left | Level 15 Right | Level 20 Left | Level 20 Right | Level 25 Left | Level 25 Right |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Base Damage | +50 | +25 |  |  |  |  |  |  |

[corpus:liquipedia_dota2/attack_damage@2401047#Talents]

## Bonus Attack Damage

Bonus Attack Damage is the green damage value, with a plus sign on its left, displayed after the white damage number in a unit’s statistics. Whenever an item or ability grants `+Attack Damage`, such as Blades of Attack granting `+9 Damage`, it increases the affected unit’s Bonus Attack Damage.

Illusions benefit only from Main Attack Damage, although their HUD still displays the Bonus Attack Damage number as it does for other heroes, making them less obvious to enemies.

| Type | Effect |
|---|---|
| Flat Bonuses | Add a flat amount to the unit’s damage total, such as Phase Boots. |
| Main Attack Damage Percentage Bonuses | Add Bonus Attack Damage equal to a percentage of the affected unit’s Main Attack Damage, such as Vladmir’s Offering and Packleader’s Aura. These bonuses are usually positive but can be negative to reduce net attack damage, such as Static Link. |

Bonus Attack Damage is defined as:

`Bonus Attack Damage = ((Main Attack Damage × (1 + Bonus Modifiers1) × (1 + Bonus Modifiers2) × … × (1 + Bonus Modifiersn)) + Flat Bonus Values` [corpus:liquipedia_dota2/attack_damage@2401047#Bonus_Attack_Damage]

### Percentage bonuses

| Ability Granting Percentage Bonus |
|---|
| Alpha Wolf – Packleader's Aura |
| Earthshaker – Enchant Totem |
| Hellbear Smasher – Death Throe: Power |
| Lycan – Feral Impulse |
| Magnus – Empower |
| Marci – Bodyguard¹ |
| Marci – Sidekick¹ |
| Runes – Amplify Damage |
| Sven – God's Strength |
| Vengeful Spirit – Vengeance Aura |
| Visage – Silent as the Grave |
| Vladmir's Offering – Vladmir's Aura |

1 Requires facet. [corpus:liquipedia_dota2/attack_damage@2401047#Percentage_Bonuses]

## Attack Classes

There are currently 3 attack-damage classes, also known as Attack Classes. They cause attacks to deal reduced, increased, or unchanged damage against heroes, creeps—that is, non-hero units—and buildings before armor reduction.

The classes are represented by 3 abilities visible in the unit’s HUD. A unit without any of those abilities deals 100% damage, modified only by the target’s armor and other damage manipulators. [corpus:liquipedia_dota2/attack_damage@2401047#Attack_Classes]

### Runty

Runty is a passive classification affecting self. Runty units deal reduced attack damage to heroes, with a Hero Factor of 0.75. As an innate property, they deal reduced attack damage to Reinforced units, with a Unit Total Factor of 0.7.

It affects total attack damage. Reduction values are converted to multipliers for wiki calculation convenience. Runty units consider creep-heroes to be heroes and Roshan to be a creep. The hidden modifier is `modifier_creep_irresolute`. Devour-based abilities do not acquire this innate ability. [corpus:liquipedia_dota2/attack_damage@2401047#Runty]

### Piercing

Piercing is a passive classification affecting self. Piercing units deal reduced attack damage to heroes, with a Hero Factor of 0.5, and increased attack damage to creeps, with a Unit Factor of 1.5. As an innate property, they deal greatly reduced attack damage to Reinforced units, with a Unit Factor of 0.35.

It affects total attack damage. Reduction values are converted to multipliers for wiki calculation convenience. Piercing units consider creep-heroes to be heroes and Roshan to be a creep. The hidden modifier is `modifier_creep_piercing`, with `MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE`. Devour-based abilities do not acquire this innate ability. [corpus:liquipedia_dota2/attack_damage@2401047#Piercing]

### Reinforced

Reinforced is a passive classification affecting self. Reinforced units take less damage from heroes, illusions, and summoned units:

| Attacker | Factor |
|---|---:|
| Hero | 0.5 |
| Illusion | 0.6 |
| Summoned Unit | 0.9 |

They innately take less damage from Runty attacks, with a Runty Factor of 0.7, and from Piercing attacks, with a Piercing Final Factor of 0.35. They also deal greatly increased damage to Reinforced units, with a Reinforced Factor of 2.5.

It affects total attack damage. Reduction values are converted to multipliers for wiki calculation convenience. Reinforced units consider creep-heroes to be heroes and Roshan to be a creep.

| Considered summoned units |
|---|
| Summons |
| Dominated creeps |

| Not considered summoned units |
|---|
| creep-heroes |
| illusions |
| Ward-type units |

The hidden modifier is `modifier_creep_irresolute`. Devour-based abilities do not acquire this innate ability. [corpus:liquipedia_dota2/attack_damage@2401047#Reinforced]

### Attack Class definition

Attack damage against unit types is defined as:

`Attack Damage Dealt = Total Attack Damage × Attack Class × Damage Manipulation`

| Attack Class | Used by | Hero | Non-Hero | Reinforced |
|---|---|---:|---:|---:|
| Default | Heroes<br>Clones<br>Illusions<br>Creep-Heroes<br>Every single non-hero unit not explicitly listed in another attack class | 100% | 100% | 50% / 70% / 100% |
| Runty | Super Melee Creep<br>Mega Melee Creep<br>Flagbearer Creep<br>Super Flagbearer Creep<br>Mega Flagbearer Creep<br>Demonic Warrior<br>Melee Creep | 75% | 100% | 70% |
| Piercing | Ghost<br>Super Ranged Creep<br>Mega Ranged Creep<br>Demonic Archer<br>Ranged Creep<br>Hill Troll Berserker<br>Hill Troll Priest<br>Vhoul Assassin<br>Harpy Scout<br>Harpy Stormcrafter<br>Hill Troll<br>Plague Ward<br>Serpent Ward | 50% | 150% | 35% |
| Reinforced | Siege Creep<br>Tower (Tier 1)<br>Tower (Tier 2)<br>Tower (Tier 3)<br>Tower (Tier 4)<br>Super Siege Creep<br>Mega Siege Creep<br>Fountain<br>Melee Barracks<br>Ranged Barracks | 100% | 100% | 250% |

[corpus:liquipedia_dota2/attack_damage@2401047#Attack_Class_Definition]

## Instant Attacks

Instant Attacks are abilities that use a hero’s regular attack-damage values as ability damage against target units or areas. They do not use the hero’s attack animation, are independent of attack speed, and ignore the regular downtime between attacks. Certain instant-attack abilities are unaffected by evasion. Unless configured otherwise, an instant attack from a ranged hero uses the hero’s regular attack projectile.

An instant attack performed while the hero is already attacking does not interfere with regular attacks. It also neither interrupts movement, cancels ability casts, nor stops channeling.

Because Instant Attacks skip the animation and go directly to the attack point, they cannot proc effects that react to the start of an attack, such as Untouchable or Moment of Courage. They can proc effects that react to attack hits, such as Counter Helix or Retaliate, subject to exceptions.

Instant Attacks may proc on-hit effects only when allowed. An Instant Attack that cannot proc attack modifiers cannot proc on-hit effects either. Evasion and blind fully affect Instant Attacks. Like regular attacks, most also reveal the attacking hero under Disguise and/or when attacking from the Fog of War, unless their ability notes state otherwise.

Instant Attack damage does not interact with Spell Lifesteal. Magic damage from attack modifiers interacts with Spell Lifesteal, excluding cleave. [corpus:liquipedia_dota2/attack_damage@2401047#Instant_Attacks]

| Source | Procs Battle Fury? | Procs other Attack Modifiers? | Has True Strike? | Ignores Disarm? | Also Prevented By | Breaks Invisibility? |
|---|---|---|---|---|---|---|
| Burning Barrage | NoYes [?] | Yes | Yes | Yes |  | NoYes |
| Starbreaker | No | Yes | Yes | Yes |  | Yes |
| Shadow Wave | NoYes [?] | Yes | No | No |  | Yes |
| Reciprocity [?] | NoYes [?] | No | No | Yes |  | NoYes [?] |
| Sleight of Fist | Yes | Yes | No | No |  | NoYes |
| Time Lock<br>Time Walk | Yes | Yes | No | Yes | Break | NoYes |
| Side Gunner | NoYes [?] | Yes | No | Yes | Break<br>Invisibility [?] | Yes |
| Acorn Shot | NoYes [?] | Yes | No | Yes |  | NoYes [?] |
| Tether | NoYes [?] | Yes | No | No | Stun | Yes |
| Double Trouble | NoYes [?] | Yes | No | Yes |  | Yes |
| Omnislash | Yes | Yes | No | Yes |  | Yes |
| Swiftslash | Yes | Yes | No | Yes |  | Yes |
| Echo Slash | No | Yes | No | Yes |  | NoYes [?] |
| Falcon Rush | Yes | Yes | No | Yes | Dispel | NoYes |
| Grappling Claw | Yes | Yes | No | No | Forced Movement | Yes |
| Kazurai Katana | Yes | Yes | Yes | Yes |  | Yes |
| Talon Toss | Yes | Yes | Yes | Yes |  | NoYes |
| Moment of Courage [?] | Yes | Yes | No | NoYes [?] | Break | Yes |
| Infest | NoYes [?] | Yes | No | Yes |  | NoYes |
| Lunar Orbit | NoYes [?] | No | Yes | Yes |  | NoYes [?] |
| God's Rebuke | No | Yes | Yes | Yes |  | Yes |
| Boundless Strike | No | Yes | Yes | Yes |  | Yes |
| Swashbuckle | Yes | Yes | Yes | Yes | Root<br>Forced Movement | Yes |
| Shield Crash | Yes | Yes | Yes | Yes |  | Yes |
| Stifling Dagger | Yes | Yes | Yes | Yes |  | Yes |
| Phase Shift | NoYes [?] | Yes | No | Yes |  | Yes |
| Dream Coil | NoYes [?] | Yes | No | Yes |  | NoYes |
| Blink Strike | Yes | Yes | No | Yes | CD [?]<br>Root<br>Spell Block | Yes |
| Tricks of the Trade | Yes | Yes | No | Yes | Root<br>[?] | NoYes |
| Stinger<br>Epicenter<br>Epicenter | No | Yes | Yes | Yes |  | NoYes |
| Glaives of Wisdom | NoYes [?] | Yes | No | Yes |  | Yes |
| Shadowraze | NoYes [?] | Yes | Yes | Yes |  | Yes |
| Assassinate | NoYes [?] | Yes | Yes | Yes |  | Yes |
| Anchor Smash | No | Yes | Yes | Yes |  | Yes |
| Anchor Smash | No | YesNo [?] | Yes | Yes | Break | Yes |
| Tree Throw | Yes | Yes | Yes | Yes |  | Yes |
| Tree Volley | Yes | Yes | Yes | Yes |  | Yes |
| Astral Step | No | Yes | Yes | Yes | Root | Yes |
| Geminate Attack | NoYes [?] | Yes | No | NoYes [?] | Break | NoYes |
| Shukuchi | NoYes [?] | Yes | No | Yes | Dispel | NoYes |

[corpus:liquipedia_dota2/attack_damage@2401047#Instant_Attacks]

### Secondary Attacks

Secondary Attacks do not interact with other Instant Attack sources.

| Source | Procs Battle Fury? | Procs other Attack Modifiers? | Has True Strike? | Ignores Disarm? | Also Prevented By | Breaks Invisibility? |
|---|---|---|---|---|---|---|
| Searing Arrows | NoYes [?] | Yes | No | No | Mana [?]<br>Unit-Type [?] | Yes |
| Sproink | NoYes [?] | Yes | No | No |  | Yes |
| Flak Cannon | NoYes [?] | NoYes [?] | No | No |  | Yes |
| Polycephaly | NoYes [?] | NoYes [?] | No | No | Chance-based<br>Unit-Type [?] | Yes |
| Gunslinger | NoYes [?] | Yes | No | No | Break<br>Chance-based | Yes |
| Split Shot | NoYes [?] | NoYes [?] | No | No | Break | Yes |
| Split Shot | NoYes [?] | Yes | No | No | Break | Yes |
| Lil' Shredder | NoYes [?] | Yes | No | No [?] | Dispel | Yes |
| Splitshot | NoYes [?] | No | No | No | Chance-based<br>Unit-Type [?] | Yes |
| Fervor | NoYes [?] | YesNo [?] | No | No | Break<br>Chance-based<br>Unit-Type[?] | Yes |
| Mass Serpent Ward | - | - | - | - | - | - |

Most Instant Attacks follow an intuitive disarm rule: an Instant Attack generated outside the normal attack animation ignores disarm, while one generated together with a normal attack animation, such as various multishot Instant Attacks, is not generated because the normal attack is not allowed. The few exceptions are highlighted in bold in the source table. [corpus:liquipedia_dota2/attack_damage@2401047#Secondary_Attacks]

### Attack-based projectiles

Some abilities produce attack-based projectiles that are technically not attacks. They use the source’s attack projectile, deal damage based on the attacking unit’s attack damage, and flag that damage as attack damage, but are otherwise treated as regular ability projectiles, such as Magic Missile. Consequently, they cannot trigger attack modifiers or on-hit effects and ignore evasion and blind. They continue to use projectiles even when their source is a melee hero.

These “attacks” do not break invisibility from any source and do not reveal their attackers through the Fog of War.

| Spell damage-based attack that procs some Attack Modifiers |
|---|
| Luna – Moon Glaives³ |
| Storm Spirit – Overload¹ ⁴ |
| Witch Doctor – Death Ward²ᵃ ⁵ |
| Witch Doctor – Voodoo Switcheroo²ᵃ ⁵ |

1 Requires Talent.  
2a Requires Aghanim’s Scepter.  
3 Interacts with Spell Lifesteal, but not with Lifesteal.  
4 Bounce attack damage does not interact with Lifesteal or Spell Lifesteal. Overload damage interacts with Spell Lifesteal. [corpus:liquipedia_dota2/attack_damage@2401047#Attack-based_Projectiles]

### Attack Immunity

Ranged Instant Attacks may target attack-immune units but have no effect if the unit remains attack immune when the attack impacts. Instant melee attacks cannot target attack-immune units. [corpus:liquipedia_dota2/attack_damage@2401047#Attack_Immunity]

## Conditional Attack Damage Bonus

Conditional Attack Damage Bonuses grant direct attack-damage bonuses under certain circumstances. They are not displayed in the HUD, and their damage type is not restricted to physical damage. They are nevertheless attack damage because they are dealt in the same instance as the unit’s attack damage.

They are affected by Attack Classes even when dealing magical or pure damage. Percentage-based attack-damage bonuses and reductions do not affect them, but flat reductions such as Damage Block can reduce them.

### Physical damage

| Conditional Attack Damage Bonus |
|---|
| Anti-Mage – Mana Break |
| Diffusal Blade – Manabreak |
| Disperser – Manabreak |
| Demonic Warrior (Book of the Dead) – Mana Break |
| Demonic Warrior (Underlord) – Mana Break |
| Abyssal Blade – Bash |
| Skull Basher – Bash |
| Roshan – Bash |
| Slardar – Bash of the Deep |
| Battle Fury – Quell |
| Quelling Blade – Quell |
| Drow Ranger – Frost Arrows |
| Drow Ranger – Marksmanship |
| Earth – Demolish |
| Ember Spirit – Sleight of Fist |
| Hoodwink – Acorn Shot |
| Kunkka – Tidebringer |
| The Leveller – Demolish |
| Lifestealer – Feast |
| Lifestealer – Open Wounds |
| Mars – Bulwark²ᵃ ⁴ |
| Medusa – Mystic Snake²ᵃ ⁴ |
| Medusa – Cold Blooded²ᵃ ⁴ |
| Medusa – Stone Gaze |
| Riki – Cloak and Dagger |
| Shadow Blade – Shadow Walk³ |
| Silver Edge – Shadow Walk³ |
| Sniper – Headshot |
| Spirit Bear – Demolish |
| Storm – Wind Walk³ |
| Tidehunter – Anchor Smash |
| Tiny – Tree Grab |
| Tusk – Tag Team |
| Ursa – Fury Swipes |

1 Requires a talent.  
2a Requires Aghanim’s Scepter.  
3b Requires Aghanim’s Shard.  
3 Grants Conditional Attack Damage Bonus on the attack that breaks invisibility.  
4 Damage amplified is considered Conditional Attack Damage Bonus for this ability. [corpus:liquipedia_dota2/attack_damage@2401047#Conditional_Attack_Damage_Bonus]

### Magical damage

| Conditional Attack Damage Bonus |
|---|
| Bloodthorn – Pierce |
| Javelin – Pierce |
| Monkey King Bar – Pierce |

[corpus:liquipedia_dota2/attack_damage@2401047#Magical_Attack_Damage_Bonus_2]

### Pure damage

| Conditional Attack Damage Bonus |
|---|
| Bloodseeker – Bloodrage²ᵇ |

1 Requires a talent.  
2a Requires Aghanim’s Scepter.  
2b Requires Aghanim’s Shard. [corpus:liquipedia_dota2/attack_damage@2401047#Pure_Attack_Damage_Bonus_2]

### Reducing sources

| Source | Effect |
|---|---|
| Axe – Counter Helix | Reduces the attack damage of debuffed enemies when they attack Axe. |
| Juggernaut – Blade Fury | During Blade Fury, Juggernaut’s attacks deal 0 damage except against wards and buildings. |

[corpus:liquipedia_dota2/attack_damage@2401047#Reducing_Sources_2]