---
title: Cooldown
kind: concept
patch: 7.41d
card:
  entity: cooldown
  sentences:
  - text: A cooldown is a waiting period before a spell, ability, or item power can
      be used again.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634
  - text: An ability usually enters cooldown after activation and completion of its
      cast time.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Mechanics
  - text: Activating one version of an item puts every version in its shared cooldown
      group on cooldown.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Mechanics
  - text: Final cooldown is calculated as `CD = (Base CD - Σ Flat Reductions) × %
      CD Reductions Multiplier - Σ Current CDR`.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Reduction
  - text: Flat cooldown reductions apply before percentage-based changes and stack
      additively.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Flat_Reduction
  - text: Current cooldown reductions apply after percentage-based changes, affect
      running cooldowns, and stack additively.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Current_Cooldown_Reduction
  - text: Percentage-based modifiers affect items, passives, and charge replenish
      times but do not retroactively change running cooldowns.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Percentage-based
  - text: Percentage-based reductions stack multiplicatively as `%CD Reduction Multiplier
      = ∏ᵢ₌₁ⁿ(1 - rᵢ)`.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Percentage-based
  - text: In the Level 1 Black Hole example, a 180 cooldown, 25% reductions from Octarine
      Core and Arcane Rune, and a -20-second talent reduction produce a 90-second
      cooldown.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Examples
  - text: Casting a charge-based ability consumes one charge instead of putting the
      ability on cooldown.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Charges
  - text: Multiple missing charges replenish one after another rather than simultaneously.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Charges
  - text: Some abilities instantly reset ability or item cooldowns, making them ready
      for use again.
    marks:
    - corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting
---

# Cooldown

A cooldown is a waiting period before a spell, ability, or item power can be used again. [corpus:liquipedia_dota2/cooldown@2391634]

## Mechanics

An ability usually enters cooldown after it is activated and its cast time has passed. If a hero is interrupted before the channel time ends, the ability does nothing, while its cooldown and mana are wasted. Abilities with long cast times, including Assassinate and Requiem of Souls, do not enter cooldown until the cast time ends. Charge of Darkness instead enters cooldown when the charge ends or is canceled. [corpus:liquipedia_dota2/cooldown@2391634#Mechanics]

Activating one version of an item puts every version of that item on cooldown; all Dagons, for example, share a cooldown group. Some abilities and items use different cooldown durations when their conditions are met: Culling Blade has a cooldown of 0 only when it successfully kills a hero. [corpus:liquipedia_dota2/cooldown@2391634#Mechanics]

Many abilities gain reduced cooldowns when leveled, but leveling an ability that is already on cooldown does not alter its current wait time. Some abilities instead have charges with an individual replenish time; Shrapnel is an example. [corpus:liquipedia_dota2/cooldown@2391634#Mechanics]

## Cooldown reduction

The total or final cooldown of an ability is defined as:

`CD = (Base CD - Σ Flat Reductions) × % CD Reductions Multiplier - Σ Current CDR` [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Reduction]

### Flat reduction

Flat cooldown modifiers change cooldowns by flat amounts and can affect abilities already on cooldown. They are applied before percentage-based changes, and multiple flat cooldown reductions stack additively. [corpus:liquipedia_dota2/cooldown@2391634#Flat_Reduction]

| Source | Effect |
|---|---|
| Invoker — Invoke | Invoke Cooldown Reduction per Orb Level: 0.3. Each level of Quas, Wex, and Exort reduces the ability’s cooldown. [corpus:liquipedia_dota2/cooldown@2391634#Flat_Reduction] |

#### Talents

Cooldown Reduction is passive, affects the hero itself, has a varying reduction, and reduces all of the hero’s cooldowns. Multiple percentage-based cooldown reduction sources do not stack; the highest value takes priority. [corpus:liquipedia_dota2/cooldown@2391634#Talents]

| Existing cooldown-reduction values |
|---|
| 6%/8%/10%/12%/14%/15%/20%/25%/30%/40%/50%/65% [corpus:liquipedia_dota2/cooldown@2391634#Talents] |

The modifier is hidden. Heroes can have talents that grant cooldown reduction at levels 10, 15, 20, or 25 on either the left or right talent choice. Some hero talents instead reduce the cooldowns of specific abilities by a flat amount. [corpus:liquipedia_dota2/cooldown@2391634#Talents]

### Current cooldown reduction

Current cooldown modifiers change current cooldowns by flat amounts and affect abilities already on cooldown. They are applied after percentage-based changes, and multiple current flat cooldown reductions stack additively. [corpus:liquipedia_dota2/cooldown@2391634#Current_Cooldown_Reduction]

| Source | Requirement |
|---|---|
| Abaddon — The Quickening | Requires facet. [corpus:liquipedia_dota2/cooldown@2391634#Current_Cooldown_Reduction] |
| Dazzle — Bad Juju | — [corpus:liquipedia_dota2/cooldown@2391634#Current_Cooldown_Reduction] |
| Keeper of the Light — Chakra Magic | — [corpus:liquipedia_dota2/cooldown@2391634#Current_Cooldown_Reduction] |
| Windranger — Focus Fire | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Current_Cooldown_Reduction] |

The source requirement markers are: `1` requires talent; `2a` requires Aghanim’s Scepter; `2b` requires Aghanim’s Shard; and `3` requires facet. [corpus:liquipedia_dota2/cooldown@2391634#Current_Cooldown_Reduction]

### Percentage-based changes

Percentage-based modifiers reduce or increase the cooldowns of all abilities and items by a percentage when used. After such a modifier is acquired, abilities and items enter reduced or increased cooldowns, but already-running cooldowns are not retroactively changed. These modifiers affect all cooldowns, including items, passives, and charge replenish times. [corpus:liquipedia_dota2/cooldown@2391634#Percentage-based]

Multiple percentage-based cooldown reductions stack multiplicatively. Their multiplier is:

`%CD Reduction Multiplier = ∏ᵢ₌₁ⁿ(1 - rᵢ)` [corpus:liquipedia_dota2/cooldown@2391634#Percentage-based]

| Percentage-based cooldown-changing source |
|---|
| Ancient Frostbitten Golem — Time Warp Aura [corpus:liquipedia_dota2/cooldown@2391634#Percentage-based] |
| Runes — Arcane [corpus:liquipedia_dota2/cooldown@2391634#Percentage-based] |
| Octarine Core — Cooldown Reduction [corpus:liquipedia_dota2/cooldown@2391634#Percentage-based] |
| Faceless Void — Time Dilation [corpus:liquipedia_dota2/cooldown@2391634#Percentage-based] |
| Faceless Void — Time Zone [corpus:liquipedia_dota2/cooldown@2391634#Percentage-based] |

### Unique percentage-based sources

The following abilities provide cooldown reduction under specific conditions. [corpus:liquipedia_dota2/cooldown@2391634#Unique_Percentage-based_Sources]

| Source | Values and conditions |
|---|---|
| Nyx Assassin — Burrow | Cooldown Reduction: 25%. Reduces the cooldown of Impale, Mind Flare, and Spiked Carapace while burrowed. [corpus:liquipedia_dota2/cooldown@2391634#Unique_Percentage-based_Sources] |
| Rubick — Spell Steal | Stolen Spell Cooldown Reduction: —. Applies only to the acquired ability. [corpus:liquipedia_dota2/cooldown@2391634#Unique_Percentage-based_Sources] |
| Telescope — Prescient Aura | Radius: 1200; Scan Cooldown Reduction: 50%; Aura Linger Duration: 0.5. The aura affects all nearby allies, and multiple instances do not stack. This is an old ability. [corpus:liquipedia_dota2/cooldown@2391634#Unique_Percentage-based_Sources] |

### Ratio

Ratio-based cooldown manipulation comprises Acceleration and Deceleration. [corpus:liquipedia_dota2/cooldown@2391634#Ratio]

### Example

For a Level 1 Black Hole when Enigma has Octarine Core, is affected by Arcane Rune, and has a talent-specific 20 seconds ability bonus cooldown reduction:

| Component | Value |
|---|---|
| Black Hole Level 1 cooldown | 180 [corpus:liquipedia_dota2/cooldown@2391634#Examples] |
| Octarine Core cooldown reduction | 25% [corpus:liquipedia_dota2/cooldown@2391634#Examples] |
| Arcane Rune cooldown reduction | 25% [corpus:liquipedia_dota2/cooldown@2391634#Examples] |
| Talent-specific flat cooldown reduction | -20 seconds [corpus:liquipedia_dota2/cooldown@2391634#Examples] |

`Percentage-based Cooldown Reduction Multiplier = (1 - 0.25) × (1 - 0.25) = 0.5625`

`Final Ability Cooldown = (180 - 20) × 0.5625 = 90`

Enigma’s Level 1 Black Hole cooldown is 90 seconds in this example. [corpus:liquipedia_dota2/cooldown@2391634#Examples]

## Cooldown resetting

Some abilities instantly reset ability and item cooldowns, making them ready to use again. Rearm does not reset the cooldowns of Aeon Disk, Arcane Boots, Black King Bar, Hand of Midas, Helm of the Dominator, Helm of the Overlord, Linken’s Sphere, Meteor Hammer, Pipe of Insight, Refresher Orb, Refresher Shard, or Neutral Items. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting]

| Source | Reset behavior |
|---|---|
| Axe — Culling Blade | Resets its own cooldown when the kill succeeds. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting] |
| Ex Machina — Reset Cooldowns | Resets all item cooldowns except Refresher Orb and Refresher Shard. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting] |
| Grimstroke — Phantom’s Embrace | Resets its own cooldown when the Phantom successfully returns to the caster. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting] |
| Invoker — Invoke | Resets its own cooldown when invoking an already invoked ability. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting] |
| Phoenix — Supernova | Resets all basic-ability cooldowns for Phoenix and the allied hero. It does not reset item cooldowns. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting] |
| Phantom Assassin — Blur | Killing an enemy hero resets all her basic-ability cooldowns. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting] |
| Refresher Orb — Reset Cooldowns | Resets all ability and item cooldowns except those of other Refresher Orbs, Refresher Shard, and Ex Machina. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting] |
| Refresher Shard — Reset Cooldowns | Resets all ability and item cooldowns except Refresher Orb and Ex Machina. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting] |
| Tinker — Rearm | Resets hero abilities but not hero items. [corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Resetting] |

## Other interactions

| Source | Interaction |
|---|---|
| Blink Dagger — Blink | Taking hero- or Roshan-based damage triggers a short cooldown. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Arcane Blink — Arcane Blink | Taking hero- or Roshan-based damage triggers a short cooldown. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Overwhelming Blink — Overwhelming Blink | Taking hero- or Roshan-based damage triggers a short cooldown. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Swift Blink — Swift Blink | Taking hero- or Roshan-based damage triggers a short cooldown. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Guardian Greaves — Mend | The heal-restricting buff’s duration is affected by percentage-based cooldown reductions. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Mekansm — Restore | The heal-restricting buff’s duration is affected by percentage-based cooldown reductions. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Crimson Guard — Guard | The guard stack-restricting buff’s duration is affected by percentage-based cooldown reductions. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Linken’s Sphere — Transfer Spellblock | Triggers its cooldown upon cast and again when the allied buff blocks a spell. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Lifestealer — Infest | The cooldown triggers upon leaving the infested unit rather than upon cast. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Morphling — Adaptive Strike (Agility) | Casting Adaptive Strike (Agility) puts Adaptive Strike (Strength) on a second cooldown. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Morphling — Adaptive Strike (Strength) | Casting Adaptive Strike (Strength) puts Adaptive Strike (Agility) on a second cooldown. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Monkey King — Tree Dance | Taking hero- or Roshan-based damage triggers a short cooldown. A cooldown also triggers upon landing on a tree after a jump and upon unperching from a tree. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Sniper — Take Aim | The cooldown triggers upon losing the provided buff rather than upon cast. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Spirit Bear — Return | Taking hero- or Roshan-based damage triggers a short cooldown. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Spirit Breaker — Charge of Darkness | The cooldown triggers when the charge ends rather than upon cast. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Tiny — Tree Grab | The cooldown triggers upon losing the tree rather than upon cast. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Tranquil Boots — Break | The downtime is affected by percentage-based cooldown reductions but cannot be reset. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Tumbler’s Toy — Vault | Taking hero- or Roshan-based damage triggers a short cooldown. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |
| Visage — Stone Form | The hero’s sub-ability periodically sets its cooldown equal to the shortest Stone Form cooldown among the Familiars. [corpus:liquipedia_dota2/cooldown@2391634#Other_Interactions] |

### Unaffected by cooldown manipulation

An ability may be unaffected by default cooldown manipulation because it uses a custom cooldown system or because its cooldown serves another purpose, such as indicating a delay before an effect takes place. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation]

| Ability | Value | Behavior |
|---|---:|---|
| Abyssal Blade — Bash | Cooldown: 2.3 | Unlike Skull Basher, it uses a custom cooldown because a regular cooldown would prevent use of the item’s active ability. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Blink Dagger — Blink | Damage Cooldown: — | Damage puts it on a fixed cooldown instead of disabling it. This cooldown is unaffected by cooldown resetting. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Arcane Blink — Arcane Blink | Damage Cooldown: — | Damage puts it on a fixed cooldown instead of disabling it. This cooldown is unaffected by cooldown resetting. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Overwhelming Blink — Overwhelming Blink | Damage Cooldown: — | Damage puts it on a fixed cooldown instead of disabling it. This cooldown is unaffected by cooldown resetting. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Swift Blink — Swift Blink | Damage Cooldown: — | Damage puts it on a fixed cooldown instead of disabling it. This cooldown is unaffected by cooldown resetting. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Fallen Sky — Fallen Sky | Damage Cooldown: — | Damage puts Fallen Sky on a fixed cooldown instead of disabling it. This cooldown is affected by cooldown resetting. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Crimson Guard — Guard | Stack Limit Duration: 7 | The stack-limit duration is set upon cast and is unaffected by cooldown manipulation. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Guardian Greaves — Mend | Heal Stack Limit Duration: — | The heal stack-limit duration is set upon cast and is unaffected by cooldown manipulation. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Holy Locket — Energy Charge | Passive Charge Gain Interval: 15 | Cooldown reduction does not reduce the interval; it is always 1 charge per 15 seconds. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Linken’s Sphere — Transfer Spellblock | Cooldown: — | The cooldown triggered when blocking a spell for an ally always uses the default cooldown value for unknown reasons. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Mekansm — Restore | Heal Stack Limit Duration: — | The heal stack-limit duration is set upon cast and is unaffected by cooldown manipulation. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Monkey King — Tree Dance | Damage Cooldown: — | Damage puts Tree Dance on a fixed cooldown instead of disabling it. This cooldown is affected by cooldown resetting. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Gleipnir — Chain Lightning | Cooldown: — | Uses a custom cooldown because a regular cooldown would prevent use of the item’s active ability. This is an old ability. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Maelstrom — Chain Lightning | Cooldown: — | Uses a custom cooldown system for unknown reasons. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Mjollnir — Chain Lightning | Cooldown: — | Uses a custom cooldown because a regular cooldown would prevent use of the item’s active ability. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Riki — Cloak and Dagger | Fade Delay: 4/3/2 | Uses the cooldown system to indicate the invisibility fade delay; it has visual purposes only. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Slark — Pounce | — | During the leap, Pounce is on a non-refreshable cooldown bound to the leap buff. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |
| Treant Protector — Nature’s Guise | Fade Delay: — | Uses the cooldown system to indicate the invisibility fade delay; it has visual purposes only. [corpus:liquipedia_dota2/cooldown@2391634#Unaffected_by_Cooldown_Manipulation] |

## Charges

Charge-based abilities have a set number of charges that replenish over time. Each cast consumes one charge instead of putting the ability on cooldown. Multiple charges permit rapid successive casts, but the ability cannot be used with no charges remaining. Every charge takes a specified time to replenish, and multiple missing charges recharge one after another rather than simultaneously. [corpus:liquipedia_dota2/cooldown@2391634#Charges]

After the final charge is used, the ability appears to be on cooldown, but this display only visualizes when the next charge will become ready. Current charges and recharge time are shown as a number at the bottom-left corner of the ability icon, surrounded by a green circle that fills while a charge recharges. [corpus:liquipedia_dota2/cooldown@2391634#Charges]

Charge replenish time can be affected by the cooldown reductions of Octarine Core, Arcane Rune, and talents. Refresher Orb can replenish all charges, while Chakra Magic and Time Dilation also affect them. Other cooldown-manipulation sources cannot restore charges or affect recharge times. [corpus:liquipedia_dota2/cooldown@2391634#Charges]

### Charge-based abilities

| Ability | Requirement |
|---|---|
| Batrider — Flamebreak | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Bloodseeker — Rupture | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Broodmother — Spin Web | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Broodmother — Spinner’s Snare | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Clinkz — Death Pact | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Dark Seer — Ion Shell | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Death Prophet — Spirit Siphon | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Disruptor — Kinetic Fence | Requires selecting the corresponding facet. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Doom — Devour | Requires selecting the corresponding facet. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Earth Spirit — Stone Remnant | Requires selecting the corresponding facet. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Ember Spirit — Fire Remnant | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Ember Spirit — Sleight of Fist | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Hoodwink — Acorn Shot | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Hoodwink — Scurry | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Keeper of the Light — Recall | Requires selecting the corresponding facet and Aghanim’s Shard. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Keeper of the Light — Solar Bind | Requires selecting the corresponding facet and Aghanim’s Shard. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Largo — Catchy Lick | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Mirana — Leap | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Muerta — Dead Shot | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Phoenix — Launch Fire Spirit | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Riki — Blink Strike | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Ringmaster — Escape Act | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Ringmaster — Impalement Arts | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Shadow Demon — Demonic Purge | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Shadow Demon — Disruption | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Silencer — Arcane Curse | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Slark — Pounce | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Sniper — Shrapnel | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Techies — Proximity Mines | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Tiny — Toss | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Treant Protector — Eyes In The Forest | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Ursa — Earthshock | Requires talent. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Venomancer — Plague Ward | Requires selecting the corresponding facet. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Void Spirit — Astral Step | — [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |
| Void Spirit — Resonant Pulse | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities] |

The requirement markers are: `1` requires talent; `2a` requires Aghanim’s Scepter; `2b` requires Aghanim’s Shard; `3a` requires selecting the corresponding facet; and `3b` requires selecting the corresponding facet and Aghanim’s Shard. [corpus:liquipedia_dota2/cooldown@2391634#Charge-based_Abilities]

### Self-restoring item charges

| Item ability |
|---|
| Hand of Midas — Transmute [corpus:liquipedia_dota2/cooldown@2391634#Self-Restoring_Item_Charges] |
| Holy Locket — Energy Charge [corpus:liquipedia_dota2/cooldown@2391634#Self-Restoring_Item_Charges] |
| Royal Jelly — Consume [corpus:liquipedia_dota2/cooldown@2391634#Self-Restoring_Item_Charges] |

## Recent changes

| Version | Date | Description |
|---|---|---|
| 7.31 | 2022-02-23 | Percentage-based cooldown reductions now stack multiplicatively. [corpus:liquipedia_dota2/cooldown@2391634#Recent_Changes] |
| 7.30 | 2021-08-18 | Percentage-based cooldown reductions no longer stack. REMOVED REPLACED all cooldown reduction talents. [corpus:liquipedia_dota2/cooldown@2391634#Recent_Changes] |
| 7.06 | 2017-05-15 | Refresher Orb now replenishes all charges to charge-based abilities. [corpus:liquipedia_dota2/cooldown@2391634#Recent_Changes] |