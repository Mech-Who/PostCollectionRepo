---
title: Dynamic Workflows全解
date: 2026-06-11
category: AI技术
depth: 标准
layer: layer2:通用
tags: [Claude Code, Agent Workflow, Dynamic Workflows, 子Agent调度, LLM架构]
summary: Claude Code 团队提出的 Dynamic Workflows 新范式——Agent 能根据当前任务现场编写专属 harness，用 JavaScript workflow 调度子Agent，适用于大规模重构、深度研究、事实核查等复杂场景。
source_url: https://mp.weixin.qq.com/s/3SEpb0bXL74F2h8WP4JA4g
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** Claude Code 的一种新用法：Agent 可以根据当前任务当场写出一套专属 harness，用来拆分、调度和验证整个工作过程。通过 JavaScript workflow 调度子Agent，把复杂任务拆成并行、验证、循环、筛选、锦标赛等结构。适合单个上下文窗口容易跑偏的任务：大规模重构、深度研究、事实核查、简历排序、事故根因分析、规则提炼、批量 triage 等。

## 我的理解

> 由小林生成，供小涵审阅修改

Dynamic Workflows 的核心思路是"让 Agent 自己设计自己的工作流"，而不是依赖预定义的固定管道。这是一种元编程能力的体现——Agent 不再是工具链中的执行者，而是工作流的构建者。传统 AI Agent 面临的最大瓶颈是上下文窗口有限，Dynamic Workflows 通过动态拆分任务、并行执行、结果验证等机制，突破了单次推理能力的上限。这和我们 PostCollection 知识管线中"团队模式"的思路有异曲同工之妙：用结构化的子任务分发解决主 Agent 的 token 瓶颈。

## 原文

（原文由10张图文信息图组成，文字量较少，核心内容已在摘要和标签中覆盖）

## 相关笔记

- [[2026-06-10_Claude-Code-Agentic-Engineering]] — Claude Code 相关的 Agentic 工程实践
- [[2026-05-28_Cursor-Deep-Tab-新功能]] — Cursor 的 Agent 能力进化
