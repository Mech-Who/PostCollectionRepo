---
title: Google开源78个Agent Skills，不到一天1.4万star
date: 2026-07-17
category: AI应用
depth: 标准
layer: layer2
tags: [Google, Agent Skills, 上下文工程, SKILL.md, 按需加载, 开源, gcloud, Claude Code]
summary: Google开源skills仓库（不到一天1.4万star），提供78个覆盖Google Cloud全产品线的Agent Skill，采用按需加载架构防止上下文膨胀，以Skill格式沉淀操作知识、执行顺序和安全边界，强调"不能省"的检查步骤和人工确认点。实测经验显示：Skill多了之后选择冲突成为新问题，需要通过优先级编排或MCP统一调度解决。
source_url: https://mp.weixin.qq.com/s/cYCj1MrgiQdn8rjCtq5qDg
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** Google开源了skills仓库（github.com/google/skills），提供78个覆盖GCP全产品线（AI/模型、基础设施/数据、平台/业务工具）的Agent Skill。核心设计理念：按需加载（SKILL.md只含导航，references/scripts/assets分层暴露）、聚焦"不能省"的检查步骤（如gcloud技能要求执行前必须用`gcloud help`验证具体命令、显式指定项目区域、高风险操作必须人工授权）。同时指出了Skill生态的新问题：大量Skill并存时激活冲突比想象中严重，需要通过优先级编排或MCP统一调度解决。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章与Anthropic的Skill方法论（[[2026-06-08_Anthropic公开内部Skill方法论]]）形成了完美的互补——Google从"工程实践"角度展示了Skill体系在云运维场景中的落地形态，而Anthropic更聚焦于Skill本身的设计哲学。

最值得关注的两个点：

1. **"不能省"的步骤是Skill的灵魂**：Google的gcloud skill明确要求"执行前必须用gcloud help验证到具体子命令""必须显式指定项目和区域"。这和Anthropic提出的"Gotchas（常踩的坑）"是同一个理念——Skill的真正价值不是告诉模型怎么做事，而是告诉模型"做之前必须检查什么、什么情况下必须停下来"。

2. **Skill选择冲突**：这是一个被忽视但真实的问题。78个Skill并存时，同一个任务可能激活多个相似Skill导致逻辑打架。建议的解决方式是"手工编排优先级或MCP统一调度"——这和我们当前PostCollection概念体系中的"概念体系维护"遇到的问题类似：知识越多，路由和去重成本越高。

## 原文

（见来源链接——微信公众平台，小G GitHubStore）

## 相关笔记
- [[2026-06-08_Anthropic公开内部Skill方法论]] — Skill设计哲学（互补阅读）
- [[2026-07-16_Agent治理_Hook堵住LLM偷懒越权失忆]] — Skill的上下文中"不能省"的步骤（"Prompt定意图，Skill定规矩，框架Hook定边界"）
- [[2026-06-28_Loop Engineering开源操作系统构建Agent]] — Worktree安全机制的Skill化思路
