[Skip to main content](https://creators.vrchat.com/avatars/animator-parameters/preview-mode/#__docusaurus_skipToContent_fallback)

On this page

Preview Mode is an [animator parameter](https://creators.vrchat.com/avatars/animator-parameters/)
 that indicates whether the user is currently previewing your avatar in the VRChat menu. Your Animator Controller can use this parameter to play a specific animation to make your avatar preview look more appealing.

Usage[​](https://creators.vrchat.com/avatars/animator-parameters/preview-mode/#usage "Direct link to Usage")

-------------------------------------------------------------------------------------------------------------

To set up a preview mode animation for your avatar, follow the steps below:

1.  Open your existing Base (Locomotion) Animator Controller.
    *   If you do not have a Base layer set up in your Avatar descriptor, you can copy the existing Animator Controller provided by VRChat. It is located under `Packages/VRChat SDK Avatars/Samples/AV3 Demo Assets/Animation/Controllers/vrc_AvatarV3LocomotionLayer`. Copy this animator controller into your assets and assign it to the `Base` slot of your Avatar Descriptor.

![Base Layer Sample](https://creators.vrchat.com/assets/images/preview-mode-sample-layer-2cc3f72ad967690e0db7cad333e664e9.png)

2.  Create a new Animator parameter of type `Int` and name it `PreviewMode`.

![PreviewMode Parameter](https://creators.vrchat.com/assets/images/preview-mode-param-17d5d4adadfea566ae81a172a425343d.png)

3.  Create an Animation Clip to house your preview animation, choose a name (e.g., `PreviewOn`), and drag it into the Animator Controller.
4.  Set up a transition between the `Standing` locomotion blend tree (usually the Default state, marked in orange) to the `PreviewOn` state, and set the condition to "`PreviewMode` Equals 1". Uncheck the "Has Exit Time" checkbox.

![PreviewOn Transition](https://creators.vrchat.com/assets/images/preview-mode-transition-in-6f15b86aa6ac4f2a98e7943e3e7d1b86.png)

5.  Create another Transition in reverse from `PreviewOn` to `Standing` and set the condition to "`PreviewMode` equals 0". Uncheck the "Has Exit Time" checkbox.

![PreviewOff Transition](https://creators.vrchat.com/assets/images/preview-mode-transition-out-2afc70f5b94c7f997193b7fdb1acf508.png)

6.  The final setup should look something like this:

![PreviewMode Setup](https://creators.vrchat.com/assets/images/preview-mode-final-setup-4b269383bc105cfeb96106f3a464b090.png)

7.  Now assign your Base Animator Controller to the `Controller` slot of your Avatar's Animator component, and set up the animation to your preference.

![Plug In Animator](https://creators.vrchat.com/assets/images/preview-mode-plug-in-animator-bf03af407c5a7711ba08cfa365b42c97.png)

caution

Please note that Material swapping animations do not work correctly when previewed in the menu. However, you can still do most other things like toggling objects, or adjusting BlendShapes.

8.  When you're done - you can Build & Test your avatar.

![Pose Sample](https://creators.vrchat.com/assets/images/preview-mode-final-pose-2c25b4efa04b13f772b18d08e0ad3c25.png)

9.  When you preview your avatar in the "Other" section of the Avatars list - you should see it animate into the pose you set up in the `PreviewOn` Animation Clip.

![In Game View](https://creators.vrchat.com/assets/images/preview-mode-in-game-view-a352865746b15ab1d7b3a48828ba9459.png)

You can use different kinds of animations for the preview mode, so feel free to experiment.

*   [Usage](https://creators.vrchat.com/avatars/animator-parameters/preview-mode/#usage)