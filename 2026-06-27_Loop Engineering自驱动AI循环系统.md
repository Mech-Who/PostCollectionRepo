---
title: 手动Prompt已OUT！Loop Engineering深度实战：设计自驱动AI循环系统
date: 2026-06-27
category: AI应用
depth: 深度
layer: layer2
tags: [AI Agent, Loop Engineering, 自动化, MCP, 工作流设计, Claude Code, 自驱动循环, 生产模式]
summary: Loop Engineering 项目提供 7 大生产级 Pattern + 3 大 CLI 工具 + L0-L3 分阶段落地指南，帮助开发者从"手动 Prompt 代理"升级为"设计自驱动 AI 循环系统"。核心理念：你不应该亲自 Prompt 编码代理，而应该设计循环来驱动它们。
source_url: https://mp.weixin.qq.com/s/x-VPVPYXIJh7Qlp2IggZbw
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** Loop Engineering（GitHub: cobusgreyling/loop-engineering）是一个范式级项目，将 AI 编码代理的使用方式从"手动 Prompt"升级为"设计自驱动循环系统"。核心提炼了五大 Building Blocks（调度/工作树隔离/技能持久记忆/MCP连接器/子代理 Maker-Checker）+ Memory/State，并提供 7 个生产级 Pattern（Daily Triage、PR Babysitter、CI Sweeper 等）、3 大 CLI 工具（loop-init/loop-audit/loop-cost），以及完整的 L0→L3 分阶段落地检查清单。

## 我的理解

> 由小林生成，供小涵审阅修改

Loop Engineering 解决的是一个我一直在隐隐感受到但没能清晰表达的问题：**当 AI 编码代理（Claude Code/Codex/Grok）越来越强时，瓶颈不再是"怎么写好一个 Prompt"，而是"怎么持续协调多个代理完成复杂长期目标"。**

这个项目最核心的洞察是 **"设计循环，而非设计 Prompt"**。它的五大原语（调度、Worktree 隔离、Skills 持久意图、MCP 连接器、Maker/Checker 子代理）实际上构成了一个 AI Agent 操作系统的内核——每个原语都是正交的、可组合的。这和我之前在 WorkBuddy 上建立的 git worktree 安全机制、Skill 体系、以及子 Agent 协作架构高度吻合，证明这些模式在不同工具间是收敛的。

最值得关注的是 **L0→L3 分阶段落地策略**：L0 只文档化意图 → L1 纯报告不行动 → L2 小范围自动修复 → L3 全自动。这种"先观测、再行动、最后自动化"的渐进式方法论，是 AI 自动化领域被严重低估的最佳实践。太多人一上来就想全自动，结果造出无限修复循环和 Token 黑洞。

另一个亮点是 **loop-audit 的量化评分体系**（0-100 分），把"我准备好自动化了吗"从一个模糊的感觉变成了可衡量的指标。这对于工程团队管理 AI 自动化风险非常有价值。

对于我们的 PostCollection 知识体系，Loop Engineering 可以直接对应为 **Layer 2 通用技能**——它在本质上和我们的知识管线、Worktree 安全机制、Skill 分层加载是同一种思想的不同实现。

## 📌 关键要点

- **核心理念转变**：从"手动 Prompt AI 代理"转变为"设计循环系统来驱动 AI 代理"。Peter Steinberger、Boris Cherny（Anthropic Claude Code 负责人）、Addy Osmani 都表达了相同观点。
- **五大 Building Blocks + Memory**：
  1. **调度（Automations/Scheduling）**：循环的心跳，没有调度就只是单次运行
  2. **Worktrees（工作树隔离）**：安全并行执行的关键，避免多代理同时编辑同一文件
  3. **Skills（持久意图）**：项目的"持久记忆"，防止每次运行都从零推导
  4. **MCP/Connectors**：连接真实世界工具，least-privilege 权限
  5. **Sub-agents（Maker/Checker Split）**：写代码的代理不适合自己验证，强制分离
  - **Memory/State**：STATE.md 作为 spine，每次运行始读终写
- **7 大生产级 Pattern**：
  - Daily Triage（每日扫描 CI/issues/PRs 生成摘要）
  - PR Babysitter（自动 shepherd PR 通过 review/CI/rebase）
  - CI Sweeper（响应 failing checks，最小修复，3次尝试后升级）
  - Dependency Sweeper（Worktree 中 patch CVE/stale deps）
  - Changelog Drafter（自动生成分类 release notes）
  - Post-Merge Cleanup（处理 TODOs/deprecations/tech debt）
  - Issue Triage（去重/评分/label 新 issues）
- **3 大 CLI 工具**（全部 npm 发布，npx 即可用）：
  - `loop-init`：脚手架生成 + budget/run-log
  - `loop-audit`：最核心工具，量化 Loop Readiness Score（0-100），含 activity detection
  - `loop-cost`：Token 消耗估算
- **渐进式落地 L0→L3**：L0 Draft（文档化）→ L1 Report（triage → state，无 auto-action）→ L2 Assisted（小 auto-fix + verifier）→ L3 Unattended（全自动）
- **关键安全机制**：Denylist（.env/secrets/auth 永不 auto-edit）、Human Gate 始终存在、escalation triggers、bot 身份清晰标识
- **跨工具矩阵**：项目提供了 Grok/Claude Code/Codex/Cursor/Windsurf 的完整能力对比（docs/primitives-matrix.md），证明"能力收敛，工具名称不同"

## 原文

> 来源：微信公众号「如此才是」，作者小K，2026-06-27

### 从"手动Prompt代理"到"设计自驱动循环系统"

在 AI 编码代理（Grok、Claude Code、Codex、Cursor 等）日益普及的今天，开发者面临的核心痛点已从"如何写好单个 Prompt"转变为"如何持续 orchestrate 多个代理完成复杂、长期目标"。

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — Peter Steinberger
>
> "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops." — Boris Cherny（Anthropic Claude Code 负责人）
>
> "Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go." — Addy Osmani

Loop Engineering（GitHub: cobusgreyling/loop-engineering）是这一范式转变的实用参考实现。提供 7 个生产级 Pattern、Starter Kits、3 大 CLI 工具（loop-init、loop-audit、loop-cost）以及完整文档体系，帮助开发者从"自己反复 Prompt"升级为"设计持久、自治、可观测、可安全扩展的循环系统"。

项目提供交互式 Pattern Picker 与 Readiness Simulator，完美呼应"工具无关、Production-ready"的定位。

### 一、核心概念：Loop，五大原语 + Memory

一个 Loop 是递归目标（recursive goal）：定义目的，AI 通过迭代（常结合 sub-agents、verification、外部状态）持续工作，直到目标完成或主动交接给你。

**五大 Building Blocks + Memory：**

1. **Automations / Scheduling（调度/自动化）**：循环的心跳。没有调度就只是单次运行。
2. **Worktrees（工作树隔离）**：安全并行执行的关键。避免多个代理同时编辑同一文件导致 merge hell。
3. **Skills（技能/持久意图）**：项目的"持久记忆"。通常是 SKILL.md（+ 可选脚本），编码项目规范、历史 incident 教训等。防止每次运行都从零推导"intent debt"。
4. **Plugins & Connectors（MCP）**：连接真实世界工具。MCP 成为共同基座，支持读写 Linear/Jira、Slack/Discord、GitHub PRs、数据库、部署等。
5. **Sub-agents（Maker / Checker Split）**：可靠性核心。写代码的代理不适合自己验证。典型拆分：Implementer → Verifier（运行测试 + gates）。

**Memory / State**：模型本身无跨会话长期记忆。必须读写持久存储：STATE.md（或模式特定 state 文件）。良好 state 回答"当前在做什么？上次尝试结果？什么在等人？"。

**跨工具矩阵亮点**：调度、Skills、Sub-agents、State 在不同工具中实现不同但能力趋同。"能力收敛，工具名称不同"，设计 loop 时可工具无关地映射原语。

**Loop 解剖学（典型流程）**：
Schedule → Triage Skill → Read/Write STATE → Isolated Worktree → Implementer Sub-agent → Verifier Sub-agent（tests + gates）→ MCP/Connectors → Human Gate → 循环回 Schedule

### 二、7 大生产级 Pattern

所有 Pattern 都强调分阶段 rollout（L1 report-only → L2 assisted → L3 unattended）、明确 state schema、skills、verification、failure modes 与 human gate。

1. **Daily Triage**（1d cadence）：每天扫描 CI/issues/PRs/commits/chat，生成优先级摘要更新 STATE.md。Week 1 严格 report-only。
2. **PR Babysitter**（5-15m）：自动 shepherd PR 通过 review/CI/rebase/merge。Human 始终在 judgment seat。
3. **CI Sweeper**（5-15m）：响应 failing checks，最小修复，分类 flakes，3次尝试后 escalate。
4. **Dependency Sweeper**（6h-1d）：Worktree 中 patch CVEs 与 stale deps，major/denylist 始终 human gate。
5. **Changelog Drafter**（低风险，1d）：扫描 merges/commits 生成分类 release notes draft。
6. **Post-Merge Cleanup**（低风险，1d-6h）：处理 TODOs/deprecations/tech debt。
7. **Issue Triage**（低风险，2h-1d）：去重、评分、label 新 issues。

### 三、3 大 CLI 工具

1. **loop-init（v1.2）**：Scaffold starters + budget/run-log。`npx @cobusgreyling/loop-init . --pattern daily-triage --tool grok`
2. **loop-audit（v1.4，最核心）**：Loop Readiness Score（0-100），对应 L0-L3。含 activity detection。`npx @cobusgreyling/loop-audit . --suggest`
3. **loop-cost**：Token spend estimator。`npx @cobusgreyling/loop-cost --pattern daily-triage --level L1`

**高效使用 workflow**：loop-init → loop-cost → loop-audit → Week 1 report-only → 逐步启用 → 持续 audit

### 四、技术原理与架构

**架构核心**：原语正交组合 + 渐进添加。最小 viable loop = Scheduling + 1 个 triage skill + STATE.md。

**关键实现机制**：
- **隔离与安全**：worktree 独立 working directory，Denylist（.env/secrets/auth 等永不 auto-edit）
- **验证可靠性**：Maker/Checker 强制分离
- **可观测与成本控制**：STATE.md + loop-run-log.md + loop-budget.md
- **Human in the loop**：Human Gate 始终存在，明确 escalation triggers
- **Failure modes**：无限 fix loop、verifier theater、token burn、state bloat、noise、comprehension debt

**分阶段落地 checklist（L0-L3）**：
- L0 Draft：仅文档化 intent
- L1 Report：triage → state，无 auto-action
- L2 Assisted：小 auto-fix + verifier
- L3 Unattended：全自动

### 五、最佳实践

- 永远从 report-only + audit 开始，验证 triage 质量后再加 action
- 使用 starters + loop-init 加速
- 严格 denylist + allowlist + least-privilege MCP
- 持续 prune state，记录 human override
- 复杂场景考虑 multi-loop coordination

Loop Engineering 将"提示工程"升级为"控制系统工程"，提供了从概念、模式、工具、落地到自举的完整闭环。

## 相关笔记

- [[harness-engineering]]：AI 编码代理的 harness 工程化，Loop Engineering 是其自然延伸——从单次 harness 到持续循环
- [[AI-Native 开发工具]]：Loop Engineering 是 AI-Native 开发工具链的关键一环
- [[知识管线自动化]]：Loop Engineering 的 Daily Triage + Issue Triage Pattern 可直接应用于 PostCollection 的自动化知识管线
