#!/bin/bash
# r7900+60, on order `r7895` item ②: ** THE CONTROL ARM WITH `SRCDEC` ON, TWICE AT EACH SUM --
# once with the potential-decay source and once without it. **
#
# ⌗ NOT RETYPED: this is `r7874`'s own `gen_srcdec.sh` with two changes and no others --
#   `S006` added to the job list, because the order names a sum that revision did not run; and
#   each point run a SECOND time under `NOISW=1`, which is the instrument's own switch on the
#   `_ISW * et * (dPhi/deta + dPsi/deta)` term. Every other environment value is that script's,
#   so the `ISW on` column should reproduce its bank where the two overlap -- and the scan
#   CHECKS that rather than assuming it.
# ⌗ IDEMPOTENT: a completed point is skipped, so this can be re-entered after a container restart.
# ⛔ `SRCDEC` is required on BOTH arms: the control is that the four `isw` bilinear pairs vanish
#   when the switch is off and the other six reproduce, and that cannot be read off the total.

set -u
OUT=${OUT:-"$(cd "$(dirname "$0")" && pwd)/srcdec"}
JOBS=${JOBS:-2}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."

LC_H0=67.40; LC_OM=0.3150; LC_WB=0.0224; LC_NS=0.965

run() {   # run <tag> <MNU> <noisw 0|1>
  local tag=$1 mnu=$2 noisw=$3
  local sfx=""; [ "$noisw" = "1" ] && sfx="_noisw"
  local f="$OUT/lcdm_${tag}${sfx}.npz"
  if [ -s "$f" ]; then echo "  [have] ${tag}${sfx}"; return 0; fi
  env BVEL=1 NUFD=1 ARM=lcdm LH0="$LC_H0" LOM="$LC_OM" WBH2="$LC_WB" NS="$LC_NS" MNU="$mnu" \
      HIER=1 LMAXL=2000 LSTEP=8 NOISW="$noisw" \
      SAVE="$OUT/lcdm_${tag}${sfx}_tt.npz" POLSAVE="$OUT/lcdm_${tag}${sfx}_pol.npz" SRCDEC="$f" \
      python3 ACOUSTIC_two_arm.py > "$OUT/lcdm_${tag}${sfx}.log" 2>&1
  echo "  lcdm ${tag}${sfx} rc=$?" >> "$OUT/done.txt"
  echo "  [done] ${tag}${sfx}"
}

JOBLIST=("S000 0.00" "S006 0.06" "S030 0.30" "S060 0.60")
TODO=()
for j in "${JOBLIST[@]}"; do
  set -- $j
  for n in 0 1; do
    sfx=""; [ "$n" = "1" ] && sfx="_noisw"
    [ -s "$OUT/lcdm_$1${sfx}.npz" ] || TODO+=("$1 $2 $n")
  done
done
echo "  ${#JOBLIST[@]} sum(s) x 2 arm(s) = $(( ${#JOBLIST[@]} * 2 )) point(s); ${#TODO[@]} outstanding"
[ ${#TODO[@]} -gt 0 ] || { echo "  nothing outstanding"; exit 0; }
i=0
for j in "${TODO[@]}"; do
  set -- $j
  run "$1" "$2" "$3" &
  i=$(( i + 1 ))
  if [ $(( i % JOBS )) -eq 0 ]; then wait; fi
done
wait
echo "ALL DONE"; ls "$OUT"/lcdm_S*.npz 2>/dev/null | grep -vcE "_tt|_pol" | sed 's/^/  decompositions: /'
