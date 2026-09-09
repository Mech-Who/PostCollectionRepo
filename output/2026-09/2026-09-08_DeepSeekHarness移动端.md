---
title: 我用腾讯 Kuikly，把 DeepSeek Harness 装进了口袋
date: 2026-09-08
category: AI 应用
depth: 深度
layer: layer2:通用
tags: [DeepSeek Harness, Kuikly, 跨平台移动端, WebSocket, 断线重连, 安全隧道]
summary: DSH Mobile 用一套 Kotlin 代码覆盖 Android、iOS 与鸿蒙，把手机定位为 DeepSeek Harness 的远程控制面板。其关键工程点是 Host 协议、多事件流、可恢复重连、连接世代隔离，以及不直接暴露本地服务的 SSH 或密封 Relay 隧道。
source_url: https://mp.weixin.qq.com/s/THtcdws01AV_Q3fe2pYRlQ
source: weixin
status: 📥已采集
sync_status: ❌未同步
---

> **摘要：** DSH Mobile 用一套 Kotlin 代码覆盖 Android、iOS 与鸿蒙，把手机定位为 DeepSeek Harness 的远程控制面板。其关键工程点是 Host 协议、多事件流、可恢复重连、连接世代隔离，以及不直接暴露本地服务的 SSH 或密封 Relay 隧道。

## 我的理解
> 由小林生成，供小涵审阅修改

移动端不必复制完整 Agent 运行时，最合理的边界是“远端执行、手机控制”。这能避免把工具权限、插件环境和长任务状态搬到资源受限设备，同时让审批、补充信息和进度观察变得随手可用。真正困难的是分布式状态恢复：事件补传、历史回放、快照覆盖与世代号过滤必须一起设计，否则重连后很容易出现旧响应污染新会话。

## 关键要点

- **职责分离**：Agent 循环和工具执行留在电脑或云端，移动端只连接、交互和渲染。
- **跨端抽象**：`commonMain` 定义统一 Module，三端分别实现 WebSocket、扫码和 SSH。
- **重连协议**：重建隧道后按序号补事件、请求历史、覆盖任务快照，并丢弃旧连接的迟到响应。
- **安全边界**：本地端口仅监听 `127.0.0.1`，通过 SSH 或不接触本地服务内容的密封 Relay 连接。
- **产品边界**：适合审批和监控，不替代桌面上的长提示词输入与代码 Diff 审查。

## 原文

# 我用腾讯 Kuikly，把 DeepSeek Harness 装进了口袋

DSH Mobile 用 Kuikly 制作，一套 Kotlin 代码覆盖 Android、iOS 和鸿蒙，按官方 Host 协议连接电脑上的 DeepSeek Harness。Agent 循环、工具执行和插件仍在电脑或云端，手机负责连接、交互和渲染，适合处理审批、补充信息和查看进度。

## 技术实现

使用 KuiklyMarkdown 处理流式 Markdown、代码块和列表，KuiklyWebview 打开链接；commonMain 定义统一 Module 接口，三端分别实现 WebSocket、扫码和 SSH。Host 协议通过 HTTP RPC 与 `/api/events.mux`、`/api/events.host` 两条事件流传递会话和全局状态。重连流程是重新建立隧道、按序号补事件、请求历史、覆盖 queue/jobs 快照，并用连接世代丢弃迟到响应。

DSH 默认监听 `127.0.0.1:3080`，移动端不直接暴露公网，提供 SSH 隧道或扫码 Relay。扫码插件使用密封隧道，Relay 不访问 3080。手机定位是远程控制面板而非 IDE；长 Prompt 和代码 Diff 仍适合桌面。项目仍是 developer preview，应锁定已验证版本。

## 相关笔记

- 暂无已确认关联笔记。

## Skill 转化评估

候选。文章给出了跨端模块、事件流、重连与安全隧道的完整设计骨架，可转化为“远程 Agent 控制面板架构”Skill；本次仅记录候选，不创建 Skill。
