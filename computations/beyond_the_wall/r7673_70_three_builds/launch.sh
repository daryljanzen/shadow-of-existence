#!/bin/bash
# r7673+70 item 1: the CR half of r7039_directions/launch.sh's transfer runs (fixed and sweepown, LSTEP=8 LMAXL=2000,
# six KSLICE pieces of 250 with DLKSAVE), at the recorded point with LEAFREC=0 (lr0, the recipe check) and at the refit
# licensed point with LEAFREC=1 (lr1). Four at a time, idempotent.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/r7673}
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
CR0="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952 LEAFREC=0"
AR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066 LEAFREC=1"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  t0=$(date +%s); env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$? wall=$(( $(date +%s)-t0 ))s" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run
L=""
for lr in 0 1; do mkdir -p $D/lr$lr/dlk; [ $lr = 0 ] && C=$CR0 || C=$AR
  for t in "fixed SRCINJ=fixed" "sweepown SRCINJ=sweep SRCINJRS=own"; do set -- $t; tag=$1; shift
    for i in 0 250 500 750 1000 1250; do
      L="$L
$D/lr$lr/dlk dlk_${tag}_cr_k$i $C LSTEP=8 LMAXL=2000 KSLICE=$i:$((i+250)) $* DLKSAVE=$D/lr$lr/dlk/dlk_${tag}_cr_k${i}_T.npz"
    done; done; done
T0=$(date +%s)
printf '%s' "$L" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7673 builds COMPLETE $(date -u) total_wall=$(( $(date +%s)-T0 ))s ==="
