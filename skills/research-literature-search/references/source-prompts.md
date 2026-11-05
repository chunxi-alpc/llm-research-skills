# 文献检索：原表提示词与经验

此文件保留来源材料，供需要时查阅。当前技能的执行要求以 SKILL.md 为准；原表中的价格、额度、模型版本和个人评价是填写时的记录。

## R002 · Gemini / ChatGPT：按条件找论文

原 CSV 逻辑记录：3。

### 原始入口

````text
Gemini(https://gemini.google.com/)、GPT(https://chatgpt.com/)网页版
````

### 原始使用方法或提示词

````text
输入提示词，“帮我查找xxx领域xxx方向，在xxx年份发表在xxx会议的论文”
````

### 原表使用经验

````text
结合GPT、Gemini的强大知识库，基本可以按要求找到目标论文，如果没有已发表的相关论文，甚至会在预印本数据库（e.g., arxiv）找相关论文
````


## R003 · RefCheck.ai：BibTeX 引文检查

原 CSV 逻辑记录：4。

### 原始入口

````text
https://github.com/HuaHenry/RefCheck_ai
````

### 原始使用方法或提示词

````text
按照网站要求步骤操作即可
````

### 原表使用经验

````text
RefCheck.ai用于验证 BibTeX 引用格式，并识别可疑或不一致的引用。可上传 .bib 文件（或直接粘贴 BibTeX 内容），在浏览器中实时查看验证流程，并获得一份结构化报告——该报告会突出显示不匹配的字段（例如标题/作者/年份），并推荐来自可信学术索引的最佳匹配结果。
````


## R004 · Wispaper：关键词文献检索

原 CSV 逻辑记录：5。

### 原始入口

````text
https://www.wispaper.ai/
````

### 原始使用方法或提示词

````text
按照网站要求步骤操作即可，可自定义相关度和文献年份、出处
````

### 原表使用经验

````text
提供文献精准来源，并且自动生成Ai摘要（部分文献可能为早期Arxiv预印版，引用需要甄别出处）
````


## R005 · AMiner：学术检索与研究趋势

原 CSV 逻辑记录：6。

### 原始入口

````text
https://www.aminer.cn/
````

### 原始使用方法或提示词

````text
可以在网站直接检索，也可以使用对应的skills接入Agent使用
````

### 原表使用经验

````text
AMiner 作为 AI 赋能的科技情报挖掘平台，可高效追踪领域热点、了解领域内大牛、分析研究趋势
````


## R008 · WorkBuddy：检索并整理论文

原 CSV 逻辑记录：9。

### 原始入口

````text
workbuddyhttps://www.codebuddy.cn/
````

### 原始使用方法或提示词

````text
在workbuddy中的skill中选择academic research和agent browser，然后在交互页面中输入你的要求，例如“我需要一个XXX领域的paper，最好使用了XXXX技术，发表时间在xxxx年的A会上，请你帮我检索一下，并将符合的paper下载到XXXX，并整理一个总的大纲给我”
````

### 原表使用经验

````text
可以快速找文献，以目前使用经历来看，找到的文献都是真实准确的，其中还有很多其他skill可供使用，但是做PPT之类的功能比较差
````
