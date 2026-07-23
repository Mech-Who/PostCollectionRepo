---
title: 搭建Hermes+Obsidian，我搞定了这辈子最值的本地知识库
date: 2026-06-11
category: AI 应用
depth: 深度
layer: layer2
tags: [知识库, Obsidian, Hermes, AI, 本地部署, 知识管理, 教程]
summary: 详细教程讲解如何使用Hermes Agent + Obsidian搭建本地知识库，实现自动化收藏整理、双向链接和模糊召回，并附完整安装步骤和测试效果。
source_url: https://mp.weixin.qq.com/s/qRxVPz6SHFqUYKOpIJsqrA
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 详细教程讲解如何使用Hermes Agent + Obsidian搭建本地知识库，实现自动化收藏整理、双向链接和模糊召回。

## 我的理解
> 由小林生成，供小涵审阅修改

本文的价值在于区分了RAG和"真·知识库"的本质差异：RAG是每次临时检索拼凑答案，而Hermes+Obsidian方案是AI帮你消化内容、提取实体、建立双向链接。核心亮点是0.8秒模糊召回测试效果。文章最后一句点题最好——"知识不会自动变成你的，你得去读、去关联、去想、去用"。

## 📌 关键要点
- **核心方法**：Hermes Agent利用llm-wiki Skill自动将收藏内容提取关键实体 → 创建结构化笔记 → 加双向链接 → 维护索引
- **安装步骤**：安装Obsidian（免费281MB）→ 安装Hermes（WSL环境）→ 配置API Key → 设置知识库路径和规则
- **使用规则**："写入知识库"存内容；"结合知识库"查内容；打开Obsidian看知识图谱
- **模糊召回**：0.8秒即可从文库中找到模糊记忆的内容
- **适用场景**：多平台收藏夹整合、个人知识管理、长期知识积累

## 原文

# 搭建Hermes+Obsidian，我搞定了这辈子最值的本地知识库，从安装到测试全流程讲解！你缺的不是好内容，是一个能帮你记住的AI

作者: 一口吞天

---

[完整原文内容，详见原始链接]

---
