#!/usr/bin/env bash
# sweep_gates.sh -- run EVERY corpus/check_*.py and report pass/fail as one number.
#
# WHY THIS EXISTS.  At r2427 a line reported "twenty gates rc=0" from running them one
# at a time locally while CI had been red for twelve revisions.  At r3522-r3549 this
# line did the same thing: it ran three gates of ninety-three and reported "gates
# green" across twenty-two commits.  A subset is not a sweep, and the failure is
# silent in exactly the direction that feels like progress.
#
# Usage:  bash scripts/sweep_gates.sh [--baseline <git-ref>]
#   With --baseline, also runs the sweep at that ref and prints the DIFFERENCE,
#   which is the only number that says whether THIS work broke anything.
set -uo pipefail
cd "$(dirname "$0")/.."

run_sweep() {
  local pass=0 fail=0 failed=""
  for g in corpus/check_*.py; do
    local n; n=$(basename "$g" .py)
    if timeout 120 python3 -W ignore "$g" >/dev/null 2>&1; then
      pass=$((pass+1))
    else
      fail=$((fail+1)); failed="$failed $n"
    fi
  done
  echo "$pass|$fail|$failed"
}

echo "  sweeping $(ls corpus/check_*.py | wc -l) gates ..."
IFS='|' read -r P F FAILED <<< "$(run_sweep)"
echo "  HERE:  PASS=$P  FAIL=$F"
for n in $FAILED; do echo "      [FAIL] $n"; done

if [ "${1:-}" = "--baseline" ] && [ -n "${2:-}" ]; then
  ref="$2"; tmp=$(mktemp -d)
  git clone -q . "$tmp/base" 2>/dev/null && (cd "$tmp/base" && git checkout -q "$ref" 2>/dev/null)
  if [ -d "$tmp/base/corpus" ]; then
    pushd "$tmp/base" >/dev/null
    IFS='|' read -r BP BF BFAILED <<< "$(run_sweep)"
    popd >/dev/null
    echo
    echo "  BASE ($ref):  PASS=$BP  FAIL=$BF"
    echo "  DELTA: $((F - BF)) newly failing gate(s) attributable to work since $ref"
    for n in $FAILED; do
      case " $BFAILED " in *" $n "*) ;; *) echo "      [NEW] $n -- introduced since $ref";; esac
    done
  fi
  rm -rf "$tmp"
fi
echo
echo "  A gate failing here is not automatically this line's: check the delta, not the count."
[ "$F" -eq 0 ]
