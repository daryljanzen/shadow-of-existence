#!/bin/bash
# r7647+70: r6893_directions/step0b.sh verbatim, the cr half, $CR -> the arm of record, LEAFREC=1 set.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank6}; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
CR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066 LEAFREC=1"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__ rc=0' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 LSTEP=64 LMAXL=2000 "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
LIST="whole_cr $CR"
i=0; while [ $i -lt 1452 ]; do j=$((i+250)); LIST="$LIST
k${i}_cr $CR KSLICE=${i}:${j}"; i=$j; done
printf '%s\n' "$LIST" | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7647 SLICE CHECK COMPLETE $(date -u) ==="
