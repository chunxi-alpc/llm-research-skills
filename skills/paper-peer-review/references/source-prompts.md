# 论文模拟审稿：原表提示词与经验

此文件保留来源材料，供需要时查阅。当前技能的执行要求以 SKILL.md 为准；原表中的价格、额度、模型版本和个人评价是填写时的记录。

## R027 · ChatGPT：方法与创新性讨论

原 CSV 逻辑记录：28。

### 原始入口

````text
ChatGPT（https://chatgpt.com/）
````

### 原始使用方法或提示词

````text
将论文文件传给llm，根据具体需求写提示词即可，可以根据具体需求的难度、特点，选择“思考一下”等选项
````

### 原表使用经验

````text
个人觉得它提出的建议比大部分llm更有参考价值；但每天有免费上传文件数的限制、免费对话轮次的限制，可以将多个需求分点列出并一次传给大模型，节省对话次数
````


## R028 · Stanford Agentic Reviewer

原 CSV 逻辑记录：32。

### 原始入口

````text
Stanford Agentic Reviewer - Submit Paper
````

### 原始使用方法或提示词

````text
直接根据界面提示使用，无提示词
````

### 原表使用经验

````text
上传文件要求：上传10M以下，15页以下的PDF论文，主要是针对AI会议。

AI生成的审稿报告包括7个维度打分：原创性、重要性、论点支持、实验可靠性、清晰度、社区价值、上下文关联。最终合成1-10分的总分（针对ICLR等）。可操作修改建议：不是泛泛而谈，而是基于相关论文的比较，指出哪里可以改进。比如，“你的方法在基准测试上落后于最近的X论文，建议添加Y实验对比”。
````


## R029 · CSpaper：按会议模板审稿

原 CSV 逻辑记录：33。

### 原始入口

````text
CSpaper--https://cspaper.org/
````

### 原始使用方法或提示词

````text
首先选择待投的会议，然后选择推荐的大模型进行审稿
````

### 原表使用经验

````text
一个账号有免费三次机会，cspaper审稿模板基本和会议本身的审稿模板一致，针对AI会议。

对比斯坦福审稿AI，审稿结果在【形式上】会更符合想要投会议的要求，审稿意见也会更mean一些。因为cspaper次数有限，可以先用斯坦福多次审稿后，再使用cspaper进行终版辅助检查。
````


## R030 · Strict & Precise：严格审稿提示词

原 CSV 逻辑记录：34。

### 原始入口

````text
https://chatgpt.com/
提示词网站：https://github.com/kody-black/The-Strict-Precise-AI-Academic-Reviewer
````

### 原始使用方法或提示词

````text
在GPT上上传论文文件后，输入该提示词：（提示词见gihub网址内容）
````

### 原表使用经验

````text
审稿语气十分严厉，给出的意见非常的mean，可以作为主要修改的点，但不要因为过于严厉的审稿意见而灰心。
````


## R031 · 通用会议模拟审稿提示词

原 CSV 逻辑记录：35。

### 原始入口

````text
各种大模型
````

### 原始使用方法或提示词

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

### 原表使用经验

````text
如果想获取比较严格的建议，想了解更多潜在的不足，可以进一步追问：Please list more shortcomings of this paper from all aspects
````
