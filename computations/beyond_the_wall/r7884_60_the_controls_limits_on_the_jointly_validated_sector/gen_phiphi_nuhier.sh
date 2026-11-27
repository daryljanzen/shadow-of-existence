#!/bin/bash
# r7884+60, on order `r7879` item ③: ** THE LENSING GRID WITH THE JOINTLY VALIDATED CLOSURE ON. **
#
# ⚑ NOT RETYPED: this is `r7870`'s own `gen_phiphi_nufd_only.sh` with the hierarchy switched ON, the
#   grid pinned to the two numbers `r7882`'s gates fixed, and the sum nodes narrowed to the ones the
#   hierarchy can run at.  Nothing else differs, so a difference between these points and `r7870`'s
#   is the CLOSURE and not the method.
#
# ⛔ ONLY THE FIVE POSITIVE SUM NODES ARE HERE, AND THAT IS NOT A SHORTCUT.  `PREDICTION.md`'s
#   structural read ③: the switch refuses a zero sum, because at zero sum the species is exactly
#   massless and there is no massive species for its hierarchy to describe.  So the eight
#   parameter-offset directions per arm -- EVERY ONE of which `r7870` runs at `MNU = 0.00` -- and the
#   zero node itself are the SAME spectra with the hierarchy on or off, and are carried from the
#   landed grid WITHOUT approximation.  The limit read checks each carried point's own recorded
#   config rather than assuming it.
#
# ⚠ AND THE TWO NEGATIVE NODES ARE ABSENT BECAUSE THEY CANNOT BE RUN AT ALL.  A negative sum is
#   not a mass: the per-node energy has no reading at `y² < 0`.  `PREDICTION.md` registers that as a
#   fork on where the profile's minimum falls, with NO LIMIT READ if it falls at a negative node.
#
# ⚑ OUTPUT IS KEYED BY CONFIGURATION, in the DIRECTORY and not only in a log.
# ⚑ IDEMPOTENT: a completed point is skipped.
set -u
# ⌗ the output directory is KEYED BY THE CARRY, because two carries were compared and one
#   grid silently standing for the other is exactly the mistake phiphi.py already made once.
ETAREF=${ETAREF:-4000}
OUT=${PPOUT:-"$(cd "$(dirname "$0")/../bank" && pwd)/phiphi_grid_eta${ETAREF}_bvel1_primnorm1_nufd_only"}
export ETAREF
JOBS=${JOBS:-4}
MAXB=${MAXB:-99}
mkdir -p "$OUT"
# ⛔ the generator lives in `r7846`, not beside this copy: the first run of this file
#   inherited `cd "$(dirname "$0")"` from the original and found no `phiphi_point.py`.
cd "$(cd "$(dirname "$0")/.." && pwd)"/r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers

CR_H0=68.570730; CR_OM=0.291246; CR_WB=0.021643; CR_NS=1.015066
LC_H0=67.40;     LC_OM=0.3150;   LC_WB=0.0224;   LC_NS=0.965
S_H0=2.0; S_OM=0.0150; S_WB=0.0008; S_NS=0.020

run() {   # run <arm> <tag> <MNU> <H0> <OM> <WB> <NS>
  local arm=$1 tag=$2 mnu=$3 h0=$4 om=$5 wb=$6 ns=$7
  if [ "$arm" = cr ]; then
    env BVEL=1 NUFD=1 NUHIER=1 NQ=12 LMAXNU=12 QMAXNU=20 PRIMNORM=1 PPARM="$arm" PPTAG="$tag" PPOUT="$OUT" ARM=cr CRH0="$h0" CROM="$om" WBH2="$wb" NS="$ns" \
        MNU="$mnu" HIER=1 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 ZSTART=3e7 NOPROJ=1 \
        python3 phiphi_point.py > "$OUT/${arm}_${tag}.log" 2>&1
  else
    env BVEL=1 NUFD=1 NUHIER=1 NQ=12 LMAXNU=12 QMAXNU=20 PRIMNORM=1 PPARM="$arm" PPTAG="$tag" PPOUT="$OUT" ARM=lcdm LH0="$h0" LOM="$om" WBH2="$wb" NS="$ns" \
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
  for s in "0.06 S006" "0.15 S015" "0.30 S030" "0.45 S045" "0.60 S060"; do
    set -- $s
    JOBLIST+=("$arm $2 $1 $h0 $om $wb $ns")
  done
  #: ⛔ *the eight parameter-offset directions are NOT here: every one of them is at a ZERO
  #: sum, where the hierarchy is provably inert, so they are CARRIED from the landed grid
  #: without approximation rather than re-run.  See PREDICTION.md reads ③ and ④.*
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
