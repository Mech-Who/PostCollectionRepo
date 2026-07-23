---
title: 有了这个skills，再也不愁画架构图了——内置12种视觉风格
date: 2026-07-22
category: 工具推荐
depth: 标准
layer: layer2
tags: [架构图, Agent Skill, Codex, Claude Code, SVG, UML, C4, Loop Engineering, 可视化]
summary: fireworks-tech-graph是一份供Codex和Claude Code共用的Agent Skill，将自然语言描述转化为经过几何校验的SVG/PNG/GIF/交互HTML。内置11种生成器风格+1种AI手绘风格，含C4评审、云部署、事件流、可靠性排查四种工程风格，支持14种UML图类型。核心差异化是"生成→校验→视觉回读→定向修正"的Loop Engineering闭环。
source_url: https://mp.weixin.qq.com/s/a-IGLuyZWxiqT6z3A7VC8A
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** fireworks-tech-graph是一个为AI Coding Agent设计的架构图生成Skill，核心创新在于"生成后再验证"的闭环：自然语言→图表契约→语义IR→SVG构建→结构校验→PNG视觉回读→定向修正→验证后输出。内置12种视觉风格（含C4评审画布、Cloud Fabric、Event Transit、Ops Pulse四种工程风格），支持14种UML图类型和AI/Agent Pattern。解决了"AI画图好看但几何不对"的痛点。

## 我的理解

> 由小林生成，供小涵审阅修改

这篇文章介绍的fireworks-tech-graph不仅是一个工具，更是"AI生成内容的质量控制方法论"的典型案例。

1. **Loop Engineering在图像生成中的落地**：项目的核心流程——生成→校验→视觉回读→定向修正——与Benoit在另一篇文章中讲的"软件工程不是写代码"完全一致。AI生成的东西即使看起来对，也需要验证环节来确认。

2. **"验证比生成更重要"的设计哲学**：校验器检查XML结构、箭头marker引用、路径几何、节点碰撞、连线重叠等确定性规则；PNG渲染后视觉回读检查文字裁切、标签碰撞、留白。先用规则判断，规则看不见的交给视觉模型。

3. **聚焦修正防止无限循环**：默认最多两轮聚焦修正，每次只调整已诊断的问题，然后重新校验。这防止了Agent陷入"没有终点的自我修改"。

4. **C4评审画布的工程价值**：每个容器带职责与技术栈，连线说明动作和协议——图可以直接进入架构评审，而不是只能充当配图。Ops Pulse围绕固定观察窗口、Golden Signals、关键请求路径和关联Trace展开。

对于小涵正在做的工作（架构图、系统设计文档、概念体系可视化），这个Skill有直接的实用价值。

## 原文

让AI画一张架构图，画的很快，但当你放大一看：连线从节点中间穿过去，两个标签挤在一起。你让它"再优化一下"，第二版可能只是换了个地方出错。

fireworks-tech-graph是由Codex和Claude Code共用的Agent Skill。它将自然语言描述转化为经过几何校验的SVG、高分辨率PNG、经过媒体探测验证的SVG转GIF语义动效与离线交互HTML。

先看效果：直接说"画一张Mem0的架构图，暗黑风格"→Skill识别为Memory Architecture Diagram，Style 2→生成含泳道、圆柱体、语义箭头的SVG→导出1920px PNG。

核心流程：很多AI绘图工具完成条件是模型认为自己已完成了。fireworks-tech-graph的完成条件更严格：必须有校验器结果和实际渲染证据。

自然语言描述→图表契约→语义IR→风格规范→线路规划→SVG构建→结构校验→PNG视觉回读→定向修正→验证后的SVG+PNG

校验器检查XML结构、箭头marker引用、路径几何、节点与保留区域的碰撞，以及连线是否共用不该重叠的轨道。版本化Diagram IR在渲染前拦截重复ID、悬空引用、非法waypoint和非有限坐标。

然后真正渲染PNG，回读图片检查文字裁切、标签碰撞、留白、层级和走线。发现问题后只调整已诊断问题，重新校验。默认最多两轮聚焦修正。最终输出明确：validation: passed, visual_review: passed。

12种视觉风格

前八种：扁平图标、暗黑终端、工程蓝图、Notion极简、玻璃态、Claude风格、OpenAI风格、暗黑奢华。

四种工程风格：
- C4评审画布：只呈现一个抽象层级，节点含职责、技术栈和评审状态，关系线上写清动作与协议
- Cloud Fabric：强调Region、VPC、部署归属、全局入口和跨区域机制
- Event Transit：把Topic、处理节点、Consumer Group、DLQ和状态投影组织成事件轨道
- Ops Pulse：围绕固定观察窗口、Golden Signals、关键请求路径和关联Trace

支持类图、组件图、部署图、活动图、状态机图、序列图、时序图、ER图等14种UML类型。内置RAG、Agentic Search、Mem0、Multi-Agent和Tool Call等AI/Agent Pattern。

快速开始：npx -y skills@1.5.17 add ... --agent codex claude-code

GitHub: https://github.com/yizhiyanhua-ai/fireworks-tech-graph

## 相关笔记
- Loop Engineering——生成→验证→修正闭环在此处落地到图像生成领域
- 软件工程不是写代码（2026-07-22）——验证比生成更重要
