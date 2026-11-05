"""Download source archives only; never install or execute upstream projects."""
from pathlib import Path, PurePosixPath
import concurrent.futures
import json
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = [
    ("blader--humanizer", "blader/humanizer", [44], "MIT", None),
    ("adkid-zephyr--anti-defensive-writing", "Adkid-Zephyr/anti-defensive-writing-Skill", [45], "MIT", None),
    ("kiterlin--anti-defensive-writing", "Kiterlin/anti-defensive-writing", [48], "MIT", None),
    ("deathcats4--scientific-manuscript-editor", "deathcats4/scientific-manuscript-editor", [43], "MIT", None),
    ("orchestra-research--ai-research-skills", "Orchestra-Research/AI-Research-SKILLs", [47], "MIT", "20-ml-paper-writing/"),
    ("obra--superpowers", "obra/superpowers", [23], "MIT", None),
    ("imbad0202--academic-research-skills", "Imbad0202/academic-research-skills", [53], "CC-BY-NC-4.0", None),
    ("yuan1z0825--nature-skills", "Yuan1z0825/nature-skills", [39], "Apache-2.0", None),
    ("multica-ai--andrej-karpathy-skills", "multica-ai/andrej-karpathy-skills", [22], "MIT (README declaration)", None),
]

def fetch(project):
    key, repo, rows, license_name, selected = project
    archive = ROOT / "downloads" / "upstream" / (key + ".zip")
    archive.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://codeload.github.com/{repo}/zip/main"
    if not zipfile.is_zipfile(archive):
        request = urllib.request.Request(url, headers={"User-Agent": "llm-research-skills-collection"})
        with urllib.request.urlopen(request, timeout=90) as response:
            archive.write_bytes(response.read())
    dest = ROOT / "third_party" / key
    with zipfile.ZipFile(archive) as source:
        for member in source.infolist():
            relative = PurePosixPath(member.filename)
            if len(relative.parts) <= 1 or member.is_dir():
                continue
            relative = PurePosixPath(*relative.parts[1:])
            if ".." in relative.parts or relative.is_absolute():
                raise ValueError(f"Unexpected archive path: {relative}")
            # Orchestra's full suite remains available as the untouched archive.
            # The browsable copy contains the writing skills and root notices.
            if selected and not (str(relative).startswith(selected) or str(relative) in {"LICENSE", "README.md"}):
                continue
            target = dest.joinpath(*relative.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read(member))
    return {
        "key": key, "repository": repo, "url": f"https://github.com/{repo}",
        "branch": "main", "retrieved": "2026-11-05", "source_ids": [f"R{i:03d}" for i in rows],
        "license": license_name, "supplemented_by_name": rows[0] in {22, 39},
        "archive": archive.relative_to(ROOT).as_posix(),
        "local": dest.relative_to(ROOT).as_posix(),
        "local_scope": selected or "complete repository",
        "skill_files": [p.relative_to(dest).as_posix() for p in sorted(dest.rglob("SKILL.md"))],
        "archive_bytes": archive.stat().st_size,
    }

def main():
    report = ROOT / "reports" / "download-log.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    results, errors = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        tasks = {executor.submit(fetch, p): p[0] for p in PROJECTS}
        for future in concurrent.futures.as_completed(tasks):
            try:
                results.append(future.result())
            except Exception as exc:
                errors.append({"project": tasks[future], "error": str(exc)})
    results.sort(key=lambda p: p["key"])
    report.write_text(json.dumps({"projects": results, "errors": errors}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = ROOT / "sources" / "upstream.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Downloaded {len(results)} project archives; errors: {len(errors)}. Details: reports/download-log.json")
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
