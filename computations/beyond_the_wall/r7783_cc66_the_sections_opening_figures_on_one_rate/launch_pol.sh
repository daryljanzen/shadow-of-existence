#!/usr/bin/env bash
# r7783+cc66: the LEAFGEOM=1 REFIT arm's polarisation run, for item (3)'s fourth-feature comparison.
# Registered in PREDICTION.md R4 before this file existed.
#
# IDEMPOTENT by design: it skips a finished .npz, because this container restarts unpredictably.
# And it checks for a running solver by reading /proc/*/environ for ACOUSTIC_two_arm, NEVER by a
# bare pgrep name test -- a name test matches this script, the editor, and the grep itself.
#
# Switches are the banked refit arm's own, verbatim from its __SWITCHES__ line, plus POLSAVE:
#   ARM=cr CRH0=68.585672 CROM=0.294463 HIER=1 LEAFGEOM=1 LEAFREC=1 LEAFSCALES=1
#   LMAXL=2000 LSTEP=8 NS=0.961379 WBH2=0.022181 ZSTART=3e7
set -u
BW="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$BW/spectra/r7783_leafgeom_refit_pol_cr.npz"

if [ -s "$OUT" ]; then
  echo "DONE already: $OUT ($(stat -c%s "$OUT") bytes) -- nothing to do"
  exit 0
fi

# ⛔ THE /proc/*/environ READ NEEDS TWO EXCLUSIONS IN THIS CONTAINER, MEASURED THE HARD WAY.
#   The standing rule is to find a running solver by reading /proc/*/environ for ACOUSTIC_two_arm
#   rather than by a bare pgrep name test -- a name test matches the grep, the editor and this
#   script.  But the first form of this launcher reported "already running" with no solver up at
#   all: the wrapper that invokes it carries this script's own text, ACOUSTIC_two_arm included, in
#   its ENVIRONMENT, so the test fired on its own ancestry.  ⇒ Keep the environ read, and
#   ⒜ skip this process and every ancestor of it, and
#   ⒝ require the candidate's own CMDLINE to name ACOUSTIC_two_arm.py -- which is what a running
#      solver has and what a shell carrying the string in its environment does not.
#   *That is not the bare name test the rule warns against: it is the environ read, with the
#   self-match removed.*
mine=""
pid=$$
while [ -n "$pid" ] && [ "$pid" != "0" ] && [ "$pid" != "1" ]; do
  mine="$mine $pid"
  pid=$(awk '{print $4}' "/proc/$pid/stat" 2>/dev/null)
done

running=0
for e in /proc/*/environ; do
  [ -r "$e" ] || continue
  cand=$(echo "$e" | cut -d/ -f3)
  case " $mine " in *" $cand "*) continue ;; esac
  tr '\0' '\n' < "$e" 2>/dev/null | grep -q 'ACOUSTIC_two_arm' || continue
  tr '\0' ' ' < "/proc/$cand/cmdline" 2>/dev/null | grep -q 'ACOUSTIC_two_arm\.py' || continue
  echo "a solver is up: pid $cand -- $(tr '\0' ' ' < /proc/$cand/cmdline 2>/dev/null | cut -c1-90)"
  running=1
  break
done
if [ "$running" = 1 ]; then
  echo "not launching a second"
  exit 0
fi

cd "$BW" || exit 1
echo "launching: POLSAVE -> $OUT"
ARM=cr CRH0=68.585672 CROM=0.294463 HIER=1 LEAFGEOM=1 LEAFREC=1 LEAFSCALES=1 \
  LMAXL=2000 LSTEP=8 NS=0.961379 WBH2=0.022181 ZSTART=3e7 POLSAVE="$OUT" \
  python3 ACOUSTIC_two_arm.py
rc=$?
echo "solver exit $rc; output: $( [ -s "$OUT" ] && stat -c%s "$OUT" || echo MISSING ) bytes"
exit $rc
