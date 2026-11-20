#!/bin/bash
# r7838+60: the arms' own unlensed spectra on a GRID in the neutrino-mass sum.
#
# r7836 carried the sum as a single +/- pair at 0.06 eV and expanded quadratically in it.  Over a
# posterior that reaches 0.3 eV that is a quadratic extrapolation to five steps out, which is not a
# model of anything.  This generates the arms' own spectra AT each grid sum instead, so the sum
# direction is interpolated inside the generated range and never extrapolated.
#
# Two at a time on a four-core box: each run is single-threaded but the box also carries the gate
# suite, and r7836's Q1 lesson is that contention is what breaks a timing, not the arithmetic.
set -u
OUT=${OUT:-/tmp/claude-0/mnu_grid2}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."
run() {   # run ARM SUM TAG
  local arm=$1 s=$2 tag=$3
  local f="$OUT/${arm}_${tag}.npz"
  if [ -s "$f" ]; then echo "  [have] $arm $s"; return 0; fi
  if [ "$arm" = cr ]; then
    env ARM=cr CRH0=68.570730 CROM=0.291246 HIER=1 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 \
        MNU="$s" NS=1.015066 SAVE="$f" WBH2=0.021643 ZSTART=3e7 \
        python3 ACOUSTIC_two_arm.py > "$OUT/${arm}_${tag}.log" 2>&1
  else
    env ARM=lcdm HIER=1 LMAXL=2000 LSTEP=8 MNU="$s" SAVE="$f" \
        python3 ACOUSTIC_two_arm.py > "$OUT/${arm}_${tag}.log" 2>&1
  fi
  echo "  $arm $s rc=$?" >> "$OUT/done2.txt"
  echo "  [done] $arm $s"
}
Q=( "cr -0.12 Sm12" "cr 0.15 S015" "cr 0.30 S030"
    "lcdm -0.12 Sm12" "lcdm 0.00 S000" "lcdm 0.15 S015" "lcdm 0.30 S030" )
i=0
while [ $i -lt ${#Q[@]} ]; do
  set -- ${Q[$i]};         run "$1" "$2" "$3" &
  p1=$!
  i=$((i+1))
  if [ $i -lt ${#Q[@]} ]; then set -- ${Q[$i]}; run "$1" "$2" "$3" & p2=$!; i=$((i+1)); else p2=""; fi
  wait $p1 ${p2:-}
done
echo "ALL DONE"; cat "$OUT/done2.txt"
