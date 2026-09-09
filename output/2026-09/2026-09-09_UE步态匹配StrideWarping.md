---
title: 如何在 UE 引擎中实现“步态匹配”？
date: 2026-09-09
category: 游戏开发
depth: 深度
layer: layer2:通用
tags: [Unreal Engine, 步态匹配, Stride Warping, 角色动画, IK, 根运动]
summary: 步态匹配的核心是把角色移动速度拆成步幅和步频两个可独立控制的维度，避免只在 Idle、Walk、Run 动画间混合造成滑步。ALS 通过混合空间、步幅曲线和播放速率协同控制，UE5/Lyra 则可用 Stride Warping 按胶囊体速度与动画根运动速度之比缩放脚部位置，并配合骨盆和大腿补偿保持接地与腿长约束。
source_url: https://mp.weixin.qq.com/s/NnorOetG0jmf5LCS0An0aQ
source: weixin
status: 📥已采集
sync_status: ❌未同步
---

> **摘要：** 步态匹配的核心是把角色移动速度拆成步幅和步频两个可独立控制的维度，避免只在 Idle、Walk、Run 动画间混合造成滑步。ALS 通过混合空间、步幅曲线和播放速率协同控制，UE5/Lyra 则可用 Stride Warping 按胶囊体速度与动画根运动速度之比缩放脚部位置，并配合骨盆和大腿补偿保持接地与腿长约束。

## 我的理解
> 由小林生成，供小涵审阅修改

“速度驱动动画”并不等于“把速度接进混合空间”。混合空间只能决定不同动画样本的权重，无法保证混合结果的脚掌位移正好等于角色在世界中的位移。滑步的根因，是动画根运动速度、角色移动组件速度、步幅和播放速率之间没有建立可校准的约束。

步态匹配应分两层处理。上层先决定当前是走、跑还是两者过渡，并用播放速率控制步频；下层再根据目标移动速度与动画自身速度的比值调整步幅。UE5 的 Stride Warping 将后一层变成骨骼空间求解：以大腿和脚的几何关系计算缩放枢轴，移动 IK 脚骨，再调整骨盆和大腿，避免脚离地、腿过伸或身体重心突变。

这套方案并不是免费替代动画资产。缩放幅度过大时，膝盖弯曲、脚掌朝向和上半身节奏仍会失真；根运动缺失、速度采样不稳定或地面法线错误也会让图表模式退化。因此更可靠的做法是先准备覆盖主要速度区间的动画样本，再让 Warping 负责样本之间的小范围适配。

## 关键要点

- **问题定义**：角色速度由步频和步幅共同决定，只混合 Idle、Walk、Run 不能保证脚掌速度与胶囊体速度一致。
- **ALS 方案**：用 `WalkRunBlend` 选择走跑区间，用速度曲线控制 `Stride Blend`，用当前速度除以该步态最高速度得到播放速率。
- **Lyra/UE5 方案**：Stride Warping 可用一条带根运动的动画，通过 `LocomotionSpeed / RootMotionSpeed` 得到 `ActualStrideScale`。
- **脚部求解**：以脚部位置和步态方向构造缩放参考点，将脚相对参考点的向量按步幅倍率缩放。
- **身体补偿**：根据 IK 脚目标与原始 FK 腿长迭代下拉骨盆，再旋转大腿并钳制 IK 腿长，维持接地与腿形。
- **工程边界**：根运动、IK/FK 骨骼配置、重力方向、地面法线、速度阈值和插值参数必须一致；大倍率变形应回到动画资产层解决。

## 原文整理

公众号转载自知乎作者羽川翼：<https://zhuanlan.zhihu.com/p/1923458131284955885>。

### 1. 为什么普通一维混合空间会滑步

现实中的移动速度由步频和步幅共同决定。常见的 `Idle -> Walk -> Run` 一维混合空间根据速度改变动画权重，但行走和跑步资产可能拥有相近的步幅或步频。当角色移动速度位于两个样本之间时，动画虽然混合得更快，脚掌的实际位移却没有同比增加，于是角色看起来像在地面滑动。

### 2. ALS：分别控制步态、步幅和步频

ALS 将控制量拆为三个部分：

1. `WalkRunBlend` 通常由玩家输入或步态状态决定，用于在走路区间和跑步区间之间切换。
2. `Stride Blend` 根据角色速度查询曲线。速度增加时步幅增大；走路和跑步使用不同曲线或区间。
3. `Striding Play Rate` 用角色当前速度除以当前步态的标称最高速度，调节动画播放速率，从而改变步频。

ALS 的混合空间为走和跑分别保留样本，并使用静态姿势近似缺失的起步阶段。这能降低直接从 Idle 混入走跑动画时的姿势突变，但效果仍依赖动画资产及曲线标定。

### 3. UE5/Lyra：Stride Warping

UE5 提供 Stride Warping 节点，可在骨骼层调整脚步跨度。Manual 模式手动提供 `Stride Scale` 和 `Stride Direction`：`Stride Scale = 1` 表示保持原动画，方向通常设为角色正前方。Graph 模式从当前动画子图的根运动推导方向和动画速度，`LocomotionSpeed` 绑定角色移动速度。

图表模式的核心倍率为：

```cpp
ActualStrideScale = LocomotionSpeed / CachedRootMotionDeltaSpeed;
```

当动画根运动速度低于 `MinRootMotionSpeedThreshold` 时，倍率回到 `1.0`，避免除以接近零的速度。随后倍率经过 `StrideScaleModifierState.ApplyTo(...)` 做钳制与插值；图表模式还会缩放并覆盖当前根运动增量，使动画姿势和移动贡献保持一致。

### 4. `EvaluateSkeletalControl_AnyThread` 的求解链路

#### 4.1 提取根运动与方向

图表模式先通过 `IAnimRootMotionProvider` 提取根运动增量，以其平移方向作为 `ActualStrideDirection`。如果缺少根运动且启用了 `bDisableIfMissingRootMotion`，节点会提前退出。

#### 4.2 缩放 IK 脚位置

对每只脚读取 IK 脚骨和大腿骨的组件空间位置。先用重力方向、地面法线和大腿位置构造步态扭曲平面，再把脚投影到垂直于步态方向的平面上得到缩放枢轴 `ScaleOrigin`：

```cpp
const FVector ScaleOrigin = FVector::PointPlaneProject(
    IKFootLocation,
    StrideWarpingPlaneOrigin,
    ActualStrideDirection);

const FVector WarpedLocation =
    ScaleOrigin + (IKFootLocation - ScaleOrigin) * ActualStrideScale;
```

这个公式只缩放脚在步态方向上的距离：倍率大于 `1` 时迈得更远，小于 `1` 时迈得更短。

#### 4.3 调整骨盆

脚部位置变化后，原始骨盆位置可能无法同时满足各条腿的长度约束。`PelvisIKFootSolver` 保存每只 FK 脚到骨盆的原始距离，并根据已经扭曲的 IK 脚位置迭代求解新的骨盆位置。每轮计算所有脚的理想骨盆位置并取平均，当调整量小于误差阈值时提前收敛。

求解结果再经过弹簧插值和 `PelvisAdjustmentMaxDistance` 钳制，避免骨盆突然跳动或移动过远。

#### 4.4 大腿旋转补偿与腿长钳制

应用骨盆偏移后，系统计算原始大腿到 FK 脚的方向 `InitialDir`，以及调整后大腿到 IK 脚的方向 `TargetDir`，再用 `FQuat::FindBetweenNormals` 得到旋转补偿。若 IK 目标距离超过原始 FK 腿长，则沿 `TargetDir` 将脚位置限制在可达范围内，防止腿部过伸。

最后把大腿和 IK 脚的变换加入 `OutBoneTransforms`，按骨骼索引排序后输出。

### 5. 实施检查清单

1. 确认角色骨架已配置 IK 脚骨、FK 脚骨、大腿骨和骨盆骨。
2. 确认 Graph 模式使用的动画子图能提供有效根运动；否则使用 Manual 模式或明确回退策略。
3. 将角色移动速度接入 `LocomotionSpeed`，并校准动画根运动的标称速度。
4. 为 `Stride Scale` 设置合理上下限和插值，避免把资产差异全部交给骨骼变形。
5. 在起步、停步、走跑切换、转向、斜坡、撞墙和低帧率下检查脚滑、腿过伸与骨盆抖动。
6. 使用动画调试绘制脚部目标与缩放枢轴，区分输入速度、根运动、IK 配置和地面法线问题。

## 相关笔记

- [[UE5.8AnimGen机器学习角色动画Epic新示例项目]]：同属角色动画适配，但 AnimGen 更偏生成式动画，Stride Warping 是运行时几何修正。

## Skill 转化评估

已触发。文章具备明确实施步骤、UE 特定节点与源码接口，且现有 Skill 未覆盖 UE 步态扭曲；本次已生成 `ue-stride-warping` Skill 草案，并把单篇文章中未经验证的参数保留为待项目实测项。由于用户级 Skill 目录位于工作区之外，草案尚未安装，待用户明确授权后再写入。
