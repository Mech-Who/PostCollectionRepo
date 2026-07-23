---
title: 谷歌开源Agent OKF标准：Karpathy力推的AI知识库通用格式来了
date: 2026-06-16
category: AI技术
depth: 标准
layer: layer2
tags: [OKF, 知识管理, AI Agent, Google, 开放标准, Karpathy]
summary: 谷歌发布Open Knowledge Format (OKF) v0.1开放规范——用Markdown文件目录为AI Agent构建可互通的知识库。核心设计：每个概念一个md文件（YAML frontmatter+正文），用Markdown链接建立关系图。三个原则：最小约束、生产者消费者独立、格式非平台。
source_url: https://mp.weixin.qq.com/s/nhF1cy_lIQukq_niVFvRCA
source: weixin
author: AI寒武纪
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 谷歌发布Open Knowledge Format (OKF) v0.1开放规范——用Markdown文件目录为AI Agent构建可互通的知识库。核心设计：每个概念一个md文件（YAML frontmatter+正文），用Markdown链接建立关系图。三个原则：最小约束、生产者消费者独立、格式非平台。

## 我的理解
> 由小林生成，供小涵审阅修改

OKF的有趣之处在于它的反平台哲学——不是又一个大一统系统，而是一个最小公约数的文件格式约定。这和Karpathy的LLM维护Markdown Wiki思路一脉相承。对我们的推文知识管理体系有启发：如果未来想把知识库开放给Agent消费，OKF格式是一个现成的参考标准。三个设计原则（最小约束、独立生产者消费者、格式非平台）本身也是好的协议设计方法论。

## 原文

谷歌发布Open Knowledge Format（OKF）开放规范，解决AI agent知识碎片化问题。

## 问题
AI agent需要的内部知识散落在元数据目录、内部Wiki、共享文档、代码注释中，互不兼容互不流通。每个团队都在重新发明数据结构，知识被锁死在创建它的平台里。

## Karpathy模式
过去一年流行起来的方式：用Markdown文件给AI agent建知识库，让agent自己读写更新。LLM不会无聊、不会忘记更新交叉引用、一次改15个文件。

## OKF设计
一个OKF bundle = 一个Markdown文件目录。每个文件代表一个概念（数据表、数据集、指标、操作手册、API等），文件路径是唯一标识。

目录结构示例：
```
sales/
├── index.md
├── datasets/orders_db.md
├── tables/orders.md, customers.md
└── metrics/weekly_active_users.md
```

每个文件：顶部YAML frontmatter（含type字段，唯一强制）+ Markdown正文。概念间用Markdown链接互引用。

## 三个设计原则
1. **最小约束**：只强制type字段，其他自由
2. **生产者和消费者独立**：人手写→AI读，元数据流水线→可视化工具浏览，LLM生成→LLM查询
3. **格式不是平台**：不绑定云服务/数据库/模型厂商/agent框架，无专有账号或SDK

## 参考实现
- 数据丰富agent：自动扫描BigQuery→起草OKF文档→LLM补充schema/引用
- 静态HTML可视化：把OKF bundle转成交互图视图
- 三个样例bundle：GA4电商、Stack Overflow、比特币公开数据集

v0.1，开源在GitHub。

## 相关笔记
- （待关联）
