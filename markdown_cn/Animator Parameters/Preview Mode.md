# Preview Mode 预览模式
Preview Mode 是一个动画器参数 ，用于指示用户当前是否正在 VRChat 菜单中预览您的头像。您的 Animator Controller 可以使用此参数播放特定动画，以使您的头像预览看起来更具吸引力。

## Usage  用法
要为您的头像设置预览模式动画，请按照以下步骤作：

1. 打开现有的 Base （Locomotion） Animator Controller。
    - 如果您没有在 Avatar 描述符中设置 Base Layer，则可以复制 VRChat 提供的现有 Animator Controller。它位于`Packages/VRChat SDK Avatars/Samples/AV3 Demo Assets/Animation/Controllers/vrc_AvatarV3LocomotionLayer`下。将此动画器控制器复制到您的资源中，并将其分配给 Avatar Descriptor 的 Base 插槽。
![](https://creators.vrchat.com/assets/images/preview-mode-sample-layer-2cc3f72ad967690e0db7cad333e664e9.png)
2. 创建一个 Int 类型的新 Animator 参数，并将其命名为 PreviewMode。
![](https://creators.vrchat.com/assets/images/preview-mode-param-17d5d4adadfea566ae81a172a425343d.png)
3. 创建一个动画剪辑来容纳您的预览动画，选择一个名称（例如 PreviewOn），然后将其拖动到 Animator Controller 中。
4. 在 Standing locomotion 混合树（通常是 Default 状态，标记为橙色）到 PreviewOn 状态之间设置过渡，并将条件设置为“PreviewMode Equals 1”。取消选中 “Has Exit Time” 复选框。
![](https://creators.vrchat.com/assets/images/preview-mode-transition-in-6f15b86aa6ac4f2a98e7943e3e7d1b86.png)
5. 反向创建另一个从 PreviewOn 到 Standing 的过渡，并将条件设置为“PreviewMode 等于 0”。取消选中 “Has Exit Time” 复选框。
![alt text](https://creators.vrchat.com/assets/images/preview-mode-transition-out-2afc70f5b94c7f997193b7fdb1acf508.png)
6. 最终设置应如下所示：
![](https://creators.vrchat.com/assets/images/preview-mode-final-setup-4b269383bc105cfeb96106f3a464b090.png)
现在，将 Base Animator Controller 分配给 Avatar 的 Animator 组件的 Controller 插槽，并根据您的喜好设置动画。
![](https://creators.vrchat.com/assets/images/preview-mode-plug-in-animator-bf03af407c5a7711ba08cfa365b42c97.png)
#### 注意
请注意，在菜单中预览时，材质交换动画无法正常工作。但是，您仍然可以执行大多数其他作，例如切换对象或调整 BlendShape。

8. 完成后 - 您可以构建和测试您的头像。
![](https://creators.vrchat.com/assets/images/preview-mode-final-pose-2c25b4efa04b13f772b18d08e0ad3c25.png)
9. 当您在 Avatars 列表的 “Other” 部分中预览您的头像时，您应该会看到它以动画形式呈现您在 PreviewOn 动画剪辑中设置的姿势。
![](https://creators.vrchat.com/assets/images/preview-mode-in-game-view-a352865746b15ab1d7b3a48828ba9459.png)
您可以为预览模式使用不同类型的动画，因此请随意尝试。