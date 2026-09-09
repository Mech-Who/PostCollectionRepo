---
id: kf-2026-09-08-ai-app-six-layers
title: 从零设计 AI 应用的六层架构
date: 2026-09-08
category: AI 应用
layer: layer2:通用
tags: [AI架构, Harness, 上下文预算, Agent编排, 评测, 可观测性]
source_url: https://mp.weixin.qq.com/s/4Jje4HQ1nRrdx1DWV24IEg
---

## A · Applicable

适用于从零设计 AI 应用、面试系统设计、技术方案评审，以及把原型升级为可信线上服务。

## B · Boundary

不同错误代价不能复用同一自治方案；没有黄金评测集时，不应把模型或提示调整宣称为有效优化。

## C · Core

- 先按错误代价区分 Copilot 和 Autonomous 的权限与恢复责任。
- 数据按语义边界切分并携带来源、时效和业务元数据。
- 为提示、工具、检索、历史和输出显式分配上下文预算。
- 可枚举步骤优先工作流，Agent 必须限制资源并校验输入输出。
- 从线上 badcase 构建评测集，保存运行快照形成持续回归。

## D · Data

```yaml
agent_limits:
  max_steps: required
  token_budget: required
  timeout: required
  idempotency_key: task_and_step
validation:
  external_input: untrusted
  output: schema_and_business_rules
```
