# LLM 辅助科研资料与 Skills

找论文、读论文、修改论文、准备模型图、整理编程需求——从你现在要做的一件事开始。

**[按任务选技能](#choose)** · **[下载 10 个技能合集](downloads/research-skills-starter.zip?raw=true)** · **[直接复制提示词](#prompts)** · [按类别找资料](#resources)

这里有 **10 个科研技能、53 条工具与使用经验**。Skill 是可重复使用的任务说明和配套参考文件，供支持 Skills 的 AI 工具读取。如果平时只用聊天网页，可以直接复制提示词。

**第一次使用？** 从 [把论文写得更清楚](#start) 开始，看看如何用技能改进自己的论文段落。

<a id="choose"></a>

## 你现在想做什么？

「复制提示词」跳到对应示例。点击代码块右上角的复制按钮，即可把整段提示词发给 AI。「用法」包含所需材料和技能调用示例。

| 我想…… | 可以得到什么 | 下载与使用 |
|---|---|---|
| 找某个方向的论文 | 按主题、年份和会议整理的论文清单，附来源链接 | [下载 ZIP](downloads/individual/research-literature-search.zip?raw=true) · [复制提示词](#prompt-research-literature-search) · [用法](skills/research-literature-search/SKILL.md) |
| 读懂论文、比较几篇方法 | 问题与方法梳理、原文依据、多论文对比表 | [下载 ZIP](downloads/individual/research-paper-reading.zip?raw=true) · [复制提示词](#prompt-research-paper-reading) · [用法](skills/research-paper-reading/SKILL.md) |
| 把论文写得更清楚 | 保留研究事实的修订段落和重要修改说明 | [下载 ZIP](downloads/individual/academic-language-polish.zip?raw=true) · [复制提示词](#prompt-academic-language-polish) · [用法](skills/academic-language-polish/SKILL.md) |
| 检查 Method 是否讲通 | 逻辑问题定位、符号定义与术语统一建议 | [下载 ZIP](downloads/individual/method-logic-check.zip?raw=true) · [复制提示词](#prompt-method-logic-check) · [用法](skills/method-logic-check/SKILL.md) |
| 讨论研究想法是否可行 | 关键假设、优先改进方向和小规模验证建议 | [下载 ZIP](downloads/individual/research-idea-discussion.zip?raw=true) · [复制提示词](#prompt-research-idea-discussion) · [用法](skills/research-idea-discussion/SKILL.md) |
| 投稿前模拟审稿 | 有原文依据的优点、问题和优先修改建议 | [下载 ZIP](downloads/individual/paper-peer-review.zip?raw=true) · [复制提示词](#prompt-paper-peer-review) · [用法](skills/paper-peer-review/SKILL.md) |
| 只改拼写和语法错误 | 纠错后的文本和修改清单，正确表达保持原样 | [下载 ZIP](downloads/individual/academic-proofreading.zip?raw=true) · [复制提示词](#prompt-academic-proofreading) · [用法](skills/academic-proofreading/SKILL.md) |
| 翻译中英文学术段落 | 保留原意、逻辑、数值和术语的译文 | [下载 ZIP](downloads/individual/academic-translation.zip?raw=true) · [复制提示词](#prompt-academic-translation) · [用法](skills/academic-translation/SKILL.md) |
| 把编程需求讲清楚 | 可交给编码工具的任务说明和完成标准 | [下载 ZIP](downloads/individual/coding-task-brief.zip?raw=true) · [复制提示词](#prompt-coding-task-brief) · [用法](skills/coding-task-brief/SKILL.md) |
| 准备论文模型图 | 模块与箭头说明、布局建议、可复制的绘图提示词 | [下载 ZIP](downloads/individual/paper-figure-brief.zip?raw=true) · [复制提示词](#prompt-paper-figure-brief) · [用法](skills/paper-figure-brief/SKILL.md) |

想一起保存？[下载 10 个技能合集](downloads/research-skills-starter.zip?raw=true)。想找 Humanizer、Nature Skills 等现成项目？[查看第三方技能与套件](docs/third-party-skills.md)。

<a id="start"></a>

## 第一次使用：把论文写得更清楚

以论文 Method 中介绍检索流程的段落为例：让读者看清每一步做什么、为什么需要这一步，以及各步骤如何衔接。

1. **下载。** 点击 [学术语言润色技能](downloads/individual/academic-language-polish.zip?raw=true)。
2. **解压并导入。** 把整个 `academic-language-polish` 文件夹导入所用工具，或放入它的技能目录。需要保留其中的参考文件，目录应如下所示。[查看具体安装方法](docs/getting-started.md#3-导入或放入技能目录)。

   ~~~text
   academic-language-polish/
   ├── SKILL.md
   ├── SOURCE.md
   └── references/
   ~~~

3. **开始对话。** 加载技能后，把下面的任务复制给 AI。可以先试用这段演示文本，也可以替换成自己的论文段落：

   ~~~text
   使用 academic-language-polish，润色下面的论文 Method 段落。
   让读者清楚理解为什么需要重排序，以及检索、重排序和生成之间的关系。
   可以调整句序、拆分长句、删除重复表达；保留方法步骤、数值和术语，不增加原文没有的结果或结论。
   请给出修改后的英文段落，并用中文简要说明关键改动。

   原文：
   For each question, we first retrieve 20 candidate passages from the corpus. These passages are then processed by a reranker, which is used because some of the retrieved passages are not relevant to the question. The reranker assigns a relevance score to each question–passage pair. Based on these scores, we select the five passages with the highest scores, and these selected passages are used as the context for the language model to generate an answer.
   ~~~

**改写示意：**

> For each question, we retrieve 20 candidate passages from the corpus. To filter out irrelevant passages, a reranker scores each question–passage pair by relevance. We select the five highest-scoring passages and provide them to the language model as context for answer generation.

改写后，“检索 20 个候选段落 → 重排序 → 选出前 5 个 → 作为生成回答的上下文”的流程更容易读懂；重排序的目的紧接对应操作，重复表达也被删去。实际输出可以不同，重点是保留方法事实，让步骤和衔接更清楚。

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

下面的示例可以直接发给 AI。处理自己的任务时，把示例里的主题或材料换成你的内容。

<a id="prompt-research-literature-search"></a>

### 找某个方向的论文

~~~text
请联网查找 2022—2025 年关于检索增强生成中证据重排序的论文，优先检索 ACL、EMNLP 和 NAACL。
选出最相关的论文，最多 5 篇。用表格给出题目、作者、年份、发表会议、原文链接和证据重排序方法。
请用会议论文集或论文主页核对发表信息。
~~~

<a id="prompt-research-paper-reading"></a>

### 读懂论文、比较几篇方法

~~~text
请对比下面两段示例摘要。用表格说明每种方法的输入、处理步骤、输出和评测指标。
请引用原句说明关键差异，并指出摘要未交代的信息。

摘要 A
给定一个问题，系统检索 20 个候选段落，按检索分数选出 5 段供模型生成答案。实验报告答案准确率。

摘要 B
给定一个问题，系统检索 20 个候选段落，用重排序模型打分，再选出 5 段供模型生成答案。实验报告证据召回率。
~~~

<a id="prompt-academic-language-polish"></a>

### 把论文写得更清楚

~~~text
请润色下面的论文 Method 段落，说明阈值如何选定，以及它在哪里使用。保留数据划分和评价指标。
先给出修改后的英文段落，再用中文说明关键改动。

We use the validation set for the purpose of selecting a threshold.
The selection of the threshold is done by choosing the value that gives the highest F1 score.
After the threshold is selected, we use the selected threshold on the test set.
~~~

<a id="prompt-method-logic-check"></a>

### 检查 Method 是否讲通

~~~text
请检查下面的 Method 片段，重点看变量定义、术语和每一步的输入输出。
用表格列出问题位置、原因和修改建议。缺少的定义或步骤请标为待确认。

给定问题 q，检索器返回候选段落集合 D。重排序模块为每个证据片段计算得分 s_i。
生成模块根据文档集合 C 生成答案。推理时，生成模块使用标注证据选择文档。
~~~

<a id="prompt-research-idea-discussion"></a>

### 讨论研究想法是否可行

~~~text
我想在检索增强问答中加入重排序。现有方法从 20 个候选段落中按检索分数选 5 段，新方法按重排序分数选 5 段。
我有 100 道带答案和证据标注的问题。请指出最关键的假设，设计一个小规模验证实验。
写清对照方法、评测指标，以及什么结果会支持这个想法。
~~~

<a id="prompt-paper-peer-review"></a>

### 投稿前模拟审稿

~~~text
请模拟审阅下面这段演示稿件，重点判断实验能否支持论文的主张。
先概括贡献，再列出优点、主要问题和优先修改建议。请为每条主要意见指出对应句子。

我们在检索器后加入重排序模型，以提高跨领域问答准确率。
在一个领域的测试集上，加入重排序后，答案准确率从 60% 提高到 63%。
我们据此认为，重排序能在不同领域稳定提高问答准确率。
~~~

<a id="prompt-academic-proofreading"></a>

### 只改拼写和语法错误

~~~text
请只修改下面英文的拼写和语法错误，保留正确的句子、术语和数值。
先给出校对后的完整段落，再列出每处错误和改法。

Our model use two encoders to extract featuers.
It improves accuracy by 2.1 percentage points on the test set.
~~~

<a id="prompt-academic-translation"></a>

### 翻译中英文学术段落

~~~text
请把下面的中文翻译成英文，保留数值、比较条件和不确定性。只输出译文。

在使用相同训练数据的条件下，加入重排序模块后，答案准确率提高了 2.1 个百分点。
该模块在低资源设置下可能有效，仍需更多实验验证。
~~~

<a id="prompt-coding-task-brief"></a>

### 把编程需求讲清楚

~~~text
请把下面的需求整理成一段可交给编码 AI 的任务说明，写清输入、输出和验收方式。

现有项目使用 Python。我想把文件夹中的 Markdown 笔记导出成一个 CSV。
每份笔记占一行，记录文件名和第一个一级标题。没有一级标题时，标题列留空。
CSV 需要能用 Excel 打开。
~~~

<a id="prompt-paper-figure-brief"></a>

### 准备论文模型图

~~~text
请根据下面的方法规划一张论文模型图。列出模块、箭头方向和图内英文标签，区分训练与推理。
最后给出一段可直接发给绘图 AI 的提示词。

训练时，用问题、正负证据段落和排序损失训练重排序模型。
推理时，为每个问题从语料库检索 20 个候选段落，用训练好的重排序模型打分。
得分最高的 5 个段落和问题一起输入生成模型，得到答案。
~~~

更多模板见 [原始提示词集合](prompts/original-prompts.md)。文件上传、联网检索等能力由所用工具提供。

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
