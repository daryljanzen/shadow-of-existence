#!/usr/bin/env python3
r"""r7800 (60) -- ADDENDUM, DECLARED POST HOC.

The eight arms of PREDICTION.md were pushed before anything was measured.  They answered the order's
question -- the displacement survives omega_b being free, essentially untouched -- but they do not say
WHY, and the registration did not ask.  This file asks, after the fact, and is kept separate for that
reason.  Nothing here is a registered prediction.

** WHAT IT COMPUTES. **  The SHAPE overlap between the omega_b response and the signature, in the
metric's own units: for each window, the fraction of the signature's own chi^2 that the best multiple
of the omega_b direction can remove, and the correlation between the two templates under the
covariance.  Neither is a new spectrum: both come from the banked response and the banked baseline.
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
_z = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra',
                          'L820_lcdm_L2512_nk800.npz'))
LS, RAW = _z['ls'].astype(float), _z['Dl'].astype(float)


def _fisher(keep):
    cov = CS.COV_TT[np.ix_(keep, keep)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(keep.sum())))
    return 0.5 * (F + F.T)


_k0 = np.isfinite(CS.bin_spectrum(LS, RAW))
_F0 = _fisher(_k0)
_m0 = CS.bin_spectrum(LS, RAW)[_k0]
DL = RAW * float((_m0 @ _F0 @ CS.X_DATA[_k0]) / (_m0 @ _F0 @ _m0))

WZ = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra',
                          'r6897_wb_response_lcdm.npz'), allow_pickle=True)
WBS = np.array(sorted({float(k.split('__')[1]) for k in WZ.files if k.startswith('Dl__')}))
WB0 = WBS[len(WBS) // 2]


def _key(pref, w):
    return next(k for k in WZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)


WL = WZ[_key('ls', WB0)].astype(float)
WD = np.array([WZ[_key('Dl', w)].astype(float) for w in WBS])
RAT = PchipInterpolator(WBS, WD / WD[len(WBS) // 2], axis=0)

print("=" * 100)
print("  r7800 ADDENDUM -- WHY omega_b CANNOT ABSORB THE SIGNATURE: THE SHAPES DO NOT OVERLAP")
print("=" * 100)
print("\n  the two templates in l, as fractional departures from the baseline:")
print(f"  {'l':>6}{'signature S-1':>16}{'omega_b +4% ratio-1':>22}")
for lsel in (200, 500, 800, 996, 1200, 1500, 1760, 1900):
    j = int(np.argmin(abs(WL - lsel)))
    s = float(np.exp(-K * (WL[j] / LD) ** 2) - 1.0)
    w = float(np.asarray(RAT(WBS[3]))[j] - 1.0)
    print(f"  {WL[j]:>6.0f}{s:>16.5f}{w:>22.5f}")
print("\n  ⇒ the signature falls MONOTONICALLY with l -- it is a Gaussian envelope.  The omega_b")
print("    response does not: it is NEGATIVE below about l = 900 and POSITIVE above it, because")
print("    omega_b moves the PEAKS, through the baryon loading, and not the envelope.")

print("\n  the overlap in the metric's own units, per window:")
print(f"  {'window':>12}{'bins':>6}{'corr(S, wb)':>14}{'chi2 removable':>17}{'by tilt':>10}")
for lo, hi in ((100, 1758), (700, 1760), (1000, 1760)):
    keep = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
    n = int(keep.sum())
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]
    tgt = CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep]
    d_sig = tgt - base * float((base @ F @ tgt) / (base @ F @ base))
    wbdir = CS.bin_spectrum(LS, DL * np.interp(LS, WL, np.asarray(RAT(WBS[3])))) [keep]
    d_wb = wbdir - base * float((base @ F @ wbdir) / (base @ F @ base))
    tl = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep]
    d_tl = tl - base * float((base @ F @ tl) / (base @ F @ base))
    def frac(d):
        return float((d_sig @ F @ d) ** 2 / ((d @ F @ d) * (d_sig @ F @ d_sig)))
    print(f"  {f'{lo}-{hi}':>12}{n:>6}"
          f"{float((d_sig @ F @ d_wb) / np.sqrt((d_sig @ F @ d_sig) * (d_wb @ F @ d_wb))):>14.4f}"
          f"{frac(d_wb) * 100:>16.1f}%{frac(d_tl) * 100:>9.1f}%")
print("\n  ⇒ the tilt direction overlaps the signature strongly, which is why it absorbs 70-96%.")
print("    The omega_b direction overlaps it weakly, which is why freeing it changes the fitted")
print("    displacement by about a part in a hundred and not by a factor.")
print("\n  ⇒ ⛭ SO THE ROW'S TERMINATING CLAUSE IS NOT MET BY THE BARYON DENSITY, AND THE REASON IS")
print("      STRUCTURAL RATHER THAN A MATTER OF PRECISION: the signature is an ENVELOPE and omega_b")
print("      is a PEAK-PHASE direction.  A parameter has to have the shape to absorb a shape.")
