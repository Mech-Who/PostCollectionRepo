---
title: 185000 星的 Superpowers 插件，90% 的人只用了它 10% 的功能
date: 2026-05-16
tags: [AI编程, Superpowers, ClaudeCode, 工作流, 工程纪律, AI工具, 调试, 测试]
summary: 深度拆解 Superpowers 插件的 14 个核心 skill，重点剖析 brainstorming（9步完整流程）、systematic-debugging（四阶段+三次失败规则）、writing-plans（2-5分钟任务粒度+零占位符规则）、subagent-driven-development 和工作流收尾的最佳实践。
category: AI应用
status: 📥已采集
---

> **摘要：** Superpowers 不是给 AI 加能力，而是加纪律。本文深度拆解了 5 个最核心的 skill：brainstorming 的 9 步完整流程（含 Hard Gate 不写代码规则）、systematic-debugging 的四阶段调试法（三次失败必须停下来）、writing-plans 的 2-5 分钟任务粒度和零占位符规则、subagent-driven-development vs executing-plans 的选型策略，以及 finishing-a-development-branch 的干净收尾流程。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章的信息密度很高，但最让我触动的不是那些具体的 skill 用法，而是背后的核心理念：AI 缺的不是能力，是纪律。这个判断很敏锐——Claude/GPT 的"勤快"恰恰是最大的问题，它们太急于给出答案而跳过应有的流程。如果把AI视为一个"过于热心的新人"，那 Superpowers 就是在建立一套 SOP。我在实践中的体会是，systematic-debugging 的"三次失败规则"可能是最有实用价值的——遇到复杂 Bug 时，最消耗人的不是 bug 本身，是第六次、第七次无头苍蝇式的乱试。给自己设一个"三次上限"，失败了后退一步想架构层面的问题，这个节奏对人也同样适用。

## 📌 关键要点
- **核心方法**: Superpowers 的核心是行为约束而非功能增强 —— 每个 skill 本质上是纯文本的流程规范。brainstorming 的 HARD-GATE 确保设计闭环，systematic-debugging 的四阶段确保根因驱动修复。
- **踩坑经验**: 大多数用户只用了 brainstorming 的前 3 步（问问题），跳过了步骤 6-8（写 spec 文档并让用户审阅），导致执行阶段上下文漂移、记忆不一致。
- **适用场景**: 适合所有使用 Claude Code 的 AI 编程工作流。小项目也可用——spec 可以短但不能省。支持 subagent 的环境优先选 subagent-driven-development，避免上下文串扰。

## 原文

你有没有用 Claude Code 的时候遇到这种情况——

让它帮你加一个功能，三百行代码噼里啪啦就下来了，跑起来一看，逻辑对了七八成，但剩下那两成全是它自己发明的需求。

你说这是测试的 bug，它说好，又改了一通，结果把能跑的地方也顺手改坏了。

这不是 Claude Code 不够聪明。是它太"勤快"了——不问、不验、不收，直接上手干。

**Superpowers 解决的就是这个问题。** 不是给 Claude 加能力，而是给 Claude 加纪律。

这个插件在 GitHub 上六个月跑到 185,000 stars（v5.1.0，2026 年 5 月），但码哥观察了一下，大多数人装完之后用法是这样的：开一个新功能，喊一句 `/brainstorming`，然后一路回答问题，最后让它写代码。仅此而已。

相当于买了套瑞士军刀，每次只用开瓶器。

这篇文章从 Superpowers 的 SKILL.md 源文件出发，拆解那些大多数人没认真看过的核心 skill，把完整工作流跑通。

## Superpowers 是什么：不是插件，是工程纪律的文本分发

先说一个可能颠覆你认知的事情：**Superpowers 里的每一个 skill 本质上是一个 Markdown 文件**，里面写的是"当你遇到这类任务时，你必须按这个流程走"。

不是代码，不是工具调用，就是纯文本的行为约束。

这背后有一个很深刻的观察：AI 编程 Agent 缺的从来不是能力，而是**纪律**。

Claude 知道该写测试，但在"快速给我跑一遍看看"的语境下，它会跳过；Claude 知道 debug 要找根因，但你说"快帮我改一下"，它就直接猜着改了。

Superpowers 做的事情就是——用文本"强制执行"这些工程师该有的纪律，让 Claude 不管你怎么催，都不会绕过应走的流程。

插件目前包含 14 个 skill，分三类：

**测试类：** test-driven-development

**调试类：** systematic-debugging、verification-before-completion

**协作/工作流类：** brainstorming、writing-plans、executing-plans、subagent-driven-development、dispatching-parallel-agents、requesting-code-review、receiving-code-review、using-git-worktrees、finishing-a-development-branch、writing-skills、using-superpowers

下面拆解最核心的五个。

## brainstorming：有一道硬门，过不去就不许写代码

这是大多数人用得最多、也用得最浅的 skill。

多数人的用法是：喊 `/brainstorming`，回答几个问题，然后……让它直接开写。相当于只走了 brainstorming 的前三步，最关键的后六步全跳过了。

打开 brainstorming 的 SKILL.md，第一个硬约束是这样写的（原文引用）：

```
<HARD-GATE>Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it.</HARD-GATE>
```

注意这是 `<HARD-GATE>`，不是 "建议"，是"不管你觉得多简单，过不了这道门，一行代码都不许写"。

**完整的 brainstorming 流程是 9 步：**

1. 探索项目现状（看文件、commits、文档）
2. 如果有视觉问题，先提供可视化伴侣（独立消息）
3. 逐条问澄清问题（每次只问一个）
4. 提出 2-3 个方案并给出推荐理由
5. 按章节展示设计方案，每段都要确认
6. 把设计写入 `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` 并 commit
7. 自检 spec：扫描 TBD/TODO、内部矛盾、范围、歧义
8. 让用户审阅 spec 文件
9. 移交 writing-plans skill

**最容易跳过的是步骤 6-8。**

大多数人跑到步骤 4-5 就觉得"差不多了，直接写吧"，结果设计没有落到文档里，后面执行阶段 Claude 的"记忆"就开始漂移，做到一半忘了之前说好的接口怎么定义。

还有一个细节：brainstorming 明确规定，**它的终态只有一个——移交 writing-plans**。不许调用 frontend-design，不许调用 mcp-builder，只能移交 writing-plans。这强制让你走完整个设计→计划→实现链条，而不是跳着来。

码哥用这个 skill 做过一次重构任务，第一次走完整 9 步花了 40 分钟，感觉很慢。但后面执行阶段几乎没有返工。对比之前直接让 Claude 上手写，"设计"环节省了 30 分钟，但后来改了三轮，总时间反而多了两小时。

**有一个反直觉的设计：** brainstorming 里说，"如果你觉得这个项目太简单、不需要设计，那更要走流程。简单项目里的隐含假设，是浪费工作的最大来源。"

就连一个配置改动，也必须走完整流程，设计可以短（几句话），但不能省。

## systematic-debugging：四阶段，禁止没有根因就动手

这是码哥认为 Superpowers 里价值最被低估的 skill。

普通的调试姿势是：报错了 → 把错误贴给 Claude → 它说"可能是 X，试试改这里" → 你试了 → 没好 → 再贴 → 它说"那可能是 Y" → 反复横跳。

这种模式下，按照 Superpowers 里的数据：**系统调试平均耗时 2-3 小时；用 systematic-debugging，15-30 分钟**。

差距这么大的原因是：Claude 的默认模式是猜，systematic-debugging 强制它必须找到根因才能提修复。

**铁律（原文）：**

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

**四个阶段（必须按顺序，前一阶段没完成不许进下一阶段）：**

**Phase 1：根因调查**
- 完整读错误信息（不是"看一眼"，是"读完整"）
- 稳定复现步骤
- 检查最近的 git 变更
- 对多组件系统，在每个边界打诊断日志，先跑一次收集证据，再分析哪里断了

**Phase 2：模式分析**
- 找到同一个 codebase 里类似的、能跑通的代码
- 和坏的代码逐项对比差异（"每一个差异，不管多小，都列出来，不要假设那个没关系"）
- 理解依赖和假设条件

**Phase 3：单假设验证**
- 写下一个具体的假设（"我认为 X 是根因，因为 Y"）
- 做最小变更验证
- 不对的话：换新假设，不要叠加改动

**Phase 4：实现修复**
- 先写能复现问题的测试
- 只改一处
- 如果三次修复都没解决问题：停下来，讨论是不是架构层面的问题

**这里有一个最实用的设计：Phase 4 有个"三次失败规则"。**

如果试了 3 次修复都没有解决，systematic-debugging 要求你停下来，不再尝试第四次，而是退后一步讨论"是不是这个模式本身就有问题"。

这和大多数工程师的直觉是相反的——大多数人在第三次失败之后会更焦虑地试第四次、第五次。但每次额外的猜测修复，都在给代码引入新的不确定性，而且还在浪费时间。

Superpowers 里有一份"常见借口对照表"，码哥觉得写得非常准：

| 借口 | 真相 |
|------|------|
| "这个 issue 很简单，不用走流程" | 简单的 bug 也有根因，流程对简单问题反而更快 |
| "紧急情况，没时间调查" | 系统性调试比猜测快多了，"紧急"不是理由 |
| "先试一下再说" | 第一次就确立猜测模式，后面就一直