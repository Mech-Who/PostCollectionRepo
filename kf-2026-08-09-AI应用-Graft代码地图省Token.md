---
id: kf-2026-08-09-AI应用-Graft代码地图省Token
title: Graft：给 AI Agent 建立代码地图，省 Token 又防漏改
type: fragment
domain: AI应用
layer: layer2
source_type: weixin
source_ref: [[2026-08-09_Graft给代码建立档案让Agent更省Token]]
source_url: https://mp.weixin.qq.com/s/KvePCTm5GUhEQ_LQ4FgdIQ
tags: [Graft, AI编程, 代码地图, Tree-sitter, Token优化, Claude Code, Codex, 上下文工程]
related_fragments: [kf-2026-08-09-AI技术-OpenRSI递归自我进化]
related_concepts: [harness-engineering, context-engineering, 工具推荐与开源, 游戏工程-AI辅助开发工具链]
status: stable
created: 2026-08-09
version: 1
---

# Graft：用确定性代码地图替代 Agent 的盲目搜索

## A - Applicable：什么时候用

- **已有复杂多模块项目**里让 AI 做重构、修跨文件 Bug——地图能沿依赖链找全"改了 A 必须改 B"的文件
- Agent 新会话频繁 grep/打开无关文件烧 Token 时，用 Graft 把探索成本前置到毫秒级静态分析
- 用户说"AI 改代码老漏文件""Agent 太费 Token""给 AI 建代码索引"时命中

## B - Boundary：边界条件

- **能力锁死在已索引的本地代码库内**：涉及库外新技术、外部 SDK、未拉取依赖、未开始的架构方案时完全帮不上忙——它是"本地代码字典与导航图"，不是通用大脑
- **设计取舍**：刻意不用向量嵌入、不用后台数据库（纯 TF-IDF/BM25 词汇重叠）——所以对新概念/新词汇没有语义泛化能力
- **阈值拦截是特性**：匹配分低于阈值直接放弃注入上下文，避免噪声——"注入错误上下文比不注入更糟"
- **不适用**：探索全新业务、讨论代码库里不存在的新东西时，不必期待它提供帮助

## C - Core：核心要点

- **原理**：Tree-sitter 静态语法分析毫秒级解析函数/类/依赖关系 → 生成 `.graft/` 目录 Markdown 本地地图 → Agent 优先读地图跳过盲目试探搜索
- **实测收益**：162 次控制变量测试减少 46% 工具调用、42% Token 消耗；SWE-bench Verified 通过率 65%→75%（多文件联动修改不漏文件）
- **底层实现**（src/ask/ask.ts）：① 纯确定性词汇重叠——基于 Tree-sitter 符号名+注释+提问词汇做 TF-IDF/BM25 词频匹配，无向量嵌入无数据库；② 严格阈值——词汇无重叠则得分归 0，低于阈值放弃注入
- **零维护**：`graft init` 自动构建图谱、写 Hook 到 `.claude/`、`graft/` 自动加 `.gitignore`；改代码后台毫秒级静默更新

## D - Data：关键示例

```text
// 安装与初始化（一行命令开箱即用）
npm install -g @nanonets/graft
graft init          # 项目根目录运行：构建图谱 + 写入.claude/ Hook + gitignore

// 效果数据（官方基准）
工具调用: -46%   Token消耗: -42%   SWE-bench Verified: 65% → 75%

// 适用判断
✅ 已有复杂多模块项目重构/跨文件Bug修复 → 大幅省钱减少漏改
❌ 全新业务/库外新技术/未拉取依赖/未开始的架构 → 帮不上忙
```

**与 OpenRSI 的共性**：长程 Agent 任务中"按需检索有界证据/确定性地图"替代"全量探索/全量历史"，单位 token 价值大幅提升——精准上下文供给比模型原始探索能力更决定效率。
