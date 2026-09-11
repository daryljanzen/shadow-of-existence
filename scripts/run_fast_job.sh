#!/usr/bin/env bash
# run_fast_job.sh -- run the `fast` CI job LOCALLY, with its lists READ FROM gates.yml.
#
# ** WHY THIS EXISTS, AND IT IS THIS LINE'S OWN DEFECT TWICE IN ONE SESSION. **
#
# `sweep_gates.sh` runs every `corpus/check_*.py` and NOTHING ELSE.  The `fast` job also runs
# ten `scripts/` generators with `--check` and a hollow-assertion lint.  ⇒ At r6478 two CI
# failures landed that the sweep could not see, because BOTH were in those ten.
#
# ⛔ AND THE OBVIOUS REMEDY -- "run the gate list too" -- FAILED THE NEXT TIME, for a different
#   reason: the list was TRANSCRIBED BY HAND into a shell loop.  main added `check_pages_current`
#   while this branch was open; the copied list did not have it; the local run was green and CI
#   was red on the one gate the copy predated.
#     ⇒ *** A COPY OF A LIST IS A CLAIM ABOUT THE LIST AT THE MOMENT IT WAS COPIED. ***  The
#       first failure was a list that was too SHORT; the second was a list that was too OLD.
#       Widening the copy fixes neither, because the defect is the copying.
#
# ⌗ ** So this script holds no list at all. **  It parses the `for g in ...` and `for c in ...`
#   loops out of `.github/workflows/gates.yml` and runs exactly what CI will run.  A gate added
#   to the workflow is picked up here on the next invocation, by nobody, which is the point.
#
# ⚠ ** It does NOT replace `sweep_gates.sh` ** -- that answers a different question (every gate in
#   the tree, including ones CI does not run) and its NODE/timeout/UNRUN specification is its own.
#   *Two instruments, two questions.  This one answers: "will the fast job be green?"*
#
# Usage:  bash scripts/run_fast_job.sh
# Exit 0 if the fast job would pass, 1 otherwise.
set -uo pipefail
cd "$(dirname "$0")/.."

WF=".github/workflows/gates.yml"
[ -f "$WF" ] || { echo "  ⛔ $WF not found -- this script reads CI's own lists and has none of its own."; exit 2; }

eval "$(python3 - "$WF" <<'PY'
import re, sys
s = open(sys.argv[1], encoding='utf-8').read()
gates, gens = [], []
for m in re.finditer(r'for (\w+) in ((?:[^;]|\n)*?); do', s):
    var, body = m.group(1), m.group(2)
    toks = [t for t in re.split(r'\s+|\\\n', body) if t and not t.startswith('#') and t != '\\']
    (gates if var == 'g' else gens if var == 'c' else []).extend(toks)
print('GENS="%s"' % ' '.join(dict.fromkeys(gens)))
print('GATES="%s"' % ' '.join(dict.fromkeys(gates)))
PY
)"

export NODE="${NODE:-ci}"
# The workflow sets this so check_compile reports UNRUN rather than demanding a toolchain; the
# compile question is asked in the `compile` job, which has texlive.  Declared, not defaulted.
export COMPILE_UNRUN_OK="${COMPILE_UNRUN_OK:-the \`compile\` job -- texlive-full, on main and on schedule}"

echo
echo "  RUN-FAST-JOB -- lists read from $WF, never from this file"
echo "    $(echo $GENS | wc -w) generator(s), $(echo $GATES | wc -w) gate(s), plus the hollow-assertion lint"
echo

fails=""
for c in $GENS; do
  python3 "scripts/$c.py" --check >/dev/null 2>&1 || fails="$fails $c"
done
for g in $GATES; do
  timeout 420 python3 -W ignore "corpus/$g.py" >/dev/null 2>&1 || fails="$fails $g"
done
python3 scripts/lint_assertions.py >/dev/null 2>&1 || fails="$fails lint_assertions"

if [ -n "$fails" ]; then
  echo "  ⛔ THE FAST JOB WOULD BE RED:$fails"
  echo "     Re-run the named one alone for its output."
  echo
  exit 1
fi
echo "  every step of the fast job passes on this tree."
echo "  ⌗ Green here is a claim about CI's CURRENT list, because the list was read and not remembered."
echo
exit 0
