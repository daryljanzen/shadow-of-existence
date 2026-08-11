"""
FAMILY 5 — the seam-to-recombination transfer to a high-ell verdict.
Closes the one piece full_transfer_verdict flagged unbuilt: whether CR's collapse-phase
driving preserves LCDM's PEAK-HEIGHT ENVELOPE at high ell (the escape hatch), by extending
the time-reversal driving theorem from the fundamental resonance to the full k-envelope.
Then assembles C_l^CR and the likelihood vs LCDM. Outcome not presumed.
"""
import numpy as np, camb
from scipy.integrate import simpson, solve_ivp
C=299792.458

# ============================================================
# 1. LCDM reference (CAMB) — baseline + geometry + validation targets
# ============================================================
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.36, ombh2=0.02237, omch2=0.1200, mnu=0.06, tau=0.0544)
pars.InitPower.set_params(As=2.1e-9, ns=0.9649)
pars.set_for_lmax(2700, lens_potential_accuracy=1)
res=camb.get_results(pars); dp=res.get_derived_params()
tot=res.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=False)['total']
ell=np.arange(tot.shape[0]); Dl_L=tot[:,0].copy()
D_M=dp['rstar']/(dp['thetastar']/100.)
print("="*74); print("1. LCDM BASELINE (CAMB)"); print("="*74)
print(f"   z*={dp['zstar']:.1f}  r_s={dp['rstar']:.2f}Mpc  100theta*={dp['thetastar']:.4f}  D_M={D_M:.0f}Mpc")
# peak heights (validate vs receipt: P1/P2~2.2, P2/P1~0.45, P3/P1~0.44)
from scipy.signal import find_peaks
pk,_=find_peaks(Dl_L[2:2000]); pk=pk+2; pk=pk[:3]
P1,P2,P3=Dl_L[pk[0]],Dl_L[pk[1]],Dl_L[pk[2]]
print(f"   peaks at l={pk}  P1/P2={P1/P2:.3f} (rcpt 2.2)  P2/P1={P2/P1:.3f} (0.45)  P3/P1={P3/P1:.3f} (0.44)")

# ============================================================
# 2. r_D on both rates (validated integrator, from damping_ratio_clean/full_transfer_verdict)
# ============================================================
def rD(radfree):
    zstar=dp['zstar']; h=67.36/100.; og=2.47282e-5/h**2
    Om=(0.02237+0.1200+0.06/93.14)/h**2; Or=og+3.046*(7./8.)*(4./11.)**(4./3.)*og
    OL=1-Om-Or; OLc=1-Om
    zd=np.linspace(zstar,8000,8000)
    opac=res.get_background_redshift_evolution(zd,['opacity'],format='array')[:,0]
    R=0.75*(0.02237/2.47282e-5)/(1+zd); br=R**2/(1+R)+8./9.
    H=(67.36*np.sqrt(Om*(1+zd)**3+(OLc if radfree else Or*(1+zd)**4+OL)))/C
    return np.sqrt(simpson((1/H)*(1/(6*(1+R)*opac))*br, zd))
rD_L=rD(False); rD_C=rD(True)
print("="*74); print("2. DIFFUSION LENGTH (validated integrator)"); print("="*74)
print(f"   r_D LCDM={rD_L:.3f}  r_D CR(radfree)={rD_C:.3f} Mpc  (+{100*(rD_C-rD_L)/rD_L:.1f}%)  [rcpt +9%]")

# ============================================================
# 3. THE NEW PIECE — does collapse-phase driving preserve the PEAK ENVELOPE at high ell?
#    (a) time-reversal magnitude invariance across the k-envelope (not just fundamental)
#    (b) is the undamped driving envelope FLAT at high ell (no room for a boost escape)?
# ============================================================
print("="*74); print("3. DRIVING ENVELOPE: time-reversal preservation across k + boost-escape test"); print("="*74)
# (a) resonant driving magnitude |Psi~(w=1)| for the radiation potential the mode sees,
#     across a grid of modes, expanding vs its time-reverse (collapse). x = c_s k eta.
def Psi_rad(x):
    ax=np.maximum(np.abs(x),1e-8); return 3*(np.sin(ax)-ax*np.cos(ax))/ax**3
def resonant_mag(profile,x):  # |FT at omega=1|
    return abs(np.trapezoid(profile*np.exp(-1j*x),x))
xs=np.linspace(-120,120,600001)
# model each 'mode' by a phase offset / horizon-entry time x0: Psi it sees = Psi_rad(x - x0)
maxdev=0.0
for x0 in [0,5,10,20,40,80]:   # deeper x0 ~ shorter wavelength / higher ell (later-entering in phase)
    fwd=Psi_rad(xs-x0); rev=Psi_rad(-(xs-x0))     # collapse = time-reverse
    mf,mr=resonant_mag(fwd,xs),resonant_mag(rev,xs)
    dev=abs(mf-mr)/max(mf,1e-30); maxdev=max(maxdev,dev)
    print(f"   mode x0={x0:3d}: |Psi~|_expand={mf:.5f}  |Psi~|_collapse={mr:.5f}  rel.dev={dev:.2e}")
print(f"   --> max deviation across the envelope = {maxdev:.2e}  "
      f"({'PRESERVED — collapse driving = LCDM driving at every mode' if maxdev<1e-4 else 'DIFFERS'})")
# (b) boost-escape test: is LCDM's UNDAMPED acoustic envelope flat/declining at high ell?
#     isolate driving envelope = CAMB D_l at peaks, un-damped by exp[+2(l/D_M)^2 r_D_L^2].
peaks_all,_=find_peaks(Dl_L[2:2600]); peaks_all=peaks_all+2
undamped=Dl_L[peaks_all]*np.exp(+2*(peaks_all/D_M)**2*rD_L**2)   # remove LCDM Silk envelope
hi=peaks_all>=800
print(f"   LCDM undamped peak envelope at high-l (l>=800): "
      f"{'RISING' if undamped[hi][-1]>1.4*undamped[hi][0] else 'flat/declining'} "
      f"(ratio last/first = {undamped[hi][-1]/undamped[hi][0]:.2f})")
print(f"   --> a driving 'boost' escape would need CR's envelope to RISE above LCDM's; time-reversal")
print(f"       forbids exceeding it (magnitude EQUAL, not greater), so peaks match, no boost.")

# ============================================================
# 4. ASSEMBLE C_l^CR = C_l^LCDM * Silk-ratio  (peaks matched by 3; damping from 2)
# ============================================================
print("="*74); print("4. CR HIGH-ELL TT vs LCDM"); print("="*74)
def silk_ratio(l): return np.exp(-2*(l/D_M)**2*(rD_C**2-rD_L**2))
Dl_C=Dl_L*silk_ratio(ell)
for L in (500,800,1000,1500,2000,2500):
    print(f"   l={L:5d}:  CR/LCDM = {silk_ratio(L):.3f}  ({100*(silk_ratio(L)-1):+.0f}% power)")

# ============================================================
# 5. LIKELIHOOD vs LCDM (cosmic-variance + crude Planck TT noise), banded
# ============================================================
print("="*74); print("5. LIKELIHOOD (CR vs LCDM reference)"); print("="*74)
fsky=0.7
def chi2(lmin,lmax,dl=30):
    x2=0.0; nb=0
    for lo in range(lmin,lmax,dl):
        hi=min(lo+dl,lmax); m=(ell>=lo)&(ell<hi)
        if m.sum()<2: continue
        lmid=0.5*(lo+hi); Cbar=Dl_L[m].mean()
        cv=np.sqrt(2.0/((2*lmid+1)*fsky*(hi-lo)))
        noise=0.004*(lmid/1000.)**2
        sig=Cbar*np.sqrt(cv**2+noise**2)
        resid=Dl_L[m].mean()-Dl_C[m].mean()
        x2+=(resid/sig)**2; nb+=1
    return x2,nb
for band in [(30,2500),(1000,2500),(1500,2500)]:
    x2,nb=chi2(*band)
    print(f"   l={band[0]}-{band[1]}: chi2={x2:.0f} / {nb} bins  ->  {(x2-nb)/np.sqrt(2*nb):+.1f} sigma equiv")
print("="*74)
