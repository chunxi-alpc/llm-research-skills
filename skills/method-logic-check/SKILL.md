---
name: method-logic-check
description: "根据已有定义统一术语和符号，检查方法描述中的逻辑问题。"
metadata:
  source-records: "R010, R014"
---

# 方法逻辑与术语一致性检查

根据用户的任务选用对应的提示词，代入用户提供的材料执行。

## 按已有定义统一符号，检查方法逻辑

来源见原表 R010。

````text
请按[前文或章节]中的形式化表示，统一本小节的符号、术语和定义。检查推理或步骤之间是否有缺失的环节。尽量用常见表达。需要引入新术语时，请先解释清楚。
````

**怎么用**

例如把 [前文或章节] 换成「第 2 节」，在提示词下贴上「第 2 节定义 q 为查询、D 为候选文档集合。第 3 节写道：输入问题 x 后，我们对段落集合 C 排序。」一起发送。

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
