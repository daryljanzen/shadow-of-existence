#!/bin/bash
# ** r7041 ⓐ AND ⓑ -- THE MIRROR OF `C59`, ON THE ARM, WITH THE CONTROL AT EVERY SAME SETTING. **
#
#   `C59` converged the CONTROL and said so in its own scope -- "No CR number is computed here at all".
#   `C60` discharged its deferral and then named gate order 1, 2 and 4 outstanding, THE CR RUN among
#   them.  So the arm has never been convergence-validated, on an instrument whose own k_max setting
#   moves P1/P2 by 14 per cent and P1/P3 by 63 per cent.  This is that run.
#
#   ⛭ ** THE QUANTITY TO CONVERGE IS THE RETENTION, NOT ONLY THE HEIGHTS. **  `C59` converged heights.
#   The retention is the l rung divided by the SOURCE rung, so every run carries `SRCSAVE` -- the
#   source before the kernel touches it, term by term -- and not only the spectrum.  Without it a
#   converged height says nothing about the quantity this row is about.
#
#   ⓑ ** EVERY SETTING IS RUN ON BOTH ARMS. **  A setting converged on the control is not thereby
#   converged on the arm: the eta-a relation differs by construction and D_M by 0.449 per cent.  The
#   report says, per setting, whether the two arms reach convergence at the same place.
#
# ⛔ ** KFAC UPWARD ONLY -- `alias_gate` fails closed below k_max/l_max = 1.9 and KFAC=2.0 is at 2.00. **
# ⚠ ** AND `NK` IS EXPECTED TO BE INERT ON THE ARM, WHICH IS A RESULT AND NOT A BUG. **  On the control
#   `lL = linspace(12, KMAXL, NK*3)`; on the arm the ladder is sqrt(L(L+2))*stretch out to KMAXL and
#   `NK` is only a decimation cap the reported settings do not reach.  The runs are made anyway, so the
#   inertness is measured rather than asserted from reading the source.
#
# ** Unsliced: `hier_run` already batches on KBATCH internally, so memory is bounded and KSLICE would
#    only split across processes.  IDEMPOTENT AND RESUMABLE on each run's own __DONE__ marker. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r7041; mkdir -p $D/real
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
  env HIER=1 "$@" SAVE=$out/$tag.npz SRCSAVE=$out/${tag}_src.npz \
      python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D

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
for s in "${SET[@]}"; do
  set -- $s; sname=$1; shift; senv="$*"
  LIST="$LIST
$D/real real_lcdm_${sname} $LCDM LSTEP=8 LMAXL=2000 $senv"
  LIST="$LIST
$D/real real_cr_${sname} $CR LSTEP=8 LMAXL=2000 $senv"
done
echo "--- ⓐ/ⓑ the real arms: $(printf '%s' "$LIST" | sed '/^$/d' | wc -l) runs, solver ON ---"
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7041 ⓐ LAUNCH COMPLETE $(date -u) ==="
