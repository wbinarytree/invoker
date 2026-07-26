---
title: Vision
kind: concept
patch: 7.41d
card:
  entity: vision
  sentences:
  - text: Vision is a team-shared circular visibility system in which all heroes except
      listed exceptions have 1800 daytime and 800 nighttime vision; Fog of War hides
      enemies outside allied vision, and True Sight reveals otherwise unseen invisible
      units.
    marks:
    - corpus:liquipedia_dota2/vision@2383431
    - corpus:liquipedia_dota2/vision@2383431#Heroes
  - text: 'There are 2 vision types: ground vision is obstructed by higher elevations,
      trees, and vision blockers, while flying vision is unhindered under the general
      rules.'
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Types_of_Vision
  - text: Non-friendly units inside Fog of War cannot be seen or directly targeted,
      but non-targeted spells can still hit them.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Fog_of_War
  - text: An ability cast is canceled if its enemy enters the fog during cast time;
      an attack is not canceled if its target enters during the attack animation.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Fog_of_War
  - text: Most units have greater daytime and shorter nighttime vision, although some
      reverse this relationship or have identical values.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Time_of_Day
  - text: Observer Wards have 360 day and night vision, while Sentry Wards have 0.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Wards
  - text: A unit’s maximum vision range is 4000.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Vision_Increasing_Sources
  - text: Except for Charge of Darkness and Track during Shadow Walk, a unit-target
      spell on an enemy within 1800 range, or an attack against that enemy, grants
      it 150-radius ground vision around the caster or attacker for 2 seconds.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Caster_Vision
  - text: Roshan’s pit blockers prevent vision both into and out of the pit, including
      flying vision.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Roshan_Pit
  - text: Exposure makes an enemy visible and targetable through Fog of War without
      revealing its surroundings.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Exposing
  - text: Unit-targeted spells generally require vision of their targets, while ground-targeted
      and non-targeted spells generally do not.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Vision_interaction_with_spells
  - text: Once cast, spells usually function regardless of vision, and area effects
      usually affect enemies without vision.
    marks:
    - corpus:liquipedia_dota2/vision@2383431#Vision_interaction_with_spells
---

# Vision

Vision determines what a unit can and cannot see within a circular area based on its current location and state. Unseen places are covered by the Fog of War, which hides enemy but not allied units. Invisible units remain unseen outside the fog unless revealed by True Sight. Ground vision is blocked by trees and higher elevation; flying vision is unobstructed by them. Abilities may grant temporary vision limited to an area of effect. [corpus:liquipedia_dota2/vision@2383431]

Vision is shared across a team: players see everything visible to allied player-controlled units and allied NPCs, including lane creeps and buildings. [corpus:liquipedia_dota2/vision@2383431]

## Fog of War

Areas outside friendly vision are constantly covered by the Fog of War. Non-friendly units inside it cannot be seen or directly targeted, but non-targeted spells can still hit them. An allied unit must gain vision over the area to reveal them. If an enemy enters the fog during an ability’s cast time, the cast is canceled; attacks are not canceled when their target enters the fog during the attack animation. [corpus:liquipedia_dota2/vision@2383431#Fog_of_War]

### Elevation

Units with ground vision cannot see areas at higher elevations. Thus, a unit in the river cannot see past the surrounding cliffs or beyond ramps leading out of it. Units on higher elevation effectively have unobstructed vision over lower elevation; a unit on an elevated ward spot can see the entire surrounding area without nearby trees obstructing it, regardless of vision type. Flying vision is not obstructed by higher elevations. [corpus:liquipedia_dota2/vision@2383431#Elevation]

### Trees

Trees block pathing and obstruct vision for units on the same elevation and units one elevation above them. Their obstruction behaves like a shadow: the closer a unit is to a tree, the larger and wider the blocked section of its circular vision area. The exact numbers are unknown. [corpus:liquipedia_dota2/vision@2383431#Trees]

Trees created by Iron Branch, Ironwood Tree, Woodland Striders, and Sprout have narrower vision blockers than regular map trees. Flying vision is not obstructed by trees. [corpus:liquipedia_dota2/vision@2383431#Trees]

### Artificial vision blockers

Artificial vision blockers supplement normal visibility rules at certain locations. Flying vision is generally unaffected by them. [corpus:liquipedia_dota2/vision@2383431#Vision_Blockers]

| Source | Effect |
|---|---|
| Drow Ranger — Glacier | Creates an ice hill beneath Drow Ranger. Its front obscures enemy vision, while allied heroes on top receive flying vision. |

[corpus:liquipedia_dota2/vision@2383431#Vision_Blockers]

#### Fountain entrances

Each fountain has a vision blocker at its stairs that prevents enemies of the fountain’s team from seeing the fountain area from outside. Although the fountain’s higher elevation normally provides this protection, the blocker also prevents vision from nearby high ground, such as the Radiant fountain ward cliff. [corpus:liquipedia_dota2/vision@2383431#Fountain_Entrances]

#### Roshan’s pit

Roshan’s pit is sealed by blockers that prevent vision both into and out of the pit, including vision from units with flying vision. Green tiles can see into the pit but cannot be seen from inside; red tiles can see out but cannot be seen from outside. [corpus:liquipedia_dota2/vision@2383431#Roshan_Pit]

The entrance contains asymmetric “phantom spots.” Units there can either see into the pit while remaining unseen from inside, or see out while remaining unseen from outside. These spots can support juking, scouting Roshan attempts, and hiding wards, especially Psionic Traps. With ground vision, a unit on a phantom spot can be seen only by standing within 3 tiles in rectilinear distance. [corpus:liquipedia_dota2/vision@2383431#Roshan_Pit]

Phantom spots are not marked in-game. A subtle brightening of a small area of ground indicates direct vision of some phantom-spot tiles and implies that the observer is also in a phantom spot. The right side of the entrance contains the largest continuous phantom spot and is the most forgiving location. [corpus:liquipedia_dota2/vision@2383431#Roshan_Pit]

## Time of day

Time of day affects vision. Most units have greater daytime vision and shorter nighttime vision. Some instead have shorter day vision and longer night vision, while others have identical vision at both times. [corpus:liquipedia_dota2/vision@2383431#Time_of_Day]

## Base vision ranges

Most units have day and night vision; very few have no vision. Vision bonuses and reductions can alter these values. [corpus:liquipedia_dota2/vision@2383431#Base_Vision_Ranges]

### Heroes

All heroes have 1800 daytime and 800 nighttime vision except for the listed value pairs below; the corresponding unit names are not stated. [corpus:liquipedia_dota2/vision@2383431#Heroes]

| Unit | Day | Night |
|---|---:|---:|
| — | 800 | 1800 |
| — | 1800 | 1200 |
| — | 1800 | 1200 |
| — | 1800 | 1000 |
| — | 1800 | 1000 |
| — | 1800 | 1800 |
| — | 1800 | 1400 |

[corpus:liquipedia_dota2/vision@2383431#Heroes]

### Lane creeps

All lane creeps have 750 day and night vision, except for an unstated exception list. [corpus:liquipedia_dota2/vision@2383431#Lane_Creeps]

### Neutral creeps

All neutral creeps have 800 day and night vision except the following. [corpus:liquipedia_dota2/vision@2383431#Neutral_Creeps]

| Unit | Day | Night |
|---|---:|---:|
| Tormentor | 1400 | 1400 |
| Ancient Ice Shaman | 1400 | 800 |
| Pollywog | 400 | 400 |
| Kobold | 1400 | 800 |
| Hill Troll Priest | 1400 | 800 |
| Vhoul Assassin | 400 | 400 |
| Harpy Scout | 1200 | 800 |
| Harpy Stormcrafter | 1800 | 1800 |
| Ancient Rumblehide | 1400 | 800 |
| Ancient Thunderhide | 1400 | 800 |
| Roshan | 1400 | 1400 |

[corpus:liquipedia_dota2/vision@2383431#Neutral_Creeps]

### Summoned creeps

All summoned creeps have 800 day and night vision except the following. [corpus:liquipedia_dota2/vision@2383431#Summoned_Creeps]

| Unit | Day | Night |
|---|---:|---:|
| Demonic Archer | 1500 | 800 |
| Demonic Warrior | 1500 | 800 |
| Zealot | 750 | 750 |
| Raptor | 600/650/700/750 | 600/650/700/750 |
| Razorback | 1400 | 800 |
| Treant | 500 | 500 |
| Spiderling | 400 | 400 |
| Eidolon | 1200 | 800 |
| Forged Spirit | 1200 | 800 |
| Lycan Wolf | 1200 | 800 |

[corpus:liquipedia_dota2/vision@2383431#Summoned_Creeps]

### Creep-heroes

| Unit | Day | Night |
|---|---:|---:|
| Warlock Golem | 1800 | 1800 |
| Earth | 1800 | 800 |
| Astral Spirit | 350 | 350 |
| Storm | 1800 | 800 |
| Fire | 1800 | 800 |
| Familiar | 400 | 400 |

[corpus:liquipedia_dota2/vision@2383431#Creep-Heroes]

### Couriers

| Unit | Day | Night |
|---|---:|---:|
| Courier | 200 | 200 |

[corpus:liquipedia_dota2/vision@2383431#Couriers]

### Wards and related units

| Unit | Day | Night |
|---|---:|---:|
| Proximity Mine | 64 | 64 |
| Ice Spire | 800 | 800 |
| Phoenix Sun | 1800 | 800 |
| Tornado | 300 | 300 |
| Sticky Bomb | 700 | 700 |
| Power Cog | 1600 | 600 |
| Jex | 600 | 600 |
| Fiend’s Gate | 500 | 500 |
| Skeleton Archer | 800 | 800 |
| Roshan’s Banner | 1200 | 1200 |
| Ofrenda | 0 | 0 |
| Wheel Decoy | 1800 | 800 |
| Observer Ward | 360 | 360 |
| Sentry Ward | 0 | 0 |
| Minefield Sign | 0 | 0 |
| M.A.D. | 400 | 400 |
| Keen Cannon | 700 | 700 |
| Anchor | 0 | 0 |
| Tombstone | 1200 | 1200 |
| Plague Ward | 800 | 800 |

[corpus:liquipedia_dota2/vision@2383431#Wards]

### Attached units

| Unit | Day | Night |
|---|---:|---:|
| Treant’s Eyes | 800 | 800 |
| Beetle | 321 | 321 |
| Phantom | 200 | 200 |

[corpus:liquipedia_dota2/vision@2383431#Attached]

### Buildings

| Building | Day | Night | True Sight | Attack Range |
|---|---:|---:|---|---|
| Outpost | 500 | 500 |  |  |
| Watcher | 800 | 450 |  |  |
| Ancient | 2600 | 2600 |  |  |
| Effigy Building | 900 | 600 |  |  |
| Tower (Tier 1) | 1900 | 600 |  |  |
| Tower (Tier 2) | 1900 | 1100 |  |  |
| Tower (Tier 3) | 1900 | 1100 |  |  |
| Tower (Tier 4) | 1900 | 1100 |  |  |
| Twin Gate | 500 | 500 |  |  |
| Lotus Pool | 500 | 500 |  |  |
| Shrine of Wisdom | 0 | 0 |  |  |
| Fountain | 1800 | 1800 |  |  |
| Melee Barracks | 900 | 600 |  |  |
| Ranged Barracks | 900 | 600 |  |  |

[corpus:liquipedia_dota2/vision@2383431#Buildings]

## Types of vision

There are 2 vision types: ground vision, also called obstructed vision, and flying vision, also called unobstructed vision. Ground vision is impaired by higher elevations, trees, and vision blockers, while flying vision is completely unhindered under the general rules. Every hero has ground vision. [corpus:liquipedia_dota2/vision@2383431#Types_of_Vision]

| Vision type | Other units |
|---|---|
| Ground | Warlock Golem, Earth, Astral Spirit, Proximity Mine, Outpost, Ice Spire, Siege Creep, Undying Zombie, Phoenix Sun, Ghost, Warpine Raider, Sticky Bomb, Power Cog, Storm, Jex, Fiend’s Gate, Watcher, Skeleton Archer, Roshan’s Banner, Ofrenda, Minor Imp, Ancient, Effigy Building, Tower (Tier 1), Tower (Tier 2), Tower (Tier 3), Tower (Tier 4), Twin Gate, Lotus Pool, Wheel Decoy, Tormentor, Ancient Frostbitten Golem, Ancient Ice Shaman, Super Melee Creep, Mega Melee Creep, Super Ranged Creep, Mega Ranged Creep, Super Siege Creep, Mega Siege Creep, Flagbearer Creep, Super Flagbearer Creep, Mega Flagbearer Creep, Observer Ward, Sentry Ward, Pollywog, Boglet, Croaker, Ancient Croaker, Marshmage Apprentice, Marshmage, Ancient Marshmage, Shrine of Wisdom, Demonic Archer, Demonic Warrior, Minefield Sign, Zealot, Keen Cannon, Fire, Tempest Double, Melee Creep, Ranged Creep, Kobold, Kobold Soldier, Kobold Foreman, Hill Troll Berserker, Hill Troll Priest, Vhoul Assassin, Fell Spirit, Harpy Scout, Harpy Stormcrafter, Centaur Courser, Centaur Conqueror, Giant Wolf, Alpha Wolf, Satyr Banisher, Satyr Mindstealer, Ogre Bruiser, Ogre Frostmage, Mud Golem, Satyr Tormenter, Hellbear, Hellbear Smasher, Wildwing, Wildwing Ripper, Hill Troll, Dark Troll Summoner, Skeleton Warrior, Ancient Black Drake, Ancient Black Dragon, Ancient Rock Golem, Ancient Granite Golem, Ancient Rumblehide, Ancient Thunderhide, Shard Golem, Roshan, Fountain, Razorback, Anchor, Treant, Tombstone, Spiderling, Melee Barracks, Ranged Barracks, Eidolon, Plague Ward, Ancient Prowler Acolyte, Ancient Prowler Shaman, Nimbus, Courier, Wraith King Skeleton, Nether Ward, Death Ward, Psionic Trap, Healing Ward, Forged Spirit, Serpent Ward, Lycan Wolf, Homing Missile, Phantom, Spin Web, Ignis Fatuus |
| Flying | Tornado, Treant’s Eyes, M.A.D., Raptor, Beetle, Familiar |

[corpus:liquipedia_dota2/vision@2383431#Types_of_Vision]

## Modifying vision

Several abilities and items grant or reduce vision. Unless stated otherwise, most vision bonuses stack additively. [corpus:liquipedia_dota2/vision@2383431#Modifying_Vision]

### Vision increases

A unit’s maximum vision range is 4000. [corpus:liquipedia_dota2/vision@2383431#Vision_Increasing_Sources]

| Vision-increasing ability or item effect |
|---|
| Lycan — Shapeshift |
| Lycan — Wolf Bite |
| Luna — Lunar Blessing |
| Moon Shard — Consume |
| Moon Shard — Shade Sight |

[corpus:liquipedia_dota2/vision@2383431#Vision_Increasing_Sources]

### Setting vision

The following abilities set vision to specific values. [corpus:liquipedia_dota2/vision@2383431#Setting_Vision]

| Source | Set value | Rules |
|---|---|---|
| Bane — Nightmare | Set Vision Range: 200 | Sets the affected unit’s vision for its sleep duration. It takes priority over every other vision-changing effect except Shade Sight. |
| Bristleback — unnamed ability | Set Vision Radius: | Sets the affected unit’s vision radius for its rage duration. |
| Hoodwink — Bushwhack | Set Vision Range: 0 | Sets the affected unit’s vision for its stun duration. |
| Hoodwink — Decoy | — | Once triggered, its set vision values are based on Bushwhack. |
| Monkey King — Tree Dance | Day Vision: 700; Night Vision: 500 | Affects the caster until unperched. It takes priority over every other vision-changing effect except Shade Sight. |

[corpus:liquipedia_dota2/vision@2383431#Setting_Vision]

### Talents

The passive Vision talent affects the hero and grants 200 bonus day and night vision. It does not counter vision-reducing effects. Its modifier is hidden. [corpus:liquipedia_dota2/vision@2383431#Talents]

The passive Day Vision talent affects the hero and grants 400 bonus day vision. It does not counter vision-reducing effects. Its modifier is hidden. [corpus:liquipedia_dota2/vision@2383431#Day_Vision_Talents]

The passive Night Vision talent affects the hero and grants a varying night-vision bonus. Existing values are 400/500/600/800/1000, including a listed +500 talent. It does not counter vision-reducing effects, and its modifier is hidden. [corpus:liquipedia_dota2/vision@2383431#Night_Vision_Talents]

## Sources of vision

Units are not the only vision sources. Many abilities create fixed-duration vision cells of varying sizes on the world. [corpus:liquipedia_dota2/vision@2383431#Sources_of_Vision]

### Caster vision

Caster vision is a flying vision cell granted to victims of targeted spells and attacks. When a unit casts a unit-target spell—except Charge of Darkness and Track during Shadow Walk—on an enemy within 1800 range, or attacks that enemy, the enemy receives 150-radius ground vision around the caster or attacker for 2 seconds. This limits repeated harassment from the Fog of War, including long-distance spells such as Arcane Bolt and ranged attacks. [corpus:liquipedia_dota2/vision@2383431#Caster_Vision]

Only one caster-vision cell can exist per unit. A new targeted order during the existing cell’s duration does not create another cell; it updates the old cell’s location, resets its duration, and changes its type to flying vision. Unit-targeted abilities blocked by Spell Block provide caster vision, while ground-targeted abilities blocked by Spell Block do not. [corpus:liquipedia_dota2/vision@2383431#Caster_Vision]

| Listed ability |
|---|
| Boulder Smash |
| Wrath of Nature |
| Lightning Bolt |
| Eternal Chains |

[corpus:liquipedia_dota2/vision@2383431#Caster_Vision]

### Ground-vision sources

Ground vision is obstructed by trees, higher elevations, and vision blockers. [corpus:liquipedia_dota2/vision@2383431#Ground_Vision]

| Source | Vision | Behavior |
|---|---|---|
| Aegis of the Immortal — Reincarnation | Day: 1800; Night: 800 | Around the hero upon triggering; lingers for 5 seconds. |
| Ancient Black Dragon — Fireball | 85 | Within the target area; lingers for seconds. |
| Arc Warden — Spark Wraith | 300 | Around the stationary wraith starting on cast; lingers for 1+16 seconds. Triggering the wraith removes it. |
| Bane — Fiend’s Grip | 400 | At the target unit’s initial position. Duration follows channel time after reductions and amplifications and always lasts fully if canceled. |
| Bloodseeker — Blood Rite | 600 | Within the area; lingers for 5 seconds. |
| Crystal Maiden — Crystal Nova | 900 | At the target area; lingers for 6 seconds. |
| Disruptor — Kinetic Field | 70 | Ground radius within the target area; lingers for 5 seconds. |
| Enigma — Black Hole | 800 | At the target area; lingers for 4 seconds. |
| Kunkka — Torrent | 400 | At the target area; lingers for 2.9 seconds. |
| Kunkka — X Marks the Spot | 400 | Around the ground mark; lingers for 5.94 seconds. |
| Luna — Eclipse | 6/9/12 | Within the target area when ground-cast; lingers for 2.4/4.2/6 seconds. |
| Manta Style — Mirror Image | 1000 | Around the caster upon cast; lingers for 0.1 seconds. |
| Monkey King — Primal Spring | 1.75 | Within the target area. Duration is the channel time plus distance-based travel time and always lasts fully if canceled. |
| Phantom Lancer — Doppelganger | 1 | Within the illusion gather area; lingers for 2 second. |
| Phoenix — Launch Fire Spirit | 20/40/60/80 | Within the affected area on impact; lingers for 1 second. |
| Riki — Tricks of the Trade | 2 | Within the attack radius. Duration follows channel time and always lasts fully if canceled. |
| Spectre — Spectral Dagger | 200 | Around the shadow trail and hit enemy heroes; lingers for seconds. |
| Techies — Proximity Mines | 400 | Around itself upon exploding; lingers for 1 second. |
| Tidehunter — Gush | 0 ( 200) | Requires Aghanim’s Scepter. At each hit enemy’s location; lingers for 2 seconds. |
| Undying — Reincarnation | 1800 | Around the hero upon triggering; lingers for 5 seconds. This is an old ability. |
| Wraith King — Reincarnation | Day: 1800; Night: 800 | Around the hero upon triggering; lingers for 3 seconds. |
| Clockwerk — Hookshot | 200; 400 at maximum distance | Non-lingering around the hook tip during travel and retraction; grants 400-radius vision at maximum distance if it does not latch. |
| Elder Titan — Astral Spirit | 400 | Non-lingering around the spirit until it returns or dies. |
| Timbersaw — Timber Chain | 100 | Non-lingering around the hook tip while it travels. |

[corpus:liquipedia_dota2/vision@2383431#Ground_Vision]

### Flying-vision sources

Flying vision is not obstructed by trees, higher elevations, or vision blockers under the general rules. [corpus:liquipedia_dota2/vision@2383431#Flying_Vision]

| Source | Vision | Behavior |
|---|---|---|
| Ancient Apparition — Ice Vortex | 200 | At the target area; lingers for 16%/19%/22%/25% seconds. |
| Ancient Apparition — Ice Blast | 500 | Around both projectiles. Tracer vision does not linger; ice-ball vision lingers for 3.5 seconds. |
| Ancient Apparition — Release | 750 | At the marked area upon cast; lingers for 5.3 seconds. |
| Batrider — Sticky Napalm | 500 | At the targeted area; lingers for 2 seconds. |
| Chaos Knight — Phantasm | 400 | Around the caster upon cast; lingers for 0.5 seconds. |
| Clockwerk — Rocket Flare | 600 | Around the traveling rocket; lingers for 10 seconds. |
| Disruptor — Thunder Strike | 450 | At the target’s location on the final strike; lingers for 3 seconds. |
| Disruptor — Static Storm | 450 | At the target area; lingers for 6 ( ) seconds. |
| Elder Titan — Earth Splitter | 500 | Spawns 12 cells along the crack at 0.22-second intervals and 200 distance between cells; lingers for 4 seconds. |
| Faceless Void — Chronosphere | 475 | At the target area; lasts 0.1 seconds. |
| Gyrocopter — Call Down | 350 | At the target area upon cast; lingers for 4 seconds. |
| Invoker — Sun Strike | 400 | At the target area upon cast; lingers for 179 seconds. |
| Io — Spirits | 350 | Around a hit enemy hero on impact; lingers for 3 seconds. |
| Io — Relocate | 150 | At the targeted point upon cast; lingers for 2.7 seconds. |
| Jakiro — Ice Path | 150 | Along the entire path; lingers for 3 seconds. |
| Juggernaut — Omnislash | 300 | Around the caster on every slash; lingers for 1 second. |
| Keeper of the Light — Illuminate | 375 | Spawns cells in a line before the caster at 0.5-second intervals and 150 distance between cells until channeling ends; lingers for 10.34 seconds. |
| Kez — Raven’s Veil | 775 | Around the activation point; lingers for 3 seconds. |
| Mars — Arena of Blood | 100 | Within the target area upon cast; lasts 6 seconds. |
| Naga Siren — Mirror Image | 450 | Around the caster upon cast; lingers for 0.5 seconds. |
| Nature’s Prophet — Sprout | 500 | At the target area upon cast; lingers for 8 seconds. |
| Night Stalker — Dark Ascension | 1800 | Around the hero; active for for 1 seconds. |
| Puck — Illusory Orb | 450 | Around the traveling orb; lingers for 3.34 ( 10.02) seconds. |
| Pudge — Meat Hook | 400 | Around the latched unit upon latching; lingers for 4 seconds. |
| Razor — Plasma Field | 800 | Around the caster for the entire duration; lingers for 2 seconds. |
| Sniper — Shrapnel | 1.2 | Within the target area after the effect delay; lingers for seconds. |
| Timbersaw — Chakram | 2000 | Around the sawblade after it reaches the target, until it begins returning. |
| Timbersaw — Second Chakram |  | Around the sawblade after it reaches the target, until it begins returning. |
| Vengeful Spirit — Wave of Terror | 300 | Around the traveling wave; lingers for 4 seconds. |
| Zeus — Lightning Bolt | 750 | Around the target point or enemy; lingers for 4.5 seconds. |
| Zeus — Thundergod’s Wrath | 500 | Around each hit enemy hero; lingers for 3 seconds. |
| Sentry Ward — Plant | 150 | Around the ward upon cast; lingers for 12 seconds. |
| Town Portal Scroll — Teleport | 200 | At the destination from channel begin. Duration follows channel time and always lasts fully if canceled. |
| Meteor Hammer — Meteor Hammer | 400 | Within the target area upon cast; lingers for 2.8 seconds. |
| Shiva’s Guard — Arctic Blast | 800 | Around the caster for the entire duration; lingers for 2 seconds. |
| Arc Warden — Spark Wraith | 300 | Non-lingering around the traveling wraith, then at the target on impact for 3.34 seconds. |
| Disruptor — Glimpse | 400 | Non-lingering around the projectile, then at the target’s location after teleporting back for 3.34 seconds. |
| Grimstroke — Stroke of Fate | 120/250 | 120 non-lingering vision around the traveling trail; 250 at the end location for 2 seconds. |
| Gyrocopter — Homing Missile | 400 | Non-lingering around the missile, then at the target on impact for 4 seconds. |
| Invoker — Tornado | 200 | Non-lingering around the tornado, then at maximum distance for 1.75 seconds. |
| Invoker — Chaos Meteor | 500 | Non-lingering around the rolling meteor, then at maximum distance for 3 seconds. |
| Mars — Spear of Mars | 300 | Non-lingering around the spear, then at maximum distance or an impaled enemy. Lingers for 1 second if not impaled, or 1.3/1.6/1.9/2.2 ( ) seconds if impaled. |
| Mirana — Sacred Arrow | 500 | Non-lingering around the arrow, then at maximum distance or a hit enemy for 3.5 seconds. |
| Oracle — Fortune’s End | 200 | Non-lingering around the orb, then at the target on impact for 2 seconds. |
| Phantom Assassin — Stifling Dagger | 450 | Non-lingering around the dagger, then at the target on impact for 3.34 seconds. |
| Shadow Demon — Shadow Poison | Path: 350; Hit/End: 300 | Non-lingering around the cloud; vision around each hit enemy and at maximum distance lingers for 3.5 seconds. |
| Skywrath Mage — Arcane Bolt | 325 | Non-lingering around the bolt, then at the target on impact for 3.34 seconds. |
| Skywrath Mage — Concussive Shot | 300 | Non-lingering around the shot, then at the target on impact for 3.34 seconds. |
| Snapfire — Mortimer Kisses | 500 | Non-lingering around the lava blobs, then at the marked location on impact for 3.5 seconds. |
| Tiny — Tree Throw | 100 | Non-lingering around the tree if ground-targeted; none while traveling if unit-targeted. Grants the same vision at impact regardless of targeting and lingers for 2 seconds. |
| Tiny — Tree Volley | Tree: 2.5; Impact: 100 | Non-lingering around traveling trees; vision at each hit enemy on impact lingers for 2 seconds. |
| Tusk — Ice Shards | Projectile: 200; Shards: 100 | Non-lingering around the projectile; vision around each created shard lingers for 2 seconds. |
| Venomancer — Venomous Gale | 350 | Non-lingering around the traveling gale. |
| Windranger — Powershot | 400 | Non-lingering around the arrow, then at maximum distance for 3.34 seconds. |
| Batrider — Flamebreak | 300 | Non-lingering around the traveling explosive cocktail. |
| Beastmaster — Wild Axes | 350 | Non-lingering around the traveling axes. |
| Drow Ranger — Multishot | 100 | Non-lingering around the traveling arrows. |
| Kunkka — Ghostship | 400 | Non-lingering around the traveling ships. |
| Lich — Chain Frost | 800 | Non-lingering around the traveling ice ball. |
| Medusa — Mystic Snake | 300 | Non-lingering around the traveling snake. |
| Meepo — Earthbind | 300 | Non-lingering around the traveling net. |
| Sven — Storm Hammer | 225 | Non-lingering around the traveling fist. |
| Storm Spirit — Ball Lightning | 400 | Non-lingering around the traveling ball of lightning. |
| Void Spirit — Aether Remnant | Travel: 150; Stationary: 200 | Non-lingering around the traveling remnant. After the delay, spawns 2 cells ahead: one at maximum distance and one halfway through it. They last while the remnant exists; if triggered, vision ends when pulling ends. |
| Weaver — The Swarm | 321 | Non-lingering around each individual beetle while the swarm travels. |

[corpus:liquipedia_dota2/vision@2383431#Flying_Vision]

### Shared vision

Some abilities share an enemy’s vision with the player’s team, allowing opponents to see everything that unit sees. [corpus:liquipedia_dota2/vision@2383431#Shared_Vision]

| Shared vision with True Sight |
|---|
| Bounty Hunter — Track¹ |
| Essence Distiller — Soul Release |
| Meepo — Earthbind |
| Medusa — Gorgon’s Grasp |
| Sniper — Assassinate⁴ |

| Shared vision without True Sight |
|---|
| Grimstroke — Soulbind |
| Razor — Static Link |
| Silencer — Last Word |
| Spectre — Spectral Dagger⁵ |
| Spirit Breaker — Charge of Darkness⁶ |

[corpus:liquipedia_dota2/vision@2383431#Shared_Vision]

Grimstroke’s Phantom’s Embrace is a unique case: it dies instantly if the unit to which it is attached is invisible. Track¹ requires a talent. Assassinate⁴ shares vision from cast begin until the cast is canceled or a hit succeeds, but for no longer than 4 seconds; it does not share vision when targeting an invulnerable unit. Spectral Dagger⁵ shares the vision of all hit enemy heroes while they continue creating a shadow path. Charge of Darkness⁶ shares its target’s vision until the charge stops by reaching the target or being canceled early. [corpus:liquipedia_dota2/vision@2383431#Shared_Vision]

## Exposing

Exposure reveals and makes an enemy model targetable through the Fog of War without providing vision of its surroundings. Abilities treat exposed enemies as visible units. Unlike area-based vision such as an Observer Ward’s, exposure is attached to the unit. [corpus:liquipedia_dota2/vision@2383431#Exposing]

Exposure does not cancel invisibility, though it usually reveals a silhouette. An invisible enemy revealed only as a silhouette cannot be attacked or targeted by single-target abilities and still counts as invisible for ability interactions, with very few exceptions. The silhouette can nevertheless be clicked to inspect the unit. Some exposure sources also provide True Sight. [corpus:liquipedia_dota2/vision@2383431#Exposing]

Debuff Immunity does not protect against Expose or True Sight except for Curse of the Oldgrowth. Debuff Immunity may be paired with a Dispel that removes Expose or True Sight when it is tied to a dispellable debuff. Shared vision includes exposure by default, so every shared-vision ability also exposes enemies. [corpus:liquipedia_dota2/vision@2383431#Exposing]

| Exposure without True Sight |
|---|
| Dark Willow — Terrorize |
| Disruptor — Thunder Strike |
| Grimstroke — Ink Trail |
| Tusk — Snowball |

| Exposure with True Sight |
|---|
| Bloodseeker — Thirst |
| Bane — Fiend’s Grip |
| Bounty Hunter — Track |
| Broodmother — Spinner’s Snare⁴ |
| Faceless Void — Chronosphere |
| Gem of True Sight — Reveal |
| Primal Beast — Pulverize |
| Pugna — Life Drain |
| Slardar — Corrosive Haze |
| Tidehunter — Dead in the Water |

[corpus:liquipedia_dota2/vision@2383431#Exposing]

| Special case | Rules |
|---|---|
| Hoodwink — Bushwhack | Cannot bind invisible or debuff-immune units. If a bound unit becomes invisible or debuff immune, its silhouette is revealed. |
| Nature’s Prophet — Curse of the Oldgrowth | The debuff cannot be applied to an invisible hero. Exposure is disabled while the hero is debuff immune. If the hero becomes invisible, its silhouette is not revealed. |
| Spirit Breaker — Nether Strike | Cannot target or expose an invisible unit. Unlike other cases, it exposes during cast time. If the unit becomes invisible, its silhouette is not revealed. |
| Troll Warlord — Battle Trance | Cannot target or expose an invisible unit. If the unit becomes invisible, its silhouette is not revealed. |

[corpus:liquipedia_dota2/vision@2383431#Exposing]

The section’s conditions are: ¹ requires a talent; 2a requires Aghanim’s Scepter; 2b requires Aghanim’s Shard; 3 requires the selected facet; and Spinner’s Snare⁴ does not trigger on a debuff-immune hero, but becoming debuff immune does not protect an already-bound enemy from exposure. [corpus:liquipedia_dota2/vision@2383431#Exposing]

## Vision interaction with spells

Unit-targeted spells generally require vision of their targets, while ground-targeted and non-targeted spells may generally be cast without it. Once cast, spells usually function regardless of vision, and area effects usually do not need vision to affect enemies. Some non-targeted spells that select their own targets require vision. All these rules have exceptions. [corpus:liquipedia_dota2/vision@2383431#Vision_interaction_with_spells]

| Spells that require vision to affect enemies |
|---|
| Abaddon — Aphotic Shield area damage |
| Bristleback — Area Viscous Nasal Goo²ᵃ |
| Dark Willow — Bedlam attacks |
| Dazzle — Poison Touch secondary projectiles |
| Drow Ranger — Marksmanship splinters²ᵃ |
| Ember Spirit — Searing Chains |
| Gyrocopter — Rocket Barrage |
| Gyrocopter — Homing Missile⁴ |
| Gyrocopter — Flak Cannon |
| Gyrocopter — Side Gunner |
| Harpy Stormcrafter — Chain Lightning |
| Juggernaut — Omnislash |
| Leshrac — Lightning Storm |
| Leshrac — Pulse Nova’s Lightning Storms²ᵃ |
| Lich — Frost Shield area damage |
| Lion — Mana Drain²ᵃ ⁵ |
| Luna — Moon Glaives |
| Luna — Eclipse |
| Maelstrom — Chain Lightning |
| Medusa — Split Shot |
| Mirana — Starstorm⁶ |
| Mjollnir — Chain Lightning |
| Morphling — Adaptive Strike¹ |
| Nature’s Prophet — Wrath of Nature |
| Night Stalker — Void²ᵃ |
| Ogre Magi — Ignite |
| Ogre Magi — Multicast⁷ |
| Phantom Assassin — Stifling Dagger¹ |
| Puck — Phase Shift¹ |
| Razor — Eye of the Storm |
| Rubick — Fade Bolt |
| Shadow Shaman — Ether Shock |
| Shadow Shaman — Mass Serpent Ward²ᵃ |
| Skywrath Mage — Arcane Bolt¹ ²ᵃ |
| Skywrath Mage — Concussive Shot |
| Skywrath Mage — Ancient Seal²ᵃ |
| Skywrath Mage — Mystic Flare²ᵃ |
| Spirit Breaker — Charge of Darkness⁴ |
| Storm Spirit — Electric Vortex²ᵃ |
| Tinker — Laser²ᵃ |
| Tinker — Heat-Seeking Missile |
| Undying — Soul Rip |
| Undying — Tombstone |
| Visage — Soul Assumption¹ |
| Witch Doctor — Death Ward²ᵃ |
| Zeus — Arc Lightning |

[corpus:liquipedia_dota2/vision@2383431#Vision_interaction_with_spells]

¹ requires a talent; 2a requires Aghanim’s Scepter; 2b requires Aghanim’s Shard; and 3 requires the corresponding facet. When Homing Missile⁴ or Charge of Darkness⁴ loses its current target to death, it chooses only visible enemies as new targets. Mana Drain⁵ immediately ends if its target enters the Fog of War. Starstorm’s initial wave⁶ requires vision, but its secondary single projectile does not. Multicast⁷ items and Ignite select only visible secondary targets. [corpus:liquipedia_dota2/vision@2383431#Vision_interaction_with_spells]

## Historical changes

| Version | Date | Change |
|---|---|---|
| 7.41c | 2026-05-06 | Units with flying vision no longer ignore Roshan-pit vision restrictions and cannot see into a pit from outside or vice versa. Affects Jetpack, Glacier, Tree Dance, Dark Ascension, Eyes In The Forest, and Visage’s Familiars. |
| 7.23 | 2019-11-26 | Firefly no longer grants flying vision while active. |
| 6.83 | 2014-12-17 | Vision and Fog of War can use any numerical value rather than only 0, 64, 192, 320, 448, 576, 704, 800, 832, 960, 1088, 1216, 1344, 1472, 1600, and 1728. Previously, values between the fixed intervals were clamped to a fixed value. |

[corpus:liquipedia_dota2/vision@2383431#Recent_Changes]