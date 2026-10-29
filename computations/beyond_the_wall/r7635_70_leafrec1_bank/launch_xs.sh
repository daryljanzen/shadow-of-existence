#!/bin/bash
# r7635+70: the control's r6911 source with its SRCXS swap re-pointed at the arm of record's distance.
# The control is unchanged; SRCXS = D_M(arm of record)/D_M(control) = 14133.9546/13954.3535 (was 1.004492152).
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank}
mkdir -p $D/srcl
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
XS_LCDM=1.012870613
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> "$out/$tag.log"; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
for i in $(seq 0 250 2546); do echo "$D/srcl src_lcdm_k$i HIER=1 $LCDM LSTEP=8 LMAXL=2000 KSLICE=$i:$((i+250)) SRCXS=$XS_LCDM SRCSAVE=$D/srcl/src_lcdm_k${i}_fields.npz"; done \
 | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7635 XS BATCH COMPLETE $(date -u) ==="
