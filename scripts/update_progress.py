#!/usr/bin/env python3
"""Sync every questionbank.md with its solution files.

- Creates a C++ template for any problem that does not have a solution file yet.
- Marks a problem ✅ once its .cpp file contains code beyond the template.
- Updates the "Solved" column in the root README.md.

Run it from anywhere: python3 scripts/update_progress.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADER = "| Done | # | Problem | Difficulty | Key idea | Solution |"
DIVIDER = "|---|---|---|---|---|---|"

TEMPLATE = """\
// {num}. {title}
// {url}
// Difficulty: {diff} | Topic: {topic}

#include <bits/stdc++.h>
using namespace std;

// Write your solution below this line.


/*
Explanation:


Complexity:
  Time:
  Space:

Dry run:

Note:
  The solution is my own. I used AI to help write this explanation, so my
  ideas are explained in a clear, standard way that anyone can follow.
*/
"""


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def has_code(path):
    """True when the file has a line that is not a comment, include or using."""
    text = re.sub(r"/\*.*?\*/", "", path.read_text(), flags=re.S)
    for line in text.splitlines():
        line = line.split("//", 1)[0].strip()
        if line and not line.startswith("#") and not line.startswith("using "):
            return True
    return False


def sync_bank(bank):
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
            slug = url.rstrip("/").rsplit("/", 1)[-1]
            sol = bank.parent / f"{int(num):04d}-{slug}.cpp"
            if not sol.exists():
                sol.write_text(TEMPLATE.format(num=num, title=title, url=url, diff=diff, topic=topic))
            done = has_code(sol)
            solved += done
            total += 1
            mark = "✅" if done else "☐"
            out.append(f"| {mark} | {num} | {problem} | {diff} | {idea} | [C++]({sol.name}) |")
        else:
            out.append(line)
    bank.write_text("\n".join(out) + "\n")
    return solved, total


def main():
    counts = {}
    for bank in sorted(ROOT.glob("*/**/questionbank.md")):
        counts[bank.relative_to(ROOT).as_posix()] = sync_bank(bank)

    readme = ROOT / "README.md"
    out = []
    for line in readme.read_text().splitlines():
        m = re.search(r"\]\(([^)]+/questionbank\.md)\)", line)
        if line.startswith("|") and m and m.group(1) in counts:
            s, t = counts[m.group(1)]
            line = line.rsplit("|", 2)[0] + f"| {s} / {t} |"
        elif line.startswith("| Topic |"):
            line = line.rsplit("|", 2)[0] + "| Solved |"
        out.append(line)
    readme.write_text("\n".join(out) + "\n")

    solved = sum(s for s, _ in counts.values())
    total = sum(t for _, t in counts.values())
    print(f"{solved} / {total} solved across {len(counts)} question banks")


if __name__ == "__main__":
    main()
