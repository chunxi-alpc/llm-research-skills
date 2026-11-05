# LLM 辅助科研资料与 Skills

面向学生的中文资料仓库：**53 条原表内容、10 个新 Skills、现成技能与完整项目套件**。保留原始提示词和使用经验，按科研任务查找。

## 先下载 Skills

| 需要什么 | 下载与说明 |
|---|---|
| 第一次使用，先拿到 10 个新技能 | **[下载新 Skills 入门合集](downloads/research-skills-starter.zip)** |
| 只安装某一个新技能 | [10 个新技能与单独下载](skills/README.md) |
| Humanizer、两套 Anti-Defensive Writing 等现成技能 | [第三方技能下载与条件](docs/third-party-skills.md) |
| 保留插件、共享文件和原项目结构的完整套件 | [全部下载包](downloads/README.md) |
| 工具没有技能导入功能 | [复制原始提示词](prompts/original-prompts.md) |

**下载 → 解压 → 导入或放入所用 Agent 的技能目录 → 提交任务。**

解压入门合集后，`skills/` 下的每一个目录是一个技能，请连同其中的 `references/` 一起复制。先选一个与任务匹配的技能即可。具体目录、导入方式和第三方套件区别见 [使用指南](docs/getting-started.md)。

例如：

```text
使用 research-paper-reading，对比我提供的 5 篇论文，重点看方法和实验设置。
请用表格列出差异，并给出原文位置。
```

## 10 个新技能

| 科研任务 | 技能 |
|---|---|
| 找论文 | [文献检索](skills/research-literature-search/SKILL.md) |
| 读论文、比较方法 | [论文阅读与多论文对比](skills/research-paper-reading/SKILL.md) |
| 改善论文表达 | [学术语言润色](skills/academic-language-polish/SKILL.md) |
| 检查方法表述 | [方法逻辑与术语一致性检查](skills/method-logic-check/SKILL.md) |
| 讨论想法 | [研究思路讨论](skills/research-idea-discussion/SKILL.md) |
| 投稿前检查 | [论文模拟审稿](skills/paper-peer-review/SKILL.md) |
| 只找错，不改文风 | [拼写与语法纠错](skills/academic-proofreading/SKILL.md) |
| 保留原意翻译 | [中英文学术翻译](skills/academic-translation/SKILL.md) |
| 编码前写清需求 | [编程任务需求整理](skills/coding-task-brief/SKILL.md) |
| 准备模型图 | [模型图说明与绘图提示词](skills/paper-figure-brief/SKILL.md) |

这 10 个技能由本表提示词和经验整理制作，使用 [Agent Skills 格式](https://agentskills.io/specification)，每个目录都附来源说明。绘图技能默认输出绘图说明和提示词。

## 按科研任务查资料

- [文献检索与引文核对](catalog/literature.md)
- [论文阅读与知识整理](catalog/reading.md)
- [论文写作、润色、纠错与翻译](catalog/writing.md)
- [研究思路与模拟审稿](catalog/ideas-review.md)
- [科研编程与需求整理](catalog/coding.md)
- [模型图与科研绘图](catalog/figures.md)
- [提示词集合与方法参考](catalog/reference.md)

[53 条覆盖清单](catalog/coverage.md) · [计算机科研方法总目录](references/computer-science-methods.md) · [资料 CSV](sources/resources.csv)

## 来源与维护

原表中的工具评价、价格、额度和模型名称保留为填写时的经验；当前服务条件以项目或产品说明为准。按名称补充的 Nature Skills 与 Karpathy Skills 在相应条目中单独标注。第三方文件保持原许可，详情见 [许可说明](LICENSE.md)和[第三方来源](docs/third-party-skills.md)。

本仓库只收集文件与使用说明，不自动安装或运行第三方项目。维护方法见 [贡献指南](CONTRIBUTING.md)，交付检查见 [验证报告](reports/verification.md)。
