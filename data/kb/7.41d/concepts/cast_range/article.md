---
title: Cast Range
kind: concept
patch: 7.41d
card:
  entity: cast_range
  sentences:
  - text: Cast range (c) is the distance at which a hero can use an ability on a target;
      an attempt beyond it makes the hero move into range, while most unit-targeted
      abilities with nonzero cast points have a 250 motion buffer.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234
    - corpus:liquipedia_dota2/cast_range@2363234#Motion_Buffer
  - text: Certain abilities and talents increase cast range, but no talent currently
      increases a hero’s basic cast range.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234
  - text: For no-target abilities, actual range is c = c_b + Σc_i; collision size
      does not count.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#No_Target
  - text: Bonuses increase vector- and area-targeted cast range with the no-target
      formula but do not increase area of effect.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#Vector_Targeting
    - corpus:liquipedia_dota2/cast_range@2363234#Target_Area
  - text: Unit-targeted maximum range is c_b + Σc_i + col_s + col_t + 250, measured
      from the caster’s edge to the target’s edge.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#Target_Unit
  - text: For most unit-targeted abilities, the 250 motion buffer requires the target
      to move at least 251 range away for cancellation.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#Motion_Buffer
  - text: A 0 cast point has no motion buffer; with a nonzero cast point, the cast
      succeeds if affected targets remain within the applicable buffer after the animation.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#Motion_Buffer
  - text: Assassinate has a 600 motion buffer, and Nether Strike has 500.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#Motion_Buffer
  - text: Point-targeted maximum range is c_b + Σc_i + col_s, with no motion buffer.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#Target_Point
  - text: Listed granting bonuses are Spirit Form 40/45/50, Arcane Supremacy 60/120/180/240,
      Boundless Enchantment 275, and Keen-Eyed Enchantment 125/135/145.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#Bonuses
  - text: Documented talent bonus values are 50/60/75/100/125/150/175/200/225/250/275/300/325/350/400.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#Details
  - text: Bane’s Enfeeble and Tinker’s Warp Flare reduce an affected target’s cast
      range by a percentage.
    marks:
    - corpus:liquipedia_dota2/cast_range@2363234#Reductions
---

# Cast Range

Cast range (\(c\)) is the distance at which a hero may use an ability on its target. Attempting to cast beyond this range causes the hero to move within range before casting. Certain abilities and specific talents can increase cast range, but no talents currently increase a hero’s basic cast range. [corpus:liquipedia_dota2/cast_range@2363234]

## Collision Size Bonus Range

An ability’s maximum or actual cast range depends on the hero’s collision size and the ability’s targeting type. [corpus:liquipedia_dota2/cast_range@2363234#Collision_Size_Bonus_Range]

### No Target

No-target abilities are cast immediately when their button is pressed. Many lack a cast time, but they do not have an instant cast time. They cannot directly target a unit or point; the same applies to abilities toggled on or off. Only flat cast-range bonuses count, not collision size.

\[
c=c_b+\sum_{i=1}^{n}c_i
\]

Here, \(c_b\) is the ability’s base cast range and \(c_i\) represents cast-range bonus sources. [corpus:liquipedia_dota2/cast_range@2363234#No_Target]

#### Vector Targeting

Cast-range bonuses increase every vector-targeting ability’s cast range using the no-target formula, but do not increase its area of effect. [corpus:liquipedia_dota2/cast_range@2363234#Vector_Targeting]

#### Target Area

Cast-range bonuses increase every area-targeted ability’s cast range using the no-target formula, but do not increase its area of effect. The related mechanic is **Area of Effect Increasing**. [corpus:liquipedia_dota2/cast_range@2363234#Target_Area]

### Target Unit

Unit-targeted abilities require the caster to target a unit directly and cannot be used on the ground. Their actual range is slightly greater than the displayed value because of a **250** motion buffer: if the target moves beyond cast range but remains within an additional **250** range when the cast point completes, the ability is cast.

Range is measured from the caster’s edge to the target’s edge, accounting for both units’ collision sizes:

\[
\max\{c\}=c_b+\sum_{i=1}^{n}c_i+col_s+col_t+250
\]

Here, \(c_b\) is the base cast range, \(c_i\) represents cast-range bonus sources, \(col_s\) is the caster’s collision size, and \(col_t\) is the target’s collision size. The related mechanic is **Attack Range**. [corpus:liquipedia_dota2/cast_range@2363234#Target_Unit]

#### Motion Buffer

When the distance between caster and target exceeds the default cast range during the cast animation, the motion buffer can still allow the ability to be cast. For most unit-targeted abilities, the default buffer is **250**; the target must move at least **251** range away for the ability to be canceled. If the target is outside the buffer, the ability is cast once the target and caster move within the default range.

When an ability’s cast point is not **0**, it is cast successfully after its cast animation if the affected target or targets remain within the applicable motion buffer. An ability with a cast point of **0** has no cast-range buffer.

| Ability | Motion Buffer Range |
|---|---:|
| Sniper — Assassinate | 600 |
| Spirit Breaker — Nether Strike | 500 |

[corpus:liquipedia_dota2/cast_range@2363234#Motion_Buffer]

#### Example: Lucent Beam

Luna casts Lucent Beam on an enemy Abaddon.

| Type | Source | Value |
|---|---|---:|
| Cast range | Lucent Beam | 800 |
| Collision size | Luna | 27 |
| Collision size | Abaddon | 27 |

\[
\max\{c\}
=800+\underbrace{(27+27)}_{\text{Collision Size}}
+\underbrace{(250)}_{\text{Buffer}}
=1104
\]

Lucent Beam’s actual cast range in this example is **1104**, rather than **800**. [corpus:liquipedia_dota2/cast_range@2363234#Example]

### Target Point

Point-targeted abilities require the caster to target a point or area. Both flat cast-range bonuses and edge-to-edge range based on the caster’s and target’s collision sizes are considered, but the motion buffer is not.

\[
\max\{c\}=c_b+\sum_{i=1}^{n}c_i+col_s
\]

[corpus:liquipedia_dota2/cast_range@2363234#Target_Point]

#### Example: Waveform

Morphling casts Waveform.

| Type | Source | Value |
|---|---|---:|
| Cast range | Level 4 Waveform | 925 |
| Collision size | Morphling | 27 |

\[
\max\{c\}=925+27=952
\]

Waveform has a maximum cast range of **952** in this example. [corpus:liquipedia_dota2/cast_range@2363234#Example_2]

## Other Cast-Range Bonuses

Some abilities use different cast ranges or provide bonuses only under specific conditions.

| Source | Stated ranges or bonuses | Conditions and effects |
|---|---|---|
| Dragon Knight — Elder Dragon Form | Dragon Tail Cast Range Bonus: 300<br>Fireball Cast Range Bonus: 800 | While in Dragon Form, Dragon Tail and Fireball have **450** and **1400** cast range respectively. |
| Earth Spirit — Boulder Smash | Unit Cast Range: 150<br>Stone Cast Range:<br>Stone Knockback Distance: 2000 | Has **150** cast range when smashing a unit. Its cast range equals the stone knockback distance when smashing a Stone Remnant within a radius or targeting a Stone Remnant farther away. |
| Earth Spirit — Enchant Remnant | Cast Range (Ally/Self): 500<br>Cast Range (Enemy): 175 | — |
| Nyx Assassin — Impale | Cast Range: 750 (1250)<br>Spikes Travel Distance: 750 (1250) | Cast range and travel distance increase while Burrowed. |
| Nyx Assassin — Mind Flare | Cast Range: 800 ( ) | Cast range increases while Burrowed. |
| Force Staff — Force | Cast Range (Ally/Self): 550<br>Cast Range (Enemy): 850 | — |
| Hurricane Pike — Hurricane Thrust | Cast Range (Ally/Self): 425<br>Cast Range (Enemy): 650<br>Push Distance (Ally/Self): 425<br>Push Distance (Enemy): 600 | — |

[corpus:liquipedia_dota2/cast_range@2363234#Other_Cast_Range_Bonuses]

## Cast-Range Granting Abilities

Special interactions with cast-range increases are collected under **Cast Range Interactions**. [corpus:liquipedia_dota2/cast_range@2363234#Cast_Range_Granting_Abilities]

### Bonuses

| Source | Bonus Cast Range | Notes |
|---|---|---|
| Keeper of the Light — Spirit Form | 40/45/50 | — |
| Rubick — Arcane Supremacy | 60/120/180/240 | Passive. |
| Aether Lens — Aethereal Focus |  | Does not stack with Aether Lens-based items. This is an old ability. |
| Boundless Enchantment | 275 | Tier 5 neutral item enchantment. |
| Keen-Eyed Enchantment | 125/135/145 | Tier 2–3 neutral item enchantment. |
| Mystical Enchantment |  | Tier 1–4 neutral item enchantment. |

[corpus:liquipedia_dota2/cast_range@2363234#Bonuses]

### Talents

**Cast Range** is a passive ability affecting self. It increases the hero’s cast range, and its **Cast Range Bonus** varies. [corpus:liquipedia_dota2/cast_range@2363234#Talents]

#### Details

The following bonus values exist:

`50/60/75/100/125/150/175/200/225/250/275/300/325/350/400`

General increased-cast-range talents use the bonus label **Cast Range** and are organized by **Level 10**, **Level 15**, **Level 20**, and **Level 25**, each divided into **Left** and **Right**.

| Hero and talent | Stated effect |
|---|---|
| Arc Warden — Talent by Level 10 Right | +200 Flux Cast Range: |
| Bloodseeker — Talent by Level 20 Right | +400 Rupture Cast Range: |
| Grimstroke — Talent by Level 20 Right | +80% Stroke of Fate Damage: |
| Monkey King — Talent by Level 15 Right | No Primal Spring Cooldown: |
| Morphling — Talent by Level 10 Left | +12s Morph Duration: |
| Phoenix — Talent by Level 25 Left | +1000 Icarus Dive Cast Range: |
| Timbersaw — Talent by Level 25 Left | x1.75 Timber Chain Range/Projectile Speed: |

[corpus:liquipedia_dota2/cast_range@2363234#Details]

### Reductions

The following abilities reduce an affected target’s cast range by a percentage:

| Hero | Ability |
|---|---|
| Bane | Enfeeble |
| Tinker | Warp Flare |

[corpus:liquipedia_dota2/cast_range@2363234#Reductions]

## Patch History

| Date | Description |
|---|---|
| 21 May 2025 | Hovering over abilities with long cast ranges now also shows the cast range on the minimap. |
| 01 Oct 2022 | Fixed certain abilities’ mouse-hover previews not interacting correctly with cast-range bonuses, such as Arcane Supremacy. |
| 08 Aug 2019 | Hovering over a unit’s portrait now displays a range finder for its current vision range.<br>Ability ranges are now shown when hovering over enemy hero abilities, using the maximum-level ranges.<br>Fixed cases where the cast-range range finder did not match the actual cast range, such as Earth Spike. |

[corpus:liquipedia_dota2/cast_range@2363234#Patch_History]