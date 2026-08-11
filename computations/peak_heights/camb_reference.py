"""LCDM peak-height reference (CAMB, Planck-2018 params). The digit-by-digit target the
peak-height build must reproduce; also the machinery-validation gate (arc discipline)."""
import numpy as np, camb
from camb import model
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.36, ombh2=0.02237, omch2=0.1200, mnu=0.06, tau=0.0544)
pars.InitPower.set_params(As=2.1e-9, ns=0.9649)
pars.set_for_lmax(2700, lens_potential_accuracy=0)
res=camb.get_results(pars)
tot=res.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=False)['total']  # D_l = l(l+1)C_l/2pi
ell=np.arange(tot.shape[0]); Dl=tot[:,0]                                     # TT
# find first three acoustic peaks (local maxima) above l=100
def peaks(ell,Dl,lo=100,hi=1100):
    m=(ell>=lo)&(ell<=hi); e,d=ell[m],Dl[m]
    idx=[i for i in range(2,len(d)-2) if d[i]>d[i-1] and d[i]>d[i+1] and d[i]>d[i-2] and d[i]>d[i+2]]
    # merge close, take top 3 by height in ell order
    pk=sorted([(e[i],d[i]) for i in idx], key=lambda t:t[0])
    # keep prominent ones
    out=[]
    for L,H in pk:
        if not out or L-out[-1][0]>120: out.append((L,H))
        elif H>out[-1][1]: out[-1]=(L,H)
    return out[:3]
pk=peaks(ell,Dl)
P=[h for _,h in pk]; L=[l for l,_ in pk]
print("LCDM (CAMB, Planck-2018) acoustic peaks:")
for i,(l,h) in enumerate(pk,1): print(f"  P{i}:  ell={l:4d}   D_l={h:7.1f} uK^2")
if len(P)>=3:
    print(f"\n  ratios:  P1/P2 = {P[0]/P[1]:.3f}   P2/P1 = {P[1]/P[0]:.3f}   P3/P1 = {P[2]/P[0]:.3f}   P3/P2 = {P[2]/P[1]:.3f}")
    print(f"  spacing: dl(1->2)={L[1]-L[0]}, dl(2->3)={L[2]-L[1]}")
    print(f"\n  (paper's observed anchors: P1/P2 ~ 2.2, P2/P1 ~ 0.46, P3/P1 ~ 0.45-0.46)")
    # --- r2376+c54.160: PIN THE BOLTZMANN REFERENCE.  The paper (sec:coherence) cites this receipt
    # for the peaks CR's are claimed to reduce to, "digit by digit": P1/P2 ~ 2.2, P2/P1 ~ 0.45,
    # P3/P1 ~ 0.44.  Those three ratios and the three peak multipoles are pinned here, so a CAMB
    # version change or a peak-finder regression fails the gate instead of silently moving the
    # reference the whole height argument is measured against.
    assert L[0] == 220 and L[1] == 536 and L[2] == 813, f"peak multipoles = {L}"
    assert abs(P[0] - 5734.1) < 5.0, f"P1 height = {P[0]} uK^2"
    assert abs(P[0]/P[1] - 2.211) < 0.010, f"P1/P2 = {P[0]/P[1]}"      # paper: ~2.2
    assert abs(P[1]/P[0] - 0.452) < 0.005, f"P2/P1 = {P[1]/P[0]}"      # paper: ~0.45
    assert abs(P[2]/P[0] - 0.443) < 0.005, f"P3/P1 = {P[2]/P[0]}"      # paper: ~0.44
