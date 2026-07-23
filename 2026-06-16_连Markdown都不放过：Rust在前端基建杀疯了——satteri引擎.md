---
title: 连Markdown都不放过：Rust在前端基建杀疯了——satteri引擎
date: 2026-06-16
category: 工具推荐
depth: 标准
layer: layer2
tags: ["Rust", "前端基建", "Markdown", "MDX", "Vite", "Astro"]
summary: 介绍satteri——一个基于Rust的Markdown引擎，底层依赖Oxc编译器，支持CommonMark+GFM+MDX，可作为Vite插件使用，已被Astro生态渐进式集成。特点是解析速度快但JS插件层保持兼容。
source_url: https://mp.weixin.qq.com/s/P56zQxaGl5SWslJRnUSvgQ
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 介绍satteri——一个基于Rust的Markdown引擎，底层依赖Oxc编译器，支持CommonMark+GFM+MDX，可作为Vite插件使用，已被Astro生态渐进式集成。特点是解析速度快但JS插件层保持兼容。

## 我的理解
> 由小林生成，供小涵审阅修改

Rust『锈化』前端基建的趋势越来越明显：Vite→Rolldown、React编译器用Rust、Deno用Rust、现在连Markdown引擎也Rust了。satteri的巧妙之处在于解析器用Rust但插件层仍然用JS——既提速了核心又保持了生态兼容。

## 原文

satteri是一个基于Rust的Markdown/MDX引擎，底层依赖Oxc编译器和Lightning CSS。特点：解析器和AST用Rust编写(速度极快)，插件层仍然用JS编写(生态兼容)。可作为Vite插件、支持CommonMark+GFM+数学公式、已被Astro生态集成。当前局限：不支持remark/rehype插件。
