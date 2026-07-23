---
title: 拒绝玩具大模型：从通用多模态RAG到垂直行业RAG的研究思路
date: 2026-07-17
category: AI技术
depth: 深度
layer: layer2
tags: [RAG, 多模态, EagleRAG, 微内核架构, 插件化, PixelRAG, 生物医药, Agentic BI, 行业RAG]
summary: 开源多模态RAG项目EagleRAG通过"微内核+插件化"架构重构，以像素原生感知技术(PixelRAG)解决传统RAG的多模态信息丢失问题，并在生物医药研发（智能路由化学解析）和企业Agentic BI（语义层+动态看板）两大行业场景中落地验证，展示了从"行业无关工具"到"深耕行业底座"的演进路径。
source_url: https://www.xiaoheihe.cn/app/bbs/link/434c722236ec
source: xiaoheihe
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 开源多模态RAG项目EagleRAG直面传统RAG的四大痛点（多模态信息丢失、算力成本灾难、缺乏行业语境、只读不写），提出"微内核架构+插件化"的重构方案。核心底座EagleRAG Core只负责文档流转和对话编排，行业专属逻辑（生物医药插件BioMed-Plugin、企业BI插件Data-BI-Plugin）通过Hook机制注入。文章详细展示了在生物医药场景中如何通过智能VLM路由（化学图→RDKit，纯文本→OCR）降低80%成本，以及如何将RAG升级为"会读图、懂业务、能写SQL并自动画图的超级数据分析师"。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章最有价值的是**"从通用到垂直"的架构演进思路**——EagleRAG 的"微内核+插件化"是RAG架构的进化方向。

与当前AI Agent领域的Skill架构（Google Skills仓库、Anthropic Skill方法论）形成了有趣的对照：

| 维度 | EagleRAG插件化 | Agent Skill架构 |
|------|---------------|----------------|
| 内核 | Core只做调度编排 | SKILL.md只做路由导航 |
| 扩展 | Hook点注入行业逻辑 | references/scripts按需加载 |
| 目标 | 让RAG适配行业 | 让Agent拥有专业能力 |

两者本质是同一个思想在不同层的体现：**把通用能力和领域能力解耦**。

两个具体技术点值得关注：

1. **VLM智能路由**（预解析拦截器）：不是所有页面都需要昂贵的VLM，通过轻量分类器判断页面类型，化学分子式→RDKit/DECIMER，纯文本→OCR，只有复杂图表才走VLM。成本降80%，精度反升。这是实践中的"性价比思维"。

2. **语义层（Semantic Layer）桥接**：Agentic BI场景中，EagleRAG的角色不是直接查数据库，而是解析DDL、dbt脚本和指标字典，把"业务口径"作为Context喂给SQL Agent。这恰好是RAG与Agent结合的正确姿势——RAG处理非结构化知识，Agent处理结构化操作。

## 📌 关键要点
- **核心方法**：微内核架构 + 插件化Hook扩展（EagleRAG Core + Plugins）
- **踩坑经验**：
  - 通用多模态RAG直接落地行业会面临算力成本灾难
  - "全量过VLM"不可行，需要预解析判断页面类型再选择解析策略
  - 传统RAG的"只读"局限，需要与Agent结合实现"读写闭环"
- **适用场景**：医药研发文档处理、企业BI/Text-to-SQL、专利分析、任何含复杂图表/结构式的文档场景

## 原文

（见来源链接——小黑盒平台，EagleRAG项目分享）

## 相关笔记
- [[ai-Agent架构设计模式]] — Agent的Controller→Planner映射与EagleRAG的微内核设计理念相通
- [[2026-07-17_Google开源78个AgentSkills_不到一天1.4万star]] — Skill的按需加载vs RAG插件化
- [[tool-工具推荐与开源]] — EagleRAG作为开源项目的使用评估
