#!/bin/bash
# ** r6891 order (2), second pass: the PAIRED tests.  r4558's rule is that a switch reporting no
#   change cannot be told from a switch that is not connected -- so every switch the screen reports
#   inert has to be shown connected somewhere, or its inertness is not a result.  Each run here sets
#   the switch together with the OTHER switch its own source text makes it conditional on.
# ** IDEMPOTENT AND RESUMABLE **.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6891/screen; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
CRNOZ="ARM=cr CRH0=68.581133 CROM=0.297209 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
GRID="HIER=1 LSTEP=16 LMAXL=500"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env $GRID "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D GRID
printf '%s\n' \
 "pairLRSFROMbase_lcdm  $LCDM LZSTART=6761" \
 "pairLRSFROM_lcdm      $LCDM LZSTART=6761 LRSFROM=start" \
 "pairLATARGbase_cr     $CRNOZ" \
 "pairLATARG_cr         $CRNOZ LATARG=310.0" \
 "pairGSRC_cr           $CR GSRC=1" \
 "pairGSRC_lcdm         $LCDM GSRC=1 STACKPERT=1" \
 "pairGSRCbase_lcdm     $LCDM STACKPERT=1" \
 "pairKCONT_cr          $CR KCONT=1" \
 | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6893 PASS2 COMPLETE $(date -u) ==="
