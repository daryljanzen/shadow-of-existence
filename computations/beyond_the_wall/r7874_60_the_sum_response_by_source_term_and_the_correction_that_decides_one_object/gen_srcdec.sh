#!/bin/bash
# r7874+60, on order `r7873` item ①: ** THE CONTROL ARM WITH `SRCDEC` ON, so the sum response can
# be read PER TERM PAIR instead of only on the total. **
#
# ⛔ WHY PAIRS AND NOT TERMS.  The `SRCDEC` block's own comment settles it: the source terms ADD,
# but `C_l` is QUADRATIC in the transfer, so the projected pieces do NOT.  What closes is the full
# bilinear decomposition -- ten pairs summing to `C_l` exactly.  The order asks for "each term's
# response"; the object supplies ten pair responses, four of which involve `isw`.
#
# ⌗ NOT RETYPED: this is `r7872`'s own NUFD-off generator with the switch back ON (which is
#   `r7870`'s separating-grid generator upstream of that), narrowed to the control arm and the
#   three sums item ① names, with `SRCDEC` added and the output keyed to it.  So nothing but the
#   decomposition switch differs from the bank the response was read off.
# ⌗ IDEMPOTENT: a completed point is skipped.

set -u
OUT=${OUT:-"$(cd "$(dirname "$0")" && pwd)/srcdec"}
JOBS=${JOBS:-3}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."

LC_H0=67.40; LC_OM=0.3150; LC_WB=0.0224; LC_NS=0.965

run() {   # run <tag> <MNU>
  local tag=$1 mnu=$2
  local f="$OUT/lcdm_${tag}.npz"
  if [ -s "$f" ]; then echo "  [have] $tag"; return 0; fi
  env BVEL=1 NUFD=1 ARM=lcdm LH0="$LC_H0" LOM="$LC_OM" WBH2="$LC_WB" NS="$LC_NS" MNU="$mnu" \
      HIER=1 LMAXL=2000 LSTEP=8 \
      SAVE="$OUT/lcdm_${tag}_tt.npz" POLSAVE="$OUT/lcdm_${tag}_pol.npz" SRCDEC="$f" \
      python3 ACOUSTIC_two_arm.py > "$OUT/lcdm_${tag}.log" 2>&1
  echo "  lcdm $tag rc=$?" >> "$OUT/done.txt"
  echo "  [done] $tag"
}

JOBLIST=("S000 0.00" "S030 0.30" "S060 0.60")
TODO=()
for j in "${JOBLIST[@]}"; do
  set -- $j
  [ -s "$OUT/lcdm_$1.npz" ] || TODO+=("$j")
done
echo "  ${#JOBLIST[@]} point(s) in the list, ${#TODO[@]} outstanding"
[ ${#TODO[@]} -gt 0 ] || { echo "  nothing outstanding"; exit 0; }
pids=()
for j in "${TODO[@]}"; do
  set -- $j
  run "$1" "$2" & pids+=($!)
done
for p in "${pids[@]}"; do wait "$p"; done
echo "ALL DONE"; ls "$OUT"/lcdm_S*.npz 2>/dev/null | grep -vcE "_tt|_pol" | sed 's/^/  decompositions: /'
