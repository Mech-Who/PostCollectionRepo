---
title: K-Fragment：WeKnora 知识生命周期平台
category: 工具推荐
layer: layer2:通用
tags: [K-Fragment, WeKnora, RAG, Wiki, Agent]
source_url: https://mp.weixin.qq.com/s/L8ZPlnsFnGymz2jW-7KO4Q
---

## A · Applicable
团队需要统一管理知识采集、解析修订、权限、检索、Wiki 和 Agent 消费时，用于评估 WeKnora。

## B · Boundary
只需简单问答、画布编排或极致 PDF 解析时，应同时比较 MaxKB、Dify 和 RAGFlow。正式部署前需验证许可证、模型成本、权限隔离和备份恢复。

## C · Core
- RAG、ReAct Agent 与自动 Wiki 共用同一知识底座。
- 分块可编辑、重建索引并保留版本和回滚记录。
- 多数据源、多 IM 渠道和四级权限适合企业场景。
- Skill 在隔离沙箱执行，降低主服务风险。
- 模型、检索、存储、解析器和沙箱均可替换。

## D · Data
最小试点：选择熟悉文档，检查解析与分块，测试引用准确性，再逐项启用 Agent、Wiki、GraphRAG 和沙箱。
