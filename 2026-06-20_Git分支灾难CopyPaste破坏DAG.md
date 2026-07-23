---
title: 一次 Copy-Paste 引发的 Git 分支灾难——从 DAG 视角理解为什么 Copy-Paste 是毒药
date: 2026-06-20
category: 认知提升
depth: 标准
layer: layer2
tags: [Git, 分支管理, 合并冲突, DAG, 版本控制, 工程实践, 协作规范, 踩坑]
summary: 完整复盘一次 copy-paste 跨分支同步代码导致的连锁灾难：丢失 Git 祖先关系 → 四个分支口径不一致 → 所有人合 test 都冲突。核心洞察：Git 是有向无环图（DAG），copy-paste 只搬运节点内容不搬运边——图断了，后续所有基于图的算法（合并、回溯、回滚）都会出问题。附五条 Git 分支协作铁律：feature 不往回拉 test、永远不用 copy-paste 同步、同一功能只一个分支、合入前确保口径一致、频繁小粒度合并。
source_url: https://mp.weixin.qq.com/s/0L9hXFGu5HfqXUycTl830w
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 一个看似无害的 copy-paste 操作——把 `export_feature` 分支的代码复制到新分支 `export`——导致丢失 Git 祖先关系、四个分支口径不一致、所有人合并 test 全部冲突。本文从 DAG（有向无环图）视角拆解了为什么 copy-paste 是毒药：Git 的每次 merge 都在 DAG 上加边记录"曾合并过"，而 copy-paste 只搬运文件内容不搬运图结构——图断了。附带五条 Git 分支协作铁律和自动合并/必须手动解冲突的条件判断规则。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章的独特价值在于：它从一个"我也可能犯"的日常错误出发，一路追溯到 Git 的底层数据结构（DAG），完成了一次从症状到根因的完整诊断。

对你非常实用的两条：

**1. 用"正规结婚 vs 私奔"比喻记住 merge vs copy-paste 的区别。** merge = 正规结婚，民政局有记录（DAG 上有 merge commit 记录两个分支曾合并过），以后办事能查到（Git 能找到 merge base 跳过已合并内容）。copy-paste = 私奔，虽然住一起了，但系统里查不到记录，分财产时乱套（下次 merge 时 Git 找不到 merge base，尝试把已合并的内容再合并一遍→冲突）。

**2. 五条铁律可以直接写进团队规范。** 每一条都是从事故中提炼出来的、有根因解释的规则——不只是"不要这样做"，而是"为什么不要这样做+怎么做才对"。特别是第 1 条（feature 不从 test 往回拉）和第 2 条（永远不用 copy-paste 同步代码，用 merge 或 cherry-pick），是这种事故的一级预防。你的 Unity 项目如果有多人协作或者你自己多个分支并行开发，这几条可以直接用。

另一层启示：**很多看似"技术"的问题，根在认知模型。** 这次事故的根因不是"操作失误"，而是对 Git 的理解停留在"文件同步工具"层面，没有意识到它是一个 DAG 版本管理系统。当你把 Git 当 Dropbox 用时，copy-paste 看起来很合理；当你理解 DAG 后，就知道它在切断图的连通性。这个"认知模型决定操作正确性"的原则，同样适用于 Unity 的 Prefab/Scene 体系、思源的文档引用关系、甚至 Harness Engineering 中的规则设计——操作层面的谨慎永远弥补不了认知层面的缺口。

## 📌 关键要点

- **根因**：copy-paste 跨分支同步代码 → 丢失 Git 祖先关系（DAG 中的边断了）→ 后续所有基于图的操作（merge、回溯、回滚）出问题
- **Git 合并机制**：三方合并依赖 merge base（最近公共祖先）。merge 创建 merge commit 记录祖先关系 → 未来合并能跳过已合并内容。copy-paste 生成的新 commit 只有一个 parent → 图里没有"曾合并过"的记录 → 下次 merge 找不到 merge base → 重新合并一遍 → 冲突
- **自动合并 vs 手动冲突**：两分支改不同行 → 自动合并（行级别粒度）。改同一行 → 冲突。copy-paste 导致的冲突无法避免因为同一个文件的同一个方法同一块代码在两个分支上写法不同且无共同祖先
- **五条铁律**：
  1. feature 分支只放自己的代码，只往 test 合，不从 test 往回合
  2. 永远不 copy-paste 同步代码，用 `git merge` 或 `cherry-pick`
  3. 同一功能只在一个分支上迭代；多分支则 merge 旧分支
  4. 合入上游前确保所有下游分支口径一致
  5. 频繁小粒度合并，不攒大 PR

## 原文

> 以下原文转自微信公众号「一只蜘猪」，作者一只蜘猪，2026-06-20。

---

### 事件还原

**背景**：上线流程 feature → test → pre → master（流水线自动推）。在 `export_feature` 分支开发导出功能，迭代了 9 次提交，同时做了重构（6 个业务方法内联→封装）。

**Step 1（❌ 错）**：`git merge test` 把 test 合入 export_feature。test 是公共集成分支，上面有所有人的代码——别人的提交通过我的 feature 二次进入。如果要回滚我的功能，别人的代码也一起被回滚。

**铁律：feature 只放自己的代码，只往 test 合，不从 test 往回合。**

**Step 2（❌ 错）**：从 master 签出 `export`，copy-paste export_feature 的代码过来。

- merge = 正规结婚：DAG 上有 merge commit 记录两个分支曾合并过，以后 Git 能找到 merge base 跳过已合并内容
- copy-paste = 私奔：虽然住一起了，但系统里查不到记录，分财产时乱套

**Step 3（❌ 错）**：复制不完整——只拷了方法定义（3 个封装方法），6 处调用没改，还是旧的内联写法。结果：3 个死方法 + 6 处内联展开。

**Step 4**：export 合入 master/pre → 内联写法 + 死方法。test 上是封装调用风格。不同分支对同一方法写法不同 → 冲突种子已埋下。

**Step 5**：mentor 基于 master 开发后合 test → 同一行代码 master 上是内联展开（几十行），test 上是封装调用（一行）→ 6 个方法全冲突。

### Git 三方合并原理

```
merge base:  port: 8080    （第5行）
分支 A:      port: 9090    （改了第5行）
分支 B:      port: 3000    （也改了第5行）
→ 冲突！Git 不知道该保留 9090 还是 3000

改不同行 → 自动合并。改同一行 → 冲突。
```
粒度是**行级别**，不是文件级别。

我们的冲突不可避免因为：同一文件、同一方法、同一块代码、两种写法、无共同祖先。

### 每条正确做法

| 出错操作 | 正确做法 |
|---------|---------|
| `git merge test` 到 feature | `git rebase test` 或 `git merge master`（只同步已上线代码） |
| 从 master 签新分支 + copy-paste | 从 master 签新分支 + `git merge export_feature` |
| 两套代码同时存在 | 一个功能一个分支，合并口径统一后再合入 |
| 没统一口径就合入 master/pre | 先确保所有分支写法一致，再逐级合入 |

### 五条 Git 分支协作铁律

1. **feature 分支只放自己的代码，只往 test 合，不从 test 往回合**
2. **永远不要 copy-paste 同步代码，用 git merge 或 cherry-pick**
3. **同一功能的代码只在一个分支上迭代；多分支则 merge 旧分支**
4. **合入上游前确保所有下游分支口径一致**
5. **频繁小粒度合并，不攒大 PR**

## 相关笔记

- 关联概念：`ai-编程实践` — "认知模型决定操作正确性"——理解 Git 的 DAG 本质比记住命令更重要
- 关联概念：`cognitive-结构决定行为` — DAG 结构决定合并行为，copy-paste 破坏结构导致行为出错
- 可迁移原则：任何有"引用关系"的系统（Unity Prefab/Scene、思源文档引用、代码依赖），复制粘贴都可能破坏结构完整性——优先用系统提供的引用/合并机制
