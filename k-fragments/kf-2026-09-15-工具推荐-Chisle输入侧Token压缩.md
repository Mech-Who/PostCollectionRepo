---
title: K-Fragment：Chisle 输入侧 Token 压缩
category: 工具推荐
layer: layer2:通用
tags: [K-Fragment, Chisle, Token优化, 上下文工程]
source_url: https://mp.weixin.qq.com/s/B62ZCCyevRMaOoppT5CElQ
---

## A · Applicable
AI 编码会话被超长日志、搜索结果和重复工具输出挤占时，用于设计可恢复的输入压缩。

## B · Boundary
不要压缩会被后续精确编辑依赖的内容；不可重放结果必须先保存原件；节省不足时不应介入。

## C · Core
- 优先治理输入侧工具输出，而非只限制最终回复。
- 用白名单决定可压缩工具，默认拒绝未知结构。
- 保留头尾、错误行和完整原件路径。
- 压缩后必须还原原工具返回结构。
- 同时评估平均收益、最坏膨胀和正确性。

## D · Data
`npx chisle --list` 可只读探测；`npx chisle --dry-run` 可预览修改；升级使用 `npx chisle@latest --update`。
