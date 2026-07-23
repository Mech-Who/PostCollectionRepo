---
title: "三器合一：gstack + Superpowers + OpenSpec 工程化 AI 编程实战"
date: 2026-05-18
tags: [AI编程, gstack, Superpowers, OpenSpec, 工程化]
summary: 通过完整案例演示 OpenSpec（需求管理）+ Superpowers（质量门禁）+ gstack（全流程管线）三套工具如何在一个 Claude Code 会话中自动串联，实现从需求对齐到发布归档的工程化 AI 编程流水线。
category: AI应用
source_url: https://mp.weixin.qq.com/s/j5_WRygYB_N4eagUCPSZwA
source: weixin
status: 📥已采集
depth: 深度
---

> **摘要：** 文章以"给应用加暗色模式"为完整案例，演示 OpenSpec（需求 DAG 依赖图）、Superpowers（HARD-GATE + TDD 铁律）、gstack（Browse 引擎 + 7 阶段 Sprint 管线）三套工具如何在同一 Claude Code 会话中自动串联。核心价值在于工具间不靠手动传数据，而是通过产物落盘和规则自检自动衔接。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章展示了 AI 编程工具链从"单个助手"走向"多工具编排"的演进方向。三个工具的职责划分非常清晰：OpenSpec 回答"做什么"、Superpowers 回答"做得好"、gstack 回答"怎么做"。它们自动串联的关键机制是 OpenSpec 的产物落盘 → gstack 的评审直接读文件 → Superpowers 的门禁被产物满足。对我最有启发的是"三套规则在同一个会话里自动生效、互相补位"的设计理念——不是拼图式集成，而是规则级融合。

## 📌 关键要点
- **核心方法**：用 DAG 依赖图做需求管理（OpenSpec），HARD-GATE + TDD 做质量门禁（Superpowers），Browse 引擎 + 7 阶段 Sprint 管线做流程管理（gstack）
- **踩坑经验**：不要手动传递数据给工具——让工具通过文件系统自动发现产物；不要三个工具交替使用——让它们在会话内自动触发
- **适用场景**：团队正在使用 Claude Code 做 AI 编程，需要工程化质量保障和发布流程的场景
- **核心命令链**：`/opsx:propose → /autoplan → (写代码) → /review → /qa → /ship → /opsx:archive`

## 原文
（原始推文内容）

## OpenSpec 管需求，Superpowers 管质量，gstack 管全流程

三个工具解决三个不同的问题，装在一起不冲突：

工具 | 管什么 | 核心机制
---|---|---
OpenSpec | 做什么 | DAG 产物依赖图，写代码前先对齐需求
Superpowers | 做得好 | HARD-GATE + TDD 铁律，自动拦截低质量代码
gstack | 怎么做、怎么发 | Browse 引擎 + 7 阶段 Sprint 管线

关键不是"三个工具都装上"，而是它们之间**怎么自动串联**。下面用一个完整案例讲清楚。

---

## 安装：三者共存的方式

装完之后，三个工具在同一个 Claude Code 会话里共存。OpenSpec 的 `/opsx:*` 命令、Superpowers 的 TDD 铁律、gstack 的 `/ship` `/review` `/qa` 技能，全部在同一个 REPL 里可用。

它们不互相覆盖，因为管的层次不同。OpenSpec 的产物存在 `openspec/` 目录，Superpowers 的规则存在 CLAUDE.md 和 skill 文件里，gstack 的状态存在 `.gstack/` 目录。三套状态互不干扰。

---

## 核心问题：它们之间怎么串联

这是最关键的部分。三个工具不是"你用完我再用"的接力赛，而是**在同一个会话里自动触发、互相衔接**。

### 串联点 1：OpenSpec 的产物 → gstack 的评审输入

OpenSpec 的 `/opsx:propose` 会生成四个文件：`proposal.md`、`specs/`、`design.md`、`tasks.md`。这些文件落盘后，gstack 的 `/autoplan` 能直接读取它们作为评审输入。

具体机制：`/autoplan` 启动 CEO → design → eng → DX 四类评审。每个评审角色会读取当前工作区的文件。因为 OpenSpec 的产物就在 `openspec/changes//` 目录下，评审角色自然能读到 proposal 和 specs。

你不需要手动复制粘贴。OpenSpec 写完产物，gstack 的评审直接读文件。

### 串联点 2：Superpowers 的 HARD-GATE → 自动拦截编码

Superpowers 的 `brainstorming` skill 有一个 HARD-GATE：

    Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it.

这意味着：即使你跳过了 OpenSpec 直接说"帮我加个功能"，Superpowers 也会强制你先走设计流程。它不需要知道 OpenSpec 的存在——它只关心"设计有没有被批准"。

如果 OpenSpec 已经生成了 `design.md`，你把它展示给 Superpowers 看，它会把这份设计当作"已批准的设计"，HARD-GATE 自动放行。这就是串联：OpenSpec 的产物满足了 Superpowers 的门禁条件。

### 串联点 3：Superpowers 的 TDD → gstack 的 /review 自动生效

Superpowers 的 TDD 铁律要求"先写失败测试再写代码"。这个过程不需要你手动触发——它是 skill 文件里的规则，Claude Code 每次写代码时自动遵守。

写完代码后，你运行 gstack 的 `/review`。`/review` 不关心代码是怎么写出来的——它只看 diff。但它会发现：因为 TDD 铁律的存在，每个功能都有对应的测试。`/review` 的审查质量因此更高，因为它有测试作为行为契约。

### 串联点 4：gstack 的 /ship → OpenSpec 的 /opsx:archive

`/ship` 发布完成后，你运行 `/opsx:archive`。归档过程读取 `openspec/changes//` 下的 Delta 规范，自动合并到 `openspec/specs/` 主规范里。

归档不触发发布，发布不触发归档。它们是两个独立步骤，但顺序固定：先 `/ship` 上线，再 `/opsx:archive` 收尾。

---

## 举个例子：给应用加暗色模式

一个功能从想法到上线的完整流程。重点不是"做了什么"，而是**每一步怎么触发下一步、工具之间怎么衔接**。

### 第 1 步：OpenSpec 生成需求产物

    /opsx:propose add-dark-mode

OpenSpec 的 DAG 引擎解析依赖关系，自动生成四个产物：

    openspec/changes/add-dark-mode/
    ├── proposal.md          ← 为什么做
    ├── specs/ui/spec.md     ← 需求场景（GIVEN/WHEN/THEN）
    ├── design.md            ← 技术方案（CSS 变量 + Context）
    ├── tasks.md             ← 任务清单（4 组 8 个子任务）
    └── .openspec.yaml       ← 变更元数据

### 第 2 步：gstack /autoplan 读取产物做评审

    /autoplan

`/autoplan` 自动串起四类评审。每个评审角色读取 `openspec/changes/add-dark-mode/` 下的文件：

### 第 3 步：Superpowers TDD 铁律自动生效

你没有手动调用 Superpowers 的任何命令。TDD 铁律是 skill 文件里的规则，Claude Code 写代码时自动遵守。

### 第 4 步：gstack /review 审查代码

    /review

`/review` 扫描当前分支的 diff。因为 Superpowers 的 TDD 铁律确保了每个功能都有测试，`/review` 的审查质量更高——它可以用测试作为行为契约来验证实现是否正确。

### 第 5 步：gstack /qa 浏览器验收

    /qa

`/qa` 用 Playwright Chromium 打开应用，执行真实用户操作。

### 第 6 步：gstack /ship 发布

    /ship

`/ship` 自动执行一系列操作，包括测试、覆盖率审计、版本升级、CHANGELOG 生成、推送、创建 PR。

### 第 7 步：OpenSpec /opsx:archive 归档

    /opsx:archive add-dark-mode

归档后，`openspec/specs/` 目录始终反映系统当前状态。下次再加功能时，OpenSpec 的 AI 会读取这些 specs 作为上下文。

---

## 串联机制

整个流程中，你手动输入的命令只有 7 个：

    /opsx:propose → /autoplan → (写代码) → /review → /qa → /ship → /opsx:archive

三个工具之间的衔接不需要你手动传递数据。OpenSpec 的产物落盘后，gstack 的评审角色直接读文件。gstack 的评审结论满足了 Superpowers 的 HARD-GATE 条件。Superpowers 的 TDD 铁律确保了 /review 有测试可依。

这就是"三器合一"的核心：不是三个独立工具的拼凑，而是**三套规则在同一个会话里自动生效、互相补位**。
