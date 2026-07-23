---
title: 别再问我什么是爱马仕！——Hermes Agent橙皮书2.0
date: 2026-06-09
category: AI应用
depth: 深度
layer: layer2
tags: [Hermes, AI Agent, 开源框架, 自我进化, Agent框架对比, Nous Research, OpenClaw]
summary: Hermes 是 Nous Research 开源的自进化 AI Agent 框架（GitHub 18万+ Star），2026年2月上线两个月内从2.7万飙升至18万星。核心理念是"不用你调教，它会自己长"——自动提炼经验（小抄）、自我修正、内部管家整理、目标自动续命。对比 OpenClaw 的关键分野：Hermes 把 Harness 五件套（指令/约束/反馈/记忆/编排）焊进了出厂设置且缰绳会自己长。
source_url: https://mp.weixin.qq.com/s/vQmx59bhienmbcK7UalPXA
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** Hermes 是 Nous Research 开源的自进化 AI Agent 框架，OpenRouter CLI Agent 排行第一（4.91T tokens，是第二名 OpenClaw 的近4倍）。核心理念是"Agent 会自己长"——自动提炼经验为小抄、自我修正、内部管家整理合并、目标自动续命，用得越久越顺手。与 OpenClaw 的关键分野：一个像招了会自学的同事（Hermes），一个像养宠物手把手教（OpenClaw）。

## 我的理解
> 由小林生成，供小涵审阅修改

花叔这篇文章的核心洞见不在技术细节，而在一个产品哲学的拐点判断：**Agent 框架正在从"你教它"转向"它自学"**。OpenClaw 代表的上一代范式要求用户写 SOUL.md、手动调教——本质是 Harness Engineering（搭缰绳）。Hermes 把缰绳焊进了出厂设置，且缰绳会自己长。这个转变的意义类似从命令行到 GUI：使用门槛骤降，但用户对 Agent 的控制粒度也变粗了。18万 Star 的增速说明市场用脚投票——大多数人不想当 Agent 训练师，只想有个会干活的数字同事。

## 📌 关键要点

- **核心方法**：Hermes 的自我进化三件套——①自动提炼经验为"小抄"存储复用；②观察用户反馈自动修正小抄；③内部"管家"定期整理（合并重复/归档无用/封存不可执行），目标自动续命防止遗忘
- **踩坑经验**：Hermes 从 v0.7.0 到 v0.16.0 迭代了9个大版本才稳定；v0.7 时期是"住在云端靠 Telegram 操控的极客玩具"，现在有原生桌面 App、浏览器管理面板、简体中文、23个消息平台、多 Agent 协同看板
- **适用场景**：需要自进化能力的个人 AI 助手；不想花时间调教 Agent 的用户；多平台消息接入（23个平台）；从 OpenClaw 迁移（内建 `claw migrate` 命令）
- **关键对比**：OpenClaw 需写 soul.md 手动调教 → Hermes 自动学习；OpenClaw 像养宠物 → Hermes 像招自学同事

## 原文
（原文由花叔原创，公众号「花叔」）

**核心内容：**

OpenRouter CLI Agent 排行：Hermes 4.91T tokens（第一），OpenClaw 1.25T tokens（第二），差距近4倍。

Hermes 由 Nous Research 开源，2026年2月25日上线。4月初版橙皮书时2.7万星，目前已超18万星，两个月翻7倍，2026年增速最快的开源 Agent 框架。

**自我进化机制：** 自动提炼经验为小抄→观察反馈自动修正→内部管家定期整理→目标自动续命。这是"不用你调教"的核心——你用得越久它越顺手，因为它在调教自己。

**v0.16.0 新能力（The Surface Release）：** 原生桌面 App、浏览器管理面板、简体中文、23个消息平台接入、多 Agent 协同看板、安全模型。GitHub 简介从"self-improving"改为"The agent that grows with you"。

**橙皮书2.0：** 6部分21节，覆盖自我进化机制、记忆系统、23平台连接、多Agent协同、部署安全、边界问题（一个会自己改自己的Agent，边界在哪）。中英文PDF免费下载：github.com/alchaincyf/hermes-agent-orange-book

## 相关笔记
- [[2026-06-04_Claude Code工程化落地翻车]] — Agent 框架的工程化挑战
- [[2026-06-08_Hermes多Agent技术活管理活]] — Hermes 多 Agent 协作
- [[Harness Engineering]] — Harness 五件套理论
