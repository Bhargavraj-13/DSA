#!/usr/bin/env python3
"""Sync every questionbank.md with its solution files.

First run, pick your language (saved in .dsa.json):
    python3 scripts/update_progress.py --lang java

After that, just run:
    python3 scripts/update_progress.py

- Creates a blank solution file for any problem that does not have one yet.
- Marks a problem ✅ once its solution file contains code beyond the template.
- Updates the "Solved" column in the root README.md.
"""
import argparse, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / ".dsa.json"
HEADER = "| Done | # | Problem | Difficulty | Key idea | Solution |"
DIVIDER = "|---|---|---|---|---|---|"

# language: (extension, display name, line comment, block start, block end, preamble)
LANGS = {
    "cpp": ("cpp", "C++", "//", "/*", "*/", "#include <bits/stdc++.h>\nusing namespace std;"),
    "c": ("c", "C", "//", "/*", "*/", "#include <stdio.h>\n#include <stdlib.h>"),
    "java": ("java", "Java", "//", "/*", "*/", "import java.util.*;"),
    "python": ("py", "Python", "#", '"""', '"""', "from typing import *"),
    "javascript": ("js", "JavaScript", "//", "/*", "*/", ""),
    "typescript": ("ts", "TypeScript", "//", "/*", "*/", ""),
    "go": ("go", "Go", "//", "/*", "*/", "package main"),
    "rust": ("rs", "Rust", "//", "/*", "*/", ""),
    "kotlin": ("kt", "Kotlin", "//", "/*", "*/", ""),
    "csharp": ("cs", "C#", "//", "/*", "*/", "using System;\nusing System.Collections.Generic;"),
}
# Lines that only set up the file, so they do not count as a solution.
SETUP_PREFIXES = ("#", "using ", "import ", "from ", "package ")

AI_NOTE = """\
Note:
  The solution is my own. I used AI to help write this explanation, so my
  ideas are explained in a clear, standard way that anyone can follow.
"""


def template(lang, ai_note, **info):
    _, _, c, bs, be, preamble = LANGS[lang]
    head = [f"{c} {info['num']}. {info['title']}", f"{c} {info['url']}",
            f"{c} Difficulty: {info['diff']} | Topic: {info['topic']}", ""]
    if preamble:
        head += [preamble, ""]
    body = "\nExplanation:\n\n\nComplexity:\n  Time:\n  Space:\n\nDry run:\n\n"
    return "\n".join(head) + f"\n{c} Write your solution below this line.\n\n\n{bs}{body}{AI_NOTE if ai_note else ''}{be}\n"


def has_code(path, lang):
    """True when the file has a line that is not a comment or setup line."""
    _, _, c, bs, be, _ = LANGS[lang]
    text = re.sub(re.escape(bs) + r".*?" + re.escape(be), "", path.read_text(), flags=re.S)
    for line in text.splitlines():
        line = line.split(c, 1)[0].strip()
        if line and not line.startswith(SETUP_PREFIXES):
            return True
    return False


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def sync_bank(bank, lang, ai_note):
    lines = bank.read_text().splitlines()
    topic = lines[0].lstrip("# ").strip()
    solved = total = 0
    out = []
    for line in lines:
        c = cells(line) if line.startswith("|") else []
        if c and c[0] == "Done":
            out.append(HEADER)
        elif c and set(line) <= set("|-"):
            out.append(DIVIDER)
        elif len(c) >= 5 and c[1].isdigit():
            num, problem, diff, idea = c[1], c[2], c[3], c[4]
            title, url = re.match(r"\[(.+)\]\((.+)\)", problem).groups()
            done, link = False, ""
            if lang:
                slug = url.rstrip("/").rsplit("/", 1)[-1]
                sol = bank.parent / f"{int(num):04d}-{slug}.{LANGS[lang][0]}"
                if not sol.exists():
                    sol.write_text(template(lang, ai_note, num=num, title=title, url=url, diff=diff, topic=topic))
                done = has_code(sol, lang)
                link = f"[{LANGS[lang][1]}]({sol.name})"
            solved += done
            total += 1
            out.append(f"| {'✅' if done else '☐'} | {num} | {problem} | {diff} | {idea} | {link} |")
        else:
            out.append(line)
    bank.write_text("\n".join(out) + "\n")
    return solved, total


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", choices=sorted(LANGS), help="language for your solution files (saved for next time)")
    ap.add_argument("--ai-note", action=argparse.BooleanOptionalAction, default=None,
                    help="add a note to new templates saying AI helped write the explanations")
    args = ap.parse_args()

    config = json.loads(CONFIG.read_text()) if CONFIG.exists() else {}
    if args.lang:
        config["language"] = args.lang
    if args.ai_note is not None:
        config["ai_note"] = args.ai_note
    if args.lang or args.ai_note is not None:
        CONFIG.write_text(json.dumps(config, indent=2) + "\n")
    lang, ai_note = config.get("language"), config.get("ai_note", False)

    counts = {}
    for bank in sorted(ROOT.glob("*/**/questionbank.md")):
        counts[bank.relative_to(ROOT).as_posix()] = sync_bank(bank, lang, ai_note)

    solved = sum(s for s, _ in counts.values())
    total = sum(t for _, t in counts.values())
    update_readme(counts, solved, total)

    if not lang:
        print("No language chosen yet. Run: python3 scripts/update_progress.py --lang <language>")
        print("Languages:", ", ".join(sorted(LANGS)))
        return
    print(f"{solved} solved, {total - solved} remaining, across {len(counts)} question banks ({LANGS[lang][1]})")


COUNT_HEADERS = {"Questions", "Solved", "Remaining"}
PROGRESS = "**Progress:**"


def update_readme(counts, solved, total):
    """Write Solved and Remaining columns, plus an overall progress line."""
    readme = ROOT / "README.md"
    out, width = [], 0
    for line in readme.read_text().splitlines():
        if line.startswith(PROGRESS):
            continue
        c = cells(line) if line.startswith("|") else []
        m = re.search(r"\]\(([^)]+/questionbank\.md)\)", line)
        if c and c[0] == "Topic":
            c = [x for x in c if x not in COUNT_HEADERS] + ["Solved", "Remaining"]
            width = len(c)
            line = "| " + " | ".join(c) + " |"
        elif c and width and set(line) <= set("|-"):
            line = "|" + "---|" * width
        elif c and m and m.group(1) in counts:
            s, t = counts[m.group(1)]
            c = [x for x in c if not re.fullmatch(r"\d+( / \d+)?", x)] + [str(s), str(t - s)]
            line = "| " + " | ".join(c) + " |"
        out.append(line)

    # Put the overall progress line after the intro paragraph, replacing any old one.
    while out[3:4] == [""] and out[4:5] == [""]:
        del out[3]
    out[3:3] = ["", f"{PROGRESS} {solved} solved, {total - solved} remaining, out of {total} problems."]
    readme.write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
