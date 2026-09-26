#!/bin/bash
# ** r6897's order: is the contrast excess and the alternation excess ONE number? **
#
#   (a) the effective zero point: the value Theta_0 + Psi swings ABOUT at the visibility peak, in
#       units of that arm's own Psi -- measured, not inferred.  ZPSAVE is its reporting-path save.
#   (b) what each arm's own loading predicts for it: R = 3 rho_b / 4 rho_g at its own visibility
#       peak.  In the header from this revision on; also written into the ZPSAVE bank.
#   (c) the effective d(omega_b) each residual implies, from the CONTROL's own measured response --
#       five omega_b on the control at the reported resolution, the centre being the refit value so
#       it doubles as a cross-check against the banked spectrum.
#
# ** EVERY LONG RUN IS SLICED ON KBATCH BOUNDARIES **, which r6895+cc66.38 measured as exact to
# 1e-16 on both arms -- so a container restart costs one slice and not a run.
# ** IDEMPOTENT AND RESUMABLE. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6897; mkdir -p $D/zp $D/noop $D/wb
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D

echo "--- the no-op gate: the ZPSAVE edit must change nothing when it is unset ---"
printf '%s\n' \
 "$D/noop noop_lcdm  $LCDM LSTEP=16 LMAXL=500" \
 "$D/noop noop_cr    $CR   LSTEP=16 LMAXL=500" \
 | xargs -P 2 -I{} bash -c 'run {}'

echo "--- (a)/(b): the fields at the visibility peak, both arms, full k grid ---"
printf '%s\n' \
 "$D/zp zp_lcdm  $LCDM LSTEP=64 LMAXL=2000 ZPSAVE=$D/zp/fields_lcdm.npz" \
 "$D/zp zp_cr    $CR   LSTEP=64 LMAXL=2000 ZPSAVE=$D/zp/fields_cr.npz" \
 | xargs -P 2 -I{} bash -c 'run {}'

echo "--- (c): the control's omega_b response at the reported resolution, sliced on KBATCH ---"
LIST=""
for w in 0.02020872 0.02108736 0.021966 0.02284464 0.02372328; do
  i=0
  while [ $i -lt 2547 ]; do
    j=$((i+250))
    LIST="$LIST
$D/wb wb${w}_k${i} $LCDM WBH2=$w LSTEP=8 LMAXL=2000 KSLICE=${i}:${j}"
    i=$j
  done
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6897 LAUNCH COMPLETE $(date -u) ==="
