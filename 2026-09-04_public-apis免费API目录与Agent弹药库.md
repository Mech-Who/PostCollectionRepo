---
title: public-apis：免费 API 目录与 Agent 的外部能力索引
date: 2026-09-04
category: 工具推荐
depth: 标准
layer: layer2
tags: [public-apis, 免费API, GitHub, CORS, HTTPS, 原型开发, AI Agent, MCP]
summary: public-apis 是一个由社区维护的免费公共 API 分类目录，以 README 表格记录 API 名称、用途、认证要求、HTTPS 和 CORS 支持情况。它适合快速寻找天气、金融、新闻、音乐、地理和机器学习等领域的数据源，也可作为 Agent 工具发现的候选索引。但“免费收录”不等于稳定可用于生产，实际接入前仍需检查限流、服务条款、许可证、隐私、可用性和返回结构。
source_url: https://mp.weixin.qq.com/s/BABEEh0aYcRDIBOd9TikyQ
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** `public-apis` 把分散在互联网中的公共 API 整理为可检索目录，降低原型开发和 Agent 工具接入时的发现成本。它是候选源索引，不是对服务质量的担保。

## 我的理解
> 由小林生成，供小涵审阅修改

这个项目最有价值的不是“收录很多免费接口”，而是把 API 发现阶段标准化。开发者可以先按领域、认证、HTTPS 和 CORS 过滤候选，再进入各自文档验证，避免每次从搜索引擎重新开始。

对 Agent 系统而言，它更像工具目录的上游数据源。真正让 Agent 稳定调用，还需要为选中的 API 定义输入输出 schema、鉴权、超时、重试、限流、错误转换和结果验证，不能把一张链接表直接等同于可用工具。

文章展示的浏览器 `fetch` 示例适合 Demo。进入生产环境后，还要考虑密钥暴露、跨域策略变化、第三方服务下线和数据合规。免费 API 最适合验证想法，不宜默认承担关键业务。

## 项目内容

- 项目从 2016 年开始由社区维护，核心资产是一份分类 README，而不是复杂服务端系统。
- 每个条目通常包含名称、描述、认证要求、HTTPS 支持和 CORS 支持等字段。
- 目录覆盖天气、金融、动物、新闻、音乐、地理位置和机器学习等 50 多类场景。
- 文章举例包括 Open-Meteo、CoinGecko、NASA APOD、The Cat API、Dog CEO 和 PoetryDB。
- 社区存在围绕该目录制作的 MCP 服务和 CLI，可进一步用于搜索或调用候选 API。
- 文章发布时称项目约有 47 万 Star、1600 多个 API 和 800 多名贡献者；这些数字会持续变化，应以仓库当前页面为准。

## 接入检查清单

1. **用途与数据质量**：确认数据范围、刷新频率、准确性和缺失值处理。
2. **认证与密钥**：判断是否需要 API Key、OAuth，以及密钥能否安全保存在服务端。
3. **网络条件**：确认 HTTPS、CORS、地区可访问性和域名稳定性。
4. **容量限制**：检查限流、配额、请求成本、超时和批量接口。
5. **错误语义**：记录状态码、错误结构、重试条件和幂等要求。
6. **合规条件**：检查服务条款、许可证、署名要求、隐私和商业使用限制。
7. **替代方案**：关键功能应准备缓存、降级数据或第二供应商，避免单点依赖。

## 最小调用示例

```javascript
const response = await fetch("https://dog.ceo/api/breeds/image/random");

if (!response.ok) {
  throw new Error(`Dog API request failed: ${response.status}`);
}

const data = await response.json();
document.querySelector("#dog").src = data.message;
```

相比原文示例，这里增加了 HTTP 状态检查；真实项目还应加入超时、schema 校验和错误提示。

## 项目地址

- https://github.com/public-apis/public-apis

## 相关笔记

- [[2026-09-03_黄仁勋Agent外骨骼AGI不是即插即用]]
- [[2026-08-26_读懂Pi你就是AI应用之王agent-loop源码]]
