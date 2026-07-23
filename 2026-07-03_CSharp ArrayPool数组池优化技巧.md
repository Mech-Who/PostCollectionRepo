---
title: C#开发小技巧之ArrayPool数组池优化
date: 2026-07-03
category: 游戏开发
depth: 深度
layer: layer2
tags: [C#, Unity, 性能优化, ArrayPool, GC, 数组池, 游戏开发]
summary: 详细介绍 .NET ArrayPool 在 Unity 游戏开发中的应用，涵盖基本使用（Rent/Return模式）、三个实战场景（战斗检测/网络序列化/寻路节点）、自定义池配置，以及常见误区与最佳实践。提供了性能对比数据（3倍提升，零GC分配）。
source_url: https://mp.weixin.qq.com/s/K83VC2wQaBOFqc7bjfNWcQ
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** 本文系统讲解了 .NET ArrayPool 在 Unity 游戏开发中的实践方法，覆盖 Rent/Return 基本模式、战斗范围检测/网络序列化/路径寻路三个实战场景、自定义池配置，以及小数组更应该池化、生命周期长的数组不要池化等关键误区。性能数据显示，10000次循环下 ArrayPool 比 new[] 快3倍且零GC分配。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章非常适合小涵目前的 Unity 项目（GameDev101）。原因是：

**你正在做 NPC 寻路追踪、战斗系统、逻辑帧更新等高频场景**，这些场景中大量的临时数组分配是 GC 卡顿的典型来源。

当前你的项目（LogicUpdate → NpcManager/PropManager）中，如果能嵌入 ArrayPool 模式，收益最大的点：

1. **AOE 范围检测**：`Physics.OverlapSphereNonAlloc` + ArrayPool 组合，这是 Unity 官方推荐的标准优化姿势。你战斗系统中每帧检测敌人范围时，如果能用这个组合，GC Alloc 可以降一个数量级。

2. **寻路节点缓存**：A* 寻路中 openSet/closedSet 的频繁 new 是已知的 GC 大户。用 ArrayPool 替换后，配合你正在做的 NPC 追踪逻辑，可以做到零分配寻路。

3. **网络消息序列化**：虽然你项目目前可能还没到这一步，但一旦接入多人同步，这个场景就是性能瓶颈。

文中提到的"小数组更需要池化"这个反直觉观点特别值得注意——因为小数组分配频率最高，GC 扫描成本也最高。

另外，文末提到的 `PooledArray<T>` 扩展方法封装是一个好实践：用 `using` 语句自动归还，消除忘记 Return 的风险。

## 📌 关键要点

- **核心机制**：`ArrayPool<T>.Shared.Rent(minLength)` 从池租借数组，`Return()` 归还复用。Rent 返回的数组可能比请求的长度大，必须用实际长度而非 `Length` 属性遍历。
- **try/finally 强制保证**：异常发生时如果没 Return，数组永泄露。好习惯是 Return 后置 null 防止意外使用。
- **典型场景**：战斗范围检测（AOE）、网络消息序列化、A* 寻路节点存储——高频分配+短生命周期是最大收益点。
- **性能数据**：10000次循环，new[] 分配400KB/GC 2.3ms/总耗时12.5ms → ArrayPool 分配0B/GC 0ms/总耗时3.8ms（3倍提升）。
- **常见误区**：小数组更要池化（分配频率最高 ≠ 节省少）；长时间存活的大数组不池化；Rent 时只请求实际最小长度。
- **最佳实践**：定义 PoolConstants 常量 + 封装 `PooledArray<T>` 扩展方法（using 自动归还）+ 结合 Unity ObjectPool 形成完整对象池体系。

## 原文

大家好，我是小木。今天我们来聊一个在游戏开发中极其重要，但很多人又容易忽略的性能优化话题——数组池（ArrayPool）。

如果你做过Unity开发，肯定遇到过GC（垃圾回收）导致的卡顿问题。特别是在战斗系统、粒子特效、网络通信这些高频场景，频繁的数组分配和回收简直就是性能噩梦。今天这篇文章，我会带你彻底搞懂ArrayPool，让你的游戏帧率再上一个台阶。

### 为什么需要数组池？

先看一个典型的游戏场景。假设我们正在做一个MMO的伤害计算系统，每一帧都需要：
1. 获取范围内的100个敌人
2. 创建一个数组来存储伤害结果
3. 计算完后丢弃这个数组

如果每秒60帧，每帧创建一个100元素的数组，那就是每秒6000个数组元素的分配。GC一扫描，你的帧率就掉下来了。

这就是数组池要解决的问题：**复用数组，减少GC压力**。

### ArrayPool的基本使用

.NET从Core 2.1开始就内置了ArrayPool，Unity 2021+也已经支持。使用起来其实很简单：

```csharp
using System.Buffers;

int minLength = 100;
int[] rentedArray = ArrayPool<int>.Shared.Rent(minLength);

try
{
    for (int i = 0; i < minLength; i++)
    {
        rentedArray[i] = CalculateDamage(i);
    }
    ProcessDamageResults(rentedArray, minLength);
}
finally
{
    ArrayPool<int>.Shared.Return(rentedArray);
}
```

关键点：
1. Rent返回的数组可能比你请求的大，使用时用实际需要的长度，而非Length属性
2. 一定要用try/finally保证归还
3. 归还后不要再使用数组，最好置为null

### 游戏实战场景

**场景一：战斗范围检测**
```csharp
public class AoeSkill : MonoBehaviour
{
    private const int MaxTargets = 50;
    
    private void OnSkillTriggered()
    {
        Collider[] targets = ArrayPool<Collider>.Shared.Rent(MaxTargets);
        try
        {
            int hitCount = Physics.OverlapSphereNonAlloc(
                transform.position, radius, targets, enemyLayer);
            for (int i = 0; i < hitCount; i++)
                ApplyDamage(targets[i]);
        }
        finally
        {
            ArrayPool<Collider>.Shared.Return(targets);
        }
    }
}
```

**场景二：网络消息序列化**
（代码略，详见原文）

**场景三：路径寻路节点存储**
```csharp
public class AStarPathfinder
{
    private const int MaxNodes = 1000;
    
    public List<Vector3> FindPath(Vector3 start, Vector3 end)
    {
        PathNode[] openSet = ArrayPool<PathNode>.Shared.Rent(MaxNodes);
        PathNode[] closedSet = ArrayPool<PathNode>.Shared.Rent(MaxNodes);
        try
        {
            // 寻路算法实现...
            return BuildResultPath(openSet, closedSet, nodeCount);
        }
        finally
        {
            ArrayPool<PathNode>.Shared.Return(openSet);
            ArrayPool<PathNode>.Shared.Return(closedSet);
        }
    }
}
```

### 高级用法：自定义ArrayPool

```csharp
var customPool = ArrayPool<int>.Create(
    maxArrayLength: 1024 * 1024,
    maxArraysPerBucket: 50);
```

需要自定义的场景：超大数组、专用线程池、敏感数据清理（clearArray: true）。

### 性能对比

| 方式 | 内存分配 | GC时间 | 总耗时 |
|:---|:---|:---|:---|
| new T[] | 400KB | 2.3ms | 12.5ms |
| ArrayPool | 0B | 0ms | 3.8ms |

### 最佳实践

```csharp
public static class ArrayPoolExtensions
{
    public static PooledArray<T> RentTemp<T>(this ArrayPool<T> pool, int minLength)
    {
        return new PooledArray<T>(pool, minLength);
    }
}
// 使用using自动归还
using var targets = ArrayPool<Collider>.Shared.RentTemp(50);
```

## 相关笔记
- 与「游戏开发/编程知识」下的性能优化笔记可关联
- 可与 Unity ObjectPool 配合形成完整对象池体系
