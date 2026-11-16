#!/usr/bin/env python3
r"""r7814 addendum -- WHY the screen's lower bound broke on the published window.

The probe found ratio 0.65 on an INTERIOR fit, which is the registered negative of the arm that
tests r7806's lower-bound claim as r7808 scoped it.  Before that is reported as the claim's
failure, one alternative has to be ruled out or in: the screening DIRECTION is evaluated at one
grid step above the centre (+4 per cent), while the fit lands at +0.3 per cent of it.  If the
response is appreciably non-linear across that distance, the direction being screened is not the
direction the fit actually moves along, and the shortfall is the probe's and not the claim's.

This recomputes the screen's prediction with the direction taken at a sequence of step sizes.
It asserts nothing; it prints.
"""
import json
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

MZ = np.load(os.path.join(SP, 'r7809_omm_response_lcdm.npz'), allow_pickle=True)
BANK = json.loads(str(MZ['config']))['bank']
WS_ = np.array(sorted(float(x) for x in MZ['omega_m']))
W0 = float(WS_[int(np.argmin(np.abs(WS_ - float(BANK['LOM_centre']) * (BANK['LH0'] / 100.) ** 2)))])


def _key(pref, w):
    return next(k for k in MZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-9)


ML_ = MZ[_key('ls', W0)].astype(float)
MD = np.array([MZ[_key('Dl', w)].astype(float) for w in WS_])
_WR = PchipInterpolator(WS_, MD / MD[int(np.argmin(np.abs(WS_ - W0)))], axis=0)

# the three fitted optima, copied from the probe's own printed output
FITTED = {'100-1758': 0.141199, '700-1760': 0.140521, '1000-1760': 0.140651}
MEASURED = {'100-1758': 0.224, '700-1760': 0.171, '1000-1760': 0.063}

print("=" * 100)
print("r7814 addendum -- the screen's prediction as a function of WHERE the direction is taken")
print("=" * 100)
print(f"\n  the centre is {W0:.6f}; the fits land at "
      + ", ".join(f"{k} -> {v:.6f} ({100 * (v / W0 - 1):+.3f} %)" for k, v in FITTED.items()))

for lo, hi in ((100, 1758), (700, 1760), (1000, 1760)):
    lbl = f'{lo}-{hi}'
    keep = (np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi))
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v):
        return v - base * float((base @ F @ v) / (base @ F @ base))

    def corr(a, b):
        return float((a @ F @ b) / np.sqrt((a @ F @ a) * (b @ F @ b)))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))
    c_st = corr(d_sig, d_tl)

    print(f"\n  window {lbl}   corr(signature, tilt) = {c_st:+.4f}   "
          f"measured gain {MEASURED[lbl]:.3f} %")
    print(f"      {'step %':>9}{'omega_m':>11}{'corr(dir,resid)':>18}{'PREDICTED':>12}{'ratio':>8}")
    STEPS = sorted(set([0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 100 * (FITTED[lbl] / W0 - 1)]))
    for pct in STEPS:
        w = W0 * (1.0 + pct / 100.0)
        if w > WS_[-1] or w < WS_[0]:
            continue
        rb = np.asarray(_WR(w))
        d_w = perp(CS.bin_spectrum(LS, DL * np.interp(LS, ML_, rb))[keep])
        c = corr(d_w, resid)
        pred = c ** 2 * (1.0 - c_st ** 2) * 100.0
        tag = '  <- AT THE FIT' if abs(w - FITTED[lbl]) < 1e-9 else (
            '  <- r7806/r7808/r7812 convention' if abs(pct - 4.0) < 1e-9 else '')
        print(f"      {pct:>8.2f}%{w:>11.6f}{c:>18.4f}{pred:>11.3f}%"
              f"{(MEASURED[lbl] / pred if pred > 0 else float('nan')):>8.2f}{tag}")
print("\n  ⌗ a prediction that moves with the step is a statement about the LINEARISATION;")
print("    a prediction that does not is a statement about the claim.")


# ======================================================================================
#  AND THE SAME TEST ON THE A_L BANK, because r7806/r7808/r7812's ratios were all
#  computed with the one-grid-step convention this has just shown to be step-dependent.
#  Those are THIS seat's own published numbers; whether they survive a smaller step is
#  not something to hedge about when the bank is right here.
# ======================================================================================
print("\n" + "=" * 100)
print("  THE SAME TEST ON r7805's A_L BANK -- do r7812's published ratios survive a smaller step?")
print("=" * 100)
AZ = np.load(os.path.join(SP, 'r7805_alens_response_lcdm.npz'), allow_pickle=True)
ACFG = json.loads(str(next(AZ[k] for k in AZ.files if k.startswith('config'))))
AS_ = np.array(sorted(float(x) for x in ACFG['ALENS']))
A0 = float(AS_[int(np.argmin(np.abs(AS_ - 1.0)))])


def _akey(pref, w):
    return next(k for k in AZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)


AL_ = AZ[_akey('ls', A0)].astype(float)
AD = np.array([AZ[_akey('Dl', w)].astype(float) for w in AS_])
_AR = PchipInterpolator(AS_, AD / AD[int(np.argmin(np.abs(AS_ - 1.0)))], axis=0)
A_STEP = float(AS_[AS_ > A0].min())

A_FITTED = {'100-1758': 1.37732, '700-1760': 1.18409, '1000-1760': 1.04435}
A_MEASURED = {'100-1758': 4.18, '700-1760': 1.79, '1000-1760': 0.15}
print(f"\n  the centre is {A0}; r7812's one-grid-step direction was taken at {A_STEP}")
print("  the fits land at " + ", ".join(f"{k} -> {v}" for k, v in A_FITTED.items()))

for lo, hi in ((100, 1758), (700, 1760), (1000, 1760)):
    lbl = f'{lo}-{hi}'
    keep = (np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi))
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v):
        return v - base * float((base @ F @ v) / (base @ F @ base))

    def corr(a, b):
        return float((a @ F @ b) / np.sqrt((a @ F @ a) * (b @ F @ b)))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))
    c_st = corr(d_sig, d_tl)
    print(f"\n  window {lbl}   measured gain {A_MEASURED[lbl]:.2f} %   "
          f"(r7812 published the ratio at the {A_STEP} step)")
    print(f"      {'A_L':>9}{'offset':>10}{'corr(dir,resid)':>18}{'PREDICTED':>12}{'ratio':>8}")
    for a in (1.005, 1.01, 1.02, 1.05, A_STEP, A_FITTED[lbl]):
        if a > AS_[-1] or a < AS_[0]:
            continue
        rb = np.asarray(_AR(float(a)))
        d_a = perp(CS.bin_spectrum(LS, DL * np.interp(LS, AL_, rb))[keep])
        c = corr(d_a, resid)
        pred = c ** 2 * (1.0 - c_st ** 2) * 100.0
        tag = '  <- r7812' if abs(a - A_STEP) < 1e-12 else (
            '  <- at the fit' if abs(a - A_FITTED[lbl]) < 1e-9 else '')
        print(f"      {a:>9.5f}{100 * (a / A0 - 1):>9.2f}%{c:>18.4f}{pred:>11.3f}%"
              f"{(A_MEASURED[lbl] / pred if pred > 0 else float('nan')):>8.2f}{tag}")
