#!/bin/bash
# ⛭ r7713 — the liveness check and relaunch, as a COMMITTED script rather than a form retyped into
#            each check-in prompt, because the form itself is what went wrong twice.
#
# ⛔ TWO UNSOUND FORMS, BOTH RECORDED:
#   ① a bare `pgrep dense.py` name test (r7711+cc66.3): it answers "is there a process whose name
#     matches", which is not "is the computation running", and it happened to give the right answer
#     for the wrong reason.
#   ② a /proc scan that joins each argv into one string and substring-matches it. That replaced ①
#     and was WORSE in one specific way: THE SCANNING SHELL'S OWN COMMAND LINE CONTAINS THE PATTERN,
#     so the scan matched itself and reported a runner when there was none. At 19:40Z it returned 1
#     with nothing running, and only the uptime of 28 s made the contradiction visible.
#
# ⇒ WHAT IS SOUND, and why each part is load-bearing:
#   - exclude THIS process by PID, so the scanner cannot be its own answer;
#   - exclude any `turn_gates` process, which may legitimately carry the name in a child's argv;
#   - match argv ELEMENTS exactly (`grep -qx`), not a substring of the joined line, so a command that
#     merely MENTIONS the script is not a command that RUNS it;
#   - require BOTH the interpreter and the script among the elements;
#   - and read the machine's uptime alongside, so the two sides are established independently and a
#     disagreement between them is visible instead of silently resolved.
set -u
cd "$(dirname "$0")"
D="$(pwd)"
UP=$(cut -d. -f1 /proc/uptime)
# ⛔ the total is NOT hardcoded: it moved from 56 to 112 when the checkpoint was halved, and a
#    hardcoded denominator would have gone on printing a figure that was of the old instrument.
BLOCKS=$(ls "$D"/pseudo/block__*.npy 2>/dev/null | wc -l)
BSZ=$(sed -n 's/^BLOCK = \([0-9]*\).*/\1/p' "$D/dense.py" | head -1)
PER=$(( (693 + BSZ - 1) / BSZ ))
TOT=$(( 4 * PER ))
DONE=$(ls "$D"/pseudo/pseudo__*.npz 2>/dev/null | wc -l)
self=$$
n=0
for p in /proc/[0-9]*/cmdline; do
  pid=${p%/cmdline}; pid=${pid#/proc/}
  [ "$pid" = "$self" ] && continue
  c=$(tr '\0' '\n' < "$p" 2>/dev/null) || continue
  case "$c" in *turn_gates*) continue;; esac
  if printf '%s' "$c" | grep -qx 'dense.py' && printf '%s' "$c" | grep -qx 'python3'; then
    n=$((n+1))
  fi
done
echo "uptime=${UP}s  blocks=${BLOCKS}/~${TOT} (${PER} per combination at BLOCK=${BSZ})  assembled=${DONE}/4  real_runners=${n}"
if [ "$DONE" -ge 4 ]; then
  echo "ALL FOUR ASSEMBLED -- run analyse.py; do NOT relaunch"
  exit 0
fi
if [ "$n" -eq 0 ]; then
  OUT=${1:-/tmp/dense_out.txt}
  setsid nohup bash "$D/run_dense.sh" > "$OUT" 2>&1 < /dev/null &
  sleep 5
  echo "$(date -u +%H:%M:%SZ) relaunched: uptime ${UP}s, blocks ${BLOCKS}, real runners 0" >> "$D/restarts.log"
  echo "RELAUNCHED (output -> ${OUT})"
else
  echo "running; nothing to do"
fi
