---
title: Matt Pocock 开源 skill：技能描述 Token 成本狂降 63%，AI 自主判断技能调用
date: 2026-06-18
category: AI应用
depth: 标准
layer: layer2
tags: [MattPocock, skills, Token优化, AI工程, 技能系统, VibeCoding, TypeScript]
summary: TypeScript 大神 Matt Pocock 更新了其 skills 项目 v1 版本，核心改进包括：技能描述 Token 成本降低 63%，引入用户主动调用/模型自主调用两类技能，新增 /ask-matt 元技能路由器，以及 /codebase-design、/domain-modeling 等新技能。
source_url: https://mp.weixin.qq.com/s/JbGJzgSL53wvuMmP4Dlr0A
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** Matt Pocock 的 skills v1 版本是一次重要的架构升级。核心变化是将技能分为"用户主动调用"和"模型自主调用"两类，大幅精简技能描述文字以降低 Token 成本，并新增 /ask-matt 元技能。这篇文章分享了 Matt 的 Skill 设计哲学，尤其是"认知负担更多地放在用户身上"这一观点，对 WorkBuddy 的 Skill 设计有直接参考价值。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章虽然是一篇编译报道，但 Matt Pocock 的 Skill 设计哲学非常值得 WorkBuddy 参考：

1. **Token 成本降低 63% 是怎么做到的？**——核心不是压缩文字，而是架构调整：把大量技能从"模型自动调用"改为"用户手动调用"。模型不再需要在每次推理时都扫描所有技能的描述，只需要在用户明确触发时才加载。这个思路对 WorkBuddy 的 Skill 三层加载规范（L1/L2/L3）是一个很好的印证。

2. **用户主动调用 vs 模型自主调用的分界**——Matt 的设计核心是：涉及决策和流程把控的技能必须用户手动触发（避免失控）；诊断类、修复类的技能可以让 AI 自主判断。这个分界点很精确，WorkBuddy 的 Skills 也可以按这个逻辑重新审视分类。

3. **/ask-matt 元技能路由器**——本质上是把 Matt 本人的工程思考框架打包成一个"总指挥" Skill。你输入一个任务，它先分析性质，然后推荐最合适的技能组合和流程。这跟 knowledge-workflow-manager 的"总控 T 台"定位异曲同工。

4. **"认知负担更多地放在用户身上"**——这句 Matt 的原话值得细品。现在的 AI 工具都在追求"全自动"，但 Matt 反向思考：把控制权交还给用户，让用户能理解每一步、能纠错。这与 GSD/BMAD 等方法"试图掌控整个流程"形成鲜明对比。对 WorkBuddy 来说，Skill 应该是"增强用户能力"而不是"替代用户决策"。

5. **writing-great-skills 的重写**——Matt 花了 6 小时和一个 Agent 一起思考，定义了一套词汇表并写入 skill。这个"人+AI 协作提炼方法论"的工作方式也值得学习。

## 原文

### Matt Pocock 开源 skill：技能描述 Token 成本狂降 63%，AI 自主判断技能调用

编辑 | 林芯

如果你写 TypeScript，大概率绕不开 **Matt Pocock** 这个名字。刚刚，TypeScript 大神 Matt Pocock 更新了 GitHub 上超 13w star 的项目 mattpocock/skills。

就像 Matt 在博客里介绍："这些是我每天用来做真正工程开发的智能体技能，而不是靠感觉写代码（Vibe Coding）。"

这次 v1 版本更新，直接让"技能描述的 Token 成本降低了 63%。"

### AI 有了工程直觉？自行判断技能触发的时机

这是 v1 最重大的架构升级之一。Matt 把技能明确分为两类：

- **用户主动调用**：必须由你手动输入才会触发。适合需要你把控节奏、涉及决策的流程。
- **模型自主调用**：AI 根据当前任务上下文，自己判断是否需要调用。

关键变化：
- /grilling（拷问）变为模型可调用
- /diagnosing-bugs 更新为模型可调用
- 限制套娃：用户调用技能可以调用模型调用技能，但不能调用其他用户调用技能

### "总指挥"角色登场

/ask-matt 是一个用户触发的路由器：
- 你把一个真实任务或问题扔进去
- 它先分析任务性质，然后推荐最合适的技能组合和流程
- 接着指导按顺序执行：需求拷问 → 领域建模 → 架构设计 → TDD → 代码实现 → Grill 验证

### 更多硬核新 skill

- **/codebase-design**：深模块（Deep Module）架构方法论
- **/domain-modeling**：领域建模技能，维护 CONTEXT.md 和 ADR
- **/writing-great-skills**：关于如何把写作和编辑技能做好的参考指南

### Token 成本降低的真相

主要是上下文负载问题：把大量技能从"模型自动调用"改为"用户手动调用"，同时大幅精简了 skill 的描述文字。

**Matt 在评论区的一句话值得关注：** "我更希望认知负担更多地放在用户身上。GSD、BMAD 和 Spec-Kit 等方法试图通过掌控整个流程来提供帮助。但与此同时，它们也剥夺了你的控制权，使流程中的错误难以解决。"

## 相关笔记
- [[2026-06-18_Harness工作流评测系统]] — 同为 AI 工程化方法论，Harness Eval 提供的是评测视角
- [[2026-05-XX_Skill分层加载]] — WorkBuddy 的 L1/L2/L3 三层加载与 Matt 的用户/模型调用分类有相似性
