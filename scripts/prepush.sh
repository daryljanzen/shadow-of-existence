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
# ⌗ `check_receipts` is NOT here.  It is the right gate and it takes ~27 s; this set takes under
#   two.  ** A pre-push check that people start skipping is worse than none, and the way it starts
#   being skipped is by being slow. **  The full 93 stay in `sweep_gates.sh`.
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
# ⌗ *Warns rather than blocks, and says what to set: this file is 60's lane under r2497, so 59
#  makes the check visible and leaves the decision to block with the line that owns the file.*
if [ -z "${NODE:-}" ]; then
  echo "  ⚠ NODE is unset, so the revision BAND cannot be checked before this push."
  echo "    Set NODE to your line (54, 56, 57, 59, 60, cc54) to check it; NODE=ci skips it."
  echo "    Twenty-one collisions passed between r3606 and r3678 with the band unchecked."
fi
export NODE="${NODE:-ci}"

fail=""
for g in check_depmatrix check_appendix_current check_marker_buried check_landing_rows_trace; do
  if timeout 120 python3 -W ignore "corpus/$g.py" >/tmp/_pp.$$ 2>&1; then
    printf '  [ok]   %s\n' "$g"
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
