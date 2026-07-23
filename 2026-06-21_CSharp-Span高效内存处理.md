---
title: C#开发小技巧之Span高效内存处理
date: 2026-06-21
category: 游戏开发
depth: 深度
layer: layer2
tags: [C#, Span, Unity, 性能优化, GC, 游戏开发, 内存管理, IL2CPP]
summary: 深度讲解C# Span\<T\>在Unity游戏开发中的三大经典应用场景（字符串解析、stackalloc临时缓冲区、数组切片）、性能对比（零GC + 2.7倍速度提升）、避坑指南以及 Unity 各版本的兼容性差异。核心命题：分配即罪恶，Span让你零拷贝操作内存。
source_url: https://mp.weixin.qq.com/s/udELu6QEWo3CSjkRQIJNUw
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 本文系统介绍了 C# Span\<T\> 在 Unity 游戏开发中的三种经典应用——字符串零GC解析、stackalloc 每帧临时缓冲区、数组切片分批处理粒子系统，提供了完整的可编译代码示例和性能对比数据（10万次解析：零GC，47ms vs 传统126ms），并总结了4个常见踩坑点。

## 我的理解

这是一篇**实战导向**的 Unity C# 性能优化教程，核心价值不在于"Span 是什么"的概念讲解，而在于**三个可直接复用的代码模式**和**经过实测的性能数据**。

几个让我印象深刻的点：

1. **"分配即罪恶"**——这个原则对游戏开发尤其重要。移动端+热路径的每帧 GC 分配是卡顿的隐形杀手，Span 作为值类型+零拷贝的设计，直接在栈上操作内存，从根源上消除了这个隐患。

2. **stackalloc + Span 的组合很惊艳**——以前我在 Unity 里处理临时缓冲区只能 new 数组，每帧都在堆上分配。`stackalloc` 让临时缓冲区的分配成本归零，方法结束后自动释放。但要注意栈空间有限（<1KB），大块数据还是要用 `ArrayPool`。

3. **作者没有回避兼容性问题**——很实在地列出了 Unity 2020.3/2021.3/2022.3 各个版本的支持情况，并指出 IL2CPP + Burst 对 Span 有深度优化。这对仍在用旧版本 Unity 的团队很有参考价值。

4. **与已有知识的连接**：这篇文章提到的 Span 零拷贝思想，和之前我们讨论的 Claude Code、Agent 架构中的"数据指针传递 vs 全文复制"设计有异曲同工之妙——都是在"避免复制"这个抽象层面上做优化。本质上是**同一类架构思想在不同领域的体现**。

## 📌 关键要点

- **核心方法**：Span 是一个栈上分配的"内存视图"，记录起始位置和长度，不持有数据，实现零拷贝切片。`Span<T>` 可读写，`ReadOnlySpan<T>` 只读——API 参数优先用后者。
- **三大模式**：
  ① Span + `AsSpan()` 替代 `Substring()` → 字符串零GC解析
  ② `stackalloc` + Span 替代 `new float[]` → 每帧临时缓冲区零分配
  ③ `AsSpan(i, count)` 切片替代 `Array.Copy` → 数组子范围零拷贝处理
- **性能数据**：10万次字符串解析测试，Span 方案 GC 分配 0KB/47ms，传统 Substring 方案 3.8MB/126ms（2.7x 提升）。
- **兼容性**：Unity 2020.3+ 基本支持，2021.3+ 完整支持，2022.3+ IL2CPP 深度优化。Burst 编译器对 Span 有特别优化。
- **避坑四则**：不能存类字段（用 Memory）、不能跨 await（用 Memory）、stackalloc 别超 1KB、stackalloc 需手动 Clear()。

## 原文

大家好，今天咱们来聊聊 C# 里那个被称为".NET性能终极武器"的特性——Span。如果你做Unity开发，又经常被GC卡顿折磨，那这篇文章绝对值得你花10分钟看完。

## 为什么游戏开发者需要关心Span？

先讲个真实的故事：上个月我优化一个MMO项目的战斗系统，发现每帧都在生成大量字符串做日志和网络协议解析，GC每30秒就来一次"大清理"，玩家反馈打团时经常卡顿。

用Profiler一查，好家伙，每帧光字符串Substring就分配了几十KB的内存。后来用Span重构了那部分代码，GC分配直接降到了0，帧率稳定提升了15帧。

这就是Span的魔力：它让你 **零拷贝** 地操作内存，从根源上减少GC压力。

* * *

## Span到底是什么？

简单说，Span是一个"内存视图"。它本身不持有数据，只记录"从哪里开始、有多长"。

```
int[] array = { 1, 2, 3, 4, 5 };
Span<int> span = array;  // 直接包装整个数组

// 修改span会直接修改原数组！
span[0] = 99;
Debug.Log(array[0]);  // 输出 99
```

**核心特性：**
- ✅ **零GC分配**：Span是值类型，在栈上分配
- ✅ **零拷贝切片**：切分数据不产生新数组
- ✅ **类型安全**：不像裸指针那样危险
- ❌ **作用域受限**：不能作为类字段，不能跨await

* * *

## 游戏开发中的3个经典应用场景

### 场景1：字符串解析（零GC版本）

这是最常见的场景。比如解析网络协议、CSV配置表、玩家聊天消息等。

**传统写法（有GC）：**
```
string packet = "POS:100.5,200.3,50.1";
int colonPos = packet.IndexOf(':');
int commaPos = packet.IndexOf(',');
string xStr = packet.Substring(colonPos + 1, commaPos - colonPos - 1);
float x = float.Parse(xStr);  // 产生GC
```

**Span写法（零GC）：**
```csharp
using System;
using UnityEngine;

public class SpanStringParser : MonoBehaviour
{
    void Start()
    {
        string packet = "POS:100.5,200.3,50.1";
        ParsePosition(packet);
    }

    void ParsePosition(string packet)
    {
        ReadOnlySpan<char> span = packet.AsSpan();

        int colonPos = span.IndexOf(':');
        int firstComma = span.IndexOf(',');
        int secondComma = span.LastIndexOf(',');

        // 零拷贝切片！
        var xSpan = span.Slice(colonPos + 1, firstComma - colonPos - 1);
        var ySpan = span.Slice(firstComma + 1, secondComma - firstComma - 1);
        var zSpan = span.Slice(secondComma + 1);

        float x = float.Parse(xSpan.ToString());
        float y = float.Parse(ySpan.ToString());
        float z = float.Parse(zSpan.ToString());

        Debug.Log($"Position: {x}, {y}, {z}");
    }
}
```

### 场景2：每帧临时缓冲区（stackalloc + Span）

比如做音频采样、顶点数据处理、物理碰撞检测时，经常需要一小块临时缓冲区。

**传统写法（每帧分配）：**
```
void Update()
{
    float[] tempBuffer = new float[256];  // 每帧new一个数组！GC哭了
    ProcessAudio(tempBuffer);
}
```

**Span写法（零GC）：**
```csharp
using System;
using UnityEngine;

public class SpanStackAlloc : MonoBehaviour
{
    const int BUFFER_SIZE = 256;

    void Update()
    {
        // 栈上分配，方法结束自动释放，完全零GC！
        Span<float> tempBuffer = stackalloc float[BUFFER_SIZE];

        // ⚠️ 重要：stackalloc的内存不会自动初始化！
        tempBuffer.Clear();  // 手动清零

        FillAudioData(tempBuffer);
        ProcessAudio(tempBuffer);
    }

    void FillAudioData(Span<float> buffer)
    {
        for (int i = 0; i < buffer.Length; i++)
        {
            buffer[i] = Mathf.Sin(Time.time * 440 + i * 0.1f);
        }
    }

    void ProcessAudio(Span<float> buffer)
    {
        float volume = 0;
        foreach (float sample in buffer)
        {
            volume += Mathf.Abs(sample);
        }
        volume /= buffer.Length;

        if (Time.frameCount % 60 == 0)
        {
            Debug.Log($"Average volume: {volume:F3}");
        }
    }
}
```

**⚠️ 注意事项：**
- stackalloc适合小块内存（建议<1KB），太大可能栈溢出
- stackalloc的内存不会自动初始化，记得调用Clear()
- 栈内存生命周期与方法相同，不能传出去长期持有

### 场景3：数组切片处理粒子系统

假设你有一个大的粒子数组，只想更新其中某一部分：

**传统写法（拷贝整个子数组）：**
```
void UpdateParticleBatch(Particle[] allParticles, int start, int count)
{
    Particle[] batch = new Particle[count];
    Array.Copy(allParticles, start, batch, 0, count);
    foreach (var p in batch) { p.position += p.velocity * Time.deltaTime; }
}
```

**Span写法（零拷贝）：**
```csharp
using System;
using UnityEngine;

public struct Particle
{
    public Vector3 position;
    public Vector3 velocity;
    public float lifetime;
}

public class SpanParticles : MonoBehaviour
{
    Particle[] allParticles = new Particle[10000];

    void Start()
    {
        for (int i = 0; i < allParticles.Length; i++)
            allParticles[i].velocity = Random.insideUnitSphere * 5;
    }

    void Update()
    {
        for (int i = 0; i < allParticles.Length; i += 2000)
        {
            int count = Mathf.Min(2000, allParticles.Length - i);
            Span<Particle> batch = allParticles.AsSpan(i, count);
            UpdateParticleBatch(batch);
        }
    }

    void UpdateParticleBatch(Span<Particle> particles)
    {
        float dt = Time.deltaTime;
        for (int i = 0; i < particles.Length; i++)
        {
            particles[i].position += particles[i].velocity * dt;
            particles[i].lifetime -= dt;
            if (particles[i].lifetime <= 0)
            {
                particles[i].position = Vector3.zero;
                particles[i].velocity = Random.insideUnitSphere * 5;
                particles[i].lifetime = 5f;
            }
        }
    }
}
```

## ReadOnlySpan vs Span：什么时候用哪个？

| 类型 | 适用场景 | 典型用法 |
|:----|:--------|:--------|
| `Span<T>` | 需要修改数据 | 缓冲区写入、原地修改 |
| `ReadOnlySpan<T>` | 只需要读取 | 字符串解析、配置读取 |

**最佳实践：** 方法参数能用ReadOnlySpan就用ReadOnlySpan，既表达了"不修改"的语义，又能接收更多类型的输入。

## Span vs Memory：别搞混了

| 特性 | Span | Memory |
|:----|:----|:-------|
| 跨await | ❌ 不行 | ✅ 可以 |
| 作为类字段 | ❌ 不行 | ✅ 可以 |
| 性能 | 更高 | 稍低 |
| 适用场景 | 同步短生命周期 | 异步/长期持有 |

## Unity中的兼容性说明

| Unity版本 | 支持情况 |
|:---------|:--------|
| 2020.3+ | 基本支持，但Mono对Span优化有限 |
| 2021.3+ | 完整支持，推荐使用 |
| 2022.3+ | IL2CPP深度优化，性能接近原生 |

## 性能对比

10万次字符串解析测试（Unity 2022.3 + IL2CPP）：
| 方法 | GC分配 | 耗时 |
|:----|:------|:----|
| string.Substring + Parse | 3.8MB | 126ms |
| Span.Slice + Parse | 0KB | 47ms |

**性能提升：2.7倍，且零GC！**

## 避坑指南

1. ❌ 把Span存到类字段 → 编译错误，用Memory
2. ❌ 在async方法里跨await使用Span → 编译错误，用Memory
3. ❌ stackalloc太大的内存（>1KB）→ 可能栈溢出
4. ❌ 忘记初始化stackalloc的内存 → 调用Clear()

## 相关笔记
- （无直接关联，但可与 Unity IL2CPP 性能优化、多Agent文件通信架构中的"零拷贝设计"思想类比）
