---
title: C++并发系列·第五章：C++ 内存模型在约束什么？
date: 2026-06-28
category: 认知提升
depth: 深度
layer: layer2
tags: [C++, 内存模型, happens-before, release-acquire, 并发编程, 数据竞争, atomic, mutex, 可见性, 顺序性]
summary: C++并发系列第五章，深入讲解内存模型的底层规则：sequenced-before（线程内顺序）、synchronizes-with（release/acquire跨线程同步）、happens-before（可见性传递链）、数据竞争红线和修改顺序。通过Producer/Consumer经典案例，展示了atomic和mutex如何建立跨线程可见性保证。
source_url: https://mp.weixin.qq.com/s/moCMm_Y7ygrlZNt6mCTu6w
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** C++并发系列第五章，系统讲解C++内存模型的核心规则体系：从sequenced-before（单线程内的执行顺序保证）到synchronizes-with（release/acquire跨线程同步机制）到happens-before（可见性的传递链）。通过经典的Producer/Consumer代码案例，展示了atomic的release/acquire和mutex的lock/unlock如何建立跨线程的可见性保证。同时阐述了数据竞争（Data Race）的定义及其导致未定义行为的机制、修改顺序（Modification Order）的按对象隔离特性，以及"可见性"与"顺序性"的关键区分。

## 我的理解

> 由小林生成，供小涵审阅修改

这篇文章是C++并发编程的"地基课"，它回答了一个看似简单但至关重要的问题：**为什么一个普通变量的写入，在另一个线程看到原子标志位翻转后一定可见？**

答案被拆成了三层递进的抽象：

1. **sequenced-before**（线程内）：同一线程内前面的语句一定先于后面的语句完成——这是最基础的保证。
2. **synchronizes-with**（跨线程）：通过release/acquire配对或mutex的lock/unlock，在不同线程间拉起同步线。
3. **happens-before**（传递链）：将sequenced-before和synchronizes-with串联起来，形成"写入→可见"的传递链。

对我最有启发的几个点：

- **数据竞争的后果不止是"读到旧值"**，而是编译器会基于"程序没有数据竞争"的前提做优化推理，可能导致死循环等可怕后果（`while(!stop)` → 编译器优化成 `while(true)`）。
- **mutex同样建立happens-before**——很多人把锁和内存模型割裂开，其实mutex的unlock自带release语义，lock自带acquire语义，是最可靠的同步机制。
- **可见性 vs 顺序性是两件不同的事**——relaxed只保证单个原子变量的原子性（可见性），不保证跨变量的顺序（a=1, b=2的顺序在其他线程看来可能颠倒），这是很多bug的根源。

**对小涵的关联**：小涵用Unity/C#，C#的内存模型基本遵循类似的规则（.NET内存模型也定义了volatile、Interlocked等）。理解C++内存模型的底层逻辑，对写Unity中的多线程代码（Job System、Burst Compiler、ECS）有直接帮助——本质上都是同一套"什么时候我的写入能被另一个线程看到"的问题。

## 📌 关键要点

- **sequenced-before**：单线程内部，前面的语句一定先于后面的语句完成。但不保证对其他线程的可见性——CPU写缓冲区和编译器重排可能让其他线程看到"颠倒"的结果
- **synchronizes-with**：跨越线程的同步关系。release store → acquire load配对，Producer在release前的所有写入（包括普通变量）对Consumer在acquire后的所有读取可见
- **happens-before**：核心偏序关系，具有传递性。A sequenced-before B + B synchronizes-with C + C sequenced-before D → A happens-before D
- **数据竞争 = 未定义行为**：两个不同线程访问同一内存位置，至少一个写，且无happens-before关系。后果不是"偶尔读错"，而是编译器可能做出完全错误的优化（如将while(!stop)优化为while(true)）
- **mutex也在建立happens-before**：unlock自带release语义，lock自带acquire语义。锁同一把mutex = 安全；锁不同的mutex = happens-before链断裂 = bug
- **修改顺序（Modification Order）**：每个原子变量有独立的修改顺序，所有线程认可同一顺序。relaxed也保这个，但只限于单个变量
- **可见性 vs 顺序性**：relaxed只保可见性（单个原子变量的原子读写），release/acquire在此基础上保跨变量顺序，seq_cst把全部原子操作排进全局顺序
- **为什么需要这么复杂？** 性能——如果每次写入都要等所有核心确认，CPU的写缓冲区和编译器指令重排就没意义了。C++选择把控制权交给程序员，通过memory_order精确控制同步成本

## 原文

上一章讲完了 `std::atomic` 的基础保证：单个对象上的读、写、读改写都是原子的，不会被撕裂，不会丢更新。但在实际的多线程代码里，我们经常看到一种写法：一个线程先准备好一批普通数据，然后翻一个原子标志位；另一个线程轮询标志位，看到翻转后就去读那批数据。

```cpp
int data = 0;
std::atomic<bool> ready{false};

void Producer() {
    data = 42;
    ready.store(true);
}

void Consumer() {
    while (!ready.load()) {
    }
    Use(data);
}
```

`ready` 是原子变量，并发读写它没问题。但 `data` 不是原子变量——它只是一个普通的 `int`。Consumer 在看到 `ready == true` 之后去读 `data`，凭什么能保证读到的是 42 而不是 0？ `std::atomic` 只保护了 `ready`，它怎么连带着把 `data` 也保护了？

这个问题的答案不在 `std::atomic` 本身，而在 C++ 内存模型。内存模型定义了一套规则，告诉我们在什么条件下，一个线程的写入对另一个线程可见。

## 单线程里的顺序：sequenced-before

sequenced-before（先序于）只描述当前线程内部的顺序。它不对其他线程做任何承诺。Consumer看到ready==true之后去读data，如果没有额外的同步机制，可能读到0——因为data=42这个写入可能还没有对Consumer所在的CPU核心可见（写缓冲区Store Buffer + 编译器指令重排）。

## 跨线程同步：synchronizes-with

最常见的建立方式：release/acquire配对。

- Producer用 `release` 语义写入ready：store之前的所有写入（包括普通变量）都不允许被重排到store之后
- Consumer用 `acquire` 语义读取ready：load之后的所有读取不允许被重排到load之前
- 当Consumer的acquire load读到了Producer的release store写入的值，建立synchronizes-with关系

同步链：data=42 sequenced-before ready.store(release) synchronizes-with ready.load(acquire) sequenced-before Use(data) → data一定=42。

## happens-before：内存模型的核心偏序

happens-before的建立方式：①同线程sequenced-before ②跨线程synchronizes-with + sequenced-before传递。happens-before可传递（A→B, B→C → A→C）。不是物理时间先后，是C标准定义的逻辑关系。

## mutex 也建立 happens-before

mutex的unlock自带release语义，lock自带acquire语义。Producer lock_guard析构(unlock release) → Consumer lock_guard构造(lock acquire)，建立synchronizes-with。必须锁同一把mutex，不同mutex = 没有同步关系。

## 数据竞争：内存模型画的红线

定义：两个不同线程访问同一内存位置，至少一个写，无happens-before关系 → 数据竞争 = 未定义行为。编译器会假设不存在数据竞争来做优化推理，可能导致死循环等灾难性后果。解决方案：std::atomic 或 std::mutex。

## 修改顺序：每个原子对象有自己的时间线

每个原子变量有独立的、所有线程认可的修改顺序。不同原子变量的修改顺序彼此独立。即使relaxed也保证单个变量的修改顺序一致（不会出现线程A看到1→2→3，线程B看到3→1→2）。

## 可见性和顺序性是两件不同的事

可见性（Visibility）：一个线程写入的值，另一个线程能不能看到。顺序性（Ordering）：多个写入之间的先后关系，是否能被其他线程正确感知。release/acquire同时解决两者；relaxed只解决可见性（单个原子变量），不解决跨变量顺序性。

## 为什么需要这么复杂的模型

答案是性能——CPU写缓冲区、编译器指令重排都是巨大的性能优化。C++选择把控制权交给程序员：默认允许重排和延迟，用memory_order精确控制同步点。seq_cst（最强保证/最高代价）→ release/acquire（定向可见性/适中）→ relaxed（最弱/最低代价）。

## 内存模型全景：五条核心规则

1. sequenced-before管单线程
2. synchronizes-with管跨线程
3. happens-before是可见性保证
4. 没有happens-before = 数据竞争 = 未定义行为
5. 每个原子变量有自己的修改顺序

> 作者：程序喵大人 | 系列前四章：多线程读写出错原理、锁的作用、volatile真相、std::atomic基础保证
