#!/bin/bash
# r7729+70: the build's runs -- the SRCFIELD solves (both arms, every k-slice, the reported r6911 configuration)
# and the CR verify re-run for the instrument-blob re-bank.  IDEMPOTENT AND RESUMABLE: a finished job is skipped.
cd "$(dirname "$0")/.." || exit 1
D=${R7729_OUT:?set R7729_OUT}; mkdir -p $D/fld $D/rebank
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248 LEAFREC=1"
CR="ARM=cr CRH0=68.570730 CROM=0.291246 WBH2=0.021643 NS=1.015066 LEAFREC=1 LEAFSCALES=1 ZSTART=3e7"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.run.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
LIST="$D/rebank verify_cr $CR LMAXL=2000 LSTEP=8"
mk () { arm=$1; env=$2; nk=$3; i=0
  while [ $i -lt $nk ]; do j=$((i+250))
    LIST="$LIST
$D/fld ${arm}_k${i} $env LMAXL=2000 LSTEP=64 KSLICE=${i}:${j} SRCFIELD=$D/fld/${arm}_k${i}.npz"; i=$j; done; }
mk lcdm "$LCDM" 2547; mk cr "$CR" 1452
printf '%s\n' "$LIST" | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7729 LAUNCH COMPLETE $(date -u) ==="
