# Performance Ranks
Avatar Performance Ranking System 允许您通过分析用户 Avatar 上的组件来了解该用户的 Avatar 对性能的影响程度。您也可以在自己身上使用它来查看您的头像的性能如何。

提供此系统是为了告知用户其 Avatar 上性能最重的组件是什么，并就优化其 Avatar 时应注意的事项提供基本建议。

它还用于驱动 [最低显示性能等级](https://creators.vrchat.com/avatars/avatar-performance-ranking-system#minimum-displayed-performance-rank-on-pc) 系统，这是用户根据其 Performance Rank 决定他们希望显示哪些头像的一种方式。

该系统并不是关于头像性能的最终解决方案 ，而是一个很好的通用指南，可以指示头像是否需要更多的工作才能达到性能。
##### 性能等级不是最终目的
尽管性能等级系统会尽最大努力判断头像性能的“最坏情况”，但有很多方法可以让优化良好的头像显示为非常差，并保持优秀的FPS。

对于技术倾向者：Performance Rank 系统基于对 Avatar 属性的静态分析，而不考虑动画器、着色器、纹理分辨率、像素光和更多因素等因素。 然而 ，它往往提供了一个很好的试金石，可以在 95% 的时间内检测有问题的头像！

## 简短版本
争取 Good 等级。 如果你不能达到这个目标，Medium 就完全没问题。

创建头像已经很困难了，创建优化的头像更是难。这是一项需要很长时间才能培养的技能！

请记住，如果您以 Very Poor 头像出现，VRChat 中的许多事件、群组和地点可能会要求您更改头像。因此，即使您选择在小型实例中与朋友一起使用 Very Poor 头像，也请确保您也有一个用于更多人的实例的头像。

您的头像会影响其他人的帧率，因此请注意您的选择如何影响其他人的体验。否则，他们可能会看到你的备用模型(而不是你)！
## 性能等级图标
当您打开快捷菜单时，您会看到图标出现在用户的铭牌顶部。
等级如下：
| 图标 | 性能等级     | 描述                                                                 |
|------|--------------|----------------------------------------------------------------------|
| ![](data:image/png;base64,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) | 非常好       | 这是你能得到的最好的！真不错！                            |
| ![](https://creators.vrchat.com/assets/images/good-12ca687123e41921dcfbbde51814362d.png) | 好           | 够好！一个很好的目标。                                              |
| ![](https://creators.vrchat.com/assets/images/medium-29559721165021dfafaef1c7dece9bab.png) | 中等         | 不要被这个名字骗了，Medium 已经足够好了。如果你在这里并且不想再往上走，那很好。 |
| ![](https://creators.vrchat.com/assets/images/poor-8ffee00013eff2bb8073c3f37a9119fa.png) | 差           | 可能需要一些工作。                                                 |
| ![](https://creators.vrchat.com/assets/images/very-poor-ad76572d037c51878b00b3d7ed492bb0.png) | 非常差       | 此头像存在一些严重的性能问题。由于此等级是无限的，因此您的性能很可能会因此头像可见而受到影响。 |

## 查看详细的 Avatar 统计数据

如果您在打开快捷菜单的情况下点击用户，您会注意到左侧有一个新的`查看模型详情`按钮，显示该用户的性能等级图标。
![](https://creators.vrchat.com/assets/images/view-avatar-details-qm-b2d08ac3fe261fcb11e247e5f8eb0510.png)
如果您单击此图标，则可以查看该头像的详情。您可以通过转到模型菜单，单击您的一个模型，然后单击屏幕左下角的模型详情按钮来访问您自己的头像。
![](https://creators.vrchat.com/assets/images/view-avatar-details-preview-6927ecc7999a2f7bbb0e9a5880ff020e.png)
当您单击模型详情按钮时，您将弹出一个窗口，其中包含您正在查看的模型或您自己的模型的详细信息（如果您单击 Avatar 选项卡中的按钮）。
![](https://creators.vrchat.com/assets/images/avatar-perormance-breakdown-4db75b7acd4f77567101100469d76cd2.gif)
文本的颜色与特定统计信息“拖动”等级下降到的等级相匹配。

您还将看到 “Original” 和 “Perf Filtered” 行形式的 “before and after”。如果您使用的是 最低显示性能等级 系统，则可以查看系统删除组件之前和之后的统计信息。如果 最低显示性能等级 系统出于性能原因阻止了虚拟形象，您将只能看到原始统计数据。

在上面给出的示例中，Lights 和 Particle Systems 由于超出定义的限制而被禁用。由于 Particle Systems 每个系统至少使用一种材质，因此也会从预先过滤的 Avatar 中减去 Particle Systems 中的材质计数。

您还可以看到我们链接到我们的文档 ，特别是我们的 [Avatar 优化技巧]() 。

## Avatar Performance Ranking 统计数据
以下是系统查看的所有统计数据及其描述的列表。
加粗的指标如果超过“最低显示性能等级”，将导致该头像被完全屏蔽。
如果是其他非加粗指标（边界除外）超过该等级，则头像只会被部分屏蔽，相关的组件将被移除，但头像本身仍会显示。

例如，将`最低显示性能等级`设置为`差`时，将显示具有9个`Trail Renderer`（差）的头像，并删除其所有 `Trail Renderer`。请参阅[最低显示性能等级]()以了解更多信息。
| Avatar Quality | Quality Description |
|----------------|---------------------|
| 三角形数（Triangles） | 模型的三角形数量。（过去曾被误称为“多边形数”。） |
| 边界大小（Bounds Size） | 头像的整体尺寸。如果这个数值非常大，该用户可能在头像上使用了某个不一直显示的大型动画。<br>**重要说明：即使边界大小低于“最低显示性能等级”设置，也不会导致头像被屏蔽。** |
| 纹理内存（Texture Memory） | 头像纹理所占用的内存估算值。这些纹理同时占用系统内存和显卡内存。 |
| 蒙皮网格数（Skinned Meshes） | 头像上 Skinned Mesh Renderer 组件的数量。 |
| 基础网格数（Basic Meshes） | 头像上非蒙皮的 Mesh Renderer 组件的数量。 |
| 材质槽数（Material Slots） | 头像的材质槽数量。材质槽是你为网格分配材质的位置。该项影响子网格（Submesh）的创建，从而带来更多绘制调用。<br>请注意：粒子系统使用一个材质槽，带轨迹的粒子系统使用两个，线条渲染器使用一个材质槽。 |
| 物理骨骼组件数（PhysBones Components） | 头像上的 PhysBone 组件数量。 |
| 受物理骨骼影响的变换数（PhysBones Affected Transforms） | 头像上被 PhysBone 组件影响的变换总数。 |
| 物理骨骼碰撞器数（PhysBones Colliders） | 头像上 PhysBone 碰撞器脚本的数量。 |
| 物理骨骼碰撞检查次数（PhysBones Collision Check Count） | 每个碰撞器可以影响的 PhysBone 变换数总和。由于一个变换可能被多个碰撞器影响，因此可能被多次计数。 |
| 动态接触点数（Avatar Dynamics Contacts） | 头像上的 Avatar Dynamics 接触点数量。不包括设置为“仅本地”过滤的接收器。 |
| 约束数量（Constraint Count） | 头像上的 VRChat 约束与 Unity 约束的总数。[点击此处了解详细信息] |
| 约束深度（Constraint Depth） | 头像上所有约束中依赖链最深的深度。[点击此处了解详细信息] |
| 动画器数量（Animators） | 头像上的 Animator 数量。**重要说明：由于根 Animator 会被计入，因此该值最少为 1。**这意味着若要达到“非常好”评级，不能再额外添加 Animator。 |
| 骨骼数（Bones） | 头像绑定骨骼的数量。 |
| 光源数（Lights） | 头像上的 Light 组件数量。 |
| 粒子系统数（Particle Systems） | 头像上的粒子系统组件数量。 |
| 总粒子数量（Total Particles Active） | 头像所有粒子系统的最大粒子数量（maxParticles）总和。 |
| 网格粒子三角形数（Mesh Particle Active Polys） | 活动中由粒子系统发射的网格粒子的三角形总数。换句话说，是 maxEmission × meshParticleVerts。 |
| 粒子轨迹启用（Particle Trails Enabled） | 如果头像上的任一粒子系统启用了粒子轨迹，此项为 True。 |
| 粒子碰撞启用（Particle Collision Enabled） | 如果头像上的任一粒子系统启用了粒子碰撞，此项为 True。 |
| 轨迹渲染器（Trail Renderers） | 头像上的 Trail Renderer 数量。 |
| 线条渲染器（Line Renderers） | 头像上的 Line Renderer 数量。 |
| 布料组件（Cloths） | 头像上的 Cloth 组件总数。 |
## 模型性能等级 - 每项的最大值
下面，您将找到每个性能等级的限制。如果您在任何类别中超过这些数字，您将被降低到下一个等级。
例如（在 PC 上），如果您的头像有 2 个蒙皮网格，则您的头像将被评为“良好”，因为这低于了“优秀”的评级，但不会超过“良好”的评级。
#### 所有游戏对象和组件都将被计数！
所有游戏对象和组件（ 包括当前禁用的游戏对象和组件）都计入 Avatar 性能等级。
#### 网格读写禁用说明
如果您在头像上的任何网格（包括粒子系统）上禁用网格读/写，则“三角形”计数将显示“网格读/写已禁用”，并且头像的性能等级将立即降级为“非常差”，而不管头像上的实际三角形数量如何。

SDK 会警告您此问题，并要求您在上传之前修复它。
## PC 限制
| Avatar Quality（头像质量） | 非常好 | 好 | 中等 | 差 |
|---------------------------|--------|----|------|----|
| 三角形数 | 32,000 | 70,000 | 70,000 | 70,000 |
| 边界大小 | 2.5m x 2.5m x 2.5m | 4m x 4m x 4m | 5m x 6m x 5m | 5m x 6m x 5m |
| 纹理内存 | 40 MB | 75 MB | 110 MB | 150 MB |
| 蒙皮网格数 | 1 | 2 | 8 | 16 |
| 基础网格数 | 4 | 8 | 16 | 24 |
| 材质槽数 | 4 | 8 | 16 | 32 |
| 物理骨骼组件数 | 4 | 8 | 16 | 32 |
| 受物理骨骼影响的变换数 | 16 | 64 | 128 | 256 |
| 物理骨骼碰撞器数 | 4 | 8 | 16 | 32 |
| 物理骨骼碰撞检查次数 | 32 | 128 | 256 | 512 |
| 动态接触点数 | 8 | 16 | 24 | 32 |
| 约束数量 | 100 | 250 | 300 | 350 |
| 约束深度 | 20 | 50 | 80 | 100 |
| 动画器数量 | 1 | 4 | 16 | 32 |
| 骨骼数 | 75 | 150 | 256 | 400 |
| 光源数 | 0 | 0 | 0 | 1 |
| 粒子系统数 | 0 | 4 | 8 | 16 |
| 总粒子数量 | 0 | 300 | 1000 | 2500 |
| 网格粒子三角形数 | 0 | 1000 | 2000 | 5000 |
| 粒子轨迹启用 | 否 | 否 | 是 | 是 |
| 粒子碰撞启用 | 否 | 否 | 是 | 是 |
| 轨迹渲染器数 | 1 | 2 | 4 | 8 |
| 线条渲染器数 | 1 | 2 | 4 | 8 |
| 布料组件数 | 0 | 1 | 1 | 1 |
| 布料顶点总数 | 0 | 50 | 100 | 200 |
| 物理碰撞器数 | 0 | 1 | 8 | 8 |
| 物理刚体数 | 0 | 1 | 8 | 8 |
| 音频源数 | 1 | 4 | 8 | 8 |
上表描述了确定的PC模型性能等级
### PC 默认性能等级盾
在 PC 上，默认的`最低显示性能等级`级别为非常差。这意味着默认情况下，用户可以看到大多数头像。如果用户启用了`最低显示性能等级`系统，则他们可以选择隐藏性能较差的头像。
但是，如果您的头像极度未优化，VRChat 可能会阻止您使用它。您可以通过提高其性能等级来解决此问题，确保其不超过 VRChat 的 avatar 大小限制 ，然后重新上传 avatar。

## 移动设备限制
Android 和 iOS（手机、平板电脑和 Meta Quest）上的 VRChat 比 PC 上的 VRChat 具有更严格的限制。
下表描述了移动头像获得特定性能等级的要求：
| Avatar Quality（头像质量） | 非常好 | 好 | 中等 | 差 |
|---------------------------|--------|----|------|----|
| 三角形数 | 7,500 | 10,000 | 15,000 | 20,000 |
| 边界大小 | 2.5m x 2.5m x 2.5m | 4m x 4m x 4m | 5m x 6m x 5m | 5m x 6m x 5m |
| 纹理内存 | 10 MB | 18 MB | 25 MB | 40 MB |
| 蒙皮网格数 | 1 | 1 | 2 | 2 |
| 基础网格数 | 1 | 1 | 2 | 2 |
| 材质槽数 | 1 | 1 | 2 | 4 |
| 动画器数量 | 1 | 1 | 1 | 2 |
| 骨骼数 | 75 | 90 | 150 | 150 |
| 物理骨骼组件数 | 0 | 4 | 6 | 8 |
| 受物理骨骼影响的变换数 | 0 | 16 | 32 | 64 |
| 物理骨骼碰撞器数 | 0 | 4 | 8 | 16 |
| 物理骨骼碰撞检查次数 | 0 | 16 | 32 | 64 |
| 动态接触点数 | 2 | 4 | 8 | 16 |
| 约束数量 | 30 | 60 | 120 | 150 |
| 约束深度 | 5 | 15 | 35 | 50 |
| 粒子系统数 | 0 | 0 | 0 | 2 |
| 总粒子数量 | 0 | 0 | 0 | 200 |
| 网格粒子三角形数 | 0 | 0 | 0 | 400 |
| 粒子轨迹启用 | 否 | 否 | 否 | 是 |
| 粒子碰撞启用 | 否 | 否 | 否 | 是 |
| 轨迹渲染器数 | 0 | 0 | 0 | 1 |
| 线条渲染器数 | 0 | 0 | 0 | 1 |

### 移动设备默认性能等级盾
在移动设备上，`最低显示性能等级`默认为“Medium”。这意味着用户无法看到任何等级为“差”或“非常差”的头像。
用户可以将他们的`最低显示性能等级`级别设置为 “Poor”，以允许他们看到 “Poor” 头像。但是，他们无法将其`最低显示性能等级`级别设置为 “Very Poor”。
例如，如果移动头像超过 20,000 个三角形，则为“非常差”，用户无法在 VRChat 中看到它。但是，用户可以通过选择用户并单击 “Show Avatar” 来强制显示 “Very Poor” 头像。
#### warning  警告
将来，VRChat 可能会删除“非常差”的移动头像，并删除对“非常差”的移动头像使用“显示头像”的功能。在创建移动头像时，请记住这一点。
### 移动模型的组件限制
某些 Avatar 组件仅限于移动 Avatar。您不能超过以下限制：
- 8 个 PhysBone 组件
- 64 个受影响的 PhysBones 变换
- 16 个 PhysBones 碰撞器
- 64 个 PhysBones 碰撞器检查
- 16 Avatar Dynamics 联系
- 150 个约束组件
- 50 的最大约束深度
您无法通过使用 “Show Avatar” 来绕过上述限制。如果移动头像超过限制，则即使您启用了“Show Avatar”，也会从 VRChat 中的头像中删除所有受限的头像组件。
### 移动删除的组件
以下组件在移动设备上处于禁用状态，因为它们永远不会显示在头像上：
- Lights：光源
- Cloths：布料
- Total Cloth Vertices：布料顶点总数
- Physics Colliders：物理碰撞器
- Physics Rigidbodies：物理刚体
- Audio Sources：音频源
这些值可能仍显示在 VRChat 的头像详细信息屏幕中，但它们始终为零。
## 最低显示性能等级
您可以选择根据虚拟形象性能等级来管理虚拟形象。此选项位于性能选项菜单中，可通过主菜单中安全选项卡右上角的按钮访问。
当您在 VRChat 的菜单中选择性能等级时，所有低于该级别的 Avatar 都将按照如下所述管理其组件/显示。
| 参数 | 描述 |
|------|------|
| 三角形数 | 头像被替换为备用头像 |
| 边界大小 | 无变化 |
| 纹理内存 | 头像被替换为备用头像 |
| 蒙皮网格 | 头像被替换为备用头像 |
| 基础网格 | 头像被替换为备用头像 |
| 材质槽数 | 头像被替换为备用头像 |
| 物理骨骼组件、变换、碰撞器、碰撞检查次数或接触点 | 所有 PhysBone、PhysBone 碰撞器和接触组件将被移除 |
| 约束数量或深度 | 所有约束组件将被移除 |
| 动画器 | 所有动画器（除根动画器外）将被移除 |
| 骨骼 | 头像被替换为备用头像 |
| 光源 | 所有光源将被移除 |
| 粒子系统 | 所有粒子系统将被移除 |
| 活动粒子总数 | 所有粒子系统将被移除 |
| 网格粒子三角形数 | 所有粒子系统将被移除 |
| 启用粒子轨迹 | 所有粒子系统将被移除 |
| 启用粒子碰撞 | 所有粒子系统将被移除 |
| 轨迹渲染器 | 所有轨迹渲染器将被移除 |
| 线条渲染器 | 所有线条渲染器将被移除 |
| 布料组件 | 所有布料组件将被移除 |
| 布料顶点总数 | 所有布料组件将被移除 |
| 物理碰撞器 | 所有物理碰撞器将被移除 |
| 物理刚体 | 所有物理刚体将被移除 |
| 音频源 | 所有音频源将被移除 |
### PC上的最低显示性能等级
在 PC 上，最低显示性能等级默认设置为“非常差”。这意味着，默认情况下，由于 PC 上的性能原因，任何头像的组件或显示都不会受到影响。如果您想更改此设置，您可以在 “Medium”（中等）、“Poor”（差）或 “Very Poor”（非常差）选项之间进行选择。
### 移动设备上的最低显示性能等级
在移动设备的 VRChat 上，Avatar Performance Rank Block 默认设置为“Medium”。您可以选择将其更改为 “Poor” 以查看该等级的头像，但您的性能可能会因此受到影响。

您无法在移动设备上禁用低显示性能等级系统。换言之，等级为“非常差”的头像将始终具有其移动设备的显示托管 VRChat，并且可能根本不显示。

无论您选择哪种设置，如果在移动设备上超出 Avatar Dynamics 组件限制，则所有这些组件都将被删除。简而言之，移动头像上的 Avatar Dynamics 组件存在硬上限。

### 覆盖单个头像

**非常差的头像功能的“显示头像”功能将来可能会被删除，并且非常差的头像可能会从 Android 和 iOS 中完全删除。** 在移动设备上为 VRChat 创建头像时，请记住这一点。

您可以通过在要显示的每个用户上选择“Show Avatar”（显示头像）来选择覆盖整个系统（和安全系统）。

## 脚注

Bounds Size （边界大小） 由头像上所有组件的最大大小决定。Trail 和 Line Renderer 不计入此计算。

如果模型在移动设备上超过了Very Poor等级，则无论头像的当前“Show Avatar”状态如何，都将删除所有与Avatar Dynamics相关的组件。