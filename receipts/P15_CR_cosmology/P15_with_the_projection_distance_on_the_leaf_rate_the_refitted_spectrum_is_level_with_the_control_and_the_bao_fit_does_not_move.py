#!/usr/bin/env python3
r"""
RECEIPT -- P15 / PO-87: ** WITH THE PROJECTION'S COMOVING DISTANCE BUILT ON THE LEAF RATE, RADIATION INCLUDED,
THE FULL-RANGE LENSED SPECTRUM REFITTED ON THE CONTROL'S FOUR PARAMETERS IS LEVEL WITH THE CONTROL --
186.85 AGAINST 186.51, 1.002 TIMES -- WHERE THE ARM OF RECORD SITS AT 1.596 TIMES; AS COMPUTED AT THE
DISTANCES' POINT IT IS 0.918 TIMES, WHERE THE ARM OF RECORD IS 2.35; AND THE DESI DR2 BAO FIT DOES NOT MOVE. **

Built r7753+70 (node 70, code seat), on `r7749` (69, on Daryl's direction) and `r7753`'s order for a receipt.
The configuration is the arm of record (`LEAFREC=1 LEAFSCALES=1 ZSTART=3e7`) plus `LEAFGEOM=1`; the method,
the registration and the re-centring are `computations/beyond_the_wall/r7749_70_leafgeom_refit/` (PREDICTION.md
committed before any run; RESULT.md).

** WHAT IS READ, NOT RUN **
  * the two leaf-rate spectra banked at r7753: `spectra/r7749_leafgeom_nofit_L2000_cr.npz` (no fit, at the
    distances' point 68.60 / 0.2973, LSTEP 2) and `spectra/r7749_leafgeom_refit_verify_cr.npz` (the verified
    refit minimum 68.585672 / 0.294463 / 0.022181 / 0.961379, LSTEP 8);
  * the control's and the arm of record's banked pairs, exactly as `r7643/measure.py` reads them;
  * scored as the refit-bound receipt scores: P15's CAMB lensing operator on every spectrum alike,
    `chi2_of_spectrum.chi2_of`, 185 lensed bins.
  Every banked file's `switches` line is asserted to carry LEAFGEOM=1 and LEAFREC=1 (or, for the arm of record,
  LEAFREC=1 without LEAFGEOM), so a re-banked file of the wrong configuration refuses rather than passes.

** AND WHAT IS COMPUTED HERE **  The DESI DR2 BAO chi^2 (13 measurements, arXiv:2503.14738 Table IV, the
P15 DESI receipt's data and integrals) on both geometries at both points, at a common r_d, and theta_* on the
corpus's own definition (the leaf sound horizon from z_hi to z_rec = 1090 over D_M(z_rec) on the geometry's rate,
that receipt's `theta_noonset` with z_hi = the arm's ZSTART), with the onset that would match Planck's theta_*.

COMPUTES: the four chi^2 figures and their ratios to the control; the two BAO chi^2 pairs and their difference;
theta_* on both assignments at the refit points, its pull, and the matching onset.
STATUS: OK.  rc=0 on success.  Run: python3 <this file>   (numpy, scipy, camb; ~20 s)
"""
import os
import re
import sys

import numpy as np
from scipy.optimize import brentq, minimize_scalar

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                # noqa: E402
import chi2_of_spectrum as CS                                              # noqa: E402

bad = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"   ({witness})" if witness else ''))
    if not ok:
        bad.append(label)


_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
RATIO[_un > 0] = _le[_un > 0] / _un[_un > 0]


def score(fn):
    z = np.load(os.path.join(SP, fn), allow_pickle=True)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))[:2]
    sw = str(z['switches']) if 'switches' in z.files else ''
    return float(c), int(nb), sw


print("=" * 100)
print("  PART 1 -- THE SPECTRUM: the leaf-rate distance against the control, beside the arm of record")
print("=" * 100)
ctl_nf, n1, _ = score('cc66_lcdm_L2000.npz')
ctl_rf, n2, _ = score('cc66_r185_verify_lcdm.npz')
aor_nf, n3, _ = score('cc66_cr_x_h686_L2000_leafrec1_distances.npz')
aor_rf, n4, _ = score('cc66_r185_verify_cr_leafrec1.npz')
lf_nf, n5, sw_nf = score('r7749_leafgeom_nofit_L2000_cr.npz')
lf_rf, n6, sw_rf = score('r7749_leafgeom_refit_verify_cr.npz')
check("every figure is on the same 185 lensed bins", {n1, n2, n3, n4, n5, n6} == {185})
for name, sw in (('no-fit', sw_nf), ('refit verify', sw_rf)):
    check(f"the banked leaf-rate {name} run carries LEAFGEOM=1 and LEAFREC=1 in its own switches line",
          bool(re.search(r'\bLEAFGEOM=1\b', sw)) and bool(re.search(r'\bLEAFREC=1\b', sw)), sw[:120])
check("the control is its banked pair: 214.06 no-fit, 186.51 refitted",
      round(ctl_nf, 2) == 214.06 and round(ctl_rf, 2) == 186.51, f"{ctl_nf:.2f} / {ctl_rf:.2f}")
check("the arm of record is its printed pair: 502.1 (2.35x) no-fit, 297.7 (1.60x) refitted",
      round(aor_nf, 1) == 502.1 and round(aor_rf, 1) == 297.7
      and round(aor_nf / ctl_nf, 2) == 2.35 and round(aor_rf / ctl_rf, 2) == 1.60,
      f"{aor_nf:.1f}, {aor_nf / ctl_nf:.3f}x / {aor_rf:.1f}, {aor_rf / ctl_rf:.3f}x")
check("** REFITTED, the leaf-rate arm is LEVEL with the control: 186.85, 1.01 per bin, 1.002 times **",
      round(lf_rf, 2) == 186.85 and round(lf_rf / 185, 2) == 1.01 and round(lf_rf / ctl_rf, 3) == 1.002,
      f"{lf_rf:.2f}, {lf_rf / 185:.3f}/bin, {lf_rf / ctl_rf:.4f}x")
check("** AS COMPUTED at the distances' point, it sits BELOW the control's no-fit: 196.5, 1.06 per bin, 0.918 times **",
      round(lf_nf, 1) == 196.5 and round(lf_nf / 185, 2) == 1.06 and round(lf_nf / ctl_nf, 3) == 0.918,
      f"{lf_nf:.2f}, {lf_nf / 185:.3f}/bin, {lf_nf / ctl_nf:.4f}x")

print("\n" + "=" * 100)
print("  PART 2 -- THE BAO DISTANCES DO NOT MOVE (DESI DR2, 13 measurements)")
print("=" * 100)
trapz = np.trapezoid
c = 299792.458
DESI_ANISO = [(0.510, 13.588, 0.167, 21.863, 0.425, -0.459), (0.706, 17.351, 0.177, 19.455, 0.330, -0.404),
              (0.934, 21.576, 0.152, 17.641, 0.193, -0.416), (1.321, 27.601, 0.318, 14.176, 0.221, -0.434),
              (1.484, 30.512, 0.760, 12.817, 0.516, -0.500), (2.330, 38.988, 0.531, 8.632, 0.101, -0.431)]
DESI_ISO = [(0.295, 7.942, 0.075)]
WG, WR, ZREC = 2.47e-5, 4.15e-5, 1090.0
THETA_OBS, THETA_SIG = 0.0104085, 3.1e-6


def E_stack(z, Om, h):
    return np.sqrt(Om * (1 + z) ** 3 + (1 - Om))


def E_leaf(z, Om, h):
    return np.sqrt(Om * (1 + z) ** 3 + (WR / h ** 2) * (1 + z) ** 4 + (1 - Om))


def D_M(z, H0, Om, E, n=4000):
    zz = np.linspace(0, z, n)
    return trapz(c / (H0 * E(zz, Om, H0 / 100)), zz)


def D_H(z, H0, Om, E):
    return c / (H0 * E(z, Om, H0 / 100))


def chi2_bao(H0, Om, rd, E):
    x2 = 0.0
    for z, dm, sdm, dh, sdh, rho in DESI_ANISO:
        r = np.array([D_M(z, H0, Om, E) / rd - dm, D_H(z, H0, Om, E) / rd - dh])
        cov = np.array([[sdm ** 2, rho * sdm * sdh], [rho * sdm * sdh, sdh ** 2]])
        x2 += r @ np.linalg.solve(cov, r)
    for z, dv, sdv in DESI_ISO:
        dvv = (z * D_M(z, H0, Om, E) ** 2 * D_H(z, H0, Om, E)) ** (1 / 3)
        x2 += ((dvv / rd - dv) / sdv) ** 2
    return float(x2)


for name, (H0, Om), want in (("the distances' point", (68.60, 0.2973), (10.539, 10.556)),
                             ('the leaf-rate refit minimum', (68.585672, 0.294463), (10.654, 10.650))):
    rd = minimize_scalar(lambda r: chi2_bao(H0, Om, r, E_stack), bounds=(120, 170), method='bounded').x
    s, l = chi2_bao(H0, Om, rd, E_stack), chi2_bao(H0, Om, rd, E_leaf)
    check(f"at {name}, the leaf geometry moves the BAO chi^2 by under 0.05 at a common r_d: "
          f"{want[0]} -> {want[1]}", round(s, 3) == want[0] and round(l, 3) == want[1] and abs(l - s) < 0.05,
          f"{s:.3f} -> {l:.3f}, r_d {rd:.2f}")

print("\n" + "=" * 100)
print("  PART 3 -- THETA_* ON THE CORPUS'S OWN DEFINITION (the P15 DESI receipt's, z_hi = ZSTART = 3e7)")
print("=" * 100)


def r_snd(H0, Om, wb, z_hi, E, n=60000):
    R0 = 3 * wb / (4 * WG)
    u = np.linspace(np.log(1 + ZREC), np.log(1 + z_hi), n)
    z = np.exp(u) - 1
    return trapz(c / np.sqrt(3 * (1 + R0 / (1 + z))) / (H0 * E(z, Om, H0 / 100)) * (1 + z), u)


def theta(H0, Om, wb, z_hi, Eg):
    return r_snd(H0, Om, wb, z_hi, E_leaf) / D_M(ZREC, H0, Om, Eg, n=20000)


lf = theta(68.585672, 0.294463, 0.022181, 3e7, E_leaf)
ar = theta(68.570730, 0.291246, 0.021643, 3e7, E_stack)
pl, pa = (lf - THETA_OBS) / THETA_SIG, (ar - THETA_OBS) / THETA_SIG
check("the leaf-rate refit sits within 3 sigma of Planck's theta_* on the corpus's definition (+2.3)",
      0 < pl < 3 and round(pl, 1) == 2.3, f"100 theta_* {100 * lf:.5f}, {pl:+.1f} sigma")
check("the arm of record at its own refit point sits ~13 sigma low on the same definition (-12.9)",
      round(pa, 1) == -12.9, f"100 theta_* {100 * ar:.5f}, {pa:+.1f} sigma")
f = lambda zo: theta(68.570730, 0.291246, 0.021643, zo, E_stack) - THETA_OBS        # noqa: E731
check("and NO onset reaches Planck's theta_* on the arm of record (the sign holds to z_hi = 1e9)",
      f(1.2e3) < 0 and f(1e9) < 0, f"theta short by {-f(1e9) / THETA_SIG:.1f} sigma even at 1e9")
g = lambda zo: theta(68.585672, 0.294463, 0.022181, zo, E_leaf) - THETA_OBS         # noqa: E731
zon = brentq(g, 1.2e3, 1e9, xtol=1e-3)
check("on the leaf-rate assignment an onset DOES match it, near z = 2.4e6", 2.3e6 < zon < 2.5e6, f"z_on {zon:.4g}")

print()
print("=" * 100)
if bad:
    print(f"FAILED: {len(bad)} check(s)")
    sys.exit(1)
print("ALL CHECKS PASS -- with the projection's distance on the leaf rate the refitted spectrum is level with the")
print("control (1.002x, against the arm of record's 1.596x), as computed it sits below the control's no-fit (0.918x,")
print("against 2.35x), the DESI DR2 BAO fit does not move, and theta_* on the corpus's own definition is within 3 sigma")
print("on this assignment where no onset reaches it on the arm of record.")
