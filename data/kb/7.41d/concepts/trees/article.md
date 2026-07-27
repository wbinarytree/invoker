---
title: Trees
kind: concept
patch: 7.41d
card:
  entity: trees
  sentences:
  - text: Trees are normally impassable, vision-blocking terrain features covering
      much of the map; every permanent tree has a 128x128-unit block size, and the
      map contains 2357 trees—1215 Radiant and 1142 Dire.
    marks:
    - corpus:liquipedia_dota2/trees@2217001
    - corpus:liquipedia_dota2/trees@2217001#Mechanics
    - corpus:liquipedia_dota2/trees@2217001#Tree_Count
  - text: Normal attacks and most abilities cannot target trees, with exceptions including
      Tree Dance.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Mechanics
  - text: Tree collision is governed by the clip mesh as impassable terrain, affecting
      the navigation-grid square it contacts.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Mechanics
  - text: Destroyed trees regrow after 3 minutes.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Respawn_Time
  - text: If a unit is within 150 range of a respawn point, the tree waits to regrow
      until the unit leaves that range.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Respawn_Time
  - text: Treant Protector’s Eyes In The Forest sets natural-tree respawn time to
      360 but does not affect planted trees.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Respawn_Time
  - text: Acquiring Eyes In The Forest respawns all trees globally.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Respawn_Time
  - text: Tree-walking permits unobstructed movement through trees.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Tree-Walking
  - text: Flying or unobstructed movement sources grant tree-walking while active.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Tree-Walking
  - text: Planted trees usually have a smaller collision size than naturally occurring
      trees.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Planted_Trees
  - text: Most forced-movement sources continuously destroy trees directly collided
      with by moving entities or affected units.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Destroying_Trees
  - text: Version 7.33 increased the total tree count from 2122 to 2357.
    marks:
    - corpus:liquipedia_dota2/trees@2217001#Recent_Changes
---

# Trees

Trees are prominent terrain features that cover much of the map, particularly the forests separating the lanes and bordering the map. They block vision and are normally impassable. [corpus:liquipedia_dota2/trees@2217001]

## Mechanics

Trees cannot be targeted by normal attacks or most abilities, with a handful of exceptions such as Tree Dance. Despite differences in appearance and apparent size, every permanent tree has a block size of a `128x128` unit square. Trees do not strictly have a collision size; the clip mesh drives them like impassable terrain and affects the navigation grid square it contacts. The cheat-enabled console command `dota_treerespawn` respawns every destroyed tree on the map. [corpus:liquipedia_dota2/trees@2217001#Mechanics]

### Respawn Time

Trees regrow 3 minutes after being destroyed. If a unit is standing within 150 range of the respawn point, the tree instead respawns once the unit leaves that range, preventing the unit from becoming stuck in the trees. [corpus:liquipedia_dota2/trees@2217001#Respawn_Time]

Treant Protector’s Eyes In The Forest modifies tree respawning as follows: [corpus:liquipedia_dota2/trees@2217001#Respawn_Time]

| Property | Effect |
|---|---|
| Set Respawn Time | 360 [corpus:liquipedia_dota2/trees@2217001#Respawn_Time] |
| Acquisition | Respawns all trees globally upon acquiring the item. [corpus:liquipedia_dota2/trees@2217001#Respawn_Time] |
| Passive effect | Sets the respawn time of all natural trees but does not affect planted trees. [corpus:liquipedia_dota2/trees@2217001#Respawn_Time] |
| Requirement | Innate to Treant Protector and requires Eyes In The Forest to be unlocked. [corpus:liquipedia_dota2/trees@2217001#Respawn_Time] |

### Tree Count

Each tree has an `ent_dota_tree` classname in the map entity file. There are currently 2357 trees: the Radiant uses 8 different types of assorted Bamboo Tree, Oak Tree, and Pine Tree, totaling 1215 trees, while the Dire uses 3 types, totaling 1142 trees. [corpus:liquipedia_dota2/trees@2217001#Tree_Count]

| Faction | Tree type | Model | Count |
|---|---|---|---|
| Radiant | Bamboo Tree | 00 / 03 | 0 [corpus:liquipedia_dota2/trees@2217001#Tree_Count] |
| Radiant | Bamboo Tree | 01 / 02 | 34 / 78 [corpus:liquipedia_dota2/trees@2217001#Tree_Count] |
| Radiant | Oak Tree | 01 / 01b / 02 | 112 / 173 / 112 [corpus:liquipedia_dota2/trees@2217001#Tree_Count] |
| Radiant | Oak Tree | 03 / 04 / 05 / 06 | 0 [corpus:liquipedia_dota2/trees@2217001#Tree_Count] |
| Radiant | Pine Tree | 01 / 02 / 03b | 501 / 149 / 56 [corpus:liquipedia_dota2/trees@2217001#Tree_Count] |
| Radiant | Pine Tree | 04 / 05 | 0 [corpus:liquipedia_dota2/trees@2217001#Tree_Count] |
| Dire |  | 001 / 002 / 003 / 005 / 006 / 009 / 010 / 011 / 012 | 0 [corpus:liquipedia_dota2/trees@2217001#Tree_Count] |
| Dire |  | 004 / 007 / 008 | 757 / 139 / 246 [corpus:liquipedia_dota2/trees@2217001#Tree_Count] |

## Tree-Walking

Tree-walking is a buff granted by certain abilities that permits unobstructed movement through trees. All flying or unobstructed movement sources also grant tree-walking while active. [corpus:liquipedia_dota2/trees@2217001#Tree-Walking]

| Source | Values and effects |
|---|---|
| Hoodwink – Scurry | Passive Tree Search Radius: 15%/20%/25%/30%. Active Move Speed Bonus: . Grants phased movement. [corpus:liquipedia_dota2/trees@2217001#Tree-Walking] |
| Treant Protector – Nature’s Guise | Tree Search Radius: 200. Move Speed Bonus: 0 ( ). This innate ability does not need to be learned and does not grant phased movement. [corpus:liquipedia_dota2/trees@2217001#Tree-Walking] |
| Roshan – Strength of the Immortal | The status buff also grants phased movement. [corpus:liquipedia_dota2/trees@2217001#Tree-Walking] |

## Planted Trees

Some abilities plant trees in addition to the naturally occurring trees. These planted trees usually last for a limited time, have a smaller collision size, and block less vision than regular trees. [corpus:liquipedia_dota2/trees@2217001#Planted_Trees]

| Source | Effect |
|---|---|
| Hoodwink – Acorn Shot | Creates a tree when targeting the ground. [corpus:liquipedia_dota2/trees@2217001#Planted_Trees] |
| Hoodwink – Decoy | Sends a decoy illusion to the target location. When attacked or hit by a unit-targeted ability, the illusion is destroyed and plants a tree in its place that applies a lesser Bushwhack to nearby enemy heroes. [corpus:liquipedia_dota2/trees@2217001#Planted_Trees] |
| Iron Branch – Plant Tree | Consumes the item upon cast and plants a tree with a smaller collision size. Tango doubles the health regeneration bonus duration when cast on an Ironwood Tree. [corpus:liquipedia_dota2/trees@2217001#Planted_Trees] |
| Nature’s Prophet – Sprout | Creates a ring of trees around the targeted point or unit. [corpus:liquipedia_dota2/trees@2217001#Planted_Trees] |

## Tree-Interacting Abilities

The following abilities interact with trees or grant bonuses while interacting with them. [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities]

| Ability | Requirement marker |
|---|---|
| Hoodwink – Bushwhack |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Hoodwink – Scurry |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Mars – Spear of Mars |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Monkey King – Mischief |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Monkey King – Tree Dance |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Muerta – Dead Shot |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Nature’s Prophet – Nature’s Call |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Nature’s Prophet – Curse of the Oldgrowth |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Tango – Devour |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Tango (Shared) – Devour |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Timbersaw – Timber Chain |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Timbersaw – Whirling Death |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Tiny – Tree Grab |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Tiny – Tree Volley |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Treant Protector – Nature’s Grasp |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Treant Protector – Nature’s Guise |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Treant Protector – Eyes In The Forest |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Treant Protector – Overgrowth | 2a [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| Windranger – Shackleshot |  [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| 2a | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |
| 2b | Requires Aghanim’s Shard. [corpus:liquipedia_dota2/trees@2217001#Trees_Interacting_Abilities] |

### Destroying Trees

Most forced-movement sources continuously destroy trees directly collided with by the moving entities or affected units. Certain abilities instead destroy trees in a single instance; the following sources interact directly with trees and destroy them uniquely. [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees]

| Unique tree-destroying source |
|---|
| Battle Fury – Chop Tree [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| Quelling Blade – Chop Tree [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| Tango – Devour [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| Tango (Shared) – Devour [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| Muerta – Dead Shot [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| Timbersaw – Timber Chain [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| Timbersaw – Flamethrower [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| Tiny – Tree Grab [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| Tiny – Tree Volley [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |

| Marker | Requirement |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| 2a | Requires Aghanim’s Scepter. [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |
| 2b | Requires Aghanim’s Shard. [corpus:liquipedia_dota2/trees@2217001#Destroying_Trees] |

## Recent Changes

| Version | Date | Scope | Change |
|---|---|---|---|
| 7.33 | 2023-04-20 | Timing | Happened between 7.33 and 7.33d. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Total | Increased total tree count from 2122 to 2357. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Radiant | Reduced `tree_bamboo_01` from 48 to 34. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Radiant | Increased `tree_bamboo_02` from 70 to 78. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Radiant | Reduced `tree_oak_01` from 187 to 112. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Radiant | Reduced `tree_oak_01b` from 175 to 173. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Radiant | Increased `tree_oak_02` from 85 to 112. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Radiant | Increased `tree_pine_01` from 296 to 501. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Radiant | Reduced `tree_pine_02` from 168 to 149. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Radiant | Reduced `tree_pine_03b` from 67 to 56. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Dire | Increased `dire_tree004` from 695 to 757. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Dire | Reduced `dire_tree007` from 150 to 139. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.33 | 2023-04-20 | Dire | Increased `dire_tree008` from 181 to 246. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.32e | 2023-03-07 | Muerta | Added Dead Shot, an ability that interacts with trees. Muerta fires a projectile that ricochets on the targeted tree and is destroyed upon the initial projectile impact. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |
| 7.32 | 2022-08-24 | Nature’s Prophet | Added Curse of the Oldgrowth, an ability that interacts with trees. It curses every enemy hero within the radius, displaying them in the Fog of War while slowing and damaging them over time based on the number of trees within the radius. Treants count as trees for the ability. [corpus:liquipedia_dota2/trees@2217001#Recent_Changes] |