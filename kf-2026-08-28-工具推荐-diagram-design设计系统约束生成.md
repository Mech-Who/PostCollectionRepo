---
id: kf-2026-08-28-工具推荐-diagram-design设计系统约束生成
title: diagram-design — 用设计系统约束 AI 图表生成
type: fragment
domain: 工具推荐
layer: layer2
source_type: blog
source_ref: [[2026-08-28_画图不再手搓diagram-design一键生成39种图表]]
source_url: https://mp.weixin.qq.com/s/JJKkzrrf9Rmr62YMkchykQ
tags: [diagram-design, 图表生成, 设计token, 品牌风格, Mermaid, Draw.io, Agent Skill, WCAG]
related_fragments: [kf-2026-08-26-AI应用-读懂Pi的agentloop源码]
related_concepts: [agent-skill工程化, harness-engineering, context-engineering]
status: stable
created: 2026-08-29
version: 1
---

# diagram-design — 用设计系统约束 AI 图表生成

## A — Applicable：什么时候用

- 写技术文档/产品方案需要配图（架构图、流程图、时序图、ER 图、甘特图等）且要求风格统一、可直接放进正式文档时
- 已有 Draw.io / Mermaid 存量图，想统一换皮升级为"编辑级质感"而不重画内容时
- 团队/产品有多张图要出，需要一次性绑定品牌配色字体、后续全自动保持一致时
- 给不同受众出同一张图的不同版本（工程师版 vs 高管版、文档内嵌 vs 16:9 幻灯）时

## B — Boundary：边界条件

- **适用前提**：结构化图表（节点/连线/层次类）；要求数据可视化精细分析（复杂交互图表）时不是首选
- **不适用的场景**：艺术插画/写实图像生成——这是图表 Skill，不是画图模型；需要像素级品牌验收的对外物料仍需设计师终审
- **注意事项**：
  - 需要四大 harness 之一（Claude Code / Codex / Factory Droid / Pi）才能安装使用；WorkBuddy 等其他客户端可借鉴其思路（SVG + 语义 token）而非直接安装
  - Google Fonts 是唯一网络依赖，离线环境字体会回退
  - 品牌风格抓取基于目标网站首页，网站本身配色混乱时映射质量有限

## C — Core：核心要点

1. **痛点定性**：AI 画图的问题是"画不稳"（颜色随机/间距失控/风格脱节）而非"画不出"；解法是设计系统约束生成，不是换更强的模型
2. **语义 token 是稳定性的来源**：把颜色/字体抽象成语义角色（背景/线条/强调），一次配置全局生效——"图表世界的 CSS"
3. **品牌接入一句话**：抓取网站主色/字体 → 语义角色映射 → 预览确认 → 写入配置；附带 WCAG 对比度检查，小字对比不足主动提示
4. **内容与样式分离**：同一份 Mermaid/Draw.io 源，按四维换皮——格式（HTML/SVG/PNG）、尺寸、细节密度（保真/平衡/简化）、受众（工程师/高管措辞）
5. **工程交付形态**：自包含 HTML + 内嵌 SVG，零构建、零 JS 依赖、双击即看、可归档可 diff
6. **Skill 生态意义**：专业审美被固化为可安装的工程资产（39 图型 × 3 变体模板库 + token 约束），"能力包 > 单次 prompt"的又一实证

## D — Data：关键示例

```text
# 安装（Claude Code 为例）
/plugin marketplace add cathrynlavery/diagram-design
/plugin install diagram-design@diagram-design
# GitHub: https://github.com/cathrynlavery/diagram-design
# 在线画廊: https://cathrynlavery.github.io/diagram-design/

# 生成（自然语言 → 自包含 HTML+SVG）
/diagram-design-main 帮我画一个架构图：前端、后端、数据库、Redis 缓存

# 品牌风格接入（一次配置，后续全部生效）
帮 diagram-design 接入 https://yoursite.com 的品牌风格

# 存量重画（内容不变，风格换新；四维可调）
/diagram-design:import-drawio platform.drawio --size=slide-16x9 --detail=simplified --audience=executive
/diagram-design:import-mermaid architecture.mmd --size=slide-16x9 --detail=simplified

# 四维参数速查
格式: HTML / SVG / PNG
尺寸: 文档内嵌 / 16:9 幻灯 / 社交媒体图
细节: 保真 / 平衡 / 简化（节点数随之精简）
受众: 工程师（技术措辞）/ 高管（简化说法）

# 默认风格：白烟色底 + 墨黑线条 + 橙色强调；39 图型 × 3 变体（浅色/深色/完整编辑版）
```

---

来源：RUNOOB 菜鸟教程（微信公众号）
