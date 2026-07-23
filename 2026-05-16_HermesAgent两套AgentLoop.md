---
title: "Hermes Agent 中的两套 Agent Loop"
date: 2026-05-16
tags: [AI技术, Agent, 架构设计, Hermes, RL训练]
summary: Hermes Agent源码中同时存在两套Agent Loop——AIAgent（面向用户交互）和HermesAgentLoop（面向RL rollout）。分析指出不同场景的目标函数已变时，循环层不应强行共用，复用点应在工具调度层而非循环体本身。
category: AI技术
status: 📥已采集
---

> **摘要：** Hermes Agent 源码中同时存在两套 Agent Loop：`AIAgent`（面向用户交互，数千行，处理流式/重试/打断/上下文压缩等）和 `HermesAgentLoop`（面向 RL rollout，轻量简洁，专注 async/并发/token级数据）。核心启示：不同场景的目标函数变了，循环层就不该强行共用——复用点应放在工具调度层，而非循环体本身。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章的价值不在于 Hermes 本身，而在于它提供了一个重要的架构决策案例：**不要为了"统一抽象"而强行合并本质上不同的控制流**。AIAgent 优化的是用户体验和鲁棒性，HermesAgentLoop 优化的是吞吐和训练信号精度——它们都叫 Agent Loop，但回答的不是同一个工程问题。

这个决策原则可以泛化到很多系统设计中：当两个场景的"目标函数"已经不同，表面相似的抽象层就应该拆开，而不是强行收敛。复用点放在基础设施层（工具调度、结果存储），业务控制流各自独立。

## 📌 关键要点
- **AIAgent**：面向用户交互（CLI/Gateway/Telegram/Discord），处理流式输出、Provider容错、上下文压缩、用户中断、预算耗尽Grace Call、子Agent委派、插件钩子
- **HermesAgentLoop**：面向RL rollout（被Atropos调用），专注async并发、token/logprobs/masks、tool+reward同一sandbox
- **核心原则**：不合成一个超级Loop，因为两个场景的目标函数完全不同
- **复用策略**：不共用循环体，而是公用底层工具调度层（handle_function_call、工具结果预算、持久化基础设施）
- **架构启发**：上层按场景定义各自的循环控制策略，下层复用工具调度和基础设施

## 原文

### 两套 Agent Loop 的定位

1. **AIAgent**（`run_agent.py`）
   - 对应 CLI、Gateway、Telegram、Discord 等面向人的入口
   - 处理：流式输出、Provider容错、上下文压缩、用户中断、预算耗尽Grace Call、子Agent委派、插件钩子
   - 复杂度来自"调模型失败以后怎么办"，而非"调模型"这一步
   - 数千行代码，是一条完整的交互控制链

2. **HermesAgentLoop**（`agent_loop.py`）
   - 被 Atropos 调起来做 rollout（RL训练场景）
   - 关键要求：async（并发跑大量rollout）、token/logprobs/masks（供GRPO训练）、工具执行和reward验证在同一个sandbox、循环体轻量
   - 产出 AgentResult + managed_state + ScoredDataItem(tokens, masks, scores) → GRPO trainer

### 核心启示
不合成一个"统一循环"。用户交互和RL训练这两个场景的目标函数完全不同，强行融合会导致循环复杂度过高、可靠性降低。复用点不在 Loop 本身，而在工具执行链路。
