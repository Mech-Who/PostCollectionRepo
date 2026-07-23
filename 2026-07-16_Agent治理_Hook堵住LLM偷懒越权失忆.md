---
title: Agent 治理：用 Hook 堵住 LLM 的偷懒、越权与失忆
date: 2026-07-16
category: AI技术
depth: 深度
layer: layer2
tags: [Agent治理, Hook拦截, LLM安全, 长文本Offload, HITL, DECO, 上下文失忆]
summary: DECO数据仓库Agent引擎通过基于Hook链的护栏体系——长文本完整性Offload、危险操作HITL确认、上下文联动闭环——系统性解决LLM的偷懒、越权与失忆三大问题，实现"Prompt定意图，Skill定规矩，框架Hook定边界"。
source_url: https://mp.weixin.qq.com/s/ISwjIw5lj7JlcQJV7BOx5g
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 腾讯DECO团队在实践中发现，LLM在生产环境中存在三类核心问题：长脚本偷懒截断、越权操作、上下文失忆。本文提出了基于"Hook链"的解决方案——在Agent框架的Hook切面上挂载拦截逻辑，包括长文本读写两侧Offload（降低90%输出token）、危险操作HITL确认（物理阻断越权）、以及"Hook采集→state存储→Attachment注入"的上下文联动闭环。核心理念是：能用确定性兜底的，别交给模型。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章是对我之前见过的"Prompt定意图，Skill定规矩"理念的重要补充——**"框架Hook定边界"**。三层分工非常清晰：

- **Prompt** 定义Agent的意图和目标
- **Skill** 定义操作的标准流程和边界
- **Hook** 在框架层面强制兜底，模型绕不过去

三个核心方案中有两个对我当前工作有直接启发：

1. **长文本"读写两侧Offload"**：把长脚本全文存到沙箱文件，LLM上下文里只留引用句柄。这一招解决了LLM处理长文本时"假装写完了"的问题——模型只输出路径，框架从文件加载全文。这个思路可以应用到我们自己的Agent开发中。

2. **上下文联动闭环**：最精妙的设计。"Hook采集→state存储→Attachment注入"——Agent执行改表操作后，Hook自动触发下游风险分析，结果自动注入下一轮Prompt。这比让LLM自己去检查靠谱得多：把"主动查"变成"框架推"。

3. **DangerousToolGuard**：在beforeTool切面上挂载，通过配置文件定义危险工具清单，执行前弹窗确认。物理层面的防护，模型能力再强也绕不过if语句。

推荐与 [[2026-07-17_Google开源78个AgentSkills_不到一天1.4万star]] 和 [[2026-06-08_Anthropic公开内部Skill方法论]] 联动阅读，三篇共同构成了"Agent工程实践"的完整拼图。

## 📌 关键要点
- **核心方法**：Hook链护栏体系（Offload + HITL + 联动闭环）
- **踩坑经验**：
  - LLM不能靠prompt防止越权操作，必须在框架层面物理阻断
  - 长文本处理中，模型倾向于截断和占位略写，需要Offload策略
  - 让LLM自己执行"检查步骤"不可靠，应由Hook自动触发并注入
- **适用场景**：数据仓库Agent、生产环境中的Agent系统、任何涉及不可逆操作的Agent

## 原文

（见来源链接——微信公众平台，腾讯程序员，DECO实践系列）

## 相关笔记
- [[ai-Agent架构设计模式]] — Hook链与设计模式中的职责链模式相似
- [[2026-07-17_Google开源78个AgentSkills_不到一天1.4万star]] — Skill的上下文工程
- [[2026-06-08_Anthropic公开内部Skill方法论]] — Context Engineering理念
