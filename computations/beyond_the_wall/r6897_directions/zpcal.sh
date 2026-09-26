#!/bin/bash
# ** r6897 (a)/(b): THE CALIBRATION THE MEASUREMENT NEEDS BEFORE ITS VERDICT COUNTS. **
#   The zero-point estimator says the arm's displacement is a few per cent BELOW the control's in
#   units of its own R.  r4558's rule applies to a measurement as much as to a knob: a number that
#   has not been shown to move when the thing it measures moves is not a measurement.  ⇒ So the
#   control is re-run with its baryon density displaced by +-8 per cent and the estimator is asked
#   whether it tracks the KNOWN dR.  It also gives d(offset)/d(omega_b) directly, which is what
#   converts the arm-control offset difference into an effective d(omega_b).
# ** IDEMPOTENT. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6897/zp; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 NS=0.954248"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 LSTEP=64 LMAXL=2000 "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
printf '%s\n' \
 "zp_wblo  $LCDM WBH2=0.02020872 ZPSAVE=$D/fields_wblo.npz" \
 "zp_wbhi  $LCDM WBH2=0.02372328 ZPSAVE=$D/fields_wbhi.npz" \
 | xargs -P 2 -I{} bash -c 'run {}'
echo "=== r6897 ZPCAL COMPLETE $(date -u) ==="
