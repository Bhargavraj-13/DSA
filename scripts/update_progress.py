#!/usr/bin/env python3
"""Sync every questionbank.md with its solution files.

First run, pick your language (saved in .dsa.json):
    python3 scripts/update_progress.py --lang java

After that, just run:
    python3 scripts/update_progress.py

- Creates a blank solution file for any problem that does not have one yet.
- Marks a problem ✅ once its solution file contains code beyond the template.
  A problem that appears in several topics is ticked in all of them once you
  solve it in any one, and links to that solution.
- Writes each topic's prerequisites at the top of its question bank.
- Updates the progress line and the Solved and Remaining columns in README.md.
"""
import argparse, json, os, re
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

# Topics to finish before starting each topic (folder paths from the repo root).
C, A = "concepts/", "algorithms/"
PREREQS = {
    C + "01-arrays": [],
    C + "02-strings": [C + "01-arrays"],
    C + "03-hashmap": [C + "01-arrays", C + "02-strings"],
    C + "04-pointers/two-pointers": [C + "01-arrays", C + "02-strings"],
    C + "04-pointers/sliding-window": [C + "04-pointers/two-pointers", C + "03-hashmap"],
    C + "05-binary-search": [C + "01-arrays"],
    C + "06-stacks-and-queues": [C + "01-arrays", C + "02-strings"],
    C + "07-linked-lists": [C + "04-pointers/two-pointers"],
    C + "08-recursion": [C + "07-linked-lists"],
    C + "09-backtracking": [C + "08-recursion"],
    C + "10-trees": [C + "08-recursion", C + "06-stacks-and-queues"],
    C + "11-heaps": [C + "10-trees"],
    C + "12-tries": [C + "10-trees", C + "03-hashmap"],
    C + "13-dfs": [C + "08-recursion", C + "10-trees"],
    C + "14-bfs": [C + "06-stacks-and-queues", C + "10-trees"],
    C + "15-graphs": [C + "13-dfs", C + "14-bfs"],
    C + "16-greedy": [C + "01-arrays", C + "11-heaps"],
    C + "17-dp": [C + "08-recursion", C + "09-backtracking"],
    C + "18-bit-manipulation": [C + "01-arrays"],
    C + "19-math": [C + "01-arrays"],
    A + "01-kadane": [C + "01-arrays"],
    A + "02-prefix-sum-difference-array": [C + "01-arrays", C + "03-hashmap"],
    A + "03-boyer-moore-voting": [C + "01-arrays"],
    A + "04-merge-sort": [C + "08-recursion"],
    A + "05-quick-sort-quickselect": [C + "08-recursion", C + "04-pointers/two-pointers"],
    A + "06-floyd-cycle-detection": [C + "07-linked-lists"],
    A + "07-kmp": [C + "02-strings"],
    A + "08-rabin-karp": [C + "02-strings", C + "03-hashmap", C + "05-binary-search"],
    A + "09-z-algorithm": [A + "07-kmp"],
    A + "10-manacher": [C + "02-strings"],
    A + "11-union-find": [C + "15-graphs"],
    A + "12-topological-sort": [C + "15-graphs"],
    A + "13-dijkstra": [C + "15-graphs", C + "11-heaps"],
    A + "14-bellman-ford": [C + "15-graphs", A + "13-dijkstra"],
    A + "15-floyd-warshall": [C + "15-graphs", C + "17-dp"],
    A + "16-mst-prim-kruskal": [A + "11-union-find", C + "11-heaps"],
    A + "17-tarjan-bridges-scc": [C + "13-dfs", C + "15-graphs"],
    A + "18-segment-tree-fenwick": [C + "10-trees", C + "08-recursion"],
    A + "19-sieve-and-gcd": [C + "19-math"],
}
PREREQ_LABEL = "**Prerequisites:**"

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


def is_row(c):
    return len(c) >= 5 and c[1].isdigit()


def read_banks():
    """Return {folder: (bank path, topic name, lines)}, concepts before algorithms."""
    banks = {}
    paths = sorted(ROOT.glob("*/**/questionbank.md"),
                   key=lambda p: (p.relative_to(ROOT).parts[0] != "concepts", p.relative_to(ROOT).as_posix()))
    for bank in paths:
        lines = bank.read_text().splitlines()
        banks[bank.parent.relative_to(ROOT).as_posix()] = (bank, lines[0].lstrip("# ").strip(), lines)
    return banks


def prereq_line(folder, banks):
    here = banks[folder][0].parent
    links = [f"[{banks[p][1]}]({os.path.relpath(banks[p][0], here)})" for p in PREREQS.get(folder, []) if p in banks]
    return f"{PREREQ_LABEL} " + (", ".join(links) if links else "None, start here.")


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

    banks = read_banks()

    # Pass 1: make sure every problem has a file, and find which files have code.
    own, solved_at = {}, {}
    if lang:
        for folder, (bank, topic, lines) in banks.items():
            for line in lines:
                c = cells(line) if line.startswith("|") else []
                if not is_row(c):
                    continue
                num, (title, url), diff = c[1], re.match(r"\[(.+)\]\((.+)\)", c[2]).groups(), c[3]
                slug = url.rstrip("/").rsplit("/", 1)[-1]
                sol = bank.parent / f"{int(num):04d}-{slug}.{LANGS[lang][0]}"
                if not sol.exists():
                    sol.write_text(template(lang, ai_note, num=num, title=title, url=url, diff=diff, topic=topic))
                own[(folder, num)] = sol
                if has_code(sol, lang):
                    solved_at.setdefault(num, (sol, topic))

    # Pass 2: rewrite each question bank.
    counts, all_nums = {}, set()
    for folder, (bank, topic, lines) in banks.items():
        out, solved, total = [], 0, 0
        for line in lines:
            c = cells(line) if line.startswith("|") else []
            if line.startswith(PREREQ_LABEL):
                continue
            if c and c[0] == "Done":
                out.append(HEADER)
            elif c and set(line) <= set("|-"):
                out.append(DIVIDER)
            elif is_row(c):
                num = c[1]
                all_nums.add(num)
                link, done = "", False
                if lang:
                    sol = own[(folder, num)]
                    name = LANGS[lang][1]
                    if has_code(sol, lang):
                        done, link = True, f"[{name}]({sol.name})"
                    elif num in solved_at:
                        other, other_topic = solved_at[num]
                        done, link = True, f"[{name} ({other_topic})]({os.path.relpath(other, bank.parent)})"
                    else:
                        link = f"[{name}]({sol.name})"
                solved += done
                total += 1
                out.append(f"| {'✅' if done else '☐'} | {num} | {c[2]} | {c[3]} | {c[4]} | {link} |")
            else:
                out.append(line)
        # Prerequisites go right after the focus line (title, blank, focus, blank).
        while out[3:5] == ["", ""]:
            del out[3]
        out[4:4] = [prereq_line(folder, banks), ""]
        bank.write_text("\n".join(out) + "\n")
        counts[bank.relative_to(ROOT).as_posix()] = (solved, total)

    solved_unique = len(solved_at)
    update_readme(banks, counts, solved_unique, len(all_nums))

    if not lang:
        print("No language chosen yet. Run: python3 scripts/update_progress.py --lang <language>")
        print("Languages:", ", ".join(sorted(LANGS)))
        return
    print(f"{solved_unique} solved, {len(all_nums) - solved_unique} remaining, "
          f"out of {len(all_nums)} problems ({LANGS[lang][1]})")


COUNT_HEADERS = {"Questions", "Solved", "Remaining"}
PROGRESS = "**Progress:**"


def update_readme(banks, counts, solved, total):
    """Write Solved, Remaining and Start after columns, plus an overall progress line."""
    readme = ROOT / "README.md"
    out, width, start_col = [], 0, None
    for line in readme.read_text().splitlines():
        if line.startswith(PROGRESS):
            continue
        c = cells(line) if line.startswith("|") else []
        m = re.search(r"\]\(([^)]+)/questionbank\.md\)", line)
        if c and c[0] == "Topic":
            c = [x for x in c if x not in COUNT_HEADERS] + ["Solved", "Remaining"]
            width, start_col = len(c), (c.index("Start after") if "Start after" in c else None)
            line = "| " + " | ".join(c) + " |"
        elif c and width and set(line) <= set("|-"):
            line = "|" + "---|" * width
        elif c and m and f"{m.group(1)}/questionbank.md" in counts:
            s, t = counts[f"{m.group(1)}/questionbank.md"]
            c = [x for x in c if not re.fullmatch(r"\d+( / \d+)?", x)] + [str(s), str(t - s)]
            if start_col is not None:
                c[start_col] = ", ".join(banks[p][1] for p in PREREQS.get(m.group(1), []) if p in banks) or "None"
            line = "| " + " | ".join(c) + " |"
        out.append(line)

    # Put the overall progress line after the intro paragraph, replacing any old one.
    while out[3:4] == [""] and out[4:5] == [""]:
        del out[3]
    out[3:3] = ["", f"{PROGRESS} {solved} solved, {total - solved} remaining, out of {total} problems."]
    readme.write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
