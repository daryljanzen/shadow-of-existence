#!/usr/bin/env bash
# cut_bundle_two_part.sh <rev-label>
#
# Cut a FULL programme bundle in TWO parts, each well under 30 MB, with NO FILE
# SPLIT ACROSS PARTS.  Written r2376+c54.151 because the split was being done by
# hand each revision and the hand version had once cut a file in half.
#
#   part1_corpus   : top-level files + corpus/ figures/ receipts/ verification/
#   part2_working  : every other top-level directory
#
# Together the two parts are the whole tree, minus build cruft and .git.
# Usage:  bash scripts/cut_bundle_two_part.sh 'r2376+c54.151'
set -euo pipefail
rev="${1:?usage: cut_bundle_two_part.sh <rev-label>}"

prog_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
parent_dir="$(dirname "$prog_dir")"
prog_name="$(basename "$prog_dir")"

EXCLUDES=(
  --exclude='*.aux' --exclude='*.log' --exclude='*.fls'
  --exclude='*.fdb_latexmk' --exclude='*.out' --exclude='*.synctex.gz'
  --exclude='*.toc' --exclude='*.bbl' --exclude='*.blg'
  --exclude='*.pre_*' --exclude='__pycache__' --exclude='.git'
)

P1_DIRS=(corpus figures receipts verification)

cd "$parent_dir"

# --- part 1: top-level regular files, plus the four corpus-side directories ---
mapfile -t topfiles < <(find "$prog_name" -maxdepth 1 -type f -printf '%p\n' | sort)
out1="/root/CR_bundle_${rev}_part1_corpus.tar.xz"
tar cJf "$out1" "${EXCLUDES[@]}" \
  "${topfiles[@]}" \
  "${P1_DIRS[@]/#/$prog_name/}"

# --- part 2: every other top-level directory ---
mapfile -t p2dirs < <(
  find "$prog_name" -maxdepth 1 -mindepth 1 -type d -printf '%f\n' | sort |
  grep -v -x -e corpus -e figures -e receipts -e verification -e .git
)
out2="/root/CR_bundle_${rev}_part2_working.tar.xz"
tar cJf "$out2" "${EXCLUDES[@]}" "${p2dirs[@]/#/$prog_name/}"

for f in "$out1" "$out2"; do
  sz=$(stat -c%s "$f")
  printf '%s  %s bytes (%s)\n' "$f" "$sz" "$(du -h "$f" | cut -f1)"
  if [ "$sz" -ge 31457280 ]; then echo "  ⛔ OVER 30 MB"; exit 1; fi
done
echo "both parts under 30 MB"
