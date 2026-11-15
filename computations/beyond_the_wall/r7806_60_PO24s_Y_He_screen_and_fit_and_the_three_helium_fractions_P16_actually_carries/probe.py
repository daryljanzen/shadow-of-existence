#!/usr/bin/env python3
r"""r7806 (60) -- PO-24's Y_He screen and fit, on order r7805 (69).

Same harness as r7800/r7804 (r7611+70's joint fit: baseline, metric, binning, covariance), with the
free direction swapped to Y_He, read from 70's r7801 bank as a RATIO to its own centre -- never as
an absolute spectrum, because the bank's grid differs from the baseline's (L2512/nk800 against
LMAXL 2000/KFAC 2), even though its centre equals the baseline's own helium fraction.

The screen runs FIRST, on r7804's own measure, and the fit runs REGARDLESS of it, as the order says.
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

# ---- THE THREE HELIUM FRACTIONS P16 CARRIES, each read out of P16's own files ---------------------
YP_BORN = 0.2432          # INPUT: P16's network, Born level, before the radiative correction
YP_CORR_FAC = 1.016       # INPUT: the standard radiative/Coulomb correction the Born network omits
YP_NET = 0.2471           # INPUT: = YP_BORN * YP_CORR_FAC, the figure P16 quotes
YP_NET_FRAC = 0.006       # INPUT: P16_theory_error_and_likelihood.py's sYp_frac, the theory error
YP_OBS, YP_OBS_SIG = 0.2453, 0.0034   # INPUT: the same receipt's OBS['Yp'], Aver et al. 2021
YP_BORN_STANDALONE = 0.2506           # INPUT: P16's standalone weak-freeze-out receipt
YP_NET_SIG = YP_NET * YP_NET_FRAC

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


# ---- 70's Y_He bank ------------------------------------------------------------------------------
YZ = np.load(os.path.join(SP, 'r7801_yhe_response_lcdm.npz'), allow_pickle=True)
YS = np.array(sorted({float(k.split('__')[1]) for k in YZ.files if k.startswith('Dl__')}))
Y0 = YS[len(YS) // 2]


def _key(pref, w):
    return next(k for k in YZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)


YL = YZ[_key('ls', Y0)].astype(float)
YD = np.array([YZ[_key('Dl', w)].astype(float) for w in YS])
YRAT = YD / YD[len(YS) // 2]
_YR = PchipInterpolator(YS, YRAT, axis=0)


def ratio_on_LS(y):
    rb = np.asarray(_YR(float(y)))
    return np.interp(LS, YL, rb, left=rb[0], right=rb[-1])


print("=" * 100)
print("r7806 (60) -- PO-24's Y_He screen and fit: does the helium fraction absorb the displacement?")
print(f"  signature exp[-(r^2-1)(l/l_D)^2], r = {R}, l_D = {LD}")
print("=" * 100)

print("\n  Ⓑ②  THE THREE HELIUM FRACTIONS P16 CARRIES -- DIFFERENT OBJECTS, ENUMERATED")
print(f"    ① the network's own computed value, radiatively corrected : {YP_NET:.4f}"
      f"  +/- {YP_NET_SIG:.5f}  ({YP_NET_FRAC * 100:.1f} %)")
print(f"    ② the observational determination P16 quotes (Aver 2021)   : {YP_OBS:.4f}"
      f"  +/- {YP_OBS_SIG:.4f}  ({YP_OBS_SIG / YP_OBS * 100:.1f} %)")
print(f"    ③ P16's standalone Born-level weak freeze-out             : {YP_BORN_STANDALONE:.4f}")
print(f"    ⌗ the correction is ONE-WAY, not a range: {YP_BORN:.4f} x {YP_CORR_FAC} = "
      f"{YP_BORN * YP_CORR_FAC:.7f}")
print(f"    ⌗ ① and ② disagree by {YP_NET - YP_OBS:+.4f}, which is "
      f"{(YP_NET - YP_OBS) / YP_NET_SIG:+.2f} of ①'s OWN error -- so a disjunction, not a pin")
print(f"    ⌗ ROOM, in fractional terms: Y_He {YP_NET_FRAC * 100:.1f} % against N_eff's 5.7 and "
      f"omega_b's 0.65")
print("      ⇒ the purest envelope direction the instrument has is ALSO the most tightly pinned.")

print(f"\n  Ⓐ①  70's bank: Y_He = {list(YS)}, centre {Y0}")
print(f"    the instrument's own default is _YP = 0.2454 and YHE unset is byte-identical,")
print(f"    so the centre IS the baseline's helium fraction: offset {Y0 - 0.2454:+.4f}")
print(f"    ⌗ but the bank is centred on ② and NOT on ①: {Y0 - YP_NET:+.4f} = "
      f"{(Y0 - YP_NET) / YP_NET_SIG:+.2f} of ①'s error, carried explicitly below")
print(f"    its l grid: {YL[0]:.0f} to {YL[-1]:.0f} step {YL[1] - YL[0]:.0f}, {len(YL)} points")

INV = {}
for nm in ('lA', 'rs', 'DM'):
    INV[nm] = np.array([float(YZ[_key(nm, w)]) for w in YS])
    sp = float(INV[nm].max() - INV[nm].min())
    print(f"    {nm:>4s} across the five: {INV[nm][0]:.6f} .. {INV[nm][-1]:.6f}   spread {sp:.3e}")

REACH = float(YL[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]
print(f"\n    reach = {REACH:.0f}; available windows: {AVAIL}")

d1 = np.diff(YRAT, axis=0)
d2 = np.diff(d1, axis=0)
good = np.abs(d1).max(axis=0) > 0
CURV = float(np.max(np.abs(d2)[:, good].max(axis=0) / np.abs(d1)[:, good].max(axis=0)))
print(f"    worst |second difference| / |first| across the grid: {CURV:.4f}")
for lsel in (500, 996, 1500, 1900):
    j = int(np.argmin(abs(YL - lsel)))
    print(f"        l = {YL[j]:>5.0f} : ratio over the five Y_He = "
          f"[{', '.join(f'{v:.5f}' for v in YRAT[:, j])}]")

# ---- Ⓒ③ THE SCREEN, FIRST, ON r7804's OWN MEASURE -----------------------------------------------
print("\n" + "=" * 100)
print("  Ⓒ③  THE SCREEN, RUN BEFORE THE FIT -- OVERLAP WITH THE RESIDUAL THE TILT LEAVES")
print("=" * 100)
print(f"\n      {'window':>12}{'corr(S,tilt)':>15}{'Y_He vs resid':>16}"
      f"{'Y_He removes':>15}{'tilt removes':>14}")
OVER = []
for lo, hi in AVAIL:
    keep = window(lo, hi)
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v):
        return v - base * float((base @ F @ v) / (base @ F @ base))

    def corr(a, b):
        return float((a @ F @ b) / np.sqrt((a @ F @ a) * (b @ F @ b)))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_yh = perp(CS.bin_spectrum(LS, DL * np.interp(LS, YL, np.asarray(_YR(YS[3]))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))

    def sh(d):
        return float((d_sig @ F @ d) ** 2 / ((d @ F @ d) * (d_sig @ F @ d_sig))) * 100.0
    OVER.append(dict(lbl=f'{lo}-{hi}', c_sig=corr(d_sig, d_yh), rem=sh(d_yh), tilt=sh(d_tl),
                     c_st=corr(d_sig, d_tl), r_yh=corr(d_yh, resid)))
    o = OVER[-1]
    print(f"      {o['lbl']:>12}{o['c_st']:>15.4f}{o['r_yh']:>16.4f}"
          f"{o['rem']:>14.1f}%{o['tilt']:>13.1f}%")
print("      ⌗ against the residual, N_eff scored -0.034, +0.134, +0.180 and omega_b")
print("        -0.343, -0.096, +0.134 (r7804).  Those are the numbers this column is read beside.")

# ---- Ⓓ④ THE FIT, RUN REGARDLESS OF THE SCREEN ---------------------------------------------------


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
        for y0 in (YS[1], Y0, YS[3]):
            o = minimize(at, x0=[dn0, y0], method='L-BFGS-B',
                         bounds=[(-3.0, 3.0), (YS[0], YS[-1])],
                         options={'ftol': 1e-14, 'gtol': 1e-12})
            runs.append((float(o.fun), float(o.x[0]), float(o.x[1])))
    best = min(runs)          # r7802's form: a deterministic argmin, no tie-break epsilon
    spread = tuple(max(x[i] for x in runs) - min(x[i] for x in runs) for i in range(3))
    return best[1], best[2], best[0], spread


print("\n" + "=" * 100)
print("  Ⓓ④ / Ⓔ⑤ / Ⓖ⑦ / Ⓗ⑧ -- THE FIT, RUN REGARDLESS OF THE SCREEN, AS THE ORDER SAYS")
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
    dn3, yh3, c3, sp3 = fit3(tgt, keep, F)
    ROWS.append(dict(lo=lo, hi=hi, n=n, dn2=dn2, dn3=dn3, c2=c2, c3=c3, c_amp=c_amp, yh3=yh3,
                     d1=yh3 - YP_NET, d2=yh3 - YP_OBS, sp3=sp3,
                     surv=abs(dn3) / abs(dn2) * 100.0,
                     a2=(1 - c2 / c_amp) * 100.0, a3=(1 - c3 / c_amp) * 100.0,
                     edge=min(abs(yh3 - YS[0]), abs(yh3 - YS[-1])) < 1e-9))
    r = ROWS[-1]
    print(f"\n      window {lo}-{hi}, {n} bins")
    print(f"        + tilt         : chi^2/bin {c2 / n:>8.4f}  Delta n {dn2:+.5f}"
          f"  absorbed {r['a2']:5.1f} %")
    print(f"        + tilt + Y_He  : chi^2/bin {c3 / n:>8.4f}  Delta n {dn3:+.5f}"
          f"  absorbed {r['a3']:5.1f} %")
    print(f"        Y_He wanted    : {yh3:.5f}"
          + ("   ⛔ AT THE BANK'S EDGE" if r['edge'] else ""))
    print(f"          vs ① {YP_NET:.4f} +/- {YP_NET_SIG:.5f} : {r['d1']:+.5f} = "
          f"{r['d1'] / YP_NET_SIG:+.2f} sigma")
    print(f"          vs ② {YP_OBS:.4f} +/- {YP_OBS_SIG:.4f} : {r['d2']:+.5f} = "
          f"{r['d2'] / YP_OBS_SIG:+.2f} sigma")
    print(f"        SURVIVES       : {r['surv']:.3f} per cent   (multistart spread: "
          f"Delta n {sp3[1]:.1e}, Y_He {sp3[2]:.1e})")

print(f"\n      survival across the windows: "
      f"{', '.join('%.3f' % r['surv'] for r in ROWS)} per cent")
print(f"      absorbed-share GAIN from freeing Y_He: "
      f"{', '.join('%+.2f' % (r['a3'] - r['a2']) for r in ROWS)} points")

# ---- Ⓕ⑥ THE SCREEN AGAINST THE FIT --------------------------------------------------------------
print("\n" + "=" * 100
      + "\n  Ⓕ⑥  DOES THE SCREEN PREDICT WHAT THE FIT MEASURES?\n" + "=" * 100)
print(f"\n      {'window':>12}{'screen: removes':>18}{'fit: gain':>14}{'difference':>14}")
for o, r in zip(OVER, ROWS):
    print(f"      {o['lbl']:>12}{o['rem']:>17.2f}%{r['a3'] - r['a2']:>13.2f}%"
          f"{o['rem'] - (r['a3'] - r['a2']):>13.2f}%")

np.savez(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'runs', 'r7806_probe.npz'),
         ys=YS, yrat=YRAT, surv=np.array([r['surv'] for r in ROWS]),
         yh3=np.array([r['yh3'] for r in ROWS]),
         a2=np.array([r['a2'] for r in ROWS]), a3=np.array([r['a3'] for r in ROWS]),
         r_yh=np.array([o['r_yh'] for o in OVER]), rem=np.array([o['rem'] for o in OVER]),
         c_st=np.array([o['c_st'] for o in OVER]))
print("\n  ⌗ probe written to runs/r7806_probe.npz")
