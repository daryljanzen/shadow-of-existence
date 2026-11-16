#!/bin/bash
# r7813 (69) order ①: the control at Planck 2018's published point on the polarisation path,
# at the arms' KFAC (2.0) and at 1.5x it (3.0), each summed over KSLICE pieces of 250.
# Registered in PREDICTION.md before this ran.  ** IDEMPOTENT AND RESUMABLE: a finished slice is skipped. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n70/r7813; mkdir -p $D/k3 $D/k2
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
PLANCK="ARM=lcdm LH0=67.36 LOM=0.313773 WBH2=0.02237 NS=0.9649"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
modes () {  # the instrument's own mode count at this KFAC, read from a zero-width slice's header
  env HIER=1 $PLANCK KFAC=$1 LSTEP=8 LMAXL=2000 KSLICE=0:0 SAVE=/dev/null timeout 600 \
    python3 -u ACOUSTIC_two_arm.py 2>&1 | grep -o 'modes = [0-9]*' | head -1 | grep -o '[0-9]*'; }
LIST=""
for kf in 3 2; do
  N=$(cat $D/k$kf/NMODES 2>/dev/null || { n=$(modes $kf.0); echo $n > $D/k$kf/NMODES; echo $n; })
  [ -n "$N" ] || { echo "no mode count for KFAC=$kf"; exit 1; }
  echo "  KFAC=$kf.0: $N modes"
  i=0
  while [ $i -lt $N ]; do
    j=$((i+250))
    LIST="$LIST
$D/k$kf k${kf}_s${i} $PLANCK KFAC=$kf.0 LSTEP=8 LMAXL=2000 KSLICE=${i}:${j}"
    i=$j
  done
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P ${NPAR:-4} -I{} bash -c 'run {}'
echo "=== r7813 LAUNCH COMPLETE $(date -u) ==="
