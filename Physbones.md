# Physbones
PhysBones 是一组组件，可让您向头像添加辅助运动，从而允许您为头发、尾巴、耳朵、衣服等内容添加运动！很好地使用这些会让你的头像看起来更有活力和真实。

PhysBones 是 Dynamic Bones 的替代品。虽然这两个系统有很多共同的概念，但与 PhysBones 存在一些重大差异，因此并非所有头像都可以直接转换为 VRChat 的系统。

有关如何使用 Physbones 的示例，请参阅 SDK 中的 `VRCSDK\Examples3\Dynamics\Robot Avatar`。
## VRCPhysBone 骨骼
定义要使用 PhysBones 设置动画的骨骼链。这些可用于模拟软体和辅助运动，如头发、尾巴、松软的耳朵等等！它有许多配置选项，并且可以通过多种方式进行设置。

此外，您和其他人都可以与 PhysBones 进行交互！如果您已向其他用户授予权限，则其他人可以获取在您的头像上设置的 PhysBones，并在按住 PhysBone 的同时扣动扳机，以“摆姿势”并将其保持在原位。您还可以在配置中禁用此功能，以允许摆姿势、不允许抓取或根本不允许碰撞。

虽然不是这样设计的，但 PhysBones 也可以作为合理的布料替代品，直到我们实现自己的布料组件。
![alt text](https://creators.vrchat.com/assets/images/physbones-ca9ee06-2022-05-04_18-23-09_Unity-b5504c435b24026584dcf8bd452e79ec.png)
### Versions  版本
现在，您可以选择要直接在组件上使用的 VRCPhysBone 组件版本。默认情况下，创建新组件时将选择最新版本。现有头像将继续使用其先前版本，除非手动更新并重新上传。
Version 1.0:  版本 1.0：

- VRCPhysBone 组件的基本版本。

Version 1.1:  版本 1.1：

- Squishy Bones 更新，允许骨骼挤压和长度受运动影响。

- 重力现在充当骨骼在静止时旋转距离的比率。骨骼需要正 Pull 才能沿重力方向移动。

- 刚度现在充当一个比率，使骨骼保持其先前的方向。

### Transforms  变换
- Root Transform (根变换) - 此组件开始的变换。如果留空，则假定我们从此游戏对象开始。 
- Ignore Transforms （忽略变换） - 不应受此组件影响的被忽略变换的列表。忽略的转换会自动包含该转换的任何子项。
- Endpoint Position - 用于在链的每个端点处创建其他骨骼的向量。仅当值为非零时使用。通常，您需要沿 +Y 增加此值，这将指向骨骼的 “上方”。
- Multi-Child Type - 当存在多个骨骼链时根骨骼的行为。这有三种模式：

    - 如果设置为 Ignore，根骨骼不会移动，并且会忽略物理特性。对于头发等内容很有用，因为您可以在根上使用一个 Physbone 组件来影响所有头发骨骼！

    - 如果设置为 First ，根骨骼将与层级中的第一个骨骼链形成一个连续链。所有其他链仍然有效，但它们将从每个相应链中的第一个骨骼开始，而不是像第一个链那样从根开始。

    - 如果设置为 Average，根骨骼的运动将是所有其他链的平均值。这意味着每条链的底部将能够移动。
#### 注意
如果您使用的是单个根骨骼，或者具有多个子骨骼（但没有孙子骨骼）的单个根骨骼， 则必须定义一个端点位置！

例如，如果将 PhysBone 组件放在下面的任何 RootBone 上， 则必须定义 Endpoint Position 才能使 PhysBones 正常工作。这与 Dynamic Bones有区别。

单根骨骼
- 根骨骼

多个子骨骼，一个根骨骼
- 根骨骼
- 子骨骼1
- 子骨骼2
- 子骨骼3
- 子骨骼4

您还可以通过在每个 ChildBone 后添加 “end bones” 来解决此问题，但这涉及编辑骨架。

### Force 力
Integration Type 定义用于模拟受此组件影响的任何变换的运动的数学类型。根据您选择的选项，Forces （力） 部分中的可用选项将发生变化。您可以在以下两种方式之间进行选择：
- Simplified(简化) - 是一种更稳定的方法，感觉有点慢，对外部冲动和力的反应性更小，但更容易配置。
- Advanced 不太稳定，但允许更复杂的配置，并且往往对外部脉冲和力更敏感。
使用默认设置时，这两种模式的行为非常相似，但调整设置并对其进行测试将很快分清它们的不同。
##### Info
下面的大多数（如果不是全部）选项都允许通过按滑块旁边的 C 按钮来 Curves。曲线允许您调整骨骼链长度上的值，并允许在骨骼链中进行非常复杂的设置！
事实上，大多数 PhysBones 设置都允许使用 Curves（曲线）！了解如何使用它们，您的 PhysBones 看起来会很棒！
![](https://creators.vrchat.com/assets/images/physbones-054e326-2022-04-19_11-32-12_Unity-b113a7a250a3dd1674a328f93e47f6ea.png)
- Pull - 用于将骨骼返回到其静止位置的力的大小。
- Spring - 骨骼在尝试到达其静止位置时将会摆动的量。仅在 Simplified Integration Type 中可用。
- Momentum - 骨骼在尝试到达其静止位置时将摆动的量。仅在 Advanced Integration Type 中可用。尽管描述相同，但效果与 Spring 略有不同。
- Stiffness （刚度） - 骨骼尝试保持在其静止位置的量。仅在 Advanced Integration Type 中可用。
- Gravity - 应用到骨骼上的重力量。正值向下拉骨头，负值向上拉动。
- Gravity Falloff - 仅当 Gravity （重力） 不为零时可用。它控制在静止位置时移除的 Gravity 量。值为 1.0 表示 Gravity （重力） 在处于静止位置时完全不会影响骨骼。这样，当骨骼从初始位置旋转时，就可以获得重力效果，而不会影响骨骼的静止状态。
    - 使用 Gravity Falloff 参数的一种方法是，如果头发建模为正常站立时已处于所需的姿势，则可以使用 1.0 重力衰减。这样，当你站在那里时，重力不会影响你，你的头发会停留在建模的位置。如果你的头发是笔直向外 45 度建模的，并且你希望它受重力的影响足以产生漂亮的曲线（但不是完全笔直或完全笔直向下），滑块允许你摆弄它并使用 0.5-0.8 来只有一小部分重力静止姿势。
- Immobile Type 改变了 Immobile 的工作方式。
    - 如果设置为 All Motion （所有运动）， 则 Immobile 会减少从根变换的父级计算的任何运动。这是新 PhysBones 和转换后的 Dynamic Bones 的默认模式 。在此模式下，场景空间或游戏空间中的所有 PhysBone 移动都将受到 Immobile 因子的抑制。
    - 如果设置为 World （Experimental）（世界（实验性）），Immobile 仅从场景根变换的引用中否定位置移动。通过动画或 IK 进行的运动仍会正常影响骨骼。 此模式将来可能会更改！这意味着在游戏空间中四处移动仍会影响 PhysBones 的正常移动，但移动（推动纵杆移动）的移动会因 Immobile 因素而受阻。
## Limits  限制
设置 Limits 允许您限制 PhysBone 链可以移动的量。当您不希望头发夹入头部时，这非常有用，并且比碰撞器的性能要高得多 ！

此外，在为 Limits （限制） 配置选项时，当您选择了 PhysBone 链时，这些限制的可视化将显示在 Scene （场景） 视图中。这些在微调 Limits 时非常有用！

Limit Type 有几种模式。它们都允许根据 Pitch、Yaw 和 Roll 分别交替地沿 X、Y 和 Z 轴调整 Rotation。
- None - 表示在此骨骼链上不启用限制。没有配置选项。
- Angle 角度
![alt text](https://creators.vrchat.com/assets/images/physbones-b7abe1f-2022-04-19_11-49-26_Unity-1019f682db46ee4458a8fc00f1275f16.png)
Angle （角度 ） 表示骨骼链将被限制为某个 Max Angle（最大角度 ），以 Rotation 定义的轴为中心。这在 Scene 视图中可视化为 Cone。
- Hinge  铰链
![](https://creators.vrchat.com/assets/images/physbones-b7723cc-2022-04-19_11-50-04_Unity-9f8c43ea4a22b77769d81a99134bc9d5.png)
Hinge 意味着骨骼链将限制为沿 Rotation 定义的平面的某个 Max Angle 。这被可视化为一个圆圈的切片，类似于比萨饼或馅饼。
- Polar  极
![](https://creators.vrchat.com/assets/images/physbones-824db3c-2022-04-19_11-51-22_Unity-954792a12c7d0a047b794e74b716be50.gif)

Polar 稍微复杂一些。如果选取一个 Hinge 并将其扫过偏航 （Yaw） 一定量，则会得到极坐标中的球体段。您可以配置 Max Pitch 和 Max Yaw 来调整分段的大小，并使用 Rotation 来定义该分段在球体上的位置。Polar 的可视化特别有用。

不要过度使用 Polar 限制，因为它们的性能成本较高。使用大量 （挥手：超过 64） 可能会导致一些问题。如果你的 Max Pitch 和 Max Yaw 值相似或相同，则 Angle 限制就足够了，并且性能成本较低。
### Collision  碰撞
- Radius - 每个骨骼周围的碰撞半径（以米为单位）。用于碰撞和抓取。
- Allow Collision （允许碰撞 ） - 允许与此组件上指定的碰撞体以外的碰撞体发生碰撞。目前，唯一的其他碰撞体是每个玩家的手和手指，由其头像定义。
- Colliders - 专门与这些骨骼碰撞的碰撞体列表。
### Stretch & Squish  拉伸 & 挤压
- Stretch Motion - 运动将影响骨骼的拉伸/挤压的量。 值为零意味着骨骼只会因抓取或碰撞而拉伸/挤压。
- Max Stretch - 骨骼可以拉伸的最大量。 该值是原始骨骼长度的倍数。 注： [最大边界](https://creators.vrchat.com/avatars/avatar-dynamics/physbones#maximum-bounds)
- Max Squish - 骨骼可以收缩的最大数量。 该值是原始骨骼长度的倍数。
### Grab & Pose  抓取和摆姿势
- Allow Grabbing - 允许玩家抓取骨骼。
- Allow Poseing（允许摆姿势 ） - 允许玩家在抓取骨骼后摆出骨骼的姿势。
- Grab Movement - 控制抓取的骨骼的移动方式。零值会导致骨骼使用拉力和弹簧到达抓取位置。值为 1 会导致骨骼立即移动到抓取位置。
- Snap To Hand - 当骨骼被抓取时，它将对齐到抓取它的骨骼。
### Options  选项
