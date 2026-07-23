---
title: 如何用AI学会所有东西：基于Obsidian+Claude Code的个人知识库构建
date: 2026-05-20
category: AI应用
depth: 深度
tags: [个人知识库, Obsidian, Claude Code, LLM Wiki, 苏格拉底学习法, AI学习, 知识管理, 论文阅读方法论]
summary: Erber结合Karpathy的LLM Wiki和吴乐旻的苏格拉底学习法，设计了一套AI自动维护的研究型知识库系统——人只负责扔原料和提问，LLM负责维护结构、生成概念连接和用苏格拉底法教学。
source_url: https://mp.weixin.qq.com/s/8UmnbmSgL97Yi5XsSNsdgQ
source: weixin
status: 📥已采集
sync_status: ❌未同步
---

> **摘要：** Erber结合Karpathy的LLM Wiki和吴乐旻的苏格拉底学习法，设计了一套AI自动维护的研究型知识库系统——人只负责扔原料和提问，LLM负责维护结构、生成概念连接和用苏格拉底法教学。并提出了论文/概念的四级分级体系（L0-L4）来避免无限深挖的陷阱。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章跟小涵目前在做的推文知识管理和思源笔记体系高度相关，非常值得认真琢磨。

**核心洞察：知识管理的终极形态不是维护结构，而是让AI自动维护结构**
这个观点解决了知识管理最大的痛点——大部分人搭建完知识管理系统的头两周动力十足，后面就"维护不动"了。Erber经过三次迭代得出的结论是：让人来维护知识结构本身就是不合理的。

我们现在的推文知识管理流程（tweet-knowledge-manager）已经做到了"自动分类+自动加工+自动归档"，但这里还有更深一层——从"归档"到"学习"的跃迁。Erber的体系展示了怎么做：归档后AI自动提炼concepts、自动发现connections、自动生成questions，然后用户可以用苏格拉底法跟AI对话来真正理解内容。

**论文阅读四级分级（L0-L4）非常实用**
这个分级体系直接解决了"学太深vs学太浅"的决策问题。很多知识管理系统的缺陷是"一视同仁"——所有内容经过同样的加工流程。但实际上，95%的文章只需要L1（知道做什么），4%需要L2（能复述），1%需要L3-L4（能实现/能扩展）。给每篇文章标一个目标等级，能大幅节省精力。

**对我们现有体系的启发**
我们现在有7类推文分类 + 三级加工深度（轻量/标准/深度），这个体系可以作为"推文阅读/学习"阶段的补充——在"已加工归档"之后，增加一个"我想学这篇"的按钮，引导用户选择学习深度，然后用苏格拉底法对话。

## 📌 关键要点
- **知识管理的终极形态**：人只负责扔原料和提问，AI自动维护结构、生成概念连接
- **四层Wiki结构**：papers（原始知识粗处理）→ concepts（跨论文聚合）→ connections（跨概念桥梁）→ questions（开放问题驱动下一步）
- **苏格拉底学习法**：AI以问答对话形式教学，逐步深入概念，比被动阅读效果好得多
- **论文/概念四级分级**：L0知道存在 → L1能定位 → L2能使用 → L3能复述/实现 → L4能扩展
- **读论文三阶段**：Global orientation（5min全局定位）→ Local drilling（20-40min苏格拉底追问）→ Global reintegration（5-10min接回知识体系）
- **维护哲学**：不要让人维护笔记结构，让AI持续维护，人只负责扔原料和提问

## 原文

**如何用AI学会所有东西：基于Obsidian+Claude Code的个人知识库构建**

作者：Erber

我的Obsidian最开始是传统派：全部手写。后来有cli工具了，我用Claude Code重构过一次Obsidian，搞完之后还是维护不动，几周就废弃了。后来发现，不对啊，让人来维护本身就是不合理的，AI应该持续维护结构，人只负责扔原料和提问。

这套体系的灵感来源是Karpathy的LLM Wiki和吴乐旻老师的苏格拉底学习法。

### 1. 准备工作

首先你得有一个Obsidian，然后有一个Claude Code。然后在终端创建以下目录：

```
research-wiki
├── claude.md
├── raw
│   ├── assets
│   ├── books
│   ├── clips
│   ├── courses
│   └── papers
└── wiki
    ├── concepts
    ├── connections
    ├── questions
    ├── index.md
    ├── learner_profile.md
    ├── log.md
    ├── papers
    ├── progress.md
    ├── revision_notes.md
    └── system.md
```

`raw` 文件夹是使用者手动维护的，只负责加东西进去。
`wiki` 文件夹是核心，包含LLM-Wiki区域和苏格拉底法区域。

### 2. 四层Wiki结构

papers → concepts → connections → questions

- **papers/**: 一篇论文一个页面，记录核心贡献、方法、结果、局限
- **concepts/**: 一个概念一个页面，聚合多篇论文的同一个idea
- **connections/**: 跨概念的桥梁，记录"A和B之间的关系"——这是idea产生的地方
- **questions/**: 开放问题，未来研究方向的种子

这是一个循环：papers喂进来 → 长出concepts → concepts之间碰撞出connections → 还想不清楚的变成questions → questions驱动你去找新的papers喂进来

### 3. 论文阅读四级分级

**L0 知道它存在**（5-15min）：知道论文大概做什么，是否和自己的问题相关
**L1 能定位它**（30-60min）：知道解决什么问题、方法大概是什么、和我的研究问题有什么关系——**大多数论文到这里就够了**
**L2 能使用它**（2-4h）：能放进wiki，解释核心claim、主要evidence、和其他论文的关系
**L3 能复述/推导/实现核心机制**（半天到几天）：不看原文讲清主线，解释关键公式，走一遍toy example
**L4 能扩展它**（几天到一周+）：修改方法、推广理论、设计新实验

### 4. 读论文三阶段流程

1. **Global orientation**（5min）：先告诉AI"当前概念在整篇论文里的位置"
2. **Local drilling**（20-40min）：用苏格拉底法追问一个核心概念或公式
3. **Global reintegration**（5-10min）：把刚学的东西重新接回paper/wiki

每次读论文前，让AI生成一个Reading Mission：
```
Paper: xxx
Role: survey / ingredient / nearest prior work
Target level: L0/L1/L2/L3/L4
Why I am reading this: 它和我的哪个研究问题有关？
Must understand: 最多5个点
Can ignore: 第一次阅读可以跳过的部分
Stopping criterion: 达到什么程度就停止
```

> 作者：Erber
> 来源：游戏开发技术教程（公众号）
