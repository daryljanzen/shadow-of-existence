#!/usr/bin/env bash
# record_run.sh <project-dir> <out-file>
# r7265+71: a run record a reader can check where the build cannot be re-run.
# Removes the project's OWN .lake/build (never its packages: `lake clean` invalidated
# mathlib's cached build here and started a from-source rebuild), rebuilds, runs
# check_no_sorry.py, and writes everything raw -- toolchain, dependency SHAs, the
# full build output and the checker's full stdout -- to <out-file>.
set -u
here="$(cd "$(dirname "$0")" && pwd)"
proj="$(cd "$1" && pwd)"; out="$2"
export PATH="$HOME/.elan/bin:$PATH"
{
  echo "# RUN RECORD -- written by computations/formalisation/record_run.sh"
  echo "# date (UTC): $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "# project: ${proj#*/shadow-of-existence/}"
  echo "# tree commit at run: $(git -C "$proj" rev-parse HEAD)"
  echo "## lean --version"; (cd "$proj" && lean --version)
  echo "## lean-toolchain"; cat "$proj/lean-toolchain"
  echo "## dependency revisions (lake-manifest.json)"
  python3 -c "import json,sys;[print(p['name'],p.get('rev')) for p in json.load(open(sys.argv[1]))['packages']]" "$proj/lake-manifest.json"
  echo "## rm -rf .lake/build (own package only) then lake build -- raw output"
  (cd "$proj" && rm -rf .lake/build; start=$(date +%s); lake build 2>&1; echo "exit=$? wall=$(( $(date +%s) - start ))s")
  echo "## python3 lean/check_no_sorry.py <project> -- raw stdout"
  (cd "$proj" && python3 "$here/lean/check_no_sorry.py" "$proj" 2>&1; echo "exit=$?")
} > "$out" 2>&1
tail -1 "$out"
