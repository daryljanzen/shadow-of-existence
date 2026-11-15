#!/usr/bin/env python3
r"""r7800 (60) -- PO-24's terminating test, on order r7799 (69).

Reuses r7611+70's joint-fit harness (baseline, metric, binning, covariance) and adds ONE free
direction: the baryon density, from r6897's banked five-point response.  The response enters as a
RATIO and never as an absolute spectrum, because the response run is a different configuration from
the baseline (LSTEP=8 LMAXL=2000, summed over eleven KSLICE pieces) and a ratio cancels what differs.
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

R, LD = 1.0926, 1489.5783          # INPUT: the damping ratio, and r7797+cc66.1's one-rate multipole
K = R ** 2 - 1
ETA10, ETA10_SIG = 6.13, 0.04      # INPUT: the corpus's own printed inherited datum (P16)
WB_FRAC_SIG = ETA10_SIG / ETA10    # omega_b is proportional to eta, so this is its precision

print("=" * 100)
print("r7800 (60) -- PO-24's terminating test: is the tilt displacement absorbed by omega_b?")
print(f"  signature exp[-(r^2-1)(l/l_D)^2] with r = {R}, l_D = {LD}  (the one-rate multipole)")
print(f"  omega_b's inherited precision, from the corpus's own eta_10 = {ETA10} +/- {ETA10_SIG}:"
      f"  {WB_FRAC_SIG * 100:.3f} %")
print("=" * 100)

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
A_UNITS = float((_m0 @ _F0 @ CS.X_DATA[_k0]) / (_m0 @ _F0 @ _m0))
DL = RAW * A_UNITS


def sig(l):
    return np.exp(-K * (np.asarray(l, float) / LD) ** 2)


def window(lo=None, hi=None):
    keep = np.isfinite(CS.bin_spectrum(LS, DL))
    if lo is not None:
        keep &= (CS.BIN_LO >= lo)
    if hi is not None:
        keep &= (CS.BIN_HI <= hi)
    return keep


# ----------------------------------------------------------------- the omega_b response, as a RATIO
WZ = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra',
                          'r6897_wb_response_lcdm.npz'), allow_pickle=True)
WBS = np.array(sorted({float(k.split('__')[1]) for k in WZ.files if k.startswith('Dl__')}))
WB0 = WBS[len(WBS) // 2]


def _key(pref, w):
    for k in WZ.files:
        if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-12:
            return k
    raise KeyError(w)


WL = WZ[_key('ls', WB0)].astype(float)
WD = np.array([WZ[_key('Dl', w)].astype(float) for w in WBS])
WRAT = WD / WD[len(WBS) // 2]                     # ratio to the centre, per omega_b, on the bank grid
_RAT_OF_WB = PchipInterpolator(WBS, WRAT, axis=0)  # smooth in omega_b; the response SATURATES


def ratio_on_LS(wb):
    """the response ratio at omega_b, interpolated in omega_b and then onto the baseline's grid.
    Outside the bank's l reach the ratio is held at its endpoint value -- which is why every window
    used below ends inside the reach, and why Ⓑ② asserts the reach rather than trusting this."""
    r_bank = np.asarray(_RAT_OF_WB(float(wb)))
    return np.interp(LS, WL, r_bank, left=r_bank[0], right=r_bank[-1])


print(f"\n  the banked response: omega_b = {WB0:.8f} at "
      f"{[round((w - WB0) / WB0 * 100, 1) for w in WBS]} per cent")
print(f"  its l grid: {WL[0]:.0f} to {WL[-1]:.0f} in steps of {WL[1] - WL[0]:.0f}, {len(WL)} points")

# ======================================================================== Ⓑ② THE REACH
print("\n" + "=" * 100)
print("  B2 -- THE RESPONSE'S REACH, AND WHICH WINDOWS IT LEAVES AVAILABLE")
print("=" * 100)
REACH = float(WL[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
for lo, hi in WINDOWS:
    ok = hi <= REACH
    n = int(window(lo, hi).sum())
    print(f"      window {lo:>5}-{hi:<5} : {n:>4} covered bins   "
          f"{'AVAILABLE' if ok else 'OUT OF REACH (hi > %.0f)' % REACH}")
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]
print(f"      ⇒ the reach is l = {REACH:.0f}, so {len(AVAIL)} of {len(WINDOWS)} windows are available")

# ======================================================================== Ⓑ③ SATURATION
print("\n" + "=" * 100)
print("  B3 -- IS THE RESPONSE LINEAR IN omega_b, OR DOES IT SATURATE?")
print("=" * 100)
mid = len(WBS) // 2
for lsel in (500, 1000, 1500, 1900):
    j = int(np.argmin(abs(WL - lsel)))
    col = WRAT[:, j]
    d1 = np.diff(col)
    d2 = np.diff(d1)
    print(f"      l = {WL[j]:>5.0f} :  ratio over the five omega_b = "
          f"[{', '.join(f'{v:.5f}' for v in col)}]")
    print(f"                  first differences  {['%+.2e' % v for v in d1]}")
    print(f"                  |second| / |first| = "
          f"{', '.join('%.3f' % abs(d2[i] / d1[i]) for i in range(len(d2)))}")
CURV = float(np.max([abs(np.diff(np.diff(WRAT[:, j]))).max() / abs(np.diff(WRAT[:, j])).max()
                     for j in range(len(WL)) if abs(np.diff(WRAT[:, j])).max() > 0]))
print(f"      ⇒ worst |second difference| / |first difference| over the whole grid: {CURV:.4f}")
print("      ⇒ the response is NOT linear in omega_b, so the fit interpolates the five values")
print("        (monotone PCHIP) rather than extrapolating a derivative.")

# ======================================================================== Ⓐ① and Ⓒ THE FITS
def fit2(target, keep, F):
    """A and Delta n, as r7611's harness does it"""
    def at(dn):
        m = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** dn)[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r), A
    o = minimize_scalar(lambda d: at(d)[0], bounds=(-3.0, 3.0), method='bounded',
                        options={'xatol': 1e-10})
    c, A = at(float(o.x))
    return float(o.x), c, A


def fit3(target, keep, F):
    """A, Delta n and omega_b together.  omega_b is BOUNDED to the bank's own grid: a fit that
    wants more than the bank measured is reported at the edge and named, never extrapolated."""
    def at(p):
        dn, wb = float(p[0]), float(p[1])
        m = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** dn * ratio_on_LS(wb))[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r), A
    best = None
    for dn0 in (-0.30, -0.10, 0.0, 0.10):
        for wb0 in (WBS[1], WB0, WBS[3]):
            o = minimize(lambda p: at(p)[0], x0=[dn0, wb0], method='L-BFGS-B',
                         bounds=[(-3.0, 3.0), (WBS[0], WBS[-1])],
                         options={'ftol': 1e-14, 'gtol': 1e-12})
            if best is None or o.fun < best.fun:
                best = o
    c, A = at(best.x)
    return float(best.x[0]), float(best.x[1]), c, A


print("\n" + "=" * 100)
print("  A1 and C -- THE FITS")
print("=" * 100)
ROWS = []
for lo, hi in AVAIL:
    keep = window(lo, hi)
    n = int(keep.sum())
    F = _fisher(keep)
    tgt = CS.bin_spectrum(LS, DL * sig(LS))[keep]
    c_amp = None
    m_amp = CS.bin_spectrum(LS, DL)[keep]
    A_amp = float((m_amp @ F @ tgt) / (m_amp @ F @ m_amp))
    r_amp = tgt - A_amp * m_amp
    c_amp = float(r_amp @ F @ r_amp)
    dn2, c2, _ = fit2(tgt, keep, F)
    dn3, wb3, c3, _ = fit3(tgt, keep, F)
    abs2 = 1.0 - c2 / c_amp
    abs3 = 1.0 - c3 / c_amp
    dwb = (wb3 - WB0) / WB0
    ROWS.append(dict(lo=lo, hi=hi, n=n, c_amp=c_amp, dn2=dn2, c2=c2, dn3=dn3, wb3=wb3,
                     c3=c3, abs2=abs2, abs3=abs3, dwb=dwb))
    print(f"\n      window {lo}-{hi}, {n} covered bins")
    print(f"        amplitude alone        : chi^2/bin {c_amp / n:>9.4f}")
    print(f"        + tilt   (2 params)    : chi^2/bin {c2 / n:>9.4f}   Delta n = {dn2:+.5f}"
          f"   absorbed {abs2 * 100:5.1f} %")
    print(f"        + tilt + omega_b (3)   : chi^2/bin {c3 / n:>9.4f}   Delta n = {dn3:+.5f}"
          f"   absorbed {abs3 * 100:5.1f} %")
    print(f"        the omega_b it wants   : {wb3:.8f}  =  {dwb * 100:+.3f} %  "
          f"=  {dwb / WB_FRAC_SIG:+.1f} sigma of the inherited value"
          + ("   ⛔ AT THE BANK'S EDGE" if min(abs(wb3 - WBS[0]), abs(wb3 - WBS[-1])) < 1e-9 else ""))
    print(f"        the tilt's survival    : |Delta n(3)| / |Delta n(2)| = "
          f"{abs(dn3) / abs(dn2) * 100:5.1f} %")

# ======================================================================== Ⓓ⑧ THE ABSENCE
print("\n" + "=" * 100)
print("  D8 -- THE OTHER INHERITED PARAMETERS, AND WHAT THE BANK HOLDS FOR THEM")
print("=" * 100)
SPDIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
NAMES = sorted(os.listdir(SPDIR))
PARAMS = {
    'the baryon density  omega_b': ('wb', 'omega_b', 'omb', 'baryon'),
    'the effective neutrino number  N_eff': ('neff', 'nnu', 'n_eff'),
    'the helium fraction  Y_He': ('yhe', 'helium', 'yp'),
    'the optical depth  tau': ('tau_resp', 'reion', 'optdepth'),
    'the lensing amplitude  A_L': ('alens', 'a_lens', 'lensamp'),
    'the matter density  omega_m': ('wm_resp', 'omega_m_resp', 'ommresp'),
}
for label, pats in PARAMS.items():
    hits = [f for f in NAMES if any(p in f.lower() for p in pats)]
    print(f"      {label:<40s} : {len(hits):>2} file(s) matching "
          f"{list(pats)}" + (f"  -> {hits}" if hits else ""))
print(f"      ⌗ searched {len(NAMES)} entries of the one directory every banked spectrum lives in,")
print(f"        {SPDIR.replace(ROOT + os.sep, '')}, by the lowercase substring patterns printed above")
print("        on each entry's filename -- so the absence below is a statement about that directory")
print("        and those patterns, and about nothing else.")
print("      ⇒ ONE of the six has a response bank.  The other five would each need a run of the")
print("        instrument at five parameter values summed over eleven mode slices, which is hours")
print("        of compute in pieces on the seat that owns the instrument.  NAMED, NOT MEASURED.")

print("\n" + "=" * 100)
print("  THE ANSWER TO THE ORDER")
print("=" * 100)
for r in ROWS:
    print(f"      {r['lo']}-{r['hi']}: Delta n {r['dn2']:+.5f} -> {r['dn3']:+.5f}"
          f"  ({abs(r['dn3']) / abs(r['dn2']) * 100:.1f} % survives)"
          f"   at omega_b {r['dwb'] * 100:+.2f} % = {r['dwb'] / WB_FRAC_SIG:+.1f} sigma")
