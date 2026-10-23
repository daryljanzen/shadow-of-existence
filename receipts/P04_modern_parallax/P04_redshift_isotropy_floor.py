"""
P04_redshift_isotropy_floor.py -- verifies: the redshift-isotropy floor a matter-tracking expansion would
  produce. Light crossing independent cells of uniform density, each of comoving length R = 8 h^-1 Mpc and
  expanding at its own rate H(1 - f delta_R/3), accumulates a redshift scatter sigma_path ~ 8.8e-3; with the
  correlations of the matter field along the ray it is ~1.6e-2.  Both exceed the rms of the whole measured
  CMB temperature anisotropy (4.1e-5) by more than two orders of magnitude.  [P4 modern_parallax sec:floor]
STATUS: ✔✔   RUN: python3 P04_redshift_isotropy_floor.py   RUNTIME: ~30s
COMPUTES: the Planck 2018 base-LCDM linear matter spectrum with CAMB (sigma_8 = 0.811, z_* = 1089.9); the
  growth rate f from the same spectrum; g = a H f / 3 from the separate-universe rate; the uncorrelated floor
  sigma_path^2 = int dchi g^2 R sigma_R^2(z) and the correlated value int dchi g^2 (1/2pi) int dk k P_R, for
  R = 4..300 h^-1 Mpc; the cell count chi_*/R; the rms of the CAMB temperature spectrum over l = 2..2508; the
  ratios.  GENUINE-FLOOR checks: the correlated value exceeds the uncorrelated one at every R (correlation
  leaves fewer independent cells); holding sigma_R at its present value along the path (no growth
  weighting) raises the floor nearly tenfold.  CONTROL: a rate that does not track the density (f -> 0 in g) gives zero.
BOUND: the linear separate-universe rate H_loc = H(1 - f delta/3), derived here from delta a/a = -delta/3, is
  taken as the hypothesis; the temperature rms is that of the Planck 2018 best-fit spectrum, which fits the
  measured spectrum.
"""
import numpy as np
import sympy as sp
import camb
from scipy.integrate import simpson

def check(t, c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok = True
print("=" * 70); print("P04 redshift-isotropy floor: the scatter a matter-tracking rate accumulates"); print("=" * 70)

# separate-universe rate, derived: rho a^3 = const -> delta a/a = -delta/3; d/dt with delta-dot = f H delta
_a, _rho, _da, _drho = sp.symbols("a rho da drho")
coeff = sp.solve(sp.Eq(_drho/_rho + 3*(_da/_a), 0), _da/_a)[0] / (_drho/_rho)
ok &= check("delta a/a = -(1/3) delta from mass conservation rho a^3 = const", sp.simplify(coeff + sp.Rational(1, 3)) == 0)
_t, _H, _f = sp.symbols("t H f", positive=True)
_D = sp.Function("D")(_t)
dHrel = sp.diff(coeff*_D, _t)                         # H_loc - H = d/dt (delta a/a), with delta = D(t)
ok &= check("H_loc - H = -(1/3) f H delta  (delta-dot = f H delta)",
            sp.simplify(dHrel.subs(sp.Derivative(_D, _t), _f*_H*_D) + _f*_H*_D/3) == 0)

# Planck 2018 base-LCDM
p = camb.CAMBparams()
p.set_cosmology(H0=67.32, ombh2=0.02238, omch2=0.1201, tau=0.0544, mnu=0.06)
p.InitPower.set_params(As=2.101e-9, ns=0.9660)
p.set_for_lmax(2600, lens_potential_accuracy=0)
zs = np.concatenate([np.linspace(0, 10, 101), np.geomspace(10.5, 1100, 60)])
p.set_matter_power(redshifts=zs[::-1], kmax=50.0, nonlinear=False)
r = camb.get_results(p)
h = 0.6732
PK = r.get_matter_power_interpolator(nonlinear=False, hubble_units=False, k_hunit=False)
s8 = float(r.get_sigma8_0()); zstar = r.get_derived_params()['zstar']
ok &= check(f"sigma_8 = {s8:.3f} ~ 0.811, z_* = {zstar:.1f} ~ 1089.9", abs(s8 - 0.811) < 0.005 and abs(zstar - 1089.9) < 0.5)

k = np.geomspace(1e-4, 50, 4000)
W = lambda x: 3*(np.sin(x) - x*np.cos(x))/x**3
zg = np.concatenate([np.linspace(0, 10, 400), np.geomspace(10.01, zstar, 400)])
chi = r.comoving_radial_distance(zg); H = r.hubble_parameter(zg)/2.99792458e5; a = 1/(1 + zg)
D = np.sqrt(PK.P(zg, 0.02)); f = -np.gradient(np.log(D), np.log(1 + zg))
g = a*H*f/3

def floors(Rh, growth=True):
    R = Rh/h
    s2R = np.array([simpson(k**2*PK.P(z if growth else 0.0, k)*W(k*R)**2, x=k)/(2*np.pi**2) for z in zg])
    lin = np.array([simpson(k*PK.P(z, k)*W(k*R)**2, x=k)/(2*np.pi) for z in zg])
    unc = np.sqrt(simpson(g**2*s2R*R, x=chi))
    cor = np.sqrt(simpson(g**2*lin, x=chi))
    return unc, cor, chi[-1]/R

L = np.arange(2, 2509)
TT = r.get_cmb_power_spectra(p, CMB_unit=None, raw_cl=True)['total'][:, 0]
rms = np.sqrt(np.sum((2*L + 1)*TT[L])/(4*np.pi))
ok &= check(f"rms of the temperature anisotropy, l = 2..2508: {rms:.3e} ~ 4.1e-5", abs(rms - 4.13e-5) < 0.03e-5)

res = {Rh: floors(Rh) for Rh in (4, 8, 20, 50, 100, 300)}
for Rh, (u, c, n) in res.items():
    print(f"    R = {Rh:3d} h^-1 Mpc:  uncorrelated {u:.2e}   correlated {c:.2e}   cells {n:5.0f}   corr/rms {c/rms:6.0f}")
u8, c8, n8 = res[8]
ok &= check(f"uncorrelated floor at R=8: {u8:.2e} ~ 8.8e-3 over {n8:.0f} ~ 1200 cells", abs(u8 - 8.8e-3) < 0.1e-3 and abs(n8 - 1200) < 60)
ok &= check(f"correlated value at R=8: {c8:.2e} ~ 1.6e-2", abs(c8 - 1.6e-2) < 0.05e-2)
ok &= check(f"floor / measured rms = {u8/rms:.0f} ~ 210; correlated / rms = {c8/rms:.0f} ~ 380",
            abs(u8/rms - 214) < 6 and abs(c8/rms - 381) < 6)
ok &= check(f"uncorrelated 6.8e-3 at R=20, 2.6e-3 at R=100: {res[20][0]:.2e}, {res[100][0]:.2e}",
            abs(res[20][0] - 6.8e-3) < 0.1e-3 and abs(res[100][0] - 2.6e-3) < 0.1e-3)
want = {4: 1.9e-2, 20: 1.1e-2, 50: 5.9e-3, 100: 3.3e-3, 300: 9.5e-4}
ok &= check("correlated R scan: 1.9e-2, 1.1e-2, 5.9e-3, 3.3e-3, 9.5e-4 at R = 4, 20, 50, 100, 300 (two figures)",
            all(abs(res[R][1] - v) <= 0.05*10**np.floor(np.log10(v)) + 1e-12 for R, v in want.items()))
ok &= check(f"at R = 300 the correlated value is {res[300][1]/rms:.0f} ~ 23 times the measured rms", abs(res[300][1]/rms - 23) < 1.0)
# genuine floor
ok &= check("GENUINE FLOOR: correlation raises the scatter at every R", all(c > u for u, c, _ in res.values()))
u8_const, _, _ = floors(8, growth=False)
ok &= check(f"GENUINE FLOOR: no growth weighting (sigma_R held at z=0) raises it, {u8_const:.2e} = {u8_const/u8:.1f}x",
            u8_const > u8)
# control: the same line integral with a density-independent rate
g0 = a*H*0.0*f/3
s2R8 = np.array([simpson(k**2*PK.P(z, k)*W(k*8/h)**2, x=k)/(2*np.pi**2) for z in zg])
ok &= check("CONTROL: a rate that does not track the density (f -> 0) accumulates no scatter",
            np.sqrt(simpson(g0**2*s2R8*(8/h), x=chi)) == 0.0 and np.sqrt(simpson(g**2*s2R8*(8/h), x=chi)) > 0)
print("=" * 70)
print("RESULT:", "ALL PASS -- a matter-tracking rate would scatter the CMB redshift by ~1e-2, more than\n"
      "         two hundred times the whole measured anisotropy even for uncorrelated cells." if ok else "SOME FAILED")
print("=" * 70)

# --- ASSERTIONS -------------------------------------------------------------------------------
assert ok, "P04 isotropy floor: at least one floor/exclusion check FAILED"
assert abs(u8 - 8.8e-3) < 0.1e-3 and abs(c8 - 1.6e-2) < 0.05e-2
assert abs(rms - 4.13e-5) < 0.03e-5
assert 205 < u8/rms < 220 and 375 < c8/rms < 390
assert u8_const > 9*u8
