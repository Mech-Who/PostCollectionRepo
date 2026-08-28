---
title: 画图不再手搓！diagram-design — 适配各大 Agent Harness 的 39 种图表一键生成 Skill
date: 2026-08-28
category: 工具推荐
depth: 深度
layer: layer2
tags: [diagram-design, Agent Skill, 图表生成, 架构图, Mermaid, Draw.io, 品牌风格, 设计系统, 工具推荐]
summary: RUNOOB 推荐 diagram-design Skill（github.com/cathrynlavery/diagram-design）：适配 Claude Code / Codex / Factory Droid / Pi 四大 Agent Harness，内置 39 种图表类型 × 3 套变体（浅色/深色/完整编辑版），输出零依赖自包含 HTML+SVG。核心解法不是"更强的生成模型"而是"设计系统约束生成"——语义化颜色角色 + 一句话接入品牌风格（自动抓网站主色/字体映射为语义 token + WCAG 对比度检查），还支持把存量 Draw.io / Mermaid 图换皮重画。
source_url: https://mp.weixin.qq.com/s/JJKkzrrf9Rmr62YMkchykQ
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** 开发者用 AI 画技术图的三大痛点：颜色随机、间距不统一、与文档风格脱节——想要好看的图还是得回 Figma/Draw.io 手搓半小时。diagram-design 这个 Agent Skill 把"编辑级质感"做成了可安装的能力包：39 种图型（架构/流程/时序/状态机/ER/甘特/桑基/鱼骨/Wardley/用户旅程等）、每类 3 套静态变体、零依赖自包含 HTML 输出；一句话即可接入品牌风格（抓取网站配色字体→语义化角色映射→WCAG 对比度检查→写入配置），并支持 import-drawio / import-mermaid 存量重画（格式/尺寸/细节/受众四维可调）。

## 我的理解
> 由小林生成，供小涵审阅修改

**这篇文章真正值得记住的，不是又一个新工具，而是它对"AI 画图痛点"的定性：问题不是画不出，而是画不稳。** AI 生成图表的内容正确性早已够用，败在颜色随机、间距失控、与文档风格脱节——这些恰恰是自由生成模型的盲区。diagram-design 的解法思路值得单独提炼：

| 层 | 传统做法 | diagram-design 做法 |
|----|---------|-------------------|
| 风格来源 | prompt 里祈祷（"画得好看点"） | 语义化设计 token（背景/线条/强调色角色化） |
| 品牌一致 | 每张图手动调色 | 一次抓取网站→映射 token→写入配置，后续全自动 |
| 可读性保障 | 肉眼检查 | WCAG 对比度自动检查 + 主动调整建议 |
| 存量迁移 | 重画 | import-drawio / import-mermaid，内容与样式分离换皮 |

**本质是"图表世界终于有了 CSS"**：内容（结构/数据）与样式（token）彻底分离，同一份 Mermaid 源可以按受众换四套皮（格式 HTML/SVG/PNG、尺寸、细节密度、工程师措辞 vs 高管措辞）。这和 Web 把结构与表现分离是同一次思想革命在图表领域的重演。

**对 Skill 生态的意义**：这是"能力包 > 单次 prompt"模式的又一实证——39 图型 × 3 变体的模板库 + 语义 token 约束打包成一个 plugin，四大 harness（Claude Code/Codex/Factory Droid/Pi）一行命令即获得"编辑级"排版能力。专业审美不再依赖每次对话的 prompt 运气，而是被固化成可分发的工程资产。与 `agent-skill工程化`、`harness-engineering` 的方向一致：**把隐性专业知识显性化为可安装的约束系统**。

**工程细节加分项**：输出是自包含 HTML（内嵌 SVG），无构建步骤、不依赖 JS 和外部图片资源——双击即看、可归档、diff 友好，唯一网络依赖是 Google Fonts（离线场景会回退字体）。

**与已有知识的连接：**
- `agent-skill工程化` / `harness-engineering`：Skill 作为 harness 生态的能力分发单元，本篇是工具型 Skill（对比知识型/流程型 Skill）的典型样本
- `context-engineering`：品牌风格抓取→语义角色映射→配置文件，是把"审美"这种隐性 context 显性化、持久化的范例
- `工具推荐与开源`：开源工具入库

## 📌 关键要点

- **痛点定性**：AI 画图的问题是"画不稳"不是"画不出"——风格随机、间距失控、与文档脱节；解法是**设计系统约束生成**，不是换更强的模型
- **39 种图型 × 3 变体**：架构/流程/时序/状态机/ER/时间线/泳道/象限/雷达/飞轮/树状/组织架构/甘特/散点/桑基/鱼骨/Wardley 地图/看板/用户旅程/部署图/依赖图/UML 类图/数据库表结构等，每类提供简约浅色、简约深色、完整编辑版
- **零依赖输出**：自包含 HTML + 内嵌 SVG，无构建、无 JS、无外部图片，双击浏览器即开（仅 Google Fonts 需联网）
- **品牌风格一句话接入**："帮 diagram-design 接入 https://yoursite.com 的品牌风格" → 自动抓首页主色/字体 → 映射语义角色 → 展示修改预览 → 确认写配置；附 WCAG 对比度检查，小字对比不足主动提示
- **存量重画**：`/diagram-design:import-drawio` 和 `import-mermaid` 读取源文件用同一套设计系统重画，四维可调——输出格式（HTML/SVG/PNG）、尺寸（文档内嵌/16:9 幻灯/社媒图）、细节（保真/平衡/简化）、受众（工程师/高管）
- **四大 harness 安装**：Claude Code / Codex / Factory Droid / Pi 各有一条 plugin marketplace 命令（见原文）

## 原文

> RUNOOB 菜鸟教程 · 2026年8月28日 · 来源：RUNOOB（公众号）

作为开发人员，我们每天都在跟各种图表打交道：系统架构图、API流程图、数据库 ER 图、部署流程图...

写技术文档、做产品方案，经常需要配各种配图：架构图、流程图、时序图。现在让 AI 帮我们画，确实比自己动手快，但生成出来的东西颜色随机、间距不统一、和文档其他部分的风格完全对不上。

想要真正好看、和品牌调性一致的图，还是得打开 Figma 或者 Draw.io，手动拖拽半小时，调色、对齐、留白，一个都不能少。

尤其是 Mermaid，虽然方便，但画出来的东西往往离设计感还有十万八千里。

很多时候图画到一半就放弃了，干脆用文字凑合过去。

今天给大家介绍一个适配各大 Agent Harness 的图表制作 Agent Skill -- **diagram-design**。

Diagram Design 是一个给 Claude Code、Codex、Factory Droid、Pi 这些 AI 编程工具用的 Skill，专门画"编辑级质感"的图——不是那种一眼假的 AI 生成图，是看起来像专业设计师做出来的图。

Diagram Design 内置 39 种图表类型：架构图、流程图、时序图、状态机、ER 图、时间线、泳道图、象限图、雷达图、飞轮循环图、树状图、组织架构图、甘特图、散点图、桑基图、鱼骨图、Wardley 地图、看板、用户旅程图、部署图、依赖关系图、UML 类图、数据库表结构图等等，覆盖了技术文档和产品方案里能用到的绝大部分图表场景。

- **GitHub：https://github.com/cathrynlavery/diagram-design**
- **在线画廊：https://cathrynlavery.github.io/diagram-design/**
- **支持工具：Claude Code、Codex、Factory Droid、Pi**

全部 39 种图表都提供 3 套静态变体：简约浅色、简约深色、完整版编辑样式，直接用浏览器打开即可，无需构建步骤，不依赖 JS 和外部图片资源。

也可以本地打开 `skills/diagram-design/assets/index.html`，切换浅色 / 深色 / 完整版标签浏览全部 39 种图表。

### 安装方式

**1、Claude Code**

```
/plugin marketplace add cathrynlavery/diagram-design
/plugin install diagram-design@diagram-design
```

**2、Codex**

```
codex plugin marketplace add cathrynlavery/diagram-design
codex plugin add diagram-design@diagram-design
```

Codex 在启动时刷新已配置的 Git 插件市场。如需立即拉取更新：

```
codex plugin marketplace upgrade diagram-design
```

之后新建会话。

**3、Factory Droid**

```
droid plugin marketplace add https://github.com/cathrynlavery/diagram-design
droid plugin install diagram-design@diagram-design --scope user
```

Factory Droid 通过 Git commit 跟踪插件，而非清单版本号。获取更新：

```
droid plugin marketplace update diagram-design
droid plugin update diagram-design@diagram-design --scope user
```

之后新建会话。

**4、Pi**

```
pi install https://github.com/cathrynlavery/diagram-design
```

### 快速上手

**1、简单使用**

装好之后，可以直接指定 /diagram-design 来生成图片，用自然语言描述你要的图就行：

```
/diagram-design-main 帮我画一个架构图：前端、后端、数据库、Redis 缓存
```

完成后就会生成 html 页面，里面是 svg 图片。

生成出来的是一个自包含的 HTML 文件，双击直接在浏览器里打开，不需要联网（除了加载 Google Fonts），没有构建步骤，没有额外依赖。

**2、最实用的功能：让图自动匹配你的品牌风格**

默认情况下，生成的图是黑白配橙色调（白烟色底、墨黑线条、橙色强调色），直接截图用也不难看。

但只需要一句话，就能让它读取你网站的配色和字体，自动套用到之后生成的所有图上：

```
帮 diagram-design 接入 https://yoursite.com 的品牌风格
```

比如接入苹果的设计风格：

```
帮 diagram-design 接入 https://www.apple.com/ 的品牌风格
```

AI 会自动抓取网站首页，提取主色调和字体，映射成语义化的角色，展示一份修改预览，确认之后写入配置文件。

之后每张新生成的图，背景色用你网站的背景色，重点强调色用你网站按钮的颜色，字体也跟你网站正文字体保持一致。

整个过程还会自动做 WCAG 对比度检查，确保文字在背景上清晰可读，如果你网站的配色在小字号下对比度不够，会主动提示并给出调整建议。

**3、还能把已有的 Draw.io、Mermaid 图重新画一遍**

手上如果已经有 Draw.io 或者 Mermaid 格式的图，Diagram Design 可以直接读取源文件，用同一套设计系统重新画一遍——内容不变，风格换新：

```
/diagram-design:import-drawio platform.drawio --size=slide-16x9 --detail=simplified --audience=executive
/diagram-design:import-mermaid architecture.mmd --size=slide-16x9 --detail=simplified
```

重画的时候有四个可以调的维度：输出格式（HTML/SVG/PNG）、尺寸（文档内嵌、16:9幻灯片、社交媒体图等）、细节程度（保真/平衡/简化，节点数量会跟着精简）、目标受众（工程师看得懂的技术措辞，还是给高管看的简化说法）。

## 相关笔记
- [[2026-08-26_读懂Pi的agentloop源码]]（Pi harness 生态）
- `agent-skill工程化`、`harness-engineering` 概念
