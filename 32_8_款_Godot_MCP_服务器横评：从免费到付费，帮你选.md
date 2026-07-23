---
title: 8 款 Godot MCP 服务器横评：从免费到付费，帮你选到最合适的方案
date: 2026-05-16
tags: [Godot, MCP, 游戏引擎, AI编程, 工具评测, 游戏开发]
summary: 2026年5月市场上有8款Godot MCP服务器，分两条技术路线：Headless CLI（零安装）和EditorPlugin+WebSocket（实时编辑器操控）。godot-mcp-enhanced是免费Headless CLI方案的最强者，Godot MCP Pro是付费全家桶首选。
category: 游戏开发
status: 📥已采集
---

> **摘要：** 本文横评了2026年5月市场上的8款Godot MCP服务器，梳理出两条技术路线——Headless CLI（零安装，通过命令行操控）和EditorPlugin+WebSocket（需安装插件，支持实时编辑器交互）。其中godot-mcp-enhanced以59个工具和84%通过率成为免费Headless CLI赛道最强，而MCP Pro（$16/月）则是功能最全的付费"全家桶"方案。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇横评很实用，8 款产品快速分类的方式非常清晰——先看你要的是零安装还是实时编辑器操控，再看你的预算。我个人会更倾向 godot-mcp-enhanced，因为它的 Godot API 内省（4 个文档查询工具）对 AI 来说非常有价值，可以让 AI "查文档"而不是"猜 API"，这在写 GDScript 时能大幅减少幻觉。而且 59 个工具、84% 通过率，在免费方案里确实能打。不过如果你需要可视化编辑器交互（比如拖拽节点、查看运行中的场景），EditorPlugin 路线是绕不开的——这时候 xulek/godotmcp（免费、~70 工具）可能是性价比最高的选择。

## 原文

> 本文横评了8款Godot MCP服务器

MCP（Model Context Protocol）让 AI 助手能直接操控 Godot 项目，读场景、写脚本、运行游戏、截图验证。AI 从「只能给建议」升级为「直接帮你干活」。

2026 年 5 月，Godot MCP 市场已经形成两条技术路线。

**路线 A，Headless CLI**

命令行启动 Godot headless 进程执行操作，零安装零配置，不需要编辑器插件。

**路线 B，EditorPlugin + WebSocket**

在 Godot 编辑器内安装插件，通过 WebSocket 实时通信，能操控运行中的编辑器。

两条路线各有优劣，下面逐一拆解。

**8 款产品速览**

截至 2026 年 5 月，市场上 8 款值得关注的 Godot MCP 实现。

- **Godot MCP Pro** 收费 $16/月 62 工具 | EditorPlugin
  功能最全，实时编辑器操控 + 输入模拟 + 动画系统 + 性能分析。唯一的「全家桶」方案。

- **GDAI MCP** $19 一次性 ~30 工具 | EditorPlugin
  Python 实现，支持实时编辑器操控和输入模拟。便宜但工具数偏少。

- **xulek/godotmcp** 免费 ~70 工具 | EditorPlugin
  免费方案中工具数最多的 EditorPlugin 实现。支持运行时场景树查询和动画系统。

- **tomyud1/godot-mcp** 免费 ~32 工具 | EditorPlugin
  TypeScript 实现，功能中规中矩，输入模拟和实时编辑器操控都有。

- **6NineLives / bradypp / Coding-Solo** 免费 14-20 工具
  入门级方案，基础场景和脚本操作覆盖。bradypp 和 Coding-Solo 走 Headless CLI 路线。

- **godot-mcp-enhanced（本文重点）** 免费开源 59 工具 | Headless CLI
  免费 Headless CLI 赛道最强。59 个工具，84% 通过率。独家 Godot API 内省、Autoload 上下文执行、测试闭环。

**功能逐项对比**

**基础能力**：所有方案都能做项目发现、启动编辑器、运行/停止项目、创建场景、添加节点、保存场景。

**脚本能力**：读/写/编辑 GDScript 脚本，所有 EditorPlugin 方案和 enhanced 都支持。动态执行 GDScript，只有 enhanced、MCP Pro、GDAI、xulek 能做。Autoload 上下文，只有 enhanced 有。

**场景与节点**：解析 .tscn 场景文件，大部分方案都支持。运行时场景树查询，enhanced、MCP Pro、xulek、tomyud1 有。批量添加节点，只有 enhanced 和 MCP Pro 支持。

**领域专项工具**：TileMap 编辑、材质读写、Shader 编辑、物理射线/碰撞、3D 节点、导航寻路、信号管理，只有 enhanced 和 MCP Pro 有。

**enhanced 的核心竞争力**

三个独家能力：
1. **零安装成本**：Headless CLI 路线，只需要一个 Godot 二进制文件，直接 CLI 调用。
2. **Godot API 内省（独家）**：4 个文档查询工具，AI 可以实时查询并生成正确代码。
3. **动态执行 + 测试闭环**：在 headless Godot 进程中执行任意 GDScript，配合 GUT 单元测试集成，形成写代码→运行测试→查看结果→修复→再测试的完整闭环。

**怎么选**

1. 预算充足且要全家桶，选 **Godot MCP Pro**。
2. 想要实时编辑器操控且预算有限，选 **xulek/godotmcp**。
3. 追求零安装 + API 内省 + 测试闭环，选 **godot-mcp-enhanced**。
4. 刚入门只想试试 MCP，选 **bradypp** 或 **Coding-Solo**。
