#!/bin/bash
set -e; cd "$(dirname "$0")"
for PHI in 0.7854 2.3562; do
  HIER=1 BSPLIT=1 ARM=cr NK=900 LMAXL=3000 ETAEND=4000 KBATCH=300 CRPHI=$PHI \
    SAVE=spectra/item38_cr_phi${PHI}_prod.npz python3 ACOUSTIC_two_arm.py > /tmp/item38fill_phi${PHI}.log 2>&1
  echo "saved phi=$PHI"
done
echo "FILLS DONE"
