#!/usr/bin/env python3
"""The driving, derived: fractional decay of Phi PER oscillation half-period at the mode's
first compression.  Steep decay per period (Phi changes a lot while the mode swings once) =
resonant driving.  Adiabatic decay (Phi ~ frozen over a period) = undriven.  No turnover
detector on the DATUM -- we read the potential's own decay against the oscillation's own phase.
Reported CR vs control as a differential."""
import numpy as np
from scipy.signal import argrelextrema

def diag(path, tag):
    z=np.load(path,allow_pickle=True)
    eta=z['eta']; phi=z['phi']; dg=z['dg']; q=z['qpk']; k=z['kpk']
    print(f"  {tag}")
    out=[]
    for i in range(len(q)):
        ph=phi[i]; d=dg[i]
        osc=[e for e in sorted(list(argrelextrema(d,np.greater,order=2)[0])+
                               list(argrelextrema(d,np.less,order=2)[0])) if k[i]*eta[e]>1]
        if len(osc)<2:
            # no full period sampled before rec; use start->first turnover if any, else skip
            if len(osc)==1:
                a,b=0,osc[0]
            else:
                out.append(np.nan); print(f"    q={float(q[i]):.2f}: <1 turnover before rec (mode still on first compression)"); continue
        else:
            a,b=osc[0],osc[1]                     # one half-period (compression->rarefaction)
        # fractional Phi decay across that half-period, per unit phase (pi)
        dphi=abs(ph[a]-ph[b]); phi_a=abs(ph[a])
        frac_per_half=dphi/phi_a if phi_a else np.nan
        out.append(frac_per_half)
        print(f"    q={float(q[i]):.2f} k={float(k[i]):.4f}: "
              f"|dPhi/Phi| over 1st full half-period = {frac_per_half:.4f}")
    return np.array(out)

base='/tmp/claude-0/-home-user-shadow-of-existence/e37412c9-b73d-5dc0-927f-d18006c9d057/scratchpad/'
print("Fractional potential decay per acoustic half-period (steep=driven, ~0=undriven):")
cr=diag(base+'cr_phi.npz','CR arm (leaf rate)')
lc=diag(base+'lcdm_phi.npz','LCDM control')
m=np.isfinite(cr)&np.isfinite(lc)
if m.any():
    print(f"\n  CR/control ratio per mode: {np.round(cr[m]/lc[m],3)}")
    print(f"  CR mean {np.nanmean(cr[m]):.4f}  control mean {np.nanmean(lc[m]):.4f}  "
          f"ratio {np.nanmean(cr[m])/np.nanmean(lc[m]):.3f}")
