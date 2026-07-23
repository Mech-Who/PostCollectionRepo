---
title: 开源语音Agent平台 Dograh AI，2分钟拖拽上线生产级语音机器人
date: 2026-05-20
category: 工具推荐
depth: 深度
tags: [语音Agent, 开源, Dograh AI, Vapi替代, 自托管, 对话AI, 开源工具]
summary: Dograh AI是100%开源的语音Agent平台，BSD 2-Clause许可，支持拖拽式工作流构建器，一行Docker命令自托管，对标Vapi/Retell，支持BYO LLM/STT/TTS、电信集成、测试模式等生产级特性。
source_url: https://mp.weixin.qq.com/s/KE7Ts_Am1lk8o0VAuR-IlQ
source: weixin
status: 📥已采集
sync_status: ❌未同步
---

> **摘要：** Dograh AI是100%开源的语音Agent平台，BSD 2-Clause许可，支持拖拽式工作流构建器，一行Docker命令自托管，对标Vapi/Retell，支持BYO LLM/STT/TTS、电信集成、测试模式等生产级特性。

## 我的理解
> 由小林生成，供小涵审阅修改

对于正在做语音Agent相关项目的人来说，Dograh AI值得关注。核心价值在于**完全开源 + 自托管**，对比Vapi/Retell的按分钟收费和厂商锁定，差异极大。

从技术栈来看：Next.js 15 + FastAPI + Pipecat + pgvector + Redis，架构清晰可扩展。Pipecat作为底层语音管道框架，支持实时STT→LLM→TTS流式处理。

最有意思的设计是**QA Node**——内置在拖拽工作流中的节点，专门分析其他节点Prompt的质量。这个设计把"测试驱动"的理念嵌入到了工作流构建器中。

另外，Test Mode（无真实通话测试）、Headless Mode（自动化测试）等设计也体现了生产级工程的思维，不是随手写的玩具项目。

对于想自建语音客服/外呼系统的团队，这可能是目前最好的开源选项。

## 📌 关键要点
- **开源许可证**：BSD 2-Clause，100%开源可修改
- **核心定位**：自托管语音Agent平台，对标Vapi/Retell
- **安装方式**：一行Docker命令 (`docker compose up`)，或从源码安装
- **核心技术栈**：Next.js 15 + FastAPI + Pipecat（语音管道）+ pgvector + Redis + MinIO
- **核心功能**：拖拽式工作流构建器、电信集成（Twilio/Vonage等）、WebRTC实时通话、Test Mode、QA Node、Headless Mode
- **适用场景**：Inbound呼入、Outbound外呼营销、线索筛选、复杂多轮对话+人工转接
- **优势**：无厂商锁定、数据完全自主、任意LLM/STT/TTS提供商、源码完全可改

## 原文

Dograh AI 的核心定位是**开源、可自托管的生产级语音Agent平台**，支持拖拽式工作流构建器（drag-and-drop workflow builder），直接对标Vapi和Retell。

### 项目亮点
- 100%开源、无厂商锁定（BSD 2-Clause许可）
- 自托管优先：本地Docker一键启动
- 灵活集成：任意LLM/STT/TTS提供商
- 数据完全自主：所有音频、对话记录、向量数据都在你自己的基础设施上
- 维护团队：YC校友+退出创始人

### 核心功能

1. **拖拽式工作流构建器**：图形化节点编辑器，内置LLM调用、工具调用、QA分析节点、条件分支、语音响应等节点
2. **语音能力**：基于Pipecat框架的实时低延迟处理，支持多语言、OpenAI Realtime Models、实时噪声抑制
3. **电信集成**：支持Twilio、Vonage、Vobiz、Plivo、Telnyx等，支持Inbound/Outbound双模式、人工转接
4. **测试与质量**：Test Mode（无真实通话）、In-Dashboard Web Call、QA Node智能分析Prompt质量、Headless Mode自动化测试
5. **其他**：实时WebRTC支持、背景任务队列、向量数据库、Langfuse追踪集成

### 快速安装

```bash
# Docker一键安装（推荐）
curl -o docker-compose.yaml https://raw.githubusercontent.com/dograh-hq/dograh/main/docker-compose.yaml && \
  REGISTRY=ghcr.io/dograh-hq ENABLE_TELEMETRY=true docker compose up --pull always
```

启动后访问 `http://localhost:3010`。

### 技术架构

- **前端**：Next.js 15 + React 19 + TypeScript + Tailwind CSS
- **后端**：FastAPI + Pydantic + SQLAlchemy异步ORM + Alembic
- **语音核心**：Pipecat子模块——开源语音Agent框架
- **基础设施**：pgvector/PostgreSQL + Redis + MinIO + Coturn + Nginx

> 来源：如此才是（公众号）
