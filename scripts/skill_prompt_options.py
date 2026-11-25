"""Render the same reusable prompt and example in the catalog and skill downloads."""

import json
import re


def fenced(value):
    fence = "`" * max(4, max((len(run) + 1 for run in re.findall(r"`+", value)), default=4))
    return f"{fence}text\n{value}\n{fence}"


def options_for_skill(options, slug):
    matches = (option for option in options if slug in option["skills"])
    return sorted(matches, key=lambda option: option["skills"][0] != slug)


def render_prompt(option):
    return f"{fenced(option['text'])}\n\n**怎么用**\n\n{option['example']}"


def render_skill_files(root, options):
    skills = json.loads((root / "sources/new-skills.json").read_text(encoding="utf-8"))
    for skill in skills:
        name = skill["name"]
        path = root / "skills" / name / "SKILL.md"
        frontmatter, separator, _ = path.read_text(encoding="utf-8").partition("\n---\n")
        if not separator or not frontmatter.startswith("---\n"):
            raise ValueError(f"Missing skill frontmatter in {path}")
        description = json.dumps(skill["description"], ensure_ascii=False)
        source_records = json.dumps(", ".join(skill["source_ids"]))
        frontmatter = re.sub(
            r"^description: .*$", lambda _: f"description: {description}", frontmatter, count=1, flags=re.M
        )
        frontmatter = re.sub(
            r"^  source-records: .*$", lambda _: f"  source-records: {source_records}", frontmatter, count=1, flags=re.M
        )
        parts = [
            frontmatter + separator.rstrip("\n"),
            f"# {skill['title']}",
            "根据用户的任务选用对应的提示词，代入用户提供的材料执行。",
        ]
        for option in options_for_skill(options, name):
            source = option["source"]
            note = f"据原表 {source} 的用法整理。" if option["derived"] else f"来源见原表 {source}。"
            parts.extend([f"## {option['title']}", note, render_prompt(option)])
        parts.extend(["## 参考材料", "[来源说明](SOURCE.md) · [原表提示词与经验](references/source-prompts.md)"])
        if name == "paper-figure-brief":
            parts.append("[绘图说明模板](references/visual-schema.md)")
        if name == "research-idea-discussion":
            parts.append("[计算机科研方法目录](references/methods-directory.md)")
        path.write_text("\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
