# 允许的模型组件

您可以通过向头像[添加组件](https://docs.unity3d.com/2022.3/Documentation/Manual/UsingComponents.html)来向头像添加功能。但是，并非所有组件都可以在 VRChat 中使用。
- 以下列表中的任何组件都可以在 VRChat 中使用。
- 其他组件或自定义脚本在 VRChat 中不起作用，并且可能会阻止您上传头像。

#### 信息
VRChat 的 Android 版本还有其他限制 。

VRChat
- VRCAvatarDescriptor
- VRCConstraint
- VRCContactReceiver
- VRCContactSender
- VRCHeadChop
- VRCIKFollower - 已弃用！您应该改用 VRChat 约束 。
- VRCPhysBone
- VRCPhysBoneCollider
- VRCPipelineManager
- VRCSpatialAudioSource
- VRCStation

Unity

- AimConstraint
- Animation
- Animator
- AudioSource
- Camera (See notes below)
- Cloth
- Collider
- FlareLayer
- Joints
- Light
- LineRenderer
- LookAtConstraint
- MeshFilter
- MeshRenderer
- ParentConstraint
- ParticleSystemRenderer
- ParticleSystem
- PositionConstraint
- Rigidbody
- RotationConstraint
- ScaleConstraint
- SkinnedMeshRenderer
- TrailRenderer
- Transform

## 头像上的摄像机
对于本地用户使用的头像，Camera 组件已完全列入白名单。对于远程用户，以下规则适用：
- 在所有情况下，加载头像时，远程用户的 Camera 组件都会被禁用。
    - 您可以使用动画来启用 Camera （摄像机） 组件。
- 如果本地用户和远端用户是好友，则不会删除 Camera 组件。
    - 请注意，与用户成为好友不会自动重新加载其头像。
- 如果本地用户在 VRChat 的快捷菜单中为远程用户选择了“显示头像”，则不会删除摄像机组件。
- 如果以上两种情况都不成立，则 Camera 组件将被删除且无法启用。

## Root Motion (FinalIK)  根运动 （FinalIK）
VRChat 对其 FinalIK 的实现进行了高度修改。因此，这些组件可能无法按文档所述工作。

我们不直接支持或测试头像上的自定义 FinalIK 实现。但是，它们应该可以正常工作，如果我们必须故意破坏其中的一个或多个，我们将尽最大努力通知创作者。

如果您发现错误，请[告诉我们](https://feedback.vrchat.com/)。

| 英文模块名             | 中文名               | 描述 |
|------------------------|----------------------|------|
| Aim IK                 | 瞄准IK               | 控制角色或物体朝向目标，常用于武器瞄准或视线控制。 |
| Biped IK               | 双足IK               | 控制双足角色的基本IK，包括上下肢与头部的控制。 |
| CCDIK                  | CCD反向运动学        | 使用循环坐标下降法的IK解算器，适合多关节链条控制。 |
| FABRIK                 | FABRIK反向运动学     | 使用向后向前迭代的IK算法，解算速度快，适合复杂骨骼。 |
| Full Body Biped IK     | 全身双足IK           | 高级全身IK系统，支持自然站姿、动作过渡与全身调整。 |
| Grounder               | 地面贴合系统         | 让角色的脚部自然贴合不平地形，避免“漂浮”或“穿插”。 |
| Limb IK                | 四肢IK               | 控制手臂或腿部末端的位置，适合局部动作控制。 |
| Rotation Limits        | 旋转限制             | 限制关节的旋转角度，避免不自然的弯曲或穿模。 |
| Shoulder Rotator       | 肩部旋转器           | 用于更自然地控制肩膀动作，尤其在上肢动作中很重要。 |
| Twist Relaxer          | 扭转缓解器           | 减少骨骼链条中的扭转积累，提升自然度和稳定性。 |
| VRIK                   | 虚拟现实IK（VRIK）   | 为VR专门设计的全身IK系统，支持实时手柄和头部跟踪。 |

## DynamicBone
对 Dynamic Bone 的支持已弃用。您应该改用 PhysBones。

- DynamicBone  DynamicBone （动态骨骼）
- DynamicBoneCollider （动态骨骼碰撞器）

### 脚注
1. 在人形头像上使用此脚本会破坏它。↩
