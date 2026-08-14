---
title: DeepSeek Harness 发布：首创「一切皆插件」Agent 架构并全面开源（MIT）
date: 2026-08-13
category: AI技术
depth: 轻量
layer: layer1
tags: [DeepSeek, Agent框架, 插件化架构, Cordis, 开源]
summary: DeepSeek 于 8 月 13 日开放 Harness 开发者预览版（v0.1，MIT 协议开源），首创基于 Cordis 插件系统的「一切皆插件」Agent 架构——模型、工具、技能、会话、沙箱、UI 全部封装为可自由组合的插件，并提供 append-only 全链路会话日志。
source_url: https://www.xiaoheihe.cn/app/bbs/link/a8bc724af414
source: xiaoheihe
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** 2026-08-13，DeepSeek Harness 团队开放开发者预览版 v0.1 并以 MIT 协议开源。核心架构「一切皆插件」基于 Cordis 元框架：模型、工具、技能、会话、沙箱、存储、循环、调度、UI 全部为独立插件，通过服务与事件协作，无需改底层源码即可替换扩展。提供标准/PTC/极简/创造四种运行模式，append-only 会话日志支持恢复、分叉、检索与回放。

## 原文

**来源：小黑盒，2026-08-13**

2026年8月13日，北京 —— DeepSeek Harness 团队今日正式面向全球开发者开放 Harness 开发者预览版（v0.1 版本），并同步以 MIT 协议开放项目源代码。此次发布标志着 DeepSeek 在智能体（Agent）基础设施领域迈出关键一步，其首创的"一切皆插件"架构旨在为开发者提供高度灵活、可组合的 Agent 构建框架。

作为早期预览版本，v0.1 确立了核心架构方向，基础接口与核心插件将在后续版本中持续迭代。

### 核心架构：基于 Cordis 的「一切皆插件」

DeepSeek Harness 的核心设计理念为"一切皆插件"。该框架基于具备时空可组合性的 Cordis 插件系统构建。在 Cordis 元框架下，模型、工具、技能、会话、沙箱、存储、循环、调度及 UI 等所有 Agent 能力均被封装为独立插件。插件之间通过 Cordis 服务与事件进行协作，并支持在配置层自由组合。开发者无需修改底层源码，即可根据业务需求独立选择、替换或扩展任意功能模块，极大降低了二次开发与定制化门槛。

### 技术亮点：多模式运行与全链路追踪

四种运行模式：

- **标准模式**：提供完整的工具组合，适用于常规 Agent 开发
- **PTC 模式（程序化工具调用）**：支持由模型生成代码来组合多轮工具调用，提升复杂任务执行效率
- **极简模式**：仅保留 Shell 与文件编辑工具，专为最小环境下的模型基准测试设计
- **创造模式**：允许开发者在运行时检查环境、在内存中试验 Cordis 插件，并据此组合创作新的运行模式

该框架实现了"每一次运行都有迹可循"。系统采用仅追加（append-only）设计的会话日志，完整记录系统提示词、思维链、工具调用结果、子 Agent 调度及上下文注入等全量信息。开发者可通过 Trajectory 视图按来源追溯运行细节，并支持会话的恢复、分叉、检索与回放，所有操作共享同一事件流。

### 快速接入与使用

1. 快速启动：在已安装 Node.js 环境的系统中，执行命令 `npx @deepseek-ai/dsh web` 即可启动 Web UI
2. 源码安装：`git clone https://github.com/deepseek-ai/deepseek-harness` 获取完整源码

DeepSeek Harness 团队诚邀全球开发者参与 DSH 插件生态共建。
