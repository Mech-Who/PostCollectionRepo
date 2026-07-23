---
title: "有人花3天做了个开源工具，一句话生成各种场景的HTML"
date: 2026-05-19
category: AI应用
depth: 深度
tags: [html-anything, AI工具, HTML生成, AI Agent, 开源工具, Claude Code, 内容创作, 逛逛GitHub]
summary: 介绍开源项目html-anything——一款本地AI Agent驱动的HTML生成工具，内置75套模板、9种输出格式（杂志/PPT/海报/小红书卡片等），零额外API Key配置，一键导出适配微信/X/知乎等多平台，将"HTML is the new markdown"理念落地为实用工具。
source: 微信公众号
source_url: https://mp.weixin.qq.com/s/QgiNczY1L3XHIW2INcReAw
status: 📥已采集
sync_status: ✅已同步
---

> **摘要：** 开源项目html-anything由Open Design团队花3天、15000行代码打造，是一款与本地Coding Agent CLI（Claude Code/Cursor/Codex等）配合使用的HTML生成工具。内置75套模板覆盖9种输出格式（杂志文章、PPT、海报、小红书卡片、推文卡片、网页原型、数据报告、视频帧、简历），零额外API Key配置，一键导出适配微信/X/知乎等多平台。核心理念继承自Thariq和Karpathy的"HTML is the new markdown"——让AI帮你写HTML，你只负责内容。

## 我的理解
> 由小林生成，供小涵审阅修改

这个工具的出现很有意思，它不只是又一个AI包装工具，而是把"HTML is the new markdown"这个理念真正做成了可落地的产品。三个点让我觉得值得关注：

**1. 零配置复用现有Agent生态**：不自己造Agent，而是扫描PATH里已有的CLI工具。这意味着如果你已经在用Claude Code或Cursor，边际成本为零——不需要额外API Key，不需要学习新工具。这个设计哲学很聪明，避开了"又一个独立工具"的陷阱。

**2. 多平台一键导出的实用价值**：对小涵来说，如果你需要做内容输出（公众号文章、PPT、数据报告），这个工具可以大幅减少排版时间。特别是"导出到微信公众号自动内联CSS"这个功能，可以直接粘贴到微信编辑器不乱格式——做自媒体的痛点。

**3. 核心理念的启示**："Markdown是草稿，HTML才是最终形态"这个观点，本质上是在说AI可以承担"从草稿到成品"的所有排版工作。对于小涵的ICME论文排版、答辩PPT准备，如果把这个工具和Claude Code配合使用，可能也能找到应用场景——比如快速生成数据报告的可视化HTML版本。

不过也要理性看待：工具才做了3天，75套模板的质量和稳定性有待验证。建议先跑起来试几篇，看看实际效果再决定是否纳入日常流程。

## 📌 关键要点
- **核心功能**：本地AI Agent（Claude Code/Cursor等）配合75套模板，一键生成9种格式的HTML输出
- **零配置**：自动检测已安装的Coding Agent CLI，复用已有会话和API Key
- **多平台适配**：微信（CSS内联）、X/小红书/微博（2x PNG复制）、知乎（公式转换）
- **技术栈**：本地运行（localhost:3000），SSE流式传输实时预览HTML渲染过程
- **适用场景**：内容创作（公众号/小红书/推特）、PPT制作、数据报告、网页原型设计
- **使用方式**：`git clone` → 本地启动 → 选模板 → 粘贴内容 → ⌘+Enter

## 原文

# 有人花 3 天做了个开源工具，一句话生成各种场景的 HTML。

**作者：** 逛逛（逛逛GitHub）
**来源：** 微信公众号

---

大概就是前段时间 Claude Code 工程师在 X 上发了一篇文章，核心观点就一句话：**HTML is the new markdown**。
他已经不再写 Markdown 文件了，几乎所有东西都改成让 Claude Code 生成 HTML。
这篇文章在开发者圈子里炸了。
有人赞同也有部分人反对，在这场争论刷屏的时候，有人直接动手了。

Open Design 团队花了 3 天、15000 行代码，做出了一个开源项目叫 **html-anything**。
就是把 Thariq 和 Karpathy 说的那套理念，做成了一款谁都能用的工具。
X 上已经有一堆人在晒作品了。

---

### 01｜html-anything 是什么

一句话：**你的本地 AI agent 帮你写 HTML，你直接发布。**
它能接入你电脑上已经登录的 Coding Agent CLI，自动检测你装了哪些工具，然后复用你现有的会话。
你只需要粘贴内容，选一个模板，按下 ⌘+Enter，几秒钟就能拿到一份设计精美的 HTML 文件。
支持 8 种 Agent：Claude Code、Cursor、Codex、Gemini CLI、OpenCode 等。
不需要额外的 API Key，你之前怎么登录的就怎么用，边际成本为 0。

> 开源地址：https://github.com/nexu-io/html-anything

---

### 02｜三个让人眼前一亮的点

#### 1. 75 套模板，9 种输出格式
这是 html-anything 最核心的武器。内置了 75 套 Skill 模板，覆盖了 9 种输出格式：

- 杂志文章
- PPT 演示文稿
- 海报
- 小红书卡片
- 推文卡片
- 网页原型
- 数据报告
- Hyperframes 视频帧
- 简历

每种格式下还有多种风格可选。
比如 PPT 就有瑞士国际主义、杂志风、小红书粉彩风、赛博霓虹风等 20 种。
视频帧有液态背景 Hero、纽约时报风格数据图表、故障风标题卡、电影光效等 10 种。
从你写的内容到最终交付物之间的距离，被压缩到了一次 ⌘+Enter。

#### 2. 零 API Key，直接复用你的 Coding Agent
html-anything 不自己造 Agent。它的哲学是：**你装的那个就够了。**
启动时它会扫描你电脑的 PATH（这些 GUI 程序通常扫不到的目录）。
找到什么就用什么，Claude Code 也行，Cursor 也行，Codex 也行。
你之前用 `claude login` 或者 `cursor login` 登录过的会话，直接复用。不需要再配置一次 API Key，不需要多花一分钱。

#### 3. 一键导出，零二次排版
这一条对做内容的人来说太关键了。

- 导出到微信公众号：CSS 自动内联，直接粘贴到编辑器里格式不乱。
- 导出到 X / 小红书 / 微博：自动渲染成 2x 高清 PNG，复制到剪贴板，直接贴到发布框。
- 导出到知乎：数学公式自动替换成知乎能渲染的格式。
- 还能直接下载独立的 `.html` 文件或者高清 `.png` 图片，分享给谁都行。

不需要二次排版，不需要在不同平台之间来回调格式。

---

### 03｜如何使用

**三行命令跑起来：**

```bash
git clone https://github.com/nexu-io/html-anything
```

打开 http://localhost:3000，顶部的工具栏会自动显示你电脑上装了哪些 Coding Agent CLI。
选一个模板，粘贴你的内容，按下 ⌘+Enter。
然后你就能看到 AI 一行一行地把 HTML 渲染出来。SSE 流式传输，实时预览。
不喜欢随时打断，换 prompt 重新来。

Markdown 是草稿，HTML 才是给人看的最终形态。
过去不选 HTML 是因为手写太麻烦，但在 Agent 时代，你不应该再手写 HTML 了，让 AI 来。

---

### 04｜关注逛逛GitHub

这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛GitHub，后台对话聊天就行了。
