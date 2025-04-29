# Shader Blocking and Fallback System
本页介绍了 Shader Blocking System（着色器阻塞系统）、其作方式以及着色器作者如何使用它，以便在用户使用给定着色器在头像上阻止了着色器时，其着色器可以正常回退。

## VRChat 2021.4.2 回退系统升级
着色器回退改进通过使用着色器顶部的“Tags”字段来实现。
默认情况下，tags 字段可能如下所示。
```shader
Tags{"Queue"="Geometry"}
```
现在，您可以在 VRCFallback 名称下添加不同的标签，以指定要尝试使用的回退着色器：
```shader
Tags{"Queue"="Geometry" "VRCFallback"="Toon"}
```
一些 fallback 标签是可组合的，例如，您可以使用 ToonCutout：
```shader
Tags{"Queue"="Geometry" "VRCFallback"="ToonCutout"}
```
支持的标签如下：
```
Unlit
VertexLit
Toon
Transparent
Cutout
Fade
Particle
Sprite
Matcap
MobileToon
DoubleSided
Hidden //(this will hide the mesh from view if the shader is blocked, useful for things like raymarching effects.)
```
Toon 和 Unlit 还可以与 Transparent、Cutout、Fade 和 DoubleSided 标签结合使用，以实现更精细的控制。Toon 支持 DoubleSided Cutout 等变体。
#### 注意
请注意，在 Toon 中使用 Transparent 或 Fade 标签将导致它回退到 Transparent Unlit。在选择回退标签时，您可能需要考虑到这一点。
指定任何其他标签将导致 Standard 着色器回退。
如果未提供标签，则将使用旧的回退系统，其后遵循模式着色器名称、关键字等。
我们现在还将所有标准着色器参数复制到回退材质，包括以下内容：
```shader
_MainTex
_MetallicGlossMap
_SpecGlossMap
_BumpMap
_ParallaxMap
_OcclusionMap
_EmissionMap
_DetailMask
_DetailAlbedoMap
_DetailNormalMap
_Color
_EmissionColor
_SpecColor
_Cutoff
_Glossiness
_GlossMapScale
_SpecularHighlights
_GlossyReflections
_SmoothnessTextureChannel
_Metallic
_SpecularHighlights
_GlossyReflections
_BumpScale
_Parallax
_OcclusionStrength
_DetailNormalMapScale
_UVSec
_Mode
_SrcBlend
_DstBlend
_ZWrite
```
## 旧的 Fallback 系统
当着色器被安全系统阻止时，首先会检查此列表中是否存在内部预编译着色器之一：
    预编译的内部着色器
```shader
  "Standard",
  "Standard (Specular setup)",
  "Effects/Rim",
  "Effects/GlowAdditiveSimple",
  "Legacy Shaders/Bumped Diffuse",
  "Legacy Shaders/Bumped Specular",
  "Legacy Shaders/Decal",
  "Legacy Shaders/Diffuse",
  "Legacy Shaders/Diffuse Detail",
  "Legacy Shaders/Diffuse Fast",
  "Legacy Shaders/Lightmapped/Diffuse",
  "Legacy Shaders/Lightmapped/Specular",
  "Legacy Shaders/Lightmapped/VertexLit",
  "Legacy Shaders/Parallax Diffuse",
  "Legacy Shaders/Parallax Specular",
  "Legacy Shaders/Reflective/Bumped Diffuse",
  "Legacy Shaders/Reflective/Bumped Specular",
  "Legacy Shaders/Reflective/Bumped Unlit",
  "Legacy Shaders/Reflective/Bumped VertexLit",
  "Legacy Shaders/Reflective/Diffuse",
  "Legacy Shaders/Reflective/Parallax Diffuse",
  "Legacy Shaders/Reflective/Parallax Specular",
  "Legacy Shaders/Reflective/Specular",
  "Legacy Shaders/Reflective/VertexLit",
  "Legacy Shaders/Self-Illum/Bumped Diffuse",
  "Legacy Shaders/Self-Illum/Bumped Specular",
  "Legacy Shaders/Self-Illum/Diffuse",
  "Legacy Shaders/Self-Illum/Parallax Diffuse",
  "Legacy Shaders/Self-Illum/Parallax Specular",
  "Legacy Shaders/Self-Illum/Specular",
  "Legacy Shaders/Self-Illum/VertexLit",
  "Legacy Shaders/Specular",
  "Legacy Shaders/Transparent/Bumped Diffuse",
  "Legacy Shaders/Transparent/Bumped Specular",
  "Legacy Shaders/Transparent/Cutout/Bumped Diffuse",
  "Legacy Shaders/Transparent/Cutout/Bumped Specular",
  "Legacy Shaders/Transparent/Cutout/Diffuse",
  "Legacy Shaders/Transparent/Cutout/Soft Edge Unlit",
  "Legacy Shaders/Transparent/Cutout/Specular",
  "Legacy Shaders/Transparent/Cutout/VertexLit",
  "Legacy Shaders/Transparent/Diffuse",
  "Legacy Shaders/Transparent/Parallax Diffuse",
  "Legacy Shaders/Transparent/Parallax Specular",
  "Legacy Shaders/Transparent/Specular",
  "Legacy Shaders/Transparent/VertexLit",
  "Legacy Shaders/VertexLit",
  "MatCap/Vertex/Textured Lit",
  "Mobile/Bumped Diffuse",
  "Mobile/Bumped Specular",
  "Mobile/Bumped Specular (1 Directional Light)",
  "Mobile/Diffuse",
  "Mobile/Unlit (Supports Lightmap)",
  "Mobile/Particles/Additive",
  "Mobile/Particles/Alpha Blended",
  "Mobile/Particles/Multiply",
  "Mobile/Particles/VertexLit Blended",
  "Particles/~Additive-Multiply",
  "Particles/Additive",
  "Particles/Additive (Soft)",
  "Particles/Alpha Blended",
  "Particles/Alpha Blended Premultiply",
  "Particles/Anim Alpha Blended",
  "Particles/Multiply",
  "Particles/Multiply (Double)",
  "Particles/VertexLit Blended",
  "Sprites/Default",
  "Sprites/Diffuse",
  "Toon/Lit",
  "Toon/Lit (Double)",
  "Toon/Lit Cutout",
  "Toon/Lit Cutout (Double)",
  "Toon/Lit Outline",
  "UI/Default",
  "Unlit/FailShader",
  "VRChat/UI/Default"
```
如果匹配了内部着色器，则回退是相同类型的新着色器，但使用内部编译的着色器。将复制所有参数。未包含的新版本或变体将不起作用，因为它们将被替换。

如果着色器内部不匹配，则使用着色器的名称（不是文件名，而是在着色器源的顶行中提供的名称）来匹配某些标识功能，并替换为类似类型的回退着色器：
    回退着色器名称搜索
```shader
  "Unlit",
  "VertexLit",
  "Toon",
  "Outline",
  "Transparent",
  "Fade",
  "Cutout",
  "Particle",
  "Sprite",
  "MatCap"
```
这些名称可以位于着色器名称的完整字符串中的任意位置。
此外，有些着色器可以这样找到：
    着色器属性
```shader
"_Ramp" == "Toon"
"_ALPHABLEND_ON" == "Transparent"
"_ALPHATEST_ON" == "Cutout"
```
所有匹配都区分大小写。
尝试创建近似于匹配名称的后备材料。例如，包含“Sprite”的名称会回退到 Unity 内置的“Sprites/Default”着色器。
您可以将“Toon”和“Cutout”或“Toon”和“Outline”组合用于组合着色器，但是“Transparent”和“Fade”当前没有 Toon Lit 着色器，而是回退到“Unlit/Transparent”。
对 “Outline” 的支持是高度实验性的，如果性能受到影响，可能会删除。
对于“Toon”着色器，将复制“_Ramp”参数 （Texture2D）。对于“MatCap”着色器，将复制“_MatCap”参数 （Texture2D）
如果在着色器名称中未找到匹配项，则使用 Standard 材质。
尝试将名为 “_MainTex” 和 “_Color” 的参数传输到回退着色器。如果两个参数都不匹配，则会提供 Matcap 着色器，并将颜色设置为用户的等级颜色。
在我们调整着色器回退系统时，所有这些都很容易发生变化。
## 预览 Avatar 的回退着色器
可以通过 Action Menu （作菜单） 中的切换按钮强制您自己的头像在本地使用回退着色器。要激活此选项，请打开您的作菜单，然后选择“选项”-> “头像” -> “回退着色器”。打开后，您使用的任何头像都将使用回退着色器在本地显示。该选项在切换头像时将保持活动状态，但在世界更改时会重置。此选项不会影响其他人查看您的头像的方式。