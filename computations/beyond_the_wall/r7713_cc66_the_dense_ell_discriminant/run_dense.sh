#!/bin/bash
# ⛭ r7713 — relaunch the block-checkpointed dense build until it exits 0.
#
# ⛔ This does NOT survive a container restart: measured twice, at two separate
#    restarts, by a liveness scan over /proc/[0-9]*/cmdline that found no process
#    running dense.py with the machine up under six minutes. It only covers a
#    crash or a nonzero exit WITHIN a window. After a recycle something outside
#    the container has to start the job again. That is the third obstruction,
#    reported in FOR_66.md under r7713+cc66, not worked around here.
#
# Completed blocks are never recomputed, so a relaunch costs at most the block
# that was in flight.
set -u
cd "$(dirname "$0")"
for i in $(seq 1 400); do
  python3 -u dense.py && exit 0
  echo "--- pass ${i} exited nonzero at $(date -u +%H:%M:%SZ), retrying"
  sleep 2
done
echo "--- gave up after 400 passes"
exit 1
