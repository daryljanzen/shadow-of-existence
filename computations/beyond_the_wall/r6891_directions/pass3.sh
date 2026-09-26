#!/bin/bash
# ** r6891 order (2), third pass: the FULL-REACH confirmation.  The screen ran at LMAXL=500 because
#   connectivity is path-dependent and not resolution-dependent -- but a switch that acts only in the
#   damping tail would be invisible there, and `DAMPX` and `RD` are exactly such switches.  ⇒ Every
#   switch the screen calls INERT is re-run at the reported l reach (LMAXL=2000), on the control arm,
#   before the table calls it inert.  LSTEP=32 samples the l grid coarsely and cannot hide a move.
# ** IDEMPOTENT AND RESUMABLE **.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6891/full; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
GRID="HIER=1 LSTEP=32 LMAXL=2000"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env $GRID "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D GRID
printf '%s\n' \
 "base_lcdm          $LCDM" \
 "DAMPX_lcdm         $LCDM DAMPX=2.0" \
 "DSCAN_lcdm         $LCDM DSCAN=1" \
 "DSAVE_lcdm         $LCDM DSAVE=$D/junk_dsave.npz" \
 "NOPROJ_lcdm        $LCDM NOPROJ=1" \
 "PHISAVE_lcdm       $LCDM PHISAVE=$D/junk_phi.npz" \
 "QK_lcdm            $LCDM QK=0.02,0.05,0.10" \
 "QMIN_lcdm          $LCDM QMIN=1" \
 "QTURN_lcdm         $LCDM QTURN=vel" \
 "RD_lcdm            $LCDM RD=8.0" \
 "pairLRSFROMbase_lcdm  $LCDM LZSTART=6761" \
 "pairLRSFROM_lcdm      $LCDM LZSTART=6761 LRSFROM=start" \
 | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6893 PASS3 COMPLETE $(date -u) ==="
