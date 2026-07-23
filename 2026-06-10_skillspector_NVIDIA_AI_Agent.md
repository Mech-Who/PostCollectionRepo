---
title: "skillspector：NVIDIA 开源了 AI Agent 技能安全扫描器！"
date: 2026-06-10
source: "微信公众号：AI开源提效指南"
author: "AI开源提效指南"
category: "工具推荐"
depth: "🟡标准"
layer: "layer1"
processed_date: 2026-06-10
sync_si: "✅已同步"
mempalace: "❌未入库"
---

# skillspector：NVIDIA 开源了 AI Agent 技能安全扫描器！

## 原文内容

大家好！这里是`AI开源提效指南`！

平时安装三方 Skill 时，总是担心安全问题，毕竟网上贡献者五花八门，里面有没有后门真不好说！

之前我总是使用 [asm：Claude Code、Codex、Cursor、OpenClaw 等多种 AI 编程助手技能统一管理神器！](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ==&mid=2247484399&idx=1&sn=851e314e7c23608ec07737749889cad2&scene=21#wechat_redirect)来对技能进行安全审计，前段时间发现 NVIDIA 开源了一款 **AI Agent Skill 安全扫描器**。

今天来试试效果！

skillspector 可以判断 Skill 安装到 Claude Code、Codex CLI、Gemini CLI 等 Agent 环境之前，先扫描它有没有恶意指令、越权行为、数据外传、供应链风险或危险代码。

换句话说，AI Agent 技能越来越多，但这些技能默认会被 Agent 信任执行，安装前到底安不安全？

作者提到的研究数据也很直观：

*   26.1% 的 Skills 至少包含一个漏洞
    
*   5.2% 呈现出疑似恶意意图
    
*   带可执行脚本的 Skills 更容易出现安全问题
    

SkillSpector 正好能解决这个问题，主要还有 NVIDIA 背景，用着也放心一点。

### 🧠 核心能力拆解

SkillSpector 的能力可以概括成 5 个关键词：**多输入、广覆盖、双阶段、可集成、可解释**。

#### 1.多格式输入扫描

它不只扫描本地目录，还支持多种输入源：

*   Git 仓库
    
*   URL
    
*   zip 文件
    
*   本地目录
    
*   单个 SKILL.md 文件
    

这意味着你既可以在安装前扫描远程仓库，也可以把它集成到内部 Skill 发布流程中。

#### 2. 64 个检测模式，覆盖 16 个安全类别

SkillSpector 内置 **64 个检测模式**，覆盖 **16 个类别**，包括：

*   Prompt Injection：提示词注入
    
*   Data Exfiltration：数据外传
    
*   Privilege Escalation：权限提升
    
*   Supply Chain：供应链风险
    
*   Excessive Agency：过度自主行为
    
*   Output Handling：输出处理风险
    
*   System Prompt Leakage：系统提示词泄露
    
*   Memory Poisoning：记忆投毒
    
*   Tool Misuse：工具滥用
    
*   Rogue Agent：恶意 Agent 行为
    
*   Trigger Abuse：触发器滥用
    
*   Dangerous Code AST：危险代码调用
    
*   Taint Tracking：污点流追踪
    
*   YARA Signatures：恶意样本特征
    
*   MCP Least Privilege：MCP 最小权限
    
*   MCP Tool Poisoning：MCP 工具投毒
    

这个覆盖面非常贴近当下 Agent 生态的真实风险，不只是简单 grep 一下敏感词。

#### 3. 两阶段分析：静态扫描 + 可选 LLM 语义分析

SkillSpector 使用两阶段检测流水线：

##### 1：静态分析

静态阶段负责快速、高召回地发现可疑问题，包括：

*   正则规则匹配
    
*   AST 危险调用检测
    
*   依赖漏洞查询
    
*   文件级扫描
    
*   可疑脚本识别
    

典型检测包括：

*   `exec()` / `eval()`
    
*   `subprocess`
    
*   `os.system`
    
*   外部脚本拉取
    
*   环境变量收集
    
*   文件读取后网络外传
    
*   未固定版本依赖
    

##### 2：LLM 语义分析

LLM 阶段用于理解上下文和意图，降低误报，并给出更清晰的解释。

比如：同样出现 `requests.post`，它可能是正常上传报告，也可能是把环境变量发到外部服务器。 LLM 语义分析可以结合上下文判断风险是否真实成立。

#### 4. 实时依赖漏洞查询

SkillSpector 的 SC4 规则会调用 OSV.dev 查询依赖漏洞：

*   不需要 API Key
    
*   支持批量查询
    
*   支持离线 fallback
    
*   内存缓存 1 小时，减少重复请求
    

这让它不仅能查 Skill 自身是否可疑，也能检查 Skill 依赖链是否存在已知 CVE。

#### 5. 多种报告格式，方便进入工程流程

SkillSpector 支持多种输出格式：

*   Terminal：终端可读报告
    
*   JSON：机器可读，适合二次处理
    
*   Markdown：适合文档归档
    
*   SARIF：适合 CI/CD、代码扫描平台、IDE 集成
    

这点很关键，因为安全工具如果只能手工跑，价值会被打折；支持 SARIF 和 JSON 后，就可以很自然地进入自动化流程。

### ⚙️ 安装方式

项目要求 Python 3.12+。

官方推荐先创建虚拟环境，再安装：

```
# Clone 仓库
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# 使用 uv 创建虚拟环境
uv venv .venv && source .venv/bin/activate
# 或使用 Python 自带 venv
python3 -m venv .venv && source .venv/bin/activate

# 生产安装
make install

# 开发安装
make install-dev
```

我看官网也没有提供打包好的二进制文件或者docker，这里我自己做了一个docker容器，大家需要的话直接去用就行！

```
registry.cn-beijing.aliyuncs.com/opencontainers/skillspector:latest
```

使用方法：

```
docker run --rm -it -v /root/.codex/skills/figma-generate-design:/skills registry.cn-beijing.aliyuncs.com/opencontainers/skillspector:latest scan /skills --no-llm
```

### 🚀 快速使用示例

扫描本地 Skill 目录：

```
skillspector scan ./my-skill/
```

扫描单个 SKILL.md 文件：

```
skillspector scan ./SKILL.md
```

扫描远程 Git 仓库：

```
skillspector scan https://github.com/user/my-skill
```

扫描 zip 包：

```
skillspector scan ./my-skill.zip
```

### 📄 输出报告示例

默认终端输出：

```
skillspector scan ./my-skill/
```

输出 JSON 报告：

```
skillspector scan ./my-skill/ --format json --output report.json
```

输出 Markdown 报告：

```
skillspector scan ./my-skill/ --format markdown --output report.md
```

输出 SARIF 报告：

```
skillspector scan ./my-skill/ --format sarif --output report.sarif
```

如果你要接入 GitHub Code Scanning、企业内部安全平台或 CI 流水线，SARIF 会很实用。

### 🤖 LLM 语义分析配置

SkillSpector 支持 `OpenAI`、 `Anthropic`、 `NVIDIA`，也支持本地 OpenAI 服务，比如 `Ollama`、`vLLM`、`llama.cpp`等提供商！

具体环境变量配置，大家去看下官方仓库就行了！

只做静态分析，跳过 LLM：

```
skillspector scan ./my-skill/ --no-llm
```

这个模式适合速度优先、成本敏感，或者不方便把待审计 Skill 内容发给外部模型的环境。

### 🧩 风险评分机制

SkillSpector 会给扫描目标计算 0-100 的风险分：

*   CRITICAL：+50 分
    
*   HIGH：+25 分
    
*   MEDIUM：+10 分
    
*   LOW：+5 分
    
*   如果包含可执行脚本，会有 1.3x 风险倍率
    

最终建议分为：

*   0-20：LOW / SAFE
    
*   21-50：MEDIUM / CAUTION
    
*   51-80：HIGH / DO NOT INSTALL
    
*   81-100：CRITICAL / DO NOT INSTALL
    

这种评分方式很适合做安装门禁：低风险放行，中风险人工复核，高风险直接阻断。

### 🛠️ 技术架构亮点

#### 1. 规则覆盖 Agent 特有风险

传统 SAST 主要看代码漏洞，而 SkillSpector 额外关注：

*   技能描述中的隐藏指令
    
*   Tool metadata 中的参数注入
    
*   Prompt 泄露诱导
    
*   Memory poisoning
    
*   MCP 权限声明不匹配
    
*   Agent 自主行为过度扩张
    

这些都是 Agent 时代的新问题。

#### 2. AST 检测危险行为

它会识别 Python 代码里的危险调用，例如：

*   `exec()`
    
*   `eval()`
    
*   `compile()`
    
*   `subprocess`
    
*   `os.system`
    
*   动态导入
    
*   动态属性访问
    

对于包含脚本的 Skill，这类检测非常必要。

#### 3. 污点追踪更接近真实攻击链

单独看到"读取文件"不一定危险，单独看到"发送网络请求"也不一定危险。

但如果数据流是：

> 读取密钥 / 环境变量 / 文件内容 → 拼接请求 → 发往外部服务器

那风险就非常高。

SkillSpector 的 taint tracking 正是用来发现这种链式问题。

### 📌 典型应用场景

#### 1. 安装第三方 Agent Skill 前做安全检查

这是最直接的使用方式：

```
skillspector scan https://github.com/someone/some-skill
```

如果评分高、建议是 DO NOT INSTALL, 就需要谨慎安装了。

#### 2. 企业内部 Skill 上架审核

团队内部如果维护自己的 Skill 市场，可以把 SkillSpector 接进审核流程：

*   PR 提交后自动扫描
    
*   输出 SARIF 报告
    
*   高危规则阻断合并
    
*   中危问题进入人工复核
    

#### 3. Agent 平台供应链安全

随着 MCP、Agent Skill、工具市场越来越多，平台方需要对第三方能力包做基础安全扫描。

SkillSpector 可以作为第一层检测器。

### 🔗 参考资源

```
GitHub 仓库：https://github.com/nvidia/skillspector
开发文档：https://raw.githubusercontent.com/NVIDIA/SkillSpector/main/docs/DEVELOPMENT.md
OSV.dev：https://osv.dev
```

---

免责声明：本文内容仅供学习交流，所述工具/方法请遵守相关平台服务条款及法律法规。如涉及第三方服务，请以官方最新政策为准。

---

**🎯** **觉得这份工具干货有用？希望收到您的支持：**

*   ⭐ 星标 / 置顶公众号，**第一时间解锁最新工具分享！**
    
*   ✅ **点赞「推荐」**，让更多技术伙伴发现优质干货！
    
*   🔗 **转发**给团队小伙伴，一起高效提效！
    
*   💬 **底部留言区**，告诉我您想找的工具/项目方向！
    

**📬 长期追踪优质开源工具**

*   关注「**AI 开源提效指南**」｜日更开源神器，玩转技术提效！
    
*   回复 **【容器加速器】**，即刻开启你的高效探索之旅～

---

## 摘要

**Key Takeaway**：NVIDIA 开源了 SkillSpector，一款面向 AI Agent Skill 生态的安全扫描工具，通过 64 个检测模式覆盖 16 类安全风险，结合静态分析与 LLM 语义分析两阶段检测，支持多种输入格式和报告输出，为 Agent 生态的供应链安全提供了企业级解决方案。

**Key Points**：
1. 支持 Git 仓库、URL、zip、本地目录、单个文件等多种输入源的扫描
2. 内置 64 个检测模式，涵盖 Prompt 注入、数据外传、权限提升、供应链风险等 16 类安全问题
3. 两阶段分析：静态扫描（快速高召回）+ 可选 LLM 语义分析（降低误报）
4. 输出支持 Terminal、JSON、Markdown、SARIF 四种格式，便于集成 CI/CD 流程
5. 包含实时依赖漏洞查询（OSV.dev）和 0-100 风险评分机制，可做安装门禁

---

## 理解

SkillSpector 解决的是一个正在快速增长的痛点——AI Agent 生态中三方 Skill 的安全信任问题。26.1% 的 Skill 至少包含一个漏洞这个数据本身就说明这不是杞人忧天。工具的设计思路很清晰：不是简单地做关键词匹配，而是针对 Agent 特有的风险场景（Prompt 注入、MCP 权限、记忆投毒等）设计检测规则，两阶段的设计（静态扫召回 + LLM 降误报）兼顾了效率和准确率。不过实际效果还需要更多生产环境的验证，尤其是 LLM 语义分析阶段对模型的依赖可能会引入成本和延迟问题。对于正在使用或开发 AI Agent 的团队来说，建议将其作为 CI 门禁的一部分引入，至少在安装三方 Skill 前做一道过滤。

---

## 元数据
- 分类：工具推荐
- 加工深度：🟡标准
- Layer：layer1
- K-Fragment：否
