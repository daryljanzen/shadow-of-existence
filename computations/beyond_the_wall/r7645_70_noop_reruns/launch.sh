#!/bin/bash
# r7645+70: the no-op re-runs by their namesakes' own commands (r68xx_directions/launch.sh: HIER=1 $CR LSTEP=16
# LMAXL=500), $CR -> the arm of record, LEAFREC=1 SET; and zpcal.sh's zp_wblo at LEAFREC=1 (the control).
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank5}
mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
AR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066 LEAFREC=1"
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 NS=0.954248"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__ rc=0' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
printf '%s\n' \
 "zp_wblo $LCDM LEAFREC=1 LSTEP=64 LMAXL=2000 WBH2=0.02020872 ZPSAVE=$D/fields_wblo.npz" \
 "r6897_noop_cr $AR LSTEP=16 LMAXL=500" \
 "r6911_noop_cr $AR LSTEP=16 LMAXL=500" \
 "r6911_xsonly_cr $AR LSTEP=16 LMAXL=500 SRCXS=1.5" \
 "r6915_noop_cr $AR LSTEP=16 LMAXL=500" \
 "r6919_noop_cr $AR LSTEP=16 LMAXL=500" \
 "r6925_noop_cr $AR LSTEP=16 LMAXL=500" \
 "r6929_unset_cr $AR LSTEP=16 LMAXL=500" \
 "r6929_zero_cr $AR LSTEP=16 LMAXL=500 VISLEAF=0" \
 | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7645 RERUNS COMPLETE $(date -u) ==="
