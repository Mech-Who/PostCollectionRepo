---
title: "强烈推荐看看这个演讲：Software Fundamentals Matter More Than Ever"
source: "微信公众号 - 逛逛GitHub"
url: "https://mp.weixin.qq.com/s/5J6OfK7MxqUY32OtRL5Aiw"
date: 2026-05-14
category: "AI应用"
depth: "🟡 标准"
tags: ["AI Coding", "工程基础", "DDD", "TDD", "Deep Modules", "Matt Pocock", "Claude Code", "Skill"]
---

## 一句话总结

Matt Pocock 在 AI Engineer 大会上的核心观点：AI 让写代码更快，但代码从来不廉价——真正用好 AI Coding 的开发者回归工程基础（统一语言、TDD、Deep Modules），而非追求 vibe coding 或 specs-to-code 的极端。

## 核心数据

| 项目 | 内容 |
|------|------|
| 演讲者 | Matt Pocock（前 Vercel 开发者布道师，Total TypeScript 作者，AI Hero 创始人） |
| 演讲标题 | Software Fundamentals Matter More Than Ever |
| 播放量 | 60 万（发布两周） |
| 开源仓库 | [mattpocock/skills](https://github.com/mattpocock/skills) |
| Star 数 | 7 万 |

## 核心观点

### 1. AI Coding 两个极端的陷阱

- **vibe coding**（凭感觉让 AI 写）：失控，不知道 AI 写了什么、为什么这么写。
- **specs-to-code**（详细规格丢给 AI）：假设代码是廉价品——但 AI 生成的代码和手写代码一样会腐烂、积累技术债。

> Matt 的定位：**把 AI 当作超级实习生——执行力强，但需要你给出清晰的方向和约束。**

### 2. 四大方法论

#### 方法论一：Grill Me —— 先被 AI 拷问，再写代码

在动手写代码前，让 AI 沿着设计决策树的每个分支拷问你，把模糊想法逼成清晰方案。

- **升级版 /grill-with-docs**：拷问过程中实时写入 `CONTEXT.md`
- **对比 SuperPowers Brainstorming**：Grill-with-docs 更适合已有代码库，需要对具体方案决策对齐并建立文档
- **本质**：AI 不会帮你做决策，它只加速你已经做出的决策。没想清楚的话，AI 加速的是混乱。

#### 方法论二：统一语言（Ubiquitous Language）

来源：Eric Evans《领域驱动设计》（2003）。让代码、开发者和领域专家说同一套术语。

- **AI 时代的放大效应**：AI 没有隐含上下文，术语不一致会被成倍放大。
- **实践**：项目根目录维护 `CONTEXT.md`，记录核心术语的精确定义。
- **真实案例**：Matt 在课程管理系统中，「Standalone Video」和「Pitch」的术语矛盾被 AI 当场发现，避免了后续命名和设计混乱。
- **Martin Fowler 补充**：统一语言的最大价值不是文档，而是迫使你在沟通中消除歧义。

#### 方法论三：TDD —— 控制节奏，不是写测试

在 AI Coding 语境下，TDD 的核心作用是**控制每一步的粒度**。

- **问题**：AI 太能写了，一口气几百行，难以验证。
- **TDD 流程**：Red（失败测试）→ Green（最少代码通过）→ Refactor（重构）
- **角色转变**：传统开发中 TDD 是质量保障，AI Coding 中 TDD 变成**过程控制**——小步快跑，每步有反馈。

#### 方法论四：Deep Modules —— 藏复杂，露简单

来源：John Ousterhout《软件设计的哲学》（2018）。

- **Deep Module**：功能丰富但接口简单（如 JavaScript 垃圾回收器）
- **反面**：功能不多但接口复杂的模块（如参数校验函数要传 10 个配置项）
- **AI 时代的价值**：AI 上下文窗口有限，Deep Modules 让它只需理解接口而非内部实现，认知负担大幅降低。
- **反直觉结论**：不是模块越小越好，而是封装得当才好。

### 3. 底层逻辑：管理认知负荷

四个方法论共同指向一个核心——**管理认知负荷**：

| 方法论 | 管理认知负荷的方式 |
|--------|------------------|
| Grill Me | 写代码前想清楚，减少返工 |
| 统一语言 | 消除术语歧义 |
| TDD | 控制每一步范围，避免一次性处理太多信息 |
| Deep Modules | 封装复杂性，每次只理解接口 |

### 4. 都不是新东西

- 统一语言 → 2003 年《领域驱动设计》
- TDD → 1999 年 Kent Beck 极限编程
- Deep Modules → 2018 年《软件设计的哲学》

**它们没有过时，在 AI 时代反而更重要了。** 当你有一个能一秒写 100 行代码的助手时，你需要的是更好的约束，不是更多的代码。

## 延伸资源

- 演讲视频：https://www.youtube.com/watch?v=v4F1gFy-hqg
- 开源 Skills 仓库：https://github.com/mattpocock/skills
- 完整工作流视频（1.5h）：YouTube 搜「Full Walkthrough: Workflow for AI Coding — Matt Pocock」
- 推荐阅读：《领域驱动设计》（Eric Evans）、《软件设计的哲学》（John Ousterhout）

## 我的理解

这篇文章触碰了一个关键问题：**AI Coding 时代，开发者的核心能力在迁移。** 过去考验的是「能不能写出来」，现在考验的是「能不能设计好」。代码生产成本的急剧下降，反而让架构设计、术语对齐、任务拆解这些「软技能」的稀缺性被放大了。

Matt 的四个方法论本质上都是**约束机制**——不是让 AI 更强，而是让 AI 的输出更可控。这和 Agentic Engineering 里「context engineering」的思路高度一致：决定 AI 产出质量上限的不是模型本身，而是你给它的上下文质量和约束精度。

另一层值得思考的是：这些方法论来自 1999~2018 年的经典软件工程，说明 AI 并没有推翻软件工程的基本规律——它只是改变了杠杆支点的位置。技术债、认知负荷、接口复杂度这些概念在 AI 时代不仅没有消失，反而因为代码产出速度的飙升而变得更加致命。
