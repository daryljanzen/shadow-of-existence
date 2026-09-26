#!/bin/bash
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6893/screen
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
CRNOZ="ARM=cr CRH0=68.581133 CROM=0.297209 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
for v in 320.0 330.0; do
  t=pairLATARG$(echo $v | tr -d '.')_cr
  [ -s "$D/$t.log" ] && grep -q '^__DONE__' "$D/$t.log" && continue
  env HIER=1 LSTEP=16 LMAXL=500 $CRNOZ LATARG=$v SAVE=$D/$t.npz python3 -u ACOUSTIC_two_arm.py > $D/$t.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$t.log; echo "  done $t"
done
echo "=== r6893 PASS4 COMPLETE $(date -u) ==="
