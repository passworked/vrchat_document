# Expressions Menu and Controls
#### 提示
您需要有关 [Unity Animator](https://docs.unity3d.com/2022.3/Documentation/Manual/class-AnimatorController.html) 的基本知识，才能在头像的动画器中使用表达式参数。
您可以在 VRChat 中使用 Expressions Menu 控制头像的动画器。这允许您使用 VRChat 的径向菜单播放动画或更改头像的外观。
要在 VRChat 中使用表达式菜单，您需要创建（至少）两个资产：
- 一个或多个 Expressions Menu 资产
- 一个 Expression Parameters 资产

创建和配置这些资产后，请确保将它们添加到“Expressions（表达式）”部分的头像描述符中。
## 创建 Expressions 菜单
1. 通过选择`Assets > Create > VRChat > Avatars > Expressions Menu `创建 Expressions Menu 资产 。
![alt text](https://creators.vrchat.com/assets/images/default-expressions-d8b7b5094c3f2602526a7b27ae1c9ea5.png)
2. 通过选择 Expressions Menu 资产并单击“Create”按钮来创建 Expression Parameters 资产 。这允许您为 Expressions Menu 创建自定义参数。
    - 单击“创建”时，表达式参数资产会自动分配给您的表达式菜单资产。
    - 您还可以通过选择 `Assets > Create > VRChat > Avatars > Expression Parameters`来创建 表达式参数 资产。
    - 表达式参数可以选择从 Animator 复制参数以快速创建参数。
![](https://creators.vrchat.com/assets/images/default-parameters-484af1106c2aa0cd239d6afe810c23b2.png)
3. 选择 Expression Parameters 资产以对其进行自定义。
    - 默认情况下，该资产包含三个参数 ：VRCEmote、VRCFaceBlendH 和 VRCFaceBlendV。您可以安全地删除它们，除非您在头像中使用它们，或者不想创建自己的 Expression （表达式） 菜单
    - 您的 Animator 始终可以访问 VRChat 的内置参数 。例如，您不应将“AFK”或“GestureLeft”参数添加到表达式参数资产中。
4. 输入自定义参数的名称。
    - 这些名称应与动画器中的参数匹配。
    - 您可以使用`/`对参数进行分类。例如，`Clothing/Hoodie`和`Clothing/Hat`。
    - VRChat 有一些[内置参数](./Animator%20Parameters/Animator%20Parameters.md) 。您始终可以在 Animator 中使用它们 - 不要将它们添加到您自己的 Expression Parameters 中。
    5. 为每个参数选择一个类型。该类型应与 Animator 的[参数类型](https://docs.unity3d.com/2022.3/Documentation/Manual/AnimationParameters.html)匹配。
    - `Int`可以是 0 到 255 之间的任何整数。
    - `Float`可以是介于 -1.0 和 1.0 之间的任意数字。
    - `Bool`可以是 true 或 false。
    6. 选择`Default value`以设置每个参数的默认值。
        - 重置头像时，参数将恢复为此值。
    7. 为在加载头像时不应自行重置的参数启用`Saved`。如果您的头像具有自定义选项或设置， 则`Saved`将阻止它们在切换到其他世界或头像后被重置。
    8. 如果此参数的状态应通过网络发送给所有其他玩家，请启用`Synced`。
        - 自定义参数的[同步类型](https://creators.vrchat.com/avatars/expression-menu-and-controls#sync-types)为 Playable（[Puppet 控件除外](https://creators.vrchat.com/avatars/expression-menu-and-controls#types-of-controls)）。
接下来，您应该将这两个资产添加到您的`VRC Avatar Descriptor`中。
![](https://creators.vrchat.com/assets/images/avatar-descriptor-params-4e790cbff8b3ef8e1415473bb1c69cee.png)
9. 选择您的头像描述符，然后向下滚动到“Expressions”部分。
10. 将 “Menu” 属性更改为你的expressions menu.
11. 将 “Parameters” 属性更改为你的expression parameters.

将这两个资产添加到您的头像描述符后，您的所有表达式参数现在都将在表达式菜单中可用，允许您对其进行自定义。
![](https://creators.vrchat.com/assets/images/populated-menu-73ba42697179cca5440061b334bfe208.png)
12. 在检查器中，点按“添加控制”。最多可以将 8 个控件添加到单个菜单中。
13. 选择名称和类型 。
14. 您还可以在此处添加图标和子菜单，或更改控件的顺序。
    - 您可以在 中找到`VRCSDK/Assets3/Expression Menu Icons/`一些默认图标。

## 控件类型
`Expressions Menu`支持不同类型的控件。选择最适合您的使用案例的类型。
| 英文名            | 中文名     | 描述 |
|:------------------|:----------|:-----|
| Button            | 按钮      | 点击时设置参数，约一秒后同步/重置时恢复，不能长按。 |
| Toggle            | 开关      | 开启开关时设置参数，关闭开关时重置参数。 |
| Sub-Menu          | 子菜单    | 打开另一个表达式菜单，进入时可设置参数，退出菜单时将参数重置为零。支持嵌套子菜单。 |
| Two-Axis Puppet   | 二轴操纵杆 | 打开一个轴向操纵菜单，根据摇杆位置控制两个浮点参数（垂直和水平），取值范围为 -1.0 到 1.0。 |
| Four-Axis Puppet  | 四轴操纵杆 | 打开一个轴向操纵菜单，根据摇杆位置控制四个浮点参数（上、右、下、左顺序），取值范围为 0.0 到 1.0。 |
| Radial Puppet     | 径向操纵杆 | 打开一个径向操纵菜单，控制单个浮点参数，类似可填充的进度条，取值范围为 0.0 到 1.0。 |
“Puppet” 类型的控件有两个特殊功能：
- “参数”属性对于人偶控件是可选的。如果使用它，它将在 Puppet 控件打开时进行设置。这样，动画制作人员就可以检测人偶控件当前是否处于打开状态。
- 当您在 VRChat 中退出puppet 控件时，它会保留“参数水平/垂直/径向”值（直到您重新打开该控件或更改其他位置的值）。这样，您就可以在导航径向菜单的同时，将人偶控件“冻结”在任何状态下。

### Puppet菜单同步
Puppet控件在打开时使用[IK同步](https://creators.vrchat.com/avatars/animator-parameters#sync-types)。如果您希望同步尽可能接近您的输入以进行快速/快速移动，则应使用Puppet菜单。

Button/Toggle 使用 Playable Sync，它是按需更新的，而不是连续更新的，适用于您“打开/关闭”但不需要高精度同步的事情。

Puppet 菜单同步始终以最大可用速率更新，并且它会为远程用户平滑值 - 当定时复制很重要时，效果会更好。