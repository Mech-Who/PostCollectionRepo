---
title: AI铁匠铺Ironsmith：用本地大模型锻造原生SwiftUI Mac应用
date: 2026-06-16
category: 工具推荐
depth: 标准
layer: layer2
tags: ["macOS", "SwiftUI", "本地AI", "Ollama", "开源工具"]
summary: Ironsmith是一个免费开源macOS菜单栏应用，用自然语言描述需求就能调用本地大模型(Ollama/MLX/Foundation Model)生成原生SwiftUI Mac应用，自动编译、签名、沙箱，支持版本回滚和一键导出。
source_url: https://mp.weixin.qq.com/s/2xND_x-lWqv-t_YfnClpgw
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** Ironsmith是一个免费开源macOS菜单栏应用，用自然语言描述需求就能调用本地大模型(Ollama/MLX/Foundation Model)生成原生SwiftUI Mac应用，自动编译、签名、沙箱，支持版本回滚和一键导出。

## 我的理解
> 由小林生成，供小涵审阅修改

这是个真正解决痛点的工具——macOS上『刚好需要一个』但App Store没有的轻量原生小工具。本地优先的设计理念保证隐私安全，沙箱和签名机制也比普通的AI生成代码安全得多。单文件生成策略(只编辑ContentView.swift)极大简化用户后续修改。

## 原文

Ironsmith——免费开源macOS菜单栏应用(GPL-3.0)，用自然语言描述生成原生SwiftUI应用。底层调用本地模型(Ollama/LM Studio/MLX)或云端模型。自动构建SwiftPM包、编译、Apple Intelligence生成图标、代码签名+沙箱+hardened runtime。核心设计：只生成/编辑一个文件ContentView.swift(单文件策略)、多层修复闭环(编译器反馈→确定性修复→LLM diff修复)、版本回滚。示例prompt可做：截图重命名、PDF拆页、剪贴板清理、CSV检查。
