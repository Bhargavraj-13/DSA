#!/usr/bin/env bash
# Tick finished problems, then commit and push.
# Usage: ./scripts/submit.sh "Solve LC 121"
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/update_progress.py
git add -- README.md concepts algorithms scripts

if git diff --cached --quiet; then
  echo "Nothing new to commit."
  exit 0
fi

git commit -m "${1:-Add solutions}"
git push -u origin "$(git branch --show-current)"
