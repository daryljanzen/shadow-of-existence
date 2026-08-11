"""
*** SUPERSEDED by hubble_expansion_confrontation_v2.py (r959). ***
This v1 carried a HIDDEN FLRW ASSUMPTION -- it fixed the physical density wm (LCDM's CMB invariant,
radiation making the peaks sensitive to physical densities) and let Om=wm/h^2 slide with H0. CR fixes
the DIMENSIONLESS Om (radiation-free => theta_*=r_s/D_M depends on Om alone; P15 sec:tensions). With
Om fixed, H0 cancels out of the BAO ratios and CR fits BAO at the local H0=73 (v2 verifies it). The
"finding" below that CR fails BAO was the imported assumption's artifact, not a real gap. Kept as the
record of the caught error. Read v2 for the correct result.

A1.4 -- the radiation-free rate vs the late-time expansion history (the data-side companion to D1).

The acoustic-scale leg (CR_acoustic_scale_and_hubble.py) shows CR matches the CMB acoustic scale
ell_A=301 at the LOCAL H0=73 -- radiation carries no term in the rate, so the sound horizon r_s is
recalibrated by the onset z_onset instead of pinned. This script extends that from the single CMB
angular scale to the FULL distance-redshift relation: does CR at H0=73 also fit the BAO ruler
D_M/r_d, D_H/r_d across 0.3<z<2.5 and the model-independent cosmic-chronometer H(z)?

FINDING (see the honest verdict at the bottom): the naive expectation -- that CR(H0=73, radiation-
free r_d) reproduces LCDM(H0=67.4)'s BAO -- FAILS. CR's radiation-free r_drag is barely reduced
(~146 vs ~147 Mpc), and at fixed CMB density wm the matter fraction Om shifts with H0 (0.315->0.268),
changing the low-z BAO shape. So BAO+chronometers prefer H0~68 in BOTH models; the acoustic-scale
match at H0=73 does NOT extend to the low-z distance ladder. Stated for reversal; a stop-and-check
against the corpus's ell_A-based Hubble claim, not a result to publish.

Data (entered from published summaries, cited; the conclusion is robust to their exact values):
  * BAO: SDSS DR12 galaxy consensus (Alam et al. 2017), r_d,fid=147.78 Mpc.
  * cosmic chronometers: a representative high-confidence subset of the Moresco et al. compilation.
"""
import numpy as np
from scipy.optimize import brentq
trapz = np.trapezoid
c = 299792.458  # km/s

# H0-independent physical densities (Planck; CMB-robust)
wm, wb, wr, wg = 0.1430, 0.02237, 4.15e-5, 2.47e-5
zrec, zeq = 1090.0, wm/wr - 1.0
R0 = 3*wb/(4*wg)
def cs(z): return c/np.sqrt(3*(1+R0/(1+z)))

def models(H0):
    h=H0/100.0; Om,Or,OL = wm/h**2, wr/h**2, 1-wm/h**2
    H_std = lambda z: H0*np.sqrt(Om*(1+z)**3+Or*(1+z)**4+OL)   # radiation IN rate
    H_cr  = lambda z: H0*np.sqrt(Om*(1+z)**3+OL)               # radiation-free
    return H_std,H_cr,Om,OL
def D_C(Hf,z,n=4000):                     # comoving distance to z
    zz=np.linspace(0,z,n); return trapz(c/Hf(zz),zz)
def D_M(Hf,z): return D_C(Hf,z)           # flat
def D_H(Hf,z): return c/Hf(z)
def r_s(Hf,z_onset,n=200000):
    u=np.linspace(np.log(1+zrec),np.log(1+z_onset),n); z=np.exp(u)-1
    return trapz(cs(z)/Hf(z)*(1+z),u)
def ell_A(Hf,z_onset): return np.pi*D_M(Hf,zrec)/r_s(Hf,z_onset)
ELL_A_OBS=301.0

z_drag = 1059.94    # Planck drag epoch (BAO ruler); r_d is r_s(z_drag), not r_s(z_rec)
def r_drag(Hf, z_onset): return r_s(Hf, z_onset, )   # integrate to z_drag below via wrapper
def r_drag(Hf, z_onset, n=200000):
    u=np.linspace(np.log(1+z_drag),np.log(1+z_onset),n); z=np.exp(u)-1
    return trapz(cs(z)/Hf(z)*(1+z),u)

# --- SDSS DR12 galaxy BAO (Alam et al. 2017): z, D_M/r_d, sig, D_H/r_d, sig ---
DR12=[(0.38,10.27,0.15,24.89,0.58),(0.51,13.38,0.18,22.43,0.48),(0.61,15.45,0.22,20.86,0.44)]
# cosmic chronometers (model-independent H(z); representative Moresco et al. subset): z,H,sig
CC=[(0.07,69.0,19.6),(0.20,72.9,29.6),(0.40,77.0,10.2),(0.88,90.0,40.0),
    (1.30,168.0,17.0),(1.43,177.0,18.0),(1.75,202.0,40.0),(1.965,186.5,50.4)]
def chi2_bao(Hf,rd): return sum(((D_M(Hf,z)/rd-dm)/sdm)**2+((D_H(Hf,z)/rd-dh)/sdh)**2
                                for z,dm,sdm,dh,sdh in DR12)
def chi2_cc(Hf):    return sum(((Hf(z)-H)/s)**2 for z,H,s in CC)

print("="*74)
print("A1.4  --  the radiation-free rate vs the late-time expansion history (HONEST FIT)")
print("="*74)
print("Physical densities fixed (CMB-robust): wm=%.4f wb=%.5f. At fixed wm, Om=wm/h^2 SHIFTS"%(wm,wb))
print("with H0 -- so raising H0 lowers Om, changing the low-z BAO shape. This is the real test.\n")

# pipeline sanity: standard LCDM at its CMB value should fit DR12 well
Hs674,_,Om674,_=models(67.4); rd674=r_drag(Hs674,1e8)
print(f"[sanity] LCDM H0=67.4 (Om={Om674:.3f}): r_drag={rd674:.1f} Mpc (std ~147.8), "
      f"chi2_BAO={chi2_bao(Hs674,rd674):.1f}/6  -> pipeline {'OK' if chi2_bao(Hs674,rd674)<8 else 'CHECK'}")

# scan H0: LCDM (r_d radiation-pinned) vs CR (r_d radiation-free, z_onset set by ell_A=301)
print(f"\n[scan] best-fit H0 from BAO+CC (r_d predicted by each model, NOT a free parameter):")
print(f"    {'H0':>5s} | {'Om':>5s} | {'LCDM rd':>7s} {'chi2':>6s} | {'CR rd':>6s} {'chi2':>6s}")
best={'lcdm':(1e9,0),'cr':(1e9,0)}
for H0 in np.arange(64,75.1,1.0):
    Hs,Hcr,Om,OL=models(H0)
    rdl=r_drag(Hs,1e8)
    z_onset=brentq(lambda z: ell_A(Hcr,z)-ELL_A_OBS, 1300, 1e8)
    rdc=r_drag(Hcr,z_onset)
    cl=chi2_bao(Hs,rdl)+chi2_cc(Hs); cc=chi2_bao(Hcr,rdc)+chi2_cc(Hcr)
    if cl<best['lcdm'][0]: best['lcdm']=(cl,H0)
    if cc<best['cr'][0]:   best['cr']=(cc,H0)
    print(f"    {H0:5.1f} | {Om:5.3f} | {rdl:7.1f} {cl:6.1f} | {rdc:6.1f} {cc:6.1f}")
print(f"\n    LCDM best-fit H0 = {best['lcdm'][1]:.0f}  (chi2={best['lcdm'][0]:.1f})")
print(f"    CR   best-fit H0 = {best['cr'][1]:.0f}  (chi2={best['cr'][0]:.1f})")
print(f"    local distance-ladder (SH0ES): H0 = 73.0 +/- 1.0")

# ---------------------------------------------------------------------------
print("\n"+"="*74)
print("HONEST FINDING (stated for reversal; NOT yet reconciled with the corpus):")
print("="*74)
print("""The radiation-free rate matches the CMB ACOUSTIC SCALE ell_A=301 at H0=73 (the
established result of CR_acoustic_scale_and_hubble.py) -- but it does so through the
high-z distance D_M(z_rec), NOT by reducing the BAO ruler r_drag. Confronted with the
LOW-z BAO + chronometers here, r_drag^CR ~ 146 Mpc is barely below LCDM's ~147, far from
the ~137 a sound-horizon resolution needs; and at fixed CMB density wm, raising H0 lowers
Om (0.315->0.268), which the BAO SHAPE disfavors. So BAO+CC prefer H0~68 in CR just as in
LCDM; CR is only marginally better at high H0. On this data the radiation-free rate does
NOT by itself carry the Hubble tension to the local H0=73 -- the acoustic-scale match does
not extend to the low-z distance ladder.

This CHALLENGES the corpus's Hubble-resolution claim as currently stated (which rests on
ell_A alone). Two readings, for Daryl's judgment -- do NOT bake either:
 (a) genuine: the resolution is real at the CMB acoustic scale but incomplete against BAO;
     something more (a real r_drag reduction, or freeing a density) is needed for full H0=73.
 (b) my error/omission: the corpus may treat the ruler or the densities differently than the
     fixed-wm inverse-distance-ladder used here, in which case this fit mis-states CR.
Either way it is a stop-and-check, not a result to publish.""")
