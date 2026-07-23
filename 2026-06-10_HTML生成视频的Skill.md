---
title: 2 个 GitHub 上最主流的 HTML 生成视频的 Skill
date: 2026-06-10
category: 工具推荐
depth: 标准
layer: layer2
tags: [视频生成, HTML渲染, HyperFrames, 开源工具, AI视频]
summary: 介绍两个开源 HTML 视频生成项目：HeyGen 的 HyperFrames（HTML→视频渲染引擎，原生为 AI Agent 设计）和 Open Design 的 html-video（在 HyperFrames 之上封装模板、链接转视频、多 Agent 后端）
source_url: https://mp.weixin.qq.com/s/gtExwq2M38F98Rt0TWQBjg
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** 介绍两个开源 HTML 视频生成项目：HyperFrames（纯 HTML 渲染引擎，为 AI Agent 设计，内置15个Skill）和 html-video（21套模板、链接转视频、多Agent后端，架构设计为可插拔渲染引擎适配器）

## 我的理解
> 由小林生成，供小涵审阅修改

两个项目的定位差异很有意思：HyperFrames 是底层渲染引擎（确定性渲染，适合自动化），html-video 是上层应用（模板+Agent，更适合内容创作者）。两者形成了完整的技术栈分层。html-video 的"渲染引擎可插拔"设计思路值得学习——业务逻辑与底层实现解耦，换引擎不用重写模板。对国内用户友好的点是支持微信公众号文章链接直接转视频。

## 原文

**01 HyperFrames**
HeyGen 今年 4 月开源的视频渲染框架，现已 2.5 万+ Star。核心思路：一个 HTML 文件就是一个视频。用 HTML data 属性定义元素时间/持续时长/轨道，GSAP 或 CSS 动画控制运动，无头 Chrome 逐帧录制 + FFmpeg 合成 MP4。完全确定性，同一 HTML 永远产出同一视频。

**核心特点：**
- 原生为 AI Agent 设计，内置 15 个 Skill，Agent 可直接说「做一个逛 GitHub 的公众号介绍视频」
- 纯 HTML 路线，不依赖 React/打包工具
- 动画引擎可选 GSAP/CSS Animations/Lottie/Three.js/Anime.js/Web Animations API
- 内置 Catalog 组件库：转场、图表、字幕、社交模板

**02 html-video**
Open Design 团队（Claude Design 开源平替作者）出品，HyperFrames 之上封装。核心功能：
- 21 套精心设计的模板（数据可视化、产品宣传、排版、Logo 等），可商用
- 链接转视频：抓取文章/GitHub 链接，AI 分析结构，拆场景，套模板渲染
- 多 Agent 后端：支持 Open Design、Claude Code、Codex、Hermes
- 本地 Studio 界面，浏览器选模板、编辑、加背景音乐和配音
- 渲染引擎可插拔（默认 HyperFrames，Remotion/Motion Canvas 路线图）

**开源地址：**
- HyperFrames：https://github.com/heygen-com/hyperframes
- html-video：https://github.com/nexu-io/html-video

## 相关笔记
- [[2026-06-10_GordenSuperPPTSkills.md]] — 同样用 AI 生成可编辑内容的 Skill
