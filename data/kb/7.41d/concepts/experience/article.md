---
title: Experience
kind: concept
patch: 7.41d
card:
  entity: experience
  sentences:
  - text: Experience (XP) is gathered only by heroes from enemy-unit deaths; accumulating
      64400 XP raises a hero from level 1 to maximum level 30, increasing base attributes
      and enabling ability, spell, and talent progression.
    marks:
    - corpus:liquipedia_dota2/experience@2404795
    - corpus:liquipedia_dota2/experience@2404795#Leveling
  - text: Each hero begins at level 1 with one free ability point.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Leveling
  - text: Each level has a set experience requirement rather than one determined by
      a formula.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Leveling
  - text: Experience is awarded within a 1500 radius when an enemy hero dies to any
      ally or an enemy non-hero unit dies to an allied or neutral creep.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Acquiring_Experience
  - text: The award is truncated and divided evenly among allied heroes in the area.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Acquiring_Experience
  - text: A hero must be alive to receive experience, but spell immunity, invulnerability,
      being hidden, and other status effects do not prevent receipt.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Acquiring_Experience
  - text: Except for Meepo Clones and the Vengeance Illusion, hero clones and illusions
      neither gain experience nor count toward sharing.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Exceptions
  - text: Hero-kill experience is always awarded to the killing player’s hero regardless
      of its distance from the death.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Hero_Kills
  - text: The hero-kill bounty formula is BountyXP = (100XP + 0.13 × DeadHeroXP) /
      n + StreakXP.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Hero_Kills
  - text: A streak-ending bonus rises from 13.75 × Level at streak length 3 to 110
      × Level at 10+, beyond which it does not increase.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Streak_Values
  - text: A denied lane creep grants enemies 50% of its experience bounty instead
      of 100%.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Denying
  - text: Roshan grants 400 experience plus 20 every minute.
    marks:
    - corpus:liquipedia_dota2/experience@2404795#Roshan
---

# Experience

## Overview

Experience (XP) is gathered by heroes by killing enemy units or being present when enemy units are killed. Experience has no effect on its own, but accumulating it increases a hero’s level. Only heroes can gather experience and reach higher levels. Levels increase base attributes by static values; they can also allow heroes to learn abilities, improve learned spells, and learn talents that improve stats or abilities. [corpus:liquipedia_dota2/experience@2404795]

## Leveling

Each hero begins at level 1 with one free ability point. Acquiring the required experience increases the hero’s level and attributes by fixed, hero-specific amounts. Further ability points can be used to learn or improve abilities, gain additional attributes, or learn talents at eligible levels. Ability points can be saved while gaining multiple levels.

Each level has a set experience requirement rather than one determined by a formula. Heroes can gain a total of 29 levels, making level 30 the highest possible level.

| Hero level | Total XP | XP needed | Unlocks |
|---:|---:|---:|---|
| 1 | 0 | 240 | |
| 2 | 240 | 400 | |
| 3 | 640 | 520 | |
| 4 | 1160 | 600 | Lvl 1 Divided We Stand |
| 5 | 1760 | 680 | |
| 6 | 2440 | 760 | Lvl 1 Ultimate |
| 7 | 3200 | 800 | |
| 8 | 4000 | 900 | |
| 9 | 4900 | 1000 | |
| 10 | 5900 | 1100 | 1 |
| 11 | 7000 | 1200 | Lvl 2 Divided We Stand |
| 12 | 8200 | 1300 | Lvl 2 Ultimate |
| 13 | 9500 | 1400 | |
| 14 | 10900 | 1500 | |
| 15 | 12400 | 1600 | 2 |
| 16 | 14000 | 1700 | |
| 17 | 15700 | 1800 | |
| 18 | 17500 | 1900 | Lvl 3 Ultimate |
| 19 | 19400 | 2000 | |
| 20 | 21400 | 2200 | 3 |
| 21 | 23600 | 2400 | |
| 22 | 26000 | 2600 | |
| 23 | 28600 | 2800 | |
| 24 | 31400 | 3000 | |
| 25 | 34400 | 4000 | 4 |
| 26 | 38400 | 5000 | |
| 27 | 43400 | 6000 | 1 |
| 28 | 49400 | 7000 | 2 |
| 29 | 56400 | 8000 | 3 |
| 30 | 64400 | - | 4 |

[corpus:liquipedia_dota2/experience@2404795#Leveling]

## Acquiring Experience

Experience is awarded within a 1500 radius when an enemy hero dies to any ally or when an enemy non-hero unit, including a creep or summon, dies to an allied or neutral creep. It is truncated and split evenly among all allied heroes in the area. Each hero therefore receives less when more heroes are present. Experience is wasted if no hero is nearby; level-30 heroes also take a share while in range, effectively wasting it.

Units with Reincarnation grant no experience when they die. Summons and illusions grant no experience when their duration expires naturally.

Heroes must be alive to receive experience. Spell immunity, invulnerability, being hidden, and other status effects do not prevent experience gain. [corpus:liquipedia_dota2/experience@2404795#Acquiring_Experience]

### Exceptions

Except for Meepo Clones and the Vengeance Illusion, hero clones and illusions neither gain experience nor count toward experience sharing. The Vengeance Illusion is treated as an allied hero in the area, so experience is split evenly between her and her allies. [corpus:liquipedia_dota2/experience@2404795#Exceptions]

### Hero Kills

Hero-kill experience is split among all present heroes. Unlike experience from non-hero kills, it is always awarded to the hero belonging to the player who made the kill, regardless of distance. If a player kills an enemy hero from outside the experience radius through a global spell or controlled unit while an ally is within the radius, the experience is split between the killing player’s hero and the allied player’s hero, regardless of the ally’s contribution.

| Hero-kill value | Amount |
|---|---:|
| Base XP | 100 |
| Factor XP | 0.13 |

`BountyXP = (100XP + 0.13 × DeadHeroXP) / n + StreakXP`

For every 7.69 experience the dying hero has, their experience bounty increases by 1, starting with a base experience of 100. The bounty does not increase past level 25.

| Dead hero level | Possible current XP of dead hero | Possible XP bounty of dead hero |
|---:|---:|---:|
| 1 | 0 - 239 | 100 - 131.07 |
| 2 | 240 - 639 | 131.2 - 183.07 |
| 3 | 640 - 1159 | 183.2 - 250.67 |
| 4 | 1160 - 1759 | 250.8 - 328.67 |
| 5 | 1760 - 2439 | 328.8 - 417.07 |
| 6 | 2440 - 3199 | 417.2 - 515.87 |
| 7 | 3200 - 3999 | 516 - 619.87 |
| 8 | 4000 - 4899 | 620 - 736.87 |
| 9 | 4900 - 5899 | 737 - 866.87 |
| 10 | 5900 - 6999 | 867 - 1009.87 |
| 11 | 7000 - 8199 | 1010 - 1165.87 |
| 12 | 8200 - 9499 | 1166 - 1334.87 |
| 13 | 9500 - 10899 | 1335 - 1516.87 |
| 14 | 10900 - 12399 | 1517 - 1711.87 |
| 15 | 12400 - 13999 | 1712 - 1919.87 |
| 16 | 14000 - 15699 | 1920 - 2140.87 |
| 17 | 15700 - 17499 | 2141 - 2374.87 |
| 18 | 17500 - 19399 | 2375 - 2621.87 |
| 19 | 19400 - 21399 | 2622 - 2881.87 |
| 20 | 21400 - 23599 | 2882 - 3167.87 |
| 21 | 23600 - 25999 | 3168 - 3479.87 |
| 22 | 26000 - 28599 | 3480 - 3817.87 |
| 23 | 28600 - 31399 | 3818 - 4181.87 |
| 24 | 31400 - 34399 | 4182 - 4571.87 |
| 25 - 30 | 34400 | 4572 |

[corpus:liquipedia_dota2/experience@2404795#Hero_Kills]

### Streak Values

Ending a killed hero’s killing streak awards bonus experience on top of the default value. The bonus depends on the killed hero’s level and does not increase past **beyond GODLIKE**.

`f(x) = (1.25x2 - 2.5x + 10) × L`

| Streak length | Streak name | Streak value (XP) |
|---:|---|---:|
| 0, 1, 2 | N/A | 0 |
| 3 | Player is on a killing spree | 13.75 × Level |
| 4 | Player is dominating | 20 × Level |
| 5 | Player is on a mega Kill streak | 28.75 × Level |
| 6 | Player is unstoppable! | 40 × Level |
| 7 | Player is wicked sick | 53.75 × Level |
| 8 | Player is on a monster kill streak | 70 × Level |
| 9 | Player is GODLIKE | 88.75 × Level |
| 10+ | Player is beyond GODLIKE, someone kill them!! | 110 × Level |

Announcer responses are customizable. [corpus:liquipedia_dota2/experience@2404795#Streak_Values]

### Denying

When a hero is denied by an ally or by itself, enemies around it receive 0% experience. Heroes killed by neutral creeps are treated the same way.

Enemies also receive 0% experience when other player-controlled units are denied. A summon killed by neutral creeps does not count as denied and grants its default experience bounty.

A denied lane creep grants enemies 50% of its experience bounty instead of 100%. Lane creeps killed by neutral creeps do not count as denied and grant their default experience bounty. [corpus:liquipedia_dota2/experience@2404795#Denying]

### Experience-Granting Abilities

Some abilities award experience when used.

| Source | Ability | Experience value | Effect |
|---|---|---|---|
| Hand of Midas | Transmute | Experience Bonus Multiplier | Multiplies the target’s experience value. |
| Helm of the Dominator | Dominate | Dominate Experience Bounty: 50% | Grants the target’s experience value. |
| Helm of the Overlord | Dominate | Dominate Experience Bounty: 100% | Grants the target’s experience value. |
| Shrine of Wisdom | Experience Fountain | Base Experience Gain: 280; Experience Gain per Interval: 280 | Stand nearby the Shrine of Wisdom to start gathering the experience. |

[corpus:liquipedia_dota2/experience@2404795#Experience_Granting_Abilities]

### Talents

Experience Gain is a passive ability that affects self. It increases all experience gained by the hero by a percentage, uses a hidden modifier, and has a varying experience multiplier.

| Existing experience-multiplier values |
|---|
| 5%/10%/15%/20%/25%/30%/35%/40%/50%/60% |

Heroes can have a talent that grants increased experience gain. [corpus:liquipedia_dota2/experience@2404795#Talents]

## Other Experience Sources

Most creeps have a fixed experience value, including lane creeps and most summoned units. Buildings grant no experience.

Each neutral creep has a unique base value that remains the same throughout the match. Neutral creeps spawned through stacking have a 15% penalty to their experience bounty. Roshan’s experience bounty increases by 20 every minute. Neutral creeps grant experience to both teams regardless of who kills them, splitting it evenly among all present heroes. [corpus:liquipedia_dota2/experience@2404795#Other_Experience_Sources]

### Lane Creeps

| Creep | Experience |
|---|---:|
| Melee Creep | 57 |
| Ranged Creep | 69 |
| Siege Creep | 88 |
| Super Melee Creep | 25 |
| Super Ranged Creep | 22 |
| Super Siege Creep | 88 |
| Mega Melee Creep | 25 |
| Mega Ranged Creep | 22 |

[corpus:liquipedia_dota2/experience@2404795#Lane_Creeps]

### Neutral Creeps

| Creep | Experience |
|---|---:|
| Kobold | 14 |
| Kobold Soldier | 17 |
| Kobold Foreman | 30 |
| Hill Troll Berserker | 28 |
| Hill Troll Priest | 28 |
| Vhoul Assassin | 30 |
| Fell Spirit | 26 |
| Ghost | 42 |
| Harpy Scout | 26 |
| Harpy Stormcrafter | 42 |
| Centaur Courser | 32 |
| Centaur Conqueror | 90 |
| Giant Wolf | 40 |
| Alpha Wolf | 60 |
| Satyr Banisher | 24 |
| Satyr Mindstealer | 46 |
| Satyr Tormenter | 90 |
| Ogre Bruiser | 32 |
| Ogre Frostmage | 48 |
| Mud Golem | 32 |
| Shard Golem | 18 |
| Hellbear | 66 |
| Hellbear Smasher | 90 |
| Wildwing | 26 |
| Wildwing Ripper | 90 |
| Hill Troll | 42 |
| Dark Troll Summoner | 90 |
| Skeleton Warrior | 4 |
| Warpine Raider | 76 |
| Ancient Black Drake | 95 |
| Ancient Black Dragon | 124 |
| Ancient Rock Golem | 95 |
| Ancient Granite Golem | 124 |
| Ancient Rumblehide | 95 |
| Ancient Thunderhide | 124 |

[corpus:liquipedia_dota2/experience@2404795#Neutral_Creeps]

### Roshan

| Unit | Experience |
|---|---|
| Roshan | 400 + 20 every minute |

[corpus:liquipedia_dota2/experience@2404795#Roshan]

### Summons

| Source | Unit | Experience |
|---|---|---:|
| Beastmaster | Raptor | 40/50/60/70 |
| Beastmaster | Razorback | 60/70/80/90 |
| Brewmaster | Earth | 0 |
| Brewmaster | Storm | 0 |
| Brewmaster | Fire | 0 |
| Brewmaster | Void | 0 |
| Broodmother | Spiderling | 9 |
| Broodmother | Spiderite | 3 |
| Clockwerk | Power Cog | 0 |
| Enigma | Eidolon | 10 |
| Gyrocopter | Homing Missile | 20 |
| Invoker | Forged Spirit | 31 |
| Juggernaut | Healing Ward | 75 |
| Lone Druid | Spirit Bear | 165 + 10 |
| Lycan | Lycan Wolf | 20 |
| Nature's Prophet | Treant | 12 |
| Nature's Prophet | Greater Treant | 30/40/50/60 |
| Phoenix | Phoenix Sun | 0 |
| Pugna | Nether Ward | 0 |
| Shadow Shaman | Serpent Ward | 31 |
| Techies | Proximity Mine | 0 |
| Techies | Stasis Trap | 6 |
| Techies | Remote Mine | 6 |
| Templar Assassin | Psionic Trap | 0 |
| Undying | Tombstone | 0 |
| Undying | Undying Zombie | 0 |
| Venomancer | Plague Ward | 20/25/30/35 |
| Visage | Familiar | 41 |
| Warlock | Warlock Golem | 98 |
| Weaver | Beetle | 20 |
| Zeus | Nimbus | 0 |
| Book of the Dead | Demonic Warrior | 150 |
| Book of the Dead | Demonic Archer | 150 |
| Observer Ward | Observer Ward | 70 |
| Sentry Ward | Sentry Ward | 0 |

[corpus:liquipedia_dota2/experience@2404795#Summons]

### Special

| Source | Unit | Experience |
|---|---|---|
| Arc Warden | Tempest Double | 70 10 |

[corpus:liquipedia_dota2/experience@2404795#Special]

## Recent Changes

| Version | Date | Description |
|---|---|---|
| 7.32 | 2022-08-24 | Changed the kill-streak experience bonus formula from `(StreakLength² - StreakLength + 8) × DeadHero LVL` to `(1.25 × StreakLength² - 2.5 × StreakLength + 10) × DeadHero LVL`. Watch Tower no longer grants `2 × GameTime` experience. |
| 7.31 | 2022-02-23 | Changed the kill-streak experience bonus formula from `(StreakLength - 1) × 10 × DeadHero LVL` to `(StreakLength² - StreakLength + 8) × DeadHero LVL`. |
| 7.29 | 2021-04-09 | Watch Tower: Changed the experience-gain formula from `20 /min - 50` to `2 /min`. Reduced the experience-gain interval from `600` to `60`. Compared with the previous version at `10/20/30/40` minutes, total experience per player changed from `150 / 500 / 1050 / 1800 XP` to `110 / 420 / 930 / 1640 XP`. |

[corpus:liquipedia_dota2/experience@2404795#Recent_Changes]