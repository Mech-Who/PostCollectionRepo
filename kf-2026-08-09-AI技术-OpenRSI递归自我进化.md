---
id: kf-2026-08-09-AI技术-OpenRSI递归自我进化
title: OpenRSI：AI 改进 AI 的可执行工程框架
type: fragment
domain: AI技术
layer: layer2
source_type: weixin
source_ref: [[2026-08-09_清华开源OpenRSI递归自我进化工程化]]
source_url: https://mp.weixin.qq.com/s/qkf-LOMFSMcs2g_SyuKviA
tags: [RSI, 递归自我进化, OpenRSI, 原子算子, 进化算法, 强化学习, 上下文管理, 消融实验]
related_fragments: [kf-2026-08-09-AI应用-Graft代码地图省Token]
related_concepts: [harness-engineering, llm-技术前沿, ai-Agent基础设施栈]
status: stable
created: 2026-08-09
version: 1
---

# OpenRSI：把"AI 改进 AI"做成可消融、可复现的工程系统

## A - Applicable：什么时候用

- 设计**自我改进/搜索增强的 agent 系统**，需要让模型在长程任务中自己改进生成结果时
- 需要**分离"模型功劳"与"框架功劳"**做系统评估时（消融设计可直接复用）
- 长程 agent 任务中**上下文预算紧张**、需要按需检索而非全量历史时
- 用户说"递归自我进化怎么做""AI 改进 AI""搜索+训练闭环"时命中

## B - Boundary：边界条件

- **作者自划边界**：OpenRSI 是"元进化"（Meta-Evolution）——在有边界、可执行的领域训练"改进者"本身，**不声称通用 RSI 已解决**；机制阶梯：进化→自进化→元进化→RSI
- **评估口径**：71.21% 最高分改变的是搜索系统（经验先验+异步搜索），不应解读为纯模型增益——引用时务必区分模型分与系统分
- **协议限制**：CC BY-NC 4.0 非商业协议，商用前要查条款

## C - Core：核心要点

- **四个原子算子**：Draft（从零起草）/ Improve（基于执行反馈改进）/ Debug（修复报错程序）/ Crossover（重组两个父本）——SFT、RL、进化搜索共用同一套动作空间，模型成为自己进化框架的"变异引擎"
- **OpenMLE 三栈闭环**：Gym（构建/执行/质检可验证 MLE 任务包）→ RL（执行反馈做 SFT+在线 RL 学算子）→ Evo（算子组合成长程搜索）；搜索产生经验→经验进训练→训完模型回搜索评测
- **功劳分离消融**：固定框架换模型 39.39%→60.61%；换未训基准 NatureBench Lite 换模型 50%→70%、换框架 20%→50%——训练和框架各自独立提升且可迁移
- **上下文效率是核心竞争力**："全量历史进上下文"→"按算子按需检索有界证据"：总 token 少 41.7%，每百万 token 有效发现高 84.3%（66 任务：模型 token 129.3M→75.3M，prompt token 少 50.3%，每百万 token 新最优更新 1.77→3.27）
- **成绩**：35B 模型单张 RTX 4090（12GB）每任务 12 小时，MLE 基准超 GPT-5.5+Codex，逼近 GPT-5.6 Sol 和 2.8T Kimi K3

## D - Data：关键示例

```text
// 四原子算子动作空间（训练与推理共用）
Draft:     从零起草解决方案
Improve:   基于执行反馈改进
Debug:     修复报错程序
Crossover: 重组两个父本

// 消融实验设计（功劳分离模板）
实验1: 固定框架换模型   39.39% → 60.61%   → 模型贡献
实验2: 换未训基准换模型 50% → 70%          → 模型可迁移
实验3: 换未训基准换框架 20% → 50%          → 框架独立贡献
实验4: +经验先验+异步搜索 → 71.21%         → 系统分，非纯模型增益

// 上下文策略对比（AIRA-Evo → OpenRSI）
全量历史进上下文          → 按算子按需检索有界证据
总token 129.3M → 75.3M（-41.7%）
每百万token有效发现 +84.3%
```

**开源入口**：GitHub FrontisAI/OpenRSI；权重 HF FrontisAI/Frontis-MA1-35B（含 GGUF）；论文 arXiv 2607.28568。
