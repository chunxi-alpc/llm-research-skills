# LLM 辅助科研资料与 Skills

找论文、读论文、修改论文、准备模型图、整理编程需求——从你现在要做的一件事开始。

**[按任务选技能](#choose)** · **[下载 10 个技能合集](downloads/research-skills-starter.zip?raw=true)** · **[直接复制提示词](#prompts)** · [按类别找资料](#resources)

这里有 **10 个科研技能、53 条工具与使用经验**。Skill 是可重复使用的任务说明和配套参考文件，供支持 Skills 的 AI 工具读取。如果平时只用聊天网页，可以直接复制提示词。

**第一次使用？** 建议先跟着 [英文纠错示例](#start) 试一次，再按需要选择其他技能。

<a id="choose"></a>

## 你现在想做什么？

下表的“下载 ZIP”直接获取单个技能；“用法”包含所需材料和调用示例。

| 我想…… | 可以得到什么 | 下载与用法 |
|---|---|---|
| 找某个方向的论文 | 按主题、年份和会议整理的论文清单，附来源链接 | [下载 ZIP](downloads/individual/research-literature-search.zip?raw=true) · [用法](skills/research-literature-search/SKILL.md) |
| 读懂论文、比较几篇方法 | 问题与方法梳理、原文依据、多论文对比表 | [下载 ZIP](downloads/individual/research-paper-reading.zip?raw=true) · [用法](skills/research-paper-reading/SKILL.md) |
| 把论文写得更清楚 | 保留研究事实的修订段落和重要修改说明 | [下载 ZIP](downloads/individual/academic-language-polish.zip?raw=true) · [用法](skills/academic-language-polish/SKILL.md) |
| 检查 Method 是否讲通 | 逻辑问题定位、符号定义与术语统一建议 | [下载 ZIP](downloads/individual/method-logic-check.zip?raw=true) · [用法](skills/method-logic-check/SKILL.md) |
| 讨论研究想法是否可行 | 关键假设、优先改进方向和小规模验证建议 | [下载 ZIP](downloads/individual/research-idea-discussion.zip?raw=true) · [用法](skills/research-idea-discussion/SKILL.md) |
| 投稿前模拟审稿 | 有原文依据的优点、问题和优先修改建议 | [下载 ZIP](downloads/individual/paper-peer-review.zip?raw=true) · [用法](skills/paper-peer-review/SKILL.md) |
| 只改拼写和语法错误 | 纠错后的文本和修改清单，正确表达保持原样 | [下载 ZIP](downloads/individual/academic-proofreading.zip?raw=true) · [用法](skills/academic-proofreading/SKILL.md) |
| 翻译中英文学术段落 | 保留原意、逻辑、数值和术语的译文 | [下载 ZIP](downloads/individual/academic-translation.zip?raw=true) · [用法](skills/academic-translation/SKILL.md) |
| 把编程需求讲清楚 | 可交给编码工具的任务说明和完成标准 | [下载 ZIP](downloads/individual/coding-task-brief.zip?raw=true) · [用法](skills/coding-task-brief/SKILL.md) |
| 准备论文模型图 | 模块与箭头说明、布局建议、可复制的绘图提示词 | [下载 ZIP](downloads/individual/paper-figure-brief.zip?raw=true) · [用法](skills/paper-figure-brief/SKILL.md) |

想一起保存？[下载 10 个技能合集](downloads/research-skills-starter.zip?raw=true)。想找 Humanizer、Nature Skills 等现成项目？[查看第三方技能与套件](docs/third-party-skills.md)。

<a id="start"></a>

## 第一次使用：跟着这个例子走

1. **下载。** 点击 [拼写与语法纠错技能](downloads/individual/academic-proofreading.zip?raw=true)。
2. **解压并导入。** 把整个 `academic-proofreading` 文件夹导入所用工具，或放入它的技能目录。需要保留其中的参考文件，目录应如下所示。[查看具体安装方法](docs/getting-started.md#3-导入或放入技能目录)。

   ~~~text
   academic-proofreading/
   ├── SKILL.md
   ├── SOURCE.md
   └── references/
   ~~~

3. **开始对话。** 加载技能后，把下面的任务复制给 AI：

   ~~~text
   使用 academic-proofreading，检查下面的英文。
   只修正拼写和语法错误，其他表达保持原样，并列出改动。

   Our method use two encoders. It improves accuracy by 2.1 points.
   ~~~

这个例子应只改 `use → uses`，第二句保持原样。接下来，把示例替换成你自己的段落即可。

**找不到“导入技能”？** 可以先用 [下方的普通提示词](#prompts)，或查看 [安装指南](docs/getting-started.md)。

<details>
<summary>更多调用示例：读论文、学术翻译、准备模型图</summary>

安装对应技能后，复制任务并提供材料。

**读论文**

~~~text
使用 research-paper-reading，阅读我上传的论文。
先说明研究问题，再按输入、关键模块、输出解释方法。
主要结论请标出原文章节或图表位置。
~~~

**学术翻译**

~~~text
使用 academic-translation，把下面的中文段落翻译为英文。
保留原意、逻辑和已有的英文术语，使用常见学术表达。
只输出适合粘贴到 Word 的译文。

【粘贴中文段落】
~~~

**准备模型图**

~~~text
使用 paper-figure-brief，把下面的方法转成模型图说明。
列出模块、箭头方向和图内英文标签，区分训练与推理。
最后给出一段可复制给绘图工具的完整提示词。

【粘贴方法段落】
~~~

</details>

<a id="prompts"></a>

## 只用聊天网页？直接复制提示词

提供论文后，可以直接发送下面这段话：

~~~text
请根据我提供的论文，解释它解决了什么问题，以及方法如何从输入得到输出。
列出主要实验结论，并给出对应的章节、页码或图表位置。
区分论文明确说明的内容与你的解释；原文未说明的细节请注明。
~~~

需要其他任务？[打开原始提示词集合](prompts/original-prompts.md)，选择检索、润色、纠错、翻译或审稿模板。文件上传、联网检索等能力由所用工具提供。

<a id="resources"></a>

## 按科研任务查找资料

资料沿用 CSV 的 **12 个类别**，名称做了简化。点进对应任务，查看工具、提示词、使用经验和相关 Skills；上方的 10 个技能提供常见任务的直接下载入口。

| 我要做的事 | 查看这一类 |
|---|---|
| 检索相关论文、核对引文 | [找论文](catalog/literature.md) |
| 读懂论文、比较方法、整理知识库 | [读论文](catalog/reading.md) |
| 寻找研究方向与新想法 | [研究想法获取](catalog/ideas.md) |
| 检查初稿思路、讨论方法与创新性 | [初稿思路把关](catalog/idea-check.md) |
| 写代码、调试、整理编程需求 | [编程与调试](catalog/coding.md) |
| 写论文、改进表达、检查方法逻辑 | [写作与润色](catalog/writing.md) |
| 整理模型结构、准备绘图提示词 | [论文模型图](catalog/figures.md) |
| 保留原意翻译学术段落 | [学术翻译](catalog/translation.md) |
| 只修改拼写和语法错误 | [拼写与语法纠错](catalog/proofreading.md) |
| 检查完整论文、获取审稿意见 | [投稿前模拟审稿](catalog/peer-review.md) |
| 查找查重与 AI 率检测入口 | [查重与 AI 率检测](catalog/originality.md) |
| 查阅综合技能套件与科研方法目录 | [综合参考资料](catalog/reference.md) |

<details>
<summary>现成技能与套件：Humanizer、Nature Skills、Superpowers 等</summary>

| 用途 | 项目与安装说明 |
|---|---|
| 修改论文表达 | [Humanizer](docs/third-party-skills.md#blader--humanizer) · [Scientific Manuscript Editor](docs/third-party-skills.md#deathcats4--scientific-manuscript-editor) |
| 减少冗余解释与铺垫 | Anti-Defensive Writing：[Adkid-Zephyr 版](docs/third-party-skills.md#adkid-zephyr--anti-defensive-writing) · [Kiterlin 版](docs/third-party-skills.md#kiterlin--anti-defensive-writing) |
| 机器学习论文写作 | [ML Paper Writing](docs/third-party-skills.md#orchestra-research--ai-research-skills) |
| 阅读、写作、绘图等科研任务 | [Nature Skills](docs/third-party-skills.md#yuan1z0825--nature-skills) · [Academic Research Skills](docs/third-party-skills.md#imbad0202--academic-research-skills) |
| 编程任务与开发流程 | [Superpowers](docs/third-party-skills.md#obra--superpowers) · [Karpathy Skills](docs/third-party-skills.md#multica-ai--andrej-karpathy-skills) |

这些项目各有安装方式和依赖，点项目名查看说明。[全部 26 个下载包](downloads/README.md)同时提供单个技能和完整套件。

</details>

---

[全部 53 条资料](catalog/coverage.md) · [资料 CSV](sources/resources.csv) · [全部下载](downloads/README.md) · [许可说明](LICENSE.md)

<details>
<summary>资料来源与维护</summary>

本仓库的 10 个科研技能由资料表中的提示词和经验整理制作，采用 [Agent Skills 格式](https://agentskills.io/specification)，每个技能目录附来源说明。第三方文件保留原许可，按名称补充的 Nature Skills 与 Karpathy Skills 在 [来源说明](docs/third-party-skills.md)中标注。

工具评价、价格和额度属于资料填写时的记录，当前条件以对应服务说明为准。

[补充与维护指南](CONTRIBUTING.md) · [内容与下载包检查记录](reports/verification.md)

</details>
