#!/bin/bash
# r7041: the thin fold first (it unblocks the receipt and is the shorter job), then the two launchers.
# ** The solver check reads /proc/*/environ for ACOUSTIC_two_arm, never a bare name test **: a name
# test matches this script's own grep and any editor holding the file open, which is how a launcher
# decides nothing is running while four solvers are, or the reverse.
cd /home/user/shadow-of-existence || exit 1
SP=computations/beyond_the_wall/spectra
live () { local n=0 p
  for p in /proc/[0-9]*; do
    tr '\0' '\n' < "$p/environ" 2>/dev/null | grep -q 'ACOUSTIC_two_arm' && n=$((n+1))
  done
  echo $n; }
echo "=== $(date -u) solvers live at start: $(live)"
until [ "$(live)" -eq 0 ]; do sleep 30; done
# ⛔ ** THE FOLD IS SKIPPED WHEN ITS BANKS EXIST, AND THIS SKIP WENT MISSING ONCE ALREADY. **
# *`bank_thin.py` costs about 40 minutes and its output is committed.  The skip was written into a copy of
# this script in /tmp; the copy that reached the repository was the PRE-patch one -- so the fix was
# reported as landed while the tracked file still ran the fold unconditionally, and a relaunch spent its
# whole window redoing finished work.*
#   ⌗ ** A fix verified in a scratch copy is not a fix in the tracked file. **  This one is patched in
#   place and the condition is written out rather than assumed.
if [ -s "$SP/r7041_accept_lcdm.npz" ] && [ -s "$SP/r7041_accept_cr.npz" ]; then
  echo "=== $(date -u) thin fold SKIPPED -- both banks present"
else
  echo "=== $(date -u) thin fold -- a bank is missing"
  python3 computations/beyond_the_wall/r7041_directions/bank_thin.py
fi
# ⛭ ONE SLICED LAUNCHER FOR BOTH STAGES, replacing `launch_c.sh` and `launch_a.sh`: this container
# restarts faster than an unsliced run finishes, so the unit of work has to be the slice.
echo "=== $(date -u) stages c and a, sliced"
# ⛔⛭ ** THE LAUNCHER RUNS FROM A SNAPSHOT, AND THIS IS A DEFECT OF MINE CLOSED RATHER THAN A PRECAUTION. **
# *`bash` reads a script AS IT EXECUTES it, by byte offset.  I edit these launchers while they are running --
# that is how this revision has worked all along, because the windows between restarts are minutes -- and an
# edit that inserts lines ABOVE the line bash has reached moves every later offset, so the next read resumes
# mid-token and bash runs something nobody wrote.*
#   ⇒ ** A snapshot decouples the two: the running instance reads a copy that no edit touches, and the next
#   relaunch picks the edit up.  ** *It is the same shape as the fold-skip lesson one file over -- except
#   there the scratch copy was the bug, and here it is the fix. The difference is which one is authoritative:
#   the snapshot is taken FROM the tracked file every launch and is never edited.*
RUN=/tmp/n66/r7041/.launch_snapshot.sh
cp computations/beyond_the_wall/r7041_directions/launch_sliced.sh "$RUN"
bash "$RUN"
echo "=== $(date -u) ALL COMPLETE"
