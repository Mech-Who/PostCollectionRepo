---
id: kf-2026-09-08-bilibili-ai-contest-analysis
title: 内容平台竞赛的数据分析流程
date: 2026-09-08
category: AI 应用
layer: layer2:通用
tags: [数据分析, 指标口径, 数据清洗, 抽样复核, 可重跑]
source_url: https://mp.weixin.qq.com/s/H7-G_vszhDe8tLaNuC4jZA
---

## A · Applicable

适用于分析内容平台榜单、竞赛作品、传播效果与产品成功因素，尤其是需要 Agent 辅助采集时。

## B · Boundary

相关性不能直接解释为因果；样本窗口不重叠、作品归并不准确或疑似非参赛内容时，应降低结论强度并人工复核。

## C · Core

- 先定义字段口径及可回答、不可回答的问题，再开始采集。
- 分离视频级、作品级、字段来源和异常标注，避免分析单位混淆。
- 曝光指标与付出型互动指标要分层解释。
- 空值保持为空，不用 0 制造虚假数据。
- 修改假设后从原表重算，抽样复核并保留可重跑脚本。

## D · Data

```text
tables: videos | works | field_definitions | issues_and_labels
null_policy: keep_null
verification: sample_against_api_or_script_each_round
reproducibility: preserve_build_script_and_recompute_from_source
```
