---
name: paper-peer-review
description: "按会议模板模拟审稿并评分，或在收到审稿意见后继续追问。"
metadata:
  source-records: "R027, R028, R029, R030, R031"
---

# 论文模拟审稿

根据用户的任务选用对应的提示词，代入用户提供的材料执行。

## 按会议模板模拟审稿并评分

来源见原表 R031。

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

## 收到初审意见后，追问更多不足

来源见原表 R031。

````text
Please list more shortcomings of this paper from all aspects.
````

**怎么用**

收到第一轮审稿意见后，在同一个对话中直接发送上面的英文追问。例如初审只谈了数据集和基线时，可以用它继续查找其他方面的不足。

## 讨论初稿中的创新性和潜在质疑

据原表 R027 的用法整理。

````text
请阅读我的论文初稿，评估方法的创新性。指出方法可能存在的问题、审稿人可能提出的质疑，以及可以如何改进。
````

**怎么用**

上传包含方法和实验的论文初稿后发送上面的提示词。例如研究的是检索模型，可以再写一句「我尤其想知道，用查询长度决定检索数量这一点，和已有方法有什么实质差异？」

## 参考材料

[来源说明](SOURCE.md) · [原表提示词与经验](references/source-prompts.md)
