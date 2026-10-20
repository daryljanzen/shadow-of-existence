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
# Usage:  bash scripts/turn_gates.sh            # LEAN: the turn batch, the push asks the heavy gates (default)
#         bash scripts/turn_gates.sh --full     # the whole batch below, about twenty minutes here
#         bash scripts/turn_gates.sh --all      # no exclusions; the full glob
#
# ** r69 (69, on Daryl's order of 2026-10-20: "trim the fat off the gates so they run more lean"). **
#   The default is now LEAN.  A turn ran 134 gates serially, about 1,210 s on this container, and
#   eleven of them were 1,085 s of it.  Every one of those eleven is ALSO run by CI's `fast` job on
#   every push, which finishes in about ten minutes and goes red on `main` where every seat can see it.
#   So a seat waiting twenty minutes for them locally was asking each question twice and waiting for
#   the slower answer.  LEAN runs the other gates (about 125 s here) and leaves those eleven to the push.
#   ⌗ The set is HEAVY_PUSHED below: named by hand with the time measured here and the date, because
#   a cost is a measurement and not a derivation (70, r7453+70.2).  Each name must also appear in the
#   `fast` job's list in gates.yml -- the script checks that, so a heavy gate dropped from CI comes
#   back into the turn the same day.  `check_compile` returns to the turn whenever a paper is edited.
set -uo pipefail
cd "$(dirname "$0")/.."
export NODE="${NODE:-69}"   # the coordinating seat (69 since 2026-10-20)
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
# ** NEEDS: a precondition the script TESTS, replacing an exclusion that estimated it. **
#   A gate listed here is skipped only while its test fails, and the skip prints the test.
#   This set cannot grow silently: when the precondition is met the gate runs.  That is the
#   difference between an environment fact and a cost guess.
needs_unmet() {
  case "$1" in
    check_compile)          command -v pdflatex >/dev/null 2>&1 || { echo "no pdflatex here"; return 0; } ;;
    check_sitemap_resolves) [ -d _site ] || { echo "no assembled _site here"; return 0; } ;;
  esac
  return 1
}

# name:reason -- reason is printed, so an exclusion cannot be silent.
EXCLUDE_NAMES="check_quote_pins check_receipts_run"
reason_for() {
  case "$1" in
    check_quote_pins)      echo "595s here, 186-279s in CI (70, r7453+70.2) -- over this 280s timeout locally; the fast job asks it every push" ;;
    check_receipts_run)    echo "a TRIGGER, not a cost: red whenever the tree digest moves (139s; the 9-minute figure described the RE-RUN, not the gate)" ;;
    # r7435: the one gate whose subject is the DEPLOYED site.  `_site/` is built
    #   by `pages.yml` and exists nowhere in a working tree, so the turn batch
    #   was asking it about a directory that is never here.  It is NOT taught to
    #   exit 0 on a missing `_site`: a gate that passes when its subject is
    #   absent is the vacuous pass its own sitemap-presence assertion exists to
    #   prevent, and moving that hole up one level is not closing it.
    check_sitemap_resolves) echo "needs the assembled _site and is the deploy job's question, not the turn's" ;;
    *) case " $pushed " in *" $1 "*) echo "LEAN: heavy, and CI's fast job asks it on every push -- run --full to ask it here"; return;; esac
       echo "no reason recorded -- THIS IS A DEFECT, add one" ;;
  esac
}

ALL=0; [ "${1:-}" = "--all" ] && ALL=1
LEAN=1; case "${1:-}" in --full|--all) LEAN=0;; esac

# HEAVY_PUSHED -- name:seconds measured here on 2026-10-20 (NODE=66, 2 cores).  Over 15 s each.
HEAVY_PUSHED="check_quote_pins:366 check_cross_row_dupes:124 check_receipts:99 check_exact_counts:57
  check_unread_figure:46 check_marker_transposition:45 check_withdrawn:37 check_compile:35
  check_prose_pins:34 check_deferrals:27 check_pdf_current:22"
pushed=""
if [ "$LEAN" -eq 1 ]; then
  ci_fast=$(sed -n '/name: the text gates/,/done$/p' .github/workflows/gates.yml)
  touched_tex=$( { git diff --name-only HEAD -- 'corpus/*.tex'; git diff --name-only '@{u}' -- 'corpus/*.tex' 2>/dev/null; } | sort -u)
  for e in $HEAVY_PUSHED; do
    n=${e%%:*}
    # A heavy gate is left to the push ONLY while the push asks it.
    echo "$ci_fast" | grep -qw "$n" || continue
    [ "$n" = check_compile ] && [ -n "$touched_tex" ] && continue
    case " $EXCLUDE_NAMES " in *" $n "*) continue;; esac
    pushed="$pushed $n"
  done
  EXCLUDE_NAMES="$EXCLUDE_NAMES$pushed"
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

MODE=full; [ "$LEAN" -eq 1 ] && MODE=lean; [ "$ALL" -eq 1 ] && MODE=all
echo "  turn batch ($MODE): ran $ran of $NEXP expected   (glob holds $NGLOB)   [NODE=$NODE, timeout=${GATE_TIMEOUT}s]"
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
