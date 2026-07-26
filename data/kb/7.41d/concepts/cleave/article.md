---
title: Cleave
kind: concept
patch: 7.41d
card:
  entity: cleave
  sentences:
  - text: Cleave causes a melee unit’s attack to deal a portion of its total pre-reduction
      attack damage as physical area damage in a trapezoid in front of the attacker.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874
    - corpus:liquipedia_dota2/cleave@2380874#Mechanics
    - corpus:liquipedia_dota2/cleave@2380874#Damage
  - text: Only melee units can cleave by default; ranged units cannot.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Mechanics
  - text: An attack is classified as melee when it does not rely on projectiles.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Ability_Draft
  - text: Cleave does not affect the primary target and cannot miss secondary targets,
      but a missed primary attack produces no cleave.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Mechanics
  - text: It hits invisible units but not hidden or invulnerable units, wards, or
      buildings.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Mechanics
  - text: Cleave pierces spell immunity and is fully affected by damage manipulation.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Damage
  - text: It counts as spell damage but has the no-spell-amplification flag.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Damage
  - text: Its isosceles-trapezoid area has the attacker centered on the shorter side,
      whose length is double the starting radius; its height is the cleave distance,
      and its longer side is double the ending radius.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Area_of_Effect
  - text: Multiple cleave sources apply independently, each using its full damage
      and its own area parameters.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Stacking
  - text: Attack modifiers that increase total attack damage, such as Critical Strike,
      increase cleave damage.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Attack_Modifier_Interactions
  - text: Most instant attacks trigger cleave when melee, but Tidebringer cannot be
      triggered by an instant attack and spell-damage-based attacks do not interact
      with cleave.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Instant_Attack
  - text: The passive Cleave ability has First Width 150, Distance 650, End Width
      360, and Cleave Damage that Varies.
    marks:
    - corpus:liquipedia_dota2/cleave@2380874#Talents
---

# Cleave

Cleave causes a melee unit’s attacks to deal a portion of its damage in an area in front of it. [corpus:liquipedia_dota2/cleave@2380874]

## Mechanics

Cleave deals damage in a trapezoid in front of the attacker, based on the unit’s total attack damage values. Only melee units can cleave by default; ranged units cannot. Cleave does not affect the primary target and cannot miss secondary targets, but a missed primary attack does not cleave. It hits invisible units, but not hidden or invulnerable units, wards, or buildings. [corpus:liquipedia_dota2/cleave@2380874#Mechanics]

### Stacking

Multiple cleave sources on one unit work fully independently. Each applies its full damage within its own area without interacting with other cleave sources. For example, Sven with level 4 Great Cleave, a level 4 Empower buff, and Battle Fury deals 3 separate cleave-damage instances per attack, each using its own starting radius, distance, and end radius. [corpus:liquipedia_dota2/cleave@2380874#Stacking]

### Ability Draft

Ranged heroes ordinarily cannot cleave: the cleave component of an ability is either disabled for them, or the ability is unobtainable. An attack is classified as melee when it does not rely on projectiles. [corpus:liquipedia_dota2/cleave@2380874#Ability_Draft]

If a game mode lets ranged heroes obtain normally unobtainable cleave abilities, including Tidebringer and Great Cleave, those cleave sources work fully. As with melee heroes, the area is based on the attacker’s position and occurs on attack hit, so damage is always applied in front of the attacking hero even when the target is much farther away. [corpus:liquipedia_dota2/cleave@2380874#Ability_Draft]

### Damage

Cleave deals physical damage based entirely on the unit’s total attack damage before reductions. It pierces spell immunity and is fully affected by damage manipulation. Although considered spell damage, it has the no-spell-amplification flag, preventing spell damage amplification from increasing it. [corpus:liquipedia_dota2/cleave@2380874#Damage]

### Area of Effect

A cleave area is an isosceles trapezoid in front of the attacker, with the attacker at the center of its shorter side. Double the starting radius is the shorter side’s length, cleave distance is the trapezoid’s height, and double the ending radius is the length of the longer parallel side. [corpus:liquipedia_dota2/cleave@2380874#Area_of_Effect]

### Attack Modifier Interactions

Cleave is an attack modifier, but works independently and does not interfere with other attack modifiers. Corruption’s armor reduction on the primary target does not increase cleave damage even though that target receives extra damage. An attack modifier that increases total attack damage, such as Critical Strike, does increase cleave damage. [corpus:liquipedia_dota2/cleave@2380874#Attack_Modifier_Interactions]

Conditional attack-damage bonuses may or may not be included. Cleave takes the following into account:

| Source | Ability or effect | Annotation |
|---|---|---:|
| Anti-Mage | Mana Break | |
| Battle Fury | Quell | 4 |
| Diffusal Blade | Manabreak | |
| Kunkka | Tidebringer | |
| Lifestealer | Feast | |
| Quelling Blade | Quell | |
| Riki | Cloak and Dagger | |
| Shadow Blade | Shadow Walk | |
| Silver Edge | Shadow Walk | |
| Slardar | Bash of the Deep | |
| Storm | Wind Walk | |
| Ursa | Fury Swipes | |

| Annotation | Meaning |
|---|---|
| 4 | Tidebringer is not affected by Quell. |

[corpus:liquipedia_dota2/cleave@2380874#Attack_Modifier_Interactions]

## Instant Attacks

Most instant attacks can trigger cleave when the hero’s attack is melee. Tidebringer cannot be triggered by an instant attack, and spell-damage-based attacks do not interact with cleave. Battle Fury is disabled for the following attacks:

| Hero | Instant attack | Condition | Battle Fury |
|---|---|---|---|
| Dawnbreaker | Starbreaker | | Disabled |
| Kez | Echo Slash | | Disabled |
| Lifestealer | Infest | Excluding first attack; 2a | Disabled |
| Mars | God’s Rebuke | | Disabled |
| Monkey King | Boundless Strike | | Disabled |
| Sand King | Stinger | | Disabled |
| Sand King | Epicenter | 2a | Disabled |
| Tidehunter | Anchor Smash | | Disabled |
| Void Spirit | Astral Step | | Disabled |

| Annotation | Requirement |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |

[corpus:liquipedia_dota2/cleave@2380874#Instant_Attack]

## Cleave Sources

None of these abilities cleave while attacking an ally:

| Source | Ability | Annotation |
|---|---|---:|
| Earthshaker | Enchant Totem | 2a |
| Kunkka | Tidebringer | 4 |
| Lion | Finger of Death | 3 |
| Magnus | Empower | |
| Sven | Great Cleave | |
| Underlord | Atrophy Aura | 3 |
| Battle Fury | Cleave | |

| Annotation | Requirement or interaction |
|---|---|
| 1 | Requires talent. |
| 2a | Requires Aghanim’s Scepter. |
| 4 | Tidebringer is not affected by Quell. |

[corpus:liquipedia_dota2/cleave@2380874#Cleave_Sources]

### Talents

The passive Cleave ability affects enemy units and deals spell/physical damage. It grants melee attacks cleave properties, dealing damage within a distance in front of the attacker whenever they attack. [corpus:liquipedia_dota2/cleave@2380874#Talents]

| Parameter | Value |
|---|---:|
| First Width | 150 |
| Distance | 650 |
| End Width | 360 |
| Cleave Damage | Varies |

[corpus:liquipedia_dota2/cleave@2380874#Talents]

It deals physical spell damage corresponding to the hero’s attack-damage value:

`CleaveDmg = ΣAtkDmg × f(Cleave)`

Damage block sources affect each enemy within the area individually. The damage has the no-spell-lifesteal and no-spell-amplification flags. It stacks independently with other cleave sources. [corpus:liquipedia_dota2/cleave@2380874#Talents]

The total area is an isosceles trapezoid in front of the hero. Damage is applied immediately to every valid enemy in the area regardless of the ability’s visual effects. Attacking an ally does not proc cleave; cleave does not damage couriers; and it neither procs nor deals damage against buildings or ward-type units. [corpus:liquipedia_dota2/cleave@2380874#Talents]

Different cleave values use different ability IDs:

| Ability ID | Cleave |
|---:|---:|
| 6845 | 15% |
| 6603 | 20% |
| 6801 | 25% |
| 7122 | 30% |
| 7899 | 35% |
| 7200 | 40% |
| 6631 | 60% |
| 6827 | 100% |
| 7201 | 130% |
| 455 | 140% |
| 7124 | 150% |
| 7670 | 175% |

[corpus:liquipedia_dota2/cleave@2380874#Talents]

The talent listing uses Level 10, Level 15, Level 20, and Level 25 columns, each divided into Left and Right, and supplies this entry:

| Bonus | Value |
|---|---:|
| Cleave | +100% |

[corpus:liquipedia_dota2/cleave@2380874#Talents]

## Splash

Splash is comparable to a ranged version of cleave. Its damage is typically dealt in a circle around the attacked unit rather than in a trapezoid in front of the attacker. It does not affect the primary target and cannot miss secondary targets, but a missed attack applies no splash damage within the radius. Splash interacts with attack modifiers in the same way as cleave. [corpus:liquipedia_dota2/cleave@2380874#Splash]

Splash also works for melee heroes. Doom can acquire Splash Attack from Ancient Black Dragon through Devour. [corpus:liquipedia_dota2/cleave@2380874#Splash]

### Splash Sources

| Source | Ability | Annotation |
|---|---|---:|
| Ancient Black Dragon | Splash Attack | |
| Dragon Knight | Elder Dragon Form | |
| Fountain | Fountain Damage | |
| Tiny | Tree Throw | |
| Tiny | Tree Volley | |
| Treant Protector | Overgrowth | 2a |

[corpus:liquipedia_dota2/cleave@2380874#Splash_Sources]

## Other Sources

Besides Cleave and Splash, some unique attack-based area-damage abilities share similarities with cleave, splash, or one another. [corpus:liquipedia_dota2/cleave@2380874#Other_Sources]

### Tree Grab

| Parameter | Value |
|---|---:|
| Area Damage Length | 200 |
| Area Damage Radius | 5/6/7/8 |

Tree Grab’s damage is based on Tiny’s total attack damage. It considers armor value and defense classes and deals physical damage. Unlike cleave’s isosceles trapezoid, Tree Grab uses a semicircle on top of a rectangle. Its area is locked in front of Tiny regardless of how far away the attack target is. [corpus:liquipedia_dota2/cleave@2380874#Tree_Grab]

### Psi Blades

| Parameter | Value |
|---|---|
| Spill Area Width | 400/500/600/700 |
| Spill Length Multiplier | 0.7/0.8/0.9/1 |

Psi Blades causes Templar Assassin’s attack to damage enemies behind the attacked target. Spill damage is based on exactly how much damage the primary target took and is dealt as pure damage to units behind it. It counts as spell damage, but ignores outgoing spell damage amplification and cannot spell lifesteal. [corpus:liquipedia_dota2/cleave@2380874#Psi_Blades]

The spill area is rectangular, with a width of `400/500/600/700` and a length of `0.7/0.8/0.9/1 × ΣAtkRange`. Other attack-range bonuses can increase it further. Templar Assassin’s position is checked when the projectile hits the target, not when it is launched. [corpus:liquipedia_dota2/cleave@2380874#Psi_Blades]

## Version History

| Version | Date | Changes |
|---|---|---|
| 7.20 | 2018-11-19 | Cleave damage became affected by armor value as well, rather than only armor type. |
| 7.00 | 2016-12-12 | Cleave changed from a circular area to a trapezoid-shaped area.<br><br>Battle Fury changed from 280 radius to 150 starting radius, 520 distance, and 280 end radius.<br><br>Empower changed from 240 radius to 150 starting radius, 460 distance, and 240 end radius.<br><br>Great Cleave changed from 300 radius to 150 starting radius, 550 distance, and 300 end radius.<br><br>Grow changed from 400 radius to 150 starting radius, 600 distance, and 400 end radius.<br><br>Tidebringer changed from 450/500/550/600 radius to 150 starting radius, 675/750/825/900 distance, and 450/500/550/600 end radius.<br><br>Cleave damage ceased to be affected by spell damage amplification and could no longer spell lifesteal. |

[corpus:liquipedia_dota2/cleave@2380874#Version_History]

## Patch History

| Date | Change |
|---|---|
| 05 Nov 2014 | Improved network performance with various multi-target attacks, including cleave. |
| 07 Feb 2013 | Fixed cleave hitting Familiars. |
| 27 Jan 2011 | Fixed cleave damage working while attacking towers. |

[corpus:liquipedia_dota2/cleave@2380874#Patch_History]