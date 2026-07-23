---
title: Anthropic凌晨发布Mythos 5！性能断层领先
date: 2026-06-10
category: AI技术
depth: 标准
layer: layer1
tags: [Anthropic, Mythos, Fable, 大模型, AI竞赛, Claude]
summary: Anthropic发布Fable 5/Mythos 5模型，基准测试断层领先。Fable 5为面向公众的"安全受限版"，Mythos 5为能力完全释放版。Stripe报告称Fable 5在5000万行代码的Ruby代码库中一天完成迁移。定价为Opus的两倍。
source_url: https://mp.weixin.qq.com/s/lvskGyt5aOZfO2VJjLnvbA
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** Anthropic发布Fable 5/Mythos 5模型，基准测试断层领先。Fable 5为面向公众的"安全受限版"，Mythos 5为能力完全释放版。Stripe报告称Fable 5在5000万行代码的Ruby代码库中一天完成迁移。定价为Opus的两倍。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章最值得关注的点不是模型性能有多强，而是三个信号：

1. **"安全护栏"成为模型分层的新维度**：Fable 5 = Mythos 5 + 严格安全限制，生物学/化学问题回退到Opus 4.8。模型能力已经强到需要主动"捂住嘴"的程度——这不再是技术问题，而是治理问题。

2. **"模型和工具不再有区别"**：Dan Shipper说的这句话很有意思。当模型能一天完成5000万行代码的迁移，Claude Code作为Coding Agent的价值就不是"辅助"而是"替代"了。持续关注这个方向对推文体系相关。

3. **OpenAI压力山大**：内部高管离职潮+GPT-5.6在6月发布，大模型领先者正在快速轮换。这不是一家独大的局面，对开发者来说是好事——模型选择更多，竞争压价。

不过要注意的是，Fable 5定价是Opus的两倍（输入$10/M，输出$50/M），长期来看Coding Agent的成本还需关注。

## 原文

**核心数据**：
- **Fable 5**（安全版）：面向公众开放，严格安全护栏
- **Mythos 5**（完全版）：仅向少数受信任机构开放
- **定价**：输入$10/M token，输出$50/M token（Opus的两倍）
- **即日至6月22日**：Pro/Max/Team/企业版套餐内免费

**基准测试亮点**：
- **Stripe报告**：在5000万行Ruby代码库中，一天完成全量迁移（团队手动需2个月）
- **FrontierCode评估**：在高质量生产代码标准下，所有模型中得分最高
- **财务推理**：Hebbia高级推理测试中所有模型最高分
- **视觉任务**：仅凭屏幕截图重建Web应用源码；仅用纯视觉组件通关《宝可梦火红》
- **长上下文**：处理数百万Token长时间任务

**争议点**：
- 用户反馈：跟Claude说句"你好"被标记为高风险行为
- 生物学/化学问题回退到Opus 4.8
- 当用于前沿LLM开发时，系统会通过提示修改、引导矢量等方法限制模型功能，不通知用户
- 网友评论："OpenAI的时代已经结束了"

**行业背景**：
- OpenAI内部：高管离职潮、秘密提交IPO招股书、美国政府介入
- GPT-5.6预计6月发布
- Anthropic从Claude模型框架（Haiku/Sonnet/Opus）延伸出Fable/Mythos新线
