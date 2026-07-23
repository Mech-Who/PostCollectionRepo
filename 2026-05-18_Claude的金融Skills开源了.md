---
title: Claude 的金融 Skills 开源了
date: 2026-05-18
category: AI应用
depth: 标准
tags: [Claude, 金融AI, Skills, Anthropic, 开源, ClaudeCode]
summary: Anthropic 官方开源了 claude-for-financial-services 仓库，包含 11 个金融 Agent 和 7 个垂直行业插件包，覆盖投行、股票研究、私募股权、财富管理等核心场景，本质是一份企业级 AI Agent 的参考实现。
source_url: https://mp.weixin.qq.com/s/8_S8ynPyy7SHy_OW0lbYuA
source: weixin
status: 📥已采集
---

> **摘要：** Anthropic 官方开源了金融行业 Claude Skills 仓库（claude-for-financial-services），包含 11 个端到端 Agent（如 Pitch Agent、Model Builder、Earnings Reviewer）和 7 个垂直行业插件包（投行、卖方研究、PE、财富管理、基金运营等）。仓库采用 Markdown + YAML 无构建步骤的设计，同时支持 Claude Cowork 插件模式和 Managed Agents API 无头模式部署。底层 11 个 MCP 数据连接器（Daloopa、FactSet、S&P Global 等）是真正的护城河，但需要数据商订阅。核心价值不是产品，而是企业级 AI Agent 的参考实现和 Skill 写作范本。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章的价值不在"金融 AI"本身，而在 Anthropic 展示的**企业级 Agent 工程化范式**。

几个关键洞察：

1. **责任边界划得极其干净**——官方明确说这些 Agent 是"起草工作底稿的，不做投资决策、不执行交易"，这种"能跑活但不背锅"的定位是金融 To B 落地的现实姿态。很多 AI 产品失败不是因为技术不行，而是责任归属没想清楚。

2. **文件即架构（file-based architecture）**——全部 Markdown + YAML，没有 build step，fork 即改。这种设计对二开极其友好，金融机构 IT 团队拿来做骨架改一改就能用。这暗示了 Claude Skills 体系的未来方向：Skill 本身应该是可读、可改、可版本控制的。

3. **MCP 连接器才是护城河**——11 个数据连接器覆盖了 Daloopa、FactSet、S&P Global、Moody's 等金融数据巨头。AI 模型本身越来越commodity，但数据接入的适配工程是深壁垒。这也提醒我们：做 AI 应用时，"连接什么数据"比"用什么模型"重要得多。

4. **对国内场景的参考价值有限**——大部分连接器是海外数据源，A 股、港股需要自己接。但这份仓库作为"Skill 写作教科书"的价值是跨地域的，去翻一翻 `plugins/agent-plugins/pitch-agent/` 的目录结构就知道好的 Skill 怎么组织了。

## 原文
（完整原文见公众号"老章很忙"）

关于 Claude Skills，我之前写过几篇：

*   [大模型世界新宠，Agent Skills 10000字教程](http://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649006999&idx=1&sn=f7ac86380ca2572cc91a66f4c2f16da8&chksm=879331bdb0e4b8abf6ea86b057649ae5ff8ab0bae8b140092446c256cbca9918fdad6a4bb24f&scene=21#wechat_redirect)
*   [AI时代，PPT的未来是HTML，一个神奇的 Skills 推荐](http://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649007136&idx=1&sn=17eb37522718519d867a10ab66069088&chksm=8793360ab0e4bf1c723b697978fbc6f34535e0c42a4205c3021517df4b597572595975d11f36&scene=21#wechat_redirect)
*   [Claude Code 是需要管的，实测一个靠谱的Skills](http://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649007136&idx=2&sn=886c8ba39823af88ff5fa228be3f7b43&chksm=8793360ab0e4bf1c8ad6e1c85dd84636967a22e9b0a6a694d4b814e324f03d665c7226e0289c&scene=21#wechat_redirect)
*   [大模型将超长文章转知识卡片，Skills实现过程分享](http://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649006211&idx=1&sn=a212dd928bc16c9461539673e0da6885&chksm=879332a9b0e4bbbf169627dc83307b622c5aba3852605a3c009d19c0e555e3e28f490d7b16ee&scene=21#wechat_redirect)

之前看到的 Skills 大多是社区开发者鼓捣出来的小工具。Anthropic 官方亲自下场了，仓库名字叫 `claude-for-financial-services`，一上来就把投行、股票研究、私募股权、财富管理这四条华尔街最贵的赛道全端了出来。

仓库地址：github.com/anthropics/financial-services

License 是 Apache 2.0，全部 Markdown + YAML，没有 build step，fork 下来就能改。

**一、它到底是个啥**

简单说，Anthropic 把华尔街分析师每天干的活，拆成了一套 Claude 可以直接装的插件包。官方原话——这些 Agent 是替分析师起草工作底稿（模型、备忘录、研报、对账单）的，**不做投资决策、不执行交易、不绑定风险、不批准开户**。

整个仓库分两层：
- **Agents（11 个）**：端到端的工作流智能体
- **Vertical Plugins（7 个垂直行业包 + 2 个合作伙伴包）**：底层的 Skill、斜杠命令、数据连接器

所有东西**两种部署方式同源**——既能在 Claude Cowork 里当插件用，也能通过 Claude Managed Agents API（`/v1/agents`）丢到自家工作流引擎后面跑无头模式。

**二、11 个 Agent 覆盖场景**

| 业务方向 | Agent | 干什么活 |
|---------|-------|---------|
| 客户与咨询 | Pitch Agent | 可比公司 + 先例交易 + LBO → pitch deck |
| | Meeting Prep Agent | 客户会议前 briefing pack |
| 研究与建模 | Market Researcher | 行业概览 + 竞争格局 + 标的清单 |
| | Earnings Reviewer | 财报电话会 → 更新模型 → 起草研报 |
| | Model Builder | DCF、LBO、三表模型，直接在 Excel 里跑 |
| 基金运营 | Valuation Reviewer | 估值模板 → LP 报告 |
| | GL Reconciler | 总账对账 break 追溯 |
| | Month-End Closer | 月末结账 |
| | Statement Auditor | LP 报表审计 |
| 运营与开户 | KYC Screener | 解析开户文档 + 规则引擎 |

**三、底层 Skill 才是真宝藏**

Vertical Plugins 是底盘，先装 `financial-analysis` 核心包，再按需叠垂直行业。

核心 Skill 包括：`comps-analysis`（`/comps`）、`dcf-model`（`/dcf`）、`lbo-model`（`/lbo`）、`3-statement-model`、`audit-xls`（`/debug-model`）、`ppt-template-creator`。

垂直行业：investment-banking（投行）/ equity-research（卖方研究）/ private-equity（私募股权）/ wealth-management（财富管理）/ fund-admin & operations（运营）。

**四、11 个数据连接器**

Daloopa（标准化财务数据）、Morningstar、S&P Global、FactSet、Moody's、MT Newswires、Aiera、LSEG、PitchBook、Chronograph、Egnyte。

**五、安装方式**

Claude Code 三行命令：
```bash
claude plugin marketplace add anthropics/claude-for-financial-services
claude plugin install financial-analysis@claude-for-financial-services
claude plugin install pitch-agent@claude-for-financial-services
```

**六、真实定位**

这不是一个产品，是一份**参考实现**。官方说「这些都是参考模板，按你公司的方式调一调才好用」。整个仓库 file-based，Markdown + YAML，没有 build step，对二开极其友好。

**七、我的判断**

Anthropic 这一手是在**给整个企业级 AI Agent 行业立标准**。把 Skill 系统从「社区好玩工具」推到了「金融机构生产级参考实现」的台阶上。对我们普通开发者来说，这是一份免费的 Skill 写作教科书。

#ClaudeSkills #Anthropic #金融AI #ClaudeCode #开源

## 相关笔记
- [Harness Engineering：耗时一周，我是如何构建 AI 编程工作流的](2026-05-16_Harness Engineering：耗时一周，我是如何构建 AI 编程工作流的.md) — 同为 AI Agent 工程化实践
