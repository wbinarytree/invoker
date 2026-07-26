---
title: Spell Damage
kind: concept
patch: 7.41d
card:
  entity: spell_damage
  sentences:
  - text: 'Spell damage is damage dealt by all abilities—including item abilities
      and attack modifiers—usually in an instance separate from attack damage, and
      it has three damage types: magical, physical, and pure.'
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019
  - text: Magical spell damage is influenced by magic resistance.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019
  - text: Physical spell damage is influenced by armor.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019
  - text: Pure spell damage is affected by neither magic resistance nor armor.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019
  - text: The spell-damage multiplier is (1 + Outgoing Manip) X (1 + Incoming Manip),
      with modifiers adding within each category before the category totals multiply.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019#Stacking
  - text: Unless stated otherwise, a summon’s spell damage ignores its hero’s outgoing
      manipulation but can be affected by incoming manipulation on the target.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019#Stacking
  - text: Multiple incoming spell-damage amplification sources stack additively and
      affect every spell-damage source except HP Removal.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019#Incoming_Spell_Damage_Amplification
  - text: Multiple outgoing spell-damage manipulation sources stack additively and
      can increase or decrease any spell damage the unit applies.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation
  - text: Equipped owner-only item bonuses are Kaya 10%, Kaya and Sange 12%, Meteor
      Hammer 10%, Timeless Enchantment 0.42%, and Yasha and Kaya 12%.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019#Item_Sources
  - text: Multiple spell-damage amplification sources from Kaya-based items do not
      stack.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019#Item_Sources
  - text: Abilities with Instant Kill, HP Removal, Delayed Damage, or similar health-manipulation
      mechanics generally ignore both incoming and outgoing spell-damage amplification.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019#Exceptions
  - text: Abilities carrying the No-Spell-Amplification flag usually cannot spell
      lifesteal.
    marks:
    - corpus:liquipedia_dota2/spell_damage@2401019#Exceptions
---

# Spell Damage

Spell damage is usually dealt in a separate instance from attack damage, with some exceptions. It includes damage from all abilities—including item abilities and attack modifiers—that deal magical, physical, or pure damage. All three damage types underlie damage manipulation. [corpus:liquipedia_dota2/spell_damage@2401019]

| Spell-damage type | Defensive interaction |
|---|---|
| Magical | Influenced by magic resistance. [corpus:liquipedia_dota2/spell_damage@2401019] |
| Physical | Influenced by armor. [corpus:liquipedia_dota2/spell_damage@2401019] |
| Pure | Affected by neither magic resistance nor armor. [corpus:liquipedia_dota2/spell_damage@2401019] |

## Spell Damage Manipulation

### Stacking

All sources of spell damage manipulation stack additively within the outgoing and incoming categories, after which the two categories are multiplied together. Outgoing spell damage manipulation and incoming spell damage manipulation stack additively with generic incoming damage manipulation and generic outgoing damage manipulation, respectively, because spell damage manipulation is part of damage manipulation. The same category stacks additively, while different categories stack multiplicatively. [corpus:liquipedia_dota2/spell_damage@2401019#Stacking]

```text
Spell Damage Multiplier = (1 + Outgoing Manip) X (1 + Incoming Manip)
```

[corpus:liquipedia_dota2/spell_damage@2401019#Stacking]

Unless otherwise stated, spell damage dealt by summons is not affected by the hero’s outgoing spell damage manipulation. Summons can be affected by incoming spell damage manipulation because it affects the damage target rather than the caster. [corpus:liquipedia_dota2/spell_damage@2401019#Stacking]

#### Example 1: Outgoing Manipulation

Bloodseeker has a level 4 Bloodrage buff and Kaya and Sange. [corpus:liquipedia_dota2/spell_damage@2401019#Example_1:_Outgoing_Manipulation]

| Source | Spell-damage amplification |
|---|---:|
| Level 4 Bloodrage | 0.3 [corpus:liquipedia_dota2/spell_damage@2401019#Example_1:_Outgoing_Manipulation] |
| Kaya and Sange | 0.12 [corpus:liquipedia_dota2/spell_damage@2401019#Example_1:_Outgoing_Manipulation] |

```text
Spell Damage Multiplier = (1 + 0.3 + 0.12) X (1 + 0) = 1.42
```

Bloodseeker’s spell damage multiplier is 1.42. [corpus:liquipedia_dota2/spell_damage@2401019#Example_1:_Outgoing_Manipulation]

#### Example 2: Incoming and Outgoing Manipulation

Bloodseeker has Dagon 5 and is affected by Mage Slayer, while Marci is affected by Spell Weakness. [corpus:liquipedia_dota2/spell_damage@2401019#Example_2:_Incoming_and_Outgoing_Manipulation]

| Input | Source | Value |
|---|---|---:|
| Dagon 5 spell damage | Energy Burst | 800 [corpus:liquipedia_dota2/spell_damage@2401019#Example_2:_Incoming_and_Outgoing_Manipulation] |
| Incoming spell damage manipulation | Spell Weakness | 0.16 [corpus:liquipedia_dota2/spell_damage@2401019#Example_2:_Incoming_and_Outgoing_Manipulation] |
| Outgoing spell damage manipulation | Bloodrage | 0.3 [corpus:liquipedia_dota2/spell_damage@2401019#Example_2:_Incoming_and_Outgoing_Manipulation] |
| Outgoing spell damage manipulation | Kaya and Sange | 0.12 [corpus:liquipedia_dota2/spell_damage@2401019#Example_2:_Incoming_and_Outgoing_Manipulation] |
| Outgoing spell damage manipulation | Mage Slayer | -0.4 [corpus:liquipedia_dota2/spell_damage@2401019#Example_2:_Incoming_and_Outgoing_Manipulation] |

```text
Spell Damage Multiplier =
(1 + 0.3 + 0.12 - 0.4) Outgoing Manip X
(1 + 0.16) Incoming Manip

Spell Damage Multiplier =
1.02 Outgoing Manip X 1.16 Incoming Manip

Spell Damage Multiplier = 1.1832
Total Spell Damage = 800 * 1.1832 = 946.56
```

Energy Burst deals Marci 946.56 spell damage before magic resistance reductions. [corpus:liquipedia_dota2/spell_damage@2401019#Example_2:_Incoming_and_Outgoing_Manipulation]

#### Example 3: Generic Damage Manipulation

Bloodseeker instead casts Dagon 5 on a Spectre with level 4 Dispersion, with all other modifiers unchanged. Dispersion is generic damage manipulation and affects all damage dealt to Spectre; despite this, it stacks additively with incoming spell damage manipulation such as Spell Weakness when spell damage is calculated. [corpus:liquipedia_dota2/spell_damage@2401019#Example_3:_Generic_Damage_Manipulation]

| Input | Source | Value |
|---|---|---:|
| Dagon 5 spell damage | Energy Burst | 800 [corpus:liquipedia_dota2/spell_damage@2401019#Example_3:_Generic_Damage_Manipulation] |
| Incoming spell damage manipulation | Spell Weakness | 0.16 [corpus:liquipedia_dota2/spell_damage@2401019#Example_3:_Generic_Damage_Manipulation] |
| Incoming generic damage manipulation | Dispersion | -0.18 [corpus:liquipedia_dota2/spell_damage@2401019#Example_3:_Generic_Damage_Manipulation] |
| Outgoing spell damage manipulation | Bloodrage | 0.3 [corpus:liquipedia_dota2/spell_damage@2401019#Example_3:_Generic_Damage_Manipulation] |
| Outgoing spell damage manipulation | Kaya and Sange | 0.12 [corpus:liquipedia_dota2/spell_damage@2401019#Example_3:_Generic_Damage_Manipulation] |
| Outgoing spell damage manipulation | Mage Slayer | -0.4 [corpus:liquipedia_dota2/spell_damage@2401019#Example_3:_Generic_Damage_Manipulation] |

```text
Sp_Mu =
(1 + (0.3 + 0.12 - 0.4)) Outgoing X
(1 + 0.16 - 0.18) Incoming

= 1.02 Outgoing X 0.98 Incoming
= 0.9996

Total Spell Damage = 800 * 0.9996 = 799.68
```

Spectre takes 799.68 spell damage before magic resistance. [corpus:liquipedia_dota2/spell_damage@2401019#Example_3:_Generic_Damage_Manipulation]

### Incoming Spell Damage Amplification

A unit with an incoming spell damage amplification debuff takes more spell damage. Multiple sources stack additively, and the amplification affects every source of spell damage except damage flagged as HP Removal. [corpus:liquipedia_dota2/spell_damage@2401019#Incoming_Spell_Damage_Amplification]

#### Sources

| Source | Ability |
|---|---|
| Ancient Black Drake | Magic Amplification Aura [corpus:liquipedia_dota2/spell_damage@2401019#Abilities] |
| Beastmaster | Wild Axes [corpus:liquipedia_dota2/spell_damage@2401019#Abilities] |
| Bloodstone | Spell Weakness Aura [corpus:liquipedia_dota2/spell_damage@2401019#Abilities] |
| Grimstroke | Soulbind¹ [corpus:liquipedia_dota2/spell_damage@2401019#Abilities] |
| Hoodwink | Hunter’s Boomerang [corpus:liquipedia_dota2/spell_damage@2401019#Abilities] |
| Veil of Discord | Spell Weakness [corpus:liquipedia_dota2/spell_damage@2401019#Abilities] |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/spell_damage@2401019#Abilities] |
| 2a | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/spell_damage@2401019#Abilities] |
| 2b | Requires Aghanim’s Shard. [corpus:liquipedia_dota2/spell_damage@2401019#Abilities] |

### Outgoing Spell Damage Manipulation

A unit with outgoing spell damage manipulation deals more or less spell damage with any spell damage it applies to any unit. Multiple sources stack additively. [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation]

| Effect | Source | Ability |
|---|---|---|
| Amplification | Bloodseeker | Bloodrage [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |
| Amplification | Io | Overcharge [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |
| Amplification | Lina | Flame Cloak²ᵃ [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |
| Amplification | Pugna | Oblivion Savant [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |
| Amplification | Rubick | Arcane Supremacy [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |
| Amplification | Rubick | Spell Steal¹ [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |
| Reduction | Mage Slayer | Mage Slayer [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |
| 2a | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |
| 2b | Requires Aghanim’s Shard. [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |
| 3 | Requires selecting the corresponding facet. [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation] |

Heroes can have talents granting outgoing spell damage amplification. The talent listing is labeled Spell Amplification and is organized by Bonus and by Left/Right choices at Level 10, Level 15, Level 20, and Level 25. [corpus:liquipedia_dota2/spell_damage@2401019#Outgoing_Spell_Damage_Manipulation]

#### Item Sources

These items grant their owners a direct spell damage amplification bonus. The effect is limited to the item’s owner, who must have the item equipped. [corpus:liquipedia_dota2/spell_damage@2401019#Item_Sources]

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Kaya | 10% | 2100 | 210 [corpus:liquipedia_dota2/spell_damage@2401019#Item_Sources] |
| Kaya and Sange | 12% | 4200 | 350 [corpus:liquipedia_dota2/spell_damage@2401019#Item_Sources] |
| Meteor Hammer | 10% | 2850 | 285 [corpus:liquipedia_dota2/spell_damage@2401019#Item_Sources] |
| Timeless Enchantment | 0.42% | N/A | N/A [corpus:liquipedia_dota2/spell_damage@2401019#Item_Sources] |
| Yasha and Kaya | 12% | 4200 | 350 [corpus:liquipedia_dota2/spell_damage@2401019#Item_Sources] |

The values exclude portions from actives or auras. For Kaya-based items, multiple sources of spell damage amplification do not stack. [corpus:liquipedia_dota2/spell_damage@2401019#Item_Sources]

## Exceptions

Certain abilities ignore both types of spell damage amplification and usually cannot spell lifesteal. In general, abilities with health-manipulation mechanics—Instant Kill, HP Removal, Delayed Damage, etc.—are not affected by either type of spell damage amplification. These cases are associated with the No-Spell-Amplification flag. [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions]

The following abilities are not affected by outgoing spell damage amplification but are affected by Hunter’s Boomerang’s incoming spell damage amplification, subject to the listed qualifications. [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions]

| Source | Ability |
|---|---|
| Battle Fury | Cleave [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Blade Mail | Damage Return [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Chipped Vest | Chipper [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Kunkka | Tidebringer [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Luna | Moon Glaives [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Magnus | Empower [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Nyx Assassin | Spiked Carapace [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Silencer | Glaives of Wisdom¹ [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Storm Spirit | Overload² [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Sven | Great Cleave [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Templar Assassin | Psi Blades [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Tiny | Tree Grab [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Tiny | Tree Throw [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| Witch Doctor | Death Ward³ [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |

| Marker | Qualification |
|---|---|
| 1 | The damage of the bouncing attacks is unaffected by outgoing spell damage amplification. The `-based` damage is fully affected, including that of the bounces. [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| 2 | The damage of the bouncing attacks is unaffected by outgoing spell damage amplification. Overload’s area damage is fully affected, including that of the bounces. [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |
| 3 | The damage of the bouncing attacks counts as spell damage but is unaffected by outgoing spell damage amplification. [corpus:liquipedia_dota2/spell_damage@2401019#Exceptions] |

### Talents

Spell Damage Amplification is a passive ability affecting self. Its Spell Damage Amp varies, it increases the hero’s outgoing spell damage amplification, and it has a hidden modifier. [corpus:liquipedia_dota2/spell_damage@2401019#Talents]

| Existing Spell Damage Amp value |
|---:|
| 3% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 4% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 5% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 6% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 7% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 8% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 9% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 10% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 11% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 12% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 14% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 15% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 16% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 18% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 19% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 20% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |
| 25% [corpus:liquipedia_dota2/spell_damage@2401019#Talents] |

## Version History

| Version | Date | Description |
|---|---|---|
| 7.30e | 2021-10-28 | Magic Weakness no longer amplifies spell damage that is not affected by outgoing spell damage amplification. [corpus:liquipedia_dota2/spell_damage@2401019#Version_History] |
| 7.06c | 2017-05-29 | Damage return from Blade Mail is no longer increased by outgoing spell amplification. [corpus:liquipedia_dota2/spell_damage@2401019#Version_History] |
| 7.00 | 2016-12-12 | Moon Glaives no longer gets boosted by outgoing spell amplification.<br>Cleave no longer gets boosted by outgoing spell amplification.<br>Spell lifesteal does not trigger heal for things that do not receive spell amplification (Moon Glaives, Cleave). [corpus:liquipedia_dota2/spell_damage@2401019#Version_History] |

## Patch History

| Patch | Description |
|---|---|
| 08 Aug 2019 | Alt now show their modified/increased spell ampification values at tooltips. [corpus:liquipedia_dota2/spell_damage@2401019#Patch_History] |