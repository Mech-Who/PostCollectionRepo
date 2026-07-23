---
title: CodeWhale v0.8.66：终端里的全能AI编码「鲸」——多模型统一路由 + MCP + Fleet子代理
date: 2026-07-04
category: 工具推荐
depth: 标准
layer: layer2
tags: [CodeWhale, AI编码Agent, 终端工具, 多模型路由, MCP, 开源工具, Rust]
summary: 详细介绍 CodeWhale —— 一个专注终端工作流的开源AI编码Agent框架。核心亮点：多 Provider 统一路由系统（RouteResolver）、MCP 扩展机制、Plan/Agent/YOLO 三级安全模式、Fleet 多角色协作、Skills 可复用工作流。与 Cursor/Windsurf 等 IDE 插件的本质区别是零 IDE 依赖，无缝嵌入 tmux/vim/zsh 生态。
source_url: https://mp.weixin.qq.com/s/qUquhCF9sG_K7sdjnsZBTw
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** CodeWhale 是一个专注于终端工作流的开源（MIT）AI编码Agent框架，前身 deepseek-tui。核心亮点：多 Provider 统一路由系统（RouteResolver）、MCP 扩展机制、Plan/Agent/YOLO 三级安全模式、Fleet 多角色协作、Skills 可复用工作流。与 Cursor/Windsurf 等 IDE Agent 的本质区别是零 IDE 依赖，嵌入 tmux/vim/zsh 生态，本地优先 + 开源模型第一。

## 我的理解

CodeWhale 是目前终端生态里最成熟的开源编码 Agent 之一，它的架构设计有很多值得参考的地方。最让我眼前一亮的是 RouteResolver 统一路由系统——它不是简单地把多个 API 拼在一起，而是为每个请求"铸造"一条包含 endpoint、wire protocol、真实 context limit 和价格状态的 resolved route，保证一致性和诚实性（不虚构价格）。MCP 支持也很完整（stdio + HTTP，OAuth，LLM 可动态启动 server）。安全模型的三级 Plan→Agent→YOLO 也很有借鉴意义。对于日常使用，CodeWhale 的价值在于：你可以一个工具统一管理 DeepSeek/Claude/GPT/Kimi/GLM 等多个模型，在终端里完成代码阅读、编辑、执行、任务规划全流程。对于 WorkBuddy 用户来说，它的 Skills + Fleet 体系（可复用 workflow + 多角色协作）和工作流理念值得关注。

关联已有概念：工具推荐与开源、AI-Native 开发工具

## 原文

### 一、项目简介

CodeWhale 前身是 deepseek-tui，最初围绕 DeepSeek 工作流构建的编码 harness。中国开发者社区大量采用、反馈与贡献后，开发者意识到 harness 价值远超单一模型，于是演进为多 Provider 通用终端 Agent 框架，并更名为 CodeWhale。

与 Cursor / Windsurf 等 IDE Agent 的本质区别：CodeWhale 专注终端工作流，零 IDE 依赖，完美嵌入现有 tmux/vim/zsh 生态；强调本地优先 + 开源模型第一 + 显式路由 + 沙箱权限；支持 headless CI/脚本场景。

### 二、核心功能

1. **TUI + CLI 双模式界面**：TUI（ratatui 构建）支持 composer 输入、自定义 statusline、多个 dashboard（provider/model/fleet/skills/mcp/config）。CLI 支持 `codewhale exec` 用于脚本和 CI。

2. **多 Provider 统一路由系统（RouteResolver）**：只需选 `--provider` + model，RouteResolver 负责铸造真实 resolved route，携带具体 endpoint、wire protocol、真实 context limit（用于 compaction，非硬编码）、价格状态。支持 DeepSeek、OpenAI、Anthropic、Kimi、GLM、Minimax、Ollama、vLLM、SGLang 等数十个 Provider。

3. **真正的 Agentic 能力**：核心循环为规划→工具调用→执行→观察结果→自纠错→继续。内置工具包括文件操作（read/write/apply_patch 自动 LSP）、Shell（经 execpolicy 沙箱批准）、任务管理（todo/tasks）、GitHub 只读、规划/子代理、RLM Python REPL 等。

4. **安全模型**：Mode 三级——Plan（默认只读）→ Agent（逐操作批准）→ YOLO（自动批准）。execpolicy 批准策略引擎 + permissions.toml 细粒度规则 + 沙箱路径隔离 + audit.log 审计。

5. **MCP（Model Context Protocol）**：CodeWhale 最具特色的可扩展性支柱。支持本地 stdio 和远程 HTTP MCP 服务器，OAuth 支持，LLM 可从 chat context 启动 MCP servers。

6. **Skills + Fleet + Sub-Agents**：Skills 为可复用 workflow（每个含 SKILL.md）；Fleet 为多角色协作，支持 per-sub-agent 显式 provider 分配（不同子代理可用不同模型/路由）；会话持久支持 `/restore` 回滚。

### 三、安装

```
npm install -g codewhale        # Node 18+
codewhale auth set --provider deepseek
codewhale doctor                 # 验证配置
codewhale                        # 进入 TUI
```

### 四、高效使用建议

- 日常流程：Plan 模式探索 → Agent 模式执行 → `/restore` 安全回滚 → Skills 固化常用模式 → Fleet 多角色协作 → MCP 扩展领域工具
- 成本控制：关注 `/provider` dashboard 的 honest cost meter
- Headless CI：`codewhale exec --allowed-tools read_file,exec_shell --max-turns 15 "fix failing tests"`
- 最佳实践：优先本地模型或高性价比 GLM/DeepSeek；YOLO 仅在完全可信沙箱使用

### 五、技术架构

- UI 层：TUI（ratatui）+ CLI/Headless + Config/Auth
- Core Engine：Agent Loop + Session/Turn 管理 + Tool Orchestration + route-aware context budget
- Tool & Extension：Built-in Tools + Skills + Hooks + MCP Servers
- LLM Layer：LLM Client → RouteResolver + ModelRegistry → Provider Catalog

## 相关笔记
- 工具推荐与开源（CodeWhale 作为终端 AI 编码工具加入工具图谱）
- AI-Native 开发工具（与 Cursor/Windsurf/Claude Code 的对比维度）
