#!/bin/bash
# r7801 (69) order: PO-24's N_eff response bank, in the mould of r6897's five-point omega_b set.
# The control at r6897's refit background (the same LCDM line), the reported resolution LSTEP=8
# LMAXL=2000, five Delta N_eff about the coded N0 = 3.000 (DNEFF, added at r7801+70 for this bank),
# each summed over eleven KSLICE pieces of 250 on KBATCH boundaries (exact to 1e-16, r6895+cc66.38).
# The centre, DNEFF=0, is checked against r6897's banked centre spectrum (the same run but for the knob).
# ** IDEMPOTENT AND RESUMABLE: a finished slice is skipped. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n70/r7801; mkdir -p $D/neff
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
LIST=""
for dn in 0 -0.5 0.5 -0.25 0.25; do
  i=0
  while [ $i -lt 2547 ]; do
    j=$((i+250))
    LIST="$LIST
$D/neff neff${dn}_k${i} $LCDM DNEFF=$dn LSTEP=8 LMAXL=2000 KSLICE=${i}:${j}"
    i=$j
  done
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P ${NPAR:-4} -I{} bash -c 'run {}'
echo "=== r7801 N_eff LAUNCH COMPLETE $(date -u) ==="
