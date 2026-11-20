#!/bin/bash
# r7838+60: the two OFF-GRID spectra the registered interpolation arm names literally -- a sum at
# 0.21 eV, which is no node of the grid the model interpolates on, generated for each arm so that
# the interpolated model can be compared against one rebuilt exactly there.
set -u
OUT=${OUT:-/tmp/claude-0/mnu_grid2}
cd "$(dirname "$0")/.."
while [ "$(grep -c 'rc=' "$OUT/done2.txt" 2>/dev/null || echo 0)" -lt 7 ]; do sleep 30; done
env ARM=cr CRH0=68.570730 CROM=0.291246 HIER=1 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 \
    MNU=0.21 NS=1.015066 SAVE="$OUT/cr_S021.npz" WBH2=0.021643 ZSTART=3e7 \
    python3 ACOUSTIC_two_arm.py > "$OUT/cr_S021.log" 2>&1 &
p1=$!
env ARM=lcdm HIER=1 LMAXL=2000 LSTEP=8 MNU=0.21 SAVE="$OUT/lcdm_S021.npz" \
    python3 ACOUSTIC_two_arm.py > "$OUT/lcdm_S021.log" 2>&1 &
p2=$!
wait $p1; echo "cr 0.21 rc=$?" >> "$OUT/done2.txt"
wait $p2; echo "lcdm 0.21 rc=$?" >> "$OUT/done2.txt"
echo OFFGRID DONE
