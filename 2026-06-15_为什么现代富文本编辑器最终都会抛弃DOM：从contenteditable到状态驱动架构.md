---
title: 为什么现代富文本编辑器最终都会抛弃DOM：从contenteditable到状态驱动架构
date: 2026-06-15
category: AI应用
depth: 深度
layer: layer2
tags: [前端, 编辑器, DOM, 架构设计, AST, 富文本]
summary: 深入分析现代富文本编辑器从DOM驱动到状态驱动的架构演进：DOM只理解HTML结构不理解文档语义（如Mention节点），导致光标丢失、Undo失效、输入法异常。现代编辑器建立自己的AST世界模型——EditorState=Document，DOM=RenderTarget，形成类React的State→Diff→Reconcile→Commit流程。AI编辑器时代这种架构更加必要。
source_url: https://mp.weixin.qq.com/s/N-dA6gkjDovSWJIFygkJsA
source: weixin
author: 渡一前端每日精选
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** 深入分析现代富文本编辑器从DOM驱动到状态驱动的架构演进：DOM只理解HTML结构不理解文档语义（如Mention节点），导致光标丢失、Undo失效、输入法异常。现代编辑器建立自己的AST世界模型——EditorState=Document，DOM=RenderTarget，形成类React的State→Diff→Reconcile→Commit流程。AI编辑器时代这种架构更加必要。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章的价值在于用一个清晰的叙事线串起了编辑器架构演变的内在逻辑。核心洞察：DOM不理解文档——它看到的永远是div/span/textNode，而编辑器需要看到mention/paragraph/codeblock等语义节点。这个从DOM即真相到状态即真相的范式转换，和React从jQuery进化过来的逻辑完全同构。对做AI编辑器或任何需要富文本处理的产品来说，这是必读的基础认知。

## 📌 关键要点
- DOM无法表达稳定语义：Ctrl+B可能生成3种不同HTML结构，视觉效果相同但数据结构不同
- Mention经典问题：编辑器关心{type:mention, id:user1}，浏览器只看到<span>@User1</span>
- Undo必须自己实现：浏览器Undo是字符级别的，业务需要的是操作级别（整个AI改写一次性撤销）
- 输入法兼容：维护isComposing开关，拼音组合阶段不更新AST
- 架构本质 = React模式：State → Diff → Reconcile → Commit DOM

## 原文

现代富文本编辑器最终演变成：状态机+事务系统+渲染引擎+协同系统+输入法兼容层。

## DOM不是文档
传统方式`contenteditable`+`document.execCommand`的根本问题：DOM既是展示结果也是数据源，但DOM不理解"文档"——只理解div/span/textNode/strong，不理解mention、加粗语义等。

经典问题：Mention `@User1` 在DOM里是`<span data-id="user1">@User1</span>`，浏览器看到的是span，编辑器关心的却是`{type:"mention", content:"@User1", data:{id:"user1"}}`。用户按Backspace时浏览器逐字符删除，但业务需要整个mention一起删。

另一个问题：`Ctrl+B`可能生成`<strong>`、`<span style="font-weight:bold">`或`<b>`，视觉效果一样但DOM结构不同。

## 现代编辑器架构
- **EditorState = Document**，DOM只是Render Target
- 输入过程：浏览器修改DOM → 编辑器解析DOM → 转换成AST文档状态
- Undo：撤销的不是DOM而是文档状态 `undoStack.push(structuredClone(state.ast))`

## 编辑器 ≈ React
```
State → Diff → Reconcile → Commit DOM
```
和React一样：EditorState → Node Tree → Reconcile → Update DOM。现代编辑器本质是状态驱动UI系统。

## AI时代更重要
AI操作的不是字符而是文档结构。AI Rewrite/Insert/Generate Block都是文档节点级别的操作。

## 自主管理的关键点
- 输入法：维护`isComposing`开关，拼音组合阶段不更新AST
- Selection不再只是浏览器能力
- Undo不再交给浏览器

## 总结
DOM不再是真相 → HTML不再是文档 → 编辑器建立自己的"文档世界" → 变成独立文档runtime。

## 相关笔记
- （待关联）
