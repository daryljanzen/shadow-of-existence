#!/bin/bash
# ** the annotation of r6893 is COMMENTS ONLY, and this revision's own standard is that "changes
#   nothing" is measured and not asserted (cc66.36's reassociation episode is why).  One re-run of
#   each arm's base, gated bit-identical against the screen's own base. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6893/screen
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 LSTEP=16 LMAXL=500 "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag"; }
export -f run; export D
printf '%s\n' "annot_lcdm   $LCDM" "annot_cr     $CR" | xargs -P 2 -I{} bash -c 'run {}'
echo "=== r6893 PASS6 COMPLETE $(date -u) ==="
