---
name: academic-language-polish
description: "润色英文学术段落，理清句间逻辑并保持术语一致。"
metadata:
  source-records: "R013, R014"
---

# 学术语言润色

根据用户的任务选用对应的提示词，代入用户提供的材料执行。

## 润色英文学术段落

来源见原表 R013。

````text
Below is a paragraph from an academic paper. Rephrase it to meet academic writing standards and improve spelling, grammar, clarity, concision, and overall readability.

Paragraph:
[Paste the paragraph here.]
````

**怎么用**

把最后一行换成自己的英文段落再发送。例如可以填入 “The purpose of this step is to make a selection of the passages that are useful for answering the question.”

## 理清句间逻辑，保持术语一致

来源见原表 R014。

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

## 参考材料

[来源说明](SOURCE.md) · [原表提示词与经验](references/source-prompts.md)
