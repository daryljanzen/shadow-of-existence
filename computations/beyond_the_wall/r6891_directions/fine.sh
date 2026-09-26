#!/bin/bash
# ** r6891 order (1): the SAME four spectra as r6889, on a four-times-finer l grid (LSTEP=2), so the
#   locator's answer can be shown not to be a property of the grid.  Same l reach (LMAXL=2000) and
#   the same refit minima, so these are comparable to spectra/{cc66_r185_verify,r6889_nufs0}_*.npz
#   line for line.  ** IDEMPOTENT AND RESUMABLE **.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6891/fine; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 LSTEP=2 LMAXL=2000 "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
printf '%s\n' \
 "cc66_r185_verify_lcdm  $LCDM" \
 "cc66_r185_verify_cr    $CR" \
 "r6889_nufs0_lcdm       $LCDM NUFS=0" \
 "r6889_nufs0_cr         $CR NUFS=0" \
 | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6893 FINE GRID COMPLETE $(date -u) ==="
