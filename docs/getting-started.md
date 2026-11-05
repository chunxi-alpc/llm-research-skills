# 下载与使用

[返回首页](../README.md) · [全部下载](../downloads/README.md)

## 1. 下载

第一次使用可下载 [新 Skills 入门合集](../downloads/research-skills-starter.zip)，其中有 10 个本表制作的技能。只需要一项任务时，从 [技能列表](../skills/README.md)选择单个包。

Humanizer、Superpowers、Nature Skills 等属于第三方项目，下载入口和使用条件见 [现成技能说明](third-party-skills.md)。完整套件 ZIP 是项目源文件归档，并不等于所有平台都能直接上传的插件包。

在 GitHub 的 ZIP 文件页面，点击下载原始文件（Download raw file）。也可以从仓库首页选择 Code → Download ZIP，解压后使用 `downloads/` 中的包。

## 2. 解压

入门合集解压后为：

```text
research-skills-starter/
├── START-HERE.md
├── LICENSE-NOTES.md
└── skills/
    ├── academic-proofreading/
    │   ├── SKILL.md
    │   ├── SOURCE.md
    │   └── references/
    └── 其余九个技能目录/
```

单个新技能包只有一个技能目录。保留整个目录，不能只复制 `SKILL.md`。第三方单个包也带原许可和来源说明；第三方套件保留项目原有的顶层目录。

## 3. 导入或放入技能目录

有“导入技能”功能的工具，按其界面选择技能目录或符合要求的 ZIP。只接受单个技能的入口不能直接导入 10 个技能合集，应拆开选择。

本地编码 Agent 常见目录如下。`~` 指当前系统用户目录。

| 工具 | 当前项目 | 当前用户的所有项目 |
|---|---|---|
| Codex | `.agents/skills/<技能名>/SKILL.md` | `~/.agents/skills/<技能名>/SKILL.md` |
| Claude Code 本地会话 | `.claude/skills/<技能名>/SKILL.md` | `~/.claude/skills/<技能名>/SKILL.md` |

Codex 的目录参照 [OpenAI 官方技能说明](https://learn.chatgpt.com/docs/build-skills)；Claude Code 的目录参照 [官方 Skills 文档](https://code.claude.com/docs/en/skills)。部分上游项目仍以 `~/.codex/skills/` 为示例，使用其安装脚本时按项目和当前客户端说明选择目标路径。

复制完成后，按客户端要求重新加载技能或开始新会话，确认技能能被找到。云端产品和本地 IDE 的目录不是同一套；云端请使用对应产品的导入入口。

**同名技能按来源选择。** 两个 Anti-Defensive Writing 的包名分别带 `adkid-zephyr` 与 `kiterlin`，但上游内部技能名相同。不要将二者解压后合并到同一个目标目录。可在不同项目分别安装；需要并用时按客户端的插件命名空间或目录区分功能处理。原文件没有为避重名擅自改名。

## 4. 提交任务

在任务中写出技能名、输入材料和希望得到的结果。例如：

```text
使用 academic-proofreading，检查下面的英文段落。
只修正拼写和语法错误，其他表达保持原样，给出修改清单。

Our method use two encoders. It improves accuracy by 2.1 points.
```

预期只改 `use → uses`，第二句保留。其他任务的调用示例在各自的 `SKILL.md` 中。

技能文件提供处理方法；联网检索、文件阅读、绘图和代码执行能力由所用 Agent 提供。第三方套件的 Python、R、LaTeX、MCP、插件和 API 等条件在 [依赖说明](third-party-skills.md)中逐项注明。

## 没有技能导入功能

打开 [原始提示词](../prompts/original-prompts.md)，复制与任务匹配的内容，替换占位材料后粘贴到对话中。也可以复制新技能的正文作为任务要求，并提供需要的参考材料。这是手动提示词用法，不会自动获得文件系统、联网或绘图工具。
