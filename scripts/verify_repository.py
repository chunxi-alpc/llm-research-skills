"""Check the requested content, relative links and extractable skill packages.

Uses only the Python standard library. Does not run third-party code or hashes.
"""
from pathlib import Path, PurePosixPath
import csv
import json
import re
import tempfile
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
COUNTS = {"records": 0, "skills": 0, "links": 0, "packages": 0, "extracted_packages": 0}

def check(condition, message):
    if not condition:
        ERRORS.append(message)

def unfence(text):
    output, marker = [], None
    for line in text.splitlines():
        match = re.match(r"\s*(`{3,}|~{3,})", line)
        if match:
            run = match.group(1)
            if marker is None:
                marker = run
            elif run[0] == marker[0] and len(run) >= len(marker):
                marker = None
            continue
        if marker is None:
            output.append(line)
    return "\n".join(output)

def anchors(text):
    found = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    repetitions = {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", unfence(text), re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        n = repetitions.get(slug, 0)
        repetitions[slug] = n + 1
        found.add(slug if n == 0 else f"{slug}-{n}")
    return found

def check_links(file, boundary, fragments=True):
    text = unfence(file.read_text(encoding="utf-8"))
    for value in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text):
        parsed = urlsplit(value)
        if parsed.scheme or value.startswith("//"):
            continue
        target = (file.parent / unquote(parsed.path)).resolve() if parsed.path else file.resolve()
        if not target.is_relative_to(boundary.resolve()):
            ERRORS.append(f"Link leaves package: {file}: {value}")
            continue
        check(target.exists(), f"Missing relative link: {file}: {value}")
        if fragments and target.is_file() and target.suffix == ".md" and parsed.fragment:
            check(unquote(parsed.fragment) in anchors(target.read_text(encoding="utf-8")), f"Missing anchor: {file}: {value}")
        COUNTS["links"] += 1

def main():
    with (ROOT / "sources/resources.csv").open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.reader(stream))
    check("贡献者" not in rows[0], "Public CSV still contains contributor column")
    content = [(i, r[:5]) for i, r in enumerate(rows[1:], 2) if any(v.strip() for v in r[1:5])]
    records = json.loads((ROOT / "sources/records.json").read_text(encoding="utf-8"))
    check(len(content) == len(records) == 53, "Expected exactly 53 content records")
    fields = ["category", "entry", "purpose", "usage", "experience"]
    for n, ((record_num, values), record) in enumerate(zip(content, records), 1):
        check(record["id"] == f"R{n:03d}", f"Unexpected record ID: {record['id']}")
        check(record["csv_record"] == record_num, f"CSV mapping mismatch: {record['id']}")
        check(record["original"] == dict(zip(fields, values)), f"Source content mismatch: {record['id']}")
        check("contributor" not in record["original"], f"Contributor field remains: {record['id']}")
        page = ROOT / "catalog/entries" / (record["id"] + ".md")
        check(page.exists(), f"Missing entry: {record['id']}")
        if page.exists():
            page_text = page.read_text(encoding="utf-8")
            for field in ["entry", "purpose", "usage", "experience"]:
                if n == 46 and field == "usage":
                    page_text_for_field = (ROOT / "references/computer-science-methods.md").read_text(encoding="utf-8")
                else:
                    page_text_for_field = page_text
                check(record["original"][field] in page_text_for_field, f"Missing original {field}: {record['id']}")
    COUNTS["records"] = len(records)
    new = json.loads((ROOT / "sources/new-skills.json").read_text(encoding="utf-8"))
    check(len(new) == 10, "Expected 10 new skills")
    for skill in new:
        folder = ROOT / "skills" / skill["name"]
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        check(match is not None, f"Missing YAML frontmatter: {skill['name']}")
        if match:
            name = re.search(r"^name: (.+)$", match.group(1), re.M)
            description = re.search(r"^description: (.+)$", match.group(1), re.M)
            check(name is not None and name.group(1) == folder.name, f"Name mismatch: {folder}")
            check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder.name)) and len(folder.name) <= 64, f"Invalid name: {folder}")
            check(description is not None and 0 < len(description.group(1)) <= 1024, f"Invalid description: {folder}")
        check((folder / "references/source-prompts.md").exists(), f"Missing source reference: {folder}")
        check((folder / "SOURCE.md").exists(), f"Missing SOURCE.md: {folder}")
        check("[TODO:" not in text, f"Unfinished scaffold: {folder}")
    COUNTS["skills"] = len(new)
    # Third-party documentation is unmodified upstream material, checked separately by package scope.
    for file in ROOT.rglob("*.md"):
        relative = file.relative_to(ROOT)
        if relative.parts[0] not in {"third_party", ".build-tools", "reports"}:
            check_links(file, ROOT)
    packages = json.loads((ROOT / "downloads/packages.json").read_text(encoding="utf-8"))
    upstream = {u["key"]: u for u in json.loads((ROOT / "sources/upstream.json").read_text(encoding="utf-8"))}
    check(len(upstream) == 9, "Expected 9 upstream project archives")
    for package in packages:
        archive = ROOT / package["path"]
        check(archive.exists(), f"Missing ZIP: {archive}")
        if not archive.exists():
            continue
        try:
            with zipfile.ZipFile(archive) as z:
                names = z.namelist()
                check(all(not PurePosixPath(n).is_absolute() and ".." not in PurePosixPath(n).parts for n in names), f"Invalid path in {archive}")
                if package["kind"] != "upstream-suite":
                    skills = [n for n in names if n.endswith("/SKILL.md")]
                    check(len(skills) == package["skill_count"], f"Wrong skill count in {archive}")
                    with tempfile.TemporaryDirectory(prefix="research-skills-") as temp:
                        z.extractall(temp)
                        COUNTS["extracted_packages"] += 1
                        if package["kind"] in {"new-skill", "starter"}:
                            for file in Path(temp).rglob("*.md"):
                                check_links(file, Path(temp))
                            expected = [s for s in new if package["kind"] == "starter" or s["name"] == package["name"]]
                            for s in expected:
                                prefix = f"research-skills-starter/skills/{s['name']}" if package["kind"] == "starter" else s["name"]
                                source = ROOT / "skills" / s["name"]
                                for original in source.rglob("*"):
                                    if original.is_file():
                                        extracted = Path(temp) / prefix / original.relative_to(source)
                                        check(extracted.exists() and extracted.read_bytes() == original.read_bytes(), f"Incomplete new skill package: {archive}: {original.name}")
                        else:
                            for entrypoint in Path(temp).rglob("SKILL.md"):
                                check_links(entrypoint, Path(temp))
                    if package["kind"] == "upstream-skill":
                        check(any(n.endswith("/LICENSE") for n in names) or package["project"] == "multica-ai--andrej-karpathy-skills", f"Missing upstream license: {archive}")
                else:
                    project = upstream[package["project"]]
                    prefix = names[0].split("/")[0] + "/"
                    check(prefix + "README.md" in names, f"Missing upstream README: {archive}")
                    if package["project"] != "multica-ai--andrej-karpathy-skills":
                        check(prefix + "LICENSE" in names, f"Missing suite LICENSE: {archive}")
                    for skill_file in project["skill_files"]:
                        check(prefix + skill_file in names, f"Missing upstream skill: {archive}: {skill_file}")
                    if package["project"] == "yuan1z0825--nature-skills":
                        check(any(n.startswith(prefix + "skills/nature-shared/") for n in names), "Missing nature-shared")
                    if package["project"] == "imbad0202--academic-research-skills":
                        for needed in ["shared", "agents", "scripts"]:
                            check(any(n.startswith(prefix + needed + "/") for n in names), f"Missing academic suite {needed}")
        except (OSError, zipfile.BadZipFile) as exc:
            ERRORS.append(f"Cannot read ZIP {archive}: {exc}")
    COUNTS["packages"] = len(packages)
    check(not (ROOT / "CONTRIBUTORS.md").exists(), "Contributor page remains")
    check(not (ROOT / "sources/original.csv").exists(), "Unredacted original CSV remains")
    report = ROOT / "reports/verification.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps({"counts": COUNTS, "errors": ERRORS}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    status = "通过" if not ERRORS else "存在待修复问题"
    text = f"# 交付验证\n\n日期：2026-11-05。结果：**{status}**。\n\n"
    text += f"- 53 条资料的 CSV 对应关系与原表内容已核对，个人署名已移除。\n- 10 个新技能的名称、描述、来源参考和目录完整。\n- 检查了 {COUNTS['links']} 个本仓库编写内容、新技能包和单个第三方技能入口的相对链接。\n- 检查了 {COUNTS['packages']} 个下载包，其中 {COUNTS['extracted_packages']} 个技能包已实际解压检查。\n- 9 个完整上游套件包含技能文件、原许可及所需共享目录。\n\n"
    text += "检查范围是内容覆盖、文件结构、链接与解压，不包含联网服务试用、第三方脚本或实验运行，也未计算哈希。上游文件保持原样；它们原有的外部链接和示例文档不纳入本库编写内容的链接检查。\n"
    text += "\n关键要求经正文复核：纠错技能只修改错误；翻译技能保留含义和结论强度；绘图技能默认交付绘图说明与提示词。该项是指令内容检查，不代表已在所有 Agent 或模型上运行评测。\n"
    if ERRORS:
        text += "\n待修复项：\n\n" + "\n".join("- " + e for e in ERRORS) + "\n"
    (ROOT / "reports/verification.md").write_text(text, encoding="utf-8", newline="\n")
    print(f"{status}: {COUNTS['records']} records, {COUNTS['skills']} skills, {COUNTS['packages']} packages; {len(ERRORS)} errors. See reports/verification.md")
    raise SystemExit(bool(ERRORS))

if __name__ == "__main__":
    main()
