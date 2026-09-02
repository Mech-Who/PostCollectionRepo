---
id: kf-2026-09-02-游戏开发-腾讯WeTest-AI测试智能体架构
title: 腾讯 WeTest AI 测试智能体 — 决策/执行/验证三层协同
type: fragment
domain: 游戏开发
layer: layer2
source_type: blog
source_ref: [[2026-09-02_腾讯游戏两套AI测试方案从脚本到智能体]]
source_url: https://mp.weixin.qq.com/s/p61fZyaMBHi7DDIxIsrpPw
tags: [腾讯, WeTest, AI测试, 游戏测试, AI Agent, 证据链, 强化学习, 黑神话悟空, 可复用架构, 视觉导航]
related_fragments: [kf-2026-08-27-AI技术-TDSQLNexa-Agent数据底座]
related_concepts: [ai-agent-架构, 游戏工程-AI辅助开发工具链, harness-engineering]
status: stable
created: 2026-09-02
version: 1
---

# 腾讯 WeTest AI 测试智能体 — 决策/执行/验证三层协同

## A — Applicable：什么时候用

- 设计游戏自动化测试 / 游戏 AI Agent 时，纠结「脚本 vs 大模型」的分工
- 想把测试从「脚本跑完了吗」升级到「游戏状态是否在预期内且可验证」、从「发现现象」升级到「定位根因」时
- 做 Unity 系统（战斗/寻路/ECS）的调试与验证，想引入「时间线对齐 + 证据留痕」能力时

## B — Boundary：边界条件

- **适用前提**：可拿到结构化游戏原生数据（坐标/状态/事件/日志）的场景；有专业团队做模型微调与 RL 训练
- **不适用的场景**：拿不到内部状态、只能纯像素输入的外部黑盒场景（此时用可复用架构的 VLM 纯视觉路线）
- **注意事项**：
  - 不要迷信「纯画面 + 大模型」——视觉直观但不精确，结构化原生状态才让 Agent 最可靠
  - 跨游戏迁移不能全自动完成：可复用的是架构/接口/训练管线/评估方法，每款游戏仍需专门 SFT + RL

## C — Core：核心要点

1. **共同架构原则**：把「决策」和「执行」分开，把「执行」和「验证」闭环——慢的想清楚、快的做稳定、最后拿证据确认
2. **Acorn 三能力**：感知（静态游戏知识 + 动态运行时状态）→ 操作（Agent 只决策何时调用脚本/Skill，微观操作仍由脚本完成）→ 判断（靠日志/性能数据/状态帧等硬证据校验）
3. **Acorn 四层架构**：中心 Agent Loop + 知识层（Game Graph/Skill Library/State Model）+ 运行时可观测层（Action Trace/UI 截图/日志/遥测毫秒级对齐成证据链）+ 分析与学习层（验证→归因→反哺）
4. **证据链价值**：多源数据毫秒级对齐到同一时间节点，事件发生时瞬间聚合还原现场；把测试从「发现掉帧」升级到「定位根因（哪个函数/资源调用导致）」
5. **可复用架构三级分工**：Brain（System 2 视觉理解/长程规划）+ Cerebellum（System 1 低延迟帧级执行，三阶段训练）+ Master Agent（编排/状态记忆/切换控制权）；黑神话悟空约 9 小时自主通第一章、Boss 胜率泛化到未训练 Boss（地狼 90%/沙国王 80%）

## D — Data：关键示例

```text
# Acorn Agent Loop 四层
中心 Agent Loop
├ 知识层：Game Graph / Skill Library / State Model（从规则/功能清单/文档提取）
├ 可观测层：Action Trace / UI 截图 / 日志 / 遥测 → 毫秒级对齐 = 证据链
└ 分析学习层：验证 → 归因 → 反哺知识层与 Skill 库

# 性能测试四阶闭环
探索（30 次运行聚类性能尖峰 → 收窄到 Area B 热点）
→ 发现 → 调查（定向复现 + utrace/深层 Trace 定位关键路径函数）→ 证明

# 可复用架构（黑神话悟空评估）
Cerebellum（System 1）：紧凑 VLM、纯像素、可变长键鼠 Action Chunk、三阶段训练
Brain（System 2）：视觉理解/长程规划/导航/GUI
Master Agent：编排/状态记忆/控制权切换
数据：约 120h 轨迹 SFT + 50h 战斗 RL；训练集仅第一章 3 Boss → 泛化地狼 90%/沙国王 80%
导航：VPR（视觉位置识别）+ VO（视觉里程计）+ 拓扑记忆地图（不几何重建）

# 四条共同原则
优先依赖结构化原生状态 / 验证深度融入执行 / 沉淀失败经验实现自愈 / AI 决策+脚本执行+证据验证融合（不取代脚本）
```

---

来源：游戏那点事整理的 gamescom dev 现场分享实录（叶桂生 + 高文）
