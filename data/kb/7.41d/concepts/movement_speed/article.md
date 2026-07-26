---
title: Movement Speed
kind: concept
patch: 7.41d
card:
  entity: movement_speed
  sentences:
  - text: Movement Speed, or Move Speed, is the speed or distance a mobile unit moves
      over a second, with default limits of 100 and 550 and flat or percentage-based
      modifiers from abilities, items, and talents.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420
  - text: Every movable unit has a fixed base movement speed that only Set Movement
      Speed sources can alter.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Base_Movement_Speed
  - text: Total Move Speed equals `(Base + MAX(Boots of Speed-based) + Flat Changes)
      × Move Speed Multiplier`, where the multiplier equals `1 + Percentage-Based
      Changes + MAX(Yasha-%based)`.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Equations
  - text: Movement-speed limits apply after total calculation; a calculated value
      of 582.25 is capped at 550.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Stacking
  - text: Set Movement Speed replaces base movement speed with a fixed value but remains
      affected by flat and percentage changes and the movement-speed limits.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Set_Movement_Speed
  - text: Absolute Movement Speed becomes total movement speed and can be overridden
      only by Haste.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Total_Movement_Speed
  - text: Haste raises both movement-speed limits to a specified value, preventing
      the unit from being slowed below it.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Haste
  - text: Restricted movement-speed bonuses are divided into 4 groups; same-group
      flat bonuses do not stack, while bonuses from different groups stack independently.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Stacking
  - text: Percentage changes are applied after flat changes; item percentages have
      stacking restrictions, but ability percentage bonuses do not.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Percentage-Based_Changes
  - text: When several minimum-movement-speed effects apply, the higher minimum takes
      priority.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Minimum_Movement_Speed
  - text: Maximum-changing abilities can raise the maximum movement speed of 550,
      with the higher value taking priority when several apply.
    marks:
    - corpus:liquipedia_dota2/movement_speed@2383420#Maximum_Movement_Speed
---

# Movement Speed

Movement Speed, sometimes abbreviated as Move Speed, is the speed or distance at which a unit can move over a second. Its default limits are 100 and 550, although a few abilities can bypass them. Only mobile units can have movement speed; granting movement speed to a non-mobile unit does not let it move. Abilities, items, and talents can grant flat bonuses, such as Boots of Speed, or percentage-based bonuses, such as Yasha. [corpus:liquipedia_dota2/movement_speed@2383420]

## Definition

| Type | Effect | Listed examples |
|---|---|---|
| Set | Overrides the unit’s base movement speed with another value. Other bonuses and reductions can still affect it within the movement speed limits. | Tether; Hex |
| Absolute | Overrides the unit’s base movement speed with another value. The fixed value cannot be modified in any way. | Toggle Movement |
| Haste | Sets both the unit’s minimum and maximum movement speed to a value without respectively increasing or unlocking those limits. The unit is immune to movement-speed bonuses and reductions. Haste has higher priority than absolute movement-speed sources. | Shukuchi; Haste Rune |
| Base | Every unit that can move has a base movement speed. Other bonuses and reductions can still affect it within the movement speed limits. | — |
| % Bonus/Reductions | Movement-speed bonuses or reductions from abilities, items, and talents. Percentage-based values stack independently of each other. | Skeleton Walk |
| Flat Bonus/Reductions | Movement-speed bonuses or reductions from abilities, items, and talents. Flat values stack independently of each other with some restrictions. | Chemical Rage |
| Minimum | Sets minimum movement speed to a value and prevents movement speed from falling below it. It does not otherwise modify current movement speed. | Starbreaker |
| Unlock Maximum | Removes the maximum movement-speed limit without otherwise modifying current movement speed. | Thirst |

[corpus:liquipedia_dota2/movement_speed@2383420#Definition]

### Total Movement Speed

Calculating total movement speed uses several values and a multiplier. Set Movement Speed overrides original base movement speed but remains fully affected by flat and percentage-based changes within the movement-speed limits. If the set value is absolute, that absolute value becomes Total Movement Speed. Absolute Movement Speed can be overridden only by Haste. [corpus:liquipedia_dota2/movement_speed@2383420#Total_Movement_Speed]

Flat bonuses from items, abilities, and talents stack independently on base movement speed subject to restrictions. Percentage-based bonuses and reductions are summed and then applied to base movement speed as a multiplier. Movement-speed modifiers cannot exceed the minimum or maximum limits unless minimum-movement-speed or maximum-unlocking sources modify those limits. If minimum movement speed is higher than an absolute movement-speed value, the absolute source can set movement speed only to the unit’s new minimum. [corpus:liquipedia_dota2/movement_speed@2383420#Total_Movement_Speed]

The HUD calculation is presented as:

```text
Total Movement Speed
= Set Move Speed Value
= Absolute Move Speed Value
= Haste Value, when Haste > Min Move Speed; else Min Move Speed Value = Base Move Speed Value
= Base Move Speed Value
± Flat Bonuses/Reductions (with Stacking Restrictions)
× Move Speed Multiplier
```

[corpus:liquipedia_dota2/movement_speed@2383420#Total_Movement_Speed]

### Equations

```text
Total Move Speed = (Base + MAX( Boots of Speed-based) + Flat Changes) × Move Speed Multiplier
Move Speed Multipler = 1 + Percentage-Based Changes i + MAX( Yasha-%based)
Move Speed Range ⇒ { 100 ≤ x ≤ 550 }
```

[corpus:liquipedia_dota2/movement_speed@2383420#Equations]

### Stacking

Flat and percentage-based movement-speed bonuses, except percentage-based bonuses from abilities, have stacking restrictions divided into 4 groups. Flat bonuses from the same group do not stack; the higher value takes priority. Flat bonuses from different groups stack independently. [corpus:liquipedia_dota2/movement_speed@2383420#Stacking]

| Group | Category | Sources |
|---|---|---|
| Group 1 | Boots of Speed-group | Fleetfooted Enchantment (115) |
| Group 1 | Boots of Speed-group | Boots of Travel 2 (110) |
| Group 1 | Boots of Speed-group | Boots of Travel 1 (90) |
| Group 1 | Boots of Speed-group | Boots of Bearing (65) |
| Group 1 | Boots of Speed-group | Tranquil Boots (65) |
| Group 1 | Boots of Speed-group | Power Treads (55) |
| Group 1 | Boots of Speed-group | Guardian Greaves (50) |
| Group 1 | Boots of Speed-group | Phase Boots (50) |
| Group 1 | Boots of Speed-group | Power Treads (45) |
| Group 1 | Boots of Speed-group | Arcane Boots (45) |
| Group 1 | Boots of Speed-group | Boots of Speed (45) |
| Group 1 | Boots of Speed-group | Tranquil Boots (Broken) (40) |
| Group 1 | Boots of Speed-group | Horsepower (0.4 per strength) |
| Group 2 | Yasha-based | Sange and Yasha (12%) |
| Group 2 | Yasha-based | Yasha and Kaya (12%) |
| Group 2 | Yasha-based | Manta Style (10%) |
| Group 2 | Yasha-based | Yasha (10%) |
| Group 3 | Wind Lace | Wind Lace (15) |
| Group 4 | Misc | Eul’s Scepter of Divinity (20) |
| Group 4 | Misc | Solar Crest (25) |
| Group 4 | Misc | Wind Waker (30) |
| Group 4 | Misc | Neutral Items |
| Group 4 | Misc | Talents |
| Group 4 | Misc | Flat Bonuses/Reductions from Abilities |
| Group 4 | Misc | %Bonuses/Reductions from Abilities |

Miscellaneous sources do not belong to the first 3 groups and fully stack with each other, multiple copies of themselves, and other item bonuses, including Wind Lace. [corpus:liquipedia_dota2/movement_speed@2383420#Stacking]

#### Example 1a: Within the Movement-Speed Limits

With level 4 Windrun active and level 4 Tether affecting her, Windranger has Boots of Travel 2, Wind Waker, and Manta Style:

| Component | Value |
|---|---:|
| Base Move Speed | 285 |
| Boots of Travel 2 | 110 |
| Wind Waker | 30 |
| Windrun | 0.6 |
| Manta Style | 0.1 |
| Tether | 0.12 |

```text
Total Movement Speed
= (285 + 110 + 30) * (1 + 0.6 + 0.1 + 0.12)
= 773.5
```

The resulting 773.5 is capped at 550 unless something unlocks maximum movement speed. [corpus:liquipedia_dota2/movement_speed@2383420#Stacking]

#### Example 1b: Limits Apply After All Calculations

If Brewmaster casts level 3 Thunder Clap on the same Windranger:

| Modifier | Value |
|---|---:|
| Windrun | 0.6 |
| Manta Style | 0.1 |
| Tether | 0.12 |
| Thunder Clap | -0.45 |

```text
Total Movement Speed
= (285 + 110 + 30) * (1 + 0.6 + 0.1 + 0.12 - 0.45)
= 582.25
```

The resulting 582.25 is again capped at 550, showing that movement-speed limits are applied only after total movement-speed calculations. [corpus:liquipedia_dota2/movement_speed@2383420#Stacking]

## Set Movement Speed

Set Movement Speed sets total movement speed to a fixed value for the duration, while leaving the unit fully affected by flat and percentage-based changes and bound to minimum and maximum limits. If several listed abilities apply, the lowest value takes priority. [corpus:liquipedia_dota2/movement_speed@2383420#Set_Movement_Speed]

### Sources

| Category | Source | Effect or value |
|---|---|---|
| Set Enemy Move Speed Abilities, priority over Haste | Naga Siren – Deluge | — |
| Set Enemy Move Speed Abilities, priority over Haste | Silver Edge – Shadow Walk | — |
| Set Ally Move Speed Abilities | Arc Warden – Tempest Double | Sets the Self’s movement speed equal to the Zet’s for its duration. |
| Set Ally Move Speed Abilities | Dawnbreaker – Starbreaker | Self Set Move Speed: 215 (0). Sets the caster’s movement speed to a fixed value while active. |
| Set Ally Move Speed Abilities | Elder Titan – Astral Spirit | Sets the Astral Spirit’s base movement speed to the caster’s current movement speed upon cast. The speed does not adapt. |
| Set Ally Move Speed Abilities | Ember Spirit – Fire Remnant | Move Speed to Remnant Speed Factor: 2.5 (5). Fire Remnants move toward their targeted location at a speed set upon cast from the caster’s current movement speed. The speed does not adapt. |
| Set Ally Move Speed Abilities | Io – Tether | Grants the target a movement-speed bonus while the caster copies the target’s movement speed while active. |
| Set Ally Move Speed Abilities | Helm of the Dominator – Dominate | Set Move Speed: 370. Sets the unit’s base movement speed to a fixed value. |
| Set Ally Move Speed Abilities | Helm of the Overlord – Dominate | Set Move Speed: 380. Sets the unit’s base movement speed to a fixed value. |
| Set Ally Move Speed Abilities | Lifestealer – Infest | If the target is a creep, Consume periodically sets its base movement speed equal to the caster’s. |
| Set Ally Move Speed Abilities | Morphling – Morph | Sets the unit’s base movement speed equal to the target’s upon cast. |

[corpus:liquipedia_dota2/movement_speed@2383420#Set_Movement_Speed]

### Hex

Besides disabling its target, hex sets the target’s movement speed to a fixed value for the duration. Flat and percentage-based changes still fully affect the unit, and other movement-speed rules apply. [corpus:liquipedia_dota2/movement_speed@2383420#Hex]

| Hex source |
|---|
| Dazzle – Poison Touch4 |
| Lion – Hex |
| Scythe of Vyse – Hex |
| Shadow Shaman – Hex |

Footnotes listed for these sources are: `1 Requires talent.`, `2a Requires Aghanim's Scepter.`, and `2b Requires Aghanim's Shard.` [corpus:liquipedia_dota2/movement_speed@2383420#Hex]

### Absolute Movement Speed

```text
Total Movement Speed
= Set Move Speed Value
= Absolute Move Speed Value
= Haste Value, when Haste > Min Move Speed; else Min Move Speed Value = Base Move Speed Value
```

These sources set movement speed to an absolute value that no other values can change. If minimum movement speed is higher than the absolute value, the source can set movement speed only to the new minimum. This also applies to all Haste sources unless explicitly stated otherwise. [corpus:liquipedia_dota2/movement_speed@2383420#Absolute_Movement_Speed]

| Category | Source |
|---|---|
| Absolute Move Speed Sources, priority over Haste | Keeper of the Light – Will-O-Wisp |
| Absolute Move Speed Sources, priority over Haste | Lich – Sinister Gaze |
| Absolute Move Speed Sources, priority over Haste | Pangolier – Roll Up |
| Absolute Move Speed Sources, priority over Haste | Pangolier – Rolling Thunder |
| Absolute Move Speed Sources, priority over Haste | Phoenix – Sun Ray |
| Absolute Move Speed Sources, priority over Haste | Tidehunter – Dead in the Water |
| Absolute Move Speed Sources, priority over Haste | Void Spirit – Aether Remnant |
| Absolute Move Speed Sources | Phoenix – Toggle Movement |

[corpus:liquipedia_dota2/movement_speed@2383420#Absolute_Movement_Speed]

## Base Movement Speed

Every unit capable of moving has a fixed base movement-speed value, which only Set Movement Speed sources can alter. [corpus:liquipedia_dota2/movement_speed@2383420#Base_Movement_Speed]

### Heroes

The following values give hero base movement speed and movement speed with the listed Boots of Speed-based bonuses. [corpus:liquipedia_dota2/movement_speed@2383420#Heroes]

| Base | (110) | (90) | (65) | (55) [?] | (50) | (45) [?] | (40) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 275 | 385 | 365 | 340 | 330 | 325 | 320 | 315 |
| 280 | 390 | 370 | 345 | 335 | 330 | 325 | 320 |
| 285 | 395 | 375 | 350 | 340 | 335 | 330 | 325 |
| 290 | 400 | 380 | 355 | 345 | 340 | 335 | 330 |
| 295 | 405 | 385 | 360 | 350 | 345 | 340 | 335 |
| 300 | 410 | 390 | 365 | 355 | 350 | 345 | 340 |
| 305 | 415 | 395 | 370 | 360 | 355 | 350 | 345 |
| 310 | 420 | 400 | 375 | 365 | 360 | 355 | 350 |
| 315 | 425 | 405 | 380 | 370 | 365 | 360 | 355 |
| 320 | 430 | 410 | 385 | 375 | 370 | 365 | 360 |
| 325 | 435 | 415 | 390 | 380 | 375 | 370 | 365 |
| 330 | 440 | 420 | 395 | 385 | 380 | 375 | 370 |

[corpus:liquipedia_dota2/movement_speed@2383420#Heroes]

### Hero Movement Animations

Heroes whose movement animations vary with movement speed are tagged with `MovementSpeedActivityModifiers` in their attributes. Their possible progression is:

```text
Walk < Run < Run Fast/Sprint < Haste
```

The listed Run, Run Fast/Sprint, and Haste table contains the following values in source order:

| Listed value |
|---:|
| 340 |
| 325 |
| 320 |
| 345 |
| - |
| 430 |
| 345 |
| 373 |
| 335 |
| - |
| 385 |
| - |
| 400 |
| 360 |
| 345 |
| 400 |
| 375 |
| 350 |
| 400 |
| 350 |
| 395 |
| 390 |
| 440 |
| 400 |
| 350 |
| 440 |
| 540 |

Not every listed hero has a unique animation for the different movement animations. [corpus:liquipedia_dota2/movement_speed@2383420#Hero_Movement_Animations]

### Creeps

| Unit | Movement Speed |
|---|---:|
| Pollywog, Kobold Soldier, Hill Troll Berserker, Vhoul Assassin, Satyr Mindstealer, Ogre Bruiser, Ogre Frostmage, Hill Troll, Skeleton Warrior, Ancient Rock Golem, Ancient Granite Golem, Ancient Rumblehide, Ancient Thunderhide, Roshan, Ancient Prowler Acolyte | 270 |
| Harpy Scout | 280 |
| Eidolon | 280/310/340/370 |
| Ancient Ice Shaman, Boglet, Marshmage Apprentice, Kobold, Hill Troll Priest, Satyr Tormenter | 290 |
| Minor Imp | 297 |
| Ancient Frostbitten Golem, Croaker, Ancient Croaker, Marshmage, Ancient Marshmage, Satyr Banisher, Wildwing, Dark Troll Summoner, Ancient Black Dragon, Ancient Prowler Shaman | 300 |
| Treant | 300/315/330/345 |
| Warpine Raider, Harpy Stormcrafter, Mud Golem, Shard Golem | 310 |
| Ghost, Centaur Courser, Centaur Conqueror, Hellbear, Hellbear Smasher, Wildwing Ripper, Forged Spirit | 320 |
| Razorback | 320/330/340/350 |
| Zealot | 325 |
| Kobold Foreman | 330 |
| Fell Spirit, Giant Wolf, Alpha Wolf, Ancient Black Drake, Spiderling, Wraith King Skeleton | 350 |
| Undying Zombie | 375 |
| Demonic Warrior | 380 |
| Lycan Wolf | 400/420/440/460 |
| Demonic Archer | 425 |
| Raptor | 460 |

[corpus:liquipedia_dota2/movement_speed@2383420#Creeps]

### Summons

| Summon | Movement Speed |
|---|---:|
| Astral Spirit | 315 |
| Warlock Golem | 320/340/360 |
| Earth | 330/355/380/380 |
| Storm | 350 |
| Familiar | 420 |
| Fire | 550 |

[corpus:liquipedia_dota2/movement_speed@2383420#Summons]

## Movement-Speed Limits

The default lower movement-speed limit is 100 and the upper limit is 550. These limits are identical for all units and cannot be exceeded by flat or percentage-based bonuses or reductions. Base movement-speed changes cannot exceed them either. [corpus:liquipedia_dota2/movement_speed@2383420#Movement_Speed_Limits]

### Minimum Movement Speed

Abilities that change minimum movement speed prevent the unit from moving below the set value. If several apply, the higher minimum takes priority. Slow-resistance sources increase minimum movement speed. [corpus:liquipedia_dota2/movement_speed@2383420#Minimum_Movement_Speed]

| Ability | Values | Condition |
|---|---|---|
| Dawnbreaker – Starbreaker | Set Move Speed: 215 (0); Min Move Speed: 0 (215) | Requires Aghanim’s Shard; otherwise, it sets the caster’s movement speed instead. |

[corpus:liquipedia_dota2/movement_speed@2383420#Minimum_Movement_Speed]

### Maximum Movement Speed

The following abilities can change the maximum movement speed of 550, permitting higher values. If several maximum-changing abilities apply, the higher value takes priority. [corpus:liquipedia_dota2/movement_speed@2383420#Maximum_Movement_Speed]

| Maximum Move Speed Changing Ability |
|---|
| Bloodseeker – Thirst |
| Broodmother – Spin Web1 |
| Force Boots – Speed Unlock |
| Spirit Breaker – Charge of Darkness |

`1 Requires talent.` [corpus:liquipedia_dota2/movement_speed@2383420#Maximum_Movement_Speed]

### Haste

Haste raises a unit’s minimum and maximum movement speed to a specific value. A hasted unit cannot be slowed below that value. [corpus:liquipedia_dota2/movement_speed@2383420#Haste]

| Haste Movement Granting Ability |
|---|
| Centaur Warrunner – Hitch A Ride |
| Centaur Warrunner – Stampede |
| Dark Seer – Surge |
| Faceless Void – Chronosphere |
| Runes – Haste |
| Lycan – Shapeshift |
| Lycan – Wolf Bite |
| Troll Warlord – Battle Trance |
| Phantom Lancer – Phantom Rush |
| Weaver – Shukuchi |

Footnotes listed for these sources are: `1 Requires talent.`, `2a Requires Aghanim's Scepter.`, and `2b Requires Aghanim's Shard.` [corpus:liquipedia_dota2/movement_speed@2383420#Haste]

When a unit is hasted, its Run animation is replaced by its Haste animation. The section identifies a category of “Heroes with Haste Animations.” [corpus:liquipedia_dota2/movement_speed@2383420#Haste_Animations]

## Flat Changes

Flat-change abilities increase or decrease movement speed by a constant value. They cannot exceed the minimum and maximum limits and are applied before percentage-based bonuses and reductions. [corpus:liquipedia_dota2/movement_speed@2383420#Flat_Changes]

### Flat Bonus Sources

| Source |
|---|
| Alchemist – Chemical Rage |
| Alchemist – Berserk Potion |
| Chen – Holy Persuasion3 |
| Drum of Endurance – Swiftness Aura |
| Boots of Bearing – Swiftness Aura |
| Dragon Knight – Elder Dragon Form |
| Juggernaut – Blade Fury2b |
| Mask of Madness – Berserk |
| Spirit Breaker – Charge of Darkness |
| Troll Warlord – Berserker’s Rage |
| Terrorblade – Demon Zeal |
| Undying – Flesh Golem |
| Lone Druid – Spirit Link |
| Gyrocopter – Rocket Barrage5 |

The listed notes are: `1 Requires talent.`, `2a Requires Aghanim's Scepter.`, `2b Requires Aghanim's Shard.`, `3 Grants flat movement speed bonus to Persuaded units only.`, `4a Grants flat movement speed bonus to all player-controlled units by Beastmaster.`, and `5 Requires Afterburner.` [corpus:liquipedia_dota2/movement_speed@2383420#Flat_Changes]

### Flat Reduction Sources

| Source | Value | Effect |
|---|---:|---|
| Tranquil Boots – Break | Move Speed Reduction: 25 | Reduces the wielder’s movement speed by a flat amount after the wielder successfully attacks an enemy hero or an enemy successfully attacks the wielder. |

[corpus:liquipedia_dota2/movement_speed@2383420#Flat_Changes]

### Flat Bonus Item Sources

These items passively grant the wielder a flat movement-speed bonus. Values exclude portions from actives or auras. [corpus:liquipedia_dota2/movement_speed@2383420#Flat_Bonus_Item_Sources]

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Arcane Boots | 45 | 1500 | 33.33 |
| Boots of Bearing | 65 | 4225 | 65 |
| Boots of Speed | 45 | 500 | 11.11 |
| Eul’s Scepter of Divinity | 20 | 2600 | 130 |
| Fleetfooted Enchantment | 115 | N/A | N/A |
| Guardian Greaves | 50 | 4450 | 89 |
| Phase Boots | 50 | 1450 | 29 |
| Quickened Enchantment | 0 | N/A | N/A |
| Solar Crest | 25 | 2575 | 103 |
| Tranquil Boots | 65 | 900 | 13.85 |
| Wind Lace | 15 | 225 | 15 |
| Wind Waker | 30 | 6800 | 226.67 |

[corpus:liquipedia_dota2/movement_speed@2383420#Flat_Bonus_Item_Sources]

### Flat Bonus Talents

The passive, self-affecting Flat Movement Speed ability grants a hero a flat bonus with the following possible values:

```text
10/15/20/25/30/35/40/45/50/60/65/75/90/100
```

It uses a hidden modifier. [corpus:liquipedia_dota2/movement_speed@2383420#Flat_Bonus_Talents]

The talent table is headed by Bonus and the Left/Right choices at levels 10, 15, 20, and 25. Its Movement Speed row lists:

| Listed bonus |
|---:|
| +20 |
| +15 |
| +20 |
| +20 |
| +15 |
| +20 |
| +30 |

[corpus:liquipedia_dota2/movement_speed@2383420#Flat_Bonus_Talents]

## Percentage-Based Changes

Percentage-based changes cannot exceed the minimum and maximum movement-speed limits and are applied after flat bonuses and reductions. Items have stacking restrictions, while percentage-based bonuses from abilities have no stacking restrictions. [corpus:liquipedia_dota2/movement_speed@2383420#Percentage-Based_Changes]

### Percentage Bonuses from Abilities

| Source |
|---|
| Axe – Battle Hunger |
| Axe – Culling Blade |
| Alchemist – Unstable Concoction |
| Batrider – Firefly |
| Beastmaster – Primal Roar |
| Bloodseeker – Thirst |
| Boots of Bearing – Endurance |
| Drum of Endurance – Endurance |
| Bounty Hunter – Track |
| Brewmaster – Drunken Brawler (Storm Stance) |
| Storm – Wind Walk |
| Bristleback – Warpath |
| Broodmother – Spin Web4a |
| Clinkz – Skeleton Walk |
| Clockwerk – Overclocking |
| Clockwerk – Jetpack |
| Demonic Archer (Book of the Dead) – Archer Aura |
| Demonic Archer (Underlord) – Archer Aura |
| Doom – Scorched Earth |
| Drow Ranger – Gust |
| Elder Titan – Astral Spirit |
| Grimstroke – Ink Swell |
| Grimstroke – Dark Portrait |
| Hoodwink – Scurry |
| Invoker – Wex |
| Invoker – Ghost Walk |
| Io – Tether |
| Keeper of the Light – Spirit Form |
| Kobold Foreman – Speed Aura |
| Kunkka – X Marks the Spot1 |
| Kunkka – Ghostship |
| Legion Commander – Overwhelming Odds |
| Leshrac – Nihilism |
| Lifestealer – Rage |
| Lifestealer – Infest |
| Lina – Fiery Soul |
| Lone Druid – Savage Roar |
| Spirit Bear – Savage Roar |
| Marci – Rebound |
| Marci – Unleash |
| Medusa – Stone Gaze |
| Mirana – Leap |
| Mirana – Moonlight Shadow |
| Night Stalker – Hunter in the Night |
| Nyx Assassin – Vendetta |
| Ogre Magi – Bloodlust |
| Phase Boots – Phase |
| Razor – Storm Surge |
| Riki – Cloak and Dagger1 |
| Shadow Blade – Shadow Walk |
| Silver Edge – Shadow Walk |
| Slardar – Guardian Sprint |
| Slark – Depth Shroud |
| Slark – Shadow Dance |
| Smoke of Deceit – Disguise |
| Ninja Gear – Solitary Disguise |
| Solar Crest – Shine |
| Spectre – Spectral Dagger |
| Spectre – Dispersion2b |
| Spectre – Shadow Step |
| Spider Legs – Skitter |
| Spirit Breaker – Bulldoze |
| Sven – Warcry |
| Techies – Reactive Tazer |
| Treant Protector – Nature’s Guise |
| Troll Warlord – Battle Trance |
| Underlord – Fiend’s Gate |
| Undying Zombie – Deathlust |
| Vengeful Spirit – Vengeance Illusion2a |
| Visage – Grave Chill4b |
| Visage – Silent as the Grave |
| Warlock – Shadow Word2b |
| Windranger – Windrun |
| Wraith King – Wraith Delay2a |

The conditions are: `1 Requires talent.`, `2a Requires Aghanim's Scepter.`, `2b Requires Aghanim's Shard.`, `4a Grants movement speed bonus to only to Broodmother, her Spiderlings and Spiderites.`, and `4b Grants movement speed bonus to only to Visage and his Familiars.` [corpus:liquipedia_dota2/movement_speed@2383420#Percentage_Bonuses]

### Percentage-Based Item Sources

The source describes these items as passively granting the wielder a flat movement-speed bonus and labels the table “Flat Bonuses from Items.” Values exclude portions from actives or auras. [corpus:liquipedia_dota2/movement_speed@2383420#Percentage-Based_Item_Sources]

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Manta Style | 10% | 4650 | 465 |
| Nimble Enchantment | 0.08% | N/A | N/A |
| Sange and Yasha | 12% | 4200 | 350 |
| Yasha | 10% | 2100 | 210 |
| Yasha and Kaya | 12% | 4200 | 350 |

[corpus:liquipedia_dota2/movement_speed@2383420#Percentage-Based_Item_Sources]

### Percentage-Based Bonus Talents

The passive, self-affecting Percentage Movement Speed ability grants a percentage-based bonus with these possible values:

```text
5%/6%/8%/10%
```

It uses a hidden modifier. The hero talent table is headed by Bonus and the Left/Right choices at levels 10, 15, 20, and 25, and identifies its row as “Movement Speed Percent.” [corpus:liquipedia_dota2/movement_speed@2383420#Percentage-Based_Bonus_Talents]

### Percentage Reductions from Abilities

| Source |
|---|
| Anti-Mage – Mana Break |
| Abaddon – Mist Coil2b |
| Abaddon – Curse of Avernus |
| Ancient Apparition – Ice Vortex |
| Ancient Apparition – Chilling Touch |
| Ancient Thunderhide – Slam |
| Arc Warden – Flux |
| Arc Warden – Magnetic Field2b |
| Arc Warden – Spark Wraith |
| Axe – Berserker’s Call2a |
| Axe – Battle Hunger |
| Batrider – Sticky Napalm |
| Batrider – Flamebreak1 |
| Beastmaster – Primal Roar |
| Bloodseeker – Blood Mist |
| Razorback – Poison |
| Bounty Hunter – Shadow Walk |
| Brewmaster – Thunder Clap |
| Brewmaster – Cinder Brew |
| Brewmaster – Drunken Brawler (Void Stance)2a |
| Bristleback – Viscous Nasal Goo |
| Bristleback – Hairball |
| Broodmother – Incapacitating Bite |
| Broodmother – Spinner’s Snare |
| Spiderling – Poison Sting |
| Centaur Warrunner – Double Edge2b |
| Centaur Warrunner – Stampede |
| Chen – Penitence |
| Crystal Maiden – Crystal Nova |
| Crystal Maiden – Freezing Field |
| Dark Seer – Wall of Replica |
| Dawnbreaker – Starbreaker |
| Dawnbreaker – Celestial Hammer |
| Dazzle – Poison Touch |
| Death Prophet – Exorcism (Passive Spirits)2a |
| Diffusal Blade – Inhibit |
| Disruptor – Thunder Strike |
| Disruptor – Kinetic Field |
| Dragon Knight – Elder Dragon Form (Frost Breath) |
| Drow Ranger – Frost Arrows |
| Drow Ranger – Multishot |
| Dust of Appearance – Reveal |
| Earth Spirit – Boulder Smash |
| Echo Sabre – Echo Strike |
| Elder Titan – Earth Splitter |
| Enchantress – Enchant |
| Ethereal Blade – Ether Blast |
| Eye of Skadi – Cold Attack |
| Faceless Void – Time Dilation |
| Ghost – Frost Attack |
| Grimstroke – Stroke of Fate |
| Gyrocopter – Call Down |
| Hoodwink – Acorn Shot |
| Hoodwink – Hunter’s Boomerang |
| Hoodwink – Sharpshooter |
| Hellbear Smasher – Thunder Clap |
| Huskar – Inner Fire2b |
| Huskar – Life Break |
| Invoker – Ghost Walk |
| Invoker – Ice Wall |
| Io – Tether |
| Jakiro – Dual Breath |
| Jakiro – Liquid Frost |
| Keeper of the Light – Solar Bind |
| Kunkka – Torrent |
| Kunkka – X Marks the Spot1 |
| Kunkka – Torrent Storm |
| Leshrac – Lightning Storm |
| Leshrac – Nihilism |
| Lich – Frost Blast |
| Lich – Frost Shield |
| Lich – Ice Spire |
| Lich – Chain Frost |
| Lifestealer – Open Wounds |
| Lion – Mana Drain |
| Lycan Wolf – Cripple |
| Lycan Lane Wolf – Cripple |
| Magnus – Shockwave |
| Magnus – Skewer |
| Magnus – Horn Toss |
| Marci – Rebound |
| Marci – Unleash |
| Mars – Spear of Mars2b |
| Mars – God’s Rebuke |
| Mars – Bulwark |
| Mars – Arena of Blood |
| Medusa – Mystic Snake |
| Medusa – Cold Blooded |
| Medusa – Stone Gaze |
| Meepo – Divided We Stand (Fling)2b |
| Mirana – Leap2b |
| Monkey King – Primal Spring |
| Demonic Archer (Book of the Dead) – Purge |
| Necrophos – Ghost Shroud |
| Night Stalker – Void |
| Nullifier – Nullify |
| Ogre Frostmage – Ice Armor |
| Ogre Magi – Ignite |
| Omniknight – Hammer of Purity |
| Orb of Frost – Frost |
| Outworld Destroyer – Astral Imprisonment2b |
| Pangolier – Shield Crash |
| Phantom Assassin – Stifling Dagger |
| Phantom Lancer – Spirit Lance |
| Phoenix – Icarus Dive |
| Primal Beast – Uproar |
| Pudge – Rot |
| Pugna – Decrepify |
| Queen of Pain – Shadow Strike |
| Razor – Plasma Field |
| Razor – Storm Surge2b |
| Roshan – Slam |
| Sand King – Burrowstrike2a |
| Sand King – Sand Storm1 |
| Sand King – Caustic Finale |
| Sand King – Epicenter |
| Shadow Demon – Demonic Purge |
| Shadow Fiend – Requiem of Souls |
| Skywrath Mage – Concussive Shot |
| Satyr Banisher – Purge |
| Shiva’s Guard – Arctic Blast |
| Silencer – Arcane Curse |
| Skywrath Mage – Concussive Shot |
| Slardar – Slithereen Crush |
| Snapfire – Scatterblast |
| Snapfire – Mortimer Kisses |
| Snapfire – Spit Out |
| Sniper – Shrapnel |
| Sniper – Headshot |
| Sniper – Concussive Grenade |
| Solar Crest – Shine |
| Spectre – Spectral Dagger |
| Spectre – Dispersion2b |
| Spectre – Shadow Step |
| Storm Spirit – Overload |
| Techies – Sticky Bomb |
| Templar Assassin – Psionic Trap |
| Templar Assassin – Psionic Projection |
| Psionic Trap – Trap |
| Terrorblade – Reflection |
| Tidehunter – Gush |
| Timbersaw – Flamethrower2b |
| Timbersaw – Chakram |
| Tiny – Tree Throw |
| Tiny – Tree Volley |
| Wildwing – Tornado |
| Treant Protector – Nature’s Grasp |
| Treant Protector – Leech Seed |
| Troll Warlord – Whirling Axes (Ranged) |
| Tusk – Ice Shards2b |
| Tusk – Tag Team |
| Tusk – Walrus Kick |
| Tusk – Walrus PUNCH! |
| Underlord – Pit of Malice2a |
| Underlord – Fiend’s Gate2a |
| Undying Zombie – Deathlust |
| Undying – Decay |
| Undying – Flesh Golem |
| Ursa – Earthshock |
| Venomancer – Noxious Plague |
| Venomancer – Poison Sting |
| Venomancer – Venomous Gale |
| Viper – Poison Attack |
| Viper – Viper Strike |
| Visage – Grave Chill |
| Void Spirit – Astral Step |
| Warlock – Upheaval |
| Warpine Raider – Seed Shot |
| Windranger – Windrun |
| Winter Wyvern – Arctic Burn |
| Winter Wyvern – Splinter Blast |
| Winter Wyvern – Cold Embrace2b |
| Wraith King – Wraithfire Blast |
| Wraith King – Reincarnation |
| Zeus – Heavenly Jump |

The conditions are: `1 Requires talent.`, `2a Requires Aghanim's Scepter.`, and `2b Requires Aghanim's Shard.` [corpus:liquipedia_dota2/movement_speed@2383420#Percentage_Reductions]

## Abilities Based on Movement Speed

| Ability | Value | Effect |
|---|---|---|
| Spirit Breaker – Greater Bash | Move Speed as Damage: 25%/30%/35%/40% (45%/50%/55%/60%) | Deals damage based on the hero’s movement speed. |

[corpus:liquipedia_dota2/movement_speed@2383420#Abilities_Based_on_Movement_Speed]

## Move Commands

Several different orders can make a unit move. The default move command is bound to Right Click or M and can also be assigned to a Hotkey. Ground-targeting it orders the unit to move to that point or until it cannot get closer, such as when the target is out of reach. The unit does not automatically attack enemies encountered during the move. [corpus:liquipedia_dota2/movement_speed@2383420#Move_Commands]

The follow command is merged with the default M move command and uses the same keys. Targeting a unit with the move command follows it. Targeting an allied unit causes the ordered unit to follow until a new order is given or the target dies. Most units have a follow range of 100 and attempt to remain within 100 range of their target. Juggernaut’s Healing Ward instead has Follow Range: 250. Following an enemy requires the follow Hotkey because Right Click on an enemy automatically issues an attack order. [corpus:liquipedia_dota2/movement_speed@2383420#Move_Commands]

### Patrol

Patrol orders a unit to move back and forth between its starting location and the targeted point until another order is given. Multiple patrol points may be assigned; the unit visits them in the order given and, after the last point, traverses them in reverse order. Like the move command, the unit automatically attacks enemies it crosses while patrolling. The default Patrol Command hotkey is `<blank>`. [corpus:liquipedia_dota2/movement_speed@2383420#Patrol]

### Attack-Move

The section associates Attack-Move with “Movement speed advantage required for a given attack efficiency when chasing.” The default Attack-Move command is bound to A and can also be assigned to a Hotkey. [corpus:liquipedia_dota2/movement_speed@2383420#Attack-Move_Command]

Attack-Move is identical to the move command except that the ordered unit attacks enemies it crosses. An attack order issued on the ground performs it and requires the attack Hotkey. If no enemies are crossed, it acts as a move order. When an enemy enters acquisition range, the unit approaches and attacks it. If the target becomes unattackable through death, becoming ethereal or invulnerable, turning invisible, or loss of sight, the unit resumes moving from its current location toward the ordered point. It does not return to where it originally left the path. [corpus:liquipedia_dota2/movement_speed@2383420#Attack-Move_Command]

## Recent Changes

| Version | Date | Description |
|---|---|---|
| 7.38 | 2025-02-19 | Units no longer gain bonus movement speed during nighttime. |
| 7.33b | 2023-04-25 | Nighttime bonus movement speed is now disabled when a hero damages an enemy controlled unit. |
| 7.33 | 2023-04-20 | All units now gain 15 movement speed during nighttime. The effect is doubled for heroes but can be broken for 5 seconds upon attacking or taking damage from player-controlled sources. |

[corpus:liquipedia_dota2/movement_speed@2383420#Recent_Changes]