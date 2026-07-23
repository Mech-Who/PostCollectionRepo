---
title: AI 写的 React 全是坑？Million.js 作者祭出「代码体检」神器，GitHub 狂揽近万 Star！
date: 2026-05-18
tags: [React, React Doctor, 代码质量, AI编程, 代码审查]
summary: Million.js 作者 Aiden Bai 发布 React Doctor，一条命令即可对 React 代码进行 0-100 健康评分，覆盖状态管理、安全、性能、无障碍、包体积、架构六大维度，并支持 Agent 安装模式从源头预防坏代码。
category: 工具推荐
source_url: https://mp.weixin.qq.com/s/wY5OF90lxngpDQ2N3OUKJQ
source: weixin
status: 📥已采集
depth: 标准
---

> **摘要：** React Doctor 是 Million.js 作者推出的 React 代码质量审计工具，扫描 6 大维度（State & Effects、Security、Performance、Accessibility、Bundle Size、Architecture）并输出 0-100 健康评分。其 Agent 安装模式能自动检测项目中的 AI Agent 并写入规则文件，从源头减少 Agent 生成坏代码的概率。配套 GitHub Action 和在线排行榜 react.review 也已上线。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章介绍的工具 React Doctor 反映了 AI 编程进入新阶段的关键信号：当 AI 生成代码成为常态，代码质量保障工具必须跟上。"Agent 安装模式"的设计非常聪明——与其写完再修，不如在 Agent 写代码之前就让规则成为上下文的一部分。六大维度的检测规则也直接针对 AI Agent 最常见的问题（useEffect 滥用、缺少 cleanup、安全性缺失等）。对于大量使用 AI 写 React 的团队，这个工具应该作为 CI 标配。

## 原文
（原始推文内容）

## 一个扎心的问题：你的 Agent 写的 React，到底有多烂？

2026 年，AI 写代码已经不新鲜了。Cursor、Claude Code、Codex……各家 Agent 都能帮你从零搭一个 React 项目，速度快到离谱。

但一个越来越明显的问题浮上来了：**Agent 写的 React 代码，质量堪忧。**

`useEffect` 里塞 fetch 请求、state 派生逻辑乱套、没有做 cleanup 的副作用到处飘、`dangerouslySetInnerHTML` 随手就用、barrel import 把 bundle size 撑到爆炸——这些问题在 AI 生成的代码里高频出现，但人工 review 又极其耗时。

尤其是当你让 Agent 连续迭代、自动修 bug 的时候，它可能修了一个问题，又悄悄引入三个新的反模式。

**代码写得快，谁来兜底质量？**

Million.js 的作者 Aiden Bai 给出了他的答案：**React Doctor**。

## 一条命令，给你的 React 代码做全身体检

React Doctor 的核心理念可以用 GitHub 上的那句 slogan 概括：

> "Your agent writes bad React. This catches it."

「你的 Agent 写了一堆烂 React 代码，这个工具帮你兜住。」

用法极其简单，在项目根目录跑一条命令：

```bash
npx -y react-doctor@latest .
```

它会扫描你的整个代码库，输出一个**0 到 100 的健康评分**，并附带可执行的诊断建议。

评分分三档：

*   **75 分以上**：Great，代码质量过关
*   **50 到 74 分**：Needs work，有明显需要改进的地方
*   **50 分以下**：Critical，赶紧修

## 六个维度，把 AI 写的坑逐个揪出来

React Doctor 的扫描覆盖六大维度，每一个都在针对 AI Agent 的常见失误：

**1. State & Effects（状态与副作用）**

AI 最爱犯的错。`useEffect` 里做数据获取、state 之间互相派生触发连锁更新、没有 cleanup 的定时器和订阅。React Doctor 内置了 `no-fetch-in-effect`、`no-derived-state-effect`、`no-cascading-set-state` 等规则，直接对准这些高频坑。

**2. Security（安全）**

`dangerouslySetInnerHTML` 带来的 XSS 风险、GET handler 里的服务端状态变更——AI 在处理安全相关逻辑时经常缺乏边界意识，React Doctor 会把这类问题标记为 error 级别。

**3. Performance（性能）**

barrel import 导致的 tree-shaking 失败、渲染函数内部声明组件、array index 做 key——这些性能陷阱 Agent 踩得非常勤快。

**4. Accessibility（无障碍）**

缺少 alt 属性、autofocus 滥用、交互元素缺少键盘支持。AI 对无障碍的重视程度远低于人类开发者。

**5. Bundle Size（包体积）**

dead code 检测、未使用的导出和文件扫描。React Doctor 集成了 knip 做全项目级的死代码检测，帮你找到那些 Agent 生成后又弃用的文件。

**6. Architecture（架构）**

组件拆分是否合理、渲染逻辑是否过度嵌套。这一层把审查从单个规则提升到了项目结构级别。

## 最狠的一招：直接教你的 Agent 学规矩

React Doctor 有个特别值得关注的功能：**Agent 安装模式**。

```bash
npx -y react-doctor@latest install
```

跑完这条命令，它会检测你项目里用了哪些 AI Agent（Claude Code、Cursor、Codex、OpenCode 等 50 多个），然后自动往项目里写入对应的规则文件——SKILL.md、AGENTS.md、.cursorrules。

这意味着什么？你的 Agent 在写代码之前，就已经知道了 React Doctor 的所有规则。**它从源头上减少了 Agent 写出坏代码的概率。**

这个设计思路很有意思：与其写完再修，不如让 Agent 写之前就知道什么能写、什么别碰。

## 不只是 CLI：GitHub Action + 在线排行榜

React Doctor 的野心不止于本地命令行。

**GitHub Action 原生支持**

你可以直接在 CI 流水线里接入 React Doctor。它作为 GitHub Marketplace 上的 composite action，支持在每次 PR 和 push 时自动扫描，并把结果以评论的形式贴回 PR 页面。

**React Review 在线平台**

React Doctor 还有一个配套网站 react.review，可以直接粘贴 GitHub 仓库 URL 进行在线审计，并且有一个**公开排行榜**，展示扫描过的 React 项目评分排名。

## AI 写代码的下半场：从生成到守门

React Doctor 背后折射出的趋势值得重视：**当 AI Agent 写代码变成常态，代码审查工具的需求会跟着爆发。**

现在的 Agent 擅长快速生成功能代码，但对框架的最佳实践、安全边界、性能陷阱的理解仍然有限。人类 reviewer 不可能每一行都 review 到，自动化的专项审查工具就成了刚需。

React Doctor 瞄准的就是这个缺口：**Agent 写完，工具兜底。**再进一步，通过 install 模式把规则前置到 Agent 的上下文里，从源头降低出错率。

如果你的团队正在大量使用 AI Agent 写 React，建议跑一次 React Doctor 看看分数。结果可能会让你重新评估对 Agent 生成代码的信任度。
