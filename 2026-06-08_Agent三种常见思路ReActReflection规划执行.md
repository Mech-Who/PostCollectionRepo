---
title: Agent三种常见思路怎么选？ReAct、Reflection、规划执行
date: 2026-06-08
tags: [AI, Agent, ReAct, Reflection, 架构设计]
summary: 系统对比构建Agent的三种核心设计思路：ReAct（边思考边行动）、Reflection（检查结果）、规划执行（先规划后执行），并给出真实场景下的组合选择建议。
category: AI技术
depth: 深度
source_url: https://mp.weixin.qq.com/s/eS21r0kAF6-US_wbmgKLDg
source: weixin
status: 📥已采集
sync_status: ✅已同步
---

> **摘要：** Agent的本质是一个循环：看到目标→想下一步→调工具→看结果→再想下一步。文章系统对比了三种主流设计思路——ReAct（边思考边行动边观察，适合路径不确定的任务）、Reflection（让模型检查结果，适合格式易出错的任务）、规划执行（先生成计划再执行，适合复杂长任务），并指出真实场景通常是三种组合使用。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章把Agent的本质讲得很清楚——就是"循环（Loop）"。不管哪种设计模式，核心都是那个不断"想→做→看→想"的循环。理解了这个底层模型，再看三种变体就清晰了。

**为什么三种模式不是非此即彼：** 文章最实用的部分是"组合使用"的思路——先规划（Plan稳住大局），中间用ReAct（Action动态适应变化），最后用Reflection（Check保证质量）。这其实很像软件开发中的"设计→开发→测试"循环，在AI Agent架构中完美映射。

**与已有知识的连接：** 最近读的几篇Agent文章都在强调"确定性"和"可观测"——ReAct灵活但容易跑偏（不可控），规划执行可控但不够灵活。解决方向可能是给ReAct加边界约束（类似RLHF的思路），或者让规划执行支持动态重规划（类似动态规划的增量更新）。这也是目前OpenAI的Compaction思路在做的事情。

## 📌 关键要点
- **核心前提：** Agent本质是一个循环——看到目标→想下一步→调工具→看结果→再想下一步
- **ReAct（Reasoning+Acting+Observation）：** 最经典模式，Thought→Action→Observation循环，适合路径不确定的任务如故障排查，风险是容易"跑散"
- **Reflection（检查结果）：** 给Agent明确的"检查环节"，基于标准校验输出，适合结果易格式错误的任务，局限在于模型不知道正确答案时反思无效
- **规划执行（Plan-and-Execute）：** 先生成计划再按计划执行，适合复杂长任务，最大问题是计划跟不上变化
- **组合建议：** 先规划，中间用ReAct动态推进，最后用Reflection检查交付——真实场景的最佳实践

## 原文

文章介绍构建Agent的三种常见设计思路。

**核心前提：** Agent的本质是一个循环——看到目标→想下一步→调工具→看结果→再想下一步。

1. **ReAct（边思考边行动边观察）：** 最经典，Reasoning+Acting+Observation，典型循环Thought→Action→Observation→Thought，适合路径不确定的任务如故障排查，风险是容易"跑散"。

2. **Reflection（让模型检查结果）：** 给Agent明确的"检查环节"，基于明确标准校验输出，适合结果易有格式错误的任务，局限性在于模型不知道正确答案时反思无效。

3. **规划执行（Plan-and-Execute）：** 先生成计划再按计划执行，适合复杂长任务，最大问题是计划跟不上变化。

**选择建议：** 路径不确定用ReAct，结果易出错用Reflection，任务复杂用规划执行。真实场景通常组合使用：先规划，中间用ReAct动态推进，最后用Reflection检查交付。
