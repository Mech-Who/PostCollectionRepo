---
title: GordenSuperPPTSkills: AI 做 PPT 赛道终结者？
date: 2026-06-10
category: AI应用
depth: 深度
layer: layer2
tags: [PPT, AI生成, Skill, Codex, 办公自动化]
summary: GordenSuperPPTSkills 是一个用 Codex 生成 PPT 的技能包，核心思路：先用 GPT 生成高质量图片型 PPT，再通过视觉识别+图层拆解+坐标重建还原为可编辑 PPTX 文件，解决"AI 生成好看但没法改"的痛点。
source_url: https://mp.weixin.qq.com/s/4exLaQWnnq2IGSArlaAytw
source: weixin
status: 📥已采集
sync_si: ✅已同步
---

> **摘要：** GordenSuperPPTSkills 分为 3 个子 Skill：GordenImagePPTGen（生成图片 PPT）、GordenImage2PPTX（图片→可编辑 PPTX 还原）、GordenSuperPPTSkill（串联工作流）。解决"AI 做的好看但没法改"的核心矛盾。

## 我的理解
> 由小林生成，供小涵审阅修改

这个项目的设计思路值得学习——不是一步到位追求可编辑，而是"先追求设计稿质量，再追求可编辑重建"的两步策略。图层拆解思路（背景层→框架层→图标层→文字层）和逆向工程的思维，类似我之前在"Harness Engineering"中看到的"先扫描不修改"原则。不过目前仅限 Codex 使用，且 GPT 转图片消耗额度较大。如果推文知识管理后续要做可视化报告输出，这个思路可以借鉴。

## 📌 关键要点
- **核心方法**：GPT 生成高质量图片 PPT → 视觉识别拆解图层（背景/框架/图标/文字）→ 坐标重建为可编辑 PPTX
- **解决痛点**：AI 生图好看但没法改 + 复杂版式人工复刻太费时间
- **技术栈**：python-pptx + pillow + numpy

### 安装方式
```bash
pip3 install python-pptx pillow numpy
git clone https://github.com/GordenSun/GordenSuperPPTSkills
cd GordenSuperPPTSkills
cp -R GordenImagePPTGen   "${CODEX_HOME:-$HOME/.codex}/skills/GordenImagePPTGen"
cp -R GordenImage2PPTX    "${CODEX_HOME:-$HOME/.codex}/skills/GordenImage2PPTX"
cp -R GordenSuperPPTSkill "${CODEX_HOME:-$HOME/.codex}/skills/GordenSuperPPTSkill"
```

### 使用限制
- ⚠️ 仅限 Codex 运行环境，依赖 GPT 图像生成和视觉能力
- ⚠️ 图片转可编辑消耗较多模型额度
- ⚠️ 越复杂的版面越考验图层提取和坐标重建能力

## 原文

（原文内容：详细介绍 GordenSuperPPTSkills 的 3 个子技能设计、技术思路、在 AI PPT 赛道中的定位。HTML 生成视频的 Skill 也采用了类似的分层设计思路。）

**GitHub 地址：** https://github.com/GordenSun/GordenSuperPPTSkills

## 相关笔记
- [[2026-06-10_HTML生成视频的Skill.md]] — 同样用 AI 生成内容的工具，HyperFrames 也是为 Agent 设计的 Skill
