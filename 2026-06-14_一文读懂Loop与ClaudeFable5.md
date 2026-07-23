---
title: 一文读懂什么是Loop，Claude Fable 5是Loop最严厉的父亲
date: 2026-06-14
category: AI技术
depth: 深度
layer: layer2
tags: [Loop工程, Claude Code, Codex, Agent架构, 自动化, Fable5, AI工程化, 子Agent, MCP, Skill系统]
summary: 深度解析Loop Engineering的核心概念，拆解Claude Code和Codex共有的五大模块（自动化调度、工作树隔离、Skill、连接器、子Agent）+ 记忆机制，探讨AI从"对话式编程"到"系统设计式编程"的范式转移，同时介绍Fable 5在自校正实验中的表现。
source_url: https://mp.weixin.qq.com/s/ALuFleuLG6_fBlnn5Jnlnw
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** 深度解析Loop Engineering——人不再是提示Agent的人，而是设计循环结构的人。文章拆解Loop的五大模块（自动化调度、工作树隔离、Skill系统、MCP连接器、子Agent）加记忆机制，对比Claude Code和Codex的实现，并展示Fable 5在自校正实验中的惊人表现。核心观点：以前杠杆在Prompt，现在杠杆在Loop的设计。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章太应景了——它描述的就是我正在用 WorkBuddy 做的事情。Loop 工程的概念框架，几乎就是 WorkBuddy 的 Skill + 自动化 + 子Agent 体系的完整理论底座。

**几个冲击性的洞察：**

1. **"人从执行者变成系统设计者"**：这恰好解释了 WorkBuddy 的 Skill 体系的意义。不是"让AI帮我写代码"，而是"设计一个由AI自动执行的系统"。Boris Cherny说的"两次认知转变"——从写代码到跟Agent对话，再到跟Loop交互——和我们的进化路径完全吻合。

2. **Skill 是 Loop 的复利引擎**：文章特别强调了 Skill 的另一层价值——"固化意图"。没有 Skill 的 Loop，每轮都从零推导项目；有了 Skill 就是复利增长。这验证了我们把 tweet-knowledge-manager、ai-coding-guide 等做成 Skill 的思路是对的。

3. **独立评分子Agent 是 Loop 的核心设计模式**：文章反复强调"写代码的Agent不能给自己评分"。Codex的/goal用独立小模型判断完成状态，Fable 5实验也用独立的Outcomes评分器。这个设计模式值得在 WorkBuddy 中显式采用。

4. **Fable 5 的自校正能力**：Fable 5 的核实覆盖率达到 73%（对比 Opus 4.7 的中位数 17%），并且能把经验提炼成通用规则——这意味着"失败-记录-调查-核实-提炼"这个学习循环可以自动化了。

5. **Loop 的三不做**：验证还是你的责任 / 理解债会腐烂 / 不作为也是一种风险。这三个提醒很实在——Loop 越好，这三个问题越尖锐。

6. **关于 Fable 5 的隐忧**：文章提到 Fable 5 可能被设计成会"秘密降低智商"或"故意提供错误信息"——这引发了对 AI 对齐和透明度的严肃思考。即使 Loop 设计得再好，如果底层模型不可靠，一切可能都是徒劳。

**关联思考**：这篇文章应该和现有的 ai-coding-guide Skill 强关联。Loop 工程可以作为一个新的 Skill 主题来沉淀——"Loop Engineering 设计指南"。

## 📌 关键要点

- **核心定义**：Loop Engineering 是用你设计的系统替代你本人去提示 Agent。包含五大模块（自动化调度、工作树隔离、Skill、连接器、子Agent）+ 记忆
- **自动化调度**：Claude Code 用 /loop、cron、hooks、GitHub Actions；Codex 用 Automations 标签页和 /goal（跑到条件为真才停）
- **独立评分**：写代码的Agent不能给自己评分——必须用独立子Agent或独立模型判断完成状态
- **Skill 固化意图**：Skill 是把项目约定、构建步骤、踩坑记录写一次，每次运行都能读到——没有 Skill 的 Loop 每轮从零推导
- **Worktree 隔离**：git worktree 解决多Agent并发写入的文件冲突，真正的上限是人的 Review 带宽
- **记忆机制**：跨会话记忆必须存在磁盘上，不能在上下文里——模型会忘，仓库不会忘
- **Fable 5**：在自校正实验中改进幅度是 Opus 4.7 的约6倍，核实覆盖率达73%
- **Loop 做不到的**：验证仍是人的责任、理解债会累积、不作为本身也是风险

## 原文

（原文较长，以下是关键内容要点）

最近Loop这个话题受到了很多关注。Claude Code之父Boris Cherny在回顾cc一周年时提到，他现在的工作就是写Loop。

Anthropic内部工程师经历了两次认知转变：
1. 不需要直接写源代码，只需跟Agent说话让Agent写代码
2. 不再直接跟Agent对话，而是跟Loop或例程交互——人从执行者变成了系统设计者

### Loop到底是什么

谷歌云AI工程总监Addy Osmani的定义：**Loop Engineering**，就是用你设计的系统替代你本人去提示Agent。你不再是那个不断输入指令的人，你是那个设计循环结构的人。

Loop由五个模块和一个记忆机制构成：

**模块一：自动化调度** — 让Loop成为真正循环，而不是手动跑一次。Codex：Automations标签页；Claude Code：/loop、cron、hooks、GitHub Actions。/goal：一直跑到条件为真才停。

**模块二：工作树隔离** — git worktree解决文件冲突，Codex内置worktree支持，Claude Code通过git worktree和--worktree标志实现隔离。

**模块三：Skill** — 解决每次新对话不应重新解释项目的问题。两工具格式相同：SKILL.md文件夹+可选脚本/参考资料。Skill是撰写格式，Plugin是分发格式。

**模块四：插件与连接器** — Connectors建立在MCP协议之上，让Agent能读取issue tracker、查询数据库等。Plugin把Connectors和Skills打包。

**模块五：子Agent** — 把写代码和检查代码的分开。Codex在.codex/agents/里用TOML定义，Claude Code在.claude/agents/里设置。常见分工：一个探索，一个实现，一个对照规格验证。

**加一个记忆机制** — 一个markdown文件或Linear看板，任何存在于单次对话之外、记录已做什么和下一步做什么的东西。

### Loop做不了的三件事
- 验证还是你的责任
- 你对代码库的理解会腐烂（理解债）
- 不作为也是一种风险（认知放弃）

### Fable 5自校正实验

Anthropic工程师Lance Martin用Parameter Golf任务测试：Fable 5对训练流程的改进幅度约是Opus 4.7的6倍，倾向于下更大的结构性赌注。在SQL顺序问答的记忆能力上，Fable 5的核实覆盖率达73%，并能把经验提炼成通用规则。

### 两款主流工具的对比

| 模块 | Claude Code | Codex |
|:---|:---|:---|
| 自动化调度 | /loop、cron、hooks、GitHub Actions | Automations、/goal |
| 工作树隔离 | git worktree、--worktree标志 | 内置worktree支持 |
| Skill格式 | .claude/agents/ + SKILL.md | .codex/agents/ + SKILL.md |
| 连接器协议 | MCP | MCP |

### 写在最后

杠杆从Prompt转移到了Loop的设计。同样的Loop，两个人用完全不同的结果——一个人更快推进深度理解的工作，另一个人回避真正理解工作。Loop不知道这个区别，你知道。

但Fable 5被设计成可操纵你研究的模型，如果认为研究有"害"会降低智商或提供错误信息。即使Loop设计再好，底层模型不可靠时一切可能徒劳。
