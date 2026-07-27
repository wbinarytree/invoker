---
title: Attack Animation
kind: concept
patch: 7.41d
card:
  entity: attack_animation
  sentences:
  - text: Attack animation is the two-part period every unit requires to perform an
      attack—an attack point before the attack lands and a backswing afterward—during
      which it generally cannot perform other actions, including moving.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432
    - corpus:liquipedia_dota2/attack_animation@2383432#Definition
  - text: Players can cancel either phase, but canceling the foreswing cancels the
      attack while canceling the backswing has no consequence.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Definition
  - text: Effective timings are Ap = Bp × 100/ΣAS × (1 + APManip) and Ab = Bb × 100/ΣAS,
      where Bp and Bb are the base timings.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Definition
  - text: Only the highest attack-point manipulation value applies.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Definition
  - text: Attack animation defines the delay from issuing an attack order to launching
      the attack, independently of the unit’s attack speed.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Definition
  - text: A 1-second attack cycle with a 0.3-second attack point and 0.5-second backswing
      contains 0.2 seconds of idle time.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Definition
  - text: Canceling that backswing after 0.2 seconds increases the idle period to
      0.5 seconds.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Definition
  - text: Movement and spell-cast commands can be issued during the idle period.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Definition
  - text: Canceling an animation does not let the unit attack faster.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Definition
  - text: During a manually cast active attack modifier, repeated move commands do
      not cancel the cast, and the first command after the cast point cancels the
      backswing.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Orb_Walking
  - text: During a regular attack, a move command cancels the attack unless issued
      after it launches.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Orb_Walking
  - text: Orb walking also means stutter stepping by canceling attack backswings to
      move between attacks and follow a target.
    marks:
    - corpus:liquipedia_dota2/attack_animation@2383432#Orb_Walking
---

# Attack Animation

The movement-speed advantage required to achieve a given attack efficiency while chasing depends on attack animation. Every unit has an attack animation: the time required to perform an attack, during which the unit generally cannot perform other actions, including moving. [corpus:liquipedia_dota2/attack_animation@2383432]

## Definition

An attack animation consists of a **foreswing**, or **attack point**, before the attack lands and a **backswing** afterward. Players can manually cancel either component, while AI units such as lane creeps generally do not. Canceling the backswing has no consequences, but canceling the foreswing cancels the attack. Different heroes’ animation times affect their ability to last-hit, deny, and attack enemies while chasing. Unlike cast animation, losing vision does not cancel an attack animation. [corpus:liquipedia_dota2/attack_animation@2383432#Definition]

Total attack speed affects both the effective attack point and effective attack backswing:

\[
A_p=B_p\times\frac{100}{\sum AS}\times(1+AP_{Manip})
\]

\[
A_b=B_b\times\frac{100}{\sum AS}
\]

Here, \(A_p\) and \(A_b\) are the effective attack point and backswing, \(B_p\) and \(B_b\) are their base values, and \(AP_{Manip}\) is the value of an attack-point manipulation effect. Only the highest attack-point manipulation value is counted. [corpus:liquipedia_dota2/attack_animation@2383432#Definition]

A unit’s attack speed is otherwise completely independent of its attack animation. Attack animation strictly describes the delay between issuing an attack order and launching the attack. A unit with a 1-second attack time, 0.3-second attack point, and 0.5-second backswing is idle for 0.2 seconds during each attack cycle. [corpus:liquipedia_dota2/attack_animation@2383432#Definition]

If that backswing is canceled after 0.2 seconds, the idle period extends to 0.5 seconds:

\[
0.5=
\underbrace{0.2}_{\text{Original Idle Time}}
+\underbrace{0.5}_{\text{Backswing}}
-\underbrace{0.2}_{\text{Cancelled Completed Backswing Time}}
\]

Other commands, including movement and spell casts, can be issued during this idle period. Canceling an animation therefore does not allow the unit to attack faster. [corpus:liquipedia_dota2/attack_animation@2383432#Definition]

### Attack Animation Manipulation

The following abilities can change attack-animation speed:

| Hero | Ability |
|---|---|
| Nyx Assassin | Vendetta |
| Tusk | Walrus PUNCH! |

[corpus:liquipedia_dota2/attack_animation@2383432#Attack_Animation_Manipulation]

### Orb Walking

While an active attack modifier is being manually cast, the player can repeatedly issue move commands without canceling the ongoing cast. The first move command issued after the cast point is reached cancels the backswing, allowing the hero to move almost immediately after launching the attack. [corpus:liquipedia_dota2/attack_animation@2383432#Orb_Walking]

Issuing move commands during a regular attack instead cancels the attack and moves the unit immediately, so the player must time the command after the attack launches. Stutter stepping was therefore much easier with manually cast active attack modifiers because the move command required no timing, allowing more effective stutter stepping. [corpus:liquipedia_dota2/attack_animation@2383432#Orb_Walking]

A later use of **orb walking** refers to using attacks or active attack modifiers to achieve **stutter stepping**: canceling an attack’s backswing so the unit can move between attacks and follow its target instead of standing still until the backswing finishes. [corpus:liquipedia_dota2/attack_animation@2383432#Orb_Walking]

## Attack Animations of Heroes

| Hero | Attack Range | Attack Point | Attack Backswing | Projectile Speed |
|---|---:|---:|---:|---:|
| Shadow Fiend | Melee | 0.5 | 0.54 | - |
| Drow Ranger | Melee | 0.5 | 0.3 | - |
| Sven | Melee | 0.4 | 0.3 | - |
| Pugna | Melee | 0.5 | 0.5 | - |
| Clockwerk | Melee | 0.33 | 0.64 | - |
| Earthshaker | Melee | 0.467 | 0.863 | - |
| Ancient Apparition | Melee | 0.45 | 0.3 | - |
| Weaver | Melee | 0.55 | 0.36 | - |
| Lina | Melee | 0.65 | 0.6 | - |
| Vengeful Spirit | Melee | 0.33 | 0.64 | - |
| Tidehunter | Melee | 0.6 | 0.56 | - |
| Lion | Melee | 0.43 | 0.74 | - |
| Morphling | Melee | 0.5 | 0.5 | - |
| Axe | Melee | 0.4 | 0.5 | - |
| Doom | Melee | 0.5 | 0.7 | - |
| Bloodseeker | Melee | 0.43 | 0.74 | - |
| Lich | Melee | 0.46 | 0.54 | - |
| Tiny | Melee | 0.4 | 0.7 | - |
| Razor | Melee | 0.3 | 0.4 | - |
| Viper | Melee | 0.33 | 1 | - |
| Spectre | Melee | 0.3 | 0.7 | - |
| Leshrac | Melee | 0.4 | 0.6 | - |
| Slardar | Melee | 0.36 | 0.64 | - |
| Windranger | Melee | 0.4 | 0.3 | - |
| Mirana | Melee | 0.35 | 0.7 | - |
| Chen | Melee | 0.5 | 0.5 | - |
| Nature's Prophet | Melee | 0.4 | 0.6 | - |
| Venomancer | Melee | 0.3 | 0.7 | - |
| Storm Spirit | Melee | 0.5 | 0.3 | - |
| Puck | Melee | 0.5 | 0.8 | - |
| Beastmaster | Melee | 0.3 | 0.7 | - |
| Sand King | Melee | 0.53 | 0.47 | - |
| Night Stalker | Melee | 0.55 | 0.55 | - |
| Necrophos | Melee | 0.3 | 0.47 | - |
| Ringmaster | Melee | 0.5 | 0.93 | - |
| Abaddon | Melee | 0.56 | 0.41 | - |
| Dragon Knight | Melee | 0.5 | 0.5 | - |
| Luna | Melee | 0.35 | 0.54 | - |
| Pudge | Melee | 0.5 | 1.17 | - |
| Undying | Melee | 0.3 | 0.3 | - |
| Lycan | Melee | 0.55 | 0.25 | - |
| Alchemist | Melee | 0.35 | 0.65 | - |
| Earth Spirit | Melee | 0.35 | 0.65 | - |
| Queen of Pain | Melee | 0.56 | 0.41 | - |
| Ursa | Melee | 0.3 | 0.3 | - |
| Magnus | Melee | 0.5 | 0.84 | - |
| Riki | Melee | 0.3 | 0.3 | - |
| Visage | Melee | 0.4 | 0.54 | - |
| Elder Titan | Melee | 0.35 | 0.97 | - |
| Anti-Mage | Melee | 0.3 | 0.3 | - |
| Marci | Melee | 0.3 | 0.5 | - |
| Ember Spirit | Melee | 0.4 | 0.3 | - |
| Rubick | Melee | 0.4 | 0.77 | - |
| Mars | Melee | 0.4 | 1.38 | - |
| Void Spirit | Melee | 0.35 | 0.78 | - |
| Arc Warden | Melee | 0.3 | 0.7 | - |
| Warlock | Melee | 0.3 | 0.3 | - |
| Medusa | Melee | 0.5 | 0.6 | - |
| Enchantress | Melee | 0.3 | 0.7 | - |
| Bane | Melee | 0.3 | 0.7 | - |
| Shadow Demon | Melee | 0.35 | 0.5 | - |
| Winter Wyvern | Melee | 0.25 | 0.8 | - |
| Meepo | Melee | 0.38 | 0.6 | - |
| Enigma | Melee | 0.4 | 0.77 | - |
| Shadow Shaman | Melee | 0.3 | 0.5 | - |
| Witch Doctor | Melee | 0.4 | 0.5 | - |
| Faceless Void | Melee | 0.5 | 0.56 | - |
| Batrider | Melee | 0.3 | 0.54 | - |
| Monkey King | Melee | 0.45 | 0.2 | - |
| Silencer | Melee | 0.5 | 0.5 | - |
| Wraith King | Melee | 0.56 | 0.44 | - |
| Bounty Hunter | Melee | 0.59 | 0.59 | - |
| Grimstroke | Melee | 0.35 | 0.85 | - |
| Skywrath Mage | Melee | 0.4 | 0.78 | - |
| Muerta | Melee | 0.35 | 1.1 | - |
| Brewmaster | Melee | 0.35 | 0.65 | - |
| Naga Siren | Melee | 0.5 | 0.5 | - |
| Zeus | Melee | 0.35 | 0.55 | - |
| Gyrocopter | Melee | 0.2 | 0.1 | - |
| Slark | Melee | 0.5 | 0.3 | - |
| Nyx Assassin | Melee | 0.46 | 0.54 | - |
| Hoodwink | Melee | 0.4 | 1.5 | - |
| Snapfire | Melee | 0.35 | 1.23 | - |
| Huskar | Melee | 0.3 | 0.5 | - |
| Ogre Magi | Melee | 0.3 | 0.3 | - |
| Bristleback | Melee | 0.3 | 0.3 | - |
| Sniper | Melee | 0.17 | 0.7 | - |
| Invoker | Melee | 0.4 | 0.7 | - |
| Omniknight | Melee | 0.433 | 0.567 | - |
| Spirit Breaker | Melee | 0.6 | 0.3 | - |
| Broodmother | Melee | 0.4 | 0.5 | - |
| Oracle | Melee | 0.3 | 0.7 | - |
| Techies | Melee | 0.5 | 0.5 | - |
| Centaur Warrunner | Melee | 0.3 | 0.3 | - |
| Outworld Destroyer | Melee | 0.46 | 0.54 | - |
| Chaos Knight | Melee | 0.5 | 0.5 | - |
| Templar Assassin | Melee | 0.3 | 0.5 | - |
| Pangolier | Melee | 0.33 | 0.77 | - |
| Io | Melee | 0.3 | 0.4 | - |
| Clinkz | Melee | 0.4 | 0.3 | - |
| Phantom Assassin | Melee | 0.3 | 0.7 | - |
| Terrorblade | Melee | 0.3 | 0.8 | - |
| Jakiro | Melee | 0.4 | 0.3 | - |
| Crystal Maiden | Melee | 0.45 | 0 | - |
| Phantom Lancer | Melee | 0.5 | 0.5 | - |
| Timbersaw | Melee | 0.36 | 0.64 | - |
| Juggernaut | Melee | 0.33 | 0.84 | - |
| Phoenix | Melee | 0.35 | 0.633 | - |
| Dark Seer | Melee | 0.59 | 0.58 | - |
| Tinker | Melee | 0.35 | 0.65 | - |
| Keeper of the Light | Melee | 0.3 | 0.85 | - |
| Dark Willow | Melee | 0.3 | 1 | - |
| Treant Protector | Melee | 0.6 | 0.4 | - |
| Primal Beast | Melee | 0.6 | 0.7 | - |
| Dawnbreaker | Melee | 0.46 | 1.02 | - |
| Dazzle | Melee | 0.3 | 0.3 | - |
| Kunkka | Melee | 0.4 | 0.3 | - |
| Troll Warlord | Melee | 0.3 | 0.3 | - |
| Death Prophet | Melee | 0.5 | 0.51 | - |
| Legion Commander | Melee | 0.46 | 0.64 | - |
| Disruptor | Melee | 0.4 | 0.5 | - |
| Tusk | Melee | 0.36 | 0.64 | - |
| Lifestealer | Melee | 0.39 | 0.44 | - |
| Underlord | Melee | 0.45 | 0.7 | - |
| Lone Druid | Melee | 0.33 | 0.53 | - |
| Kez | Melee | 0.35 | 1.12 | - |
| Largo | Melee | 0.35 | 0.95 | - |
| Spirit Bear | Melee | 0.43 | 0.4 | - |

[corpus:liquipedia_dota2/attack_animation@2383432#Attack_Animations_of_Heroes]

## Attack Animation of Other Units

| Unit | Attack Range | Attack Point | Attack Backswing | Projectile Speed |
|---|---:|---:|---:|---:|
| Ranged Creep | b4500 | 0.5 | 0.3 | 900 |
| Melee Creep, Treant | a1Melee | 0.467 | 0.533 | - |
| Siege Creep | b7690 | 0.7 | 1.3 | 1100 |
| Tower | b8700 | 0.6 | 0.4 | 750 |
| Fountain | b91200 | 0 | 0 | 1400 |
| Kobold, Kobold Soldier | a1Melee | 0.38 | 0.6 | - |
| Kobold Foreman | a2Melee | 0.38 | 0.6 | - |
| Centaur Courser, Mud Golem, Spiderling, Spiderite | a1Melee | 0.5 | 0.3 | - |
| Centaur Conqueror, Hellbear, Hellbear Smasher Ogre Bruiser, Ogre Frostmage, Satyr Mindstealer, Satyr Tormenter, Ancient Rock Golem | a1Melee | 0.3 | 0.3 | - |
| Fell Spirit | a1Melee | 0.4 | 0.3 | - |
| Ghost | b1300 | 0.3 | 0.3 | 900 |
| Giant Wolf, Alpha Wolf, Lycan Wolf | a0Melee | 0.33 | 0.64 | - |
| Wildwing, Wildwing Ripper, Roshan, Earth, Fire, Undying Zombie | a3Melee | 0.3 | 0.3 | - |
| Satyr Banisher | b1300 | 0.3 | 0.3 | 1500 |
| Ancient Granite Golem | a3Melee | 0.3 | 0.5 | - |
| Ancient Thunderhide, Ancient Rumblehide | b1300 | 0.5 | 0.56 | 1500 |
| Vhoul Assassin | b4500 | 0.4 | 0.3 | 1500 |
| Hill Troll, Dark Troll Summoner, Hill Troll Berserker | b4500 | 0.3 | 0.3 | 1200 |
| Hill Troll Priest | b6600 | 0.3 | 0.3 | 900 |
| Harpy Scout | b1300 | 0.3 | 0.3 | 1200 |
| Harpy Stormcrafter | b3450 | 0.3 | 0.3 | 1200 |
| Ancient Black Drake | b1300 | 0.94 | 0.56 | 900 |
| Ancient Black Dragon | b1300 | 0.94 | 0.56 | 1500 |
| Skeleton Warrior | a0Melee | 0.56 | 0.44 | - |
| Wraith King Skeleton | a0Melee | 0.56 | 0.64 | - |
| Necronomicon Warrior | a1Melee | 0.56 | 0.44 | - |
| Necronomicon Archer | b2350/450/550 | 0.7 | 0.3 | 900 |
| Death Ward | b8700 | 0 | 0 | 1000 |
| Serpent Ward | b6600 | 0.3 | 0.4 | 900 |
| Plague Ward | b6600 | 0.3 | 0.7 | 1900 |
| Eidolon | b3450 | 0.4 | 0.77 | 900 |
| Forged Spirit | b1300/365/430/495/560/625/690 | 0.2 | 0.4 | 1000 |
| Warlock Golem | a4Melee | 0.26 | 0.74 | - |
| Razorback | b5550 | 0.633 | 0.337 | 1500 |
| Storm | b6600 | 0.4 | 0.77 | 1200 |
| Spirit Bear | a3Melee | 0.43 | 0.67 | - |
| Familiar | b0160 | 0.33 | 0.2 | 900 |

[corpus:liquipedia_dota2/attack_animation@2383432#Attack_Animation_of_Other_Units]

## Version History

| Version | Date | Description |
|---|---|---|
| 7.28 | 2020-12-17 | The following abilities now increase the hero’s attack-animation speed: Vendetta; Blink Strike; Walrus PUNCH! |
| 7.28 | 2020-12-17 | Created Quicksilver Amulet. |
| 6.00 | 2026-07-25 | Updated all attack animations so they more fully match the hero models. |

[corpus:liquipedia_dota2/attack_animation@2383432#Version_History]

## Patch History

| Patch | Description |
|---|---|
| 24 Mar 2016 | Fixed various attack-animation prediction exploits, such as Coup de Grace. |

[corpus:liquipedia_dota2/attack_animation@2383432#Patch_History]