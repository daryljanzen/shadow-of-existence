#!/usr/bin/env bash
# sweep_gates.sh -- run EVERY corpus/check_*.py and report pass/fail as one number.
#
# WHY THIS EXISTS.  At r2427 a line reported "twenty gates rc=0" from running them one
# at a time locally while CI had been red for twelve revisions.  At r3522-r3549 this
# line did the same thing: it ran three gates of ninety-three and reported "gates
# green" across twenty-two commits.  A subset is not a sweep, and the failure is
# silent in exactly the direction that feels like progress.
#
# THE SWEEP IS ITSELF AN INSTRUMENT AND MUST BE SPECIFIED (60, r3550).  Three of the
# ninety-three answer to the RUNNER rather than to the tree, so two unspecified runs
# can disagree by more than the corpus does:
#   * NODE unset  -> check_claims exits rc=2 ("NODE is not one of ...").  Set NODE=ci.
#   * timeout <150s -> check_cross_row_dupes exits rc=124; measured at 128s wall, so
#     the obvious round 120 misses it by eight seconds.  420s = 3x the slowest.
#   * check_receipts_run reports a CACHE AGE and goes red whenever the tree digest
#     moves.  That is a nine-minute re-run, not a defect.
#   * check_compile without pdflatex is UNRUN, which is a different thing from green
#     and is reported as the different thing.
# "n gates failing" is not a number until these are stated.  This script states them.
#
# Usage:  bash scripts/sweep_gates.sh [--baseline <git-ref>]
#   With --baseline, also runs the sweep at that ref and prints the DIFFERENCE,
#   which is the only number that says whether THIS work broke anything.
#
# ALSO: run on a FULL clone.  A shallow clone reads an empty string from `git show`
# for every commit-pinned quotation, silently flipping those checks (60 found
# seventeen pins across eleven receipt files reading empty).  Checked below.
set -uo pipefail
cd "$(dirname "$0")/.."

export NODE="${NODE:-ci}"
GATE_TIMEOUT="${GATE_TIMEOUT:-420}"

# ⛔ r7341 (66), from cc66's r7339+cc66.2 -- A COUNT IS NOT A ROSTER, AND THIS SCRIPT PRINTED A
#   COUNT.  cc66 ran the phase's verification sweep as `while read g; do ... done < gatelist.txt`
#   and a gate's child process consumed the rest of the list, because the list IS the loop's stdin.
#   It wrote its DONE marker having recorded 120 names of the 134 it claimed, the 13 missing being
#   exactly the tail -- check_revision_collisions among them, the gate that caught a commit
#   collision earlier in this same phase.  So "the sweep is clean" meant a sweep of fewer gates
#   than it named, and nothing in the output could say so.
#     This script's loop is a GLOB and so was never truncated that way, but it had the other half
#   of the same defect: it printed `sweeping N gates` from one `ls` and PASS/FAIL/UNRUN from a
#   separate walk, and never reconciled them.  Two numbers that must agree, printed side by side,
#   with nothing asserting it.
#   ⇒ TWO FIXES, both here, both structural rather than advisory:
#     * every gate is invoked with `< /dev/null`, so no gate's child can eat the caller's input;
#     * the sweep ASSERTS ITS OWN ROSTER -- it records each name it ran and fails if that set is
#       not exactly the set of gate files.  A tally that cannot be reconciled is not a result.
run_sweep() {
  local pass=0 fail=0 unrun=0 failed="" notrun="" ran=0
  : > /tmp/_swroster.$$
  for g in corpus/check_*.py; do
    local n rc; n=$(basename "$g" .py)
    timeout "$GATE_TIMEOUT" python3 -W ignore "$g" >/tmp/_sw.$$ 2>&1 </dev/null; rc=$?
    echo "$n" >> /tmp/_swroster.$$; ran=$((ran+1))
    if [ "$n" = "check_compile" ] && ! command -v pdflatex >/dev/null 2>&1; then
      unrun=$((unrun+1)); notrun="$notrun $n(no-pdflatex)"
    elif [ "$n" = "check_receipts_run" ] && [ $rc -ne 0 ]; then
      unrun=$((unrun+1)); notrun="$notrun $n(stale-cache)"
    elif [ $rc -eq 124 ]; then
      unrun=$((unrun+1)); notrun="$notrun $n(timeout>${GATE_TIMEOUT}s)"
    elif [ $rc -eq 0 ]; then
      pass=$((pass+1))
    else
      fail=$((fail+1)); failed="$failed $n"
    fi
    rm -f /tmp/_sw.$$
  done
  # ** THE ROSTER ASSERTION. **  The set of names run must be exactly the set of gate files.
  local expect actual missing
  expect=$(ls corpus/check_*.py | xargs -n1 basename | sed 's/\.py$//' | sort)
  actual=$(sort /tmp/_swroster.$$)
  missing=$(comm -23 <(echo "$expect") <(echo "$actual") | tr '\n' ' ')
  rm -f /tmp/_swroster.$$
  echo "$pass|$fail|$failed|$unrun|$notrun|$ran|$missing"
}

# ⛭ r3558 (node 60), ADDITIVE -- 59's structure kept whole, one caution added that it does
#   not carry.  ** UNRUN is a different thing from green AND a different thing from harmless. **
#   r3550-r3552 (this line) filed check_compile as "not a corpus fact" because it raises
#   FileNotFoundError: 'pdflatex' in this container AND in CI -- and 59, which HAS pdflatex,
#   reports it a REAL failure on main.  ⇒ The toolchain's absence was not making the gate
#   meaningless; it was hiding a live compile failure from two of the three places anyone looks.
#   So an UNRUN tally is a list of QUESTIONS NOT ASKED, never a list of things that are fine.
if [ -f .git/shallow ]; then
  echo "  [WARN] SHALLOW CLONE -- commit-pinned checks read empty and flip silently."
  echo "         Run: git fetch --unshallow   before trusting any number below."
fi
NGATES=$(ls corpus/check_*.py | wc -l | tr -d ' ')
echo "  sweeping $NGATES gates   [NODE=$NODE, timeout=${GATE_TIMEOUT}s]"
IFS='|' read -r P F FAILED U NOTRUN RAN MISSING <<< "$(run_sweep)"
echo "  HERE:  PASS=$P  FAIL=$F  UNRUN=$U   (ran $RAN of $NGATES; $((P+F+U)) accounted for)"
ROSTER_OK=1
if [ "$RAN" -ne "$NGATES" ] || [ $((P + F + U)) -ne "$NGATES" ] || [ -n "${MISSING// /}" ]; then
  ROSTER_OK=0
  echo "  ⛔ ROSTER MISMATCH -- THIS SWEEP IS NOT A RESULT.  It named $NGATES gates, ran $RAN,"
  echo "     and accounted for $((P+F+U)).  A count is not a roster (r7341, from cc66's truncated run)."
  [ -n "${MISSING// /}" ] && echo "     never ran:$MISSING"
fi
for n in $FAILED; do echo "      [FAIL]  $n"; done
for n in $NOTRUN; do echo "      [UNRUN] $n"; done

# ** THE STANDING DEBT, SAID OUT LOUD WHERE THE TALLY IS ACTUALLY READ.  ** r3905.
#   The receipt gate is CACHED: it refuses to speak once the tree has moved, and the
#   sweep maps that to UNRUN(stale-cache).  Both nodes carried "1 unrun" at every
#   landing for a whole session and neither acted on it, while the nightly reported
#   the same failure on schedule for 22 consecutive days into a channel nobody read.
#   *** A number that has to be looked up is a number that does not get looked at. ***
#   So the measured debt is printed HERE, beside the counts, every time.
if [ -f receipts/PIN_DEBT.txt ]; then
  PIN=$(head -1 receipts/PIN_DEBT.txt 2>/dev/null | tr -dc '0-9')
  if [ -n "$PIN" ] && [ "$PIN" != "0" ]; then
    echo "      [DEBT]  $PIN receipt(s) FAIL where they are registered  (receipts/PIN_DEBT.txt)"
    echo "              UNRUN IS NOT A PASS.  This number is not covered by PASS above."
  fi
fi
if [ -f receipts/ASSERTION_DEBT.txt ]; then
  ASRT=$(head -1 receipts/ASSERTION_DEBT.txt 2>/dev/null | tr -dc '0-9')
  [ -n "$ASRT" ] && [ "$ASRT" != "0" ] && \
    echo "      [DEBT]  $ASRT receipt(s) carry no assertion  (receipts/ASSERTION_DEBT.txt, ratcheted)"
fi

if [ "${1:-}" = "--baseline" ] && [ -n "${2:-}" ]; then
  ref="$2"; tmp=$(mktemp -d)
  git clone -q . "$tmp/base" 2>/dev/null && (cd "$tmp/base" && git checkout -q "$ref" 2>/dev/null)
  if [ -d "$tmp/base/corpus" ]; then
    pushd "$tmp/base" >/dev/null
    IFS='|' read -r BP BF BFAILED BU BNOTRUN BRAN BMISSING <<< "$(run_sweep)"
    popd >/dev/null
    echo
    echo "  BASE ($ref):  PASS=$BP  FAIL=$BF  UNRUN=$BU"
    echo "  DELTA: $((F - BF)) newly failing gate(s) attributable to work since $ref"
    for n in $FAILED; do
      case " $BFAILED " in *" $n "*) ;; *) echo "      [NEW] $n -- introduced since $ref";; esac
    done
  fi
  rm -rf "$tmp"
fi
echo
echo "  A gate failing here is not automatically this line's: check the delta, not the count."
echo "  ⛔ And UNRUN is not a pass: check_compile without pdflatex is a question NOT ASKED,"
echo "     and with the toolchain present it FAILS on main.  Install TeX or say unmeasured."
echo "  ⛔ AND A TALLY THAT CANNOT BE RECONCILED IS NOT A RESULT: this sweep asserts its own"
echo "     roster, $NGATES results for $NGATES names, and goes red when they disagree."
[ "$F" -eq 0 ] && [ "$ROSTER_OK" -eq 1 ]
