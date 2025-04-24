# 约束
VRChat 提供了自定义的约束系统，允许你让头像上的骨骼相对于其他骨骼进行移动、旋转和缩放。

这个系统旨在作为 Unity 约束系统的一种一对一替代方案，并添加了一些针对 VRChat 头像常见用途的额外功能。如果你之前从未使用过约束，建议参考 [Unity 官方的约束系统文档](https://docs.unity3d.com/Manual/Constraints.html)进行了解。

在创建头像时，你应优先使用 VRChat 提供的约束系统，而不是 Unity 原生的。如果你的头像中包含 Unity 的原生约束，它们将在游戏中加载时自动转换为 VRChat 的约束。因此，直接使用 VRChat 的约束不仅能更准确地呈现头像在游戏中的实际表现，也能更真实地反映头像的性能评分。
## 约束类型
目前VRChat提供如下约束类型，与Unity内置的约束类型一一对应。
- [VRCAimConstraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-aim-constraint) - 将目标变换旋转，使其朝向源对象。你可以自定义哪个方向被视为前方。
- [VRCLookAtConstraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-look-at-constraint) - 一个简化的`AimConstraint`用于使Z轴正方向朝向源对象。
- [VRCParentConstraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-parent-constraint) - 移动并旋转目标变换，使其行为是源对象的子对象。
- [VRCPositionConstraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-position-constraint) - 改变目标对象的位置去匹配源对象的位置。
- [VRCRotationConstraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-rotation-constraint) - 改变目标对象的角度去匹配源对象的角度。
- [VRCScaleConstraint](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-scale-constraint) - 改变目标对象的大小去匹配源大小的位置。
访问这些链接来获取关于每种约束的更详细的信息

## 高级约束设置
`AdvancedSettings`折叠按钮包含VRChat约束提供的一些附加功能。
### 目标变换
`TargetTransform`（目标变换 ）设置允许您更改此约束所针对的变换。默认情况下，此设置为空，并且约束将应用于约束组件附加到的转换。请注意，无法使用动画更改此变换。
如果您想将头像上的所有约束组件保存在一个位置，或者如果您正在设置一个使用约束的系统，并且希望它可以在不同头像之间传输，这可能很有用。
### 在局部空间中求解
通常，约束是在世界空间中解算的，这意味着它将匹配其源的世界位置/旋转/缩放。如果启用了 Solve In Local Space 选项，则约束将改为匹配其源的局部位置/旋转/缩放。

这在为头像设置额外的假肢等情况下非常有用。例如，您可能有一串局部解决的旋转约束，这些约束引用头像真实手臂的每个骨骼，这会导致该链像真实手臂一样旋转。但是，这不仅限于旋转约束 - 所有类型都可以使用局部求解。

下面的视频以全局和局部求解的旋转约束之间的差异为例。在此剪辑中，中间箭头和向右箭头都使用旋转约束来匹配左箭头的旋转，其中中间箭头使用世界空间求解，右箭头使用局部空间求解。请注意，World resolved constraint 始终与世界空间中目标的旋转匹配。相反，局部解算的约束始终与目标相对于其父骨骼的朝向匹配。
[视频链接](https://youtu.be/6iBJ5QntrMU)
### 冻结到世界（Freeze To World）
启用 `Freeze To World` 时，约束将忽略其所有源，并将其目标变换锁定在世界空间中。变换的位置/旋转/缩放将保持不变，直到禁用`Freeze To World`。
此设置在打开和关闭动画时很好用。例如：
1. 为 Freeze To World （冻结到世界 ）设置[自定义菜单](https://creators.vrchat.com/avatars/expression-menu-and-controls/#types-of-controls) ，并默认将其禁用。
2. 在 Animation Clip 中启用`Freeze To World`时，变换将锁定在世界空间中。
3. 在 Animation Clip 中禁用`Freeze To World`时，变换将再次遵循约束的源。
这允许模型将对象放置在世界中的固定位置。当您走开时，该对象不会跟随您的头像。父约束最适合此情况，因为它们可以冻结目标转换的位置和旋转。但是，Freeze To World 也可用于所有其他约束类型。

Freeze To World （冻结到世界 ） 属性仅影响在 Constraint Settings （约束设置） 部分中选择为冻结的轴。如果要将对象完全固定在原地，必须冻结所有轴。否则，未冻结的轴将不会被更新，并且变换不会在世界空间中保持锁定状态。
##### 注意
启用`Freeze To World`与禁用约束组件不同！
- 禁用约束后，受影响的变换将停止在**局部**空间中移动。它仍然会跟随您的头像移动。
- 启用 Freeze To World （冻结到世界 ） 时，约束会主动在本地空间中移动变换，以防止其在世界空间中移动。
此外，默认情况下启用 Freeze To World 意味着约束将在加载时冻结在其相对于 Avatar 的起始位置/旋转/缩放处。不能保证将其放置在世界空间中的某个位置/旋转/缩放。
#### 解冻时重新烘焙偏移
启用 Rebake Offsets When Unfrozen 时，约束将通过禁用 Freeze To World 来重新计算其相对于其源的偏移，而不是保持其原始偏移的通常行为。

切换此值本身没有效果 - 它只确定禁用 Freeze To World 时应发生的情况。
## 性能
有两个与约束相关的性能类别。请参阅 [模型性能评级](https://creators.vrchat.com/avatars/avatar-performance-ranking-system#avatar-performance-ranks---value-maximums-per-rank) 页面，了解应用于每个平台的限制。
### 约束计数
约束计数相当简单 - 它是附加到头像的约束的总数，包括禁用的约束。这包括 VRChat 约束和 Unity 约束。在游戏中加载头像时，Unity 约束会自动转换为 VRChat 约束。

减少约束的总数可以提高头像的性能。
### 约束深度
当您在头像上设置约束链 （例如，沿额外肢体的旋转约束链） 时，需要按特定顺序一次评估一个约束，从链底部的约束一直到尖端的约束。如果链上有 3 个约束，则意味着链的约束深度为 3。头像的总体约束深度评级是整个头像中最长的依赖关系链。
可以通过减小最长约束链的长度来降低约束深度。请记住，此类别搜索最长的链，而不是所有链的总和 - 如果您的头像有多个臂的深度均为 3，则该头像的总分仍为 3（假设头像上其他任何地方都不再有链）。
约束深度很重要，因为它可以更好地估计头像上的约束将如何执行，而不仅仅是计算总共有多少个约束。通过组织约束以最小化它们之间的依赖关系，其中许多约束将能够同时运行，与约束必须一个接一个运行的情况相比，这会带来更好的性能。
##### 使用 Unity Constraints 的约束深度
只有当 avatar 仅使用 VRChat 约束时，才能准确计算 avatar 的约束深度。
如果您的头像包含任何 Unity 约束，则约束深度可能会被高估，因为该类别假定 Unity 约束一次只能运行一个。您可以使用 SDK 控制面板中的相关 Auto Fix 选项，将头像上的所有 Unity 约束转换为等效的 VRChat 约束。
## 使用技巧
如果 constraint 似乎不起作用，请确保它确实正在运行。
- 应启用`Is Active`选项。
- 组件本身应处于启用状态（其名称旁边的复选框），并应附加到 Avatar 上的活动游戏对象。
- 确保 Lock （ 锁定 ） 选项已启用。否则，约束将重新计算其 At Rest 和 Offset 值，而不是影响变换。
动画无法更改 Target Transform 引用。这是因为更改约束所针对的转换需要重新计算头像的性能评级。如果要更改约束的目标变换，可以尝试在多个不同的约束组件之间切换，每个组件具有不同的目标变换。
- 如果可以避免，请不要使用动画来更改约束引用的转换。对变换引用进行动画处理可能会导致头像出现性能问题，因为每次引用更改时，可能需要重新评估约束。
    - 这具体是指对约束对变换的引用进行动画处理 - 对变换的位置、旋转和缩放进行动画处理是可以的！
    - 由于技术限制，无法对单个源的转换引用进行动画处理。作为更简单的替代方法，您可以设置具有不同变换的多个源，并改为它们的权重设置动画。
## 编辑器工具信息
如果您是高级 Unity 用户，则可以使用 C# 编写自己的自定义编辑器工具，以便与约束转换器交互。
这些实用程序在此处仅简要概述。请参阅它们的内联文档，了解它们如何工作的完整描述。

## 转换方法
SDK 类`AvatarDynamicsSetup`包含 SDK 用于将 Unity 约束转换为等效 VRChat 约束的转换方法。以下约束转换方法公开供用户使用：
| 方法 (Method) | 描述 (Description) |
|---------------|---------------------|
| `ConvertUnityConstraintsAcrossGameObjects(List<GameObject> targetGameObjects)` | 将游戏对象列表上的 Unity 约束转换为 VRChat 约束。 |
| `ConvertUnityConstraintsAcrossAnimationClips(List<AnimationClip> targetAnimationClips)` | 修改 AnimationClip 列表，以便将其中针对 Unity 约束的任何轨道更新为以 VRChat 约束为目标。 |
| `DoConvertUnityConstraints(IConstraint[] unityConstraints, VRCAvatarDescriptor avatarDescriptor, bool convertReferencedAnimationClips)` | 将一组 Unity 约束转换为 VRChat 约束，可以选择包括任何引用的动画剪辑。这将立即运行，没有确认对话框。 |
| `RebindConstraintAnimationClip(AnimationClip clip, IConstraint oldConstraint)` | Attempts to modify a single animation clip to retarget tracks from Unity constraints to VRChat constraints, optionally limiting conversions to the given Unity constraint. <br>尝试修改单个动画剪辑，以将轨迹从 Unity 约束重定向到 VRChat 约束，并选择性地将转换限制为给定的 Unity 约束。 |
| `TryGetSubstituteAnimationBinding(Type unityConstraintType, string unityConstraintPropertyName, out Type vrcConstraintType, out string vrcConstraintPropertyName, out bool isArrayProperty)` |尝试将 Unity 约束属性名称和类型转换为等效的 VRChat 约束属性名称和类型。 |

为了补充上述方法，类 AvatarDynamicsSetup 还提供了一些委托（delegates），使你的工具可以控制转换器的行为。以下是可用的委托：
| 委托 | 描述 |
|------|------|
| `bool IsUnityConstraintAutoConverted(IConstraint constraint)` | 判断指定的 Unity 约束是否会在构建时由用户工具自动转换为 VRChat 约束。可用于屏蔽 SDK 通常提示用户进行转换的验证警告。 |
| `bool ConvertUnityConstraintsAcrossGameObjects(List<GameObject> gameObjects, bool isAutoFix)` | 将给定游戏对象列表中的所有 Unity 约束及相关动画剪辑转换为 VRChat 约束。若此操作是通过验证列表中的“自动修复”触发的，则 `isAutoFix` 为 `true`；若是通过菜单或自定义脚本触发，则为 `false`。返回 `true` 可阻止 SDK 内建的转换器运行。 |
| `bool ConvertUnityConstraintsAcrossAnimationClips(List<AnimationClip> animationClips)` | 将指定动画剪辑中所有引用 Unity 约束的轨道更新为引用 VRChat 约束。返回 `true` 可防止 SDK 内建的转换器介入执行。 |
