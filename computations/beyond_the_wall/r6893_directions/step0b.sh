#!/bin/bash
# ** r6891 order (1), step 0b: does slicing add AT STAGE B's OWN SLICING AND REACH? **
#   Step 0 tested one boundary at LMAXL=500 and found both arms adding to 8e-9 -- floating-point
#   summation order and nothing more.  ⛔ But r6794's caveat is about where the k SPACING varies, and
#   stage B slices eleven times over a k range four times as long.  ⇒ So the test is repeated at
#   stage B's own reach and its own 250-mode boundaries, with the l sampling made coarse (LSTEP=64) so
#   the whole run is affordable: the projection is what LSTEP costs and the k-sum is what is being
#   tested.  ** IDEMPOTENT AND RESUMABLE. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6893/slice2; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 LSTEP=64 LMAXL=2000 "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
LIST="whole_lcdm $LCDM
whole_cr $CR"
for a in lcdm cr; do
  case $a in lcdm) B="$LCDM"; N=2547;; cr) B="$CR"; N=1452;; esac
  i=0
  while [ $i -lt $N ]; do j=$((i+250)); LIST="$LIST
k${i}_${a} $B KSLICE=${i}:${j}"; i=$j; done
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6891 STEP0B COMPLETE $(date -u) ==="
