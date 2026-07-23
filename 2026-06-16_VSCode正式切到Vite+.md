---
title: VS Code 再次倒戈！正式切到 Vite+
date: 2026-06-16
category: 工具推荐
depth: 轻量
layer: layer2
tags: [Vite+, JavaScript, 工具链, VS Code, VoidZero, Rolldown, Oxc]
summary: VS Code 正式将 Vite+（vp）加入 npm.scriptRunner 列表，标志着 Vite+ 进入官方工具链体系。Vite+ 不是 Vite 的升级版，而是完整的 JavaScript 开发工具链——统一入口（vp create/install/dev/check/test/build），背后基于 Rust 工具链（Oxlint/Rolldown/Oxc）。
source_url: https://mp.weixin.qq.com/s/Gz5OIMEikUq1Jw765tTYIg
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 微软合并了 Vite+ 团队的 PR，将 `vp`（Vite+）加入 VS Code 的 npm.scriptRunner 枚举。Vite+ 定位为"JavaScript 开发工具链"，统一了 dev/build/check/test 入口，底层由 Rust 工具链（Oxlint/Oxfmt/Rolldown/Oxc）驱动。这是尤雨溪 VoidZero 在重做整个 JavaScript 基础设施的重要一步。

## 我的理解
> 由小林生成，供小涵审阅修改

Vite+ 的核心理念 —— "一个命令完成整个开发流程" —— 本质上是想解决 JavaScript 生态的工具碎片化问题。Vite+ 的类比目标很清晰：就像 `go tool` 之于 Go、`cargo` 之于 Rust，一个统一的入口管理整个开发生命周期。

对于小涵来说，如果你在做前端或全栈项目（Node.js/TS），Vite+ 的出现意味着可能不需要再维护一堆分散的配置文件（vite.config.ts/tsconfig.json/.eslintrc/.prettierrc/vitest.config.ts/turbo.json）。虽然还在早期，但这个趋势值得关注。

## 原文

最近，微软正式合并了一个来自 **Vite+** 团队的 **PR**：

> **Add "vp" (Vite+) to npm.scriptRunner enum**

很多人第一眼看到可能会觉得没什么，不就是给 **VS Code** 增加了一个新的脚本执行器吗？

（因原文较短，完整内容请查看原始链接）
