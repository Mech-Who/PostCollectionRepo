---
id: kf-2026-09-08-battle-ai-rl
title: 面向玩家体验的强化学习战斗 AI
date: 2026-09-08
category: 游戏开发
layer: layer2:通用
tags: [战斗AI, PPO, CTDE, 奖励塑形, 状态编码, NPC风格]
source_url: https://mp.weixin.qq.com/s/VKGT7E8Oc9AzevxDsvgjPw
---

## A · Applicable

适用于回合制 PvE 战斗 AI、需要不同 NPC 风格的自我博弈训练，以及将策划体验目标转成奖励信号时。

## B · Boundary

只优化胜率会产生无趣或破坏沉浸感的策略；训练可见完整状态不代表线上策略可以读取隐藏信息。

## C · Core

- 按技能、单位、阵容、全局逐层编码复杂战斗状态。
- 用 CTDE 同时获得训练信息优势和线上公平的信息边界。
- 多头价值网络拆分胜负、伤害、克制、技能和资源目标。
- 显式惩罚无意义换位等 immersion bugs。
- 用遗憾值提高困难阵容采样，并以轻量 SDK 热更新部署。

## D · Data

```text
training: PPO self-play + CTDE
sampling_weight: increase with lineup regret
deployment: TensorFlow Lite + CPU SDK
latency_target: < 1 ms per inference
```
