---
title: K-Fragment：Pi 最小 Agent 外壳
category: AI 技术
layer: layer2:通用
tags: [K-Fragment, Pi, Agent架构, 极简设计]
source_url: https://mp.weixin.qq.com/s/g1L_EeQk3WMR4X6KanKYpA
---

## A · Applicable
设计可学习、可观察、可替换的 Agent 框架核心，或评估默认内置能力是否必要时。

## B · Boundary
极简会把能力组合、隔离和运维责任交给使用者；面向大众的完整产品不能照搬全部取舍。

## C · Core
- 保留最小 Agent 循环，把产品功能交给扩展。
- 缩小默认提示词和工具描述，释放上下文窗口。
- 公开模型输入、工具调用与分支，降低黑箱成本。
- 每项“不做”都应有工程理由和替代路径。

## D · Data
最小工具集合可从 `read`、`write`、`edit`、`bash` 开始；扩展按需提供 MCP、子 Agent 和计划能力。
