"""P4's floor against Planck's MEASURED temperature spectrum, multipole by multipole, with every figure
the paper prints pinned.  Inputs: CAMB on the Planck 2018 base-LCDM parameters, and the Planck 2018
measured TT spectrum (planck_TT_full.txt: PR3 COM_PowerSpect_CMB-TT-full, l = 2..2508, D_l in muK^2).

Hypothesis: the expansion rate tracks the smoothed density, H_loc = H(1 - f delta_R/3).  Along a ray
  delta ln(1+z)(n) = - int dchi g(chi) delta_R,   g = a H f / (3c).
  single path, correlated:   sigma^2 = int dchi g^2 (1/2pi) int k P_R dk
  single path, uncorrelated cells of length R:  sigma^2 = int dchi g^2 R sigma_R^2
  angular power (Limber):    C_l = int dchi g^2/chi^2 P_R((l+1/2)/chi, z)
The comparator is the MEASURED spectrum (its rms over l = 2..2508 is 4.06e-5); l with a non-positive
measured D_l (33 of them, all at high l) are where the measured power is consistent with zero and are
left out of the minimum ratios, since there any positive prediction exceeds it.
"""
import numpy as np, camb, os
from scipy.integrate import simpson
here = os.path.dirname(os.path.abspath(__file__))
T0 = 2.7255e6; c = 299792.458
pars = camb.set_params(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, As=2.1e-9, tau=0.0544,
                       WantTransfer=True, kmax=50)
res = camb.get_background(pars); h = pars.H0/100
PK = camb.get_matter_power_interpolator(pars, nonlinear=False, hubble_units=True, k_hunit=True,
                                        kmax=50, zmax=1100, var1="delta_tot", var2="delta_tot")
zstar = res.get_derived_params()["zstar"]
zs = np.concatenate([np.linspace(0, 10, 2001)[:-1], np.geomspace(10, zstar, 400)])
chi = res.comoving_radial_distance(zs)*h; Hz = res.hubble_parameter(zs); a = 1/(1+zs)
D = np.sqrt(PK.P(zs, 1e-3)/PK.P(0, 1e-3)); f = -np.gradient(np.log(D), np.log(1+zs))
g = a*Hz/h/c*f/3
def W(x):
    x = np.maximum(x, 1e-8); return 3*(np.sin(x)-x*np.cos(x))/x**3
kk = np.geomspace(1e-4, 50, 4000); Pgrid = PK.P(zs, kk)            # (nz, nk)
def sig_corr(R): return np.sqrt(simpson(g**2*simpson(kk*Pgrid*W(kk*R)**2, x=kk, axis=1)/(2*np.pi), x=chi))
def sig_cells(R): return np.sqrt(simpson(g**2*R*simpson(kk**2*Pgrid*W(kk*R)**2, x=kk, axis=1)/(2*np.pi**2), x=chi))
m = chi > 1.0
def Cl(L, R):
    out = np.empty(len(L))
    for i, l in enumerate(L):
        kl = (l+0.5)/chi[m]; Pk = PK.P(zs[m], kl, grid=False)*W(kl*R)**2; Pk[kl > 50] = 0
        out[i] = simpson(g[m]**2/chi[m]**2*Pk, x=chi[m])
    return out

dat = np.loadtxt(os.path.join(here, "planck_TT_full.txt")); ell, Dl = dat[:, 0], dat[:, 1]
Cobs = 2*np.pi*Dl/(ell*(ell+1))/T0**2
rms = np.sqrt(np.sum((2*ell+1)/(4*np.pi)*Cobs))
ok = True
def check(name, cond, val=""):
    global ok; print(("OK   " if cond else "FAIL ")+name, val); ok &= bool(cond)

check("measured rms, l=2..2508 = 4.1e-5", abs(rms-4.06e-5) < 0.02e-5, f"{rms:.3e}")
sc, s8 = sig_cells(8.0), sig_corr(8.0)
check("uncorrelated cells, R=8: 8.9e-3, some 220x", abs(sc-8.86e-3) < 0.05e-3 and round(sc/rms, -1) == 220, f"{sc:.3e} {sc/rms:.0f}x")
check("correlated, R=8: 1.6e-2, some 390x", abs(s8-1.574e-2) < 0.01e-2 and round(s8/rms, -1) == 390, f"{s8:.3e} {s8/rms:.0f}x")
for R, v in [(4, 1.9e-2), (20, 1.1e-2), (50, 6.0e-3), (100, 3.3e-3), (300, 9.6e-4)]:
    s = sig_corr(float(R)); check(f"correlated, R={R}: {v:.1e}", round(s, -int(np.floor(np.log10(v)))+1) == v, f"{s:.3e} {s/rms:.0f}x")
check("R=300 still 24x the measured rms", round(sig_corr(300.)/rms) == 24)

L = np.arange(2, 2501); ob = Cobs[L-2]; pos = ob > 0
ratio = {R: Cl(L, float(R))/ob for R in (4, 8, 20, 50, 100, 300)}
r8 = ratio[8][pos]
check("R=8: exceeds measured at every multipole by >= 2e4 (four orders)", r8.min() >= 2e4, f"min {r8.min():.3g}")
check("R=8: median ratio 2e5", round(np.median(r8), -5) == 2e5, f"{np.median(r8):.3g}")
check("R=4: >= 2e4 at every multipole", ratio[4][pos].min() >= 2e4, f"{ratio[4][pos].min():.3g}")
check("R=20: >= 800 at every multipole", ratio[20][pos].min() >= 800, f"{ratio[20][pos].min():.3g}")
check("R=50, 100: exceed at every multipole to 2500", ratio[50][pos].min() > 1 and ratio[100][pos].min() > 1,
      f"{ratio[50][pos].min():.3g}, {ratio[100][pos].min():.3g}")
r3, L3 = ratio[300][pos], L[pos]
first_below = L3[r3 < 1][0]
check("R=300: exceeds at every multipole up to l ~ 490", 480 <= first_below <= 500, f"first l below: {first_below}")
check("R=300: by more than 60 up to l = 100", r3[L3 <= 100].min() > 60, f"{r3[L3 <= 100].min():.3g}")
np.savez(os.path.join(here, "floor_curves.npz"), ells=np.unique(np.round(np.geomspace(2, 2500, 80)).astype(int)),
         **{f"R{R}": Cl(np.unique(np.round(np.geomspace(2, 2500, 80)).astype(int)), float(R)) for R in (4, 8, 20)})
print("\nALL PASS" if ok else "\nFAILURES"); assert ok
