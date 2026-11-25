# LLM 辅助科研资料与 Skills

找论文、读论文、修改论文、准备模型图、整理编程需求——从你现在要做的一件事开始。

**[按任务选提示词](#choose)** · [下载 10 个技能合集](downloads/research-skills-starter.zip?raw=true) · [按类别找资料](#resources)

<a id="start"></a>

在下表选任务，展开想用的提示词，点代码块右上角复制。每条下方的「怎么用」演示该填哪些内容或上传什么材料。使用技能包时，请参阅[安装指南](docs/getting-started.md)。

<!-- BEGIN prompt catalog -->

<a id="choose"></a>

## 按任务选提示词

| 科研任务 | 提示词与下载 |
|---|---|
| 文献检索 | [选提示词](#prompt-research-literature-search) · [下载 ZIP](downloads/individual/research-literature-search.zip?raw=true) |
| 论文阅读与多论文对比 | [选提示词](#prompt-research-paper-reading) · [下载 ZIP](downloads/individual/research-paper-reading.zip?raw=true) |
| 学术语言润色 | [选提示词](#prompt-academic-language-polish) · [下载 ZIP](downloads/individual/academic-language-polish.zip?raw=true) |
| 方法逻辑与术语一致性检查 | [选提示词](#prompt-method-logic-check) · [下载 ZIP](downloads/individual/method-logic-check.zip?raw=true) |
| 研究思路讨论 | [选提示词](#prompt-research-idea-discussion) · [下载 ZIP](downloads/individual/research-idea-discussion.zip?raw=true) |
| 论文模拟审稿 | [选提示词](#prompt-paper-peer-review) · [下载 ZIP](downloads/individual/paper-peer-review.zip?raw=true) |
| 拼写与语法纠错 | [选提示词](#prompt-academic-proofreading) · [下载 ZIP](downloads/individual/academic-proofreading.zip?raw=true) |
| 学术翻译（中译英） | [选提示词](#prompt-academic-translation) · [下载 ZIP](downloads/individual/academic-translation.zip?raw=true) |
| 编程任务需求整理 | [选提示词](#prompt-coding-task-brief) · [下载 ZIP](downloads/individual/coding-task-brief.zip?raw=true) |
| 论文模型图 | [选提示词](#prompt-paper-figure-brief) · [下载 ZIP](downloads/individual/paper-figure-brief.zip?raw=true) |

<a id="prompts"></a>

## 提示词与使用示范

<a id="prompt-research-literature-search"></a>

### 文献检索

<details>
<summary>按领域、方向、年份和会议找论文</summary>

<a id="option-r002-search"></a>

````text
帮我查找[领域]中关于[研究方向]、发表于[年份]年[会议]的论文。
````

**怎么用**

把方括号换成自己的检索条件，例如直接发送「帮我查找自然语言处理中关于长文档摘要、发表于 2024 年 ACL 的论文。」

原表提示词 · [来源 R002](catalog/entries/R002.md)

</details>

<details>
<summary>检索符合条件的论文、下载并整理大纲</summary>

<a id="option-r008-collect"></a>

````text
请帮我检索[领域]中发表于[年份]年 A 类会议的论文，优先选择使用[技术]的工作。把符合条件的论文下载到[目录]，并整理一份总大纲。
````

**怎么用**

在 WorkBuddy 中启用 Academic Research 和 Agent Browser。可以直接发送「请帮我检索自然语言处理中发表于 2024 年 A 类会议的论文，优先选择使用对比学习的工作。把符合条件的论文下载到项目的 papers/ 文件夹，并整理一份总大纲。」

原表提示词 · [来源 R008](catalog/entries/R008.md)

</details>

<details>
<summary>比较五篇论文，找出研究空白</summary>

<a id="option-r001-compare-research-literature-search"></a>

````text
Compare these 5 papers and identify research gaps.
````

**怎么用**

在 NotebookLM 的来源列表中选中 5 篇要一起读的论文，例如 5 篇关于长文本检索的论文，然后在对话框发送上面的提示词。

原表提示词 · [来源 R001](catalog/entries/R001.md)

</details>

<a id="prompt-research-paper-reading"></a>

### 论文阅读与多论文对比

<details>
<summary>比较五篇论文，找出研究空白</summary>

<a id="option-r001-compare"></a>

````text
Compare these 5 papers and identify research gaps.
````

**怎么用**

在 NotebookLM 的来源列表中选中 5 篇要一起读的论文，例如 5 篇关于长文本检索的论文，然后在对话框发送上面的提示词。

原表提示词 · [来源 R001](catalog/entries/R001.md)

</details>

<details>
<summary>概括一篇论文的优缺点</summary>

<a id="option-r007-strengths"></a>

````text
请概括这篇论文的优点和缺点。
````

**怎么用**

上传想读的论文 PDF，例如一篇关于多语言摘要的论文，然后发送上面的提示词。

原表提示词 · [来源 R007](catalog/entries/R007.md)

</details>

<details>
<summary>总结论文的后续研究方向</summary>

<a id="option-r007-directions"></a>

````text
请根据这篇论文，总结后续可以拓展的研究方向。
````

**怎么用**

上传论文全文，或者把论文的讨论和局限性两节贴在提示词下面，一起发送给 AI。

原表提示词 · [来源 R007](catalog/entries/R007.md)

</details>

<details>
<summary>总结论文思路和方法，并给出原文依据</summary>

<a id="option-r009-evidence"></a>

````text
请总结这篇论文的研究思路和方法，并指出原文中支持这些概括的具体内容。
````

**怎么用**

上传论文 PDF 后发送上面的提示词。如果只想读懂其中一步，可以接着问「作者为什么需要重排序？请指出方法部分的依据。」

据原表用法整理 · [来源 R009](catalog/entries/R009.md)

</details>

<details>
<summary>检索符合条件的论文、下载并整理大纲</summary>

<a id="option-r008-collect-research-paper-reading"></a>

````text
请帮我检索[领域]中发表于[年份]年 A 类会议的论文，优先选择使用[技术]的工作。把符合条件的论文下载到[目录]，并整理一份总大纲。
````

**怎么用**

在 WorkBuddy 中启用 Academic Research 和 Agent Browser。可以直接发送「请帮我检索自然语言处理中发表于 2024 年 A 类会议的论文，优先选择使用对比学习的工作。把符合条件的论文下载到项目的 papers/ 文件夹，并整理一份总大纲。」

原表提示词 · [来源 R008](catalog/entries/R008.md)

</details>

<a id="prompt-academic-language-polish"></a>

### 学术语言润色

<details>
<summary>润色英文学术段落</summary>

<a id="option-r013-polish"></a>

````text
Below is a paragraph from an academic paper. Rephrase it to meet academic writing standards and improve spelling, grammar, clarity, concision, and overall readability.

Paragraph:
[Paste the paragraph here.]
````

**怎么用**

把最后一行换成自己的英文段落再发送。例如可以填入 “The purpose of this step is to make a selection of the passages that are useful for answering the question.”

原表提示词 · [来源 R013](catalog/entries/R013.md)

</details>

<details>
<summary>理清句间逻辑，保持术语一致</summary>

<a id="option-r014-clarity"></a>

````text
Write like a careful NLP student who wants peers and advisors to understand the paper.
Keep the logic explicit and smooth. Make the bridge between sentences visible instead of assuming the reader will fill it in.
Use common expressions, common words, and simple sentence structures by default. Only use uncommon terms or longer sentences when they are needed for technical precision.
Keep Abstract, Conclusion, and result discussion informative. Every sentence should contribute evidence, explanation, or a bounded claim.
Keep one canonical term for one concept. Method names, modules, datasets, metrics, and scores should not be renamed across the summary unless the scope change is real and made explicit.
Every self-defined term must be followed immediately by a plain explanation. If a term cannot be explained cleanly, do not use it.
Avoid long or showy sentences. Every sentence should carry real information.
````

**怎么用**

在提示词后粘贴待改段落。例如追加 “We use a passage ranker to select five passages. The evidence sorter then provides these passages to the generator. Here, both names refer to the same module.” 然后一起发送。

原表提示词 · [来源 R014](catalog/entries/R014.md)

</details>

Ai-prompt 写作与绘图提示词库 · [查看原文](https://github.com/Zhongxuanx/Ai-prompt)

Awesome AI Research Writing · [查看原文](https://github.com/Leey21/awesome-ai-research-writing)

<a id="prompt-method-logic-check"></a>

### 方法逻辑与术语一致性检查

<details>
<summary>按已有定义统一符号，检查方法逻辑</summary>

<a id="option-r010-method"></a>

````text
请按[前文或章节]中的形式化表示，统一本小节的符号、术语和定义。检查推理或步骤之间是否有缺失的环节。尽量用常见表达。需要引入新术语时，请先解释清楚。
````

**怎么用**

例如把 [前文或章节] 换成「第 2 节」，在提示词下贴上「第 2 节定义 q 为查询、D 为候选文档集合。第 3 节写道：输入问题 x 后，我们对段落集合 C 排序。」一起发送。

原表提示词 · [来源 R010](catalog/entries/R010.md)

</details>

<details>
<summary>理清句间逻辑，保持术语一致</summary>

<a id="option-r014-clarity-method-logic-check"></a>

````text
Write like a careful NLP student who wants peers and advisors to understand the paper.
Keep the logic explicit and smooth. Make the bridge between sentences visible instead of assuming the reader will fill it in.
Use common expressions, common words, and simple sentence structures by default. Only use uncommon terms or longer sentences when they are needed for technical precision.
Keep Abstract, Conclusion, and result discussion informative. Every sentence should contribute evidence, explanation, or a bounded claim.
Keep one canonical term for one concept. Method names, modules, datasets, metrics, and scores should not be renamed across the summary unless the scope change is real and made explicit.
Every self-defined term must be followed immediately by a plain explanation. If a term cannot be explained cleanly, do not use it.
Avoid long or showy sentences. Every sentence should carry real information.
````

**怎么用**

在提示词后粘贴待改段落。例如追加 “We use a passage ranker to select five passages. The evidence sorter then provides these passages to the generator. Here, both names refer to the same module.” 然后一起发送。

原表提示词 · [来源 R014](catalog/entries/R014.md)

</details>

<a id="prompt-research-idea-discussion"></a>

### 研究思路讨论

<details>
<summary>讨论早期研究想法的逻辑和改进方向</summary>

<a id="option-r026-idea"></a>

````text
假设你是[领域]的专家。我有一个关于[研究主题]的想法：[主要思路]。请帮我检查其中的逻辑，并指出可以改进的地方。
````

**怎么用**

填好三个位置后直接发送，例如「假设你是信息检索领域的专家。我想用查询长度决定检索多少篇文档：查询越长，就取越多文档。请帮我检查其中的逻辑，并指出可以改进的地方。」

原表提示词 · [来源 R026](catalog/entries/R026.md)

</details>

<details>
<summary>讨论初稿中的创新性和潜在质疑</summary>

<a id="option-r027-draft"></a>

````text
请阅读我的论文初稿，评估方法的创新性。指出方法可能存在的问题、审稿人可能提出的质疑，以及可以如何改进。
````

**怎么用**

上传包含方法和实验的论文初稿后发送上面的提示词。例如研究的是检索模型，可以再写一句「我尤其想知道，用查询长度决定检索数量这一点，和已有方法有什么实质差异？」

据原表用法整理 · [来源 R027](catalog/entries/R027.md)

</details>

<a id="prompt-paper-peer-review"></a>

### 论文模拟审稿

<details>
<summary>按会议模板模拟审稿并评分</summary>

<a id="option-r031-review"></a>

````text
Please help me review this paper and output the review comments in the following format.
* Overall Review
Please briefly summarize the main points and contributions of this paper.
...
* Paper Strength
Please provide a list of the strengths of this paper, including but not limited to: innovative and practical methodology, insightful empirical findings or in-depth theoretical analysis, well-structured review of relevant literature, and any other factors that may make the paper valuable to readers. (Maximum length: 2,000 characters)
(1)...
(2)...
(3)...
* Paper Weakness
Please provide a numbered list of your main concerns regarding this paper (so authors could respond to the concerns individually).
These may include, but are not limited to: inadequate implementation details for reproducing the study, limited evaluation and ablation studies for the proposed method, correctness of the theoretical analysis or experimental results, lack of comparisons or discussions with widely-known baselines in the field, lack of clarity in exposition, or any other factors that may impede the reader's understanding or benefit from the paper. Please kindly refrain from providing a general assessment of the paper's novelty without providing detailed explanations. (Maximum length: 2,000 characters)
(1)...
(2)...
(3)...
* Questions To Authors And Suggestions For Rebuttal
Please provide a numbered list of specific and clear questions that pertain to the details of the proposed method, evaluation setting, or additional results that would aid in supporting the authors' claims.
The questions should be formulated in a manner that, after the authors have answered them during the rebuttal, it would enable a more thorough assessment of the paper's quality. (Maximum length: 2,000 characters)
* Overall score (1-10)
The paper is scored on a scale of 1-10, with 10 being the full mark, and 6 stands for borderline accept. Then give the reason for your rating.
...
````

**怎么用**

上传要评审的论文全文，再把上面的英文模板原样发送。以附件 manuscript.pdf 为例，AI 会在审稿意见末尾给出 1–10 分和理由，模板中的 6 分表示临界接收。

原表提示词 · [来源 R031](catalog/entries/R031.md)

</details>

<details>
<summary>收到初审意见后，追问更多不足</summary>

<a id="option-r031-followup"></a>

````text
Please list more shortcomings of this paper from all aspects.
````

**怎么用**

收到第一轮审稿意见后，在同一个对话中直接发送上面的英文追问。例如初审只谈了数据集和基线时，可以用它继续查找其他方面的不足。

原表提示词 · [来源 R031](catalog/entries/R031.md)

</details>

<details>
<summary>讨论初稿中的创新性和潜在质疑</summary>

<a id="option-r027-draft-paper-peer-review"></a>

````text
请阅读我的论文初稿，评估方法的创新性。指出方法可能存在的问题、审稿人可能提出的质疑，以及可以如何改进。
````

**怎么用**

上传包含方法和实验的论文初稿后发送上面的提示词。例如研究的是检索模型，可以再写一句「我尤其想知道，用查询长度决定检索数量这一点，和已有方法有什么实质差异？」

据原表用法整理 · [来源 R027](catalog/entries/R027.md)

</details>

Strict & Precise 严格审稿提示词 · [查看原文](https://github.com/kody-black/The-Strict-Precise-AI-Academic-Reviewer)

<a id="prompt-academic-proofreading"></a>

### 拼写与语法纠错

<details>
<summary>只改拼写和语法错误</summary>

<a id="option-r033-proofread"></a>

````text
请检查下面论文段落中的拼写、语法、句法、时态和单复数错误。只修正这些错误，保留其余表达。
````

**怎么用**

在提示词下一行贴原文再发送。例如贴入 “Our method use two encoders.”，校对后应为 “Our method uses two encoders.”

原表提示词 · [来源 R033](catalog/entries/R033.md)

</details>

<a id="prompt-academic-translation"></a>

### 学术翻译（中译英）

<details>
<summary>保留原意和已有英文术语的中译英</summary>

<a id="option-r035-translate"></a>

````text
请把下面的中文段落翻译成英文。
1. 保留原文的全部含义和逻辑，避免增添或遗漏信息。
2. 选用直观、常见的英文词汇。
3. 尽量使用主动语态。
4. 用词符合本领域顶级学术会议的写作习惯。
5. 理清中文句子之间的逻辑关系，并在译文中准确体现。
6. 原文中已用英文写出的部分保持原样。
7. 句式尽量精炼。
````

**怎么用**

在提示词下贴入「我们先用 dense retriever 检索候选段落，再用重排序模型选出前五段。」一起发送。这样可以直接看出原有的英文术语 dense retriever 是否得到保留。

原表提示词 · [来源 R035](catalog/entries/R035.md)

</details>

<details>
<summary>适合 Word 的英文稿和中文直译</summary>

<a id="option-r036-word"></a>

````text
# Role
你是一位兼具顶尖科研写作专家与资深会议审稿人（ICML/ICLR/NeurIPS/ACL 等）双重身份的助手。你的学术品味极高，对逻辑漏洞和语言瑕疵零容忍。

# Task
请处理我提供的【中文草稿】，将其翻译并润色为适合 Word 编辑的【英文学术论文片段】。

# Constraints
1. 视觉与排版：
   - 绝对不要使用任何 Markdown 语法（包括但不限于 `###` 标题、`**` 加粗、`*` 斜体、`>` 引用或 ``` 代码块等）。
   - 请直接输出纯文本，以便于一键无缝复制到 Word 文档中，不会带入任何多余的排版符号。
   - 尽量少用引号，以免影响学术论文的视觉观感。

2. 风格与逻辑：
   - 要求逻辑严谨，用词准确，表达凝练连贯，尽量使用常见的单词，避免生僻词。
   - 尽量不要使用破折号（—），推荐使用从句或同位语替代。
   - 拒绝使用任何项目符号（Bullet points）或列表形式，必须使用连贯的段落表达。
   - 去除“AI味”，行文自然流畅，避免机械的连接词堆砌。

3. 时态规范：
   - 统一使用一般现在时描述方法、架构和实验结论。
   - 仅在明确提及特定历史事件时使用过去时。

4. 输出格式：
   - Part 1 [English Draft]：只输出翻译成英文后的内容本身。
     * 语言要求：必须是全英文。
     * 符号规范：直接输出标准文本符号（如 95%、model_v1、R&D 等），**切勿**进行类似 LaTeX 的斜杠转义。
     * 公式保留：Word 支持直接转换数学文本，请保留原草稿中的公式排版（如保留 $ 符号以界定公式范围），以数学形式的因果逻辑（$\because, \therefore, \implies$）串联推导过程。
   - Part 2 [Translation]：对应的中文直译（用于核对逻辑是否符合原意）。
   - 除以上两部分外，不要输出任何多余的对话、前缀说明或解释。

# Execution Protocol
在输出最终结果前，请务必在后台进行自我审查：
1. 审稿人视角：假设你是最挑剔的 Reviewer，检查是否存在过度排版、格式乱码、逻辑跳跃或未翻译的中文。
2. 立即纠正：针对发现的问题进行修改，确保最终输出的内容严谨、纯净且完全英文化。

# Input
[在此处粘贴你的中文草稿]
````

**怎么用**

把模板末尾的 [在此处粘贴你的中文草稿] 换成实际段落，例如「我们将训练集的 95% 用于训练 model_v1，其余样本用于验证。」发送后，把 Part 1 的英文复制到 Word，用 Part 2 的中文逐句核对原意。

原表提示词 · [来源 R036](catalog/entries/R036.md)

</details>

<a id="prompt-coding-task-brief"></a>

### 编程任务需求整理

<details>
<summary>结合项目文件修改代码</summary>

<a id="option-r016-project-files"></a>

````text
请参考我提供的项目文件，修改 [文件名]，实现 [功能]。程序的输入是 [输入内容和格式]，预期输出是 [结果和格式]。
````

**怎么用**

将现有的 `export_notes.py` 和一份 Markdown 笔记发给编程工具。把四个占位项依次填为 `export_notes.py`、提取笔记标题、一个存放 Markdown 笔记的文件夹、一张包含文件名和首个一级标题的 CSV 表，再发送提示词。

据原表用法整理 · [来源 R016](catalog/entries/R016.md)

</details>

<details>
<summary>先拆解需求，再交给编码助手实现</summary>

<a id="option-r020-break-down"></a>

````text
请梳理下面的开发需求，拆成可以逐项实现的任务，再写成一段能直接交给编码助手的提示词。

[粘贴开发需求]
````

**怎么用**

在末行填入“把文件夹中的 Markdown 笔记导出为 CSV。每行记录文件名和一级标题，没有标题就留空。”先发给 AI，再把生成的提示词交给 Codex 逐项实现。

据原表用法整理 · [来源 R020](catalog/entries/R020.md)

</details>

<details>
<summary>用六项信息说明编程需求</summary>

<a id="option-r025-brief"></a>

````text
请帮我实现 [想要的功能]。
可以使用 [已有文件、数据或接口]。
需要遵守 [限制条件]。
请优先考虑 [最重要的要求]。
请避免 [不希望出现的做法或结果]。
请用 [希望的回答或交付形式] 回复。
````

**怎么用**

要批量导出笔记标题，可以依次填入「导出笔记标题到 CSV」「已有的 Markdown 文件夹」「只用 Python 标准库」「准确识别一级标题」「避免改写笔记原文」「给出脚本和运行命令」。填好后整段发给编码助手。

据原表用法整理 · [来源 R025](catalog/entries/R025.md)

</details>

<a id="prompt-paper-figure-brief"></a>

### 论文模型图

<details>
<summary>把论文方法整理成 VISUAL SCHEMA，再生成模型图</summary>

<a id="option-r038-visual-schema"></a>

````text
请把下面的论文方法整理成一份可直接交给绘图模型的说明，以 [VISUAL SCHEMA] 开头。写清方法包含哪些模块、各模块怎样连接，以及如何安排这些模块，让读者能沿着图看懂处理流程。

[粘贴论文的方法段落或算法描述]
````

**怎么用**

将末行替换为“检索器先返回 20 个段落，重排序模型选出其中 5 段，生成模型结合问题和这 5 段作答。”把提示词发给 AI，再把它生成的整份 [VISUAL SCHEMA] 交给绘图模型生成模型图。

据原表用法整理 · [来源 R038](catalog/entries/R038.md)

</details>

Ai-prompt 写作与绘图提示词库 · [查看原文](https://github.com/Zhongxuanx/Ai-prompt)

### 综合科研提示词库

Academic AI Prompt 科研提示词库 · [查看原文](https://github.com/bohyy/academic-ai-prompt)

<!-- END prompt catalog -->

<a id="resources"></a>

## 按科研任务查找资料

按原表的 **12 个类别**查看提示词、工具和使用经验，共 53 条资料。

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
