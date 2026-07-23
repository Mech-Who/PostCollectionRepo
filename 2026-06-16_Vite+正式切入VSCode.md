---
title: VS Code 再次倒戈！正式切到 Vite+
date: 2026-06-16
category: 工具推荐
depth: 轻量
layer: layer2
tags: [Vite+, VS Code, JavaScript工具链, VoidZero, 尤雨溪, Rolldown, Oxc]
summary: 微软正式将 Vite+（vp）加入 VS Code 的 npm.scriptRunner 枚举，与 npm/pnpm/yarn/bun 并列。Vite+不是 Vite 的升级版，而是一套完整的 JavaScript 开发工具链——统一入口、Rust 后端（Oxlint/Oxfmt/tsgo/Rolldown），目标是成为 JS 生态的"大一统"工具链。
source_url: https://mp.weixin.qq.com/s/Gz5OIMEikUq1Jw765tTYIg
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 微软合并了 Vite+ 团队的一个 PR，将 "vp"（Vite+）加入 VS Code 官方支持的工具链枚举。Vite+ 定位为「完整的 JavaScript 开发工具链」，统一 dev/check/test/build 入口，背后由 Rust 工具链（Oxc/Oxlint/Oxfmt/tsgo/Rolldown）驱动。这标志着尤雨溪和 VoidZero 正在重做整个 JS 工具链。

## 我的理解
> 由小林生成，供小涵审阅修改

简单来说，Vite+ 想做的是**JS 生态的 Cargo 或 go tool**——

以前做JS项目需要：
- `vite.config.ts`
- `tsconfig.json`
- `.eslintrc`
- `.prettierrc`
- `vitest.config.ts`
- `turbo.json`
- 等等等等……

Vite+ 想实现的是：
- `vp dev`（开发）
- `vp check`（lint+format+类型检查，一次完成）
- `vp test`（运行测试）
- `vp build`（生产构建）

对前端开发者来说，这个方向非常值得关注——如果它能成功，意味着JavaScript工具链的碎片化时代可能走向终结。

## 原文

最近，微软正式合并了一个来自 Vite+ 团队的 PR：

> Add "vp" (Vite+) to npm.scriptRunner enum

（因原文较短，完整内容请查看原始链接）

## 相关笔记
- 与技术生态/工具链演进类文章可关联
