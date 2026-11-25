# 原始提示词与可复制任务说明

原文来自 CSV，保留措辞和占位符。复制后替换自己的材料。整理后的通用技能见 [Skills 列表](../skills/README.md)。

## R001 · NotebookLM：多论文比较

[完整条目](../catalog/entries/R001.md)

- [比较五篇论文，找出研究空白](../README.md#option-r001-compare)

原表具体用法

````text
输入下列提示词：“Compare these 5 papers and identify research gaps”，并选择或上传所需要检索的论文
````

## R002 · Gemini / ChatGPT：按条件找论文

[完整条目](../catalog/entries/R002.md)

- [按领域、方向、年份和会议找论文](../README.md#option-r002-search)

原表具体用法

````text
输入提示词，“帮我查找xxx领域xxx方向，在xxx年份发表在xxx会议的论文”
````

## R007 · 智谱清言：论文精读

[完整条目](../catalog/entries/R007.md)

- [概括一篇论文的优缺点](../README.md#option-r007-strengths)
- [总结论文的后续研究方向](../README.md#option-r007-directions)

原表具体用法

````text
搜索智谱清言，点击阅读论文，上传论文的PDF或word文件，即可整理出对应论文大纲。也可以输入prompt ,诸如“概括文献的优缺点”“总结后续研究拓展方向”等。
````

## R008 · WorkBuddy：检索并整理论文

[完整条目](../catalog/entries/R008.md)

- [检索符合条件的论文、下载并整理大纲](../README.md#option-r008-collect)

原表具体用法

````text
在workbuddy中的skill中选择academic research和agent browser，然后在交互页面中输入你的要求，例如“我需要一个XXX领域的paper，最好使用了XXXX技术，发表时间在xxxx年的A会上，请你帮我检索一下，并将符合的paper下载到XXXX，并整理一个总的大纲给我”
````

## R009 · DeepSeek / Kimi：论文总结与讨论

[完整条目](../catalog/entries/R009.md)

- [总结论文思路和方法，并给出原文依据](../README.md#option-r009-evidence)

原表具体用法

````text
上传论文文件，将具体需求告诉大模型，可以要求其提供原文中的具体依据（提升模型总结的准确性）
````

原表用途

````text
总结提炼论文思路、方法，可以与其讨论确定论文方法和相关细节
````

## R010 · Method 逻辑与术语统一提示词

[完整条目](../catalog/entries/R010.md)

- [按已有定义统一符号，检查方法逻辑](../README.md#option-r010-method)

原表具体用法

````text
先输入待整理的论文，并输入下列提示词：“名词定义和解释：请把这个小节的符号和定义都按照我们（上面讨论好的/Section...）形式化表示更换，注意要保持名词定义的一致性。再次检查逻辑gap，用常用的表达常用词，尽量不要提出新的名词，提出了就要解释清楚”
````

## R013 · 学术段落润色提示词

[完整条目](../catalog/entries/R013.md)

- [润色英文学术段落](../README.md#option-r013-polish)

原表具体用法

````text
先输入待整理的论文，并输入下列提示词：“Below is a paragraph from an academic paper. Rephrase the writing to meet the academic style,improve the spelling, grammar, clarity, concision and overall readability. Paragraph:"
````

## R014 · 清晰表达与固定术语提示词

[完整条目](../catalog/entries/R014.md)

- [理清句间逻辑，保持术语一致](../README.md#option-r014-clarity)

原表具体用法

````text
先输入待整理的论文，并输入下列提示词：“Write like a careful NLP student who wants peers and advisors to understand the paper.
Keep the logic explicit and smooth. Make the bridge between sentences visible instead of assuming the reader will fill it in.
Use common expressions, common words, and simple sentence structures by default. Only use uncommon terms or longer sentences when they are needed for technical precision.
Keep Abstract, Conclusion, and result discussion informative. Every sentence should contribute evidence, explanation, or a bounded claim.
Keep one canonical term for one concept. Method names, modules, datasets, metrics, and scores should not be renamed across the summary unless the scope change is real and made explicit.
Every self-defined term must be followed immediately by a plain explanation. If a term cannot be explained cleanly, do not use it.
Avoid long or showy sentences. Every sentence should carry real information."
````

## R016 · Trae：基于项目的辅助编程

[完整条目](../catalog/entries/R016.md)

- [结合项目文件修改代码](../README.md#option-r016-project-files)

原表具体用法

````text
首先上传项目中需要改写或者参考的代码文件，指定好代码的输入输出，描述清楚希望代码实现的功能，随后选择模型（效果最好的为GLM，KIMI2.6，但是可能要排队），得到结果。
````

## R020 · OpenAI Codex：需求拆解后实现

[完整条目](../catalog/entries/R020.md)

- [先拆解需求，再交给编码助手实现](../README.md#option-r020-break-down)

原表具体用法

````text
可在IDE中安装插件，也可直接安装官方软件
````

原表使用经验

````text
功能强大，但在设计提示词时注意任务拆解，可以先将实现的需求交给大模型梳理，生成提示词，再交给CodeX分点实现
````

## R025 · 编程提示词的六项需求说明

[完整条目](../catalog/entries/R025.md)

- [用六项信息说明编程需求](../README.md#option-r025-brief)

原表具体用法

````text
在利用大模型写代码时，不要只告诉它你想要什么，重点是告诉他：1、你想实现的功能。2、可用的信息。3、存在哪些限制。4、希望优先考虑什么。5、希望能避免什么。6、希望以什么方式进行回答
````

## R026 · 研究想法早期讨论提示词

[完整条目](../catalog/entries/R026.md)

- [讨论早期研究想法的逻辑和改进方向](../README.md#option-r026-idea)

原表具体用法

````text
使用的prompt：“假设你是XXXX领域的专家，现在我有一个关于XXXX的idea，主要内容是XXXXX，请你帮我检查上述的内容是否存在逻辑不严谨或可改进的地方”
````

## R027 · ChatGPT：方法与创新性讨论

[完整条目](../catalog/entries/R027.md)

- [讨论初稿中的创新性和潜在质疑](../README.md#option-r027-draft)

原表具体用法

````text
将论文文件传给llm，根据具体需求写提示词即可，可以根据具体需求的难度、特点，选择“思考一下”等选项
````

原表用途

````text
可以初步评估方法创新性、方法可能存在的问题、审稿人可能质疑的地方、方法可完善的地方及调整方法等
````

## R031 · 通用会议模拟审稿提示词

[完整条目](../catalog/entries/R031.md)

- [按会议模板模拟审稿并评分](../README.md#option-r031-review)
- [收到初审意见后，追问更多不足](../README.md#option-r031-followup)

原表具体用法

````text
使用prompt：Please help me review this paper and output the review comments in the following format.
* Overall Review
Please briefly summarize the main points and contributions of this paper.
xxx
* Paper Strength
Please provide a list of the strengths of this paper, including but not limited to: innovative and practical methodology, insightful empirical findings or in-depth theoretical analysis,
well-structured review of relevant literature, and any other factors that may make the paper valuable to readers. (Maximum length: 2,000 characters)
(1)xxx
(2)xxx
(3)xxx
* Paper Weakness
Please provide a numbered list of your main concerns regarding this paper (so authors could respond to the concerns individually).
These may include, but are not limited to: inadequate implementation details for reproducing the study, limited evaluation and ablation studies for the proposed method,
correctness of the theoretical analysis or experimental results, lack of comparisons or discussions with widely-known baselines in the field, lack of clarity in exposition,
or any other factors that may impede the reader's understanding or benefit from the paper. Please kindly refrain from providing a general assessment of the paper's novelty without providing detailed explanations. (Maximum length: 2,000 characters)
(1)xxx
(2)xxx
(3)xxx
* Questions To Authors And Suggestions For Rebuttal
Please provide a numbered list of specific and clear questions that pertain to the details of the proposed method, evaluation setting, or additional results that would aid in supporting the authors' claims.
The questions should be formulated in a manner that, after the authors have answered them during the rebuttal, it would enable a more thorough assessment of the paper's quality. (Maximum length: 2,000 characters)
*Overall score (1-10)
The paper is scored on a scale of 1-10, with 10 being the full mark, and 6 stands for borderline accept. Then give the reason for your rating.
xxx
````

原表使用经验

````text
如果想获取比较严格的建议，想了解更多潜在的不足，可以进一步追问：Please list more shortcomings of this paper from all aspects
````

## R033 · 只改错误的 typo 检查提示词

[完整条目](../catalog/entries/R033.md)

- [只改拼写和语法错误](../README.md#option-r033-proofread)

原表具体用法

````text
输入提示词，“帮我检查下面的论文中的typo问题，包括语法、句法、时态、单复数形式等。初次之外，不要修改其他内容，不要对原文的表达进行修改。”
````

## R035 · 保留原意的中文转英文提示词

[完整条目](../catalog/entries/R035.md)

- [保留原意和已有英文术语的中译英](../README.md#option-r035-translate)

原表具体用法

````text
先输入待翻译论文段落中文，并输入提示词：将上述中文翻译成英文，要求： 1. 不要丢失和增加任何意思和逻辑！！！！ 2.要用最直观最常用的英文单词，不要用晦涩不常用的英文单词 3.尽量不要使用被动语态 4.用词符合顶级学术会议习惯 5. 多去分析和揣测我给的中文上的逻辑，保证翻译的英文除了在内容上保持一致，逻辑也要保持一致 6. 我写成英文的地方就不要动了！7. 语法句式尽量精炼
````

## R036 · Word 纯文本学术翻译提示词

[完整条目](../catalog/entries/R036.md)

- [适合 Word 的英文稿和中文直译](../README.md#option-r036-word)

原表具体用法

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

## R038 · 模型图：先整理结构再生成图像

[完整条目](../catalog/entries/R038.md)

- [把论文方法整理成 VISUAL SCHEMA，再生成模型图](../README.md#option-r038-visual-schema)

原表具体用法

````text
要先让具备强逻辑理解能力的 LLM（如 Gemini 3 Pro、GPT-5、Claude 4.5 等），将论文的算法或方法结构转化为 [VISUAL SCHEMA] 蓝图。这一步类似于让 AI “看懂”你论文的逻辑，并输出清晰的视觉结构指令。然后通过绘图模型（如 Nano-Banana Pro）将上一步生成的蓝图转化为像素级视觉成品。虽然AI生成的图片有AI味，但是可以给自己提供绘图灵感，比如整体模型布局，配色等等。吸取其中的优点，自己再画一份模型图
````

## 外部提示词库

- Ai-prompt 写作与绘图提示词库 · [查看原文](https://github.com/Zhongxuanx/Ai-prompt)
- Awesome AI Research Writing · [查看原文](https://github.com/Leey21/awesome-ai-research-writing)
- Strict & Precise 严格审稿提示词 · [查看原文](https://github.com/kody-black/The-Strict-Precise-AI-Academic-Reviewer)
- Academic AI Prompt 科研提示词库 · [查看原文](https://github.com/bohyy/academic-ai-prompt)
