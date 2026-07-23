---
title: 从AI Coding到Harness Engineering的端到端工程开发实践
date: 2026-07-03
category: AI应用
depth: 深度
layer: layer2
tags: [Harness Engineering, AI Coding, 知识库工程, 端到端开发, 多Agent编排, 状态文件, DAG并行, WorkBuddy, CodeBuddy]
summary: 应用宝活动平台团队分享了从对话式AI Coding迈向Harness Engineering的完整实践。核心包括：知识库工程（800+结构化文档、90+微服务覆盖、自动化生成+人工补充+新鲜度检测三维护）、端到端开发工程（12个专家Agent、状态文件驱动、DAG并行编排+Fork-Join模式、脚本化确定性操作），以及多平台MCP集成。核心原则是"AI负责认知，脚本负责执行"。
source_url: https://mp.weixin.qq.com/s/UE-RZH9hnbBd06CVapFGrA
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** 应用宝活动平台团队系统分享了从对话式AI Coding过渡到Harness Engineering的工程实践。文章指出对话式AI Coding在复杂项目中的四个瓶颈（上下文膨胀、缺乏业务知识、缺乏工程自动化、无法并行），并给出了完整的解决方案：基于结构化知识库工程（800+文档/90+微服务）+ 端到端开发工程（状态文件驱动/DAG编排/12个专家Agent/脚本化确定性操作）。核心金句是"AI负责认知，脚本负责执行"和"长链路必须状态化"。

## 我的理解
> 由小林生成，供小涵审阅修改

**这篇文章是腾讯内部的一手工程实践报告，对小涵（作为 WorkBuddy 的产品经理和开发者）有双重价值。**

### 作为 WorkBuddy 产品经理的视角

这篇文章本质上是在回答一个核心问题：**当 WorkBuddy 已经有了 AI 辅助编码能力，下一步的工程化方向是什么？** 文章中的很多设计思路与 WorkBuddy 的 Skill 体系、团队模式、MCP 集成高度一致：

1. **知识库工程**：LLM-knowledge 的"AI 自动生成 + 人工补充"体系，和 WorkBuddy 的 Skills 体系异曲同工。但他们的实现更加系统化——每个服务8类自动生成文档 + custom.md 手工补充 + meta.yaml 注册中心 + git hash 新鲜度检测。WorkBuddy 的 Skills 可以参考这种"自动生成+人工补充+新鲜度检测"的三维护模式。

2. **状态文件驱动**：用 `product-state.json` / `e2e-state.json` 替代对话历史作为流程的唯一真相源。这正是 WorkBuddy 主从模式中"文件通信架构"的深化——他们把它推到了极致，整个需求交付的每一步都状态化。

3. **DAG 并行 + Fork-Join**：用 worktree 隔离实现多任务并行，比 WorkBuddy 当前的团队模式更细粒度。文章还讨论了四类冲突治理策略（Merge Conflict / Shared file / Proto 协议 / DB变更），这些都是 WorkBuddy 需要关注的问题。

### 作为 Unity 开发者的视角

虽然不是直接相关的技术文章，但"确定性操作脚本化"（把编译、发布、git操作等封装为脚本让AI调用，而不是让AI自己去写shell）这个原则可以迁移到 Unity 项目的自动化构建/发布流程中。

### 关键不一致点

文章提到"严格禁用项目级 Memory 以保障状态隔离"，这和 WorkBuddy 的 Memory 体系是矛盾的。但他们的场景是**需求交付自动化**（完全确定性的工程流程），而 WorkBuddy 的 Memory 服务的是**知识管理**（需要持续上下文的场景）。这是不同抽象层的设计取舍，不能直接套用。

## 📌 关键要点

- **对话式AI Coding四大瓶颈**：1) 单窗口上下文膨胀 → 有损压缩导致遗忘；2) 缺乏完整业务知识 → 每次从零喂上下文；3) 缺乏工程自动化闭环 → 仅coding环节AI化；4) 单窗口无法并行 → 只能串行或手动多窗口。
- **知识库工程双轨制**：AI自动生成（8类文档：overview/interfaces/architecture/dependencies/storage/config/pitfalls/log） + 人工补充（custom.md/custom/ + common/公共库），通过 git hash 对比实现新鲜度检测。
- **渐进式加载取代RAG**：三层检索（全局大纲→域层meta.yaml→服务层文档），4种查询模式（需求拆解/技术方案/接口搜索/知识问答），比传统RAG更精准。
- **专家Agent体系**：12个Agent按规划/执行/验证/审查/集成5类分组，每个Agent单一职责 + 上下文隔离 + 工具最小权限 + 模型可插拔。
- **状态文件驱动**：用 `product-state.json` + `e2e-state.json` 持久化流程状态，替代对话历史，实现可中断/可恢复/可观测。
- **DAG并行+Fork-Join**：task-planner 识别任务依赖→构建DAG拓扑→worktree隔离并行开发→统一merge收口。四类冲突分治策略（文件隔离/proto前置/共享串行/全局变更一次性确认）。
- **脚本化确定性操作**：15+脚本封装确定性步骤（状态解析/worktree管理/编译发布），核心原则"AI负责认知，脚本负责执行"。
- **核心原则六条**：AI负责认知脚本负责执行 / 长链路必须状态化 / 知识库必须结构化 / Agent必须职责隔离 / 执行步骤必须脚本化 / Workflow比Prompt更重要。

## 原文

> 应用宝活动平台系统支撑应用宝内包括 app、pc、手助等产品的所有日常/节假日活动，在今年上半年，我们针对整套系统进行了一次完整的重构。正值这个时间点，Harness Engineering 的概念被提出，我们团队也在重构的过程中，针对新的活动平台系统引入 Harness Engineering 的工程实践，初步搭建了一套 AI 端到端的开发流程。

### 一、为什么要实践 Harness Engineering

在最初的开发阶段，主要采用对话式AI Coding（CodeBuddy + Plan Mode、Rules + Prompt）。随着项目复杂度提升，暴露四个问题：

1. **单窗口上下文快速膨胀**：每次启动上下文窗口，还没输入需求就已经塞了大量规则和背景知识。
2. **缺乏完整的业务知识**：每个需求涉及多个服务，需要人捋清楚后喂给AI。
3. **缺乏工程上的自动化闭环**：仅coding环节AI化，部署/验证/测试仍需人执行。
4. **单窗口无法并行**：多个独立任务只能串行或手动多窗口切换。

当任务越是完整、越是规模化、越是可抽象成稳定流程，Harness Engineering的价值越高。

### 二、整体架构：知识库工程 ✖️ 端到端开发工程

两部分组成：知识库工程（底座）+ 端到端开发工程（上层流程）。包含800+结构化文档、90+微服务知识覆盖、12个专家Agent、30+业务Skill、10+固定流程脚本。

### 三、Knowledge Engineering——让AI真正懂业务

**目录结构**：总览层→域层（meta.yaml+custom/）→服务层（8类自动文档+custom/）

**8类自动生成文档**：overview/interfaces/architecture/dependencies/storage/config/pitfalls/log

**手工沉淀文档**：custom.md（服务级业务背景/架构决策）、common/（跨域公共规范）

**渐进式加载检索**：第一层总览匹配→第二层meta.yaml grep筛选→第三层按需加载。四种模式：需求拆解/技术方案/接口搜索/知识问答。

**新鲜度检测**：比较meta.yaml中记录的git_hash与当前HEAD，差异超阈值则增量更新。增量模式保留人工批注，只更新事实信息。

### 四、端到端开发工程

**状态文件驱动**：product-state.json（多Story并行）+ e2e-state.json（单Story完整流程Phase 0-7）。每个子Agent执行后写入状态文件，主调度器直接读取状态文件确定下一步。

**专家Agent体系**（12个Agent）：
- 规划：product-analyst / requirement-analyst / task-planner
- 执行：proto-engineer / backend-developer / code-fixer
- 验证：unit-tester / interface-verifier / test-case-designer
- 审查：code-reviewer
- 集成：publisher / git-committer

**DAG并行+Fork-Join**：task-planner拆解任务→构建DAG→同层任务worktree隔离并行开发→merge收口。四类冲突分治。

**脚本化执行**：15+脚本封装确定性步骤，e2e-dev.py（状态机解析）、worktree.sh（git多分支管理）、build-and-publish.sh（编译发布）。

**多平台集成**：MCP集成TAPD/Rick/123/七彩石/伽利略/Codar等，AI在流程中可直接执行跨平台操作。

### 五、复盘与思考

**核心原则**：
1. AI负责认知，脚本负责执行
2. 长链路必须状态化
3. 知识库必须结构化
4. Agent必须职责隔离
5. 执行步骤必须脚本化
6. Workflow比Prompt更重要
7. 终局认知：未来比拼的不是"用了多少AI"，而是能否把AI当作一个工程系统来设计

**下一步方向**：自我复盘迭代能力、评估体系、工程与工具解耦、从"Agent驱动"转向"代码/脚本驱动编排"

**开放性思考**：TDD在AI时代（测试用例前置而非代码前置）、AI工程架构分层（缺方法论和实践规范）、代码还重要吗？（核心系统仍需人守住架构线，看板类容错系统适合Vibe Coding）

## 相关笔记
- 与「AI应用」分类下的 WorkBuddy 相关文章强烈关联
- 与 `ai-coding-guide` Skill 中的 Harness Engineering 准则高度相关
- 与 PostCollection 主从Agent编排器 Skill 中"文件通信架构"的设计理念一致
