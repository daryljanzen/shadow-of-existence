#!/usr/bin/env python3
r"""r7804 (60) -- ADDENDUM, DECLARED POST HOC.

The nine arms of PREDICTION.md were pushed before anything was measured.  They answered the order --
the displacement survives N_eff being free, and the excursion the fit wants is INSIDE the constraint
the corpus quotes -- and Ⓒ⑦ refuted 70's shape claim.  What they do not say is WHY a "monotone tilt
across the damping tail" is a bad absorber, and the registration did not ask.  This file asks, after
the fact, and is kept separate for that reason.  Nothing here is a registered prediction.

** WHAT IT COMPUTES. **  The overlap of the N_eff direction with the TILT direction, under the same
covariance -- i.e. whether N_eff is largely a tilt already, in which case the free tilt has taken
whatever it could and N_eff can add nothing.  Compared against omega_b on the same measure.
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.interpolate import PchipInterpolator

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

R, LD = 1.0926, 1489.5783
K = R ** 2 - 1
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
_z = np.load(os.path.join(SP, 'L820_lcdm_L2512_nk800.npz'))
LS, RAW = _z['ls'].astype(float), _z['Dl'].astype(float)


def _fisher(keep):
    cov = CS.COV_TT[np.ix_(keep, keep)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(keep.sum())))
    return 0.5 * (F + F.T)


_k0 = np.isfinite(CS.bin_spectrum(LS, RAW))
_F0 = _fisher(_k0)
_m0 = CS.bin_spectrum(LS, RAW)[_k0]
DL = RAW * float((_m0 @ _F0 @ CS.X_DATA[_k0]) / (_m0 @ _F0 @ _m0))


def load(name, pref='Dl'):
    Z = np.load(os.path.join(SP, name), allow_pickle=True)
    vals = np.array(sorted({float(k.split('__')[1]) for k in Z.files if k.startswith('Dl__')}))
    c = vals[len(vals) // 2]

    def key(p, w):
        return next(k for k in Z.files
                    if k.startswith(p + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)
    L = Z[key('ls', c)].astype(float)
    D = np.array([Z[key('Dl', w)].astype(float) for w in vals])
    return vals, c, L, PchipInterpolator(vals, D / D[len(vals) // 2], axis=0)


NS, N0, NL, NRAT = load('r7801_neff_response_lcdm.npz')
WS, W0, WL, WRAT = load('r6897_wb_response_lcdm.npz')

print("=" * 100)
print("  r7804 ADDENDUM -- WHY A MONOTONE TAIL TILT IS A BAD ABSORBER: IT IS ALREADY THE TILT")
print("=" * 100)
print("\n  the three directions as fractional departures from the baseline:")
print(f"  {'l':>6}{'signature S-1':>16}{'N_eff +0.25':>14}{'omega_b +4%':>14}{'tilt dn=+0.01':>15}")
for lsel in (200, 500, 996, 1500, 1900):
    j = int(np.argmin(abs(NL - lsel)))
    s = float(np.exp(-K * (NL[j] / LD) ** 2) - 1.0)
    ne = float(np.asarray(NRAT(NS[3]))[j] - 1.0)
    jw = int(np.argmin(abs(WL - lsel)))
    wb = float(np.asarray(WRAT(WS[3]))[jw] - 1.0)
    tl = float((NL[j] / 1000.0) ** 0.01 - 1.0)
    print(f"  {NL[j]:>6.0f}{s:>16.5f}{ne:>14.5f}{wb:>14.5f}{tl:>15.5f}")

print("\n  the overlaps under the covariance, per window.")
print("  ⌗ AND THE QUANTITY THAT MATTERS IS THE LAST COLUMN, not the first two.  The first form of")
print("    this file compared each direction with the TILT and concluded that N_eff is 'far more")
print("    tilt-like than omega_b' -- which the table below CONTRADICTS, omega_b reaching 0.479")
print("    against N_eff's 0.172.  I wrote the conclusion before reading the numbers and the")
print("    refutation was printed directly above it.  ⇒ GUARD: a sentence that states a comparison")
print("    must be written after the comparison is on the screen, not before.")
print("  ⇒ What an absorber has to overlap is not the signature and not the tilt: it is the")
print("    RESIDUAL AFTER THE TILT -- the part the already-free tilt cannot take.  That is the")
print("    last column, and it is the test both parameters actually fail.")
hdr = ('window', 'corr(S,tilt)', 'corr(Neff,tilt)', 'corr(wb,tilt)',
       'Neff vs resid', 'wb vs resid')
print(f"  {hdr[0]:>12}{hdr[1]:>14}{hdr[2]:>17}{hdr[3]:>15}{hdr[4]:>15}{hdr[5]:>14}")
for lo, hi in ((100, 1758), (700, 1760), (1000, 1760)):
    keep = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v, b=None):
        b = base if b is None else b
        return v - b * float((b @ F @ v) / (b @ F @ b))

    def corr(a, b):
        return float((a @ F @ b) / np.sqrt((a @ F @ a) * (b @ F @ b)))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_ne = perp(CS.bin_spectrum(LS, DL * np.interp(LS, NL, np.asarray(NRAT(NS[3]))))[keep])
    d_wb = perp(CS.bin_spectrum(LS, DL * np.interp(LS, WL, np.asarray(WRAT(WS[3]))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    # the residual the free tilt cannot take: the signature with its best tilt multiple removed
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))
    print(f"  {f'{lo}-{hi}':>12}{corr(d_sig, d_tl):>14.4f}{corr(d_ne, d_tl):>17.4f}"
          f"{corr(d_wb, d_tl):>15.4f}{corr(d_ne, resid):>15.4f}{corr(d_wb, resid):>14.4f}")

print("\n  ⇒ The signature is almost exactly a tilt -- corr -0.85 to -0.98 -- which is why the free")
print("    tilt absorbs 70 to 97 per cent of it.  What is left is the small part no power law")
print("    removes, and THAT is what an absorber must overlap.")
print("\n  ⇒ ⛭ SO 70's SHAPE ARGUMENT DOES NOT HOLD, AND NOT FOR THE REASON I FIRST WROTE.  A")
print("      monotone tilt across the damping tail is not disqualified for being tilt-like; N_eff")
print("      is barely tilt-like.  It is disqualified because it is nearly ORTHOGONAL to the")
print("      residual the tilt leaves -- it points somewhere the problem is not.  The absorber")
print("      PO-24's clause needs must overlap that residual, and neither parameter measured so far")
print("      does.")
