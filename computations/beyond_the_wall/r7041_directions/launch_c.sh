#!/bin/bash
# ** r7041 ⓒ -- THE DIRECT TEST OF THE RETENTION, AS A CONVERGENCE SEQUENCE. **
#
#   The order: "the identical-source result -- a pure oscillation through each arm's own kernel,
#   visibility and grid, giving 1.066, exceeding the real 1.047 -- is the cleanest handle in the row:
#   no physics in the input at all.  Re-run it as a convergence sequence.  If 1.066 walks toward unity
#   as the settings refine, the retention is the integrator's and the row is answered."
#
#   ⓒ IS RUN FIRST BECAUSE IT IS THE CHEAP ONE: the analytic source replaces `S` entirely, so
#   `hier_run` skips the solver and each run is seconds of setup plus the projection.
#
# ⛔ ** UNSLICED, AND THAT SUPERSEDES THE FOUR `r7039` SLICES RATHER THAN REUSING THEM. **
#   *`r7039`'s launcher sliced on `KBATCH`, which is exact (r6895+cc66.38, 4.9e-15 relative) but needs
#   the mode count per configuration to assert the tiling -- and `KFAC` and `NK` MOVE that count.  A
#   scheme whose bookkeeping changes with the setting under test is the wrong scheme for a convergence
#   sequence.*  ⇒ One process per configuration, one file, no tiling to assert.  The `r7039` slices
#   stay on disk as the record of what was run; they are not read here.
#
# ⛔ ** KFAC RUNS UPWARD ONLY. **  `alias_gate` fails closed at k_max/l_max < 1.9 and KFAC=2.0 sits at
#   2.00, so the corpus default IS the guard's floor and the downward half of the sequence is refused
#   by the instrument.  That refusal is part of the report; it is not worked around.
#
# ** IDEMPOTENT AND RESUMABLE: a finished run is skipped on its own __DONE__ marker. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r7041; mkdir -p $D/noop $D/inj
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
# ⌗ ** THE SETTING'S ENVIRONMENT COMES AFTER THE DEFAULTS ON PURPOSE, AND `env` RESOLVES IT. **
#   `env LSTEP=8 ... LSTEP=4` takes the LAST assignment, so the `lstep4` row overrides the default
#   rather than being ignored by it.  *Verified rather than assumed, because a setting silently not
#   applied is exactly the shape `r6925`'s thirty-six wasted slices had -- and the `__SWITCHES__`
#   marker prints what actually arrived, so each log carries its own proof.*
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D

echo "--- the no-op gate: the r7039 names must still change nothing when unset ---"
printf '%s\n' \
 "$D/noop noop_lcdm  $LCDM LSTEP=16 LMAXL=500" \
 "$D/noop noop_cr    $CR   LSTEP=16 LMAXL=500" \
 | xargs -P 2 -I{} bash -c 'run {}'

# the settings, each varied ALONE with the others at their reported values.  `base` is the reported
# configuration and is the sequence's first point on every axis.
SET=(
  "base    "
  "kfac26  KFAC=2.6"
  "kfac32  KFAC=3.2"
  "kfac40  KFAC=4.0"
  "nk15    NK=1274"
  "nk20    NK=1698"
  "nlos1120 NLOS=1120"
  "nlos2240 NLOS=2240"
  "nlosw9  NLOSW=9.0"
  "nlosw12 NLOSW=12.0"
  "nlosf90 NLOSF=0.90"
  "lstep4  LSTEP=4"
)
LIST=""
for inj in "fixed SRCINJ=fixed" "sweepown SRCINJ=sweep SRCINJRS=own"; do
  set -- $inj; iname=$1; shift; ienv="$*"
  for s in "${SET[@]}"; do
    set -- $s; sname=$1; shift; senv="$*"
    LIST="$LIST
$D/inj inj_${iname}_lcdm_${sname} $LCDM LSTEP=8 LMAXL=2000 $ienv $senv"
    LIST="$LIST
$D/inj inj_${iname}_cr_${sname} $CR LSTEP=8 LMAXL=2000 $ienv $senv"
  done
done
echo "--- ⓒ the injection sequence: $(printf '%s' "$LIST" | sed '/^$/d' | wc -l) runs ---"
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7041 ⓒ LAUNCH COMPLETE $(date -u) ==="
