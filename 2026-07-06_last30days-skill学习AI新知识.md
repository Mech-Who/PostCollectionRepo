---
title: 用这个 5 万 Star 的 Skill 学习 AI 新知识，真的起飞
date: 2026-07-06
category: 工具推荐
depth: 标准
layer: layer2:通用
tags: [last30days-skill, AI学习, 社交媒体聚合, 开源工具, 信息检索, 知识获取, 工具推荐]
summary: 推荐 last30days-skill（GitHub 5 万 Star）——给 AI Agent 一个话题，它自动爬取 Reddit/X/YouTube/TikTok/HN 等平台近 30 天的真实讨论，聚合为带引用的研究简报，让 AI 基于一手信息和你问答。
source_url: https://mp.weixin.qq.com/s/XYYV68sGT8KFxh6rCJZwkw
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** last30days-skill 是一个开源 AI 工具，给一个话题就能自动聚合 Reddit/X/YouTube/TikTok/Hacker News/GitHub 等平台的近 30 天讨论，生成结构化的研究简报。核心差异在于：①深度爬取（连评论和点赞一起扒）②按真实热度排序（不按 SEO）。安装简单，4 个源免费可用，适合用来追踪国外社区对 AI 新概念的一手讨论。

## 我的理解

这篇文章推荐了一个很有意思的 Skill——**last30days-skill**。它的核心价值不是"搜索"，而是"让 AI 替你读完几十个信息源，然后跟你聊"。

两个关键差异：

1. **深度爬取 ≠ 普通搜索**：普通搜索只看标题/摘要，它把 Reddit 的评论、X 的高赞回复一起扒下来。这个差异很关键——优质信息经常埋在评论里，而且跨十几个平台一起翻的聚合视角是单平台搜索给不了的。

2. **真实热度 ≠ SEO 排名**：按 Reddit 的 upvote、TikTok 的播放量排序，而不是按谁 SEO 做得好排前面。这个在追踪 AI 新趋势时特别有用——社区真正在讨论什么 vs 谁写了一篇推广文，结果是完全不同的。

**与 WorkBuddy 的连接**：这有点像 WorkBuddy 的推文知识管理体系的一个"外部输入侧"——我们这边做的是内部知识的加工和沉淀，而 last30days-skill 是做外部一手信息的快速聚合。两者可以互补：先用它扒一圈，然后走我们的分类/K-Fragment/概念管线做深度加工。

不过也要注意它的局限——主要覆盖海外平台（Reddit/X/YouTube/TikTok/HN），对中文信息源覆盖有限。用在学习 AI 新概念（如 Loop Engineering、Agent 架构等）上挺合适，毕竟国内信息确实很多是二次咀嚼。

**安装方式**（对于 Claude Code）：
```
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

## 原文

（见原始链接：https://mp.weixin.qq.com/s/XYYV68sGT8KFxh6rCJZwkw）

## 相关笔记
- 与 PostCollection 的知识管线互补——外部聚合 + 内部深加工
- 适合用于追踪 AI 领域新概念的一手社区讨论
