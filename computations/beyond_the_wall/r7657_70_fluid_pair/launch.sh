#!/bin/bash
# r7657+70: the fluid path (HIER absent; r6760+cc66.7's recipe LSTEP=2 LMAXL=1300) -- (a) the banked fluid arm's
# sibling at the distances' point, LEAFREC=1, and the default control (a reproduction); (b) the refitted arm of record
# and its own refit control.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank8}; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
P="LSTEP=2 LMAXL=1300"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__ rc=0' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
printf '%s\n' \
 "cr_x_h686_fluid_leafrec1_distances ARM=cr CRH0=68.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1 $P" \
 "lcdm_fluid_repro ARM=lcdm $P" \
 "cr_fluid_leafrec1 ARM=cr CRH0=68.570730 CROM=0.291246 WBH2=0.021643 NS=1.015066 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1 $P" \
 "lcdm_fluid_refit ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248 $P" \
 | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7657 FLUID COMPLETE $(date -u) ==="
