---
title: Damage Manipulation
kind: concept
patch: 7.41d
card:
  entity: damage_manipulation
  sentences:
  - text: Damage manipulation is a percentage-based system that increases or reduces
      damage dealt by a dealing unit or taken by a receiving unit, applies to negative
      damage, and can reverse the sign of damage when the manipulation percentage
      exceeds 100%.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Overview
  - text: The `MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE` property provides additive
      percentage manipulation of spell damage.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Spell_Damage_Amplification
  - text: Kaya-based amplification uses `MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE_UNIQUE`;
      such items do not stack, and only the highest value applies.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Unique_Spell_Amplification
  - text: '`MODIFIER_PROPERTY_TOTALDAMAGEOUTGOING_PERCENTAGE` generally manipulates
      outgoing damage of every type by percentage.'
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Outgoing_Universal_Damage_Manipulation
  - text: Damage negation makes an entire damage instance deal no damage while leaving
      it registered, allowing effects without a minimum-damage threshold to react.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Damage_Negation
  - text: Physical damage negation uses `MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_PHYSICAL`,
      and every Ethereal source provides it.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Physical_Damage_Negation
  - text: Pure damage negation uses `MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_PURE`; Debuff
      Immunity provides it except against pure damage that pierces Debuff Immunity.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Pure_Damage_Negation
  - text: Universal damage negation uses `MODIFIER_PROPERTY_AVOID_DAMAGE` and affects
      all damage types.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Universal_Damage_Negation
  - text: Generic incoming manipulation uses `MODIFIER_PROPERTY_INCOMING_DAMAGE_PERCENTAGE`
      and stacks additively, so amplification can offset a 100% reduction.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Generic_Incoming_Damage_Manipulation
  - text: False Promise alone provides `MODIFIER_PROPERTY_AVOID_DAMAGE_AFTER_REDUCTIONS`,
      a constant 100% reduction that includes damage carrying the HP Removal flag.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Unique_Damage_Negation
  - text: Armor uses b = 1 and f = 0.06 in the multiplier formula 1 − (f × R)/(b +
      f × |R|), whose limits are 0 and 2 for infinitely positive and negative armor.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Armor
  - text: Generic incoming effects add together, generic outgoing effects add together,
      unique effects multiply together, and the completed groups multiply with one
      another.
    marks:
    - corpus:liquipedia_dota2/damage_manipulation@2351852#Stacking
---

# Damage Manipulation

Damage manipulation alters damage values by increasing or reducing them. [corpus:liquipedia_dota2/damage_manipulation@2351852]

## Overview

Unlike damage block, damage manipulation:

- Operates on both the dealing unit as outgoing damage manipulation and the receiving unit as incoming damage manipulation.
- Can amplify or reduce damage.
- Always changes damage by a percentage.
- Can manipulate negative damage.
- Can turn positive damage negative and negative damage positive when the manipulation percentage exceeds 100%.
- Stacks additively within the same type and multiplicatively by priority between different types.

Damage negation is a special form of damage manipulation and generally cannot be treated as 100% damage reduction. The damage manipulations below are ordered by priority. Outgoing attack damage manipulation, including illusion outgoing attack damage manipulation, is excluded and belongs to attack damage. [corpus:liquipedia_dota2/damage_manipulation@2351852#Overview]

## Outgoing Damage Manipulation

Outgoing damage manipulation causes an afflicted unit to deal increased or reduced damage. [corpus:liquipedia_dota2/damage_manipulation@2351852#Outgoing_Damage_Manipulation]

### Spell Damage Amplification

Spell damage amplification is driven by `MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE`. It affects spell damage by percentage, stacks additively, and includes some damage carrying the HP Removal flag. It does not affect damage that is Unaffected by Amplification. [corpus:liquipedia_dota2/damage_manipulation@2351852#Spell_Damage_Amplification]

#### Sources

| Effect | Source |
|---|---|
| Amplification | Anti-Mage — Counterspell³ |
| Amplification | Bloodseeker — Bloodrage |
| Amplification | Oracle — False Promise²ᵃ |
| Amplification | Io — Overcharge³ |
| Amplification | Lina — Flame Cloak²ᵃ |
| Amplification | Muerta — Pierce the Veil²ᵇ |
| Amplification | Rubick — Arcane Supremacy |
| Amplification | Rubick — Spell Steal¹ |
| Reduction | Mage Slayer — Mage Slayer [corpus:liquipedia_dota2/damage_manipulation@2351852#Spell_Damage_Amplification] |

¹ Requires talent. ²ᵃ Requires Aghanim's Scepter. ²ᵇ Requires Aghanim's Shard. ³ Requires selecting the corresponding facet. [corpus:liquipedia_dota2/damage_manipulation@2351852#Spell_Damage_Amplification]

#### Talent listing

| Bonus | Level 10 Left | Level 10 Right | Level 15 Left | Level 15 Right | Level 20 Left | Level 20 Right | Level 25 Left | Level 25 Right |
|---|---|---|---|---|---|---|---|---|
| Spell Amplification |  |  |  |  |  |  |  |  [corpus:liquipedia_dota2/damage_manipulation@2351852#Spell_Damage_Amplification] |

Many items grant direct spell-damage-amplification bonuses to their owners. The owner must have the item equipped, and the effect is limited to that owner.

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Kaya | 10% | 2100 | 210 |
| Kaya and Sange | 12% | 4200 | 350 |
| Meteor Hammer | 10% | 2850 | 285 |
| Timeless Enchantment | 0.42% | N/A | N/A |
| Yasha and Kaya | 12% | 4200 | 350 |

These values exclude portions from actives or auras. [corpus:liquipedia_dota2/damage_manipulation@2351852#Spell_Damage_Amplification]

#### Unique Spell Amplification

Kaya-based items are driven by `MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE_UNIQUE`. They do not stack with one another; only the highest value is effective. [corpus:liquipedia_dota2/damage_manipulation@2351852#Unique_Spell_Amplification]

### Outgoing Universal Damage Manipulation

Outgoing universal damage manipulation is driven by `MODIFIER_PROPERTY_TOTALDAMAGEOUTGOING_PERCENTAGE` and generally affects all damage types by percentage.

| Source | Property | Value |
|---|---|---:|
| Aeon Disk — Combo Breaker | Damage Reduction | 100% |
| Clinkz — Burning Barrage | Attack Damage as Damage |  [corpus:liquipedia_dota2/damage_manipulation@2351852#Outgoing_Universal_Damage_Manipulation] |

## Incoming Damage Manipulation

Incoming damage manipulation causes the afflicted unit to take increased or reduced damage depending on whether the source is an enemy or an ally. [corpus:liquipedia_dota2/damage_manipulation@2351852#Incoming_Damage_Manipulation]

### Damage Negation

Damage negation causes an entire damage instance to deal no damage, but the instance remains registered. Effects that react to damage without a minimum-damage threshold can therefore react to negated damage. Damage negation is separated by damage type; generally, the types have no priority between them, so different forms of damage negation can trigger simultaneously. [corpus:liquipedia_dota2/damage_manipulation@2351852#Damage_Negation]

#### Physical Damage Negation

Physical damage negation is driven by `MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_PHYSICAL`. All Ethereal sources provide physical damage negation.

| Category | Source |
|---|---|
| Hero | Leshrac — Nihilism |
| Hero | Muerta — Pierce the Veil |
| Hero | Necrophos — Ghost Shroud |
| Hero | Omniknight — Guardian Angel |
| Hero | Pugna — Decrepify |
| Hero | Winter Wyvern — Cold Embrace |
| Item | Ethereal Blade — Ether Blast |
| Item | Ghost Scepter — Ghost Form [corpus:liquipedia_dota2/damage_manipulation@2351852#Physical_Damage_Negation] |

#### Pure Damage Negation

Pure damage negation is driven by `MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_PURE`. All Debuff Immunity sources provide it, but it does not affect pure damage that pierces Debuff Immunity.

| Source |
|---|
| Black King Bar — Avatar |
| Clockwerk — Power Cogs¹ |
| Dawnbreaker — Starbreaker²ᵇ |
| Earth — Debuff Immunity |
| Elder Titan — Astral Spirit²ᵇ |
| Grimstroke — Dark Portrait |
| Huskar — Life Break, during fly |
| Juggernaut — Blade Fury |
| Legion Commander — Press the Attack¹ |
| Lifestealer — Rage |
| Lion — Mana Drain²ᵇ |
| Pangolier — Roll Up²ᵇ |
| Pangolier — Rolling Thunder [corpus:liquipedia_dota2/damage_manipulation@2351852#Pure_Damage_Negation] |

¹ Requires talent. ²ᵃ Requires Aghanim's Scepter. ²ᵇ Requires Aghanim's Shard. [corpus:liquipedia_dota2/damage_manipulation@2351852#Pure_Damage_Negation]

#### Universal Damage Negation

Universal damage negation is driven by `MODIFIER_PROPERTY_AVOID_DAMAGE` and affects all damage types. Some damage carrying the HP Removal flag can also be negated, but its trigger conditions depend on the ability source.

| Source |
|---|
| Abaddon — Borrowed Time |
| Buildings — Glyph of Fortification |
| Faceless Void — Backtrack |
| Monkey King — Mischief |
| Nyx Assassin — Spiked Carapace |
| Templar Assassin — Refraction [corpus:liquipedia_dota2/damage_manipulation@2351852#Universal_Damage_Negation] |

### Base Damage Manipulation

Armor and magic resistance are the most common damage manipulators, respectively affecting incoming physical and magical damage. [corpus:liquipedia_dota2/damage_manipulation@2351852#Base_Damage_Manipulation]

### Incoming Physical Damage Manipulation

Incoming physical damage manipulation is driven by `MODIFIER_PROPERTY_INCOMING_PHYSICAL_DAMAGE_PERCENTAGE`. It affects only physical attack damage and stacks additively.

| Effect | Source | Property | Value |
|---|---|---|---|
| Amplification | Attack Damage — Reinforced | Attack Damage Bonus Against Reinforced Units | 0.5 |
| Amplification | Medusa — Stone Gaze | Physical Damage Amp | ( ) |
| Reduction | Axe — Counter Helix | Damage Reduction per Stack |  |
| Reduction | Windranger — Windrun | Damage Reduction |  [corpus:liquipedia_dota2/damage_manipulation@2351852#Incoming_Physical_Damage_Manipulation] |

### Generic Incoming Damage Manipulation

Generic incoming damage manipulation is driven by `MODIFIER_PROPERTY_INCOMING_DAMAGE_PERCENTAGE`, and most damage-affecting abilities use it. It increases or reduces damage depending on whether the source is an enemy or ally. All listed sources stack additively, so some 100% reductions can still receive damage when stacked with damage amplification. Some manipulations affect only specific damage, with the exact restrictions belonging to their respective abilities. [corpus:liquipedia_dota2/damage_manipulation@2351852#Generic_Incoming_Damage_Manipulation]

#### Amplification sources

| Source | Property | Value |
|---|---|---|
| Ancient Black Drake — Magic Amplification Aura | Spell Damage Amp | 5%/6%/7%/9% |
| Beastmaster — Wild Axes | Damage Amp per Stack | 5%/6%/7%/8% ( 6.5%/7.5%/8.5%/9.5%) |
| Bounty Hunter — Track | Damage Amp | 8%/12%/16% |
| Courier — Passive Bonus | Incoming Melee Damage Amplification |  |
| Grimstroke — Soulbind | Bound Units Spell Damage Amp | 25% |
| Hoodwink — Hunter's Boomerang | Spell Damage Amp | 20% |
| Undying — Flesh Golem | Damage Amp | 25%/30%/35% |
| Veil of Discord — Magic Weakness | Spell Damage Amp |  [corpus:liquipedia_dota2/damage_manipulation@2351852#Generic_Incoming_Damage_Manipulation] |

#### Reduction sources

| Source | Property | Value |
|---|---|---|
| Aeon Disk — Combo Breaker | Damage Reduction | 100% |
| Bristleback — Bristleback | Rear Damage Reduction | 16%/24%/32%/40% ( 24%/32%/40%/48%) |
| Bristleback — Bristleback | Side Damage Reduction | 8%/12%/16%/20% ( 12%/16%/20%/24%) |
| Leshrac — Pulse Nova | Damage Reduction | 10% |
| Lich — Frost Shield | Attack Damage Reduction | 45%/50%/55%/60% ( 55%/60%/65%/70%) |
| Luna — Lunar Orbit (Moonshield Facet) | Attack Damage Reduction |  |
| Mars — Bulwark | Front Attack Damage Reduction | 40%/50%/60%/70% ( ) |
| Mars — Bulwark | Side Attack Damage Reduction | 20%/25%/30%/35% ( ) |
| Martyr's Plate — Martyrdom | Damage Reduction | 25% |
| Nyx Assassin — Burrow | Damage Reduction | 40% |
| Spectre — Dispersion | Damage Reduction | 9%/12%/15%/18% ( 13%/16%/19%/22%) |
| Underlord — Fiend's Gate | Damage Reduction | 9.5% ( 14.5%) |
| Ursa — Enrage | Damage Reduction | 80% |
| Winter Wyvern — Winter's Curse | Damage Reduction | 0.5 |
| Buildings — Backdoor Protection | Damage Reduction | 0.5 |
| Buildings — Backdoor Protection | Protected Illusion Damage Reduction |  [corpus:liquipedia_dota2/damage_manipulation@2351852#Generic_Incoming_Damage_Manipulation] |

### Unique Damage Negation

Unique damage negation is driven by `MODIFIER_PROPERTY_AVOID_DAMAGE_AFTER_REDUCTIONS`. It applies a constant 100% damage reduction, including against damage carrying the HP Removal flag. Only False Promise belongs to this category. [corpus:liquipedia_dota2/damage_manipulation@2351852#Unique_Damage_Negation]

### Illusion Incoming Damage Manipulation

Illusion incoming damage manipulation is driven by `MODIFIER_PROPERTY_INCOMING_DAMAGE_ILLUSION`. Illusions receive this damage manipulation when taking damage. [corpus:liquipedia_dota2/damage_manipulation@2351852#Illusion_Incoming_Damage_Manipulation]

### Target Dummy Damage Negation

Target Dummy Damage Negation affects all damage, including damage carrying the HP Removal flag. [corpus:liquipedia_dota2/damage_manipulation@2351852#Target_Dummy_Damage_Negation]

### Armor

Every unit, including buildings, has an inherent base armor value and attack class. Physical damage dealt to a unit is multiplied by the damage multiplier, producing damage reduction or amplification according to the target's armor. The damage multiplier also calculates Effective HP: a lower multiplier produces higher Effective HP and vice versa.

| Constant | Symbol | Value |
|---|---|---:|
| Armor Formula Base | \(b\) | 1 |
| Armor Formula Factor | \(f\) | 0.06 |

For every real-valued armor value:

\[
\text{Damage Multiplier}
=1-\frac{f\times R}{b+f\times|R|}
\]

Here, \(DMu\) is the Damage Multiplier and \(R\) is the armor value. The multiplier approaches limits of 0 and 2 for infinitely positive and infinitely negative armor, respectively.

| Armor (+) | Multiplier | Armor (-) | Multiplier |
|---:|---:|---:|---:|
| 1 | 94% | -1 | 106% |
| 2 | 89% | -2 | 111% |
| 3 | 85% | -3 | 115% |
| 4 | 81% | -4 | 119% |
| 5 | 77% | -5 | 123% |
| 6 | 74% | -6 | 126% |
| 7 | 70% | -7 | 130% |
| 8 | 68% | -8 | 132% |
| 9 | 65% | -9 | 135% |
| 10 | 63% | -10 | 138% |
| 11 | 60% | -11 | 140% |
| 12 | 58% | -12 | 142% |
| 13 | 56% | -13 | 144% |
| 14 | 54% | -14 | 146% |
| 15 | 53% | -15 | 147% |
| 16 | 51% | -16 | 149% |
| 17 | 50% | -17 | 150% |
| 18 | 48% | -18 | 152% |
| 19 | 47% | -19 | 153% |
| 20 | 45% | -20 | 155% |
| 21 | 44% | -21 | 156% |
| 22 | 43% | -22 | 157% |
| 23 | 42% | -23 | 158% |
| 24 | 41% | -24 | 159% |
| 25 | 40% | -25 | 160% |
| 26 | 39% | -26 | 161% |
| 27 | 38% | -27 | 162% |
| 28 | 37% | -28 | 163% |
| 29 | 36% | -29 | 164% |
| 30 | 36% | -30 | 164% |
| 31 | 35% | -31 | 165% |
| 32 | 34% | -32 | 166% |
| 33 | 34% | -33 | 166% |
| 34 | 33% | -34 | 167% |
| 35 | 32% | -35 | 168% |
| 36 | 32% | -36 | 168% |
| 37 | 31% | -37 | 169% |
| 38 | 30% | -38 | 170% |
| 39 | 30% | -39 | 170% |
| 40 | 29% | -40 | 171% |
| 41 | 29% | -41 | 171% |
| 42 | 28% | -42 | 172% |
| 43 | 28% | -43 | 172% |
| 44 | 27% | -44 | 173% |
| 45 | 27% | -45 | 173% [corpus:liquipedia_dota2/damage_manipulation@2351852#Armor] |

## Stacking

Armor and magic resistance operate separately from other damage manipulators and always stack multiplicatively with every listed ability. Incoming generic effects stack additively with one another, as do outgoing generic effects. Unique effects stack multiplicatively with one another. After each of these three groups is combined internally, the groups stack multiplicatively with one another.

Conditional manipulation is calculated independently for every damage instance; Bristleback, for example, manipulates only damage striking its back or sides. Outgoing generic manipulation does not affect damage that is Unaffected by Amplification.

The total damage manipulation \(D_M\) is:

\[
D_M=
\left(1+\sum(\text{Generic Incoming Dmg Manip})\right)
\times
\left(1+\sum(\text{Generic Outgoing Dmg Manip})\right)
\times
\prod(\text{1 + Unique Dmg Manip})
\quad\&\quad D_M\geq0
\]

Outgoing manipulation stacks additively in the same manner as incoming manipulation. Because outgoing and incoming calculations occur at different times, with outgoing manipulation calculated first, they stack multiplicatively with each other. [corpus:liquipedia_dota2/damage_manipulation@2351852#Stacking]

### Example 1: Spell Damage Manipulation

Spectre has level 4 Dispersion and is affected by level 3 Fiend's Gate, Magic Weakness, and Ghostship's rum buff. An enemy has cast level 4 Bloodrage on himself and has Kaya.

| Group | Source | Stated value |
|---|---|---|
| Incoming Generic | Dispersion | -0.18 |
| Incoming Generic | Fiend's Gate | -Expression error: Unexpected / operator. |
| Incoming Generic | Magic Weakness | Expression error: Unexpected / operator. |
| Outgoing Generic | Bloodrage | Expression error: Unexpected / operator. |
| Outgoing Generic | Kaya | 0.1 |
| Unique Generic | Ghostship | -Expression error: Unexpected / operator. |

For spell damage:

\[
\begin{aligned}
D_M
&=
\underbrace{
(1-0.18-\text{Expression error: Unexpected / operator.}
+\overbrace{\text{Expression error: Unexpected / operator.}}^{\text{Spell Only}})
}_{\text{Generic Incoming}}
\\
&\quad\times
\underbrace{
(1+\overbrace{\text{Expression error: Unexpected / operator.}+0.1}^{\text{Spell Only}})
}_{\text{Generic Outgoing}}
\times
\underbrace{
(1-\text{Expression error: Unexpected / operator.})
}_{\text{Unique}}
\\
&=
(\text{Expression error: Unexpected < operator.})
\times
(\text{Expression error: Unexpected < operator.})
\times
(\text{Expression error: Unexpected < operator.})
\\
&=\text{Expression error: Unexpected < operator.}\%
\end{aligned}
\]

Magic Weakness, Bloodrage, and Kaya affect only spell damage, so non-spell damage requires another calculation:

\[
\begin{aligned}
D_M
&=
\underbrace{
(1-0.18-\text{Expression error: Unexpected / operator.})
}_{\text{Generic Outgoing}}
\times
\underbrace{(1)}_{\text{Generic Incoming}}
\times
\underbrace{
(1-\text{Expression error: Unexpected / operator.})
}_{\text{Unique}}
\\
&=
(\text{Expression error: Unexpected < operator.})
\times(1)
\times
(\text{Expression error: Unexpected < operator.})
\\
&=\text{Expression error: Unexpected < operator.}\%
\end{aligned}
\]

Spectre would take `Expression error: Unexpected < operator.%` spell damage and `Expression error: Unexpected < operator.%` non-spell damage from the enemy. [corpus:liquipedia_dota2/damage_manipulation@2351852#Example_1:_Spell_Damage_Manipulation]

### Example 2: Additive Stacking

These examples use the highest possible ability level, exclude talents and Aghanim's upgrades unless stated otherwise, and ignore armor and magic resistance.

| Scenario | Stated calculation |
|---|---|
| Ursa is Enraged and affected by Flesh Golem. | `100% - 80% + = Expression error: Missing operand for +.% damage` |
| Spectre has Dispersion and is affected by Fiend's Gate. | `100% - 18% - = Expression error: Missing operand for -.% damage` |
| A hero is affected by Winter's Curse and Flesh Golem simultaneously. | `100% - 2 + = Expression error: Missing operand for +.% damage` [corpus:liquipedia_dota2/damage_manipulation@2351852#Example_2:_Additive_Stacking] |

### Example 3: Other Multiplicative Stacking

These examples use the highest possible ability level, exclude talents and Aghanim's upgrades unless stated otherwise, and ignore armor and magic resistance.

| Scenario | Stated calculation |
|---|---|
| Medusa has activated Mana Shield and is affected by Flesh Golem. | `(100% + ) * (100% - 2%) = Expression error: Missing operand for +.% damage` |
| Medusa has activated Mana Shield and is affected by Ghostship's rum buff and Flesh Golem. | `(100% + ) * (100% - 2%) * (100% - %) = Expression error: Missing operand for +.% damage` |
| A Conjure Image illusion taking 250% damage is affected by Flesh Golem and Fiend's Gate. | `(100% + - ) * 250% = Expression error: Missing operand for +.% damage` [corpus:liquipedia_dota2/damage_manipulation@2351852#Example_3:_Other_Multiplicative_Stacking] |

## Preventing On-damage Effects

Many abilities react when a unit receives damage. Fully negating that damage can prevent some from triggering, but effects that react to 0 damage can still trigger after the damage has been negated. [corpus:liquipedia_dota2/damage_manipulation@2351852#Preventing_On-damage_Effects]

### Effects that do not react to fully negated damage

| Source | Effect |
|---|---|
| Aegis of the Immortal | Expire Restore |
| Ancient Black Dragon | Splash Attack¹ |
| Blink Dagger | Blink |
| Bloodthorn | Soul Rend |
| Bottle | Regenerate |
| Bristleback | Bristleback² |
| Clarity | Replenish |
| Healing Salve | Salve |
| Lifesteal | All sources |
| Lifestealer | Open Wounds |
| Mjollnir | Static Charge |
| Monkey King | Tree Dance |
| Orchid Malevolence | Soul Burn |
| Pugna | Life Drain |
| Runes | Regeneration |
| Spell lifesteal | All sources |
| Spirit Vessel | Soul Release |
| Templar Assassin | Psi Blades¹ |
| Tidehunter | Kraken Shell² |
| Urn of Shadows | Soul Release |
| Visage | Soul Assumption² [corpus:liquipedia_dota2/damage_manipulation@2351852#Preventing_On-damage_Effects] |

¹ These effects work when Aphotic Shield negates the damage. ² These abilities have damage counters that do not work when the damage is negated. [corpus:liquipedia_dota2/damage_manipulation@2351852#Preventing_On-damage_Effects]

### Effects that still react to fully negated damage

| Source | Effect |
|---|---|
| Bane | Nightmare |
| Batrider | Sticky Napalm |
| Battle Fury | Cleave |
| Blade Mail | Damage Return |
| Chen | Divine Favor |
| Death Prophet | Exorcism |
| Dragon Knight | Elder Dragon Form, splash damage |
| Elder Titan | Echo Stomp |
| Invoker | Ghost Walk |
| Kunkka | Tidebringer |
| Lifestealer | Feast |
| Lone Druid | Summon Spirit Bear |
| Magnus | Empower |
| Spectre | Dispersion¹ |
| Spirit Bear | Return |
| Sven | Great Cleave |
| Tiny | Tree Grab |
| Tiny | Tree Throw |
| Viper | Corrosive Skin |
| Warlock | Fatal Bonds¹ [corpus:liquipedia_dota2/damage_manipulation@2351852#Preventing_On-damage_Effects] |

¹ Dispersion's damage and Fatal Bonds' spread damage are unaffected by every form of reduction except magic resistance and armor. [corpus:liquipedia_dota2/damage_manipulation@2351852#Preventing_On-damage_Effects]