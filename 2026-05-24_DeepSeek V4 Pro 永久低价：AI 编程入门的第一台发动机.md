---
title: DeepSeek V4 Pro 永久低价：AI 编程入门的"第一台发动机"
date: 2026-05-24
tags: [DeepSeek, V4 Pro, AI编程, 定价分析, spec-driven development, 入门指南]
summary: DeepSeek V4 Pro 将限时 2.5 折活动转为永久定价，输入 $0.435/输出 $0.87 每百万 token，比 Claude Sonnet 便宜约 17 倍。虽然编程能力不及 Opus 4.7 和 GLM-5.1，但大幅降低了 AI 编程的入门门槛，让更多人能以低成本体验 AI 编程
category: AI应用
status: 📥已采集
sync_status: ✅已同步
source: weixin
source_url: https://mp.weixin.qq.com/s/4c_gqhdPCq1j5OfJ-2sDcg
depth: 标准
---

> **摘要：** DeepSeek V4 Pro 将 2.5 折活动转为永久定价（输入 $0.435/输出 $0.87 每百万 token），比 Claude Sonnet 便宜约 17 倍、比 GPT-5.5 便宜约 34 倍。支持 1M 上下文、兼容 Anthropic 格式。虽然编程能力不如顶级模型，但大幅降低了 AI 编程的入门门槛。文章还给出了 spec-driven development 的入门建议：先写清晰 spec → 拆解为小 task → 逐步实现。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章的价值不只是 DeepSeek 的定价分析，而是它点出了一个关键事实：**AI 编程最大的门槛不是技术，是钱包。**

DeepSeek 这波操作很有策略——用"2.5 折限时活动"制造紧迫感吸引用户，然后在活动到期前宣布转为永久定价，既收割了流量又赢得了口碑。对标的是那些月费几百块的海外模型，直接打价格战。

但更值得关注的是文中提到的 **spec-driven development 方法论**：设计 → 任务 → 代码。这和 Harness Engineering 的思想高度一致——在用 AI 写代码之前，先用人话把需求说清楚。模糊的需求只会得到模糊的代码，spec 有多清晰，代码就有多像样。

这对于正在用 WorkBuddy + AI 编程的小涵来说，是一个很好的印证。

## 原文

夯爆了！刚刚 DeepSeek 再次杀疯！

我刚翻 DeepSeek 的 API 文档，看完直接笑了。5/31 晚 11 点 59 一过，V4 Pro 那个 2.5 折活动就结束。

我本来以为要涨回去，点进去一看，人家直接把这个价写成永久定价，往后就按四分之一价格，并没有恢复原价。

峰哥真懂程序员，海外那几家估计开会到天亮。

对比一下：

DeepSeek V4 Pro 现在输入 $0.435 / 输出 $0.87 每百万 token。

Claude Sonnet 4.6 是 $3 / $15，Opus 4.7 是 $5 / $25

GPT-5.5 是 $5 / $30。

光看输出 token，V4 Pro 比 Sonnet 便宜约 17 倍，比 Opus 便宜约 29 倍，比 GPT-5.5 直接便宜约 34 倍。

这是个什么概念？同样的预算，你在 deepseek 这边能跑一个多月，搁海外那边一天都不一定撑得到。

更猛的是 V4 Pro 顶 1M 上下文，中等项目的仓库塞进去都不会爆。API 也兼容 Anthropic 格式，配几行环境变量就能在 Claude Code 里跑了。

肯定有人说 V4 Pro 编程能力一般般，比不上 Claude Opus 4.7 和 GLM-5.1。这一点我认，实战体感确实还差一截。

那 V4 Pro 是不是就没意义了？还真不是。

它最有价值的地方在于，让更多人能用低成本的方式体验上 AI 编程。

很多贫穷大学生只能用得起 DeepSeek，还好峰哥价格亲民，懂大学生没收入的不容易。做课设、跑小项目，这价位就放心写、放心错、反复磨。

我一直觉得，AI 编程最大的门槛就是钱包。多少人想入门，是被一个月几百块的订阅劝退，这波 DeepSeek 直接给踹开了。

给刚入门用 DeepSeek + Claude Code 的同学一个建议：别一上来就让 AI 写代码。

先用人话写一份 spec：要做什么、数据怎么存、边界在哪、什么算做完。让 AI 把 spec 再打磨一遍，补没想到的边界。然后把 spec 拆成小 task，一步步做，每写完一段你看一眼。

这套方法国外叫 spec-driven development，听着挺玄乎？

拆开看就一句话：设计 → 任务 → 代码。模糊的需求只会得到一坨模糊代码，spec 几分清楚，代码就几分像样。

等你以后真用得起 Claude Max，这能力会成倍放大。

到时候别忘了，曾经陪你度过新手时期的，是 DeepSeek。

## 相关笔记
- [[2026-05-20_Harness三层进化PromptContextHarness]] — Harness Engineering 方法论，与 spec-driven development 高度互补
