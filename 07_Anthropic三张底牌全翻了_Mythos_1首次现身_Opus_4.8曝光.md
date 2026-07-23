---
url: https://mp.weixin.qq.com/s/77A38l8_iyaVA7u7wL6-7w
title: Anthropic三张底牌全翻了！Mythos 1首次现身，Opus 4.8曝光
date: 2026-05-25
source: weixin
status: ok
category: AI技术
depth: 🟡标准
tags: [Anthropic, Claude, Opus, Sonnet, Mythos, 安全模型, AI竞赛]
author: 新智元
layer: layer2
sync_si: true
---

## 摘要

Anthropic三大模型几乎同时曝光：Claude Opus 4.8在Google Vertex后台被发现、Sonnet 4.8跳过4.7版本通过51万行意外泄露代码证实、曾被称为"太危险"的Mythos 1安全模型也在Claude界面中短暂现身，标志着AI ASI竞赛全面加速。

---

## Opus 4.8惊现

开发者在Google Vertex AI后台发现"claude-opus-4.8"模型标识。此前Anthropic的Opus 4.6和4.7都是先在Vertex AI被发现后才正式发布，暗示Opus 4.8已进入测试阶段，预计下个月正式发布。

## 51万行源码泄露Sonnet 4.8

Anthropic在推送Claude Code npm更新时忘记在.npmignore中加上.map文件，导致59.8MB、51.2万行TypeScript源码被推送到npm公共仓库。泄露代码确认Sonnet 4.8将跳过4.7版本，预计四大升级：视觉能力飙升（UI识别超98%）、编程能力大幅提升、新增"X high"推理层级、更新的分词器（Token消耗增30%）。

## Mythos 1安全模型解禁

曾被称为"太危险"不公开的Mythos安全模型在Claude界面中短暂现身。Anthropic正将其从受限的安全研究工具转变为面向开发者的专业产品线，包括Claude Code + Mythos（安全编程助手）和Claude Security + Mythos（企业级漏洞发现与修复平台）两条产品线。

## 三线作战的ASI竞赛

这一波连环曝光显示Anthropic正在三线并进。AI进化的速度已脱离线性叙事，Mythos的商业化意味着AI已拥有颠覆网络世界攻防格局的能力，这是迈向ASI阶段的必经之路。

---

## 金句

> 1. "Anthropic三大'杀手锏'，一口气全曝光了！"
> 2. "AI进化的速度，已经彻底脱离了线性叙事。"
> 3. "Anthropic正在用'代码+安全'的双螺旋结构，为通往ASI的暴力美学扣上最后一枚安全锁。"
> 4. "最让人细思极恐的，是走向商业化的Mythos 1。"

---

## 我的理解

这则报道的核心信号不是模型版本号之争，而是 **Anthropic 正在构建"代码 + 安全"的双螺旋产品矩阵**。三线并进（Opus 前沿能力、Sonnet 性价比、Mythos 安全商业化）本质上是把"安全"从一个研究课题转化为可销售的产品线。最具战略意义的不是 Opus 4.8 的迭代升级，而是 Mythos 1 从"太危险不公开"到"走向商业化"的态度逆转——这意味着 AI 安全能力本身已经成为竞争壁垒和商业价值。对于 AI 应用开发者的启示：如果你依赖 AI API，需要关注"安全层"是否会成为下一代 API 的标配组件。

---

## 原文

**新智元报道**

**【新智元导读】** 几乎同一天，Anthropic三大超级AI提前曝光！Claude Opus 4.8突袭谷歌后台，Sonnet 4.8跳级4.7。曾经叫嚣着「太危险不公开」的Mythos 1，也现身了。

Anthropic三大「杀手锏」，一口气全曝光了！

就在今天，开发者在Google Vertex后台，意外发现一个新的模型标识——claude-opus-4.8。

时隔一个多月，Claude又一次大版本更新已经箭在弦上，呼之欲出！

几乎同一天，代号Mythos 1的「安全专用模型」，也在Claude界面中短暂现身。

而且，源码中新增了指向Claude Code和Claude Security的字符串。

另外，此前全网疯传的51万行泄露代码，提前剧透了Claude Sonnet 4.8。

代码还证实了，它将直接跳过4.7版本，或于6月中旬震撼发布。

Sonnet 4.8预计会继承Opus 4.7的视觉升级，在UI设计稿、架构图上，视觉准确率超98%。

不仅如此，它生成的代码将更加干净利落，还支持高级推理。

不难看出，Anthropic正三线并进，火力全开。

毕竟在IPO前夕，OpenAI依旧步步紧逼：下一代GPP-5.6现身，拥有极其强悍的前端爆发力。

再加上，谷歌Gemini 3.5 Pro也将于6月入局。

硅谷的ASI终极之战一触即发，三巨头的「贴身肉搏」，现在才真正开始。

---

**Opus 4.8惊现，全部底牌曝光**

4月，Claude Opus 4.7爆更，击败了全球顶流Gemini 3.1 Pro、GPT-5.4。

短短一个多月时间，Anthropic内部又训出了Opus 4.8。

开发者can最先爆料：在Google Vertex AI平台的模型列表中，赫然出现了「claude-opus-4.8」的标识。

消息一出，全网坐不住了。

顺便提一句，Anthropic此前两次重大发布——

Opus 4.6、Opus 4.7，都是先在Vertex AI的后端被提前发现，然后才正式公布。

这意味着，已在测试中的Opus 4.8，离真正发布不远了，许多人预计下个月就可以看到。

---

**51万行源码泄「天机」，Sonnet 4.8跳过4.7**

Opus 4.8的曝光让人兴奋，但Sonnet 4.8的信息其实更早泄露。

早在3月31日，Anthropic在推送Claude Code的npm更新（v2.1.88版本）时，犯了一个令人窒息的低级错误——

有人忘了在.npmignore文件中加上.map这一行。

就这一行配置的缺失，导致一份59.8MB、包含51.2万行TypeScript代码、1900个内部文件的source map被完整推送到了npm公共仓库。

Claude Code之父Boris Cherny事后确认，这是一个「普通的开发者失误」。

但这个「普通失误」暴露的信息量，堪称Anthropic有史以来最大规模的内部泄露。

而就在泄露代码里，确认的关键信息——

在未发布的关键词过滤器中，出现了Sonnet 4.8和Opus 4.7的引用，没有任何Sonnet 4.7的痕迹。

这直接确认了一件事：Anthropic打算跳过Sonnet 4.7，直奔4.8。

根据泄露信息和社区分析，Sonnet 4.8预计将带来四大升级：

- **视觉能力飙升**  
  继承Opus 4.7的视觉升级，对UI Mockup和复杂架构图的识别准确率，有望突破98%。  
  Opus 4.7在视觉准确率上已经达到了98.5%，Sonnet 4.8将把这个能力下放到更便宜的模型层级。

- **编程能力大幅提升**  
  更干净的一次性代码生成，更精确的「指令遵循」。

- **新增「X high」推理层级**  
  一种新的推理强度设定，能在不显著增加生成时间的前提下，增强逻辑推理能力。

- **更新的分词器**  
  坏消息是，Token消耗量将增加约30%。同样的prompt，新版分词器会用掉更多Token。

---

**Mythos 1能用了？Anthropic突然改口**

比Claude 4.8更猛的是，那个传说中「太危险」的Claude Mythos真的要来了！

就在昨天，Anthropic发布首份报告，公开了过去一个月，Claude Mythos所有战果——

在关键软件中，10000万个高危漏洞全被揪出。

才过一天，AI测试追踪平台TestingCatalog爆料：

有用户在Claude界面中，短暂看到了「Mythos 1」模型选项。

虽然很快消失，但源代码中新增的字符串泄露了关键信息：Claude Code，Claude Security。

这意味着Anthropic正在将Mythos从一个受限的安全研究工具，升级为面向开发者的**专业产品线**。

模型标识为「claude-mythos-1-preview」，明确指向代码生成和安全两大应用场景。

此前，Anthropic的口径一直是：Mythos太危险，不会公开发布。

但最新的Project Glasswing更新中，Anthropic的态度正在微妙转变，出现了一段耐人寻味的表述——

期待通用发布

这个措辞的转变，意味着Mythos走向大众只是时间问题。

与此同时，Claude Security的产品化工作也在加速推进。

一个全新的安全仪表盘正在搭建中，将展示已发现的漏洞、7天和30天历史图表、以及更深层的分类分析结果。目前仅面向企业客户。

这意味着，Anthropic正在将Mythos从一个「研究预览」转变为一个可商业化的安全产品矩阵：

- **Claude Code + Mythos**：面向开发者的安全编程助手
- **Claude Security + Mythos**：面向企业的自动化漏洞发现与修复平台

代码生成与代码安全，两手都要抓，两手都要硬。

---

**三线作战，ASI竞赛加速**

这一波连环曝光，彻底扯下了AI竞赛最后的温情面纱。

三线并进，火力全开。

Anthropic这一次倾巢而出的底牌，向全行业传递了一个极其明确的信号：

AI进化的速度，已经彻底脱离了线性叙事。

最让人细思极恐的，是走向商业化的Mythos 1。

作为曾经的「安全禁地」，它的解禁意味着，AI已经拥有了颠覆网络世界攻防格局的能力。

这恰恰是，迈向ASI阶段的必经之路。

超级智能的诞生，从来不只是拼算力和参数的堆砌，而是看它能否在拥有毁灭性破坏力的同时，具备绝对的自我规训与安全进化能力。

Anthropic正在用「代码+安全」的双螺旋结构，为通往ASI的暴力美学扣上最后一枚安全锁。

GPP-5.6、Gemini 3.5 Pro步步紧逼，在这场诸神之战中，谁能率先推开ASI的大门？

**编辑：** 桃子 David
