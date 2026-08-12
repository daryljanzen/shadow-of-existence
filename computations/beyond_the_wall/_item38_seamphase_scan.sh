#!/bin/bash
# FOR_54 item 38: does the seam phase (CRPHI) move the ASYMPTOTIC acoustic intercept (peaks 4-8)?
# PRODUCTION settings, matched EXACTLY to c54.186_cr_L3000 (spectra/README.md):
#   HIER=1 BSPLIT=1 NK=900 LMAXL=3000 ETAEND=4000 KBATCH=300
# NK=900 gives 5.7 samples per Bessel period at LMAXL=3000 (default NK=260 aliases -- a first
# under-resolved run gave phi=0 -> 1.0053 with 10 spurious peaks instead of 0.878 with 8).
# Three well-separated seam phases {0, pi/2, pi}. phi=0 is its OWN control: must reproduce ~0.878.
# State NO expected outcome; fit peaks 4-8 (B4 method) and report what the intercept does.
set -e
cd "$(dirname "$0")"
for PHI in 0.0 1.5708 3.1416; do
  echo "=== CRPHI=$PHI (production: NK=900 HIER=1 BSPLIT=1) ==="
  HIER=1 BSPLIT=1 ARM=cr NK=900 LMAXL=3000 ETAEND=4000 KBATCH=300 CRPHI=$PHI \
    SAVE=spectra/item38_cr_phi${PHI}_prod.npz python3 ACOUSTIC_two_arm.py > /tmp/item38p_phi${PHI}.log 2>&1
  echo "  saved spectra/item38_cr_phi${PHI}_prod.npz"
done
echo "=== ALL THREE DONE — B4-method fit (argrelextrema order=3, polyfit index 4-8) ==="
python3 - <<'PY'
import numpy as np, os
from scipy.signal import argrelextrema
SP='spectra'
def b4(name):
    z=np.load(os.path.join(SP,name+'.npz')); ls,Dl,lA=z['ls'],z['Dl'],float(z['l_A'])
    pk=ls[argrelextrema(Dl,np.greater,order=3)[0]]
    n=np.arange(1,len(pk)+1); m=(n>=4)&(n<=8); a,b=np.polyfit(n[m],pk[m],1)
    return len(pk), a/lA, -b/lA, [int(x) for x in pk]
print(f"  {'CRPHI':>8} {'npk':>4} {'slope/lA':>9} {'phi/pi':>8}   peaks")
rows=[]
for phi in ['0.0','1.5708','3.1416']:
    npk,s,ph,pk=b4(f'item38_cr_phi{phi}_prod')
    rows.append((phi,npk,s,ph)); print(f"  {phi:>8} {npk:>4} {s:9.4f} {ph:8.4f}   {pk}")
# control check
p0=[r for r in rows if r[0]=='0.0'][0]
print(f"\n  CONTROL (phi=0) must reproduce c54.186's 0.878 with 8 peaks: got npk={p0[1]}, phi/pi={p0[3]:.4f}")
ok = (p0[1]==8) and abs(p0[3]-0.878)<0.03
print(f"  control {'VALID' if ok else 'INVALID -- settings still off, do not trust the scan'}")
ph=[r[3] for r in rows]
print(f"\n  asymptotic phi/pi vs seam phase: {ph[0]:.4f}(0) {ph[1]:.4f}(pi/2) {ph[2]:.4f}(pi)")
print(f"  SPAN across seam phase: {max(ph)-min(ph):.4f}   (vs the 0.615 CR-LCDM disagreement)")
PY
