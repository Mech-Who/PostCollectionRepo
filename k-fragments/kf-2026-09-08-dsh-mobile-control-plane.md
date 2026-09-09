---
id: kf-2026-09-08-dsh-mobile-control-plane
title: 移动端 Agent 远程控制面板架构
date: 2026-09-08
category: AI 应用
layer: layer2:通用
tags: [移动端, Agent, 断线重连, 事件流, 安全隧道]
source_url: https://mp.weixin.qq.com/s/THtcdws01AV_Q3fe2pYRlQ
---

## A · Applicable

适用于为桌面或云端 Agent 增加移动端审批、补充信息、进度查看和任务控制能力。

## B · Boundary

移动端不应承担完整 IDE 或 Agent 执行环境；本地服务不可直接暴露公网。developer preview 依赖应锁定已验证版本。

## C · Core

- 将执行面留在主机，将移动端限定为控制面和渲染层。
- 跨端公共层只定义接口，各平台实现网络、扫码和 SSH 能力。
- 重连同时处理事件补传、历史回放、快照覆盖和旧世代响应丢弃。
- 通过 SSH 或密封 Relay 保护仅监听回环地址的服务。
- 明确手机适合审批与监控，不适合长 Prompt 和大型 Diff。

## D · Data

```text
RPC: HTTP
Event streams: /api/events.mux, /api/events.host
Local endpoint: 127.0.0.1:3080
Reconnect: tunnel -> replay by sequence -> history -> queue/jobs snapshot -> discard stale generation
```
