# Animator Parameters
#### 注意
本文档需要了解 Unity 的 Animator 控制器和动画参数 。

您可以在头像的[Playable Layers](https://creators.vrchat.com/avatars/playable-layers/)中使用`Animator`参数来控制或影响头像的`Animator`状态。
- 一些参数[内置于 VRChat 中](https://creators.vrchat.com/avatars/animator-parameters/#built-in-parameters) ，您可以在任何 Playable Layer 上使用它们。
- 您还可以创建自己的[自定义参数](https://creators.vrchat.com/avatars/animator-parameters/#custom-parameters) ，这需要创建 [Expression Parameters](https://creators.vrchat.com/avatars/animator-parameters/#expression-parameters-asset) 资产 。
#### 提示
您应该假设参数总是可以更改的。避免 “死胡同” - 如果您的状态没有出口，则 Avatar 的动画控制机可能会中断。

## Built-in Parameters  内置参数

您可以通过将 VRChat 的内置头像参数添加到头像的 Playable Layers 来访问这些参数。如果您添加这些参数之一，VRChat 会根据 VRChat 中发生的情况自动更新其值。例如，如果添加 VelocityMagnitude 参数，则其值将根据玩家的当前速度进行更新。

所有内置参数都是只读的。您不能使用 Expressions Menu 或 OSC 更改它们。

下面的列表包含 VRChat 的所有内置参数、它们的描述、它们的类型和它们的同步类型 。

| Name                  | 中文名称               | Description (描述)                                                                                              | Type   | Sync      |
|-----------------------|------------------------|---------------------------------------------------------------------------------------------------------------|--------|-----------|
| IsLocal               | 是否本地佩戴           | 如果是本地佩戴该头像，则为 True，否则为 False                                                                 | Bool   | None      |
| PreviewMode           | 是否为预览模式         | 如果头像正在预览中则返回 1，否则返回 0                                                                        | Int    | None      |
| Viseme                | 发音形状索引           | Oculus 发音形状索引（0-14）；使用 Jawbone/Jawflap 时，范围为 0-100 表示音量                                     | Int    | Speech    |
| Voice                 | 麦克风音量             | 麦克风音量，范围为 0.0–1.0                                                                                     | Float  | Speech    |
| GestureLeft           | 左手手势               | 来自左手控制器的手势（0-7）                                                                                    | Int    | IK        |
| GestureRight          | 右手手势               | 来自右手控制器的手势（0-7）                                                                                    | Int    | IK        |
| GestureLeftWeight     | 左手触发权重           | 左手模拟触发器（0.0–1.0）                                                                                      | Float  | Playable  |
| GestureRightWeight    | 右手触发权重           | 右手模拟触发器（0.0–1.0）                                                                                      | Float  | Playable  |
| AngularY              | Y轴角速度              | Y 轴上的角速度                                                                                                 | Float  | IK        |
| VelocityX             | 横向速度               | 横向移动速度（米/秒）                                                                                          | Float  | IK        |
| VelocityY             | 垂直速度               | 垂直移动速度（米/秒）                                                                                          | Float  | IK        |
| VelocityZ             | 前进速度               | 前向移动速度（米/秒）                                                                                          | Float  | IK        |
| VelocityMagnitude     | 速度总量               | 移动速度的总幅度                                                                                               | Float  | IK        |
| Upright               | 站立状态               | 表示站立程度，0 为趴下，1 为完全直立                                                                          | Float  | IK        |
| Grounded              | 是否接触地面           | 如果玩家接触地面则为 True                                                                                      | Bool   | IK        |
| Seated                | 是否坐下               | 如果玩家处于 station 状态则为 True                                                                            | Bool   | IK        |
| AFK                   | 是否离开状态           | 表示玩家是否处于离开状态（如 HMD 远离或按下 End 键）                                                           | Bool   | IK        |
| TrackingType          | 跟踪类型               | 参见详细描述                                                                                                   | Int    | Playable  |
| VRMode                | 是否为 VR 模式         | 如果用户处于 VR 模式则返回 1，否则为 0                                                                         | Int    | IK        |
| MuteSelf              | 是否自我静音           | 如果用户将自己设为静音则为 True，未静音为 False                                                                | Bool   | Playable  |
| InStation             | 是否在 station         | 如果用户处于 station 中则为 True，否则为 False                                                                | Bool   | IK        |
| Earmuffs              | 是否启用耳罩模式       | 如果启用了耳罩功能，则为 True                                                                                  | Bool   | Playable  |
| IsOnFriendsList       | 是否在好友列表中       | 如果查看头像的人是佩戴者的好友，则为 True；本地始终为 False                                                  | Bool   | Other     |
| AvatarVersion         | 头像 SDK 版本          | 如果头像使用 SDK3（2020.3.2 或更高）构建则为 3，否则为 0                                                       | Int    | IK        |
| IsAnimatorEnabled     | 动画器是否启用         | 在头像动画器禁用前一帧返回 False，启用时返回 True                                                              | Bool   | None      |
### 模型缩放参数
您的试玩层可以使用以下参数对玩家的当前[头像比例](https://creators.vrchat.com/avatars/avatar-scaling)做出反应：
| Name                  | 中文名称               | Description (描述)                                                                                           | Type   | Sync      |
|-----------------------|------------------------|--------------------------------------------------------------------------------------------------------------|--------|-----------|
| ScaleModified         | 是否被缩放             | 如果使用头像缩放功能缩放用户，则返回 true；如果头像为默认大小，则返回 false                                  | Bool   | Playable  |
| ScaleFactor           | 比例因子               | 头像的默认高度与当前高度之间的比例关系。例如默认眼高 1 米，缩放到 2 米时报告为 2                             | Float  | Playable  |
| ScaleFactorInverse    | 比例因子反转           | 头像高度的反比（1/x）。例如默认眼高 1 米，缩放到 2 米时报告为 0.5。极端情况可能不准确                         | Float  | Playable  |
| EyeHeightAsMeters     | 眼睛高度（米）         | 头像的眼睛高度，以米为单位                                                                                   | Float  | Playable  |
| EyeHeightAsPercent    | 眼高百分比             | 头像眼高相对于默认缩放限制（0.2–5.0 米）的百分比。例如缩放到 2 米时报告为 0.375                              | Float  | Playable  |
### Parameter Types  参数类型
在 Parameters 对象中定义参数时，您可以访问三种类型的变量。
您最多可以使用总共 256 位的“内存”。这并不是 Avatar 的内存使用意义上的严格内存，而是与同步参数时使用的带宽有关。
| Parameter Type 参数类型 | Range 范围           | Memory Usage 内存使用情况 | Notes 笔记                             |
|--------------------------|----------------------|---------------------------|----------------------------------------|
| int    整数             | 0 - 255              | 8 bits 8 位               | Unsigned 8-bit int. 无符号 8 位 int。   |
| float 浮                | -1.0 to 1.0          | 8 bits 8 位               | Signed 8-bit fixed-point decimal². 有符号 8 位定点十进制。 |
| bool 布尔               | True or False 对或错 | 1 bit 1 位                |                                        |
### GestureLeft 和 GestureRight 值
GestureLeft 和 GestureRight 使用以下值：
| Index 指数 | Gesture 手势   | 中文名称   |
|------------|----------------|------------|
| 0          | Neutral        | 中性       |
| 1          | Fist           | 握拳       |
| 2          | HandOpen       | 张开手       |
| 3          | FingerPoint    | 指点       |
| 4          | Victory        | 胜利       |
| 5          | RockNRoll      | 摇滚手势   |
| 6          | HandGun        | 手枪       |
| 7          | ThumbsUp       | 竖起大拇指 |
### Viseme Values  语素值
我们使用 Oculus 发音嘴型索引 ，从上到下，其中 sil 为 0。供参考：
| Viseme Parameter | Viseme |
|------------------|--------|
| 0                | sil    |
| 1                | pp     |
| 2                | ff     |
| 3                | th     |
| 4                | dd     |
| 5                | kk     |
| 6                | ch     |
| 7                | ss     |
| 8                | nn     |
| 9                | rr     |
| 10               | aa     |
| 11               | e      |
| 12               | i      |
| 13               | o      |
| 14               | u      |
### AFK State  AFK 状态
- 用户摘下头戴式设备，HMD 接近传感器返回未佩戴头戴式设备
- 系统菜单已打开。这取决于您使用的平台在系统菜单启动时如何传输数据 - 例如，Oculus Dash 不会注册为 AFK，但 SteamVR 的菜单会注册为 AFK。这是一种连锁反应，而不是设计的行为。
- 用户按下了 End 键，切换了 AFK 状态。
### TrackingType Parameter
TrackingType 表示一些信息。

如果值为 3、4 或 6，而 VRMode 为 1，则该值表示虚拟形象的佩戴者已启用和当前跟踪的跟踪点数。 此值可以更改！ 如果 6 点跟踪中的用户删除了额外的 3 个跟踪点，则他们的值将从 6 变为值 3。在设计动画制作器时，请考虑到这一点。

如果值为 0、1 或 2，而 VRMode 为 1，则该值表示 avatar 仍在初始化。您不应将动画制作器设计为基于此值组合进行分支，而应等待“有效”值 3、4 或 6。
| 参数 | 描述 |
|------|------|
| 0    | 初始化。通常仅在用户切换头像且其 IK 尚未发送时发生。 |
| 1    | 通用装备。用户可能启用了任何类型的跟踪，但头像纵为 Generic，因此跟踪将被忽略。如果 VRMode 为 0，则可能是桌面用户。 |
| 2    | 仅发生在 AV2 中，因此对于头像上的 AV3 控制器来说，这不是您应该期望长时间处于的状态。SDK3 工作站可能仍会出现这种情况。无需手指的纯手动跟踪。这只会发生在过渡状态中 - 例如，您应该期望 TrackingType 再次更改，并且头像不应保持此状态。 |
| 3    | 头部和手部追踪。如果 VRMode 为 1，则此用户处于 3 点 VR 中。如果 VRMode 为 0，则这是人形头像中的 Desktop 用户。 |
| 4    | 4 点 VR 用户。头部、手部和臀部。 |
| 5    | 5 点 VR 用户。头部、手和脚被追踪。基本上是全身跟踪，但没有臀部。 |
| 6    | 全身跟踪 VR 用户。追踪头部、手部、臀部和脚部。 |

### Custom parameters 自定义参数
您可以将自己的参数添加到头像的 Playable Layers 中。
您必须创建一个 Expression Parameters 资产 ，该资产允许您在 VRChat 中控制参数 。例如，您可以设置表达式菜单并允许用户在 VRChat 中自定义您的头像。
#### 表达式参数资产
Expression Parameters 资源包含可播放图层可以使用的自定义参数列表。每个参数都有名称、类型和默认值。您还可以选择是否应为其他玩家同步参数，这样其他玩家就可以查看由动画制作器和自定义参数引起的更改。
![](https://creators.vrchat.com/assets/images/default-parameters-484af1106c2aa0cd239d6afe810c23b2.png)
#### 如何控制自定义参数
在头像的 Playable Layers and Expression Parameters 资源中设置自定义参数后，您可以通过三种不同的方式控制它们：
- 设置 Expressions 菜单 ，让用户可以轻松控制 VRChat 中的参数，例如，在服装之间切换或播放自定义动画。表达式菜单是控制自定义参数的最简单和最常用的方法。
- 您可以将状态行为 Avatar Parameter Driver 附加到 Playable Layer 中的状态。它可以自动设置、添加或随机化您在 Expression Parameters 资产中定义的参数。
- 您可以为 OSC 设置您的头像，允许用户和第三方工具控制参数。例如，VRCFaceTracking 使用面部和眼睛跟踪硬件来控制虚拟形象的面部表情参数。

#### Default AV3 Aliasing 
模板 AV3 VRChat 控制器使用了一些“默认”，如果您不想构建自己的控制器，可以使用这些控制器。由于别名，它们不会与你自己的使用发生冲突（只要你不给它们命名相同的事物）。
特别是，Default Action 和 FX 图层使用别名。您无需担心使用这些层中的 Expression。

作使用名为 VRCEmote 的别名参数，该参数是一个范围为 1 到 16 的 Int。

FX 使用称为 VRCFaceBlendH （-1,1） 和 VRCFaceBlendV （-1,1） 的别名浮点参数，如果您想尝试自己的菜单来使用它们。默认 FX 层要求您具有名为 Body 的蒙皮网格，其中包含 mood_happy 、 mood_sad 、 mood_surprised 和 mood_angry 混合变形。

重申一下，如果您有一个作为 Avatar3 头像上传的头像，没有任何自定义 Playable 图层，那么只要您有上述混合形状，您就可以对它们使用一些内置表情。

如果您还有一个 eyes_closed 混合形状，当您使用默认的 Die 表情或 go AFK 时，它将关闭它们。
#### Cross-Platform Parameter Sync 跨平台参数同步
使用同时上传了 Quest 和 PC 版本的虚拟形象时，参数将按它们在参数列表中的位置及其参数类型进行同步， 而不是按参数的名称进行同步。要使要在 PC 和 Quest 之间同步的给定参数，该参数必须位于参数列表中的相同位置，并且具有相同的参数类型。

鉴于此，您应该始终对头像的 PC 和 Quest 版本使用相同的 Expression Parameters 资产，即使一个版本没有使用所有参数。

#### Mismatched Parameter Type Conversion 不同类型之间的参数转换

当您在 Animator 中选择参数类型时，最好选择与您尝试使用的内置参数或自定义参数相同的类型。例如：如果您在动画制作器中使用 VRChat 的内置 AFK 参数，则应选择类型 bool。

但是， 您可以为参数选择不匹配的类型。VRChat 将尝试将参数的值转换为动画制作者使用的类型。例如，如果您为 AFK 参数选择浮点类型，VRChat 会自动将 AFK 设置为 1.0 或 0.0，而不是 true 或 false。这还允许您在 Animator 的 Blend Tree 中使用 AFK 参数。

下表显示了转换不匹配的参数如何更改它。
| Source Type 源类型 | Animator Type Animator 类型 | Conversion Behavior 转化行为 | Example 例 |
|--------------------|----------------------------|-----------------------------|------------|
| int                | float                    | 直接转换为 float。 | 1 → 1.0   |
| int                | bool                   | 0 为 false，其他任何内容为 true | 1 → true  |
| float         | int                        | 四舍五入到最接近的 int （与 Mathf.Round 相同） | 0.5 → 0, 0.6 → 1, 1.5 → 2 |
| float           | bool                   | 0.0 为 false，其他任何内容为 true | 0.5 → true |
| bool          | int                        | true 为 1，false 为 0 | true → 1  |
| bool          | float                    | true 为 1.0，false 为 0.0 | true → 1.0 |

#### Trigger Typed Parameters  触发器类型化参数
目前，我们不建议在动画控制器中使用 Trigger 类型参数。这些值可能会在您的 Avatar 版本之间取消同步，包括远程客户端查看您的 Avatar 或在特殊情况下（例如在镜子中查看您的 Avatar）。如果要表示头像的状态，请使用 Int、Float 或 Bool 类型参数。

## Sync Types 同步类型
VRChat 将大多数内置参数与实例中的其他播放器同步，您可以为自己的自定义参数启用同步。
同步类型决定了 VRChat 如何同步每个参数。参数使用以下同步类型之一：
- Speech 
    - 仅用于发音嘴型。
    - 输出参数取决于您的语音。
    - 在本地更新，而不是直接同步（因为它是由音频驱动的）
- Playable
    - 一种较慢的同步模式，用于同步运行时间较长的动画状态。
    - 根据参数更改（每秒 1 到 10 次更新），根据需要每 0.1 到 1 秒更新一次，但您不应依赖它来实现快速同步。
- IK
    - 一种更快的同步模式，用于同步频繁变化的值。
    - 每 0.1 秒持续更新一次（每秒 10 次更新），并为远程用户在本地插入 float 值。
    - 根据参数，这也可能只是根据虚拟形象的本地渲染 IK 状态进行计算。
- None
    - 此参数不与其他播放器同步。
    - 例如，对于本地玩家的头像，IsLocal 始终为 true，对于其他玩家的头像，IsLocal 始终为 false。

如果您为[自定义](https://creators.vrchat.com/avatars/animator-parameters/#custom-parameters)参数启用同步，VRChat 通常使用 Playable 同步类型。但是，当您使用 [Puppet 控件](https://creators.vrchat.com/avatars/expression-menu-and-controls#types-of-controls)控制参数时，VRChat 会从 Playable 切换到 IK 同步，从而提高更新速率平滑插值。当您关闭 Puppet 控件时，它会返回到 Playable 同步。

## Footnotes  脚注
GestureLeftWeight 和 GestureRightWeight 在各种手势中从 0.0 变为 1.0，具体取决于扳机扣动。例如，如果您握拳但不扣动左手的扳机键，则 GestureLeft 将为 1，但 GestureLeftWeight 将为 0.0。当您开始扣动扳机时，它会从 0.0 攀升到 1.0。这可用于创建 “模拟” 手势或有条件地检测各种事物。

远程同步的浮点值有 255 个可能的值，通过网络提供 1/127 的精度，并且可以精确存储 -1.0、0.0 和 1.0。在本地更新时（例如使用 OSC），浮点值将作为本机（32 位）浮点值存储在动画器中。