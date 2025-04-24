# Aim Constraint
`VRCAimConstraint`组件旋转目标转换，使其对准源。您可以自定义将哪个方向视为向前。
![alt text](https://creators.vrchat.com/assets/images/aim-cfcc2378c73124634c0eaee7a0150ffd.png)
- Is Active（是否激活）- 控制是否评估约束。禁用整个组件并停用带有该组件的游戏对象也会阻止约束运行。
- Weight(权重)- 控制应用于此约束的总权重。
    - 这个值通常应该在0到1的范围内，但如果您想设置超出该范围的值，您可以勾选`Free`编辑框。
- Aim Vector - 控制应面向源的轴。
- Up Vector - 控制此约束的向上轴。这是约束将尝试与下面定义的 world up 轴对齐的受影响变换的轴。
- World Up Type - 控制此目标约束所使用的世界向上方向。
    - Scene Up - 将向上视为场景的正 Y 轴。
    - Object Up - 将向上视为从约束的目标变换指向 World Up Object 属性中指定的变换的坐标轴。
    - Object Up Rotation - 将向上视为 World Up Object （世界上方向对象 ） 属性中指定的变换的局部空间中的 World Up Vector 轴。
    - Vector - 将向上视为世界空间中的 World Up Vector。
    - None - 不定义向上方向。
检查器顶部的两个按钮是实用程序，可让您：
- **激活**约束。这将保存源的当前偏移，然后激活并锁定约束。
- **将约束归零** 。这会将偏移重置为其默认值，然后激活并锁定约束。
## 约束设置
