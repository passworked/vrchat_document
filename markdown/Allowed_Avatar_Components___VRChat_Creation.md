[Skip to main content](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#__docusaurus_skipToContent_fallback)

On this page

Your can add features to your avatar by [adding components](https://docs.unity3d.com/2022.3/Documentation/Manual/UsingComponents.html)
 to it. However, not all components can be used in VRChat.

*   Any component on the following list can be used in VRChat.
*   Other components or custom scripts won't work in VRChat and may stop you from uploading your avatar.

info

The Android version of VRChat has [additional restrictions](https://creators.vrchat.com/platforms/android/quest-content-limitations#components)
.

VRChat[​](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#vrchat "Direct link to VRChat")

-------------------------------------------------------------------------------------------------------------------------------------------

*   VRCAvatarDescriptor
*   [VRCConstraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints)
    
*   [VRCContactReceiver](https://creators.vrchat.com/avatars/avatar-dynamics/contacts#vrccontactreceiver)
    
*   [VRCContactSender](https://creators.vrchat.com/avatars/avatar-dynamics/contacts#vrccontactsender)
    
*   [VRCHeadChop](https://creators.vrchat.com/avatars/avatar-dynamics/vrc-headchop)
    
*   [VRCIKFollower](https://docs.vrchat.com/docs/vrc_ikfollower)
     - Deprecated! You should use [VRChat Constraints](https://creators.vrchat.com/avatars/avatar-dynamics/constraints)
     instead.
*   [VRCPhysBone](https://creators.vrchat.com/avatars/avatar-dynamics/physbones#vrcphysbone)
    
*   [VRCPhysBoneCollider](https://creators.vrchat.com/avatars/avatar-dynamics/physbones#vrcphysbonecollider)
    
*   [VRCPipelineManager](https://creators.vrchat.com/sdk/vrcpipelinemanager/)
    
*   [VRCSpatialAudioSource](https://creators.vrchat.com/worlds/components/vrc_spatialaudiosource#spatial-audio-on-avatars)
    
*   [VRCStation](https://creators.vrchat.com/worlds/components/vrc_station)
    

Unity[​](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#unity "Direct link to Unity")

----------------------------------------------------------------------------------------------------------------------------------------

*   [AimConstraint](https://docs.unity3d.com/2022.3/Documentation/Manual/class-AimConstraint.html)
    
*   [Animation](https://docs.unity3d.com/2022.3/Documentation/Manual/class-Animation.html)
    
*   [Animator](https://docs.unity3d.com/2022.3/Documentation/Manual/class-Animator.html)
    
*   [AudioSource](https://docs.unity3d.com/2022.3/Documentation/Manual/class-AudioSource.html)
    
*   [Camera](https://docs.unity3d.com/2022.3/Documentation/Manual/class-Camera.html)
     (See [notes below](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#cameras-on-avatars)
    )
*   [Cloth](https://docs.unity3d.com/2022.3/Documentation/Manual/class-Cloth.html)
    
*   [Collider](https://docs.unity3d.com/2022.3/Documentation/Manual/CollidersOverview.html)
    
*   [FlareLayer](https://docs.unity3d.com/2022.3/Documentation/Manual/class-FlareLayer.html)
    
*   [Joints](https://docs.unity3d.com/2022.3/Documentation/Manual/Joints.html)
    
*   [Light](https://docs.unity3d.com/2022.3/Documentation/Manual/class-Light.html)
    
*   [LineRenderer](https://docs.unity3d.com/2022.3/Documentation/Manual/class-LineRenderer.html)
    
*   [LookAtConstraint](https://docs.unity3d.com/2022.3/Documentation/Manual/class-LookAtConstraint.html)
    
*   [MeshFilter](https://docs.unity3d.com/2022.3/Documentation/Manual/class-MeshFilter.html)
    
*   [MeshRenderer](https://docs.unity3d.com/2022.3/Documentation/Manual/class-MeshRenderer.html)
    
*   [ParentConstraint](https://docs.unity3d.com/2022.3/Documentation/Manual/class-ParentConstraint.html)
    
*   [ParticleSystemRenderer](https://docs.unity3d.com/2022.3/Documentation/Manual/PartSysRendererModule.html)
    
*   [ParticleSystem](https://docs.unity3d.com/2022.3/Documentation/Manual/class-ParticleSystem.html)
    
*   [PositionConstraint](https://docs.unity3d.com/2022.3/Documentation/Manual/class-PositionConstraint.html)
    
*   [Rigidbody](https://docs.unity3d.com/2022.3/Documentation/Manual/class-Rigidbody.html)
    
*   [RotationConstraint](https://docs.unity3d.com/2022.3/Documentation/Manual/class-RotationConstraint.html)
    
*   [ScaleConstraint](https://docs.unity3d.com/2022.3/Documentation/Manual/class-ScaleConstraint.html)
    
*   [SkinnedMeshRenderer](https://docs.unity3d.com/2022.3/Documentation/Manual/class-SkinnedMeshRenderer.html)
    
*   [TrailRenderer](https://docs.unity3d.com/2022.3/Documentation/Manual/class-TrailRenderer.html)
    
*   [Transform](https://docs.unity3d.com/2022.3/Documentation/Manual/class-Transform.html)
    

### Cameras on Avatars[​](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#cameras-on-avatars "Direct link to Cameras on Avatars")

For avatars worn by the local user, Camera components are fully whitelisted. For remote users, the following rules apply:

*   In all cases, the Camera components of remote users are disabled when the avatar is loaded.
    *   You can use animations to enable Camera components.
*   If the local user and remote user are friends, Camera components are not removed.
    *   Note that becoming friends with a user does not automatically reload their avatar.
*   If the local user has selected "Show Avatar" for the remote user in VRChat's quick menu, Camera components are not removed.
*   If neither of the above is true, Camera components are removed and cannot be enabled.

[Root Motion (FinalIK)](http://www.root-motion.com/finalikdox/html/index.html)
[​](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#root-motion-finalik "Direct link to root-motion-finalik")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

VRChat has highly modified its implementation of FinalIK. As such, these components may not work as documented.

We do not directly support or test custom FinalIK implementations on avatars. However, they _should_ work fine, and if we must intentionally break one or more of these, we will try our best to inform creators.

If you discover a bug, please [let us know](https://feedback.vrchat.com/)
.

*   [Aim IK](http://www.root-motion.com/finalikdox/html/page1.html)
    
*   [Biped IK](http://www.root-motion.com/finalikdox/html/page4.html)
    
*   [CCDIK](http://www.root-motion.com/finalikdox/html/page5.html)
    
*   [FABRIK](http://www.root-motion.com/finalikdox/html/page6.html)
    
*   [Full Body Biped IK](http://www.root-motion.com/finalikdox/html/page8.html)
    
*   [Grounder](http://www.root-motion.com/finalikdox/html/page9.html)
    
*   [Limb IK](http://www.root-motion.com/finalikdox/html/page12.html)
    
*   [Rotation Limits](http://www.root-motion.com/finalikdox/html/page14.html)
    
*   Shoulder Rotator
*   Twist Relaxer
*   [VRIK](http://www.root-motion.com/finalikdox/html/page16.html)
    [1](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#user-content-fn-2)
    

[DynamicBone](https://assetstore.unity.com/packages/tools/animation/dynamic-bone-16743)
[​](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#dynamicbone "Direct link to dynamicbone")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Dynamic Bone Deprecated

Support for Dynamic Bone is deprecated. You should use [PhysBones](https://creators.vrchat.com/avatars/avatar-dynamics/physbones)
 instead.

*   DynamicBone
*   DynamicBoneCollider

Footnotes[​](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#footnote-label "Direct link to Footnotes")

---------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Using this script on a humanoid avatar will break it. [↩](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#user-content-fnref-2)
    

*   [VRChat](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#vrchat)
    
*   [Unity](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#unity)
    *   [Cameras on Avatars](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#cameras-on-avatars)
        
*   [Root Motion (FinalIK)](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#root-motion-finalik)
    
*   [DynamicBone](https://creators.vrchat.com/avatars/whitelisted-avatar-components/whitelisted-avatar-components/#dynamicbone)