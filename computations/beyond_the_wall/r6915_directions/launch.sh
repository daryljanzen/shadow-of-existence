#!/bin/bash
# ** r6915's order: WHICH TERM CARRIES THE CONTRAST EXCESS AFTER PROJECTION? **
#
#   `cc66.40` located the stage: the excess is made between k and ell.  `r6915` asks which of the
#   source's terms carries it there, and names the monopole-Doppler pair as the first place to look
#   because j_l and j_l' are a quarter period out of phase.
#
# ⛔ ** THE ORDER'S OWN CLOSURE GATE NEEDS A CORRECTION, AND IT IS THE ORDER'S FIRST OUTCOME. **  The
#   order says "the projection is linear in the source, so the separately projected pieces must sum
#   to the full spectrum".  The TRANSFER is linear in the source and the pieces DO add there; C_l is
#   QUADRATIC in the transfer, so the projected SPECTRA do not add -- they are short by exactly the
#   cross terms, which is the object the order's first outcome is about.
#     ⇒ So `SRCDEC` banks the full bilinear decomposition: four transfers, ten pair products,
#       C_l = SUM_{a<=b} w_ab SUM_k P Delta^a Delta^b, which closes on D_l EXACTLY and is gated.
#
# ⌗ The Bessel evaluation is shared with the reported spectrum, so this costs four trapezoids per
#   multipole and not a second projection.
# ** Sliced on KBATCH boundaries, idempotent and resumable, as every long run on this line is. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6915; mkdir -p $D/noop $D/dec
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D

echo "--- the no-op gate: the SRCDEC edit must change nothing when it is unset ---"
printf '%s\n' \
 "$D/noop noop_lcdm  $LCDM LSTEP=16 LMAXL=500" \
 "$D/noop noop_cr    $CR   LSTEP=16 LMAXL=500" \
 | xargs -P 2 -I{} bash -c 'run {}'

echo "--- the ten term pairs, both arms, the REPORTED configuration ---"
LIST=""
mk () { arm=$1; env=$2; nk=$3
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/dec dec_${arm}_k${i} $env LSTEP=8 LMAXL=2000 KSLICE=${i}:${j} SRCDEC=$D/dec/dec_${arm}_k${i}_pairs.npz"
    i=$j
  done; }
mk lcdm "$LCDM" 2547
mk cr   "$CR"   1452
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6915 LAUNCH COMPLETE $(date -u) ==="
