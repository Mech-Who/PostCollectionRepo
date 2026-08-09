---
id: kf-2026-08-09-守望先锋StateScript技能系统
title: 守望先锋 StateScript：节点图+数据驱动的技能配置系统
type: fragment
domain: 游戏开发
layer: layer2
source_type: blog
source_ref: [[2026-08-09_守望先锋StateScript技能系统一个技能一张图]]
source_url: https://www.xiaoheihe.cn/app/bbs/link/6e8272417fa9
tags: [StateScript, 技能系统, 节点图, 数据驱动, 网络同步, 状态机, 可视化脚本, 守望先锋]
related_fragments: [kf-2026-08-08-游戏开发-组合模式与游戏UI层级管理]
related_concepts: [软件设计架构, 游戏工程-服务器架构演进]
status: stable
created: 2026-08-09
version: 1
---

# 守望先锋 StateScript：把技能做成"一张图"

## A - Applicable：什么时候用

- 设计**技能数量多、结构重复度高、需要策划频繁调平衡**的游戏（FPS/MOBA/ARPG 英雄技能）
- 需要让**策划不写代码**就能创建和调整技能时
- 需要在**多人联网**环境下做技能系统时（本文给出了完整的网络同步方案）
- 用户说"怎么设计技能系统""如何让策划配置技能""技能数据驱动"时命中

## B - Boundary：边界条件

- **适用前提**：有足够前期投入搭建节点图框架（节点系统+加载器+编辑器+网络同步推导）
- **不适用的场景**：技能数量少的小项目（<20 个技能）——框架成本高于收益，是过度设计
- **注意事项**：
  - 回滚重放时特效重复播放是经典坑——副作用必须挂"帧末净变化回调"，不能挂 OnActivate
  - "蓝图是画图写程序，StateScript 是画图定义状态机"——State 的持续性生命周期是核心，不是普通脚本
  - 属性值不一定是常量：要支持 Config Vars 表达式，平衡公式才不用改代码

## C - Core：核心要点

- 五种基础节点：Entry（入口）/ Condition（布尔分支）/ Action（瞬时原子操作）/ State（持续性行为，OnActivate→OnTick→OnDeactivate）/ Subgraph（子图复用）
- Variables 与 Properties 分离：Variables 是图运行时数据（含 state-defined 活数据），Properties 是节点行为配置，属性值可读 Config Vars 表达式
- 网络同步三特性：[Mirror]（字段自动同步）/ [SyncAll]（远程也 tick 此 State）/ [AuthorityOnly]（远程跳过副作用但图链照常推进）——结构推进与副作用执行解耦
- 三运行模式：Authority（服务器）/ Predicted（本地预测+回滚）/ Replica（远程表现），远程同步变量由加载器编译期自动推导

## D - Data：关键示例

```text
// 蓄力冲刺技能节点图（作者 Godot 项目实战）
Entry → LogicalButton(监听F)
  → 按下F: Wait(1秒) → Action(设置 isCharged = true)
  → 松开F: Condition(isCharged?)
    → true:  Dash(冲刺) → Buff(加速5秒) → Action(isCharged = false)
    → false: 什么都不发生

// 网络同步特性声明示例
[SyncAll]      // 远程客户端也激活并tick这个State（弹体飞行/爆炸）
class WeaponVolleyState : State {
    [Mirror] float chargeTimer;   // 字段自动捕获/恢复，不手写序列化
}
[AuthorityOnly] class DealDamageAction : Action { }  // 远程跳过执行伤害

// 属性表达式示例（平衡公式不改代码）
Damage = LevelVar * 1.5 + Bonus   // 属性值可以是Config Vars表达式
```
