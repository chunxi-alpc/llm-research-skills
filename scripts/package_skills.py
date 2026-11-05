"""Build self-contained skill ZIPs and the Chinese download index."""
from pathlib import Path
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]

# Whole-root projects retain their original README, scripts and references.
SINGLES = [
    ("blader--humanizer", ".", "humanizer", "Humanizer", True),
    ("adkid-zephyr--anti-defensive-writing", "skills/anti-defensive-writing", "anti-defensive-writing", "Anti-Defensive Writing 中文版（Adkid-Zephyr）", False),
    ("adkid-zephyr--anti-defensive-writing", "skills/anti-defensive-writing-en", "anti-defensive-writing-en", "Anti-Defensive Writing 英文版（Adkid-Zephyr）", False),
    ("kiterlin--anti-defensive-writing", "skill/anti-defensive-writing", "anti-defensive-writing", "Anti-Defensive Writing（Kiterlin）", False),
    ("deathcats4--scientific-manuscript-editor", ".", "scientific-manuscript-editor", "Scientific Manuscript Editor", True),
    ("multica-ai--andrej-karpathy-skills", "skills/karpathy-guidelines", "karpathy-guidelines", "Karpathy Guidelines", False),
]

INFO = {
    "blader--humanizer": (
        "Humanizer", "减少机械表达，按任务改写段落。", "SKILL.md",
        "核心技能是文本指令，没有额外运行依赖。此处单个包保留完整目录及原项目附带文件；需要插件集成时查看原 README。"),
    "adkid-zephyr--anti-defensive-writing": (
        "Anti-Defensive Writing（Adkid-Zephyr）", "围绕论文贡献组织叙述，提供中英文两个技能。", "skills/anti-defensive-writing/SKILL.md",
        "上游说明为零运行依赖，支持直接使用技能，也提供 Codex 插件结构。中文与英文技能目录不同；本库保留二者。此版本和 Kiterlin 版本是不同内容。"),
    "kiterlin--anti-defensive-writing": (
        "Anti-Defensive Writing（Kiterlin）", "删除冗余限定和解释，同时保留影响准确性的必要范围。", "skill/anti-defensive-writing/SKILL.md",
        "核心技能没有额外运行依赖。单个包使用上游 skill/anti-defensive-writing 目录，并补带根目录的原 LICENSE。与 Adkid-Zephyr 中文技能同名，请按来源选择安装。"),
    "deathcats4--scientific-manuscript-editor": (
        "Scientific Manuscript Editor", "根据论文材料进行写作和修改，配套写作参考。", "SKILL.md",
        "保留 references、agents 与 scripts。基本写作依靠 Agent；原 README 的更新或保存辅助流程提到 Python 3.9+ 和 PyYAML，使用这些脚本时按原说明配置。"),
    "orchestra-research--ai-research-skills": (
        "ML Paper Writing / AI Research Skills", "机器学习论文写作、引用工作流与会议模板。", "20-ml-paper-writing/ml-paper-writing/SKILL.md",
        "ML 技能声明 semanticscholar、arxiv、habanero、requests 等 Python 依赖；检索需要联网，文中介绍 Exa MCP 配置；编译模板需要 LaTeX。浏览副本保留完整 20-ml-paper-writing 目录，包括关联的系统论文写作、绘图和报告技能。套件 ZIP 为整个 AI Research Skills 原项目，未裁剪。"),
    "obra--superpowers": (
        "Superpowers", "覆盖规划、开发、调试与验证的技能和插件套件。", "skills/using-superpowers/SKILL.md",
        "优先按原 README 中对应 Agent 的插件或目录安装方法使用，保留 hooks、scripts、skills 和隐藏插件目录。不同客户端安装方式不同；仅复制一个 SKILL.md 不能代替完整插件。"),
    "imbad0202--academic-research-skills": (
        "Academic Research Skills", "学术研究、写作、审稿与完整流程套件。", "academic-paper/SKILL.md",
        "保留 agents、shared、scripts、tools、hooks 与各技能目录。安装按 QUICKSTART.md 和 docs/SETUP.md；子代理与工具功能需要客户端支持，并按客户端配置模型登录或 API。核心流程是提示词；使用检索、图表和导出时，再按模式配置联网、MCP、Python 或 R、Pandoc、tectonic 和字体等。原项目当前采用 CC BY-NC 4.0，完整 LICENSE、NOTICE.md、THIRD_PARTY.md 随包保留。"),
    "yuan1z0825--nature-skills": (
        "Nature Skills", "覆盖阅读、写作、绘图、引用等科研任务的技能套件。", "skills/nature-writing/SKILL.md",
        "保留 skills/nature-shared 以及各技能的 references、scripts、assets 等资源。上游 npx 安装方式要求 Node.js 18+；文献检索 MCP、Python/R、浏览器及绘图或数据库 API 按选用的技能配置。部分检索功能需要 PUBMED_EMAIL 或相关服务凭据；复制技能文件不会自动配置这些服务。"),
    "multica-ai--andrej-karpathy-skills": (
        "Karpathy Skills", "围绕先理解任务、保持简单、集中修改与验证目标的编程原则。", "skills/karpathy-guidelines/SKILL.md",
        "核心是文本规则，无专用运行依赖；原项目还提供 Claude Code 插件及 Cursor 规则用法。README 中部分安装示例仍使用 forrestchang 的旧地址，本库记录当前检索到的 multica-ai 仓库。原 README 声明 MIT，未提供独立 LICENSE 文件。"),
}

def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")

def add_tree(archive, source, prefix):
    for file in sorted(source.rglob("*")):
        if file.is_file() and "__pycache__" not in file.parts:
            archive.write(file, f"{prefix}/{file.relative_to(source).as_posix()}")

def main():
    new = json.loads((ROOT / "sources/new-skills.json").read_text(encoding="utf-8"))
    upstream = json.loads((ROOT / "sources/upstream.json").read_text(encoding="utf-8"))
    by_key = {u["key"]: u for u in upstream}
    packages = []
    start = """# 10 个科研 Skills 入门合集

下载 → 解压 → 选择 skills/ 中的完整技能目录 → 导入或复制到 Agent 的技能目录 → 提交任务。

每个技能目录包含 SKILL.md、SOURCE.md 和 references/，请一起保留。
本地 Codex 当前项目可使用 .agents/skills/；本地 Claude Code 可使用 .claude/skills/。
有导入界面的产品按界面要求逐个选择技能，合集 ZIP 不一定能直接导入。

示例：使用 academic-proofreading，只修正下面英文段落的拼写和语法错误，不润色。

没有导入功能时，可以复制 SKILL.md 正文作为任务要求，原始提示词在各技能的 references/source-prompts.md 中。
文献检索需要 Agent 自带联网能力；绘图技能默认输出绘图说明与提示词。

官方目录说明：https://learn.chatgpt.com/docs/build-skills
Claude Code：https://code.claude.com/docs/en/skills
"""
    license_note = "本合集根据用户提供的科研资料 CSV 整理。每个技能的 SOURCE.md 记录来源和整理改动。原表未声明统一开源许可，本仓库不对原资料重新授权。\n"
    starter = ROOT / "downloads/research-skills-starter.zip"
    starter.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(starter, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("research-skills-starter/START-HERE.md", start)
        archive.writestr("research-skills-starter/LICENSE-NOTES.md", license_note)
        for s in new:
            add_tree(archive, ROOT / "skills" / s["name"], "research-skills-starter/skills/" + s["name"])
    packages.append({"kind": "starter", "path": starter.relative_to(ROOT).as_posix(), "skill_count": 10})
    for s in new:
        path = ROOT / "downloads/individual" / (s["name"] + ".zip")
        path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
            add_tree(archive, ROOT / "skills" / s["name"], s["name"])
        packages.append({"kind": "new-skill", "path": path.relative_to(ROOT).as_posix(), "name": s["name"], "skill_count": 1})
    single_links = {}
    for key, relative, name, title, whole in SINGLES:
        u = by_key[key]
        root = ROOT / u["local"]
        directory = root / relative
        path = ROOT / "downloads/individual" / (key + "--" + name + ".zip")
        source_note = f"# 来源与打包说明\n\n原项目：[{u['repository']}]({u['url']})。\n\n获取日期：{u['retrieved']}，分支：{u['branch']}。\n\n原表记录：{', '.join(u['source_ids'])}。许可：{u['license']}。\n\n打包内容：{relative} 的完整文件。原技能正文未改写；增加本说明并携带原许可。依赖及具体安装方法以原项目为准。\n"
        if key.endswith("andrej-karpathy-skills"):
            source_note += "\n上游 README 的原许可声明如下（获取版本没有独立 LICENSE 文件）：\n\n## License\n\nMIT\n"
        if "anti-defensive-writing" in name:
            source_note += "\n同名技能按作者分包，请在不同项目选择版本或使用客户端支持的命名空间，不要合并到一个安装目录。\n"
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
            add_tree(archive, directory, name)
            if not whole:
                for notice in ["LICENSE", "LICENSE.md", "NOTICE", "NOTICE.md"]:
                    original = root / notice
                    if original.is_file() and not (directory / notice).exists():
                        archive.write(original, f"{name}/{notice}")
            archive.writestr(f"{name}/PACKAGE-SOURCE.md", source_note)
        packages.append({"kind": "upstream-skill", "path": path.relative_to(ROOT).as_posix(), "project": key, "name": name, "title": title, "skill_count": 1})
        single_links.setdefault(key, []).append((title, path.relative_to(ROOT).as_posix()))
    for u in upstream:
        packages.append({"kind": "upstream-suite", "path": u["archive"], "project": u["key"]})
    for package in packages:
        package["bytes"] = (ROOT / package["path"]).stat().st_size
    write("downloads/packages.json", json.dumps(packages, ensure_ascii=False, indent=2))
    doc = "# 现成 Skills：来源、下载与使用条件\n\n[返回首页](../README.md) · [下载总览](../downloads/README.md)\n\n保留 9 个原项目的完整套件 ZIP，以及适合单独使用的技能包。文件获取于 2026-11-05，分支为 main；这是下载时的副本。未运行第三方项目或安装其依赖。\n\n同名技能按来源分开存放，原文件保持原样。套件包包含项目的必要目录和原许可，使用时按上游对应平台的说明安装。\n\n| 项目 | 来源记录 | 许可 | 完整套件 |\n|---|---|---|---|\n"
    for key in INFO:
        u = by_key[key]
        title, _, _, _ = INFO[key]
        doc += f"| [{title}](#{key}) | {', '.join(u['source_ids'])} | {u['license']} | [下载 ZIP](../{u['archive']}) |\n"
    for key, (title, purpose, entry, deps) in INFO.items():
        u = by_key[key]
        doc += f"\n<a id=\"{key}\"></a>\n\n## {title}\n\n{purpose}\n\n"
        doc += f"- 原项目：[{u['repository']}]({u['url']})。\n- 浏览：[技能入口](../{u['local']}/{entry}) · [原 README](../{u['local']}/README.md)。\n- 下载：[完整套件 ZIP](../{u['archive']})。\n"
        for name, path in single_links.get(key, []):
            doc += f"- 单个技能包：[{name}](../{path})。\n"
        doc += f"\n使用条件：{deps}\n\n"
        local = ROOT / u["local"]
        notices = [x for x in ["LICENSE", "NOTICE.md", "THIRD_PARTY.md"] if (local / x).exists()]
        if notices:
            doc += "原许可与说明：" + " · ".join(f"[{n}](../{u['local']}/{n})" for n in notices) + "。\n\n"
        if u["supplemented_by_name"]:
            doc += "来源说明：原表只有名称，本项目为整理时按名称与功能补充，不能确认就是原表所指版本，不表示相关个人或出版机构的官方项目。\n\n"
        doc += "原表经验：" + "、".join(f"[{i}](../catalog/entries/{i}.md)" for i in u["source_ids"]) + "。\n"
    doc += "\n## 网站、提示词库与其他项目\n\nAi-prompt、Awesome AI Research Writing、Strict & Precise Reviewer、Academic AI Prompt、AI-Scientist、PaperDebugger 等作为网站、项目或参考入口收录，未把未提供的网页全文改造成第三方技能。其操作方法、原表经验及下载入口见 [任务分类](../catalog/README.md)。\n"
    write("docs/third-party-skills.md", doc)
    doc = "# Skills 下载\n\n[返回首页](../README.md) · [下载后的使用方法](../docs/getting-started.md)\n\n## 新 Skills 入门合集\n\n**[下载 research-skills-starter.zip](research-skills-starter.zip)**：包含本表制作的 10 个新技能、来源和配套参考。解压后从 skills/ 中选择完整技能目录导入。\n\n## 单个新技能\n\n| 技能 | 下载 |\n|---|---|\n"
    for s in new:
        doc += f"| [{s['title']}](../skills/{s['name']}/SKILL.md) | [{s['name']}.zip](individual/{s['name']}.zip) |\n"
    doc += "\n## 单个第三方技能\n\n包名带作者，用于区分来源；内部技能名保持上游原名。两个同名 Anti-Defensive Writing 不要合并安装到一个目录。\n\n| 技能 | 下载 |\n|---|---|\n"
    for p in packages:
        if p["kind"] == "upstream-skill":
            doc += f"| {p['title']} | [ZIP]({Path(p['path']).relative_to('downloads').as_posix()}) |\n"
    doc += "\n## 原项目完整套件\n\n这些 ZIP 保留项目原有目录。Superpowers、Nature Skills、Academic Research Skills 以及 ML Paper Writing 的关联功能按完整套件使用；插件、MCP、API 和运行依赖见 [逐项说明](../docs/third-party-skills.md)。归档 ZIP 不保证可直接作为插件上传。\n\n| 套件 | 下载 | 大小 |\n|---|---|---:|\n"
    for key in INFO:
        u = by_key[key]
        doc += f"| {INFO[key][0]} | [原项目 ZIP]({Path(u['archive']).relative_to('downloads').as_posix()}) | {u['archive_bytes']/1048576:.2f} MiB |\n"
    doc += "\n包内第三方许可保持不变；Academic Research Skills 含非商业条件，Karpathy Skills 的 MIT 声明位于原 README。详见 [许可说明](../LICENSE.md)。\n\n维护用文件清单：[packages.json](packages.json)。\n"
    write("downloads/README.md", doc)
    print(f"Prepared {len(packages)} download packages.")

if __name__ == "__main__":
    main()
