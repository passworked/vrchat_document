# Debugging Avatar Components 模型调试组件
由于 Avatar 组件可能变得相当复杂，因此在构建 Avatar 时很容易犯错误，这是可以理解的。为了帮助测试和调试问题，我们为用户提供了一些工具来帮助简化该过程。
## In Game Debugging  游戏内调试
##### info  信息
在下面的视频中，“Avatar Dynamics（Avatar 动力学）”指的是 PhysBones 和 Contacts。随着时间的推移，VRChat 为头像添加了更多功能，现在“Avatar Dynamics”一词的使用频率较低。

[video](https://youtu.be/8hqDquZWvhY)

使用 Action Menu（作菜单），您可以使用 Avatar Overlay 选项在游戏中实时显示骨骼和联系的视觉表示。这些对于准确查看正在发生的事情或对象是否已正确设置非常有用。

## In-Editor Debugging  编辑器内调试
动态骨骼和联系都在编辑器中运行，就像在 VRChat 中运行一样。通过进入 Play 模式，您可以模拟这些系统并查看您的头像将如何反应，而无需上传它。

您可以在 Play mode 和编辑模式下在 Editor 中测试约束。如果您愿意，可以通过 SDK 控制面板(VRChat SDK > Show Control Panel > Settings > Execute VRChat Constraints in Edit Mode)停止在编辑模式下运行的约束。

如果您在进入 Play 模式之前将 Animator Controller 添加到头像的 Animator 组件，则头像上的参数将更新，就像在 VRChat 中一样。

此外，即使没有设置动画控制器，您仍然可以查看每个组件并查看它们将为每个参数提供的值。