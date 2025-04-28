# 有关 Avatar 缩放的技术注意事项
Avatar 缩放允许玩家更改其当前 Avatar 的身高。

本页文档记录了 VRChat 的头像缩放如何在内部工作，这在一定程度上可能有助于围绕它开发社区资源。

阅读[Avatar Events](https://creators.vrchat.com/worlds/udon/players/player-avatar-scaling)文档或我们的[示例脚本](https://creators.vrchat.com/worlds/examples/udon-example-scene/avatar-scaling-settings) ，了解如何将 Avatar 缩放与 Udon 结合使用。阅读 [模型参数](https://creators.vrchat.com/avatars/animator-parameters) 页面，了解与扩展相关的可用 Avatar 参数。

## 术语定义
- Eye Height - 眼睛高度 ：处于 T-Pose时，头像视点的高度大于 0（变换位置的 Y 分量）。
- Prefab Height - 预制体高度:缩放为默认值时 avatar 的眼睛高度。这是您在 SDK 中通过放置 “View Position” 进行配置的内容。
- Target Eye Height -目标眼睛高度 ：头像要缩放到的眼睛高度，由玩家或 Udon 设置。
- Avatar Scale - 头像缩放：“预制体高度”和（目标眼睛高度）之间的比率。例如，如果目标为 4.5 米，预制件高度为 1.5 米，则“Avatar Scale”为 3。

## 值的范围

“预制体高度” 不受限制。您可以在 SDK 中将头像的视角球放置在任何高度。但请注意，您的整体头像规模会影响您的绩效排名。
Udon的“目标眼高”限制在 0.1 到 100 米之间，Action菜单中的可用缩放范围从 0.2 米到 5.0 米。但是，通过上传超出此范围的头像并且不使用此菜单，您仍然可能超过这些限制。在这种情况下，“Target Eye Height” 将等于 “Prefab Height” ，这不受限制。

此限制意味着 Udon 必须在 “avatar eye height changed”事件上重新应用缩放，以完全强制执行缩放。否则，用户可以切换到更矮或更高的头像来绕过世界设置的限制。

在禁用模型缩放的世界中，“Target Eye Height” 将始终等于 “Prefab Height” 。

## 如何应用缩放
缩放头像的工作原理是更改头像根变换的 “localScale”。 **此比例是强制性的**。除了与头像缩放相关的 Udon 函数外，没有用户可访问的方法来覆盖头像根的刻度。

每当缩放比例发生变化时（即，每当您切换头像或重置/重新加载当前头像时），头像都会在本地“重新测量”。此过程会调整您的视点以匹配新的高度，并重新定位一些内部组件，例如您的声音位置。

每个玩家的缩放会自动同步为 “眼睛高度”，量化为小数点后 3 位。对于远程用户，每当收到新的高度时，都会在短时间内平滑比例变化。

使用 Action菜单 中的刻度盘时，您的头像仅在镜像中缩放。在表盘上确认刻度时，新刻度将立即应用于您的头像，然后发送给远程用户。