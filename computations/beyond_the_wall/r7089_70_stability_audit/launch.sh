#!/bin/bash
# r7089 (70) -- the audit's runs: SRCINJ=fixed, the r7041 launcher's own arm environments, to SCRATCH (never the
# repository, never cc66's bank).  Idempotent on a __DONE__ marker.  Usage: launch.sh <outdir>
cd "$(dirname "$0")/.." || exit 1
D=$1; mkdir -p "$D"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && return 0
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run
# (1) the cancellation test: base and the first refinement on every axis that moves either arm, BOTH arms
# (3) the band-resolved steps read the same runs
# (2) the responsiveness test: a gross eta under-resolution, on ONE arm at a time
SET=("base " "kfac26 KFAC=2.6" "nlos1120 NLOS=1120" "nlosw9 NLOSW=9.0" "nlosf90 NLOSF=0.90" "lstep4 LSTEP=4"
     "coarse140 NLOS=140" "narrow3 NLOSW=3.0")
LIST=""
for s in "${SET[@]}"; do set -- $s; n=$1; shift; e="$*"
  LIST="$LIST
$D inj_fixed_lcdm_$n $LCDM LSTEP=8 LMAXL=2000 SRCINJ=fixed $e
$D inj_fixed_cr_$n $CR LSTEP=8 LMAXL=2000 SRCINJ=fixed $e"
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7089 runs complete $(date -u) ==="
