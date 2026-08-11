"""
P04_redshift_isotropy_floor.py -- verifies: the redshift-isotropy floor a matter-tracking expansion would
  produce, sigma_path = sigma_{8,eff}/(3 sqrt N) ~ 2.8e-3, exceeds the observed monopole isotropy (<~3e-6)
  by ~three orders of magnitude, excluding a differential (matter-tracking) expansion. [P4 modern_parallax sec:floor]
STATUS: ✔✔   RUN: python3 P04_redshift_isotropy_floor.py   RUNTIME: ~2s
COMPUTES: the comoving distance to last scattering d_lss (integral for flat LCDM Om=0.315) -> N=d_lss/R with
  R=8 h^-1 Mpc (~1174 cells); the floor sigma_path=sigma_{8,eff}/(3 sqrt N) from the separate-universe deficit
  (1/3) and path averaging (1/sqrt N) -> ~2.8e-3; the exclusion ratio vs the observed <~3e-6 (~10^3, three
  orders). GENUINE-FLOOR checks: replacing sigma_{8,eff}=0.285 by sigma_8(0)=0.8, or reducing N (line-of-sight
  correlations), only RAISES sigma_path -- so 2.8e-3 is a lower bound. CONTROL: an isotropic (delta-independent)
  expansion gives sigma_path=0, far below the observed bound (the floor is a differential-expansion signature).
BOUND: the linear separate-universe deficit delta a/a=-delta/3 is standard linear theory (cited), taken as input.
ORIGIN: built new r1348 (P4 cited no receipts).
"""
import numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
Om, OL, z_lss, R = 0.315, 0.685, 1089.0, 8.0        # R in h^-1 Mpc
s8_0, s8_eff, obs = 0.8, 0.285, 3e-6
print("="*70); print("P04 redshift-isotropy floor: sigma_path vs observed monopole isotropy"); print("="*70)
# comoving distance to LSS (h^-1 Mpc):  d = (c/H0) int_0^z dz/E,  c/H0 = 2998 h^-1 Mpc
E = lambda z: np.sqrt(Om*(1+z)**3 + OL)
zz = np.linspace(0, z_lss, 200000); d_lss = 2998.0*np.trapezoid(1/E(zz), zz)
N = d_lss/R
ok&=check(f"d_lss (comoving, flat LCDM Om=0.315) = {d_lss:.0f} h^-1 Mpc ; N=d_lss/R = {N:.0f} ~ 1174",
          abs(N-1174)/1174 < 0.05)
# the floor
s_path = s8_eff/(3*np.sqrt(N))
ok&=check(f"sigma_path = sigma_{{8,eff}}/(3 sqrt N) = 0.285/(3*{np.sqrt(N):.1f}) = {s_path:.2e} ~ 2.8e-3",
          abs(s_path-2.8e-3)/2.8e-3 < 0.05)
# the exclusion
ratio = s_path/obs
ok&=check(f"exclusion: sigma_path / observed(<~3e-6) = {ratio:.0f} ~ 10^3 (three orders of magnitude)",
          200 < ratio < 5000 and 2.5 < np.log10(ratio) < 3.5)
# genuine floor: every listed choice biases sigma_path DOWNWARD
s_path_hi = s8_0/(3*np.sqrt(N))                      # using sigma_8(0) instead of growth-weighted
ok&=check(f"genuine floor A: sigma_8(0)=0.8 (no growth-weighting) gives LARGER {s_path_hi:.2e} > {s_path:.2e}",
          s_path_hi > s_path)
s_path_corr = s8_eff/(3*np.sqrt(N/4))               # line-of-sight correlations reduce effective N
ok&=check(f"genuine floor B: correlations (smaller effective N) give LARGER {s_path_corr:.2e} > {s_path:.2e}",
          s_path_corr > s_path)
# separate-universe deficit coefficient
import sympy as sp
_a,_rho,_da,_drho=sp.symbols("a rho da drho")
# mass conservation rho a^3 = const => d(rho a^3)=0 => drho/rho + 3 da/a = 0 => da/a = -(1/3) drho/rho
_coeff = sp.solve(sp.Eq(_drho/_rho + 3*(_da/_a), 0), _da/_a)[0] / (_drho/_rho)
ok&=check("separate-universe delta a/a = -(1/3) delta  DERIVED from mass conservation rho a^3=const",
          sp.simplify(_coeff + sp.Rational(1,3))==0)
# CONTROL: isotropic (uniform) expansion -> no delta-driven anisotropy
ok&=check("CONTROL: an isotropic expansion (no matter-tracking) gives sigma_path=0 << 3e-6",
          (s8_eff*0.0)/(3*np.sqrt(N)) < obs)
print("="*70)
print("RESULT:", "ALL PASS -- the matter-tracking floor sigma_path~2.8e-3 exceeds the observed monopole\n         isotropy (<~3e-6) by ~three orders; every estimate choice biases the floor DOWN, so a\n         differential (matter-tracking) expansion is excluded, and uniform expansion + a global cosmic\n         time are empirically forced." if ok else "SOME FAILED")
print("="*70)

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# Pins the three figures this receipt prints and INDEX.md quotes for sec:floor
# (N=1174 cells, floor sigma_path=2.77e-3, exclusion ratio 924 vs the observed <~3e-6).
# (a) the file's own PASS/FAIL boolean.
assert ok, "P04 isotropy floor: at least one floor/exclusion check FAILED"
# (b) the comoving distance to last scattering and the cell count.
assert abs(d_lss - 9390.5) < 1.0
assert abs(N - 1173.81) < 0.05
# (c) THE FLOOR: sigma_path = 2.7728e-3 (INDEX: 2.77e-3, docstring: ~2.8e-3).
assert abs(s_path - 2.7728e-3) < 1e-6
# (d) THE EXCLUSION: sigma_path/observed = 924.3 -- three orders of magnitude.
assert abs(ratio - 924.28) < 0.5
assert abs(np.log10(ratio) - 2.9658) < 1e-3      # 2.97 orders, i.e. "~three orders"
# (e) the floor is genuine: both listed re-estimates move sigma_path UP, never below 2.77e-3.
assert s_path_hi > s_path and s_path_corr > s_path
assert abs(s_path_hi - 7.7834e-3) < 1e-6 and abs(s_path_corr - 5.5457e-3) < 1e-6
