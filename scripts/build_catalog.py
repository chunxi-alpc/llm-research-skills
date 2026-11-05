"""Regenerate the catalogue from the unchanged CSV and the curation below."""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CSV_NAME = "LLM辅助科研资料和经验汇总-工作表1.csv"
FIELDS = ["category", "entry", "purpose", "usage", "experience"]

# Stable row IDs refer to nonempty content records, not physical CSV text lines.
CURATION = [
    ("NotebookLM：多论文比较", "literature", "上传或选择待比较论文，再提出跨论文对比与研究问题。", []),
    ("Gemini / ChatGPT：按条件找论文", "literature", "给出研究领域、方向、年份与会议条件，再核对返回论文的正式入口。", []),
    ("RefCheck.ai：BibTeX 引文检查", "literature", "按项目说明上传或粘贴 BibTeX，查看不匹配字段和推荐匹配结果。", []),
    ("Wispaper：关键词文献检索", "literature", "输入关键词，再按相关度、年份和出处筛选；区分预印本与正式版本。", []),
    ("AMiner：学术检索与研究趋势", "literature", "先在网站检索主题；需要 Agent 接入时，再按官方提供的技能或接口配置。", []),
    ("腾讯 ima：论文知识库", "reading", "安装客户端，建立知识库并上传已下载论文，再围绕文献提问。", []),
    ("智谱清言：论文精读", "reading", "使用论文阅读入口上传文件，要求提取问题、方法流程与局限。", []),
    ("WorkBuddy：检索并整理论文", "reading", "按原表经验选择 academic research 和 agent browser，给出论文条件、保存位置和大纲要求。", []),
    ("DeepSeek / Kimi：论文总结与讨论", "reading", "提供论文及具体问题，要求回答附上原文依据；多篇材料可做方法对比。", []),
    ("Method 逻辑与术语统一提示词", "writing", "同时提供方法段落与已确定的定义，要求检查逻辑衔接并统一符号。", []),
    ("Ai-prompt：写作与绘图提示词库", "writing", "打开仓库，按当前章节或绘图需求选择提示词并替换输入材料。", []),
    ("PaperDebugger：Overleaf 写作助手", "writing", "通过原表的浏览器扩展入口安装，按项目说明配置后在 Overleaf 使用。", []),
    ("学术段落润色提示词", "writing", "把待修改段落接在英文提示词之后，要求改善拼写、语法和可读性。", []),
    ("清晰表达与固定术语提示词", "writing", "把这段写作要求作为论文改写的风格说明，并提供需要修改的正文。", []),
    ("Awesome AI Research Writing", "writing", "按翻译、润色、图表或审稿等任务选择原仓库模板，再补齐论文材料。", []),
    ("Trae：基于项目的辅助编程", "coding", "提供相关代码、输入输出和目标功能，在项目上下文中让 Agent 实现或调试。", []),
    ("Claude Code：编码与调试", "coding", "按官方说明安装或启用 IDE 集成，在项目中给出明确的修改任务。", []),
    ("GitHub Copilot：IDE 编程助手", "coding", "在所用 IDE 安装对应集成，选择适合任务的聊天或 Agent 功能。", ["https://github.com/features/copilot"]),
    ("通义灵码：代码生成与解释", "coding", "按官方入口安装 IDE 插件，结合当前代码说明要实现或检查的逻辑。", ["https://lingma.aliyun.com/"]),
    ("OpenAI Codex：需求拆解后实现", "coding", "先明确输入输出与完成标准，再在项目中分任务交给 Codex 实现。", ["https://developers.openai.com/codex/"]),
    ("Cursor：在 IDE 中修改代码", "coding", "打开已有项目，提供任务与相关文件，在修改视图中查看结果。", ["https://cursor.com/"]),
    ("Karpathy Skills：编程原则", "coding", "按补充的原项目入口选择技能或项目规则形式；保留其四项编程原则。", ["https://github.com/multica-ai/andrej-karpathy-skills"]),
    ("Superpowers：开发流程技能套件", "coding", "下载完整套件，按原项目中对应 Agent 的说明安装并提交开发任务。", ["https://github.com/obra/superpowers"]),
    ("DeepSeek-TUI：终端编码工具", "coding", "原表记录了 npm 安装方式；使用前从项目入口查看当前安装与 API 配置说明。", ["https://github.com/Hmbown/DeepSeek-TUI"]),
    ("编程提示词的六项需求说明", "coding", "按功能、信息、限制、优先事项、避免事项和回答形式整理任务。", []),
    ("研究想法早期讨论提示词", "ideas-review", "给出领域、问题与想法，请模型先检查最关键的逻辑与改进空间。", []),
    ("ChatGPT：方法与创新性讨论", "ideas-review", "提供论文或方法说明，把需要讨论的创新性、潜在问题和改进要求列清。", []),
    ("Stanford Agentic Reviewer", "ideas-review", "在补充入口上传论文 PDF，按页面流程提交并查看反馈。", ["https://paperreview.ai/"]),
    ("CSpaper：按会议模板审稿", "ideas-review", "先选拟投会议，再按页面提示提交论文并选择可用模型。", []),
    ("Strict & Precise：严格审稿提示词", "ideas-review", "从原仓库获取提示词，连同论文交给模型；逐项核对意见与原文的对应关系。", []),
    ("通用会议模拟审稿提示词", "ideas-review", "提供论文并复制原表英文模板；需要时使用其评分量表。", []),
    ("Grammarly：拼写语法检查", "writing", "按平台的当前集成方式检查文本，再确认建议是否保持技术含义。", []),
    ("只改错误的 typo 检查提示词", "writing", "输入原文，明确只改拼写、语法、时态和单复数等错误，其他内容保留。", []),
    ("Turnitin 相关查重入口（原表）", "writing", "原表链接与使用条件保留在下方；正式使用时通过所在机构或官方入口确认服务。", ["https://www.turnitin.com/"]),
    ("保留原意的中文转英文提示词", "writing", "提供中文终稿及固定英文术语，要求翻译不增删含义和逻辑。", []),
    ("Word 纯文本学术翻译提示词", "writing", "复制完整模板并填入中文草稿，可得到英文段落和对应中文核对文本。", []),
    ("Academic AI Prompt：科研提示词集合", "reference", "按选题、文献综述或写作任务到原仓库选择模板。", []),
    ("模型图：先整理结构再生成图像", "figures", "先把方法转成 VISUAL SCHEMA，再交给有绘图功能的工具或用于人工绘制。", []),
    ("Nature Skills：科研技能套件", "reference", "从按名称补充的项目下载，按任务选择技能；需要时连同 nature-shared 使用。", ["https://github.com/Yuan1z0825/nature-skills"]),
    ("Edit Banana：图像转可编辑图形", "figures", "上传已有图像，查看转换结果，再在相应编辑器核对并调整组件。", []),
    ("Zotero + zotero-gpt", "reading", "先安装 Zotero，再按插件说明配置兼容版本和模型服务，围绕论文提问或整理笔记。", []),
    ("AI-Scientist：自动化科研项目", "ideas-review", "阅读原项目 README，了解研究模板、模型 API 与实验运行环境，再按需配置。", []),
    ("Scientific Manuscript Editor", "writing", "下载完整技能目录，在对应 Agent 中加载并提供论文材料与修改要求。", []),
    ("Humanizer：减少机械表达", "writing", "导入技能后提交段落；可按原表经验提供少量有代表性的文风参考片段。", []),
    ("Anti-Defensive Writing（Adkid-Zephyr）", "writing", "选择该作者版本，导入其技能目录后提交需要修改的论文段落。", []),
    ("计算机科研方法总目录", "reference", "按研究问题查阅数学、算法和方法设计条目，作为进一步阅读与讨论的索引。", []),
    ("ML Paper Writing（Orchestra Research）", "writing", "读取技能说明，提供研究材料；引用检索、模板编译等功能按上游要求配置。", []),
    ("Anti-Defensive Writing（Kiterlin）", "writing", "选择该作者版本，加载技能后提交草稿，按其说明去掉冗余铺垫并保留必要范围。", []),
    ("论文初稿辅助写作网站（原表）", "writing", "按原表入口提供研究领域、目标会议、背景和问题定义；该 IP 入口未作可用性保证。", []),
    ("Paper Banana：学术图表生成", "figures", "输入图表描述，选择模板、风格和版面，再检查生成图的模块与标注。", []),
    ("Scribbr：语法检查", "writing", "在页面粘贴待检查文本，逐项查看错误标注和修改版本。", []),
    ("Manchester Academic Phrasebank", "writing", "按写作功能查找常见学术表达，结合自己的论证和上下文使用。", []),
    ("Academic Research Skills：学术流程套件", "figures", "保留完整项目，按其平台安装说明选择研究、写作、审稿或绘图任务。", []),
]

GROUPS = {
    "literature": ("文献检索与引文核对", "先说明主题和发表范围，再核对论文入口。已有一组论文时，可转到论文阅读页做对比。"),
    "reading": ("论文阅读与知识整理", "围绕具体问题阅读论文，并要求回答给出章节、页码或图表依据。多个知识库工具分别保留原表经验。"),
    "writing": ("论文写作、润色、纠错与翻译", "按任务选择：润色允许重写表达；纠错只修改错误；翻译保留原意。写作类现成技能的来源和下载见各条目。"),
    "ideas-review": ("研究思路与模拟审稿", "早期讨论优先解决关键假设，投稿前审稿优先核对主张与证据。各工具的原表体验分别列出。"),
    "coding": ("科研编程与需求整理", "给出已有代码、输入输出、限制和完成标准，再选择合适的编码工具。"),
    "figures": ("模型图与科研绘图", "先明确模块、连接和图要说明的内容，再绘图。模型示意图与依赖真实数据的统计图应分别处理。"),
    "reference": ("提示词集合与方法参考", "这里收录跨任务的提示词集合、科研技能套件和原表长篇方法目录。"),
}

SKILLS = [
    ("research-literature-search", "文献检索", [2, 3, 4, 5, 8], "给出主题、年份和会议，返回带来源的论文清单。"),
    ("research-paper-reading", "论文阅读与多论文对比", [1, 6, 7, 9, 41], "给出论文与问题，返回方法梳理、原文依据和对比表。"),
    ("academic-language-polish", "学术语言润色", [13, 14], "给出段落和文风要求，返回修订稿。"),
    ("method-logic-check", "方法逻辑与术语一致性检查", [10, 14], "给出 Method 和已有定义，返回问题定位与统一建议。"),
    ("research-idea-discussion", "研究思路讨论", [26, 27, 46], "给出研究问题与资源条件，返回关键假设和验证建议。"),
    ("paper-peer-review", "论文模拟审稿", [27, 28, 29, 30, 31], "给出论文和审稿要求，返回有依据的修改意见。"),
    ("academic-proofreading", "拼写与语法纠错", [32, 33, 51], "只修正错误，正确表达保持原样。"),
    ("academic-translation", "中英文学术翻译", [35, 36], "保留含义、逻辑、数值和固定术语。"),
    ("coding-task-brief", "编程任务需求整理", [16, 20, 25], "整理成可直接提交给编码 Agent 的任务说明。"),
    ("paper-figure-brief", "论文模型图说明与绘图提示词", [38, 40, 50], "输出模型结构、VISUAL SCHEMA 与绘图提示词。"),
]

def write(path, text):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")

def fenced(value):
    fence = "`" * max(4, max((len(x) + 1 for x in re.findall(r"`+", value)), default=4))
    return fence + "text\n" + value + "\n" + fence

def urls(value):
    return list(dict.fromkeys(x.rstrip(").,;") for x in re.findall(r"https?://[^\s<>\"（）\u3000、，；]+", value)))

def main():
    source = ROOT / "sources" / "resources.csv"
    if not source.exists():
        with (ROOT.parent / CSV_NAME).open(encoding="utf-8-sig", newline="") as stream:
            original_rows = list(csv.reader(stream))
        public_rows = [row[:5] + row[6:] for row in original_rows]
        # Remove the personal attribution embedded in one resource description.
        public_rows = [[re.sub(r"^.*?初稿skill", "基于既有论文写作思路整理的初稿 skill", cell) for cell in row] for row in public_rows]
        source.parent.mkdir(parents=True, exist_ok=True)
        with source.open("w", encoding="utf-8-sig", newline="") as stream:
            csv.writer(stream).writerows(public_rows)
    with source.open(encoding="utf-8-sig", newline="") as stream:
        raw = list(csv.reader(stream))
    valid = [(i, row[:5]) for i, row in enumerate(raw[1:], 2) if any(x.strip() for x in row[1:5])]
    if len(valid) != len(CURATION):
        raise ValueError(f"Expected {len(CURATION)} content records, got {len(valid)}")
    records = []
    for n, ((record, fields), (title, group, how, extra)) in enumerate(zip(valid, CURATION), 1):
        records.append({"id": f"R{n:03d}", "csv_record": record, "title": title, "group": group,
                        "how_to": how, "supplemental_links": extra, "original": dict(zip(FIELDS, fields))})
    write("sources/records.json", json.dumps(records, ensure_ascii=False, indent=2))
    write("sources/README.md", """# 原始资料与条目编号

[resources.csv](resources.csv) 是供仓库分发的资料副本，按用户要求移除了贡献者列与一处描述中的个人署名；保留其余资料、空行和空列。未经处理的原 CSV 留在仓库外的工作目录，不进入下载包。
[records.json](records.json) 保存 53 条实际内容及整理后的标题、分类和入口。

筛选只用于识别实际内容：除“类别”外，资料字段中至少一个字段非空就保留；只有类别的占位行和全空行不计入条目。空白字段不推测补写。原表 CSV 不包含表格颜色，无法恢复“提示词标绿”等样式。

R001—R053 按原表内容顺序编号。`csv_record` 为 CSV 逻辑记录号，表头算第 1 条；含换行的单元格仍算一条记录，不是文本编辑器的行号。

[覆盖清单](../catalog/coverage.md)列出每条资料的去向；[第三方清单](upstream.json)记录项目、分支、获取日期、原许可和保存位置，不做哈希检查。
""")
    long_text = records[45]["original"]["usage"]
    method_intro = "<!-- 来源：原表 R046；以下正文保持原样。 -->\n\n"
    write("references/computer-science-methods.md", method_intro + long_text)
    for slug, title, ids, description in SKILLS:
        text = f"# {title}：原表提示词与经验\n\n此文件保留来源材料，供需要时查阅。当前技能的执行要求以 SKILL.md 为准；原表中的价格、额度、模型版本和个人评价是填写时的记录。\n"
        for i in ids:
            item = records[i-1]
            o = item["original"]
            text += f"\n## {item['id']} · {item['title']}\n\n原 CSV 逻辑记录：{item['csv_record']}。\n\n"
            if i == 46:
                text += "长篇原文见 [方法目录](methods-directory.md)。\n"
            else:
                for label, field in [("原始入口", "entry"), ("原始使用方法或提示词", "usage"), ("原表使用经验", "experience")]:
                    if o[field]:
                        text += f"### {label}\n\n" + fenced(o[field]) + "\n\n"
        write(f"skills/{slug}/references/source-prompts.md", text)
        write(f"skills/{slug}/SOURCE.md", f"# 来源与整理说明\n\n本技能由《{CSV_NAME}》整理制作，不是第三方原项目的官方技能。\n\n来源记录：{', '.join(f'R{i:03d}' for i in ids)}。\n\n改动：将原表提示词和经验整理为适用任务、输入、处理方法、输出要求与调用示例，补充可追溯来源及任务范围说明。原始措辞见 [配套参考](references/source-prompts.md)。原表没有声明统一开源许可，本仓库不对原资料重新授权。")
    write("skills/research-idea-discussion/references/methods-directory.md", method_intro + long_text)
    upstream = json.loads((ROOT / "sources/upstream.json").read_text(encoding="utf-8"))
    upstream_by_id = {i: u for u in upstream for i in u["source_ids"]}
    for item in records:
        o = item["original"]
        text = f"# {item['id']} · {item['title']}\n\n[返回分类](../{item['group']}.md) · [53 条覆盖清单](../coverage.md)\n\n"
        text += f"原表类别：{o['category']}。CSV 逻辑记录：{item['csv_record']}。\n\n## 使用方法\n\n{item['how_to']}\n\n"
        found = urls(o["entry"]) + urls(o["usage"])
        if found or item["supplemental_links"]:
            text += "## 入口\n\n"
            for idx, url in enumerate(dict.fromkeys(found), 1):
                text += f"- [原表入口 {idx}]({url})\n"
            for url in item["supplemental_links"]:
                text += f"- [整理时补充的入口]({url})\n"
            text += "\n"
        if item["id"] in {"R022", "R039"}:
            text += "原表只提供名称。这里的链接是按名称和功能检索后补充的项目，不能确认就是原表所指版本；项目名称不表示 Karpathy 本人或 Nature 出版方的官方背书。\n\n"
        if item["id"] == "R033":
            text += "整理说明：原表功能栏写的是“检索论文”，与本条提示词不一致；本库按实际提示词归为纠错，原字段在下方完整保留。\n\n"
        if item["id"] == "R034":
            text += "整理说明：原表的 turnitinchn.com 链接与补充的 turnitin.com 官方域名不同，本条保留原入口，不将其标成官方入口。\n\n"
        if item["id"] in upstream_by_id:
            u = upstream_by_id[item["id"]]
            text += f"现成技能：[本地文件](../../{u['local']}/) · [原项目完整套件包](../../{u['archive']}) · [安装与依赖说明](../../docs/third-party-skills.md#{u['key']})。\n\n"
        related = [(slug, name) for slug, name, ids, _ in SKILLS if int(item["id"][1:]) in ids]
        if related:
            text += "本表制作的相关技能：" + "、".join(f"[{name}](../../skills/{slug}/SKILL.md)" for slug, name in related) + "。\n\n"
        text += "## 原表记录\n\n以下保留资料内容，已移除个人署名；价格、免费额度、上传限制、模型版本和效果评价属于填写时的记录，当前条件以服务页面为准。\n\n"
        for label, field in [("网站 / 入口 / 工具", "entry"), ("功能", "purpose"), ("具体用法与提示词", "usage"), ("特点与使用经验", "experience")]:
            text += f"### {label}\n\n"
            if item["id"] == "R046" and field == "usage":
                text += "[长篇原文：计算机科研方法总目录](../../references/computer-science-methods.md)\n\n"
            else:
                text += (fenced(o[field]) if o[field] else "原表未填写。") + "\n\n"
        write(f"catalog/entries/{item['id']}.md", text)
    index = "# 按科研任务查找\n\n所有条目保留独立编号；相同工具的不同经验不会因归类而删除。\n\n"
    for group, (title, intro) in GROUPS.items():
        selected = [r for r in records if r["group"] == group]
        index += f"- [{title}]({group}.md)：{len(selected)} 条。\n"
        text = f"# {title}\n\n[返回分类总览](README.md) · [Skills 下载](../downloads/README.md)\n\n{intro}\n\n| 编号 | 资料 | 如何使用 |\n|---|---|---|\n"
        for r in selected:
            text += f"| {r['id']} | [{r['title']}](entries/{r['id']}.md) | {r['how_to']} |\n"
        write(f"catalog/{group}.md", text)
    index += "\n[全部 53 条覆盖清单](coverage.md) · [可复制原始提示词](../prompts/original-prompts.md) · [长篇方法目录](../references/computer-science-methods.md)\n"
    write("catalog/README.md", index)
    coverage = "# 53 条内容覆盖清单\n\n编号按 CSV 实际内容顺序排列，合计 53 条。CSV 记录号不是物理文本行号。\n\n| 编号 | CSV 记录 | 资料位置 | 分类 | 对应新技能 |\n|---|---:|---|---|---|\n"
    for r in records:
        related = [f"[{name}](../skills/{slug}/SKILL.md)" for slug, name, ids, _ in SKILLS if int(r["id"][1:]) in ids]
        coverage += f"| {r['id']} | {r['csv_record']} | [{r['title']}](entries/{r['id']}.md) | {GROUPS[r['group']][0]} | {'、'.join(related) or '见资料条目'} |\n"
    write("catalog/coverage.md", coverage)
    prompts = "# 原始提示词与可复制任务说明\n\n原文来自 CSV，保留措辞和占位符。复制后替换自己的材料。整理后的通用技能见 [Skills 列表](../skills/README.md)。\n\n"
    for n in [1, 2, 10, 13, 14, 25, 26, 31, 33, 35, 36, 38]:
        r = records[n-1]
        prompts += f"## {r['id']} · {r['title']}\n\n[完整条目](../catalog/entries/{r['id']}.md)。\n\n" + fenced(r["original"]["usage"]) + "\n\n"
    prompts += "外部提示词库的未提供全文不在此转载，请从 [参考资料分类](../catalog/reference.md) 和 [写作分类](../catalog/writing.md)中的原项目入口获取。\n"
    write("prompts/original-prompts.md", prompts)
    skill_list = "# 本表制作的 10 个 Skills\n\n这是本仓库根据原表制作的技能，与 third_party 中的原项目文件分开保存。每个技能包含 SKILL.md、来源说明及必要参考文件。\n\n[下载与使用](../downloads/README.md) · [原始提示词](../prompts/original-prompts.md)\n\n| 技能 | 适用任务 | 单个包 |\n|---|---|---|\n"
    for slug, title, ids, description in SKILLS:
        skill_list += f"| [{title}]({slug}/SKILL.md) | {description} | [下载](../downloads/individual/{slug}.zip) |\n"
    write("skills/README.md", skill_list)
    write("sources/new-skills.json", json.dumps([{"name": s, "title": t, "source_ids": [f"R{i:03d}" for i in ids], "description": d} for s, t, ids, d in SKILLS], ensure_ascii=False, indent=2))
    print(f"Generated {len(records)} entries and {len(SKILLS)} skill source references without contributor attribution.")

if __name__ == "__main__":
    main()
