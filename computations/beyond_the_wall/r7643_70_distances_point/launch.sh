#!/bin/bash
# r7643+70: the distances' point with LEAFREC=1 (the original recipes verbatim + LEAFREC=1), the key family at the arm
# of record, c54.178 at the crossing point, and 60's 24th Layer-2 rebuild in the namesake's own slices.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank4}
mkdir -p $D/g2000 $D/g1300 $D/x $D/noop $D/zp $D/l2
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
AR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066"
L2="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952 LEAFREC=0"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> "$out/$tag.log"; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
L=""
add () { L="$L
$*"; }
# 60's 24th: r6941_fine_cr at its own configuration, LEAFREC=0, LSTEP=1, six slices (the longest first)
for i in 0 250 500 750 1000 1250; do add $D/l2 fine_cr_k$i HIER=1 $L2 LSTEP=1 LMAXL=2000 KSLICE=$i:$((i+250)); done
# the cc66_cr_x family at its own points, LEAFREC=1
X="ARM=cr CROM=0.2973 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1"
add $D/x cc66_cr_x_h686_L2000 HIER=1 $X CRH0=68.60 LSTEP=2 LMAXL=2000
add $D/x cc66_cr_x_h686_pol   HIER=1 $X CRH0=68.60 LSTEP=2 LMAXL=1300
add $D/x cc66_cr_x_h6862_pol  HIER=1 $X CRH0=68.62 LSTEP=2 LMAXL=1300
# c54.178 at the crossing point (F178, LEAFSCALES unset), LEAFREC=1
add $D/x c54.178_cr HIER=1 BSPLIT=1 NK=600 LMAXL=2000 ETAEND=4000 KBATCH=300 ARM=cr CRH0=68.62 CROM=0.2973 ZSTART=3e7 LEAFREC=1
# the two grids at the distances' point: refit_grid185/launch.sh and refit_grid/launch.sh verbatim + LEAFREC=1
for g in "g2000 2000" "g1300 1300"; do set -- $g; sub=$1; lm=$2
  while read -r t sw; do add $D/$sub $t HIER=1 LSTEP=8 LMAXL=$lm ARM=cr ZSTART=3e7 LEAFSCALES=1 LEAFREC=1 $sw; done <<GRID
cr_base CRH0=68.60 CROM=0.2973
cr_H0p CRH0=70.60 CROM=0.2973
cr_H0m CRH0=66.60 CROM=0.2973
cr_OMp CRH0=68.60 CROM=0.3123
cr_OMm CRH0=68.60 CROM=0.2823
cr_WBp CRH0=68.60 CROM=0.2973 WBH2=0.0232
cr_WBm CRH0=68.60 CROM=0.2973 WBH2=0.0216
cr_NSp CRH0=68.60 CROM=0.2973 NS=0.985
cr_NSm CRH0=68.60 CROM=0.2973 NS=0.945
GRID
done
# the noop family and r6897's fields at the arm of record
for t in r6897_noop_cr r6911_noop_cr r6915_noop_cr r6919_noop_cr r6925_noop_cr r6929_unset_cr; do add $D/noop $t HIER=1 $AR LSTEP=16 LMAXL=500; done
add $D/noop r6911_xsonly_cr HIER=1 $AR LSTEP=16 LMAXL=500 SRCXS=1.5
add $D/noop r6929_zero_cr   HIER=1 $AR LSTEP=16 LMAXL=500 VISLEAF=0
add $D/zp zp_cr HIER=1 $AR LSTEP=64 LMAXL=2000 ZPSAVE=$D/zp/fields_cr.npz
echo "$L" | sed '/^$/d' | wc -l
printf '%s' "$L" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7643 BANK COMPLETE $(date -u) ==="
