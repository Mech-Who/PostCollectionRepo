---
title: Game Programming Patterns — Command 模式（设计模式重访）
date: 2026-07-06
category: 游戏开发
depth: 深度
layer: layer2:通用
tags: [command-pattern, 设计模式, 游戏开发, 架构设计, 撤销重做, 输入控制, 命令队列]
summary: Robert Nystrom 的 Command 模式深度讲解——从输入映射、角色控制到撤销重做、网络重放。核心洞见：Command 是"具体化的方法调用"，将方法调用封装为对象，实现解耦、延迟执行、可撤销、可序列化。
source_url: https://gameprogrammingpatterns.com/command.html
source: gameprogrammingpatterns.com
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 这是 Game Programming Patterns 一书中 Command 模式的完整章节。Robert Nystrom 用三个递进的游戏开发场景（输入配置 → 角色控制 → 撤销/重做），展示了如何将方法调用"具体化"（reify）为对象。核心价值在于：一旦方法调用成为一等对象，你就可以延迟执行、队列化、撤销、序列化、网络传输——为游戏架构中的解耦问题提供了优雅的通用解决方案。

## 我的理解

这篇文章最精彩的部分不是 Command 模式本身（它只是个接口带一个 `execute()` 方法），而是 Nystrom 通过三个递进的场景，展示了一个简单模式如何随着需求复杂度自然演化：

1. **输入配置场景**（基础）：按钮 → Command 对象 → 解耦输入与动作。就是「把函数调用包起来」。这本身没太大价值，但为后续扩展铺了路。

2. **角色控制场景**（解耦深化）：把 `GameActor` 传入 `execute(actor)`，让命令不再绑定到特定角色。这个小小的参数化带来了三个连锁能力：
   - 玩家可以控制任意角色（AI 也能用同一套命令）
   - 输入产生器与命令消费者的解耦
   - 命令流可序列化 → 网络多人游戏的基础

3. **撤销/重做场景**（时间旅行）：在每次 `execute()` 时保存状态快照，用 `undo()` 恢复。配合命令历史列表，实现多级撤销和重做。这个方案的优雅之处在于：**只要所有数据修改都通过 Command 进行，撤销就变成了简单的指针移动**。

**核心洞见**：Nystrom 指出了一个关键对比——在 C++ 这种缺乏一等函数的语言中，你需要用类来"模拟"闭包。但在有真正闭包的语言（如 JS）中，Command 模式可以用函数直接实现。这也暗示了：**Command 模式本质上是在弥补语言能力的不足，但它定义的接口（execute + undo）比纯函数更清晰地表达了"可逆操作"这个语义**。

#### 与已有知识的连接

- 这与我们已有的 `软件设计架构` 概念中的 `2026-06-10_设计模式已死AI时代的经典` 形成有趣对照：那篇文章讨论 AI 时代设计模式是否过时，而本文提供了一个设计模式在游戏开发中依然极其鲜活的正面案例。
- Command 模式的"队列化"思路与 Event Queue 模式互补——Game Programming Patterns 将两者作为相邻章节处理。
- 与「微信正在输入原理」的架构思维有共鸣：都是通过增加间接层（间接层 = 命令对象 / 信令握手）来获得额外的系统能力（可撤销 / 削峰）。

## 📌 关键要点

### 方法论核心

- **Command = 具体化的方法调用**：将"做什么"封装为一个对象，使其可传递、可存储、可序列化
- **三层递进复杂度**：输入映射（简单解耦）→ 角色控制（参数化解耦）→ 撤销重做（状态管理）
- **代码层的解耦模式**：`InputHandler → Command → execute(actor)` 的三层架构是游戏输入系统的标准模式

### 实用设计建议

1. **Null Object 模式配合**：与其检查 `NULL` 指针，不如定义一个 `execute()` 什么都不做的命令，减少条件分支
2. **Memento 模式的取舍**：手动存储"变化的状态"比快照整个对象更省内存，因为命令通常只改一小部分状态
3. **持久化数据结构**：作为撤销的替代方案——每次修改返回新对象，旧对象保留，撤销就是切回旧引用
4. **重放实现**：记录每个实体每帧的 Command 流，比记录完整状态快照更省内存

### 代码示例对照

```cpp
// 基础形式：无参数 Command
class Command {
  virtual void execute() = 0;
};
class JumpCommand : Command {
  void execute() { jump(); }
};

// 参数化形式：传入 GameActor
class Command {
  virtual void execute(GameActor& actor) = 0;
};
class JumpCommand : Command {
  void execute(GameActor& actor) { actor.jump(); }
};

// 可撤销形式：绑定具体对象 + 存储历史状态
class MoveUnitCommand : Command {
  Unit* unit_;
  int xBefore_, yBefore_;
  int x_, y_;
  void execute() {
    xBefore_ = unit_->x();
    yBefore_ = unit_->y();
    unit_->moveTo(x_, y_);
  }
  void undo() {
    unit_->moveTo(xBefore_, yBefore_);
  }
};
```

## 原文

（见原始链接：https://gameprogrammingpatterns.com/command.html — Robert Nystrom 的完整章节）

## 相关笔记
- [[2026-06-10_设计模式已死AI时代的经典]] — AI 时代对设计模式的重新审视，与本文形成对照
- 软件设计架构概念（`concepts/软件设计架构.md`）— 本文可补充该概念的 Insight 集合
