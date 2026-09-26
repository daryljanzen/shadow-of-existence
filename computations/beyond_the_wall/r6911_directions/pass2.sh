#!/bin/bash
# ** THE GUARD THE ORDER ASKED FOR, RUN RATHER THAN ARGUED. **
#
# The two arms' k grids are not the same KIND of grid: the control's is `linspace(12, KMAXL, NK*3)`
# -- uniform -- and CR's is its PHYSICAL ladder k_L = sqrt(L(L+2))/r_0, whose spacing varies.  The
# projection is a SUM over that grid with `dk = np.gradient(kb)` as its measure, so a contrast read
# off the projected spectrum could be the two arms' SAMPLING of an oscillating integrand and not
# their physics.  ⚠ *Three of the last five findings on this line were resolution or reference
# artefacts, and this is that shape exactly.*
#
# ⇒ `KCONT=1` replaces the ladder with the uniform continuum sampling -- 2547 modes, the SAME count
#   and the same kind of grid as the control -- with the background, the solver and every parameter
#   untouched.  ** If the contrast excess survives it, the grid is not what makes it. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6911; mkdir -p $D/kcont
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
XS_CR=0.995527938
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
LIST=""; i=0
while [ $i -lt 2547 ]; do
  j=$((i+250))
  LIST="$LIST
$D/kcont src_crkc_k${i} $CR KCONT=1 LSTEP=8 LMAXL=2000 KSLICE=${i}:${j} SRCXS=${XS_CR} SRCSAVE=$D/kcont/src_crkc_k${i}_fields.npz"
  i=$j
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6911 PASS2 COMPLETE $(date -u) ==="
