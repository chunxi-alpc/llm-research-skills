# LLM 辅助科研资料与 Skills

找论文、读论文、修改论文、准备模型图、整理编程需求——从你现在要做的一件事开始。

**[按任务选技能](#choose)** · **[下载 10 个技能合集](downloads/research-skills-starter.zip?raw=true)** · **[复制完整技能提示词](#prompts)** · [按类别找资料](#resources)

这里有 **10 个科研技能、53 条工具与使用经验**。Skill 是可重复使用的任务说明和配套参考文件，供支持 Skills 的 AI 工具读取。如果平时只用聊天网页，可以直接复制提示词。

**第一次使用？** 从 [把论文写得更清楚](#start) 开始，看看如何用技能改进自己的论文段落。

<a id="choose"></a>

## 你现在想做什么？

点击下载旁的「复制完整提示词」，再点代码块右上角的复制按钮，即可把全文粘贴到 AI 对话中。

| 我想…… | 可以得到什么 | 下载与使用 |
|---|---|---|
| 找某个方向的论文 | 按主题、年份和会议整理的论文清单，附来源链接 | [下载 ZIP](downloads/individual/research-literature-search.zip?raw=true) · [复制完整提示词](#prompt-research-literature-search) · [用法](skills/research-literature-search/SKILL.md) |
| 读懂论文、比较几篇方法 | 问题与方法梳理、原文依据、多论文对比表 | [下载 ZIP](downloads/individual/research-paper-reading.zip?raw=true) · [复制完整提示词](#prompt-research-paper-reading) · [用法](skills/research-paper-reading/SKILL.md) |
| 把论文写得更清楚 | 保留研究事实的修订段落和重要修改说明 | [下载 ZIP](downloads/individual/academic-language-polish.zip?raw=true) · [复制完整提示词](#prompt-academic-language-polish) · [用法](skills/academic-language-polish/SKILL.md) |
| 检查 Method 是否讲通 | 逻辑问题定位、符号定义与术语统一建议 | [下载 ZIP](downloads/individual/method-logic-check.zip?raw=true) · [复制完整提示词](#prompt-method-logic-check) · [用法](skills/method-logic-check/SKILL.md) |
| 讨论研究想法是否可行 | 关键假设、优先改进方向和小规模验证建议 | [下载 ZIP](downloads/individual/research-idea-discussion.zip?raw=true) · [复制完整提示词](#prompt-research-idea-discussion) · [用法](skills/research-idea-discussion/SKILL.md) |
| 投稿前模拟审稿 | 有原文依据的优点、问题和优先修改建议 | [下载 ZIP](downloads/individual/paper-peer-review.zip?raw=true) · [复制完整提示词](#prompt-paper-peer-review) · [用法](skills/paper-peer-review/SKILL.md) |
| 只改拼写和语法错误 | 纠错后的文本和修改清单，正确表达保持原样 | [下载 ZIP](downloads/individual/academic-proofreading.zip?raw=true) · [复制完整提示词](#prompt-academic-proofreading) · [用法](skills/academic-proofreading/SKILL.md) |
| 翻译中英文学术段落 | 保留原意、逻辑、数值和术语的译文 | [下载 ZIP](downloads/individual/academic-translation.zip?raw=true) · [复制完整提示词](#prompt-academic-translation) · [用法](skills/academic-translation/SKILL.md) |
| 把编程需求讲清楚 | 可交给编码工具的任务说明和完成标准 | [下载 ZIP](downloads/individual/coding-task-brief.zip?raw=true) · [复制完整提示词](#prompt-coding-task-brief) · [用法](skills/coding-task-brief/SKILL.md) |
| 准备论文模型图 | 模块与箭头说明、布局建议、可复制的绘图提示词 | [下载 ZIP](downloads/individual/paper-figure-brief.zip?raw=true) · [复制完整提示词](#prompt-paper-figure-brief) · [用法](skills/paper-figure-brief/SKILL.md) |

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

**找不到“导入技能”？** 可以先用 [下方的完整技能提示词](#prompts)，或查看 [安装指南](docs/getting-started.md)。

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

## 完整技能提示词

每个技能的第一个代码块都收录了对应的 `SKILL.md` 全文。把全文和你的任务材料一起发给 AI，或展开下方的使用示例直接试用。

<a id="prompt-research-literature-search"></a>

### 找某个方向的论文

[查看技能文件](skills/research-literature-search/SKILL.md) · [配套参考材料](skills/research-literature-search/references/)

<!-- BEGIN skills/research-literature-search/SKILL.md -->

````text
---
name: research-literature-search
description: 按研究主题、年份和会议或期刊检索文献，给出可追溯的论文清单与相关性说明。适用于找论文、补充相关工作和追踪研究方向。
metadata:
  source-records: "R002, R003, R004, R005, R008"
---

# 文献检索

## 适用任务与输入

输入研究问题或关键词，可补充年份范围、会议或期刊、语言、已有论文和希望找到的数量。先利用已有信息开始检索；只有缺失信息会明显改变方向时才追问。

## 处理方法

1. 将问题拆成对象、方法和目标，形成少量中英文检索词及同义词。按用户给出的年份和发表范围检索。
2. 使用当前环境可用的联网检索或学术数据库。优先打开论文原文、出版社、会议论文集或预印本页面，核对标题、作者、年份和入口。
3. 为每篇论文说明与问题的具体联系。区分正式发表版本与预印本；同一论文多个版本合并列出，并保留正式版本入口。
4. 没有匹配结果时说明哪些条件没有匹配，再给出明确标注的相近候选。无法联网时，提供检索式和待查线索，不把记忆中的条目当作已核实结果。

## 输出要求

先给检索范围和使用的检索词，再给表格：论文题目、作者、年份与发表状态、来源链接、相关性、值得阅读的部分。数量按需求决定，不用虚构条目凑数。需要 BibTeX 时，只使用已核实的元数据。

## 调用示例

> 使用 research-literature-search，查找 2024—2026 年 ACL/EMNLP 关于检索增强生成中证据选择的论文，先给最相关的 8 篇，标明正式发表版本。

## 来源

本表制作的技能，依据原表检索及引文检查经验整理。需要原始说法时阅读 [原表提示词与经验](references/source-prompts.md)。联网能力由所用 Agent 提供。
````

<!-- END skills/research-literature-search/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请联网查找 2022—2025 年发表在 ACL、EMNLP 和 NAACL 上的论文，主题是检索增强生成中的证据重排序。
选出最相关的论文，最多 5 篇。用表格给出题目、作者、年份、发表会议、原文链接和证据重排序方法。
请用会议论文集或论文主页核对发表信息。
~~~

示例来源见 [按条件找论文](catalog/entries/R002.md)。

</details>

<a id="prompt-research-paper-reading"></a>

### 读懂论文、比较几篇方法

[查看技能文件](skills/research-paper-reading/SKILL.md) · [配套参考材料](skills/research-paper-reading/references/)

<!-- BEGIN skills/research-paper-reading/SKILL.md -->

````text
---
name: research-paper-reading
description: 基于用户提供的论文做精读、方法梳理和多论文对比，给出原文位置及研究差异。适用于读论文、比较方法和整理相关工作。
metadata:
  source-records: "R001, R006, R007, R009, R041"
---

# 论文阅读与多论文对比

## 适用任务与输入

输入一篇或多篇可读取的论文、链接或摘录，并说明关注的问题。可补充阅读深度以及需要中文还是英文。只收到摘要时，按摘要可支持的信息回答。

## 处理方法

1. 识别每篇论文的问题、核心主张、方法、数据、实验和作者讨论的局限。
2. 按输入、关键模块、模块之间的关系、输出梳理方法；解释重要符号和术语。对公式说明它解决什么问题及变量含义。
3. 在重要结论后给出章节、页码、图表或原文短语等可找到的位置。分别说明作者的结论与自己的解释。
4. 对比多篇论文时，统一比较任务、假设、监督信息、方法和评测设置；不同数据或指标下的分数不直接排高低。
5. 总结已有方法共同覆盖的内容和仍未解释的问题。把可能的研究方向写成待验证的问题，避免仅因几篇论文未提及就断定领域空白。

## 输出要求

单篇输出问题概述、方法流程、主要证据、局限和阅读疑问。多篇增加对比表及可用于相关工作的综合段落。没有读到的细节标明“所提供内容未说明”，不要补造实验设置。

## 调用示例

> 使用 research-paper-reading，对比附件中的 5 篇论文，重点看证据选择模块和监督信号。给出对比表，并为关键差异附上原文章节或表号。

## 来源

本表制作的技能；[原表提示词与经验](references/source-prompts.md)保留多文档阅读、知识库和原文依据方面的使用经验。
````

<!-- END skills/research-paper-reading/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请对比下面两段示例摘要。用表格说明每种方法的输入、处理步骤、输出和评测指标。
请引用原句说明关键差异，并提出一个这两段摘要尚未回答的研究问题。

摘要 A
给定一个问题，系统检索 20 个候选段落，按检索分数选出 5 段供模型生成答案。实验报告答案准确率。

摘要 B
给定一个问题，系统检索 20 个候选段落，用重排序模型打分，再选出 5 段供模型生成答案。实验报告证据召回率。
~~~

示例来源见 [论文总结与讨论](catalog/entries/R009.md)和 [NotebookLM 多论文比较](catalog/entries/R001.md)。

</details>

<a id="prompt-academic-language-polish"></a>

### 把论文写得更清楚

[查看技能文件](skills/academic-language-polish/SKILL.md) · [配套参考材料](skills/academic-language-polish/references/)

<!-- BEGIN skills/academic-language-polish/SKILL.md -->

````text
---
name: academic-language-polish
description: 润色中英文学术段落，使句子简洁、衔接清楚、术语一致，同时保持研究事实和结论强度。适用于论文表达改写和可读性提升。
metadata:
  source-records: "R013, R014"
---

# 学术语言润色

## 适用任务与输入

输入待润色段落及其章节用途，可附上下文、目标会议或期刊、固定术语、偏好的文风。用户只要求拼写语法纠错时，仅做纠错，不扩大为风格改写。

## 处理方法

1. 先识别段落的主张和支撑材料，保留数值、引文、方法名称、比较对象、适用条件和不确定性程度。
2. 让相邻句子的关系清楚，必要时拆分长句或调整句序。优先使用常见词与通行学术表达。
3. 每个概念使用一个固定名称。自定义术语首次出现时给出简明解释，不为显得新颖而改名。
4. 去掉重复、空泛的评价和无作用的铺垫。保留影响结论理解的实验条件和限制。
5. 对缺少证据或逻辑不完整的位置提出具体建议，不能靠编写数据、引文或更强的结论补齐。

## 输出要求

给出可以直接使用的修订段落，以及少量影响理解的修改说明。若用户只要最终文本，就只输出文本。沿用用户提供的 LaTeX、Word 纯文本或 Markdown 格式。

## 调用示例

> 使用 academic-language-polish 润色下面的 Method 段落。保留所有公式和方法名称，用常见表达，最后说明最重要的三处改动。

## 来源

本表制作的技能；[原始英文润色提示词](references/source-prompts.md)对应原表 R013、R014。
````

<!-- END skills/academic-language-polish/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请润色下面的论文 Method 段落，修正语法和拼写，删减重复表达。让读者看清阈值的选取和使用过程。
保留数据划分、评价指标和术语。先给出修改后的英文段落，再用中文说明关键改动。

We use the validation set for the purpose of selecting a threshold.
The selection of the threshold is done by choosing the value that gives the highest F1 score.
After the threshold is selected, we use the selected threshold on the test set.
~~~

示例来源见 [学术段落润色](catalog/entries/R013.md)和 [清晰表达与固定术语](catalog/entries/R014.md)。

</details>

<a id="prompt-method-logic-check"></a>

### 检查 Method 是否讲通

[查看技能文件](skills/method-logic-check/SKILL.md) · [配套参考材料](skills/method-logic-check/references/)

<!-- BEGIN skills/method-logic-check/SKILL.md -->

````text
---
name: method-logic-check
description: 检查论文方法部分的输入输出、步骤逻辑、符号定义和术语一致性，并提出定位明确的修改。适用于 Method 审读与统一形式化表述。
metadata:
  source-records: "R010, R014"
---

# 方法逻辑与术语一致性检查

## 适用任务与输入

输入方法章节及其相关上下文，可附术语表、符号表、已讨论好的定义和模型图。已有定义优先；有冲突时指出冲突位置，不自行决定改变算法。

## 处理方法

1. 整理输入、输出、各步骤和中间变量，确认文字、公式与图中的依赖关系能对应起来。
2. 检查术语和符号是否在使用前定义，同一概念是否多名、同一符号是否多义，缩写是否有首次解释。
3. 检查每一步是否能由已有输入和前序结果得到，训练阶段与推理阶段的可用信息是否说清。
4. 对每个实际问题记录原文位置、读者会遇到的理解困难和最小修改建议。未提供的上下文可能包含定义时，明确所检查的范围。
5. 根据已有定义给出修订措辞。缺少关键定义或算法步骤时提出针对性问题，不自行增加模块和技术名词。

## 输出要求

输出“位置—问题—原因—建议”表，以及统一后的术语或符号表。用户要求修订正文时，给出相应段落；检查任务本身不自动改动文件。

## 调用示例

> 使用 method-logic-check 检查 Section 3。按 Section 2 的符号表统一记号，重点检查检索结果如何传给生成模块，以及新术语是否已解释。

## 来源

本表制作的技能；[原表提示词](references/source-prompts.md)保留 R010、R014 的术语与逻辑检查要求。
````

<!-- END skills/method-logic-check/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请按已有定义统一下面 Method 片段的术语和符号，并检查重排序结果如何传给生成模块。
用表格列出问题位置、原因和修改建议。缺少的定义或步骤请标为待确认。

已有定义
q 表示问题，D 表示候选段落集合，C 表示重排序后选出的段落集合。

Method 片段
给定问题 q，检索器返回候选段落集合 D。重排序模块为每个文档打分。
生成模块用文档集合 R 和问题 q 生成答案。
~~~

示例来源见 [Method 逻辑与术语统一](catalog/entries/R010.md)。

</details>

<a id="prompt-research-idea-discussion"></a>

### 讨论研究想法是否可行

[查看技能文件](skills/research-idea-discussion/SKILL.md) · [配套参考材料](skills/research-idea-discussion/references/)

<!-- BEGIN skills/research-idea-discussion/SKILL.md -->

````text
---
name: research-idea-discussion
description: 围绕已有研究想法讨论问题、假设、方法可行性及最小验证实验。适用于选题早期头脑风暴、检查思路和收敛改进方向。
metadata:
  source-records: "R026, R027, R046"
---

# 研究思路讨论

## 适用任务与输入

输入研究领域、希望解决的问题、已有想法和可用资源，可补充相关论文与初步结果。先回应当前想法，不默认把任务扩展为完整论文或大规模实验。

## 处理方法

1. 用简短文字复述问题、现有办法的不足和用户提出的变化，确认讨论对象一致。
2. 找出决定方法是否成立的关键假设，区分逻辑问题、需要证据的问题和表达问题，优先处理影响最大的部分。
3. 给出少量可比较的改进方向，说明各自理由、代价及预期观察。讨论已有思路时不无限扩展备选方案。
4. 为优先方向提出最小可行验证：比较什么、观察什么、什么结果支持或削弱假设。没有实验结果时不声称已经有效。
5. 判断新颖性需要对照文献；仅基于当前材料时，将新颖性写成待检索的判断。用户需要数学或算法方法候选时，按主题查阅 [方法目录](references/methods-directory.md)，无需逐项遍历。

## 输出要求

输出想法概括、主要问题、优先改进和下一步验证。问题按重要程度排序；多轮讨论围绕用户最新反馈推进。

## 调用示例

> 使用 research-idea-discussion，讨论下面的证据选择想法。数据和算力有限，请先找最关键的假设，并提出一个小实验验证它。

## 来源

本表制作的技能；[原表提示词与经验](references/source-prompts.md)对应 R026、R027、R046。方法目录为原表长文，按需参考，不作为必须采用的方法清单。
````

<!-- END skills/research-idea-discussion/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请以检索增强问答研究者的视角讨论下面的想法。指出有待验证的关键假设和优先改进的地方。
我想在检索增强问答中加入重排序。现有方法从 20 个候选段落中按检索分数选 5 段，新方法按重排序分数选 5 段。
我有 100 道带答案和证据标注的问题。请设计一个小规模验证实验，写清对照方法、指标和支持假设的结果。
~~~

示例来源见 [研究想法早期讨论](catalog/entries/R026.md)。

</details>

<a id="prompt-paper-peer-review"></a>

### 投稿前模拟审稿

[查看技能文件](skills/paper-peer-review/SKILL.md) · [配套参考材料](skills/paper-peer-review/references/)

<!-- BEGIN skills/paper-peer-review/SKILL.md -->

````text
---
name: paper-peer-review
description: 基于论文草稿及目标会议要求模拟同行评审，给出有原文依据的优点、问题和可执行修改。适用于投稿前检查、论文模拟审稿与修订排序。
metadata:
  source-records: "R027, R028, R029, R030, R031"
---

# 论文模拟审稿

## 适用任务与输入

输入论文草稿，可补充补充材料、目标会议或期刊的审稿模板、希望关注的部分以及是否评分。缺少全文时按可读范围评审。

## 处理方法

1. 先概括论文要解决的问题、方法和主要贡献，再检查论点与实验、理论或分析证据是否对应。
2. 从方法正确性、实验比较、消融、复现细节、相关工作和表达清晰度等与论文有关的角度找问题。
3. 每个主要问题指出具体位置、依据和影响，并给出可以回答的问题或可执行修改。区分确实存在的错误与尚缺信息。
4. 评论新颖性或缺少基线时，说明比较依据；未查证的相关论文作为待检索线索，不编造“已有工作证明”等结论。
5. 按目标会议模板输出；用户未提供模板时使用下述通用格式。严谨程度体现在依据和问题质量上，不靠严厉措辞或凑缺点数量。

## 输出要求

默认依次给出 Overall Review、Paper Strength、Paper Weakness、Questions To Authors And Suggestions For Rebuttal，以及优先修改建议。问题编号便于作者逐点回应。

用户要求评分时，先说明量表，再给分数和理由。若采用原表的 1—10 分模板，注明 6 分代表该模板中的 borderline accept；不把这套标尺当成所有会议的规则。原始模板见 [参考材料](references/source-prompts.md)。

## 调用示例

> 使用 paper-peer-review 审阅附件。重点看结论是否被实验支持，给出三个最优先的修改事项，不需要预测录用概率或打分。

## 来源

本表制作的技能，综合原表的模拟审稿流程和 R031 的英文审稿模板；外部严格审稿项目保留入口，未复制其未提供的全文提示词。
````

<!-- END skills/paper-peer-review/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请按下面的会议审稿格式评审这段演示稿件，重点判断实验能否支持论文的主张。

Overall Review 概括主要贡献。
Paper Strength 列出具体优点。
Paper Weakness 编号列出主要问题，指出对应句子。
Questions To Authors And Suggestions For Rebuttal 提出作者需要回答的问题和可执行的修改建议。
Overall score 给出 1—10 分及理由，6 分为临界接收。

演示稿件
我们在检索器后加入重排序模型，以提高跨领域问答准确率。
在一个领域的测试集上，加入重排序后，答案准确率从 60% 提高到 63%。
我们据此认为，重排序能在不同领域稳定提高问答准确率。
~~~

示例来源见 [通用会议模拟审稿模板](catalog/entries/R031.md)。

</details>

<a id="prompt-academic-proofreading"></a>

### 只改拼写和语法错误

[查看技能文件](skills/academic-proofreading/SKILL.md) · [配套参考材料](skills/academic-proofreading/references/)

<!-- BEGIN skills/academic-proofreading/SKILL.md -->

````text
---
name: academic-proofreading
description: 仅纠正学术文本中的拼写、语法、句法、时态和单复数错误，保留正确的原句表达。适用于 typo 检查、校对和用户要求不要润色的任务。
metadata:
  source-records: "R032, R033, R051"
---

# 拼写与语法纠错

## 适用任务与输入

输入待校对文本，可注明英式或美式拼写以及专业词表。适用于提交前找错，不承担风格润色或逻辑重写。

## 处理方法

1. 只修改可确定的拼写、语法、句法、时态、单复数、冠词、主谓一致和标点错误。
2. 保持正确内容原样，不替换正确但普通的词，不为简洁重写句子，不调整段落结构，不改研究含义。
3. 保留术语、变量、数值、引用、公式、代码与 LaTeX 命令。时态结合上下文判断，不把全部句子机械统一成一种时态。
4. 修改会涉及科学含义或有多种合理解释时，单列疑问并保留原文，不猜测作者本意。
5. 对照输入检查每处变化都对应一个明确错误。没有发现错误时说明“未发现需要修改的拼写或语法错误”。

## 输出要求

给出校对后的全文和简短的“原文—改正—错误类型”表。用户只要错误清单或纯文本时按其要求输出。不要附加风格优化建议。

## 调用示例

> 使用 academic-proofreading，只修正错误，不润色：Our method use two encoders. It improves accuracy by 2.1 points.

应只把 `use` 改为 `uses`，第二句保持原样。不得把 `improves` 换成更夸张的表达。

## 来源

本表制作的技能；[原表提示词与经验](references/source-prompts.md)保留 R033 的“不要修改其他内容”要求，以及 R032、R051 的纠错工具经验。
````

<!-- END skills/academic-proofreading/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请只修改下面英文的拼写和语法错误，包括句法、时态和单复数。保留其余表达、术语和数值。
先给出校对后的完整段落，再列出每处错误和改法。

Our model use two encoders to extract featuers.
It improves accuracy by 2.1 percentage points on the test set.
~~~

示例来源见 [只改错误的 typo 检查](catalog/entries/R033.md)。

</details>

<a id="prompt-academic-translation"></a>

### 翻译中英文学术段落

[查看技能文件](skills/academic-translation/SKILL.md) · [配套参考材料](skills/academic-translation/references/)

<!-- BEGIN skills/academic-translation/SKILL.md -->

````text
---
name: academic-translation
description: 在中文与英文之间翻译学术文本，保留原意、逻辑关系、术语、数值和结论强度。适用于论文段落翻译、中英对照与 Word 纯文本译稿。
metadata:
  source-records: "R035, R036"
---

# 中英文学术翻译

## 适用任务与输入

输入原文和目标语言，可补充术语表、上下文、需要保留的已有英文以及输出格式。按用户要求选择只输出译文、中英对照或 Word 纯文本。

## 处理方法

1. 逐句识别主张、因果、转折、条件、比较范围和不确定性，再组织目标语言表达。
2. 不增加或遗漏意思，不补写实验、理由、引用或结论；保留数字、否定、限定词、公式和引用标记。
3. 用常用而准确的学术词汇，保持概念名称一致。中文转英文时尽量简洁、优先自然的主动语态；科学含义和上下文优先于形式偏好。
4. 原稿已有的目标语言片段默认保留，尤其是方法名称和作者要求固定的句子。明显错误可另列说明，不擅自改写。
5. 原文含糊时保留可合理保留的歧义；影响含义时指出该处并请求必要澄清。不能把推测写成原文事实。
6. 对照原文检查是否遗漏条件、加强了结论或改变了因果方向。时态反映原文含义，不把已完成的特定事件强制改为现在时。

## 输出要求

默认仅给译文。用户要求核对时增加逐段对应文本。采用原表 Word 模式时，输出纯文本的 `Part 1 [English Draft]` 与 `Part 2 [Translation]`，第二部分为对应中文，正文不添加 Markdown；原有公式按用户的编辑格式保留。

## 调用示例

> 使用 academic-translation，把这段中文翻译为英文。保留已写成英文的模块名称，不增加解释，只输出适合粘贴到 Word 的译文。

核对例：“该方法在小样本设置下可能提高准确率。”可译为 “The method may improve accuracy in the few-shot setting.” 必须保留“可能”和“小样本设置”的范围。

## 来源

本表制作的技能；[两份原始翻译提示词](references/source-prompts.md)对应原表 R035、R036。原提示词中的 Word 输出偏好作为可选模式，保留原意的要求适用于两种翻译方向。
````

<!-- END skills/academic-translation/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请把下面的中文翻译成英文。用常见、精炼的学术表达，尽量用主动语态。
保留原意、逻辑、数值和已有的英文术语。只输出译文。

在使用相同训练数据的条件下，加入 evidence reranker 后，答案准确率提高了 2.1 个百分点。
该模块在低资源设置下可能有效，仍需更多实验验证。
~~~

示例来源见 [保留原意的中文转英文](catalog/entries/R035.md)。

</details>

<a id="prompt-coding-task-brief"></a>

### 把编程需求讲清楚

[查看技能文件](skills/coding-task-brief/SKILL.md) · [配套参考材料](skills/coding-task-brief/references/)

<!-- BEGIN skills/coding-task-brief/SKILL.md -->

````text
---
name: coding-task-brief
description: 将编程需求整理成可交给编码 Agent 的任务说明，包括功能、输入输出、现有代码、限制和验收方式。适用于编码前需求澄清与任务拆解。
metadata:
  source-records: "R016, R020, R025"
---

# 编程任务需求整理

## 适用任务与输入

输入想完成的功能、已有代码或目录说明，可补充输入输出示例、环境、限制、优先事项和希望避免的问题。本技能的交付是任务说明；只有用户另行要求实现时才进入编码。

## 处理方法

1. 提取六项内容：目标功能、可用信息、限制、优先事项、希望避免的行为、期望回答形式。
2. 写明输入输出、需要修改的范围和已有接口。保留用户指定的运行环境与资源条件，不自行添加功能或迁移环境。
3. 把较大需求拆成有先后关系的小任务，每项对应可观察的完成结果。简单需求不做多余拆分。
4. 将必要的未知信息列成短问题，其余可合理推定的事项注明假设，不因次要细节停止整理。
5. 根据任务提供一个输入输出示例或验收方法。修改已有项目时要求沿用现有结构，并明确与任务无关的文件不需要改动。

## 输出要求

给出可直接复制给编码 Agent 的完整任务提示词，包含目标、材料、输入输出、约束、任务顺序、验收和交付形式。问题与假设放在提示词之后，避免混入未经确认的实现要求。

## 调用示例

> 使用 coding-task-brief，帮我把“从一批论文 PDF 中提取标题和摘要并导出 CSV”整理成编码任务。已有 Python 项目，不能上传文档到外网，先不要写代码。

## 来源

本表制作的技能；[原表经验与提示要点](references/source-prompts.md)对应原表 R016、R020、R025。
````

<!-- END skills/coding-task-brief/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请把下面的需求整理成一段可交给编码 AI 的任务说明。写清功能、已有信息、限制、优先事项、应避免的行为和期望的回答形式，并给出验收方式。

现有项目使用 Python。我想把文件夹中的 Markdown 笔记导出成一个 CSV。
每份笔记占一行，记录文件名和第一个一级标题。没有一级标题时，标题列留空。
CSV 需要能用 Excel 打开。优先保证标题提取准确，保留原始笔记文件。交付时附上运行方法和验收结果。
~~~

示例来源见 [编程提示词的六项需求说明](catalog/entries/R025.md)。

</details>

<a id="prompt-paper-figure-brief"></a>

### 准备论文模型图

[查看技能文件](skills/paper-figure-brief/SKILL.md) · [配套参考材料](skills/paper-figure-brief/references/)

<!-- BEGIN skills/paper-figure-brief/SKILL.md -->

````text
---
name: paper-figure-brief
description: 将论文方法转化为模型图说明和可复制的绘图提示词，明确模块、箭头、布局与标注。适用于科研模型图规划；默认输出绘图说明而非图片文件。
metadata:
  source-records: "R038, R040, R050"
---

# 论文模型图说明与绘图提示词

## 适用任务与输入

输入论文方法段落、算法或现有草图，可补充目标版面、图中文字语言、参考风格和强调的贡献。默认产出可供绘图模型或人工绘制使用的说明。

## 处理方法

1. 提取输入、核心模块、中间表示、输出及其真实关系。区分训练流程、推理流程、数据流和损失约束。
2. 列出模块及其确切标签，明确每条箭头的起点、终点和含义。没有依据的模块与连接不添加到图中；关键关系缺失时指出需要补充的信息。
3. 安排阅读顺序、分组、对齐、留白和重点区域。颜色用于区分模块或阶段，同时用文字与线型保持可辨认性。
4. 给出图的结构说明，再写绘图提示词。提示词明确所有必要文字、布局、连接方向及样式，不能只写“漂亮、高级、学术风”。
5. 用方法原文逐项对照模块与箭头，列出生成或绘制后需要人工核对的标签与关系。图片转可编辑图形是后续工具步骤，不保证自动转换完全正确。

## 输出要求

输出三部分：方法结构表、以 `[VISUAL SCHEMA]` 开头的详细绘图说明、可复制的绘图提示词；可附一句图注建议。具体格式见 [绘图说明模板](references/visual-schema.md)。

本技能默认输出文本，不声称已经生成图片。用户明确要求成图且环境具备绘图工具时，再调用相应工具。统计图需要真实数值数据，不从方法描述中编造结果。

## 调用示例

> 使用 paper-figure-brief，把下面的 Method 转成双栏论文的模型图说明。图内用英文，区分训练和推理，给出可交给绘图模型的完整提示词。

## 来源

本表制作的技能；[原表绘图流程与经验](references/source-prompts.md)对应原表 R038、R040、R050。
````

<!-- END skills/paper-figure-brief/SKILL.md -->

<details>
<summary>使用示例（可直接发给 AI）</summary>

~~~text
请先把下面的方法整理成 [VISUAL SCHEMA] 绘图说明。列出模块、英文标签、箭头方向和布局，区分训练与推理。
再根据这份说明写一段可直接发给绘图 AI 的提示词。

训练时，用问题、正负证据段落和排序损失训练重排序模型。
推理时，为每个问题从语料库检索 20 个候选段落，用训练好的重排序模型打分。
得分最高的 5 个段落和问题一起输入生成模型，得到答案。
~~~

示例来源见 [模型图绘制流程](catalog/entries/R038.md)。

</details>

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
