# Markdown还是HTML？这是个蠢问题！

- **来源**：[微信公众号「花叔」](https://mp.weixin.qq.com/s/4dwaOumeC7YsBk5Eucvk1A)
- **整理日期**：2026-05-10
- **分类**：#AI应用
- **加工深度**：🟡 标准
- **标签**：#Markdown #HTML #AI写作 #工具对比

---

## 核心观点

### 争论的起源
Claude Code 团队成员 Thariq 发文《HTML是新的Markdown》，24小时内获得500万+阅读，网络上随即分裂为 Markdown党 和 HTML党 两派。

### Markdown党的论据
- `AGENTS.md` 被60,000+开源项目采用，获 AWS、Anthropic、Google、Microsoft、OpenAI 等巨头支持
- Karpathy 的 `llm-wiki` 核心架构为三层 md，`CLAUDE.md` 单日涨 7,900 star
- **Token 效率极高**：同一篇博客，HTML 需 16,180 个 token，转成 md 仅需 3,150 个，压缩约 80%
- GitHub 官方观点：「文档不再是描述代码，文档就是代码」

### HTML党的论据
- **空间信息**：diff、架构图、流程图等有空间维度的内容，HTML 左右对照展示理解效率更高
- **动态体验**：产品原型的动画、交互效果，文字描述无法替代视觉呈现
- **结构化阅读**：可折叠章节、Tab 代码块、侧边栏等，让文档从"扫一眼"变成"真正阅读"
- Anthropic 推出 **Live Artifacts**，HTML 升级为可持久化、可交互、能拉实时数据的 dashboard

### 作者结论 ⭐
> **两边都赢了，因为他们各自在回答不同的问题。**
> - Markdown党回答的是「我们用什么**写**」
> - HTML党回答的是「我们给人什么**看**」

**核心分工逻辑：**
- ✍️ **生产端** → Markdown：轻量、快速、可 diff、token 高效
- 👁️ **消费端** → HTML：丰富、可视化、可交互、易分享

> AI 的出现使生产成本可被 AI 吸收，原本需要折中的需求被**解耦为两端的极端最优**。

---

## 我的理解

这篇文章戳破了一个常见的"伪对立"陷阱——Markdown vs HTML 的争论本质上是因为两派人在回答不同的问题。

**对我们的启示：**
1. **写作用 Markdown**：写推文笔记、知识库、技术文档，用 md 最高效，token 省、diff 友好、AI 处理方便
2. **展示用 HTML**：最终给读者看的内容，该有图有表有交互就上 HTML
3. **工具解耦**：不要试图用一个格式解决所有问题，AI 时代可以用工具链打通两端

**花叔的 `huashu-md-html` 工具**（MIT License）值得关注：
- GitHub：https://github.com/alchaincyf/huashu-md-html
- 支持 20+ 格式 → md，md → 4套CSS主题的精美 HTML
- 正好解决了"写用md、看用HTML"的切换成本问题

---

## 关键要点

- [ ] Markdown 适合**生产**：写作、编辑、版本对比，token效率高
- [ ] HTML 适合**消费**：展示、分享、交互体验
- [ ] AI 降低了格式转换成本，两端各自走向极端最优
- [ ] 实际工作流：写作用 md → 发布时用工具转 HTML
- [ ] 参考案例：Karpathy 的 llm-wiki（md内核 + HTML外壳）
