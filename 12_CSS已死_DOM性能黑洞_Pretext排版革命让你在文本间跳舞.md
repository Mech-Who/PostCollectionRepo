---
url: https://mp.weixin.qq.com/s/EBccCvj29Zmy-a2hRJPDpw
title: CSS 已死？DOM 性能黑洞！Pretext 排版革命让你在文本间跳舞，没有 DOM 也能纵享丝滑~
date: 2026-05-25
source: weixin
status: ok
category: 工具推荐
depth: 🟡标准
tags: [Pretext, 前端, 排版, CSS, DOM, Canvas, 文本测量, JS库]
author: 林语冰
layer: layer2
sync_si: true
---

## 摘要

Pretext 是前 React 团队大佬、现任 Midjourney AI 大神 Cheng Lou 开发的 JS 库，通过逃离 DOM 依赖、使用现代 API（Intl.Segmenter + Canvas measureText）实现文本测量性能提升 300 倍。两周 GitHub Stars 飙升至 50k，但定位仍是概念验证原型，日常开发中 99.99% 用不上。

---

## 30年的性能噩梦

前端UI中文本测量依赖DOM API，浏览器先渲染文本再调用getBoundingClientRect()测量尺寸，这会导致"强制同步布局"。计算上百个文本就会中断上百次，60fps每帧16.6ms，100次重排就会掉帧。

## Pretext基本原理

Pretext的核心创新在于发明了不需要DOM的快速文本测量算法。分两步：准备阶段用Intl.Segmenter()切割文本、Canvas API measureText()测量并缓存尺寸；布局阶段仅对缓存尺寸做数学计算。能独立于主线程运行，无布局重排。

## 适用场景与局限性

两大使用场景：无需DOM测量段落高度、手动排版渲染到Canvas/WebGL/SVG。局限性：仅支持部分CSS属性（white-space的normal/pre-wrap、word-break的normal/keep-all），需要支持现代API，MacOS需用命名字符体，SSR尚未落地。

## 总结与意义

Pretext是告别30年来"唯DOM是从"路径依赖的尝试，但营销号的"无CSS时代"纯属夸大。Pretext生于AI用于AI——由AI迭代打磨，又让AI产品性能暴涨。定位是概念验证的成功原型，而非生产就绪产品。

---

## 金句

> 1. "CSS 不能，DOM 也不能。但 Pretext 能！"
> 2. "有的营销号大肆厥词，宣称'前端要进入无 CSS 时代'，这跟台独分子的自欺欺人没啥区别。"
> 3. "CSS 是前端领域的三辆马车之一，日常开发中 99.99% 都用不上 Pretext 这种'屠龙技'。"
> 4. "Pretext 生于 AI，用于 AI。"
> 5. "Pretext 催生了一场文本排版革命，对抗 30 年来'唯 DOM 是从'的路径依赖，甚至把性能提升了 300x 倍。"

---

## 我的理解

Pretext 的技术价值不在于"干掉 CSS"，而在于**证明了脱离了 DOM 的纯数学排版是一条可行的性能优化路径**——300x 的性能提升来自彻底放弃 DOM API 的强制同步布局，改用 Canvas 测量 + 数学计算 + 缓存。它"生于 AI，用于 AI"的定位很精准：对 AI 产品（聊天列表、实时流文本、动态 UI）这类需要频繁重排的场景，意义重大；但对 99.99% 的日常前端开发，CSS + DOM 仍是更务实的方案。从这个角度看，Pretext 更像一个"概念验证的原型"，揭示了 DOM 排版模型的性能天花板到底在哪里，并给出了一个突破天花板的可能性。

---

## 原文

**👇 今日要闻**  
打破信息壁垒，走近全球前端。Hello World 大家好，我是林语冰。

你能让萌妹在文本间跳舞，同时不掉帧、不卡屏吗？比如酱紫：

CSS 不能。DOM 也不能。但 Pretext 能！

没有布局抖动，没有虚假摆拍，只有像素艺术纵享丝滑。

这就是 Pretext，上个月崭露头角的一个 JS 库，因为各种花里胡哨的文本艺术一夜爆火。

Pretext 的作者是前任 React 团队大佬、现任 Midjourney AI 大神 Cheng Lou，他抛弃了 DOM 破而后立，以浏览器字体引擎为基准，联手 AI 发明了新型文本测量算法。

Pretext 出道即巅峰，它的 GitHub stars 两天内飙升 10k，一周内又爆炸性增长，翻了两番直逼 50k。

那么这个后起之秀到底是何方神圣，它是怎么做到的，又做对了什么？本期我们就来一探究竟，偷师一下 Pretext 的技术内幕。

**👉 30 年的性能噩梦**  
前端 UI 包括聊天气泡、虚拟滚动列表等组件。

举个栗子，聊天列表为了只渲染可见消息，要求消息气泡进入视口前获取它们的尺寸。

经验法则是借助 DOM API 测量，浏览器先渲染文本，再调用 `el.getBoundingClientRect()` 方法或 `el.offsetHeight` 属性测量段落尺寸：

但这会让浏览器中断施法并重新计算布局，这种硬控正是导致布局抖动的元凶，也就是"强制同步布局"。

想象一下，如果列表需要计算上百个文本，就会中断上百次。60fps 每帧耗时 16.6 毫秒，而 100 次重排就可能导致掉帧。尤其在非发达国家的"小霸王"设备上，这会造成明显的视觉卡顿，难道你要用户眨眼补帧？

**👉 Pretext 基本原理**  
为了逃离 DOM 的性能黑洞，为了迎接 AI 时代 Prompt（提示语）工程的挑战，Pretext 应运而生。

Pretext 的天才之处在于发明了快速且精准的文本测量算法，而且还不需要 DOM，底层原理分为两大阶段：

1. 准备阶段：`prepare()` 函数执行一次性的脏活累活，重整空格，使用 ECMAScript 国际化 API `new Intl.Segmenter()` 切割文本和按需拼接，再用 Canvas API `ctx.measureText()` 测量文本段，缓存尺寸

2. 布局阶段：`layout()` 函数只要对缓存尺寸进行数学计算就欧了

虽然 Pretext 使用的是和 DOM 同款字体引擎，但它甚至能独立于主线程去运行，没有布局重排，尽量不阻塞主线程。

就像 Vue 采用基于 Signals 的细粒度响应式系统，来规避 DOM 代码屎山的技术债务，Pretext 在现代 API 的助力下实现了弯道超车。

就酱，15 年前的 Canvas 技术在一个 15Kb 的 JS 库中"文艺复兴"，Pretext 催生了一场文本排版革命，对抗 30 年来"唯 DOM 是从"的路径依赖，甚至把性能提升了 300x 倍。

**👉 适用场景**  
Pretext 文档提供了两大使用场景：

1. 无需 DOM 即可测量段落高度
2. 手动排版段落，支持渲染到 Canvas / WebGL / SVG

举个栗子，CSS 实现聊天气泡会浪费空间，`width: fit-content` 会将段落的最宽行调整为容器尺寸，如果文本末行太短就会产生突兀的留白。

而 Pretext 能用优雅的数学计算出最佳宽度，渲染出紧凑的段落，规避像素损失。

**👉 Pretext 局限性**  
注意，有的营销号大肆厥词，宣称"前端要进入无 CSS 时代"，这跟台独分子的自欺欺人没啥区别。

CSS 是前端领域的三辆马车之一，日常开发中 99.99% 都用不上 Pretext 这种"屠龙技"，反而天天要和 CSS 斗智斗勇。

相比营销号，Pretext 诚实多了，它在文档中开诚布公，暂不定位为一个完整的字体渲染引擎，目前只支持常见的文本设置：

*   CSS `white-space` 属性只支持 `normal` 和 `pre-wrap`，`word-break` 属性支持 `normal` 和 `keep-all`
*   Canvas `font` 简写之外的 CSS 文本功能没有单独建模，比如 `font-feature-settings` 等
*   运行时要求支持 `ctx.measureText()` 和 `Intl.Segmenter()` 等现代 API
*   MacOS 操作系统上，要求使用命名字体取代 `system-ui`，否则影响 `layout()` 的准确性
*   SSR 的终极目标尚未落地，还在持续迭代开发中

毕竟 Pretext 尚未首发 `v1` 主版本，目前还算不上一个生产就绪的成熟产品，而是一个概念验证的成功原型。

**👇 重点总结**  
Pretext 逃离了 DOM 的路径依赖和性能黑洞，它另辟蹊径：

*   借助现代 API 高速且精准地测量多行文本和布局
*   没有 DOM 接触，没有同步布局重排，没有像素浪费
*   支持混用多语言和双向文本
*   支持渲染到 Canvas / WebGL / SVG

Pretext 生于 AI，用于 AI，一方面它由 AI 疯狂迭代打磨而来，另一方面它让 AI 产品的组件和交互性能暴涨，还能用于 AI 产品开发阶段的有效验证，而不需要浏览器参与，这才是 Pretext 文本排版革命的划时代意义所在。
