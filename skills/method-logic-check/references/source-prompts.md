# 方法逻辑与术语一致性检查：原表提示词与经验

此文件保留来源材料，供需要时查阅。当前技能的执行要求以 SKILL.md 为准；原表中的价格、额度、模型版本和个人评价是填写时的记录。

## R010 · Method 逻辑与术语统一提示词

原 CSV 逻辑记录：11。

### 原始入口

````text
https://chatgpt.com/
````

### 原始使用方法或提示词

````text
先输入待整理的论文，并输入下列提示词：“名词定义和解释：请把这个小节的符号和定义都按照我们（上面讨论好的/Section...）形式化表示更换，注意要保持名词定义的一致性。再次检查逻辑gap，用常用的表达常用词，尽量不要提出新的名词，提出了就要解释清楚”
````


## R014 · 清晰表达与固定术语提示词

原 CSV 逻辑记录：15。

### 原始入口

````text
各种大模型
````

### 原始使用方法或提示词

````text
先输入待整理的论文，并输入下列提示词：“Write like a careful NLP student who wants peers and advisors to understand the paper.
Keep the logic explicit and smooth. Make the bridge between sentences visible instead of assuming the reader will fill it in.
Use common expressions, common words, and simple sentence structures by default. Only use uncommon terms or longer sentences when they are needed for technical precision.
Keep Abstract, Conclusion, and result discussion informative. Every sentence should contribute evidence, explanation, or a bounded claim.
Keep one canonical term for one concept. Method names, modules, datasets, metrics, and scores should not be renamed across the summary unless the scope change is real and made explicit.
Every self-defined term must be followed immediately by a plain explanation. If a term cannot be explained cleanly, do not use it.
Avoid long or showy sentences. Every sentence should carry real information."
````

### 原表使用经验

````text
改善大模型普遍存在长难句写作的弊端
````
