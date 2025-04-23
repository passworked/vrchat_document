[Skip to main content](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#__docusaurus_skipToContent_fallback)

On this page

The Avatar Performance Ranking System allows you to see how much a user's avatar is affecting performance via analysis of the components on that user's avatar. You can also use it on yourself to see how performant your avatar is.

This system is provided to inform users what is likely the most performance-heavy components on their avatars, and offer basic advice on what to look into when optimizing their avatar.

It is also used to drive the [Minimum Displayed Performance Rank](https://creators.vrchat.com/avatars/avatar-performance-ranking-system#minimum-displayed-performance-rank-on-pc)
 system, which is a way for users to decide what avatars they wish to show based on their Performance Rank.

**This system is not meant to be an end-all-be-all authority on avatar performance**, but is a good general guide to indicate if an avatar needs a bit more work to be performant.

Perf Ranks are not the final word!

Although the Performance Rank system does as best as it can to judge the "worst case" scenario of an avatar's performance, there are many ways to have a well-optimized avatar appear as Very Poor, and have a FPS hog rank as Excellent.

For the technically inclined: the Performance Rank system is based on a static analysis of the avatar's properties without any consideration paid to things like animators, shaders, texture resolution, pixel lights, and many more factors. _However_, it tends to provide an excellent litmus test for detecting problematic avatars 95% of the time!

Short Version[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#short-version "Direct link to Short Version")

--------------------------------------------------------------------------------------------------------------------------------------

**Aim for Good ranking.** If you can't hit that, **Medium is perfectly fine.**

Creating avatars is already hard, and creating optimized avatars is even harder. It is a skill that takes a long time to build!

Keep in mind that many events, groups, and locations in VRChat may ask you to change your avatar if you show up in a Very Poor avatar. As such, even if you choose to use a Very Poor avatar in small instances with your friends, make sure you also have one meant for usage in instances with more people.

Your avatar affects everyone else's framerate, so be mindful of how your choices affect other people's experiences. Otherwise, they might see you as your Fallback!

Performance Ranking Icons[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#performance-ranking-icons "Direct link to Performance Ranking Icons")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you open your Quick Menu, you'll see icons appear on top of the nameplates of users.

The ranks are as follows:

| Icon | Performance Rank | Description |
| --- | --- | --- |
| ![image](<Base64-Image-Removed>) | Excellent | This is as good as you can get! The "Gold Star on the Fridge" rank. |
| ![image](https://creators.vrchat.com/assets/images/good-12ca687123e41921dcfbbde51814362d.png) | Good | Good enough! A great target to aim for. |
| ![image](https://creators.vrchat.com/assets/images/medium-29559721165021dfafaef1c7dece9bab.png) | Medium | Don't let the name fool you, Medium is plenty good. If you're here and don't want to work any farther up, you're fine. |
| ![image](https://creators.vrchat.com/assets/images/poor-8ffee00013eff2bb8073c3f37a9119fa.png) | Poor | Could use some work. |
| ![image](https://creators.vrchat.com/assets/images/very-poor-ad76572d037c51878b00b3d7ed492bb0.png) | Very Poor | This avatar has some serious performance problems. Since this rank is unbounded, it is very possible that your performance is suffering as a result of this avatar being visible. |

Viewing Detailed Avatar Stats[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#viewing-detailed-avatar-stats "Direct link to Viewing Detailed Avatar Stats")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you click on a user with your Quick Menu open, you'll notice a new **"Show Avatar Stats"** button on the left side, displaying the icon of that user's Performance Rank.

![avatar-perormance-breakdown.gif](https://creators.vrchat.com/assets/images/view-avatar-details-qm-b2d08ac3fe261fcb11e247e5f8eb0510.png)

If you click this icon, you can view the detailed **Avatar Stats** of that avatar. You can get to this for your own avatar by going to your Avatar Menu, clicking one of your avatars, and clicking the **Avatar Stats** button in the bottom left of the screen.

![avatar-perormance-breakdown.gif](https://creators.vrchat.com/assets/images/view-avatar-details-preview-6927ecc7999a2f7bbb0e9a5880ff020e.png)

When you click the **Avatar Stats** button, you'll get a screen pop up with the details of avatar you're looking at, or your own avatar (if you clicked the button in the Avatar tab).

![avatar-perormance-breakdown.gif](https://creators.vrchat.com/assets/images/avatar-perormance-breakdown-4db75b7acd4f77567101100469d76cd2.gif)

The color of the text matches the rank that the particular stat "drags" the rank down to.

You'll also see a "before and after" in the form of the "Original" and "Perf Filtered" lines. If you're using the [Minimum Displayed Performance Rank](https://creators.vrchat.com/avatars/avatar-performance-ranking-system#minimum-displayed-performance-rank-on-pc)
 system, you can see what the stats were before and after the system removed components. In the case of the Minimum Displayed Performance Rank system blocking an avatar for performance reasons, you'll only see the original stats.

In the example given above, Lights and Particle Systems are disabled due to exceeding the limit defined. Because Particle Systems employ at least one material each, the count of materials from Particle Systems is also subtracted from the pre-filtered avatar.

You can also see that we link to our **Documentation**, in particular our [Avatar Optimization Tips](https://creators.vrchat.com/avatars/avatar-optimizing-tips)
.

Avatar Performance Ranking Stats[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#avatar-performance-ranking-stats "Direct link to Avatar Performance Ranking Stats")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here is a listing of all of the statistics that the system looks at and their description.

Bolded stats will cause the avatar to be fully blocked if they exceed the Minimum Displayed Performance Rank. If other stats (except for bounds) exceed the Minimum Displayed Performance Rank the avatar will only be partially blocked. The avatar will be shown with any components related to the exceeded stats will be removed.

For example with the Minimum Displayed Performance Rank set to Poor an avatar with 9 Trail Renderers (Very Poor) will be displayed with all of its Trail Renderers removed. Refer to [Minimum Displayed Performance Rank](https://creators.vrchat.com/avatars/avatar-performance-ranking-system#minimum-displayed-performance-rank-on-pc)
 for more information.

| Avatar Quality | Quality Description |
| --- | --- |
| Triangles | The triangle count of the model in question. (In the past, this was incorrectly referred to as "Polygons.") |
| Bounds Size | The total size of the avatar. If this is really huge, that user probably has a large animation on the avatar that isn't showing all the time.  <br>Important note: Bounds Size will not cause the avatar to be blocked, even if it is below the "Minimum Displayed Performance Rank" setting. |
| Texture Memory | The amount of memory estimated to be in use by the avatar's textures. These textures occupy space in both system RAM and in the video card's memory. |
| Skinned Meshes | The number of Skinned Mesh Renderer components on the avatar. |
| Basic Meshes | The number of (non-skinned) Mesh Renderer components on the avatar. |
| Material Slots | The number of material slots on the avatar. Material slots are the slots on the mesh where you fit materials in. This is what counts toward Submesh creation, which incurs further draw calls. Keep in mind that Particle Systems will use one material slot, Particle System with trails use two, and Line Renderers use one material slot. |
| PhysBones Components | The number of PhysBone components on the avatar. |
| PhysBones Affected Transforms | The total number of transforms affected by PhysBones components on the avatar. |
| PhysBones Colliders | The number of PhysBone collider scripts on the avatar. |
| PhysBones Collision Check Count | The sum of how many PhysBone transforms each collider can affect. This can count transforms twice or more, because a single transform can be affected by multiple colliders. |
| Avatar Dynamics Contacts | The number of Avatar Dynamics Contacts on the avatar. Does not count [receivers](https://creators.vrchat.com/avatars/avatar-dynamics/contacts/#vrccontactreceiver)<br> with [filtering](https://creators.vrchat.com/avatars/avatar-dynamics/contacts/#filtering-1)<br> set to "Local Only." |
| Constraint Count | The total number of VRChat constraints and Unity constraints on the avatar. [Click here for more detailed info.](https://creators.vrchat.com/avatars/avatar-dynamics/constraints#performance) |
| Constraint Depth | The deepest chain of dependencies across all constraints on the avatar. [Click here for more detailed info.](https://creators.vrchat.com/avatars/avatar-dynamics/constraints#performance) |
| Animators | The number of Animators on the avatar. Important note: This will always be at least 1 due to the root animator being counted. This means that for the Excellent ranking, you can have no additional animators. |
| Bones | The number of Bones in the avatar's rig. |
| Lights | The number of Light components on the avatar. |
| Particle Systems | The number of Particle System components on the avatar. |
| Total Particles Active | The sum of maxParticles across all particle systems on the avatar. |
| Mesh Particle Active Polys | The total number of triangles of Mesh Particles emitted by Particle Systems that are active. In other words, maxEmission \* meshParticleVerts. |
| Particle Trails Enabled | If any Particle Systems on the avatar have Particle Trails enabled, this will be True. |
| Particle Collision Enabled | If any Particle Systems on the avatar have Particle Collision enabled, this will be True. |
| Trail Renderers | The number of Trail Renderers on the avatar. |
| Line Renderers | The number of Line Renderers on the avatar. |
| Cloths | The total number of Cloth components on the avatar. |

Avatar Performance Ranks - Value Maximums per Rank[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#avatar-performance-ranks---value-maximums-per-rank "Direct link to Avatar Performance Ranks - Value Maximums per Rank")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below, you'll find the limits for each of the Performance Ranks. If you go above these numbers for any category, you'll be bumped into the next rank.

For example (on PC), if your avatar has 2 Skinned Meshes, your avatar will be ranked as Good, as that exceeds the rating for Excellent, but does not exceed the rating for Good.

All GameObjects and Components are counted!

All GameObjects and Components, **including those that are currently disabled**, count towards the Avatar Performance Rank.

Mesh Read/Write Disabled

If you disable Mesh Read/Write on **any** mesh on the avatar (including particle systems), the "Triangles" count will read "Mesh Read/Write Disabled" and the avatar's Performance Rank will be immediately downgraded to "Very Poor" regardless of the actual triangle count on the avatar.

The SDK warns you of this and will require that you fix it before you upload.

PC Limits[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#pc-limits "Direct link to PC Limits")

--------------------------------------------------------------------------------------------------------------------------

| Avatar Quality | Excellent | Good | Medium | Poor |
| --- | --- | --- | --- | --- |
| Triangles | 32,000 | 70,000 | 70,000 | 70,000 |
| Bounds Size[1](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fn-1) | 2.5m x 2.5m x 2.5m | 4m x 4m x 4m | 5m x 6m x 5m | 5m x 6m x 5m |
| Texture Memory | 40 MB | 75 MB | 110 MB | 150 MB |
| Skinned Meshes | 1   | 2   | 8   | 16  |
| Basic Meshes | 4   | 8   | 16  | 24  |
| Material Slots | 4   | 8   | 16  | 32  |
| [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)<br> Components | 4   | 8   | 16  | 32  |
| [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)<br> Affected Transforms | 16  | 64  | 128 | 256 |
| [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)<br> Colliders | 4   | 8   | 16  | 32  |
| [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)<br> Collision Check Count | 32  | 128 | 256 | 512 |
| Avatar Dynamics [Contacts](https://creators.vrchat.com/avatars/avatar-dynamics/contacts) | 8   | 16  | 24  | 32  |
| [Constraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints)<br> Count | 100 | 250 | 300 | 350 |
| [Constraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints)<br> Depth | 20  | 50  | 80  | 100 |
| Animators | 1   | 4   | 16  | 32  |
| Bones | 75  | 150 | 256 | 400 |
| Lights | 0   | 0   | 0   | 1   |
| Particle Systems | 0   | 4   | 8   | 16  |
| Total Particles Active | 0   | 300 | 1000 | 2500 |
| Mesh Particle Active Polys | 0   | 1000 | 2000 | 5000 |
| Particle Trails Enabled | False | False | True | True |
| Particle Collision Enabled | False | False | True | True |
| Trail Renderers | 1   | 2   | 4   | 8   |
| Line Renderers | 1   | 2   | 4   | 8   |
| Cloths | 0   | 1   | 1   | 1   |
| Total Cloth Vertices | 0   | 50  | 100 | 200 |
| Physics Colliders | 0   | 1   | 8   | 8   |
| Physics Rigidbodies | 0   | 1   | 8   | 8   |
| Audio Sources | 1   | 4   | 8   | 8   |

The table below describes the requirements for PC avatars to receive a certain performance rank:

### PC Default Performance Rank Blocking[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#pc-default-performance-rank-blocking "Direct link to PC Default Performance Rank Blocking")

On PC, the default Minimum Displayed Performance Rank level is "Very Poor". This means that users can see most avatars by default. If you a user enables the [Minimum Displayed Performance Rank](https://creators.vrchat.com/avatars/avatar-performance-ranking-system#minimum-displayed-performance-rank-on-pc)
 system, they can choose to hide avatars with poor performance.

However, if your avatar is extremely unoptimized, VRChat may prevent you from using it. You can fix this my improving its performance rank, ensuring that it doesn't exceed VRChat's [avatar size limits](https://creators.vrchat.com/avatars/avatar-size-limits)
, and then reuploading the avatar.

Mobile Limits[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#mobile-limits "Direct link to Mobile Limits")

--------------------------------------------------------------------------------------------------------------------------------------

VRChat on Android and iOS (phones, tablets, and Meta Quest) has stricter limits that VRChat on PC.

The table below describes the requirements for mobile avatar to receive a certain performance rank:

| Avatar Quality | Excellent | Good | Medium | Poor |
| --- | --- | --- | --- | --- |
| Triangles | 7,500 | 10,000 | 15,000 | 20,000 |
| Bounds Size[1](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fn-1) | 2.5m x 2.5m x 2.5m | 4m x 4m x 4m | 5m x 6m x 5m | 5m x 6m x 5m |
| Texture Memory | 10 MB | 18 MB | 25 MB | 40 MB |
| Skinned Meshes | 1   | 1   | 2   | 2   |
| Basic Meshes | 1   | 1   | 2   | 2   |
| Material Slots | 1   | 1   | 2   | 4   |
| Animators | 1   | 1   | 1   | 2   |
| Bones | 75  | 90  | 150 | 150 |
| [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)<br> Components[2](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fn-2) | 0   | 4   | 6   | 8   |
| [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)<br> Affected Transforms[2](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fn-2) | 0   | 16  | 32  | 64  |
| [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)<br> Colliders[2](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fn-2) | 0   | 4   | 8   | 16  |
| [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)<br> Collision Check Count[2](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fn-2) | 0   | 16  | 32  | 64  |
| Avatar Dynamics [Contacts](https://creators.vrchat.com/avatars/avatar-dynamics/contacts)<br>[2](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fn-2) | 2   | 4   | 8   | 16  |
| [Constraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints)<br> Count[2](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fn-2) | 30  | 60  | 120 | 150 |
| [Constraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints)<br> Depth[2](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fn-2) | 5   | 15  | 35  | 50  |
| Particle Systems | 0   | 0   | 0   | 2   |
| Total Particles Active | 0   | 0   | 0   | 200 |
| Mesh Particle Active Polys | 0   | 0   | 0   | 400 |
| Particle Trails Enabled | False | False | False | True |
| Particle Collision Enabled | False | False | False | True |
| Trail Renderers | 0   | 0   | 0   | 1   |
| Line Renderers | 0   | 0   | 0   | 1   |

### Mobile Default Performance Rank Blocking[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#mobile-default-performance-rank-blocking "Direct link to Mobile Default Performance Rank Blocking")

On mobile, The Minimum Displayed Performance Rank is "Medium" by default. This means users can't see any avatars ranked as "Poor" or "Very Poor".

Users can set their Performance Rank Block level to "Poor", allowing them to see "Poor" avatars. However, they cannot set their Performance Rank Block level to "Very Poor".

For example, if a mobile avatar exceeds 20,000 triangles, it's "Very Poor" and users can't see it in VRChat. However, users can forcefully show "Very Poor" avatars by selecting the user and clicking "Show Avatar".

warning

In the future, VRChat may remove "Very Poor" mobile avatars and the ability to use "Show Avatar" for "Very Poor" mobile avatars. Please keep this in mind when creating mobile avatars.

### Mobile Avatar Component Limits[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#mobile-avatar-component-limits "Direct link to Mobile Avatar Component Limits")

Some [avatar components](https://creators.vrchat.com/avatars/avatar-dynamics)
 are limited on mobile avatars. You cannot exceed the following limits:

*   8 [PhysBone](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)
     components
*   64 [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)
     affected transforms
*   16 [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)
     colliders
*   64 [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)
     collider checks
*   16 [Avatar Dynamics Contacts](https://creators.vrchat.com/avatars/avatar-dynamics/contacts)
    
*   150 [Constraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints)
     components
*   A dependency depth of 50 [Constraints](https://creators.vrchat.com/avatars/avatar-dynamics/constraints)
    

You cannot bypass the limits above by using "Show Avatar". If a mobile avatar exceeds a limit, all limited avatar components are removed from the avatar in VRChat, even if you enable "Show Avatar".

### Mobile Removed Components[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#mobile-removed-components "Direct link to Mobile Removed Components")

The following components are disabled on mobile devices since they can never appear on avatars:

*   Lights
*   Cloths
*   Total Cloth Vertices
*   Physics Colliders
*   Physics Rigidbodies
*   Audio Sources

These values may still appear in VRChat's avatar details screen, but they are always zero.

Minimum Displayed Performance Rank[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#minimum-displayed-performance-rank "Direct link to Minimum Displayed Performance Rank")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can choose to manage avatars based on their Avatar Performance Rank. This option is available in the [Performance Options](https://docs.vrchat.com/docs/vrchat-configuration-window)
 menu, accessible as a button in the top-right of the Safety tab in the main menu.

When you choose a Performance Rank in VRChat's menu, all avatars that are below that level will have their components/display managed as described below.

| Parameter | Description |
| --- | --- |
| Triangles | **Avatar replaced with [Fallback](https://docs.vrchat.com/docs/avatar-fallback-system)<br>** |
| Bounds Size | No change |
| Texture Memory | **Avatar replaced with [Fallback](https://docs.vrchat.com/docs/avatar-fallback-system)<br>** |
| Skinned Meshes | **Avatar replaced with [Fallback](https://docs.vrchat.com/docs/avatar-fallback-system)<br>** |
| Basic Meshes | **Avatar replaced with [Fallback](https://docs.vrchat.com/docs/avatar-fallback-system)<br>** |
| Material Slots | **Avatar replaced with [Fallback](https://docs.vrchat.com/docs/avatar-fallback-system)<br>** |
| Physics Bone Components, Transforms, Colliders, CollisionCheckCount, or Contacts | All PhysBone, PhysBone Collider,and Contact components removed |
| Constraint Count or Depth | All Constraint components removed |
| Animators | All animators (aside from root animator) removed |
| Bones | **Avatar replaced with [Fallback](https://docs.vrchat.com/docs/avatar-fallback-system)<br>** |
| Lights | All Lights removed |
| Particle Systems | All Particle Systems removed |
| Total Particles Active | All Particle Systems removed |
| Mesh Particle Active Polys | All Particle Systems removed |
| Particle Trails Enabled | All Particle Systems removed |
| Particle Collision Enabled | All Particle Systems removed |
| Trail Renderers | All Trail Renderers removed |
| Line Renderers | All Line Renderers removed |
| Cloths | All Cloth components removed |
| Total Cloth Vertices | All Cloth components removed |
| Physics Colliders | All Physics Colliders removed |
| Physics Rigidbodies | All Physics Rigidbodies removed |
| Audio Sources | All Audio Sources removed |

### Minimum Displayed Performance Rank on PC[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#minimum-displayed-performance-rank-on-pc "Direct link to Minimum Displayed Performance Rank on PC")

On VRChat for PC, the Minimum Displayed Performance Rank is set to "Very Poor" by default. This means that, by default, no avatars will have their components or display affected for performance reasons on PC. If you wish to change this, you can choose between "Medium", "Poor", or "Very Poor" options.

### Avatar Performance Rank Blocking on Mobile[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#avatar-performance-rank-blocking-on-mobile "Direct link to Avatar Performance Rank Blocking on Mobile")

On VRChat for mobile devices, the Avatar Performance Rank Block is set to "Medium" by default. You can choose to change this to "Poor" to see avatars of that rank, but your performance may suffer as a result.

You cannot disable the Avatar Performance Rank Block system on mobile. In other words, avatars that are ranked as "Very Poor" will always have their display managed VRChat for mobile, and may not display at all.

No matter what setting you choose, if the [Avatar Dynamics](https://creators.vrchat.com/avatars/avatar-dynamics)
 component limits are exceeded on mobile devices, all of those components will be removed. In short, there is a hard cap for Avatar Dynamics components on mobile avatars.

### Overriding Individual Avatars[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#overriding-individual-avatars "Direct link to Overriding Individual Avatars")

danger

**"Show Avatar" for Very Poor avatars functionality may be removed in the future, and Very Poor avatars may be removed from Android and iOS entirely.** Please keep this in mind when creating avatars for VRChat on mobile devices.

You can choose to override the the entirety of the system (and the Safety system) by selecting "Show Avatar" on each user you wish to show.

Footnotes[​](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#footnote-label "Direct link to Footnotes")

-------------------------------------------------------------------------------------------------------------------------------

1.  Bounds Size is determined by the maximum size of all components on your avatar. Trail and Line Renderers do not count for this calculation. [↩](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fnref-1)
     [↩2](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fnref-1-2)
    
2.  If the Very Poor value is exceeded on mobile, no matter the current "Show Avatar" state of the avatar, all Avatar Dynamics-related components will be removed. [↩](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fnref-2)
     [↩2](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fnref-2-2)
     [↩3](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fnref-2-3)
     [↩4](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fnref-2-4)
     [↩5](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fnref-2-5)
     [↩6](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fnref-2-6)
     [↩7](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#user-content-fnref-2-7)
    

*   [Short Version](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#short-version)
    
*   [Performance Ranking Icons](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#performance-ranking-icons)
    
*   [Viewing Detailed Avatar Stats](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#viewing-detailed-avatar-stats)
    
*   [Avatar Performance Ranking Stats](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#avatar-performance-ranking-stats)
    
*   [Avatar Performance Ranks - Value Maximums per Rank](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#avatar-performance-ranks---value-maximums-per-rank)
    
*   [PC Limits](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#pc-limits)
    *   [PC Default Performance Rank Blocking](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#pc-default-performance-rank-blocking)
        
*   [Mobile Limits](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#mobile-limits)
    *   [Mobile Default Performance Rank Blocking](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#mobile-default-performance-rank-blocking)
        
    *   [Mobile Avatar Component Limits](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#mobile-avatar-component-limits)
        
    *   [Mobile Removed Components](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#mobile-removed-components)
        
*   [Minimum Displayed Performance Rank](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#minimum-displayed-performance-rank)
    *   [Minimum Displayed Performance Rank on PC](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#minimum-displayed-performance-rank-on-pc)
        
    *   [Avatar Performance Rank Blocking on Mobile](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#avatar-performance-rank-blocking-on-mobile)
        
    *   [Overriding Individual Avatars](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/#overriding-individual-avatars)