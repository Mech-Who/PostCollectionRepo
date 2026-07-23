---
title: grill-me：让AI在写代码前先盘问你——Matt Pocock的设计哲学
date: 2026-06-15
category: AI应用
depth: 深度
layer: layer2
tags: ["AI编程", "Prompt工程", "AI协作", "工程实践", "Harness Engineering"]
summary: grill-me是Matt Pocock的一个极简Skill，只有几行指令，但精准解决了AI『急着写代码』的毛病。核心设计：沿着设计树逐分支问问题、每个问题先给推荐答案(降低你的响应成本)、一次只问一个、代码已有信息自己去查。
source_url: https://mp.weixin.qq.com/s/MBCVBDpsnQTg6Z1-IL1HzA
source: weixin
status: 📥已采集
sync_si: ❌未同步
---

> **摘要：** grill-me是Matt Pocock的一个极简Skill，只有几行指令，但精准解决了AI『急着写代码』的毛病。核心设计：沿着设计树逐分支问问题、每个问题先给推荐答案(降低你的响应成本)、一次只问一个、代码已有信息自己去查。

## 我的理解
> 由小林生成，供小涵审阅修改

这篇文章对『怎么写好AI指令』非常有启发。grill-me虽然只有几行字，但每一句都在堵AI的一个具体缺陷。『每个问题先给推荐答案』这个设计特别聪明——把开放式问题变成判断题，大幅降低沟通成本。结合我以前了解的Matt Pocock的『teach』Skill，他的设计哲学是：一个有用的工具不一定要做得复杂。

## 原文

grill-me是Matt Pocock skills仓库里的一个工具，几行字解决AI急写代码的问题。设计要点：沿着『设计树(design tree)』逐分支问问题(决策有先后的)；每个问题AI先给推荐答案(你只需同意或纠正)；一次只问一个问题(上一个回答影响下一个)；代码里已有的信息自己去查。特点：无状态(不存任何东西)、停下来的时机模糊、不分任务大小。
