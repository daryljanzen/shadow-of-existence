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

# ** r7457, ON 70's r7453+70.2: THE EXCLUSION LIST WAS SIX STATED REASONS AND FOUR WERE WRONG. **
#   70 re-measured all six here and in CI.  What it found, and every change below is its
#   proposal applied rather than a fresh judgement:
#     - `check_tilt_pins` was excluded because "the nightly backstop job asks it".  The
#       backstop is MONTHLY (`0 4 1 * *`), its tilt step was wired on 2026-10-02 -- ONE DAY
#       AFTER the last firing -- and no dispatch has run since 09-28.  *** SO THE GATE WAS
#       EXCLUDED FROM THE TURN AND ASKED NOWHERE, and the next asking was 2026-11-01. ***
#       At 170s it is under this timeout.  DROPPED FROM THE LIST, which is also what puts it
#       back where it is asked: the roster is a glob, so dropping a name IS adding the gate.
#     - `check_cross_row_dupes` measured 145s, half the timeout, and `sweep_gates.sh` -- the
#       instrument its reason named as asking it -- is in NO workflow.  DROPPED.
#     - `check_compile`'s reason is false on this container: `pdflatex` IS here and the gate
#       is green in 51s.  `check_sitemap_resolves` holds, but as a TEST, not an estimate.
#       Both are now DERIVED: see NEEDS below.
#   ⌗ 70's structural answer, which reversed its own registration: derivation YES for the
#     environment half, NO for the cost half.  *** ONE GATE MEASURED 947, 595, 279 AND 186
#     SECONDS ACROSS TWO CONTAINERS AND THREE DATES. ***  A declared cost is one value of a
#     quantity that has at least two at any moment, and a set derived from it would move with
#     whichever machine last wrote the number.  So cost entries stay HAND-WRITTEN AND STATE
#     BOTH VALUES WITH THEIR DATE -- and the timeout already derives the cost exclusion live,
#     printing any gate over it as [UNRUN] by name.
#
# ⛭⛭ r7457+cc66 ④: THE TABLE IS NO LONGER HERE -- IT IS THE SINGLE SOURCE BOTH GATE SCRIPTS READ.
#   `scripts/run_touched_readers.sh` carried a SECOND statement of one of these reasons, so correcting
#   this copy at r7457 left that one asserting two false things.  ⇒ `EXCLUDE_NAMES`, `reason_for` and
#   `needs_unmet` now live once, in `scripts/_gate_exclusions.sh`, with the policy note that explains
#   why the cost half is hand-written and the NEEDS half is tested.
[ -r scripts/_gate_exclusions.sh ] || { echo "  ⛔ scripts/_gate_exclusions.sh is missing -- it is the exclusion table's single source"; exit 2; }
. scripts/_gate_exclusions.sh

ALL=0; [ "${1:-}" = "--all" ] && ALL=1
# ⛭ r7457+cc66 ④: `--print-exclusions` prints the table and the roster and RUNS NOTHING.  The r7457 ⓓ
#   control -- corrupt one reason in the single source, confirm BOTH scripts print the corrupted text --
#   otherwise costs a 133-gate batch, which makes a control nobody re-runs.
if [ "${1:-}" = "--print-exclusions" ]; then
  echo
  echo "  TURN-GATES -- the exclusion table, from scripts/_gate_exclusions.sh, nothing run"
  echo
  for n in $EXCLUDE_NAMES; do echo "    [excluded, cost/trigger] $n -- $(reason_for "$n")"; done
  for g in corpus/check_*.py; do
    n=$(basename "$g" .py)
    case " $EXCLUDE_NAMES " in *" $n "*) continue;; esac
    if why=$(needs_unmet "$n"); then echo "    [skipped, precondition tested] $n ($why) -- $(reason_for "$n")"; fi
  done
  echo
  echo "    roster: $(ls corpus/check_*.py | wc -l | tr -d ' ') gate(s) in the glob, minus the names above"
  exit 0
fi
pass=0; fail=0; unrun=0; failed=""; notrun=""; ran=0
skipped_needs=""
: > /tmp/_tg_roster.$$
for g in corpus/check_*.py; do
  n=$(basename "$g" .py)
  if [ "$ALL" -eq 0 ]; then
    case " $EXCLUDE_NAMES " in *" $n "*) continue;; esac
    # A precondition TESTED, not estimated.  Printed, so a skip is never silent.
    if why=$(needs_unmet "$n"); then
      skipped_needs="$skipped_needs $n($why)"
      continue
    fi
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
#   r7457: a NEEDS skip is subtracted here too, from the SAME test the loop used -- not from
#   a second copy of the condition.  A gate whose precondition is met is expected and must run.
expect=$(for g in corpus/check_*.py; do n=$(basename "$g" .py)
           if [ "$ALL" -eq 0 ]; then
             case " $EXCLUDE_NAMES " in *" $n "*) continue;; esac
             if needs_unmet "$n" >/dev/null; then continue; fi
           fi
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
  echo "  EXCLUDED BY HAND, each a question NOT ASKED here -- reason re-measured by 70 at r7453+70.2:"
  for n in $EXCLUDE_NAMES; do printf '      %-24s %s\n' "$n" "$(reason_for "$n")"; done
  if [ -n "${skipped_needs// /}" ]; then
    echo "  SKIPPED BY A TESTED PRECONDITION (not an estimate; met => it runs):$skipped_needs"
  else
    echo "  SKIPPED BY A TESTED PRECONDITION: none -- every precondition is met here, so those gates RAN."
  fi
fi
[ "$fail" -gt 0 ] && rcout=1
exit $rcout
