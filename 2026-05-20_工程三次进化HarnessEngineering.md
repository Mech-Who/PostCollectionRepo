---
title: 从Prompt、Context到Harness，工程的三次进化与终局之战
date: 2026-05-20
category: AI应用
depth: 深度
tags: [Prompt Engineering, Context Engineering, Harness Engineering, AI编程, Agent, 工程方法论, RAG, OpenAI, Anthropic]
summary: AI工程方法论从Prompt Engineering（说清楚）到Context Engineering（给够信息）再到Harness Engineering（系统可靠）的三次进化，三者层层嵌套而非替代，最终指向「人类掌舵，Agent执行」的新范式。
source_url: https://mp.weixin.qq.com/s/b1VL28GX5d17sKPfkSbIsw
source: weixin
status: 📥已采集
sync_status: ❌未同步
---

> **摘要：** AI工程方法论经历了从Prompt Engineering（说清楚）到Context Engineering（给够信息）再到Harness Engineering（系统可靠）的三次进化，三者层层嵌套而非替代。最终指向「Human Steer, Agents Execute」的新范式——工程师从"写代码的人"进化为"设计让AI把代码写好的系统的人"。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章的信息密度极高，几乎是2026年AI工程领域最重要的总结之一。以下几个点最值得关注：

**Harness Engineering 的定义非常精准**——在大模型能力之外的一切都属于Harness：工具、验证机制、约束规则、多Agent协作框架。这解释了为什么同样的模型，在不同的Harness设计下产出天差地别。

**"衰变定律"是最反直觉也最有价值的洞察**：模型能力越强，所需的Harness越简单。这意味着不要过度设计那些模型未来能自我解决的问题。Harness Engineering 可能是一项过渡性技术，但在模型能力尚未完美的今天，它是让AI系统在生产环境可靠运行的必要条件。

**F-Harness（Planner + Generator + Evaluator）的代价**值得铭记：20倍的时间 + 22倍的成本，换来从"勉强可用"到"生产环境级别"的质变。这对实践中的系统设计有直接的指导意义——什么时候需要多Agent，什么时候单Agent就够了。

**对知识管理/写作工作的启发**：我现在做的推文知识管理，本质上也是在构建一套Harness——通过文件通信协议、.done信号文件、三级加工模板等规则，让内容处理更可靠。这篇文章的理论框架可以反向审视自己的工作流设计。

## 📌 关键要点
- **三次进化路线**：Prompt Engineering（说清楚）→ Context Engineering（给够信息）→ Harness Engineering（系统可靠），层层嵌套不替代
- **Harness 公式**：AI Agent系统 = 大模型 + 工具栈 + 验证闭环 + 约束规则 + 多Agent协作框架
- **Harness 衰变定律**：模型能力越强，所需Harness越简单。不要过度设计模型未来能自我解决的问题，把精力放在行业特定规则和外部接口上
- **F-Harness 分工**：Planner（规划拆解）+ Generator（逐项执行）+ Evaluator（独立审核），代价约20倍时间/22倍成本，但质量从"勉强可用"跃升至"生产环境级别"
- **工程师新范式**："Human Steer, Agents Execute"——衡量标准从"个人产出"转向"系统杠杆"（能设计多健壮的Agent系统）
- **上下文治理**：把巨量agent.md压缩至百行索引，动态加载子文档；强制单一事实来源（所有决策归档到代码仓库）

## 原文

### 引言

OpenAI内部的一支3到7人小团队，在短短五个月内，让AI生成了将近100万行生产级别的代码。全程没有一个工程师亲手写过一行业务逻辑代码。

这个问题的答案，藏在三个词里：Prompt Engineering、Context Engineering、Harness Engineering。

### 01 | Prompt Engineering：和AI说话是一门学问

大语言模型（LLM）是一个极其擅长续写的系统。你给它一段输入，它预测接下来最有可能出现的内容。

Prompt Engineering的武器库：
- 零样本提示（Zero-shot Prompting）
- 少样本提示（Few-shot Prompting）
- 思维链（Chain-of-Thought, CoT）
- 角色扮演（Role Prompting）
- 提示链（Prompt Chaining）

2023-2024年，"Prompt Engineer"曾被视为最有前途的职业。但随着模型进化，写好Prompt的边际效益显著降低。更深层的问题是：模型听懂了你说的话，但它可能不知道关键信息——上下文。

### 02 | Context Engineering 的崛起

LLM的本质是金鱼助理——每次对话，它能看到的信息被严格限制在上下文窗口内。

**RAG（检索增强生成）**：不存知识，存索引。需要什么临时去检索，精准注入。

**上下文压缩**：对抗"中间遗忘"（Lost in the Middle）现象。解决方案包括滚动摘要、重要性评分、层次记忆。

**单一事实来源**：强制将所有决策、规范、文档归档进代码仓库，确保AI的信息来源是唯一的、可追溯的、版本受控的。

### 03 | 两者的局限

即使Prompt写得好、Context给得足，Agent仍可能：做多余的事、声称测试通过但没跑过、命名风格不一致、生成重复代码。

根源在于系统层面缺乏约束、验证和反馈机制。

### 04 | Harness Engineering——驾驭AI的系统艺术

Harness = 马具。一个完整的AI Agent系统，除了大模型本身之外的所有东西都属于Harness。

**OpenAI的百万行代码实验三大策略**：
1. **上下文治理**：将巨量agent.md压缩至百行索引 + 动态加载子文档；强制单一信息来源
2. **验证闭环**：Chrome DevTools截图验证、可观测性工具查日志、强制Lint + 自动化测试
3. **技术债清理**：后台Codex任务定期扫描代码库，自动修复偏离规范的代码和过时文档

**Anthropic的F-Harness**——Planner（规划者）+ Generator（生成者）+ Evaluator（评估者）：

| 维度 | 单Agent模式 | F-Harness三Agent模式 |
|------|------------|---------------------|
| 耗时 | ~20分钟 | ~6小时 |
| 成本 | ~$9 | ~$200 |
| 输出质量 | 逻辑残缺 | 生产环境级别 |

### 05 | 三者的嵌套关系

- Prompt Engineering回答："我该跟模型说什么？"
- Context Engineering回答："模型在回答时该知道什么？"
- Harness Engineering回答："整个AI系统该如何可靠地运转？"

三者缺一不可。没有好的Prompt，Context注入的信息无法被模型正确理解。没有好的Context，Agent在信息真空中瞎跑。没有好的Harness，再好的Prompt和Context只是沙滩上的城堡。

### 06 | Harness 的衰变定律

模型能力越强，所需的Harness越简单。今天需要精心设计的许多Harness规则，未来会被模型能力自然吸收。

实践建议：把精力集中在两类场景——① 模型短期内无法自我解决的业务逻辑边界（行业特定规则、合规要求）② 即使模型能力再强也无法自行建立的外部环境接口（工具调用、API集成、权限控制）。

### 07 | 新范式：Human Steer, Agents Execute

工程师的核心职责演变为三件事：
1. **定方向（Steering）**：清楚地知道要建什么、为什么建
2. **搭架子（Harnessing）**：为Agent构建可靠的运行支架
3. **做判别（Decision Making）**：在关键决策节点介入

衡量标准从"每天能写多少行代码"转向"Harness能支撑多高的代码产出率"。

### 08 | 实践路线图

第一步：打牢Prompt基础（思维链、角色设定、结构化输出）
第二步：系统学习Context Engineering（RAG系统、上下文窗口管理、记忆系统设计）
第三步：从系统视角思考Agent设计（约束、验证机制、多Agent协作）
第四步：培养"动态Harness思维"（随时判断哪些约束是必需的，哪些可以被模型能力替代）

软件工程没有消失，它在进化。从"写代码的人"，进化为"设计让AI把代码写好的系统的人"。

> 来源：腾讯云开发者（原创作者：李伟山）
