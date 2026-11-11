#!/bin/bash
# r7737+70: the acceptance law's inputs on both arms -- GRIDSAVE (r7049+cc66.71), the r6911 configuration as
# r7729's launch.sh runs it.  It returns before any solve, in seconds.  Usage: gridsave.sh OUT_DIR
set -euo pipefail
cd "$(dirname "$0")/.."
O=${1:?OUT_DIR}; mkdir -p "$O"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
env HIER=1 ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248 LEAFREC=1 LMAXL=2000 \
    GRIDSAVE="$O/grid_lcdm.npz" python3 ACOUSTIC_two_arm.py | tail -1
env HIER=1 ARM=cr CRH0=68.570730 CROM=0.291246 WBH2=0.021643 NS=1.015066 LEAFREC=1 LEAFSCALES=1 ZSTART=3e7 \
    LMAXL=2000 GRIDSAVE="$O/grid_cr.npz" python3 ACOUSTIC_two_arm.py | tail -1
