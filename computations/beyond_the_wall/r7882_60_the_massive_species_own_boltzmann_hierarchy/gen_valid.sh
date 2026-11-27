#!/bin/bash
# r7882+60: ** THE VALIDATION LEGS, AND THE TWO CONVERGENCE STUDIES, AT THE BANKED RESOLUTION. **
#
# ⌗ NOT RETYPED: `gen_limitfit.sh`'s own runner with the limit sums replaced by `r7879`'s two
#   validation sums and a GRID argument added.  `LMAXL`, `LSTEP`, `HIER` and the control's four
#   parameters are UNCHANGED, so these legs are comparable to the banks, which is the whole point.
#
#   bank      NQ   LMAXNU   what it is
#   base      12   12       the hierarchy as built -- the legs `r7879`'s validation is read on
#   nq24      24   12       gate Ⓠ⓶: the q-grid doubled
#   lmax18    12   18       gate Ⓠ⓷: the l-cutoff raised by half
#
# ⛔ Each bank gets `r7874`'s zero leg, COPIED and not linked, because a bank is committed for
#   `cc66`'s second fit and an absolute symlink does not survive a fresh clone.
#
# ⌗ IDEMPOTENT: a completed point is skipped, so this script is the resume path if the item splits.
#   ⌗ SELECTABLE: `BANKS="base"` runs the validation legs alone, which is the split's first half.

set -u
OUT=${OUT:-"$(cd "$(dirname "$0")" && pwd)/valid"}
JOBS=${JOBS:-2}
BANKS=${BANKS:-"base nq24 lmax18"}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."

LC_H0=67.40; LC_OM=0.3150; LC_WB=0.0224; LC_NS=0.965

grid() {  # grid <bank>  ->  "NQ LMAXNU"
  case "$1" in
    base)   echo "12 12" ;;
    nq24)   echo "24 12" ;;
    lmax18) echo "12 18" ;;
    *) echo "  ⛔ unknown bank $1" >&2; return 1 ;;
  esac
}

run() {   # run <bank> <tag> <MNU>
  local bank=$1 tag=$2 mnu=$3
  local g; g=$(grid "$bank") || return 1
  set -- $g; local nq=$1 lmaxnu=$2
  local d="$OUT/$bank"; mkdir -p "$d"
  local f="$d/lcdm_${tag}_tt.npz"
  if [ -s "$f" ]; then echo "  [have] $bank/$tag"; return 0; fi
  local t0=$SECONDS
  env BVEL=1 NUFD=1 NUHIER=1 NQ="$nq" LMAXNU="$lmaxnu" ARM=lcdm LH0="$LC_H0" LOM="$LC_OM" \
      WBH2="$LC_WB" NS="$LC_NS" MNU="$mnu" \
      HIER=1 LMAXL=2000 LSTEP=8 \
      SAVE="$f" POLSAVE="$d/lcdm_${tag}_pol.npz" \
      python3 ACOUSTIC_two_arm.py > "$d/lcdm_${tag}.log" 2>&1
  local rc=$?
  echo "  [$bank/$tag] NQ=$nq LMAXNU=$lmaxnu rc=$rc wall=$((SECONDS-t0))s" | tee -a "$OUT/COST.txt"
  [ $rc -eq 0 ] || return 1
}

Z=$(ls -d r7874_*/srcdec 2>/dev/null | head -1)
fail=0
for bank in $BANKS; do
  pids=()
  for spec in "S030 0.30" "S060 0.60"; do
    set -- $spec
    run "$bank" "$1" "$2" &
    pids+=($!)
    while [ "$(jobs -rp | wc -l)" -ge "$JOBS" ]; do wait -n; done
  done
  for p in "${pids[@]}"; do wait "$p" || fail=1; done
  for f in lcdm_S000.npz lcdm_S000_tt.npz lcdm_S000_pol.npz; do
    [ -s "$Z/$f" ] && cp -f "$Z/$f" "$OUT/$bank/$f"
  done
done
echo "done fail=$fail banks=$BANKS" | tee -a "$OUT/done.txt"
exit $fail
