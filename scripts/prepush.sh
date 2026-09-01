#!/usr/bin/env bash
# prepush.sh -- THE GENERATED-ARTEFACT CHECK, RUN BEFORE THE PUSH RATHER THAN AFTER IT.
#
# ** WHY.  Routed by 59 at r3567: ** *"I have now twice landed a marker and committed before
# regenerating tab:ledger-block, and both times check_depmatrix caught it on the next run rather
# than before the push."*
#   ⇒ *** The gate was never missing.  What was missing is that it runs at a moment when the
#       commit is already written. ***  A gate that fires after the push turns a five-second
#       regeneration into a second commit that exists only to say "and now regenerated".
#
# ** WHAT IT COVERS, and it is deliberately ONE class rather than a small sweep. **  Every check
# here answers the same question -- *did you regenerate what your edit made stale?*  They are the
# gates whose failures are always mechanical and never a judgement, which is exactly the set worth
# running unattended before a push:
#     check_depmatrix           all four grains, INCLUDING tab:ledger-block -- 59's case
#     check_appendix_current    both appendix rails against their indexes
#     check_marker_buried       a \ldg / \rcpt marker left inside a comment
#     check_landing_rows_trace  a landing row naming a register worked nowhere
#
# ⌗ `check_receipts` is NOT here.  It is the right gate and it takes ~27 s; this set takes about
#   five and a half (two for the four grain gates, three and a half for the band).  ** A pre-push
#   check that people start skipping is worse than none, and the way it starts being skipped is by
#   being slow. **  The full 93 stay in `sweep_gates.sh`.
#     ⌗ *The figure was "under two" until r3728 added the band gate.  Amended by MEASUREMENT rather
#     than left to drift, because a stated runtime nobody re-times is the same kind of claim as a
#     stated tolerance nobody verifies.*
#
# INSTALL, once per clone (hooks are not committed, so this is a line and not a file):
#     git config core.hooksPath .githooks
#   with .githooks/pre-push exec'ing this script.  Or just run it by hand before you push --
#   ** it is useful either way, and a hook nobody installed is a script nobody ran. **
#
# Written r3568 (node 60), to 59's r3567 routing.
set -uo pipefail
cd "$(dirname "$0")/.."
# ** PREPUSH IS WHERE A LINE *IS* A LINE -- 59, r3695, on 60's r3696 finding. **
# *This read `${NODE:-ci}`, and `ci` holds no half, so `check_revision_collisions` printed
# "the band is NOT CHECKED this run" on EVERY prepush of both lines since r3563.  60 measured
# that at r3696: the band's PREVENTION half has never run on either side.  59's r3679 made an
# unset NODE refuse inside the gate -- and this line fed it a declared value that skips the
# check, so the refusal never fired here.*
#   ⇒ ** A runner may hold no band (see `run_all_receipts.py`); a PREPUSH may not. ** *It runs
#   immediately before a commit enters a shared history, which is the one moment the question
#   "which half is this tree taking" has an answer and must be asked.*
# ⌗ *59 warned rather than blocked and routed the decision here, this file being 60's lane under
#  r2497.*  ** 60, r3728: IT BLOCKS. **  *Checked before deciding -- NOTHING calls this script
#  automatically: there is no `.githooks/` in the tree, no workflow references it, and CI sets
#  `NODE=ci` on its own gates without going through here.  **So the only caller a block can reach
#  is a line pushing by hand without declaring its half, which is the case that must be caught.**
#  And a warning printed above a run that then exits 0 is the shape this corpus keeps recording:
#  a record dressed as a verdict.*
#   ⛔ *** WHAT THE BLOCK DOES NOT DO, said plainly rather than oversold: `NODE=ci` is still an
#   escape and someone in a hurry will type it.  The block does not remove the skip -- it makes the
#   skip a TYPED, DELIBERATE ACT instead of a default.  That is the whole of the difference. ***
#   ⌗ *It fails FAST, before the gates: if the answer is "re-run with NODE set", a minute of gate
#   output buries the one line that says so.*
if [ -z "${NODE:-}" ]; then
  echo
  echo "  ⛔ NOT READY TO PUSH: NODE is unset, so the revision BAND cannot be checked."
  echo "     Set NODE to your line (54, 56, 57, 59, 60, cc54) and re-run."
  echo "     NODE=ci still skips the band -- but you will have TYPED it, which is the point."
  echo "     Twenty-one collisions passed between r3606 and r3678 with the band unchecked,"
  echo "     and until r3696 nobody knew this script had never checked it on either line."
  echo
  exit 1
fi
export NODE="$NODE"

fail=""
# ⛔⛭⛭ ** r3728: `check_revision_collisions` WAS NOT IN THIS LOOP, and that is what the whole
#   NODE thread above was really about. **  *59 wrote a warning at r3695 and 60 wrote a block at
#   r3728, both about `NODE` -- and neither checked that the gate `NODE` selects for was among the
#   gates this script runs.  It was not.*  ⇒ *** Exporting the right value to a gate that never
#   runs is theatre, and the measurement was one grep away.  Third layer of one defect: the gate
#   defaulted, the script fed it a value that skips, and the script never called it. ***
for g in check_depmatrix check_appendix_current check_marker_buried check_landing_rows_trace \
         check_revision_collisions; do
  if timeout 120 python3 -W ignore "corpus/$g.py" >/tmp/_pp.$$ 2>&1; then
    # ⌗ ** `check_revision_collisions` EXITS 0 UNDER `NODE=ci` WHILE REPORTING THE BAND UNCHECKED,
    #   so printing `[ok]` there would read as "band checked" when it was not asked. **  *This
    #   corpus's own doctrine: UNRUN is not a pass.*
    if [ "$g" = check_revision_collisions ] && grep -q 'NOT CHECKED this run' /tmp/_pp.$$; then
      printf '  [unchecked] %s -- NODE=%s holds no half; the band was NOT asked\n' "$g" "$NODE"
    else
      printf '  [ok]   %s\n' "$g"
    fi
  else
    printf '  [FAIL] %s\n' "$g"; sed 's/^/         /' /tmp/_pp.$$ | tail -12
    fail="$fail $g"
  fi
  rm -f /tmp/_pp.$$
done

echo
if [ -n "$fail" ]; then
  echo "  ⛔ NOT READY TO PUSH:$fail"
  echo "     ** Every failure above is mechanical -- a generated artefact behind its source. **"
  echo "     Regenerate, amend, and push once:"
  echo "       python3 corpus/make_all_appendices.py     # the \\rcpt rail"
  echo "       python3 scripts/depmatrix.py              # the matrix and the ledger block"
  exit 1
fi
echo "  every generated artefact is current with what it is generated from."
