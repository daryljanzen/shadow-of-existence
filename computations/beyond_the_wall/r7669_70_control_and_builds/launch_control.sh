#!/bin/bash
# r7669+70 ①: r6941's control recipe (r6941_directions/launch.sh, fine_lcdm) at LEAFREC=0 and LEAFREC=1,
# identical code and slicing (KSLICE pieces of 250 over NK 2547), four at a time, idempotent.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/r7669}
mkdir -p $D/lr0 $D/lr1
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  t0=$(date +%s)
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?; echo "__DONE__ rc=$rc wall=$(( $(date +%s)-t0 ))s" >> "$out/$tag.log"; echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"; }
export -f run; export D
LIST=""
for lr in 0 1; do i=0; while [ $i -lt 2547 ]; do
  LIST="$LIST
$D/lr$lr fine_lcdm_k$i $LCDM LSTEP=1 LMAXL=2000 LEAFREC=$lr KSLICE=$i:$((i+250))"; i=$((i+250)); done; done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7669 control COMPLETE $(date -u) ==="
