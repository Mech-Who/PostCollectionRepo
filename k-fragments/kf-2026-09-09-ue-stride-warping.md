---
title: "UE Stride Warping 步态匹配"
date: 2026-09-09
category: "游戏开发"
depth: "深度"
layer: layer2:通用
tags: [Unreal Engine, Stride Warping, 角色动画, IK, 根运动]
source_article: "2026-09-09_UE步态匹配StrideWarping"
source_url: "https://mp.weixin.qq.com/s/NnorOetG0jmf5LCS0An0aQ"
---

# K-Fragment: UE Stride Warping 步态匹配

## A. Applicable — 适用场景

- 角色胶囊体移动速度与行走、跑步动画的脚掌位移不一致，出现可见滑步时。
- 动画样本能够覆盖主要步态，但需要在样本速度之间做小范围连续适配时。
- UE5 动画图已配置 IK/FK 脚、大腿和骨盆链，能够使用 Stride Warping 时。

## B. Boundary — 边界与注意事项

- Stride Warping 适合修正速度差，不应替代缺失的起步、急停、转向或跨度差异过大的动画资产。
- Graph 模式依赖有效根运动；根运动缺失或速度接近零时必须回退到倍率 `1.0` 或禁用节点。
- 必须钳制并平滑步幅倍率，同时检查斜坡、撞墙、转向和低帧率下的骨盆抖动、腿过伸与脚掌朝向。

## C. Core — 核心要点

1. 把移动速度拆成步态选择、步幅和步频，分别由状态、Stride Scale 和播放速率控制。
2. Graph 模式用 `LocomotionSpeed / RootMotionSpeed` 计算步幅倍率，并对倍率做阈值保护、钳制和插值。
3. 以步态方向上的投影点为枢轴，缩放 IK 脚相对枢轴的向量，而不是直接缩放整条腿。
4. 脚部扭曲后重新求解骨盆位置，再旋转大腿并用 FK 腿长钳制 IK 目标。
5. 调试时同时可视化输入速度、根运动速度、步幅倍率、脚目标和骨盆偏移，按数据链定位滑步来源。

## D. Data — 关键数据与决策记录

- 核心倍率：`ActualStrideScale = LocomotionSpeed / CachedRootMotionDeltaSpeed`。
- 根运动速度不高于 `MinRootMotionSpeedThreshold` 时，`ActualStrideScale = 1.0f`。
- 脚目标公式：`WarpedLocation = ScaleOrigin + (IKFootLocation - ScaleOrigin) * ActualStrideScale`。
- 原文未给出倍率上下限、误差阈值、骨盆最大调整距离或动画资产的实测速度范围，项目接入时需自行标定。
