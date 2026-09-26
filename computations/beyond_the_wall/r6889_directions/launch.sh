#!/bin/bash
# ** r6889+cc66.36 -- the knob shadow repaired on the REPORTING path, then the tests re-run there.
#   noop_*   the unset configuration, which must come back BIT-IDENTICAL to
#            spectra/cc66_r185_verify_{lcdm,cr}.npz.  This is the proof that BOTH edits of this
#            revision -- wiring SWSRC/DPSRC into the hierarchy and low-ell paths, and the new NUFS
#            knob -- are additive.  They run FIRST and nothing else is read until they pass.
#   hdp0_*   DPSRC=0, the Doppler dipole, on the path every refit number is computed on
#   hsw0_*   SWSRC=0, the monopole, the other half of the same source
#   nufs0_*  NUFS=0, the neutrinos as a PERFECT FLUID at the same background density -- the
#            calibration for the new knob, because a knob that reports no change is
#            indistinguishable from one that is not connected (r4558's rule, and the whole subject
#            of this revision).
# ** IDEMPOTENT AND RESUMABLE **: skips any output already on disk.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6889
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { tag=$1; shift
  [ -s "$D/$tag.npz" ] && { echo "  skip $tag"; return 0; }
  env "$@" HIER=1 LSTEP=8 LMAXL=2000 SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
printf '%s\n' \
 "noop_lcdm    $LCDM" \
 "noop_cr      $CR" \
 "hdp0_lcdm    $LCDM DPSRC=0" \
 "hdp0_cr      $CR DPSRC=0" \
 "hsw0_lcdm    $LCDM SWSRC=0" \
 "hsw0_cr      $CR SWSRC=0" \
 "nufs0_lcdm   $LCDM NUFS=0" \
 "nufs0_cr     $CR NUFS=0" \
 | xargs -P 2 -I{} bash -c 'run {}'
echo "=== r6889 BATCH COMPLETE $(date -u) ==="
