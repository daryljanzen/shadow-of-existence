"""
P15_desi_dr2_confrontation.py -- verifies the P15 sec:tensions DESI DR2 BAO claim (the receipt the paper
  states the result of but did not cite by name). DESI DR2 Table IV (arXiv:2503.14738): 13 measurements,
  7 tracers, D_M/r_d & D_H/r_d with per-tracer CORRELATIONS (full 2x2 covariance) + BGS D_V/r_d. CR one-
  parameter (Omega_m) fit, sound horizon CMB-calibrated: best-fit Omega_m=0.3066 (paper 0.307, rho_r/rho_m~2.0),
  chi^2=12.01/12 dof = 1.00 (paper ~1.0), H0-independent (D_M/rd identical at 67.4 and 73). LCDM (w_m pinned):
  H0=67.4 -> chi2/dof=2.20; H0=73 -> 13.70 (paper ~14), BREAKS. The Hubble tension and its CR resolution on
  the state-of-the-art dataset.
STATUS: ✔✔ (CR chi2/dof=1.00 at Om=0.307; LCDM(73)=13.70 match paper 1.0/14; full covariance)
RUN: python3 P15_desi_dr2_confrontation.py   RUNTIME: ~5s
ORIGIN: hubble_build/desi_dr2_confrontation.py, verified r1396.
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar
trapz=np.trapezoid; c=299792.458

# ---- DESI DR2 BAO, Table IV (arXiv:2503.14738). (z, DM/rd, sDM, DH/rd, sDH, corr) or (z, DV/rd, sDV) ----
DESI_aniso=[  # LRG1, LRG2, LRG3+ELG1, ELG2, QSO, Lya
 (0.510,13.588,0.167,21.863,0.425,-0.459),
 (0.706,17.351,0.177,19.455,0.330,-0.404),
 (0.934,21.576,0.152,17.641,0.193,-0.416),
 (1.321,27.601,0.318,14.176,0.221,-0.434),
 (1.484,30.512,0.760,12.817,0.516,-0.500),
 (2.330,38.988,0.531, 8.632,0.101,-0.431)]
DESI_iso=[(0.295,7.942,0.075)]   # BGS (DV/rd only)
NDATA = 2*len(DESI_aniso)+len(DESI_iso)   # 13

# baryon loading for the sound speed (ordinary microphysics; same both frameworks)
wb, wg = 0.02237, 2.47e-5; R0=3*wb/(4*wg)
def cs(z): return c/np.sqrt(3*(1+R0/(1+z)))
zrec=1090.0; z_drag=1059.94
THETA_OBS=0.0104085   # Planck acoustic scale (100 theta_* = 1.04109)

# ---- CR: geometric stacking rate, Om the CMB-fixed dimensionless quantity ----
def E_cr(z,Om): return np.sqrt(Om*(1+z)**3+(1-Om))
def Hcr(z,H0,Om): return H0*E_cr(z,Om)
def DM(z,H0,Om,n=4000):
    zz=np.linspace(0,z,n); return trapz(c/Hcr(zz,H0,Om),zz)
def DH(z,H0,Om): return c/Hcr(z,H0,Om)
def DV(z,H0,Om): return (z*DM(z,H0,Om)**2*DH(z,H0,Om))**(1/3)
def r_snd(H0,Om,z_onset,z_lo,n=120000):
    u=np.linspace(np.log(1+z_lo),np.log(1+z_onset),n); z=np.exp(u)-1
    return trapz(cs(z)/Hcr(z,H0,Om)*(1+z),u)
def theta_star(H0,Om,z_onset): return r_snd(H0,Om,z_onset,z_lo=zrec)/DM(zrec,H0,Om)

H0ref=70.0  # arbitrary: ratios are H0-independent
def z_onset_of(Om):
    return brentq(lambda zo: theta_star(H0ref,Om,zo)-THETA_OBS, 1200, 5e4)

def chi2_cr(Om):
    zo=z_onset_of(Om); rd=r_snd(H0ref,Om,zo,z_lo=z_drag)
    x2=0.0
    for z,dm,sdm,dh,sdh,rho in DESI_aniso:
        pm=DM(z,H0ref,Om)/rd; ph=DH(z,H0ref,Om)/rd
        r=np.array([pm-dm, ph-dh])
        cov=np.array([[sdm**2, rho*sdm*sdh],[rho*sdm*sdh, sdh**2]])
        x2+=r@np.linalg.solve(cov,r)
    for z,dv,sdv in DESI_iso:
        x2+=((DV(z,H0ref,Om)/rd-dv)/sdv)**2
    return x2

# ---- LCDM: w_m pinned by radiation-era physics, r_d in physical Mpc; fit at H0=67.4 and 73 ----
wr=4.15e-5
def E_l(z,h,wm): Om=wm/h**2; Or=wr/h**2; return np.sqrt(Om*(1+z)**3+Or*(1+z)**4+1-Om-Or)
def Hl(z,H0,wm): return H0*E_l(z,H0/100,wm)
def DMl(z,H0,wm,n=4000): zz=np.linspace(0,z,n); return trapz(c/Hl(zz,H0,wm),zz)
def DHl(z,H0,wm): return c/Hl(z,H0,wm)
def DVl(z,H0,wm): return (z*DMl(z,H0,wm)**2*DHl(z,H0,wm))**(1/3)
def rdl(H0,wm,n=120000):
    u=np.linspace(np.log(1+z_drag),np.log(1+1e8),n); z=np.exp(u)-1
    return trapz(cs(z)/Hl(z,H0,wm)*(1+z),u)
def chi2_lcdm(H0,wm):
    rd=rdl(H0,wm); x2=0.0
    for z,dm,sdm,dh,sdh,rho in DESI_aniso:
        r=np.array([DMl(z,H0,wm)/rd-dm, DHl(z,H0,wm)/rd-dh])
        cov=np.array([[sdm**2, rho*sdm*sdh],[rho*sdm*sdh, sdh**2]])
        x2+=r@np.linalg.solve(cov,r)
    for z,dv,sdv in DESI_iso:
        x2+=((DVl(z,H0,wm)/rd-dv)/sdv)**2
    return x2

print("="*78)
print("A1.4-ext :: CR (geometric stacking, 1 param Om) vs DESI DR2 BAO  [13 measurements, 7 z]")
print("="*78)
# CR best-fit Om (one parameter), sound horizon CMB-calibrated
res=minimize_scalar(chi2_cr, bounds=(0.25,0.38), method='bounded')
Om_best=res.x; x2_cr=res.fun
zo=z_onset_of(Om_best)
print(f"\nCR best-fit:  Omega_m = {Om_best:.4f}   (z_onset={zo:.0f}, rho_r/rho_m~{(1+zo)/3402:.1f})")
print(f"   chi^2 = {x2_cr:.2f} / {NDATA-1} dof = {x2_cr/(NDATA-1):.2f}   -- at ANY H0 incl. local 73")
# --- r2376+c54.160: PIN THE FIT.  The paper (sec:tensions) quotes this receipt for "with a single
# free parameter Omega_m the geometric stacking rate fits at chi2/dof ~ 1.0, at Omega_m = 0.3066 (where
# the inherited datum sits at rho_r/rho_m ~ 2.0)".  Note the paper's own correction at c54.155:
# Omega_m here is FIT to these data by minimize_scalar, not imported.  Pinned to what it returns.
assert abs(Om_best - 0.3066) < 0.0015, f"CR best-fit Omega_m = {Om_best}"
assert abs(x2_cr - 12.01) < 0.15, f"CR chi^2 = {x2_cr}"
assert abs(x2_cr/(NDATA-1) - 1.00) < 0.02, f"CR chi^2/dof = {x2_cr/(NDATA-1)}"
assert abs(zo - 6764.0) < 8.0, f"z_onset at the best fit = {zo}"
assert abs((1+zo)/3402 - 2.0) < 0.05, f"inherited datum rho_r/rho_m = {(1+zo)/3402}"
# H0-independence spot check
for H0 in (67.4,73.0):
    rd=r_snd(H0,Om_best,zo,z_lo=z_drag)
    print(f"   [H0={H0}] D_M/rd(z=0.51) = {DM(0.51,H0,Om_best)/rd:.3f}  (H0-independent check)")
    # r2376+c54.160: THE WHOLE OF THE CLAIM is that this ratio does not know about H0 -- the paper:
    # "it fits there at ANY H0 including the local 73".  Same literal at both rates, so if the
    # cancellation ever broke, one of the two would miss it.
    assert abs(DM(0.51,H0,Om_best)/rd - 13.287) < 0.005, \
        f"D_M/rd(0.51) at H0={H0} = {DM(0.51,H0,Om_best)/rd}"

print(f"\nLCDM (w_m=0.1430 pinned by radiation era):")
for H0 in (67.4,70.0,73.0):
    # let Om (via wm/h^2) ride; wm is the CMB-robust physical density
    x2=chi2_lcdm(H0,0.1430)
    tag = "  <- Planck value, fits" if H0==67.4 else ("  <- local value, BREAKS" if H0==73 else "")
    print(f"   H0={H0:5.1f}:  chi^2 = {x2:6.2f} / {NDATA} = {x2/NDATA:.2f}{tag}")
    # r2376+c54.160: PIN THE BREAK.  The paper (sec:tensions) says the radiation-pinned ruler
    # "ties LambdaCDM's fit to one H0 ... and breaks it at 73 (chi2/dof ~ 15)".  This receipt
    # divides by NDATA=13 and prints 13.70; on the paper's one-free-parameter counting (12 dof)
    # the same chi^2 is 14.85, i.e. the paper's ~15.  Both are pinned, and so is the fact that
    # the break is an order of magnitude worse than the Planck-value fit.
    if H0 == 67.4:
        assert abs(x2 - 28.56) < 0.30, f"LCDM chi^2 at H0=67.4 = {x2}"
    if H0 == 73.0:
        assert abs(x2 - 178.16) < 1.50, f"LCDM chi^2 at H0=73 = {x2}"
        assert abs(x2/NDATA - 13.70) < 0.15, f"LCDM chi^2/13 at H0=73 = {x2/NDATA}"
        assert abs(x2/(NDATA-1) - 14.85) < 0.15, f"LCDM chi^2/dof at H0=73 = {x2/(NDATA-1)}"
        assert x2/NDATA > 5*x2_cr/(NDATA-1), "the local-H0 break is no longer a break"

print("\n"+"="*78)
print("VERDICT: CR fits DESI DR2 with ONE CMB-calibrated parameter (Omega_m) at the local")
print("H0=73, because the geometric stacking rate makes every BAO ratio H0-independent. LCDM, with")
print("its radiation-pinned physical sound horizon, is forced to H0~67.4 and breaks at H0=73 --")
print("the Hubble tension, now confronted against the full DESI DR2 dataset, not just DR12.")
print("="*78)
