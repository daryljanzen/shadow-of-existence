#!/bin/bash
# r7846+60: the lensing bandpowers on both arms' grids, on order r7845 item ②.
#
# The switch values are gen_pol.sh's own -- the banked grid's centre and step -- so each phi-phi
# point sits on the SAME cosmology as the CMB point of the same tag.  NOPROJ is on: the lensing
# path needs no Bessel pass, which is why a point costs about 95 s instead of an hour.
#
# ⌗ A completed point is SKIPPED, so a batch stopped at its limit is restarted and not redone.
# ⌗ MAXB limits how many batches of four this invocation runs, as gen_pol_batched.sh does, because
#   a background job killed at its time limit loses whatever its batch had not finished.
set -u
# ⌗ the output directory is KEYED BY THE CARRY, because two carries were compared and one
#   grid silently standing for the other is exactly the mistake phiphi.py already made once.
ETAREF=${ETAREF:-4000}
OUT=${PPOUT:-/tmp/claude-0/phiphi_grid_eta$ETAREF}
export ETAREF
JOBS=${JOBS:-4}
MAXB=${MAXB:-99}
mkdir -p "$OUT"
cd "$(dirname "$0")"

CR_H0=68.570730; CR_OM=0.291246; CR_WB=0.021643; CR_NS=1.015066
LC_H0=67.40;     LC_OM=0.3150;   LC_WB=0.0224;   LC_NS=0.965
S_H0=2.0; S_OM=0.0150; S_WB=0.0008; S_NS=0.020

run() {   # run <arm> <tag> <MNU> <H0> <OM> <WB> <NS>
  local arm=$1 tag=$2 mnu=$3 h0=$4 om=$5 wb=$6 ns=$7
  if [ "$arm" = cr ]; then
    env PPARM="$arm" PPTAG="$tag" PPOUT="$OUT" ARM=cr CRH0="$h0" CROM="$om" WBH2="$wb" NS="$ns" \
        MNU="$mnu" HIER=1 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 ZSTART=3e7 NOPROJ=1 \
        python3 phiphi_point.py > "$OUT/${arm}_${tag}.log" 2>&1
  else
    env PPARM="$arm" PPTAG="$tag" PPOUT="$OUT" ARM=lcdm LH0="$h0" LOM="$om" WBH2="$wb" NS="$ns" \
        MNU="$mnu" HIER=1 LMAXL=2000 LSTEP=8 NOPROJ=1 \
        python3 phiphi_point.py > "$OUT/${arm}_${tag}.log" 2>&1
  fi
  echo "  $arm $tag rc=$?" >> "$OUT/done.txt"
  tail -1 "$OUT/${arm}_${tag}.log"
}

JOBLIST=()
for arm in lcdm cr; do
  if [ "$arm" = cr ]; then h0=$CR_H0; om=$CR_OM; wb=$CR_WB; ns=$CR_NS
  else h0=$LC_H0; om=$LC_OM; wb=$LC_WB; ns=$LC_NS; fi
  for s in "-0.12 Sm12" "-0.06 Sm06" "0.00 S000" "0.06 S006" "0.15 S015" "0.30 S030" "0.45 S045" "0.60 S060"; do
    set -- $s
    JOBLIST+=("$arm $2 $1 $h0 $om $wb $ns")
  done
  JOBLIST+=("$arm H0p 0.00 $(python3 -c "print($h0+$S_H0)") $om $wb $ns")
  JOBLIST+=("$arm H0m 0.00 $(python3 -c "print($h0-$S_H0)") $om $wb $ns")
  JOBLIST+=("$arm OMp 0.00 $h0 $(python3 -c "print($om+$S_OM)") $wb $ns")
  JOBLIST+=("$arm OMm 0.00 $h0 $(python3 -c "print($om-$S_OM)") $wb $ns")
  JOBLIST+=("$arm WBp 0.00 $h0 $om $(python3 -c "print($wb+$S_WB)") $ns")
  JOBLIST+=("$arm WBm 0.00 $h0 $om $(python3 -c "print($wb-$S_WB)") $ns")
  JOBLIST+=("$arm NSp 0.00 $h0 $om $wb $(python3 -c "print($ns+$S_NS)")")
  JOBLIST+=("$arm NSm 0.00 $h0 $om $wb $(python3 -c "print($ns-$S_NS)")")
done

TODO=()
for j in "${JOBLIST[@]}"; do set -- $j; [ -s "$OUT/$1_$2.json" ] || TODO+=("$j"); done
echo "  ${#JOBLIST[@]} point(s) in the list, ${#TODO[@]} outstanding"
JOBLIST=("${TODO[@]:-}")
[ ${#JOBLIST[@]} -eq 0 ] && { echo "  nothing outstanding"; exit 0; }

b=0
i=0
while [ $i -lt ${#JOBLIST[@]} ]; do
  b=$((b+1))
  for ((n=0; n<JOBS && i<${#JOBLIST[@]}; n++, i++)); do
    set -- ${JOBLIST[$i]}
    run "$@" &
  done
  wait
  if [ $b -ge $MAXB ]; then echo "  stopping after $b batch(es), as asked"; break; fi
done
echo "ALL DONE"
echo "  lensing-bandpower points: $(ls "$OUT"/*.json 2>/dev/null | wc -l)"
