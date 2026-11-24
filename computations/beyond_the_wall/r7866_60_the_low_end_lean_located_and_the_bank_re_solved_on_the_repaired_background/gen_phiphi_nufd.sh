#!/bin/bash
# r7866+60, on order `r7865` item ③: THE LENSING GRID TOO, ON THE REPAIRED BACKGROUND.
#
# ⛔ WHY THIS EXISTS. The first cut of item ③ re-solved the CMB bandpower bank and left this one
#   alone, and the limits then came back with NO readable minimised value and a calibrated one far
#   from everything. The scope limit had been DECLARED, which was not enough: a hedge that is
#   load-bearing belongs in the stem. With the CMB spectra on the repaired background and the
#   lensing potential still on the old one, the two terms of the same likelihood disagree about
#   which background they are on, and that is the leading candidate for what the limits did.
#   ⇒ So this grid is re-solved on the same switches, and the limits are read again on a bank
#   whose two halves agree.
#
# ⌗ THIS FILE IS `r7860`'s own script WITH TWO CHANGES AND NOTHING ELSE: `NUFD=1` on both arms,
#   `DNEFF=0.0293` on the control only as the ruling sets it, and the output directory keyed to
#   those switches so the two lensing grids cannot be confused.
#
# —— what follows is `r7860`'s own text ——
# r7860+60, on order `r7857` item ④: THE LENSING GRID, WITH `BVEL` AND `PRIMNORM` BOTH ON.
#
# ⛔ WHY.  The ordered control wants three switches on.  The CMB half was re-solved for `BVEL`
# (`gen_pol_bvel1.sh`).  This is the lensing half, and it carries BOTH solver-side switches
# NATIVELY rather than as a multiplication after the fact: `phiphi.py` has had the primordial
# normalisation behind its own switch since `r7856`, and each point's constant depends on that
# point's OWN tilt, of which the grid carries six distinct values.  ⇒ So nothing is substituted
# on this half at all.
#
# ⌗ THE SWITCH SETS ARE NOT RETYPED: this file is `r7846`'s own `gen_phiphi.sh` with the two
#   switches added to each invocation and the output directory keyed to them, so the grids cannot
#   stand in for one another -- which that file's own header says is a mistake already made once.
# ⌗ A lensing point costs about 95 s, not an hour: the lensing path needs no Bessel pass.
# ⌗ IDEMPOTENT: a completed point is skipped.
set -u
# ⌗ the output directory is KEYED BY THE CARRY, because two carries were compared and one
#   grid silently standing for the other is exactly the mistake phiphi.py already made once.
ETAREF=${ETAREF:-4000}
OUT=${PPOUT:-"$(cd "$(dirname "$0")/../bank" && pwd)/phiphi_grid_eta${ETAREF}_bvel1_primnorm1_nufd_dneff"}
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
    env BVEL=1 NUFD=1 PRIMNORM=1 PPARM="$arm" PPTAG="$tag" PPOUT="$OUT" ARM=cr CRH0="$h0" CROM="$om" WBH2="$wb" NS="$ns" \
        MNU="$mnu" HIER=1 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 ZSTART=3e7 NOPROJ=1 \
        python3 phiphi_point.py > "$OUT/${arm}_${tag}.log" 2>&1
  else
    env BVEL=1 NUFD=1 DNEFF=0.0293 PRIMNORM=1 PPARM="$arm" PPTAG="$tag" PPOUT="$OUT" ARM=lcdm LH0="$h0" LOM="$om" WBH2="$wb" NS="$ns" \
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
