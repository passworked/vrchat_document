# Rotation Constraint
VRCRotationConstraint 组件更改目标转换的位置以匹配其源的位置。
![alt text](https://creators.vrchat.com/assets/images/rotation-7417f4cfc0a670fd1a9a32419176e369.png)
- Is Active - 控制是否评估约束。禁用整个组件并停用带有该组件的游戏对象也会阻止约束运行。
- 权重 - 控制应用于此约束的总权重。
    - 这通常应该在 0 到 1 的范围内，但如果您想设置超出该范围的值，您可以勾选 Free 编辑框。
检查器顶部的两个按钮是实用程序，可让您：
- **激活**约束。这将保存源的当前偏移，然后激活并锁定约束。
- **将约束归零** 。这会将偏移重置为其默认值，然后激活并锁定约束。
## Constraint Settings  约束设置
- Rotation At Rest - 定义约束的总权重为 0 时变换的旋转角度。
- Rotation Offset - 定义应用于此约束结果的偏移。
- Lock - 启用后，将 At Rest 和 Offset 值锁定在适当的位置，以防止对其进行编辑。
    - 如果激活约束并解锁这些值，则当目标变换的位置发生变化时，将重新计算这些值。
    - 如果锁定这些值并激活约束，则约束将开始控制变换。
- Freeze Position Axes - 允许您在解算约束时从计算中排除特定轴。默认情况下，所有三个轴都被选中进行评估。
## Sources  来源
“Sources” 列表确定哪些转换会影响此约束。单击右下角的 + 按钮以添加新源。单击 - 按钮以删除当前选定的源。每个源都有以下选项：
- Source Transform （源转换 ） - 要用作源的转换。
- Weight - 控制此源对约束的影响程度。
    - 这通常应该在 0 到 1 的范围内，但如果您想设置超出该范围的值，您可以勾选`Free`编辑框。
## Advanced  高级
- Target Transform - 定义受此约束组件影响的物体。如果留空，则此约束附加到的物体将受到影响
- Solve In Local Space - 如果选中此选项，那么将会于本地空间结算该约束而不是在世界空间中解算此约束。
- Freeze To World - 如果勾选该项，则此约束将忽略其源并保持固定旋转。
- Rebake Offsets When Unfrozen - 如果选中此选项，那么当禁用`Freeze To World`时，此约束将相对于其源重新烘焙其偏移量。
有关这些高级设置如何工作的更深入说明，请参阅涵盖 Advanced Constraint Settings 的父部分。