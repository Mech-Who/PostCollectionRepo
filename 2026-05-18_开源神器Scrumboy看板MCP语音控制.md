---
title: 爆款开源神器 Scrumboy ：自托管看板 + MCP AI 代理 + 语音控制 + 粘性笔记墙，一文搞懂安装、使用、架构与高级玩法！
date: 2026-05-18
tags: [Scrumboy, 开源, 看板工具, MCP, 项目管理]
summary: Scrumboy 是一款自托管看板工具，支持匿名看板、实时协作（SSE）、语音命令、MCP AI 代理集成、粘性笔记墙、自定义工作流和 Sprint 管理。后端纯 Go + SQLite，单文件部署零依赖。
category: 工具推荐
source_url: https://mp.weixin.qq.com/s/IXfgP9zbPIjYYPw-ILznoA
source: weixin
status: 📥已采集
depth: 标准
---

> **摘要：** Scrumboy 是一款"极简+强大"的自托管看板工具：支持匿名可分享看板、SSE 实时协作、语音控制（VoiceFlow）、自定义工作流和 Sprint、粘性笔记墙、以及 MCP（Model Context Protocol）AI 代理集成。后端纯 Go + SQLite，单文件部署，强调数据隐私和零仪式感体验。提供 Docker 和源码两种安装方式。

## 我的理解
> 由小林生成，供小涵审阅修改

Scrumboy 的核心定位是"比 Notion/Trello 更轻，比 Jira 更灵活，比其他开源替代品更现代"。最吸引人的三点：一是 MCP 支持让 AI 代理可以直接与看板交互（Claude Desktop、Cursor 等），这在当前 AI 编程趋势下很有前瞻性；二是匿名看板模式降低协作摩擦，无需注册即可创建和分享；三是纯 Go + SQLite 的单文件部署对自托管的运维负担极低。粘性笔记墙 + Sprint 管理的组合也适合小团队敏捷开发。

## 原文
（原始推文内容）

被定位为"Self-hosted kanban & project management with shareable boards, voice commands, sticky-notes and MCP support"的开源项目——**markrai/scrumboy**，官网更是直截了当"Boards without the ceremony"!!!

不同于市面上那些花里胡哨的 SaaS 看板工具，Scrumboy 强调**极致简洁 + 极致强大**：零仪式感匿名看板、实时协作、语音命令、粘性笔记墙、MCP（Model Context Protocol）AI 集成、审计轨迹、自定义工作流、PWA 推送……全部自托管，数据永不离开你的服务器。

### 一、Scrumboy 核心功能

Scrumboy 支持两种运行模式（通过 `SCRUMBOY_MODE` 环境变量切换）：

- **Full 模式**（默认）：支持完整认证、2FA、项目成员、备份导出、多项目、Webhooks、MCP 完整能力。
- **Anonymous 模式**：零认证，适合公开演示或临时团队，首页直接进入匿名看板。

#### 1. 匿名 + 可分享看板

- 任何人访问 `/anon` 或 `/temp` 即可**瞬间创建**一个抛弃式看板，生成唯一 slug 链接。
- 支持实时分享给任何人，无需账号、无需注册。

#### 2. 实时协作（Realtime SSE）

- 所有看板操作通过 **Server-Sent Events (SSE)** 实时推送。
- 多用户同时编辑卡片、拖拽、分配、评论时，其他人**毫秒级**看到更新。

#### 3. 自定义工作流 + Sprints

- 每个项目可**完全自定义**看板列（Lane），并指定**唯一一个 Done 列**。
- 支持 Sprint 创建、激活、关闭、过滤。
- Dashboard 自动计算 WIP、Throughput、Avg. Lead Time、Sprint 完成率等指标。

#### 4. 粘性笔记墙（Sticky-Note Wall / Scrumbaby）

- 每个项目独立的自由画布式便签墙，支持**拖拽、缩放、多选删除、右键菜单**。
- 右键单张便签可直接"Create Todo from Note"。

#### 5. 语音命令（VoiceFlow）

- 浏览器原生语音识别 + 确定性命令系统。
- 支持自然语言控制看板（创建 Todo、移动卡片、切换 Sprint 等）。

#### 6. MCP（JSON-RPC）AI 代理集成（重磅功能）

- 完整支持 **Model Context Protocol**，暴露 `/mcp` + `/mcp/rpc`（JSON-RPC 2.0）。
- AI 代理（Claude Desktop、Cursor 等）可直接调用工具：`projects.list`、`todos.create`、`sprints.activate` 等。

#### 7. 其他

- 本地密码登录 + TOTP 2FA，OIDC/SSO 支持
- PWA + Web Push 通知
- Webhooks（Outbound）
- 备份/导入/导出 + Trello 迁移
- 深色/浅色主题、壁纸、快捷键

### 二、安装方法

#### Docker 部署（推荐）

```bash
git clone https://github.com/markrai/scrumboy.git
cd scrumboy
docker compose up --build -d
```

访问 `http://localhost:8080`。

#### 从源码安装

```bash
git clone https://github.com/markrai/scrumboy.git
cd scrumboy
cd internal/httpapi/web
npm install
npm run build
cd ../..
go run ./cmd/scrumboy
```

### 三、技术架构

- **后端**：纯 Go，使用 `net/http` + SSE
- **数据库**：SQLite + WAL + busy_timeout，单文件部署零依赖
- **前端**：TypeScript + 嵌入式静态资源（go:embed）
- **实时**：SSE（非 WebSocket，更轻量）
- **AI 集成**：MCP 双协议（传统 POST + JSON-RPC 2.0）
- **安全**：加密密钥保护 TOTP/密码重置数据；审计表 append-only

Scrumboy 是真正懂开发者痛点的自托管方案：隐私、简洁、可扩展、AI 原生。比 Notion/Trello 更轻，比 Jira 更灵活，比其他开源替代品更现代。
