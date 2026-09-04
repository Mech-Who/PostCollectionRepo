---
id: kf-2026-09-04-工具推荐-public-apis接入检查
title: public-apis 使用法：从候选目录到可靠工具接口
type: fragment
domain: 工具推荐
layer: layer2
source_type: wechat
source_ref: [[2026-09-04_public-apis免费API目录与Agent弹药库]]
source_url: https://mp.weixin.qq.com/s/BABEEh0aYcRDIBOd9TikyQ
tags: [public-apis, 免费API, CORS, 限流, Agent工具, MCP, API治理]
related_fragments: [[kf-2026-09-03-AI技术-黄仁勋AgentHarness外骨骼]]
related_concepts: [Agent工具调用, API治理]
status: stable
created: 2026-09-04
version: 1
---

# 从 public-apis 候选目录到可靠工具接口

## A - Applicable：什么时候用

- 为 Demo、学习项目或内部原型快速寻找公共数据源时。
- 给 Agent、MCP 服务或自动化脚本选择外部 API 时。
- 对候选 API 做接入前评审和生产风险检查时。

## B - Boundary：边界条件

- 收录或免费不代表稳定、准确、可商用，也不代表项目对服务质量背书。
- `No Auth + HTTPS + CORS` 只说明浏览器可能直调，不代表没有限流和隐私风险。
- 浏览器端不得暴露需要保密的 API Key；需要密钥时应由受控服务端代理。
- 关键业务不能只依赖无 SLA 的免费服务，应提供缓存、降级或替代供应商。

## C - Core：核心要点

- 用 public-apis 完成“发现候选”，再进入官方文档完成“验证可用”。
- 接入前至少检查认证、HTTPS、CORS、限流、错误语义、许可证和服务状态。
- 给 Agent 使用时，要把 API 包装成明确 schema、权限边界、超时和验证规则的工具。
- 对返回数据进行结构校验，避免第三方字段变化直接污染下游流程。
- Star、收录数量和 CORS 比例都是动态快照，不能代替运行时测试。

## D - Data：接入模板

```text
API 名称：
官方文档：
用途：
认证方式：None / API Key / OAuth
HTTPS：Yes / No
CORS：Yes / No / Unknown
限流与配额：
超时：
可重试错误：
返回 schema：
许可证与商用条件：
敏感数据：
缓存策略：
降级或替代源：
最后验证日期：YYYY-MM-DD
```
