#!/usr/bin/env python3
r"""r7804 (60) -- PO-24's N_eff fit, on order r7803 (69).

Same harness as r7800 (r7611+70's joint fit: baseline, metric, binning, covariance), with the free
direction swapped from omega_b to N_eff, read from 70's r7801 bank as a RATIO to its own centre --
never as an absolute spectrum, because the response run is a different configuration from the baseline.
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize, minimize_scalar
from scipy.interpolate import PchipInterpolator

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

R, LD = 1.0926, 1489.5783
K = R ** 2 - 1
NEFF_ADOPTED = 3.046            # INPUT: P16's adopted value, "adopted here rather than derived"
NEFF_QUOTED, NEFF_QUOTED_SIG = 2.99, 0.17   # INPUT: the constraint P16 itself quotes (Planck)

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


def window(lo, hi):
    return (np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi))


NZ = np.load(os.path.join(SP, 'r7801_neff_response_lcdm.npz'), allow_pickle=True)
NS = np.array(sorted({float(k.split('__')[1]) for k in NZ.files if k.startswith('Dl__')}))
N0 = NS[len(NS) // 2]


def _key(pref, w):
    return next(k for k in NZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)


NL = NZ[_key('ls', N0)].astype(float)
ND = np.array([NZ[_key('Dl', w)].astype(float) for w in NS])
NRAT = ND / ND[len(NS) // 2]
_RAT = PchipInterpolator(NS, NRAT, axis=0)


def ratio_on_LS(ne):
    rb = np.asarray(_RAT(float(ne)))
    return np.interp(LS, NL, rb, left=rb[0], right=rb[-1])


print("=" * 100)
print("r7804 (60) -- PO-24's N_eff fit: is the tilt displacement absorbed by the neutrino count?")
print(f"  signature exp[-(r^2-1)(l/l_D)^2], r = {R}, l_D = {LD}")
print(f"  P16 ADOPTS N_eff = {NEFF_ADOPTED} ('adopted here rather than derived') and QUOTES")
print(f"    {NEFF_QUOTED} +/- {NEFF_QUOTED_SIG} as the number a departure would have to move")
print(f"    ⇒ that is {NEFF_QUOTED_SIG / NEFF_QUOTED * 100:.2f} per cent, against omega_b's 0.65 --"
      f" about nine times more room in sigma")
print("=" * 100)
print(f"\n  70's bank: N_eff = {list(NS)}, centre {N0}")
print(f"  ⇒ OFFSET to the adopted value: {NEFF_ADOPTED - N0:+.3f}, carried explicitly below")
print(f"  its l grid: {NL[0]:.0f} to {NL[-1]:.0f} step {NL[1] - NL[0]:.0f}, {len(NL)} points")

REACH = float(NL[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]
print(f"\n  B2  reach = {REACH:.0f}; available windows: {AVAIL}")

d1 = np.diff(NRAT, axis=0)
d2 = np.diff(d1, axis=0)
good = np.abs(d1).max(axis=0) > 0
CURV = float(np.max(np.abs(d2)[:, good].max(axis=0) / np.abs(d1)[:, good].max(axis=0)))
print(f"  B4  worst |second difference| / |first| across the grid: {CURV:.4f}")
for lsel in (500, 996, 1500, 1900):
    j = int(np.argmin(abs(NL - lsel)))
    print(f"        l = {NL[j]:>5.0f} : ratio over the five N_eff = "
          f"[{', '.join(f'{v:.5f}' for v in NRAT[:, j])}]")


def fit2(target, keep, F):
    def at(dn):
        m = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** dn)[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r)
    o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
    return float(o.x), float(at(float(o.x)))


def fit3(target, keep, F):
    def at(p):
        m = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** float(p[0]) * ratio_on_LS(p[1]))[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r)
    runs = []
    for dn0 in (-0.30, -0.10, 0.0, 0.10):
        for ne0 in (NS[1], N0, NS[3]):
            o = minimize(at, x0=[dn0, ne0], method='L-BFGS-B',
                         bounds=[(-3.0, 3.0), (NS[0], NS[-1])],
                         options={'ftol': 1e-14, 'gtol': 1e-12})
            runs.append((float(o.fun), float(o.x[0]), float(o.x[1])))
    best = min(runs)          # r7802's form: a deterministic argmin, no tie-break epsilon
    spread = tuple(max(x[i] for x in runs) - min(x[i] for x in runs) for i in range(3))
    return best[1], best[2], best[0], spread


print("\n" + "=" * 100)
print("  A1, C5, C6, C8 -- THE FITS")
print("=" * 100)
ROWS = []
for lo, hi in AVAIL:
    keep = window(lo, hi)
    n = int(keep.sum())
    F = _fisher(keep)
    tgt = CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep]
    m_amp = CS.bin_spectrum(LS, DL)[keep]
    r_amp = tgt - float((m_amp @ F @ tgt) / (m_amp @ F @ m_amp)) * m_amp
    c_amp = float(r_amp @ F @ r_amp)
    dn2, c2 = fit2(tgt, keep, F)
    dn3, ne3, c3, sp3 = fit3(tgt, keep, F)
    dne = ne3 - NEFF_ADOPTED
    ROWS.append(dict(lo=lo, hi=hi, n=n, dn2=dn2, dn3=dn3, c2=c2, c3=c3, c_amp=c_amp, ne3=ne3,
                     dne=dne, sp3=sp3, surv=abs(dn3) / abs(dn2) * 100.0,
                     a2=(1 - c2 / c_amp) * 100.0, a3=(1 - c3 / c_amp) * 100.0,
                     edge=min(abs(ne3 - NS[0]), abs(ne3 - NS[-1])) < 1e-9))
    r = ROWS[-1]
    print(f"\n      window {lo}-{hi}, {n} covered bins")
    print(f"        amplitude alone : chi^2/bin {c_amp / n:>9.4f}")
    print(f"        + tilt          : chi^2/bin {c2 / n:>9.4f}  Delta n {dn2:+.5f}  absorbed {r['a2']:5.1f} %")
    print(f"        + tilt + N_eff  : chi^2/bin {c3 / n:>9.4f}  Delta n {dn3:+.5f}  absorbed {r['a3']:5.1f} %")
    print(f"        the N_eff wanted: {ne3:.5f}   = {dne:+.5f} from the adopted {NEFF_ADOPTED}"
          f"   = {dne / NEFF_QUOTED_SIG:+.2f} of the quoted sigma"
          + ("   ⛔ AT THE BANK'S EDGE" if r['edge'] else ""))
    print(f"        SURVIVES        : {r['surv']:.3f} per cent of the displacement")
    print(f"        multistart spread: fun {sp3[0]:.2e}  Delta n {sp3[1]:.2e}  N_eff {sp3[2]:.2e}")

print("\n" + "=" * 100)
print("  C7 -- 70's SHAPE CLAIM, TESTED: does the N_eff direction overlap the signature?")
print("=" * 100)
print(f"  {'window':>12}{'corr(S, Neff)':>16}{'Neff removes':>14}{'tilt removes':>14}")
for lo, hi in AVAIL:
    keep = window(lo, hi)
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v):
        return v - base * float((base @ F @ v) / (base @ F @ base))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_ne = perp(CS.bin_spectrum(LS, DL * np.interp(LS, NL, np.asarray(_RAT(NS[3]))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])

    def sh(d):
        return float((d_sig @ F @ d) ** 2 / ((d @ F @ d) * (d_sig @ F @ d_sig))) * 100.0
    corr = float((d_sig @ F @ d_ne) / np.sqrt((d_sig @ F @ d_sig) * (d_ne @ F @ d_ne)))
    print(f"  {f'{lo}-{hi}':>12}{corr:>16.4f}{sh(d_ne):>13.1f}%{sh(d_tl):>13.1f}%")
print("  ⌗ omega_b's correlations were -0.18, -0.24, -0.45 and it removed 3.3, 5.7, 20.0 per cent.")

print("\n" + "=" * 100)
print("  THE ANSWER")
print("=" * 100)
for r in ROWS:
    print(f"      {r['lo']}-{r['hi']}: Delta n {r['dn2']:+.5f} -> {r['dn3']:+.5f}"
          f"  ({r['surv']:.2f} % survives)   N_eff {r['ne3']:.4f}"
          f"  = {r['dne'] / NEFF_QUOTED_SIG:+.2f} quoted sigma")
