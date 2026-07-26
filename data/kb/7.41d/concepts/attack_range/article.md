---
title: Attack Range
kind: concept
patch: 7.41d
card:
  entity: attack_range
  sentences:
  - text: Attack range is the maximum distance over which a normal attack can hit;
      it does not determine melee or ranged classification, and most melee heroes
      have a base attack range of 150.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555
    - corpus:liquipedia_dota2/attack_range@2376555#Heroes_2
  - text: Base attack range is assigned individually to each unit and can be modified
      by bonuses appropriate to its attack-range type.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Base_Attack_Range
  - text: For normal attacks, actual attack range equals total attack range plus the
      attacker and target bound radii.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Motion_Buffer
  - text: The default motion buffer is 250 and prevents attacks or unit-targeted abilities
      from canceling when the target moves out of range before the attack point.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Motion_Buffer
  - text: For most melee heroes, total melee buffer range equals total attack range
      plus both units’ bound radii plus 350.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Miss_Chance
  - text: An attack beyond the melee buffer misses 100%, and True Strike does not
      guarantee a hit there.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Miss_Chance
  - text: Ranged units have a 25% uphill miss chance regardless of the terrain-level
      difference.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Miss_Chance
  - text: Acquisition range governs automatic attacks against visible enemies and
      defaults to 600 for melee heroes and 800 for ranged heroes.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Acquisition_Range
  - text: 'Percentage attack-range reductions are applied after flat changes: (base
      attack range ± flat values) × percentage multipliers.'
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Reducing_Sources
  - text: An active attack modifier’s cast range is based on attack range, accepts
      matching attack-range bonuses, and ignores cast-range bonuses.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Active_Attack_Modifiers
  - text: Depending on the ability, manual casting may use cast range while Autocast
      uses the hero’s attack range.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Active_Attack_Modifiers
  - text: Shapeshift and Wolf Bite set base attack range to 150, while Tree Grab sets
      it to 300.
    marks:
    - corpus:liquipedia_dota2/attack_range@2376555#Set_Base_Attack_Range
---

# Attack Range

Attack range is the maximum distance over which a normal attack can hit. It does not determine whether a unit is classified as ranged or melee; that characteristic is assigned individually, so a melee unit can have a higher attack range than a ranged unit. [corpus:liquipedia_dota2/attack_range@2376555]

## Definitions

Some heroes can switch between melee and ranged forms, allowing them to benefit from both forms for a timed duration. [corpus:liquipedia_dota2/attack_range@2376555#Definitions]

| Range type | Area | Mechanics |
|---|---|---|
| Melee | Attacks | Hits the target instantly upon reaching the attack point. |
| Melee | Attacks | If an enemy is close enough to the edge to be within the hero’s range, the hero can attack up cliffs. |
| Melee | Attacks | Attacks can use Cleave. |
| Melee | Damage Block | Damage Block is innate to melee heroes. |
| Melee | Miscellaneous | Receives an attack-range bonus when attacking Observer and Sentry Wards. |
| Melee | Miscellaneous | Flying Couriers receive additional damage from melee heroes. |
| Melee | Miscellaneous | Certain restrictions may apply to item bonuses. |
| Ranged | Attacks | Uses a ranged attack projectile and projectile speed. |
| Ranged | Attacks | Projectile landing time is defined as `BaseProjectileSpeed / DistanceBetweenTarget`. |
| Ranged | Attacks | The projectile can be disjointed. |
| Ranged | Attacks | Certain restrictions may apply to item bonuses. |
| Ranged | Miscellaneous | Certain restrictions may apply to item bonuses. |

[corpus:liquipedia_dota2/attack_range@2376555#Definitions]

The listed attack-range types are:

| Range type |
|---|
| Ranged |
| Melee |

[corpus:liquipedia_dota2/attack_range@2376555#Heroes]

### Miss Chance

The definitions summary states that when an enemy is 350 range farther than a melee attacker’s range, the attack—including an instant attack—always misses unless it has True Strike. [corpus:liquipedia_dota2/attack_range@2376555#Definitions]

The detailed miss rule states that if a target is farther than 350 range beyond a melee unit’s attack range, the attack misses 100%; True Strike does not guarantee a hit outside this buffer range. For most melee heroes:

`Total Melee Buffer Range = Unit Total Attack Range + Attacker Bound Radius + Target Bound Radius + 350` [corpus:liquipedia_dota2/attack_range@2376555#Miss_Chance]

Ranged units have a 25% chance to miss when attacking from a lower terrain level than the target, regardless of the difference in terrain level. A unit is considered to be on higher terrain when terrain causes it to no longer be visible to the player. When an enemy stands on a relatively higher ramp, the uphill miss chance applies whether or not the attacked unit is within vision. [corpus:liquipedia_dota2/attack_range@2376555#Miss_Chance]

### Motion Buffer

The default attack-range motion buffer is 250. It prevents normal attacks and unit-targeted abilities from canceling when the target moves out of attack range or before the attack point is reached. For normal attacks:

`Actual Attack Range = Total Attack Range + Attacker Bound Radius + Target Bound Radius` [corpus:liquipedia_dota2/attack_range@2376555#Motion_Buffer]

#### Tower attacking Marci

| Component | Value |
|---|---:|
| Tower (Tier 1) attack range | 700 |
| Tower (Tier 1) bound radius | 144 |
| Marci bound radius | 24 |
| Maximum attack range against Marci | `700 + 144 + 24 = 868` |

The Tower has a maximum attack range of 868 against Marci. Because the Tower cannot move, the 250 attack-range buffer does not apply. [corpus:liquipedia_dota2/attack_range@2376555#Motion_Buffer]

#### Muerta attacking Marci, with attack buffer range

| Component | Value |
|---|---:|
| Muerta attack range | 575 |
| Muerta bound radius |  |
| Marci bound radius | 24 |
| Motion buffer distance | 250 |
| Maximum attack range against Marci | `575 + 24 + 24 = 623` |

Muerta has a maximum attack range of 623 against Marci, and her attack cancels when Marci is beyond 873 distance from her. Units with a smaller bound radius therefore have a lower actual attack-range value against them. [corpus:liquipedia_dota2/attack_range@2376555#Motion_Buffer]

### Acquisition Range

Acquisition range determines how close a visible enemy must get before a unit attacks it automatically. Because it applies only to automatic attacks, it has no influence on units whose auto-attack option is set to `◎ Never`. The default is 600 for melee heroes and 800 for ranged heroes, with some exceptions mainly caused by abilities. [corpus:liquipedia_dota2/attack_range@2376555#Acquisition_Range]

| Category | Hero or condition | Acquisition range |
|---|---|---:|
| Melee | Melee Heroes | 600 |
| Ranged | Ranged Heroes | 800 |
| — | Sniper with Take Aim learned | 950 |
| — | Rubick in True Form or Berserker’s Rage ranged form | 800 |
| — | Dragon Knight in Elder Dragon Form | 600 |
| — | Lone Druid in True Form | 600 |
| — | Terrorblade in Metamorphosis form | 600 |

[corpus:liquipedia_dota2/attack_range@2376555#Acquisition_Range]

## Base Attack Range

Base attack range is a fixed value assigned individually to each unit. Attack-range bonuses can further modify it according to the unit’s attack-range type. [corpus:liquipedia_dota2/attack_range@2376555#Base_Attack_Range]

### Heroes

Most melee heroes have 150 attack range. The hero attack-range table contains the following values:

| Attack range |
|---:|
| 150 |
| 170 |
| 175 |
| 200 |
| 225 |
| 250 |
| 300 |
| 330 |
| 350 |
| 365 |
| 380 |
| 400 |
| 425 |
| 450 |
| 475 |
| 480 |
| 500 |
| 525 |
| 550 |
| 575 |
| 600 |
| 620 |
| 625 |
| 630 |
| 650 |
| 670 |
| 675 |

[corpus:liquipedia_dota2/attack_range@2376555#Heroes_2]

### Creeps

| Unit | Attack range |
|---|---:|
| Minor Imp | 80 |
| Giant Wolf, Alpha Wolf, Skeleton Warrior, Lycan Wolf | 90 |
| Warpine Raider, Ancient Frostbitten Golem, Pollywog, Boglet, Croaker, Ancient Croaker, Demonic Warrior, Kobold, Kobold Soldier, Fell Spirit, Centaur Courser, Centaur Conqueror, Satyr Mindstealer, Ogre Bruiser, Ogre Frostmage, Mud Golem, Satyr Tormenter, Hellbear, Hellbear Smasher, Ancient Rock Golem, Shard Golem, Spiderling, Ancient Prowler Acolyte, Ancient Prowler Shaman | 100 |
| Kobold Foreman | 110 |
| Wraith King Skeleton | 115 |
| Zealot, Treant | 125 |
| Undying Zombie, Wildwing, Wildwing Ripper, Ancient Granite Golem | 128 |
| Roshan | 150 |
| Marshmage Apprentice, Marshmage, Hill Troll, Dark Troll Summoner | 250 |
| Satyr Banisher | 280 |
| Harpy Scout, Ancient Black Drake, Ancient Black Dragon, Ancient Rumblehide, Ancient Thunderhide | 300 |
| Ghost | 400 |
| Eidolon | 425/450/475/500 |
| Harpy Stormcrafter | 450 |
| Ancient Ice Shaman, Ancient Marshmage, Hill Troll Berserker, Vhoul Assassin | 500 |
| Demonic Archer, Razorback | 550 |
| Hill Troll Priest | 600 |

[corpus:liquipedia_dota2/attack_range@2376555#Creeps]

### Summons

| Unit | Attack range |
|---|---:|
| Earth, Fire | 150 |
| Familiar | 180 |
| Warlock Golem | 225 |
| Storm | 600 |

[corpus:liquipedia_dota2/attack_range@2376555#Summons]

## Modifying Attack Range

### Spell Steal

Most abilities acquired through Spell Steal that modify attack range fully affect Rubick’s attack range for their duration when stolen and used. Elder Dragon Form and Metamorphosis are exceptions. [corpus:liquipedia_dota2/attack_range@2376555#Spell_Steal]

### Increasing Sources

This list includes certain active attack modifiers that grant attack-range bonuses. The cast range of an active attack modifier can be increased only by attack-range bonuses matching the caster’s range type. [corpus:liquipedia_dota2/attack_range@2376555#Increasing_Sources]

| Attack-range increasing source |
|---|
| Ancient Apparition – Chilling Touch |
| Dragon Knight – Elder Dragon Form |
| Drow Ranger – Glacier |
| Hoodwink – Acorn Shot<sup>3</sup> |
| Snapfire – Lil’ Shredder |
| Sniper – Take Aim |
| Templar Assassin – Psi Blades |
| Terrorblade – Metamorphosis |
| Terrorblade – Terror Wave<sup>2a</sup> |
| Winter Wyvern – Arctic Burn |
| Viper – Poison Attack<sup>3</sup> |

| Marker | Requirement or limitation |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |
| 3 | Applies only to the ability’s projectiles. |

[corpus:liquipedia_dota2/attack_range@2376555#Increasing_Sources]

#### Ranged Heroes

The following sources affect only ranged heroes:

| Ranged attack-range increasing source |
|---|
| Dark Willow – Shadow Realm |
| Dragon Lance – Dragon’s Reach |
| Enchanted Quiver – Ranged Attack Range Bonus |
| Enchanted Quiver – Certain Strike |
| Telescope – Prescient Aura |
| Grove Bow – Ranged Attack Range Bonus |
| Hurricane Pike – Dragon’s Reach |
| Hurricane Pike – Hurricane Thrust |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |

[corpus:liquipedia_dota2/attack_range@2376555#Ranged_Heroes]

#### Talents

Attack Range is passive, affects self, has a varying attack-range bonus, and increases the hero’s attack range. Its status effect is a hidden modifier. [corpus:liquipedia_dota2/attack_range@2376555#Talents]

| Existing attack-range bonus values |
|---|
| 50 |
| 75 |
| 100 |
| 125 |
| 150 |
| 175 |
| 200 |
| 250 |
| 275 |
| 300 |
| 325 |
| 400 |

[corpus:liquipedia_dota2/attack_range@2376555#Talents]

The attack-range talent listing is organized into Left and Right choices at levels 10, 15, 20, and 25, and contains the bonus entries `+75`, `+50`, and `+175`. [corpus:liquipedia_dota2/attack_range@2376555#Talents]

| Hero | Talent | Listed effect |
|---|---|---|
| Shadow Shaman | Level 15 Right | `+160 Serpent Ward Attack Range:` |
| Witch Doctor | Level 20 Right | `Maledict Radius Damage On Every Burst:` |

[corpus:liquipedia_dota2/attack_range@2376555#Talents]

#### Melee Heroes

There are no attack-range-increasing sources that affect only melee heroes. [corpus:liquipedia_dota2/attack_range@2376555#Melee_Heroes]

### Reducing Sources

Percentage-based reductions are calculated after all flat values:

`Σ Attack Range = (Base Attack Range ± Σ Flat Values) × %-Attack Range Multipliers` [corpus:liquipedia_dota2/attack_range@2376555#Reducing_Sources]

| Attack-range reducing source |
|---|
| Lone Druid – True Form |
| Troll Warlord – Berserker’s Rage |
| Tinker – Warp Flare |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |

[corpus:liquipedia_dota2/attack_range@2376555#Reducing_Sources]

### Set Base Attack Range

These abilities set the caster’s or affected unit’s attack range to a specified value:

| Ability | Set base attack range | Effect |
|---|---:|---|
| Lycan – Shapeshift | 150 | Shapeshifts the caster into a melee wolf. |
| Lycan – Wolf Bite | 150 | Shapeshifts the affected target into a melee wolf. |
| Tiny – Tree Grab | 300 | Sets the caster’s attack range to the specified value. |

[corpus:liquipedia_dota2/attack_range@2376555#Set_Base_Attack_Range]

### Active Attack Modifiers

The cast range of every active attack modifier-based ability is based on the caster’s attack range. It can be further increased by attack-range bonuses matching the caster’s range type, including Dragon Lance for ranged heroes and Penta-Edged Sword for melee heroes, but is unaffected by cast-range bonuses. [corpus:liquipedia_dota2/attack_range@2376555#Active_Attack_Modifiers]

Depending on the ability, manual casting or use of the designated hotkey may use cast range, while Autocast uses the hero’s attack range. [corpus:liquipedia_dota2/attack_range@2376555#Active_Attack_Modifiers]

| Active attack modifier |
|---|
| Ancient Apparition – Chilling Touch<sup>5</sup> |
| Bounty Hunter – Jinada<sup>4, 5</sup> |
| Clinkz – Searing Arrows<sup>5</sup> |
| Doom – Infernal Blade<sup>7</sup> |
| Drow Ranger – Frost Arrows |
| Enchantress – Impetus |
| Huskar – Burning Spear |
| Jakiro – Liquid Fire<sup>5</sup> |
| Jakiro – Liquid Frost |
| Kunkka – Tidebringer<sup>4, 7</sup> |
| Omniknight – Hammer of Purity<sup>4, 5</sup> |
| Outworld Destroyer – Arcane Orb |
| Silencer – Glaives of Wisdom |
| Slark – Saltwater Shiv<sup>7</sup> |
| Tusk – Walrus PUNCH!<sup>5, 6</sup> |
| Treant Protector – Leech Seed<sup>4, 5</sup> |
| Viper – Poison Attack |
| Weaver – Geminate Attack<sup>4</sup> |

| Marker | Requirement or interaction |
|---|---|
| 1 | Requires a talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |
| 3 | Requires selecting the corresponding facet. |
| 4 | Can be further increased by both attack-range bonuses and cast-range bonuses. |
| 5 | Piercess Debuff & Spell Immunity. |
| 6 | Can target a spell-immune target, but will not go into cd and will not apply effects other than a normal attack. |

[corpus:liquipedia_dota2/attack_range@2376555#Active_Attack_Modifiers]

## Recent Changes

| Version | Date | Change |
|---|---|---|
| 7.30c | 2021-09-11 | Clinkz’s attack range reduced from 625 to 600. |
| 7.29 | 2021-04-09 | Underlord’s attack range increased from 175 to 200. |
| 7.29 | 2021-04-09 | Pudge’s attack range increased from 150 to 175. |
| 7.27b | 2020-07-15 | Doom’s attack range increased from 175 to 200. |

[corpus:liquipedia_dota2/attack_range@2376555#Recent_Changes]