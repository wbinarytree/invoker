---
title: Trap
kind: concept
patch: 7.41d
card:
  entity: trap
  sentences:
  - text: A trap is a disable that completely or partially surrounds a unit with immobile
      objects or otherwise restricts its movement so it cannot escape, without preventing
      attacks or the use of abilities and items.
    marks:
    - corpus:liquipedia_dota2/trap@2226366
  - text: A pathing blocker is an invisible entity with collision size that physically
      blocks other units.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers
  - text: Phased movement cannot pass through pathing blockers, but flying or unobstructed
      movement can.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers
  - text: Lane creeps try to walk through pathing blockers and are stopped completely,
      while player-controlled units path around them when possible.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers
  - text: Minimum distance from a pathing blocker depends on both entities’ bound
      radii; Marci and a Cycloned unit’s center remain 2.5 apart.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers
  - text: A temporary fence prevents crossing by drastically slowing movement speed
      towards 0 near the field’s edges.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Temporary_Fence
  - text: The temporary-fence slow applies only during a crossing attempt and disappears
      when the unit turns away from the edge.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Temporary_Fence
  - text: Kinetic Field creates an indestructible circular barrier of 70-unit radius
      that enemies cannot walk into or out of.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Temporary_Fence
  - text: Arena of Blood creates an indestructible circular arena of 100-unit radius
      that enemies cannot walk into or out of.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Temporary_Fence
  - text: Pounce restricts a leashed target to a 2.5/2.75/3/3.25-unit radius around
      Slark’s landing position.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Temporary_Fence
  - text: Barriers instantly stop several forced-movement sources at the field’s edge
      without canceling their movement component, which may continue if the barrier
      disappears.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling
  - text: Barriers stop Rebound’s initial dash, but its leap can pass through.
    marks:
    - corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling
---

# Trap

A **trap** is a disable that completely or partially surrounds a unit with immobile objects or otherwise restricts its movement so it cannot escape. Traps do not prevent actions such as attacking or using abilities and items. Interactions between individual traps and escape skills may differ. Templar Assassin also has a sub-ability named Trap. [corpus:liquipedia_dota2/trap@2226366]

## Definition

| Type | Definition | Example |
|---|---|---|
| Pathing Blocker | An invisible entity with a collision size that physically blocks other units walking against it, unless the caster has unobstructed movement. [corpus:liquipedia_dota2/trap@2226366#Definition] | Fissure |
| Temporary Fence | A force field that uses leash to prevent a unit from moving out of or into the affected area by drastically slowing its movement speed towards 0 near the field’s edges. The slow is not shown in the HUD. [corpus:liquipedia_dota2/trap@2226366#Definition] | Kinetic Field |

## Pathing Blockers

A pathing blocker is an invisible entity with a collision size that physically blocks other units. Walking against one is like walking against a unit that is neither phased nor flying, or against trees. Phased movement cannot pass through pathing blockers, but flying or unobstructed movement can. [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers]

Lane creeps do not walk around pathing blockers; they try to walk through and are effectively stopped completely. Player-controlled units try to path around them when possible. The created pathing blockers, `npc_dota_thinker`, are generally not selectable. [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers]

The smallest distance between a pathing blocker and another unit depends on both entities’ bound radius rather than collision size. For example, the smallest distance between Marci and a Cycloned unit’s center is the sum of their bound radii, which is 2.5. Defender’s Gate uses the collision-size mechanic as a pathing blocker. [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers]

### Sources

| Source | Ability |
|---|---|
| Clockwerk | Power Cogs [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |
| Drow Ranger | Glacier [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |
| Earthshaker | Fissure [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |
| Buildings | Defender’s Gate [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |
| Nature’s Prophet | Sprout [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |
| Tusk | Ice Shards [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |
| Eul’s Scepter of Divinity | Cyclone [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |
| Wind Waker | Cyclone [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |

| Annotation | Requirement |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |
| 2a | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |
| 2b | Requires Aghanim’s Shard. [corpus:liquipedia_dota2/trap@2226366#Pathing_Blockers] |

## Temporary Fence

A temporary fence is a force field that prevents a unit from moving out of or into an affected area by drastically slowing its movement speed towards 0 near the field’s edges. The slow applies only while the unit attempts to cross the barrier; turning around and walking away from the edge removes the slow. [corpus:liquipedia_dota2/trap@2226366#Temporary_Fence]

### Barrier-Creating Abilities

| Source | Ability | Effect |
|---|---|---|
| Disruptor | Kinetic Field | Creates an indestructible circular barrier of 70-unit radius that enemies cannot walk into or out of. The field does not affect units under spell immunity. [corpus:liquipedia_dota2/trap@2226366#Temporary_Fence] |
| Grimstroke | Soulbind | Prevents the target and its linked ally from moving more than a certain range away from each other. [corpus:liquipedia_dota2/trap@2226366#Temporary_Fence] |
| Mars | Arena of Blood | Creates an indestructible circular arena of 100-unit radius that enemies cannot walk into or out of. It does not affect units under spell immunity. [corpus:liquipedia_dota2/trap@2226366#Temporary_Fence] |
| Slark | Pounce | Restricts the leashed target’s movement to a 2.5/2.75/3/3.25-unit radius around Slark’s landing position. It does not affect units under spell immunity. [corpus:liquipedia_dota2/trap@2226366#Temporary_Fence] |

### Forced Movement Disabling

Barriers also stop several sources of forced movement instantly when the affected unit is pushed towards the field’s edge. The forced-movement component is not canceled; if the barrier disappears, the movement may continue in that direction. [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling]

| Source | Forced-movement ability |
|---|---|
| Dawnbreaker | Starbreaker [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Force Boots | Force [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Force Staff | Force [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Hurricane Pike | Hurricane Thrust [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Psychic Headband | Psychic Push [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Magnus | Skewer [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Marci | Rebound¹ [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Mars | God’s Rebuke [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Monkey King | Primal Spring [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Monkey King | Tree Dance [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Mirana | Leap [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Phoenix | Sun Ray [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Slark | Pounce [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |
| Snapfire | Firesnap Cookie [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling] |

¹ Rebound’s initial dash is stopped by barriers, but its leap can pass through. [corpus:liquipedia_dota2/trap@2226366#Forced_Movement_Disabling]

## Version History

| Version | Date | Change |
|---|---|---|
| 6.81 | 2014-04-29 | Creeps no longer try to path around Fissure; they wait for it to disappear. [corpus:liquipedia_dota2/trap@2226366#Version_History] |

## Patch History

| Date | Update | Change | Affected pathing blocker |
|---|---|---|---|
| 16 Jun 2022 | UPDATE 2 | Fixed ability interactions between pathing blockers with the `DOTA_OBSTRUCTION_PROPERTY_NPC_STOPPER` flag, Roll Up, and Rolling Thunder. | Power Cogs [corpus:liquipedia_dota2/trap@2226366#Patch_History] |
| 16 Jun 2022 | UPDATE 2 | Fixed ability interactions between pathing blockers with the `DOTA_OBSTRUCTION_PROPERTY_NPC_STOPPER` flag, Roll Up, and Rolling Thunder. | Fissure [corpus:liquipedia_dota2/trap@2226366#Patch_History] |
| 16 Jun 2022 | UPDATE 2 | Fixed ability interactions between pathing blockers with the `DOTA_OBSTRUCTION_PROPERTY_NPC_STOPPER` flag, Roll Up, and Rolling Thunder. | Ice Shards [corpus:liquipedia_dota2/trap@2226366#Patch_History] |
| 05 Jan 2016 | — | Changed creep and neutral pathfinding. | Power Cogs [corpus:liquipedia_dota2/trap@2226366#Patch_History] |
| 05 Jan 2016 | — | Changed creep and neutral pathfinding. | Fissure [corpus:liquipedia_dota2/trap@2226366#Patch_History] |
| 05 Jan 2016 | — | Changed creep and neutral pathfinding. | Sprout [corpus:liquipedia_dota2/trap@2226366#Patch_History] |
| 05 Jan 2016 | — | Changed creep and neutral pathfinding. | Ice Shards [corpus:liquipedia_dota2/trap@2226366#Patch_History] |