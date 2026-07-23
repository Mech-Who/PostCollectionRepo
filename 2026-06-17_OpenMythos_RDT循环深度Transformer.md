---
title: OpenMythos — RDT 循环深度 Transformer（Claude Mythos 架构开源复现）
date: 2026-06-17
category: AI 技术
depth: 深度
layer: layer2
tags: [RDT, Transformer架构, Claude Mythos, 循环推理, 连续潜空间, MoE, MLA, DeepSeek, 参数效率, Loop]
summary: OpenMythos 是一个 22 岁开发者基于第一性原理反推 Claude Mythos 架构的开源 PyTorch 项目。核心创新是循环深度 Transformer（RDT）——同一组权重循环 1~16 次，推理在连续隐空间完成，不产生中间 token。770M 参数匹配 1.3B 标准 Transformer 质量，证明"推理深度可以靠推理时 compute 而非参数规模"。
source_url: https://github.com/kyegomez/OpenMythos
source: github
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** OpenMythos 是 Kye Gomez（22 岁独立开发者）2026 年 4 月在 GitHub 发布的开源项目。基于 11 篇公开论文的第一性原理推导，用纯 PyTorch 实现了推测中 Claude Mythos 的核心架构——循环深度 Transformer（Recurrent-Depth Transformer, RDT）。不是模型泄露、不是权重蒸馏、不是微调，纯粹是"论文推导→代码实现"。核心洞察：同一组 Transformer 权重循环执行 1~16 次，每次走不同的 MoE 专家路径，推理完全在连续隐空间完成（不产生中间 token）。770M 参数的 RDT 在同等训练数据下匹配 1.3B 标准 Transformer 质量，揭示了"推理深度 = 推理时 compute，不等于参数规模"这一范式。

## 我的理解
> 由小林生成，供小涵审阅修改

OpenMythos 的真正价值不在于它是不是 Claude Mythos 的正确复现（我们永远不会知道），而在于它把「循环深度 Transformer」这个正在学术界升温的概念变成了**可跑、可配置、可实验的代码**，而非仅仅停留在论文里。

从架构设计角度，RDT 整合了三条独立的技术路线：DeepSeek-V2 的 MLA 注意力（压缩 KV 缓存 10-20 倍）、DeepSeekMoE 的混合专家（每个循环迭代选不同专家组合）、以及 Parcae 论文的 LTI 稳定性约束（谱半径 <1，保证循环不发散）。这意味着中国团队（DeepSeek）在基础架构层的贡献已经渗透到最前沿的推理架构设计中。

对我而言最关键的启发是"深度外推"能力——训练时用 N 次循环，推理时可以用 N+k 次。这跟 CVOGL 定位任务天然呼应：简单场景早停，复杂遮挡场景多迭代。定位精度是否也能靠推理时 compute 换，而不是靠更大的模型参数？这是一个值得探索的研究问题。

更底层的启示：OpenMythos 展示了在不依赖大公司、不依赖大算力的情况下，一个人如何通过阅读公开论文、交叉验证、第一性原理推导，做出有影响力的架构研究。这是对独立研究者赋能的信号。

## 📌 关键要点

- **核心架构 RDT**：Prelude（输入编码）→ Recurrent Block（核心循环，一组权重跑 1~16 次）→ Coda（输出解码）。不同于标准 Transformer 的"一层走过去不回头"
- **隐空间推理 vs 链式思考**：RDT 在连续隐空间内反复深化理解，不产生中间 token。CoT 是「想一步，写一步」；RDT 是「在脑子里反复想 16 遍，想好了再开口」
- **三合一技术栈**：MLA 注意力（DeepSeek-V2，KV 缓存压缩 10-20 倍）+ MoE FFN（DeepSeekMoE，每循环选不同专家）+ LTI 稳定注入（Parcae，谱半径 <1 防发散）
- **状态更新公式**：h{t+1} = A·ht + B·e + Transformer(ht, e)，每次循环重新注入原始输入 e，防止隐状态漂移
- **自适应深度**：ACT（Adaptive Computation Time）——每个 token 自动学出最优循环次数。简单 token 早停，复杂 token 多迭代
- **深度外推能力**：训练时 N 次循环，推理时可用 N+k 次，无需重训就能扩展推理深度
- **参数效率实证**：770M RDT ≈ 1.3B 标准 Transformer（Parcae 论文的 scaling law 验证）
- **ACT + 深度 LoRA**：每个循环迭代附着一个低秩 adapter，让每轮行为略有不同，桥接"纯权重绑定"和"全独立层"

## 原文

### 项目背景

OpenMythos 由 Kye Gomez 于 2026 年 4 月在 GitHub 发布。Anthropic 从未发布 Claude Mythos 的技术论文，但 Gomez 基于 11 篇公开论文（包括 Parcae、DeepSeek-V2、DeepSeekMoE、Saunshi et al. 2025、COCONUT 2024 等）从第一性原理反推了 Mythos 的可能架构。

### RDT 核心机制

在标准 Transformer 中，模型通过一系列唯一层传递输入，每层有独立权重。在 RDT 中，一组固定权重在单个前向传播中被迭代应用最多 16 次。推理深度不是存储了多少参数的函数，而是推理时执行了多少次迭代。

### MoE FFN 设计

使用 DeepSeekMoE 设计：大量细粒度路由专家，每 token 仅激活稀疏的 top-K 子集，外加一小群始终激活的共享专家。路由器在每次循环深度选择不同的专家子集，使每次迭代在计算上有所区别，尽管共享相同的基础权重。

### LTI 稳定性约束

源自 Parcae 架构：强制 A 矩阵的谱半径 ρ(A) < 1，无论学习率或梯度噪声如何都保证稳定性。解决循环模型训练中"残差爆炸"的历史难题。同时 ACT 自适应停机解决"过度思考"问题。

### 参考来源

- GitHub: https://github.com/kyegomez/OpenMythos
- 知乎解析: https://zhuanlan.zhihu.com/p/2049262067161601525
- 百度百科: https://baike.baidu.com/item/OpenMythos/67653470
- OpenClaw 入门: https://openclawapi.org/blog/2026-04-26-openmythos-getting-started

## 相关笔记

- [[llm-推理范式迁移]] — RDT 是连续潜空间推理范式的具体实现，补充了现有概念缺少的"循环 Transformer"分支
- [[llm-技术前沿]] — Mythos 5 + OpenMythos 同属 2026 年 LLM 技术前沿信号
- [[loop-engineering]] — 哲学层面呼应：Loop Engineering 是"用循环替代人工指挥 AI"；RDT 是"用循环替代层层堆叠的 Transformer"
