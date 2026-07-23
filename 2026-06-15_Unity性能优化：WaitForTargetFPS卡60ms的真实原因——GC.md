---
title: Unity性能优化：WaitForTargetFPS卡60ms的真实原因——GC
date: 2026-06-15
category: 游戏开发
depth: 深度
layer: layer2
tags: ["Unity", "性能优化", "GC", "UWA", "小游戏", "游戏优化"]
summary: UWA技术分享：小游戏环境下WaitForTargetFPS耗时高的真实原因是GC而非空闲等待。GC耗时在小游戏报告中被归入同步等待模块，需结合Mono Used曲线定位。UCUI优化：SetActive频繁触发SyncTransform导致持续7ms开销。
source_url: https://mp.weixin.qq.com/s/9GCOxv1rEKLeNLCyShh9cQ
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** UWA技术分享：小游戏环境下WaitForTargetFPS耗时高的真实原因是GC而非空闲等待。GC耗时在小游戏报告中被归入同步等待模块，需结合Mono Used曲线定位。UCUI优化：SetActive频繁触发SyncTransform导致持续7ms开销。

## 我的理解
> 由小林生成，供小涵审阅修改

很实用的Unity优化知识。两个关键点：1)小游戏的GC排查不能用常规方法，WaitForTargetFPS高可能是GC在作祟；2)UI优化中localScale 0/1替代SetActive+动静分离是经典做法。Mono Reserved『只增不降』的特性在小游戏中更需要关注。

## 原文

两个实战案例：1)小游戏WaitForTargetFPS单帧60ms——实际不是空闲等待而是GC耗时被归入同步等待。定位方法：Mono Used每次下降拐点对应一次GC调用。小游戏Mono Reserved只增不降，需关注连续2-3局后的累积曲线。2)UGUI持续7ms——SetActive频繁触发SyncTransform。优化：localScale 0/1替代SetActive做显隐、动静分离、排查嵌套Canvas覆盖范围。
