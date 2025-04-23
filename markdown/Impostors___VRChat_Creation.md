[Skip to main content](https://creators.vrchat.com/avatars/avatar-impostors/#__docusaurus_skipToContent_fallback)

On this page

What are Impostors?[​](https://creators.vrchat.com/avatars/avatar-impostors/#what-are-impostors "Direct link to What are Impostors?")

--------------------------------------------------------------------------------------------------------------------------------------

Impostors are avatar body doubles, allowing you to see avatars in situations where you would typically see a fallback avatar or robot. They are intended to bridge gaps between different systems/user types in VRChat. For example, if a user’s avatar was only uploaded for Windows, VRChat makes an acceptable impostor for Quest automatically. You can only generate impostors for avatars you own and have uploaded.

Even if you've never uploaded a cross-platform version of your avatar, or if your avatar is "performance blocked" due to its performance rank, other users will still be able to see an impostor of your avatar. Eventually, impostors will be auto-generated, but for now, you create them with a few easy steps. Once you've made an impostor, you can toggle it on and off - when it's off, your fallback avatar will be shown instead.

How do I create an Impostor?[​](https://creators.vrchat.com/avatars/avatar-impostors/#how-do-i-create-an-impostor "Direct link to How do I create an Impostor?")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The first step to creating an impostor is to [create and upload an avatar](https://creators.vrchat.com/avatars/creating-your-first-avatar)
.

Once you've uploaded an avatar, creating an impostor for it is easy:

*   Log in to the VRChat website.
    
*   Navigate to the info page for the avatar you'd like to impostorize. You can do this by pressing "Avatars", then "My Avatars", then the name and icon of the one you want.
    
*   Click "Generate Impostors", or, if the avatar already has an impostor that you'd like to be updated, "Regenerate Impostors"
    
*   Wait.
    
*   Refresh the page, after some time you should now see that your avatar has impostors for Quest and PC.
    

![A screnshot of an avatar&#39;s page on vrchat.com. It allows avatar creators to (re)generate impostors and see which impostors have already been generated. You can see if impostors have been generated for PC and/or Android. You can also see if the impostor has been customized by the avatar creator.](https://creators.vrchat.com/assets/images/generation-6c75dd62f2e9e50402f379a1acd4521c.png)

note

Impostors currently only support [humanoid](https://docs.unity3d.com/Manual/AvatarCreationandSetup.html)
 avatars. [Generic](https://docs.unity3d.com/Manual/GenericAnimations.html)
 avatars will be supported in the future.

Previewing an Impostor[​](https://creators.vrchat.com/avatars/avatar-impostors/#previewing-an-impostor "Direct link to Previewing an Impostor")

------------------------------------------------------------------------------------------------------------------------------------------------

Once you've got your impostor generated, you're probably going to be pretty excited to see how it looks! Well, no worries, we've got you covered!

Once you've logged into VRChat, open the Avatar menu, and click the avatar that you generated an impostor for.

You should notice that the "Features" of the avatar now includes "Impostor".

![A screenshot of the &quot;Features&quot; section of an avatar in VRChat. It shows an &quot;Imposter&quot; icon, among other features.](https://creators.vrchat.com/assets/images/features-row-35660c9e886bfeba553b9c0ae0997479.png)

You should also see a new button underneath the avatar model preview, which will allow you to switch between viewing the impostor and the normal avatar for a quick preview.

![A screenshot of an avatar being previewed in the VRChat menu.](https://creators.vrchat.com/assets/images/preview-avatar-3c13e60cda71eba0d9cca4909d61220f.png) ![A screenshot of an avatar&#39;s imposter being previewed in the VRChat menu. A toggle near the bottom has been enabled.](https://creators.vrchat.com/assets/images/preview-impostor-ef3522020b43b1649a5552d9a93a46e5.png)

note

Impostors that are previewed in the menu may exhibit more artifacts than they would when viewed on another player.

VRCImpostorSettings[​](https://creators.vrchat.com/avatars/avatar-impostors/#vrcimpostorsettings "Direct link to VRCImpostorSettings")

---------------------------------------------------------------------------------------------------------------------------------------

Impostors come out pretty good by default. However, complex avatars may benefit from some customization.

To customize your impostor, add the "VRCImpostorSettings" component to your avatar before uploading it. Changing the settings of this component allows you to change the impostor's appearance. You can add multiple "VRCImpostorSettings" to customize different body parts.

### Resolution Scale[​](https://creators.vrchat.com/avatars/avatar-impostors/#resolution-scale "Direct link to Resolution Scale")

Changes the amount of space on the impostors texture atlas that is dedicated to this body part's texture. For instance, you can place this script on the head bone and change this value to make the head take up more or less of the texture atlas, increasing or decreasing the overall texture quality. Note that this may shrink other parts of the body on the atlas if needed.

_This is relative to the bone that VRCImpostorSettings is placed on._

### Transforms To Ignore[​](https://creators.vrchat.com/avatars/avatar-impostors/#transforms-to-ignore "Direct link to Transforms To Ignore")

Ignores these transforms when capturing data for the impostor. This will hide them from the final result.

_This is independent of the bone that VRCImpostorSettings is placed on._

### Extra Child Transforms[​](https://creators.vrchat.com/avatars/avatar-impostors/#extra-child-transforms "Direct link to Extra Child Transforms")

This is good for things like wings and tails, it will tell the Impostorizer to make a separate sprite for the bone this script is on.

As an example of what not to do - you _could_ put one of these on each finger to turn them into independent sprites. However, since all sprites share a single texture sheet, filling it with things like fingers will cause quality to decrease elsewhere - it's a balancing act.

_This is independent of the bone that VRCImpostorSettings is placed on._

### Re-parent Here[​](https://creators.vrchat.com/avatars/avatar-impostors/#re-parent-here "Direct link to Re-parent Here")

Re-parents another bone to this impostor sprite. This means that it will be impostorized with this body part, and be a part of that sprite.

For instance, if you'd like your wings to be a part of the upper body, you can re-parent the root wing bone to the chest bone during impostorization with this.

_This is relative to the bone that VRCImpostorSettings is placed on._

When is an impostor visible?[​](https://creators.vrchat.com/avatars/avatar-impostors/#when-is-an-impostor-visible "Direct link to When is an impostor visible?")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Currently, there are only three ways to see an impostor.

*   Avatar Preview (e.g. viewing the impostor on the avatar's details page)
*   Performance Blocking (e.g. the avatar's performance rank is "Very Poor" but your [minimum displayed performance rank](https://docs.vrchat.com/docs/vrchat-configuration-window#minimum-displayed-performance-rank)
     is set to "Medium").
*   Platform Mismatch (e.g. the avatar is uploaded for PC, but you're on Android or vice versa)

*   [What are Impostors?](https://creators.vrchat.com/avatars/avatar-impostors/#what-are-impostors)
    
*   [How do I create an Impostor?](https://creators.vrchat.com/avatars/avatar-impostors/#how-do-i-create-an-impostor)
    
*   [Previewing an Impostor](https://creators.vrchat.com/avatars/avatar-impostors/#previewing-an-impostor)
    
*   [VRCImpostorSettings](https://creators.vrchat.com/avatars/avatar-impostors/#vrcimpostorsettings)
    *   [Resolution Scale](https://creators.vrchat.com/avatars/avatar-impostors/#resolution-scale)
        
    *   [Transforms To Ignore](https://creators.vrchat.com/avatars/avatar-impostors/#transforms-to-ignore)
        
    *   [Extra Child Transforms](https://creators.vrchat.com/avatars/avatar-impostors/#extra-child-transforms)
        
    *   [Re-parent Here](https://creators.vrchat.com/avatars/avatar-impostors/#re-parent-here)
        
*   [When is an impostor visible?](https://creators.vrchat.com/avatars/avatar-impostors/#when-is-an-impostor-visible)