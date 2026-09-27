#!/bin/bash
# ** r6925's order: WHICH CLOCK IS THE VISIBILITY A DENSITY IN, AND DOES THE RULE DETERMINE IT? **
#
#   The rate rule: comoving separations read across leaves take the STACKING rate; scales the plasma
#   accumulates take the LEAF's.  g = tau' e^-tau is neither -- tau is accumulated by the plasma but
#   differentiated per unit eta, and eta is the stacking rate's.
#
# ⛔ ** AND THE INSTRUMENT ALREADY ANSWERS IT TWICE, DIFFERENTLY -- which is the audit's finding. **
#   `1/k_D^2` IS Jac-weighted under LEAFSCALES (line ~528), so the diffusion length takes the leaf
#   clock.  `tau` is NOT, so the optical depth takes the stacking clock.  Two objects on the same
#   side of the rule, given opposite clocks, with nothing stating the choice.
#     ⇒ `VISLEAF=1` applies to tau exactly the weighting 1/k_D^2 already applies to itself.  That is
#       what makes it the OTHER ADMISSIBLE ASSIGNMENT rather than a new invention.
#
# ⚑ AND THE GEOMETRY ANSWER IS ALREADY IN (r6925_directions/geom.py): d r_s / d chi goes
#   0.396733 -> 0.396957 on the arm, so 12.8 per cent lower becomes 12.7.  ** Both assignments give
#   the same thing. **  These runs are the CONFIRMATION on the contrast and on the comb, which the
#   order asks for side by side and refuses to have picked between.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6925; mkdir -p $D/noop $D/inj $D/comb
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D

echo "--- the no-op gate: VISLEAF unset must change nothing, on BOTH arms ---"
printf '%s\n' \
 "$D/noop noop_lcdm  $LCDM LSTEP=16 LMAXL=500" \
 "$D/noop noop_cr    $CR   LSTEP=16 LMAXL=500" \
 | xargs -P 2 -I{} bash -c 'run {}'
echo "--- and VISLEAF=1 on the CONTROL must ALSO be bit-identical, by the rate identity ---"
run $D/noop visl_lcdm $LCDM LSTEP=16 LMAXL=500 VISLEAF=1

echo "--- the injection under the other assignment, and the COMB the order asks for beside it ---"
# ⛔ ** THE FIRST VERSION OF THIS FUNCTION DROPPED ITS EXTRA ENVIRONMENT AND THIRTY-SIX SLICES RAN
#    AS PLAIN VISLEAF=0 SPECTRA. **  It did `shift 4` and then referenced `$5 $6 $7 $8`, which after
#    the shift point at the wrong arguments -- so `VISLEAF=1` and `SRCINJ=sweep` were never passed
#    and every log came back with the unset FWHM.  *Recorded rather than quietly fixed: the runs
#    completed, reported nothing wrong, and reproduced the banked spectra -- which is exactly the
#    shape that gets banked as an answer.*
#   ⇒ The extra environment is now taken as "$@" AFTER the shift, and the caller smoke-tests one
#     slice and greps the log for the marker the switch is supposed to print before the set goes out.
LIST=""
add () { tag=$1; arm=$2; env=$3; nk=$4; sub=$5; shift 5
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/$sub ${tag}_${arm}_k${i} $env LSTEP=8 LMAXL=2000 KSLICE=${i}:${j} $*"
    i=$j
  done; }
add injvl  lcdm "$LCDM" 2547 inj  VISLEAF=1 SRCINJ=sweep SRCINJRS=own
add injvl  cr   "$CR"   1452 inj  VISLEAF=1 SRCINJ=sweep SRCINJRS=own
add combvl lcdm "$LCDM" 2547 comb VISLEAF=1
add combvl cr   "$CR"   1452 comb VISLEAF=1
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6925 LAUNCH COMPLETE $(date -u) ==="
