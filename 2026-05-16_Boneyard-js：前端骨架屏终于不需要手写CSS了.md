# Boneyard-js：前端骨架屏终于不需要手写CSS了

- **来源**：前端之神（林三心不学挖掘机）
- **链接**：https://mp.weixin.qq.com/s/cYeV3evx-wQ2JWG2MZiX5g
- **日期**：2026-05-16 归档
- **分类**：工具推荐
- **加工深度**：🟡 标准
- **标签**：骨架屏 / Boneyard-js / React / Next.js / 自动生成 / CLI工具

---

## 摘要

推荐Boneyard-js全自动骨架屏生成工具。传统骨架屏需手写CSS、计算尺寸、适配响应式，该工具从真实组件生成骨架，UI变化时自动跟随。使用仅需三步：Skeleton组件包裹业务组件 → fixture提供mock数据 → `npx boneyard-js build` 扫描生成配置文件。安装 `npm install boneyard-js`，兼容React/Next.js。

## 我的理解

骨架屏从视觉设计问题变成了工程化问题。Boneyard-js的思路很聪明——不生成独立骨架代码，而是直接从真实组件提取结构，这样即使布局变了也不需要手动维护两套代码。适合Next.js等SSR场景中优化LCP（Largest Contentful Paint）。

---

*加工时间：2026-05-16*