#!/usr/bin/env bash
# cut_bundle.sh <rev>
# Cut a full-programme bundle cr_work_r<rev>.tar.gz into /root, matching the
# convention: internal top dir is cr_r988/, build cruft + in-session backups excluded.
# Usage:  bash scripts/cut_bundle.sh 1062
set -euo pipefail
rev="${1:?usage: cut_bundle.sh <rev>}"
# programme root is the dir containing this scripts/ folder.
# The on-disk dir name is a stale artifact (a past revision frozen in); the
# bundle's top dir is renamed to the CURRENT revision, cr_r<rev>, since the
# programme is one continuous revision counter.
prog_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
parent_dir="$(dirname "$prog_dir")"
prog_name="$(basename "$prog_dir")"
out="/root/cr_r${rev}.tar.gz"

tar czf "$out" \
  --directory="$parent_dir" \
  --transform="s,^${prog_name},cr_r${rev}," \
  --exclude='*.aux' --exclude='*.log' --exclude='*.fls' \
  --exclude='*.fdb_latexmk' --exclude='*.out' --exclude='*.synctex.gz' \
  --exclude='*.toc' --exclude='*.bbl' --exclude='*.blg' \
  --exclude='*.pre_P13CP' --exclude='*.pre_*' \
  --exclude='__pycache__' \
  "$prog_name"

echo "wrote $out ($(du -h "$out" | cut -f1))"
echo "top dir: $(tar tzf "$out" | head -1)"
