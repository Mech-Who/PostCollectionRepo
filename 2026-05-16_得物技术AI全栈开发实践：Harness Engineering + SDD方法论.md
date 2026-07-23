---
title: "得物技术AI全栈开发实践：Harness Engineering + SDD方法论"
date: 2026-05-16
tags: ["AI编码", "Harness Engineering", "SDD", "全栈开发", "AI应用"]
summary: "得物技术团队分享了结合Harness Engineering和SDD（Specification-Driven Development）的AI全栈开发实践。通过明确的需求规格驱动AI生成代码，配合Harness体系的质量保障，实现了高效的全栈AI开发流程。"
category: "AI应用"
status: 📥已采集
---

> **摘要：** 得物技术团队分享了结合Harness Engineering和SDD（Specification-Driven Development）的AI全栈开发实践。通过明确的需求规格驱动AI生成代码，配合Harness体系的质量保障，实现了高效的全栈AI开发流程。

## 我的理解
> 由小林生成，供小涵审阅修改

SDD+Harness的组合很有意思——SDD解决的是"AI做什么"的问题，Harness解决的是"AI怎么做得好"的问题。得物作为大厂技术团队，这个实践说明AI编码已经从小规模尝试进入了工程化部署阶段。

## 原文

### SDD方法论
- 先写规格说明（Specification），再让AI生成代码
- 规格包含：输入/输出定义、边界条件、性能要求、错误处理
- 规格本身就是测试用例的基础

### 与Harness Engineering的融合
1. SDD提供精确的任务规格
2. Harness技能库提供标准化编码流程
3. Harness知识库提供项目上下文
4. 变更管理确保代码质量

### 实际效果
- 前端页面生成：从需求到上线缩短60%
- API开发效率提升3倍
- Bug率下降约40%
