---
title: Deskreen——WebRTC黑科技让任意浏览器设备秒变电脑第二屏幕
date: 2026-05-29
category: 工具推荐
depth: 标准
tags: [Deskreen, WebRTC, 屏幕共享, 开源工具, 第二屏幕, Electron, P2P]
summary: Deskreen 是一个开源的 Electron.js 桌面应用，利用 WebRTC 技术通过本地 WiFi/LAN 将任何带浏览器的设备（手机、平板、旧笔记本）转化为电脑的第二屏幕或投屏接收端。完全离网运行、端到端加密、跨平台、无需额外硬件即可实现屏幕共享。
source_url: https://mp.weixin.qq.com/s/TYsxcLTGvICwnhUn9wPxNQ
source: weixin
status: 📥已采集
sync_status: ✅已同步
---

> **摘要：** Deskreen 是开源 WebRTC 屏幕共享工具，通过本地网络将任意带浏览器的设备变成电脑第二屏幕。支持全屏共享、单窗口演示、第二屏幕扩展（配合虚拟显示适配器）、提词器模式。完全离线、端到端加密、跨平台（Win/Mac/Linux）。项目采用 AGPL-3.0 协议，由 Pavlo Buidenkov 开发。

## 我的理解
> 由小林生成，供小涵审阅修改

Deskreen 的核心理念是"让老设备焕发新生"——与其让旧手机/旧笔记本吃灰，不如把它们变成可用的第二屏幕。这在以下几个场景中特别有价值：

1. **远程演示**：不需要 HDMI 线、不需要投屏硬件，打开浏览器就能投屏
2. **多屏办公**：配合虚拟显示适配器，旧平板/旧手机就是扩展显示器
3. **提词器**：翻转屏幕模式 + 客户端作为提词器，适合视频录制
4. **隐私保护**：单窗口共享模式可以只共享特定应用，避免暴露整个桌面

**技术栈亮点**：Electron.js + WebRTC（simple-peer）+ 端到端加密（tweetnacl），纯 P2P 通信无需云服务器，延迟低且隐私安全。这种"本地优先"的架构理念在当下 SaaS 泛滥的时代反而显得珍贵。

**与已有知识的关联**：这个工具的技术路线（WebRTC P2P + 本地优先）与之前整理的 Obscura 无头浏览器有技术共鸣——两者都在利用本地网络通信规避云端依赖。未来如果需要做本地协作工具，WebRTC 是值得深耕的方向。

## 原文

**Deskreen（pavlobu/deskreen）** 是一个由 Pavlo (Paul) Buidenkov 开发的 Electron.js 开源桌面应用（Community Edition，社区版采用 AGPL-3.0 许可）。利用 WebRTC 技术，通过本地 WiFi 或 LAN 网络，将任意带有浏览器的设备（手机、平板、旧笔记本等）瞬间转化为电脑的第二屏幕或投屏接收端。无需互联网、无需额外硬件（基础镜像模式下），即可实现屏幕共享、单应用窗口演示、第二屏幕扩展（配合虚拟显示适配器）以及电提词器等功能。

### 核心功能（Community Edition）

- **Share Screen View（共享整个屏幕）**：将主机电脑的完整桌面实时流式传输到任意浏览器设备
- **Share App View（共享单个应用窗口）**：仅共享特定应用程序窗口，适合演示或隐私保护场景
- **Second Screen（第二屏幕模式）**：配合 Virtual Display Adapter 或软件虚拟显示驱动，将客户端设备作为真正扩展的第二显示器
- **Teleprompter + Flip Screen Mode**：水平翻转屏幕镜像，客户端设备可作为提词器使用
- **WiFi Compatible**：完全离网运行，只需本地网络
- **Multiple Connected Devices**：支持同时连接多个客户端设备
- **Advanced Video Quality Control**：实时调整画面质量，支持自动质量切换
- **端到端加密（E2E）**：保护本地传输安全
- **跨平台**：Windows、macOS、Linux（包括 ARM 如 Raspberry Pi）
- **深色模式 + 多语言支持**（含中文）

### 安装方法

**预编译版本**：访问 https://deskreen.com/downloads-ce/ 下载对应平台版本

**从源码安装**：
```bash
git clone https://github.com/pavlobu/deskreen.git
npm install
cd ./src/client-viewer && npm install && cd ../..
npm run clean && npm run build && npm run start
```

### 技术架构

- **Main Process**：Electron 主进程负责应用生命周期、屏幕捕获、WebRTC Peer 连接管理
- **Renderer + Preload**：React + Blueprint.js 构建 UI，preload 确保安全上下文隔离
- **Client-Viewer**：独立浏览器端查看器，接收 WebRTC 媒体流并渲染
- **信令机制**：结合 darkwire.io 等 WebRTC 信令协议
- **核心库**：simple-peer（WebRTC P2P 连接）、tweetnacl（端到端加密）
- **构建系统**：electron-vite + electron-builder + TypeScript
