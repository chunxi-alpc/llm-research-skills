---
name: paper-figure-brief
description: "根据论文方法整理 VISUAL SCHEMA，再交给绘图模型生成模型图。"
metadata:
  source-records: "R038, R040, R050"
---

# 论文模型图

根据用户的任务选用对应的提示词，代入用户提供的材料执行。

## 把论文方法整理成 VISUAL SCHEMA，再生成模型图

据原表 R038 的用法整理。

````text
请把下面的论文方法整理成一份可直接交给绘图模型的说明，以 [VISUAL SCHEMA] 开头。写清方法包含哪些模块、各模块怎样连接，以及如何安排这些模块，让读者能沿着图看懂处理流程。

[粘贴论文的方法段落或算法描述]
````

**怎么用**

将末行替换为“检索器先返回 20 个段落，重排序模型选出其中 5 段，生成模型结合问题和这 5 段作答。”把提示词发给 AI，再把它生成的整份 [VISUAL SCHEMA] 交给绘图模型生成模型图。

## 参考材料

[来源说明](SOURCE.md) · [原表提示词与经验](references/source-prompts.md)

[绘图说明模板](references/visual-schema.md)
