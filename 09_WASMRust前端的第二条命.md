---
source_url: https://mp.weixin.qq.com/s/KHksNWoLYx5vPn7n6m0kIQ
title: WASM、Rust，前端的第二条命！
date: 2026-06-11
source: weixin
category: 工具推荐
depth: 🟡标准
layer: Layer1
tags: [WASM, Rust, 前端开发, 浏览器沙箱, 跨平台]
---

## 摘要

本文介绍了 WASM（WebAssembly）与 Rust 在前端开发中的价值与应用前景。核心论点：WASM 为前端开辟了"第二条生命线"——它解决了 JavaScript 在性能密集型任务上的短板（无法运行 C/C++ 库、小数计算弱），让浏览器可以直接运行二进制程序。作者列举了关键应用场景：运行 30-50MB 的 AI 小模型、零成本迁移桌面软件到浏览器（如 Squoosh.app）、长期可维护性（十年后仍可运行）、浏览器沙箱处理敏感数据。文章还指出 Rust 重构一切工具的趋势，以及 WASM 在跨平台开发中"一次编写，处处运行"的优势。

## 理解

这是一篇带有浓厚**个人色彩和社区文化**的技术推荐文，其特色在于：

1. **技术视角独特**：作者没有过多陷入 WASM 的技术细节，而是从"JS 做不到什么"的反向切入——JS 无法运行 OpenCV、FFmpeg 等成熟原生库、小数计算能力弱——从而引出 WASM 的价值定位。这种"痛点-方案"的叙事结构对前端开发者极具说服力。

2. **杀手级场景清晰**：文章中提到的"在浏览器中运行 AI 小模型"确实是 WASM 当前最具想象力的应用场景。30-50MB 的模型直接编译为 WASM，在用户端浏览器中完成推理，无需服务器、无需上云、零延时，这对隐私敏感应用和降低运营成本都有重要意义。

3. **生态趋势的观察**：从 GNU coreutils 到 Rust 重构的 uutils、从 Webpack 到 Rspack、从 Electron 到 Tauri 的演进图谱，清晰地展示了 Rust 在基础设施层的渗透趋势。对技术选型决策者来说，这张图谱本身就是有价值的参考。

4. **跨平台叙事**：文章中"一次 Rust 代码 → Web(wasm) + CLI + Native 库 + 移动端"的四重输出能力，是 WASM + Rust 组合最核心的技术价值点——这是 JS 在前端领域一直追求但未能实现的"一次编写，处处运行"。

5. **风格与深度之间的取舍**：文章的"吐槽式"行文风格（"资深前端现在都在学炒股和炒粉""前端貌似更没有意义了"）提升了可读性和传播性，但也牺牲了一定的技术深度。未涉及 WASM 的内存管理模型、与 JS 的通信开销、大 WASM 文件的加载策略等关键性能议题。

## 引用/原文

> "JS 是没法运行一些 C C++ 库的，比如 OpenCV 不行，其他语言则大都可以，比如 Python 这种胶水语言，这一下子就失去了很大一块儿生态。"

> "浏览器作为一个就像小程序一样的，随时装随时卸载的平台，如果能直接运行二进制程序的话就太好了，然后 WASM 就能搞定。零成本改造的魅力是很大的。"

> "在 Web 开发领域，前后端里，能做到这一点的新一点儿的语言几乎没有，PHP 都不能。JS 也不能，但是 WASM 可以，哈哈。这一点对于天天焦虑的前端，极度友好！"

> "浏览器沙箱，就能把这些东西，搬到用户端来搞。这点对敏感内容超级重要。"

> "一个 RUST 代码，可以直接搞成 Web 浏览器的 WASM，然后 CLI 工具和 Rust Native 库的移动端。一模一样的程序哦！几乎不用改。"

### 参考资料整理

| 资源 | 链接 |
|------|------|
| Squoosh.app（WASM 图像压缩） | https://squoosh.app/ |
| MDN WebAssembly 概念指南 | https://developer.mozilla.org/en-US/docs/WebAssembly/Guides/Concepts |
| Simon Willison：Hoard things you know how to do | https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/ |
| 掘金译文参考 | https://juejin.cn/post/7617879883323686962 |
