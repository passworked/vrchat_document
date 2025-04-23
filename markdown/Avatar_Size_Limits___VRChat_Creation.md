[Skip to main content](https://creators.vrchat.com/avatars/avatar-size-limits/#__docusaurus_skipToContent_fallback)

On this page

Uploading a custom avatar is a great way to express yourself in VRChat. However, unoptimized avatars require more bandwidth, RAM, and VRAM, which decreases VRChat's performance.

This page explains VRChat's maximum **download size** and **uncompressed size** for avatars, and how to decrease your avatar's size.

Download size and uncompressed size[​](https://creators.vrchat.com/avatars/avatar-size-limits/#download-size-and-uncompressed-size "Direct link to Download size and uncompressed size")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here's how VRChat calculates your avatar's file size:

*   When you build and upload an avatar, the VRChat SDK packages it into a [Unity asset bundle](https://docs.unity3d.com/Manual/AssetBundlesIntro.html)
     and compresses it. The **download size** is the file size of your avatar's compressed asset bundle.
*   When VRChat downloads an avatar, VRChat decompresses the asset bundle. The **uncompressed size** is the uncompressed bundle size.

When calculating your avatar's size, VRChat does _not_ decompress individual assets! For example: If you set "Compression" to "High Quality" in a [texture's import settings](https://docs.unity3d.com/Manual/class-TextureImporter.html)
, it increases your avatar's download size **and** uncompressed size.

Avatar size limits[​](https://creators.vrchat.com/avatars/avatar-size-limits/#avatar-size-limits-1 "Direct link to Avatar size limits")

----------------------------------------------------------------------------------------------------------------------------------------

The maximum size limit depends on the platform you're playing on:

| Platform | Download Size | Uncompressed Size |
| --- | --- | --- |
| Android | 10 MB | 40 MB |
| PC  | 200 MB | 500 MB |

How to know if you are below these limits[​](https://creators.vrchat.com/avatars/avatar-size-limits/#how-to-know-if-you-are-below-these-limits "Direct link to How to know if you are below these limits")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Within the SDK it will inform you when making a build if your avatar is breaking either limit and prevent upload, post build it will remind you what the download / uncompressed size was along with the limit. When using Build & Test size limits are not enforced.

Keep your SDK up to date!

The android uncompressed size was not enforced in the SDK until [3.5.2](https://creators.vrchat.com/releases/release-3-5-2)
, ensure you are _at least_ on this version otherwise if you upload it will just fail server-side security checks! The reduced PC limits are enforced starting [3.7.0](https://creators.vrchat.com/releases/release-3-7-0)
, so similarly if uploading to PC ensure you are _at least_ on this version.

Within the client you can see both stats within the avatar details, either within the quick menu or main menu.

How to decrease your avatar's size[​](https://creators.vrchat.com/avatars/avatar-size-limits/#how-to-decrease-your-avatars-size "Direct link to How to decrease your avatar's size")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can reduce the size of your avatar by optimizing your assets:

*   Textures
    *   Reduce the max size in the [texture import settings](https://docs.unity3d.com/Manual/class-TextureImporter.html)
        .
    *   Use fewer texture files by deleting/merging textures or materials.
    *   Resize your texture to a [power of two](https://en.wikipedia.org/wiki/Power_of_two)
         (i.e. 512, 1024, 2048) or enable "Non-Power of 2" in the [texture import settings](https://docs.unity3d.com/Manual/class-TextureImporter.html)
         to improve Unity's texture compression.
*   Audio clips
    *   Shorten long clips.
    *   Reduce the quality of clips or enable "Force to Mono" in the [Audio Clip import settings](https://docs.unity3d.com/Manual/class-AudioClip.html)
        .
*   Animation clips
    *   Reduce the number of keyframes.
*   Blend shapes
    *   Remove unused blend shapes.
    *   Reduce the number of vertices affected by blend shapes, especially if your model has a high number of blend shapes.

You can find more optimization tips on the [Avatar Optimizing Tips page](https://creators.vrchat.com/avatars/avatar-optimizing-tips)
.

*   [Download size and uncompressed size](https://creators.vrchat.com/avatars/avatar-size-limits/#download-size-and-uncompressed-size)
    
*   [Avatar size limits](https://creators.vrchat.com/avatars/avatar-size-limits/#avatar-size-limits-1)
    
*   [How to know if you are below these limits](https://creators.vrchat.com/avatars/avatar-size-limits/#how-to-know-if-you-are-below-these-limits)
    
*   [How to decrease your avatar's size](https://creators.vrchat.com/avatars/avatar-size-limits/#how-to-decrease-your-avatars-size)