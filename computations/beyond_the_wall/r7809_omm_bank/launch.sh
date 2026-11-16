#!/bin/bash
# r7809 (69) order: PO-24's omega_m response bank, in the mould of r6897's five-point omega_b set.
# The control at r6897's refit background (the same LCDM line) but for LOM, the reported resolution LSTEP=8
# LMAXL=2000, five Omega_m about 0.309826 at fixed h (omega_m = Omega_m h^2 at -8,-4,0,+4,+8 per cent, as
# r6897's omega_b), through the existing LOM knob -- no new switch,
# each summed over eleven KSLICE pieces of 250 on KBATCH boundaries (exact to 1e-16, r6895+cc66.38).
# The centre, LOM=0.309826, is checked against r6897's banked centre spectrum (the same run but for the knob).
# ** IDEMPOTENT AND RESUMABLE: a finished slice is skipped. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n70/r7809; mkdir -p $D/omm
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 WBH2=0.021966 NS=0.954248"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
LIST=""
for dn in 0.309826 0.28504 0.334612 0.297433 0.322219; do
  i=0
  while [ $i -lt 2547 ]; do
    j=$((i+250))
    LIST="$LIST
$D/omm omm${dn}_k${i} $LCDM LOM=$dn LSTEP=8 LMAXL=2000 KSLICE=${i}:${j}"
    i=$j
  done
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P ${NPAR:-4} -I{} bash -c 'run {}'
echo "=== r7801 omega_m LAUNCH COMPLETE $(date -u) ==="
