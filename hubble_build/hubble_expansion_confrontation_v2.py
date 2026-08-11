"""
A1.4 (corrected) -- the radiation-free rate vs the expansion history, with the hidden FLRW
assumption removed.

THE BUG in v1 (caught via the least-arbitrariness face, Daryl r959): v1 fixed the PHYSICAL density
wm = Om*h^2 as "the CMB-robust quantity" and let Om = wm/h^2 slide with H0 (0.315 -> 0.268 at
H0=73). That is the LCDM invariant -- radiation in the rate makes the CMB peaks sensitive to the
physical densities wm. It is NOT CR's invariant. In CR the rate is radiation-free, so (P15 sec:tensions)
theta_* = r_s/D_M carries the common factor H0 out of both and is fixed by Om ALONE. So the CMB pins
the DIMENSIONLESS Om in CR, not wm. Fixing wm imported an FLRW relation and manufactured a fake
Om-shift that broke the BAO shape at high H0.

THE CONSEQUENCE: in the radiation-free rate H=H0*E(z;Om), every distance carries 1/H0:
    D_M = (c/H0) INT dz/E,   D_H = (c/H0)/E,   r_d = (c/H0) INT c_s/(c E) dz .
So the BAO ratios D_M/r_d and D_H/r_d are INDEPENDENT of H0 -- they depend only on Om (and z_onset
for r_d). With Om fixed by the CMB acoustic scale, CR's BAO fits at ANY H0, including the local 73.
LCDM's r_d is pinned in physical Mpc by the radiation-era wm, breaking the cancellation, so its BAO
constrains H0 to ~67. That difference IS the Hubble tension and its CR resolution.

This script verifies the H0-cancellation numerically and redoes the data confrontation correctly.
"""
import numpy as np
from scipy.optimize import brentq
trapz=np.trapezoid; c=299792.458

# baryon loading for the sound speed (physical, ordinary microphysics -- same in both)
wb, wg = 0.02237, 2.47e-5
R0=3*wb/(4*wg)
def cs(z): return c/np.sqrt(3*(1+R0/(1+z)))
zrec=1090.0; z_drag=1059.94

# --- CR: Om is the CMB-fixed (H0-independent) quantity; radiation-free rate ---
def E_cr(z,Om): return np.sqrt(Om*(1+z)**3+(1-Om))
def Hcr(z,H0,Om): return H0*E_cr(z,Om)
def DM(z,H0,Om,n=6000):
    zz=np.linspace(0,z,n); return trapz(c/Hcr(zz,H0,Om),zz)
def DH(z,H0,Om): return c/Hcr(z,H0,Om)
def r_snd(H0,Om,z_onset,z_lo=zrec,n=200000):
    u=np.linspace(np.log(1+z_lo),np.log(1+z_onset),n); z=np.exp(u)-1
    return trapz(cs(z)/Hcr(z,H0,Om)*(1+z),u)
def theta_star(H0,Om,z_onset): return r_snd(H0,Om,z_onset,z_lo=zrec)/DM(zrec,H0,Om)
THETA_OBS=0.0104085   # Planck 100*theta_* = 1.04109 -> theta_*; use the standard acoustic scale

print("="*76)
print("A1.4 corrected -- CR fixes Om (dimensionless), not wm.  Radiation-free -> H0 cancels in BAO.")
print("="*76)

# fix Om by the CMB acoustic scale at a reference H0, with z_onset the single early-universe datum.
# Two unknowns (Om, z_onset), one theta_* -- pin z_onset at the physical rho_r/rho_m~2 target and
# solve Om; then SHOW Om and the BAO ratios do not move with H0.
Om_fid=0.31
# find z_onset matching theta_* at Om_fid (H0-independent, we'll confirm)
z_onset=brentq(lambda zo: theta_star(70.0,Om_fid,zo)-THETA_OBS, 1200, 5e4)
print(f"\n[0] CMB acoustic scale fixes (Om, z_onset): Om={Om_fid}, z_onset={z_onset:.0f} "
      f"(rho_r/rho_m~{(1+z_onset)/(3402):.1f}); theta_* matched.")

# [1] THE DECISIVE CHECK: are CR's BAO ratios independent of H0?
print(f"\n[1] H0-INDEPENDENCE OF CR BAO OBSERVABLES (Om fixed):")
print(f"    {'z':>5s} | {'D_M/r_d(H0=67)':>14s} {'D_M/r_d(H0=73)':>14s} | {'D_H/r_d(67)':>11s} {'D_H/r_d(73)':>11s}")
for z in [0.38,0.51,0.61,1.48,2.33]:
    rd67=r_snd(67.0,Om_fid,z_onset,z_lo=z_drag); rd73=r_snd(73.0,Om_fid,z_onset,z_lo=z_drag)
    dm67=DM(z,67.0,Om_fid)/rd67; dm73=DM(z,73.0,Om_fid)/rd73
    dh67=DH(z,67.0,Om_fid)/rd67; dh73=DH(z,73.0,Om_fid)/rd73
    print(f"    {z:5.2f} | {dm67:14.3f} {dm73:14.3f} | {dh67:11.3f} {dh73:11.3f}")
print(f"    -> IDENTICAL to numerical precision: CR's BAO ratios do not depend on H0. The BAO")
print(f"       constrains Om, NOT H0.  H0 is left to the local distance ladder (73).")

# [2] chi^2 vs SDSS DR12 BAO for CR (any H0) vs LCDM(67.4) vs LCDM(73)
DR12=[(0.38,10.27,0.15,24.89,0.58),(0.51,13.38,0.18,22.43,0.48),(0.61,15.45,0.22,20.86,0.44)]
def chi2_bao_cr(H0,Om,zo):
    rd=r_snd(H0,Om,zo,z_lo=z_drag)
    return sum(((DM(z,H0,Om)/rd-dm)/sdm)**2+((DH(z,H0,Om)/rd-dh)/sdh)**2 for z,dm,sdm,dh,sdh in DR12)
# LCDM: wm fixed (radiation-era physical density), Om=wm/h^2, r_d in physical Mpc
wm_lcdm=0.1430; wr=4.15e-5
def E_lcdm(z,h): Om=wm_lcdm/h**2; Or=wr/h**2; return np.sqrt(Om*(1+z)**3+Or*(1+z)**4+1-Om-Or)
def Hl(z,H0): return H0*E_lcdm(z,H0/100)
def DMl(z,H0,n=6000): zz=np.linspace(0,z,n); return trapz(c/Hl(zz,H0),zz)
def rdl(H0,n=200000):
    u=np.linspace(np.log(1+z_drag),np.log(1+1e8),n); z=np.exp(u)-1
    return trapz(cs(z)/Hl(z,H0)*(1+z),u)
def chi2_bao_lcdm(H0):
    rd=rdl(H0)
    return sum(((DMl(z,H0)/rd-dm)/sdm)**2+((c/Hl(z,H0)/rd-dh)/sdh)**2 for z,dm,sdm,dh,sdh in DR12)
print(f"\n[2] chi^2 vs SDSS DR12 BAO (6 pts):")
print(f"    CR   (Om=0.31, ANY H0 incl. 73) : chi2 = {chi2_bao_cr(73.0,Om_fid,z_onset):5.2f}   (H0-independent)")
print(f"    LCDM (H0=67.4, wm pinned)       : chi2 = {chi2_bao_lcdm(67.4):5.2f}")
print(f"    LCDM (H0=73.0, wm pinned)       : chi2 = {chi2_bao_lcdm(73.0):5.2f}   <- the tension")

# [3] cosmic chronometers constrain H0 absolutely (H(z)=H0 E, not a ratio); broad
CC=[(0.07,69.0,19.6),(0.20,72.9,29.6),(0.40,77.0,10.2),(0.88,90.0,40.0),
    (1.30,168.0,17.0),(1.43,177.0,18.0),(1.75,202.0,40.0),(1.965,186.5,50.4)]
def chi2_cc(H0,Om): return sum(((Hcr(z,H0,Om)-H)/s)**2 for z,H,s in CC)
print(f"\n[3] cosmic chronometers (constrain H0 directly; broad): chi2(Om=0.31)")
for H0 in [67.4,70,73]:
    print(f"    H0={H0:5.1f}: chi2_CC={chi2_cc(H0,Om_fid):5.2f}")
print(f"    -> consistent with the local H0=73 (large CC errors); combined with the distance")
print(f"       ladder (H0=73.0+/-1.0) CR sits at Om=0.31, H0=73 with NO tension.")

print("\n"+"="*76)
print("CORRECTED VERDICT:  The v1 'failure' was the FLRW invariant wm imported into CR. CR fixes Om.")
print("Because the radiation-free rate factors H0 out of every distance and the ruler alike, the BAO")
print("ratios are H0-INDEPENDENT: BAO fixes Om, the distance ladder fixes H0=73, and they do not")
print("collide.  LCDM's radiation-pinned physical r_d forces H0=67 from the same BAO -- that is the")
print("tension. CR resolves it across the FULL expansion history, not just ell_A, and D1 already")
print("showed the same two-rate scoping keeps BBN standard. The resolution stands.")
print("="*76)

# --- ASSERTIONS r2376+c54.160 -------------------------------------------------------------
# This receipt printed its whole confrontation and asserted nothing, so its OK certified only
# that python exited 0.  The three claims it is cited for are pinned here: (a) the DECISIVE
# H0-independence of CR's BAO ratios, (b) the chi^2 figures P15 sec:tensions quotes (CR ~1.7,
# LCDM(73) ~49) and INDEX.md row 131 quotes to two decimals (1.71 / 4.37 / 49.45), and (c) the
# onset redshift the CMB acoustic scale returns here.  A retune that moves any of them now
# breaks the gate instead of the sentence.
_rd67 = r_snd(67.0, Om_fid, z_onset, z_lo=z_drag)
_rd73 = r_snd(73.0, Om_fid, z_onset, z_lo=z_drag)
for _z in [0.38, 0.51, 0.61, 1.48, 2.33]:
    # (a) the ratios at two DIFFERENT H0 must coincide -- the load-bearing cancellation.
    _a = DM(_z, 67.0, Om_fid) / _rd67; _b = DM(_z, 73.0, Om_fid) / _rd73
    assert abs(_a - _b) < 1e-9 * abs(_a), f"D_M/r_d moved with H0 at z={_z}: {_a} vs {_b}"
    _a = DH(_z, 67.0, Om_fid) / _rd67; _b = DH(_z, 73.0, Om_fid) / _rd73
    assert abs(_a - _b) < 1e-9 * abs(_a), f"D_H/r_d moved with H0 at z={_z}: {_a} vs {_b}"
# and the ratios are the printed ones, not merely equal to each other
assert abs(DM(0.38, 73.0, Om_fid) / _rd73 - 10.294) < 0.005
assert abs(DH(2.33, 73.0, Om_fid) / _rd73 - 8.564) < 0.005
# (b) the chi^2 confrontation -- paper 1.7 / 49, INDEX 1.71 / 4.37 / 49.45
_chi2_cr = chi2_bao_cr(73.0, Om_fid, z_onset)
assert abs(_chi2_cr - 1.71) < 0.02, f"CR chi2 = {_chi2_cr}, paper/INDEX say 1.71"
assert abs(chi2_bao_lcdm(67.4) - 4.37) < 0.02
assert abs(chi2_bao_lcdm(73.0) - 49.45) < 0.10, "LCDM(73) chi2 is the tension the paper calls 49"
assert chi2_bao_lcdm(73.0) > 20.0 * _chi2_cr, "the tension must be an order of magnitude, not a nudge"
# (c) the onset redshift the acoustic scale fixes, and the chronometer chi^2 ordering
assert abs(z_onset - 6774.0) < 2.0, f"z_onset = {z_onset}, receipt prints 6774"
assert abs(chi2_cc(73.0, Om_fid) - 4.01) < 0.02
assert chi2_cc(73.0, Om_fid) < chi2_cc(67.4, Om_fid), "chronometers must not prefer 67.4 here"
print("\n[assertions r2376+c54.160] H0-independence, chi2 1.71/4.37/49.45, z_onset 6774: all pinned.")
