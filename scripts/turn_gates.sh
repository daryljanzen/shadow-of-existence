#!/usr/bin/env bash
# turn_gates.sh -- the gate batch a coordinating turn runs, DERIVED FROM THE GLOB.
#
# ** WHY THIS EXISTS, and it is the arbiter's own defect. **  Until r7411 the gate seat ran a
# HAND-WRITTEN list of 24 gate names every turn and reported "24 of 24 local gates green" in its
# commit messages.  The glob holds 133.  So 109 gates -- 82 per cent of them -- were never run by
# the seat that gates `main`, and the phrase it shipped read as completeness.
#   `sweep_gates.sh`'s own header had already named this failure twice, at r2427 and at r3522-r3549:
#   *"it ran three gates of ninety-three and reported 'gates green' across twenty-two commits.  A
#   subset is not a sweep, and the failure is silent in exactly the direction that feels like
#   progress."*  The arbiter was doing it while quoting the script that forbids it.
#
# ** WHAT THE FIRST FULL SWEEP FOUND (r7411). **  Of the 109 never run: 99 passed, 3 exceeded a 120 s
# probe, and SEVEN WERE RED.  Three of the seven were caused by the three revisions the seat had just
# landed -- `check_open_ledger` (open-language qualifications with no verdict, from r7401/r7407/r7409),
# `check_depmatrix` (citation counts moved by those same edits), `check_view_tables` (every row this
# phase opened widened a silent-default gap).  *** The subset excluded precisely the gates that watch
# the thing the seat was changing. ***  An eighth, `check_open_item_coherence`, was CRASHING on a
# `ValueError` for any `PO-` id and is in neither this batch's source nor `gates.yml`: a gate nobody ran.
#
# ** THE RULE THIS ENFORCES ** (70, r7405+70.2, on `run_fast_job.sh`'s hand-copied lint line):
#   *** A COPY OF A LIST IS A CLAIM ABOUT THE LIST AT THE MOMENT IT WAS COPIED. ***
#   So this script holds NO list of gates.  It globs, subtracts a declared exclusion set, and runs the
#   rest.  A gate added to `corpus/` joins this batch the day it lands, with nobody editing anything --
#   which is the failure mode that let `check_pages_current` be missed four times in one cycle.
#
# ** EXCLUSIONS ARE DECLARED WITH A REASON AND PRINTED EVERY RUN. **  An exclusion is a question not
# asked, never a question answered; the three below are excluded for MEASURED cost or for a trigger,
# and each names the instrument that does ask it.
#
# Usage:  bash scripts/turn_gates.sh            # the turn batch
#         bash scripts/turn_gates.sh --all      # no exclusions; the full glob
set -uo pipefail
cd "$(dirname "$0")/.."
export NODE="${NODE:-66}"
GATE_TIMEOUT="${GATE_TIMEOUT:-280}"

# name:reason -- reason is printed, so an exclusion cannot be silent.
EXCLUDE_NAMES="check_quote_pins check_cross_row_dupes check_tilt_pins check_receipts_run check_compile"
reason_for() {
  case "$1" in
    check_quote_pins)      echo "947s measured (r7343); run when the LEDGER moves -- sweep_gates.sh asks it" ;;
    check_cross_row_dupes) echo "128s measured; sweep_gates.sh asks it at its 1800s budget" ;;
    check_tilt_pins)       echo "exceeded a 120s probe at r7411; the nightly backstop job asks it" ;;
    check_receipts_run)    echo "CACHED -- red whenever the tree digest moves; a 9-minute re-run, not a defect" ;;
    check_compile)         echo "needs pdflatex and is the compile job's question, not the turn's" ;;
    *)                     echo "no reason recorded -- THIS IS A DEFECT, add one" ;;
  esac
}

ALL=0; [ "${1:-}" = "--all" ] && ALL=1
pass=0; fail=0; unrun=0; failed=""; notrun=""; ran=0
: > /tmp/_tg_roster.$$
for g in corpus/check_*.py; do
  n=$(basename "$g" .py)
  if [ "$ALL" -eq 0 ]; then
    case " $EXCLUDE_NAMES " in *" $n "*) continue;; esac
  fi
  timeout "$GATE_TIMEOUT" python3 -W ignore "$g" >/tmp/_tg.$$ 2>&1 </dev/null; rc=$?
  echo "$n" >> /tmp/_tg_roster.$$; ran=$((ran+1))
  if [ $rc -eq 124 ]; then unrun=$((unrun+1)); notrun="$notrun $n(timeout>${GATE_TIMEOUT}s)"
  elif [ $rc -eq 0 ]; then pass=$((pass+1))
  else fail=$((fail+1)); failed="$failed $n"; fi
  rm -f /tmp/_tg.$$
done

# ** THE ROSTER ASSERTION. **  The set run must be exactly glob-minus-exclusions.  A count is not a
#   roster (r7341): this batch states which names it ran and fails if that set is not the expected one.
expect=$(for g in corpus/check_*.py; do n=$(basename "$g" .py)
           if [ "$ALL" -eq 0 ]; then case " $EXCLUDE_NAMES " in *" $n "*) continue;; esac; fi
           echo "$n"; done | sort)
actual=$(sort /tmp/_tg_roster.$$); rm -f /tmp/_tg_roster.$$
missing=$(comm -23 <(echo "$expect") <(echo "$actual") | tr '\n' ' ')
NGLOB=$(ls corpus/check_*.py | wc -l | tr -d ' ')
NEXP=$(echo "$expect" | grep -c .)

echo "  turn batch: ran $ran of $NEXP expected   (glob holds $NGLOB)   [NODE=$NODE, timeout=${GATE_TIMEOUT}s]"
echo "  PASS=$pass  FAIL=$fail  UNRUN=$unrun"
rcout=0
if [ "$ran" -ne "$NEXP" ] || [ -n "${missing// /}" ]; then
  echo "  ⛔ ROSTER MISMATCH -- THIS RUN IS NOT A RESULT.  never ran:$missing"; rcout=1
fi
for n in $failed; do echo "      [FAIL]  $n"; done
for n in $notrun; do echo "      [UNRUN] $n"; done
if [ "$ALL" -eq 0 ]; then
  echo "  EXCLUDED, each a question NOT ASKED here and asked elsewhere:"
  for n in $EXCLUDE_NAMES; do printf '      %-24s %s\n' "$n" "$(reason_for "$n")"; done
fi
[ "$fail" -gt 0 ] && rcout=1
exit $rcout
