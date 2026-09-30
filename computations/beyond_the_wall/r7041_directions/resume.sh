#!/bin/bash
# r7041: the thin fold first (it unblocks the receipt and is the shorter job), then the two launchers.
# ** The solver check reads /proc/*/environ for ACOUSTIC_two_arm, never a bare name test **: a name
# test matches this script's own grep and any editor holding the file open, which is how a launcher
# decides nothing is running while four solvers are, or the reverse.
cd /home/user/shadow-of-existence || exit 1
live () { local n=0 p
  for p in /proc/[0-9]*; do
    tr '\0' '\n' < "$p/environ" 2>/dev/null | grep -q 'ACOUSTIC_two_arm' && n=$((n+1))
  done
  echo $n; }
echo "=== $(date -u) solvers live at start: $(live)"
until [ "$(live)" -eq 0 ]; do sleep 30; done
echo "=== $(date -u) thin fold"
python3 computations/beyond_the_wall/r7041_directions/bank_thin.py
# ⛭ ONE SLICED LAUNCHER FOR BOTH STAGES, replacing `launch_c.sh` and `launch_a.sh`: this container
# restarts faster than an unsliced run finishes, so the unit of work has to be the slice.
echo "=== $(date -u) stages c and a, sliced"
bash computations/beyond_the_wall/r7041_directions/launch_sliced.sh
echo "=== $(date -u) ALL COMPLETE"
