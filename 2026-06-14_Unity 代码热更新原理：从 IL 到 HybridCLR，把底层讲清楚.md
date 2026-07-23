---
title: Unity 代码热更新原理：从 IL 到 HybridCLR，把底层讲清楚
date: 2026-06-14
category: 游戏开发
depth: 深度
layer: layer1
tags: [游戏开发, Unity, 热更新, IL, HybridCLR, IL2CPP, AOT]
summary: 从C#编译原理讲起，系统性讲解Unity代码热更新的底层机制：IL中间语言→三种执行方式（JIT/AOT/解释执行）→iOS W^X策略为何禁止JIT→Mono与IL2CPP的本质区别→三种热更方案（Lua系/ILRuntime/HybridCLR）的原理与优劣对比。
source_url: https://mp.weixin.qq.com/s/8iDIfpsipqLKYzt1HuEuPQ
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 从C#编译原理到IL中间语言再到Unity热更新，系统性讲解：JIT/AOT/解释执行三者的区别、iOS W^X策略、Mono vs IL2CPP、三种热更方案（xLua/ILRuntime/HybridCLR）的底层原理对比。

## 我的理解

这篇文章把热更新讲得非常底层和清晰，特别是"HybridCLR是AOT+解释执行，不是AOT+JIT"这个关键区分——很多人混淆了JIT和解释执行。JIT生成机器码（iOS W^X策略禁止），解释执行逐条模拟不生成新代码（完全合规）。对于小涵（Unity/C#开发者）来说，这篇文章补上了热更新体系的理论基础，和前面两篇Addressables文章（资源热更新）形成完整的技术栈。

## 📌 关键要点

- **IL（中间语言）**：C#→IL（平台无关），Unity脚本编译为Assembly-CSharp.dll（主工程，不热更）
- **三种执行方式**：JIT（用到时编译，支持热更）+ AOT（提前编译好，不支持热更）+ 解释执行（逐条模拟，支持热更但性能差）
- **iOS W^X策略**：内存页不能同时"可写"和"可执行"，JIT流程在第三步（标记为可执行）被拒绝
- **Mono vs IL2CPP**：Mono用JIT（iOS不允许），IL2CPP将IL→C++→机器码（AOT），借Clang优化
- **三种热更方案**：
  - xLua/ToLua：换语言（Lua解释执行），方案成熟但维护两套语言
  - ILRuntime：C#实现IL解释器，热更代码还是C#，但性能差、特性支持不全
  - HybridCLR：扩展IL2CPP运行时，AOT+解释执行并行，iOS合规，开发者完全无感知
- **HybridCLR本质**：IL2CPP原本只有一条路（IL→C++→机器码），HybridCLR加了第二条路（IL→解释执行），两者共存

## 原文

文章内容见 WebFetch 抓取结果。包含完整的IL原理、三种执行方式对比表、iOS W^X策略底层机制、Mono vs IL2CPP架构图描述、HybridCLR原理解析。
