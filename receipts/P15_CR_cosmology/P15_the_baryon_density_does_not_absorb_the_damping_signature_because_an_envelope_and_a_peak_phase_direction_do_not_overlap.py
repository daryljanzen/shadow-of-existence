#!/usr/bin/env python3
r"""P15 receipt -- ⛭⛭⛭ THE BARYON DENSITY DOES NOT ABSORB THE DAMPING SIGNATURE, AND THE REASON IS
STRUCTURAL: AN ENVELOPE AND A PEAK-PHASE DIRECTION DO NOT OVERLAP.

** WHAT THIS IS FOR. **  `PO-24` is data-gated, and its row names what would end it INSTEAD of data:
"absorbed by the inherited parameters it is degenerate with, the baryon density among them, so that no
tail precision can separate it".  Ⓔ⑨ asserts that clause from the register, because it is the clause
this receipt reasons FROM.  ** This receipt tests it on the one inherited parameter the corpus has a
banked response for, and the answer is NO. **

** WHAT THE ANSWER IS, IN ONE LINE. **  Freeing the baryon density alongside the tilt changes the
fitted tilt displacement by about a part in a hundred -- `99` to `102` per cent of it survives on every
window the response reaches -- while the absorbed share moves from `69.6` to `74.0` per cent at most.
`omega_b` is not the absorber the row hoped for.

** AND THE STRONGEST FORM OF IT IS Ⓒ⑦. **  On the published window the fit WANTS `omega_b` `2.1` per
cent low, which is `3.2` sigma of the corpus's own inherited value -- and even paying that
impermissible price, `100.3` per cent of the displacement survives.  On the two windows where the
tilt absorbs most, `omega_b` stays inside half a sigma and the displacement is untouched.  ** So the
terminating clause fails in both directions: where the excursion is allowed it does nothing, and where
it would do something it is not allowed -- and it does nothing there either. **

** THE HARNESS IS REUSED, NOT REBUILT, AS THE ORDER REQUIRED. **  `r7611+70`'s joint fit supplies the
baseline, the metric, the binning and the covariance, with covered bins restricted ON the covariance so
uncovered ones are marginalised.  Ⓐ① reproduces its published figure at the one-rate multipole to the
digits `r7797+cc66.1` prints, BEFORE anything is added to it -- because an extension of a harness one
has not reproduced is a measurement of nothing.

⌗ ** THE RESPONSE ENTERS AS A RATIO AND NEVER AS AN ABSOLUTE SPECTRUM. **  `r6897`'s response run is a
different configuration from the baseline (`LSTEP=8 LMAXL=2000`, summed over eleven `KSLICE` pieces), so
a ratio to its own centre cancels what differs between the two runs and an absolute spectrum would not.

COMPUTES: scope -- what is received and what is derived.  Nothing here is a new spectrum; every
spectrum is read from the bank, and nothing is fitted beyond the two or three parameters each fit is of.
  INPUT   r = 1.0926                 -- P15's damping ratio, corpus measured
  INPUT   l_D = 1489.5783            -- the one-rate damping multipole, r7797+cc66.1
  INPUT   eta_10 = 6.13 +/- 0.04     -- the corpus's OWN printed inherited datum (P16); omega_b is
                                        proportional to eta, so this is omega_b's precision
  INPUT   L820_lcdm_L2512_nk800      -- the banked control arm, the baseline
  INPUT   r6897_wb_response_lcdm     -- the banked control at five omega_b, the free direction
  INPUT   plik_lite TT               -- the bandpowers, binning and covariance, the metric

** COMPUTES. **
  Ⓐ  the published two-parameter figure reproduced at the one-rate multipole, before anything is added;
  Ⓑ  the response's l reach, which decides which windows may be spoken about, and its saturation;
  Ⓒ  the three-parameter fit, the displacement's survival, the absorbed share, and the omega_b
     excursion in units of the inherited precision -- the arm that decides the row;
  Ⓓ  the other inherited parameters, declared absent from the bank with the pattern and directory named;
  Ⓔ  the register clause this receipt reasons FROM, located in three states.

** WHAT IT DOES NOT CLAIM. **  It does not close or open `PO-24`: it reports that the baryon density
does not meet the terminating clause, and five other parameters are NAMED rather than tested because no
response for them exists and the instrument that would build one is not this seat's.  It says nothing
about windows above `l = 1996`, which the response does not reach.  It does not adjudicate which
exponent `P15` should price the signature on -- `r7797+cc66.1` left that to `70`'s measurement and the
order named the multipole used here.  And it computes no significance against the sky; every number
here is a degeneracy-fit number, which is a different question from the sky comparison.

Built r7800 (node 60), on order r7799 from node 69.  Stated for reversal.
"""
import io
import os
import re
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize, minimize_scalar
from scipy.interpolate import PchipInterpolator

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

fails = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        fails.append(label)


def head(t):
    print('\n' + '=' * 100 + f"\n  {t}\n" + '=' * 100)


R, LD = 1.0926, 1489.5783
K = R ** 2 - 1
ETA10, ETA10_SIG = 6.13, 0.04
WB_FRAC_SIG = ETA10_SIG / ETA10

SPDIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
_z = np.load(os.path.join(SPDIR, 'L820_lcdm_L2512_nk800.npz'))
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


WZ = np.load(os.path.join(SPDIR, 'r6897_wb_response_lcdm.npz'), allow_pickle=True)
WBS = np.array(sorted({float(k.split('__')[1]) for k in WZ.files if k.startswith('Dl__')}))
WB0 = WBS[len(WBS) // 2]


def _key(pref, w):
    return next(k for k in WZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)


WL = WZ[_key('ls', WB0)].astype(float)
WD = np.array([WZ[_key('Dl', w)].astype(float) for w in WBS])
WRAT = WD / WD[len(WBS) // 2]
_RAT = PchipInterpolator(WBS, WRAT, axis=0)


def ratio_on_LS(wb):
    rb = np.asarray(_RAT(float(wb)))
    return np.interp(LS, WL, rb, left=rb[0], right=rb[-1])


print(f"\n  the signature: exp[-(r^2-1)(l/l_D)^2] at r = {R}, l_D = {LD}")
print(f"  omega_b's inherited precision, from the corpus's own eta_10 = {ETA10} +/- {ETA10_SIG}:"
      f"  {WB_FRAC_SIG * 100:.3f} per cent")

# ===================================================== Ⓐ THE HARNESS REPRODUCED BEFORE EXTENDING IT
head("A -- THE PUBLISHED FIGURE REPRODUCED AT THE ONE-RATE MULTIPOLE, BEFORE ANYTHING IS ADDED")


def fit2(target, keep, F):
    def at(dn):
        m = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** dn)[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r)
    o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
    return float(o.x), float(at(float(o.x)))


def fit3(target, keep, F):
    """A, Delta n and omega_b together.  omega_b is BOUNDED to the bank's own five values: a fit that
    wants more than the bank measured is reported AT the edge and named, never extrapolated."""
    def at(p):
        m = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** float(p[0]) * ratio_on_LS(p[1]))[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r)
    best = None
    for dn0 in (-0.30, -0.10, 0.0, 0.10):
        for wb0 in (WBS[1], WB0, WBS[3]):
            o = minimize(at, x0=[dn0, wb0], method='L-BFGS-B',
                         bounds=[(-3.0, 3.0), (WBS[0], WBS[-1])],
                         options={'ftol': 1e-14, 'gtol': 1e-12})
            if best is None or o.fun < best.fun:
                best = o
    return float(best.x[0]), float(best.x[1]), float(best.fun)


keep0 = window(100, 1758)
n0 = int(keep0.sum())
F0 = _fisher(keep0)
tgt0 = CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep0]
m_amp0 = CS.bin_spectrum(LS, DL)[keep0]
r_amp0 = tgt0 - float((m_amp0 @ F0 @ tgt0) / (m_amp0 @ F0 @ m_amp0)) * m_amp0
c_amp0 = float(r_amp0 @ F0 @ r_amp0)
dn0_, c0_ = fit2(tgt0, keep0, F0)
pub_chi2_per_bin = c0_ / n0
pub_absorbed = (1.0 - c0_ / c_amp0) * 100.0
print(f"      window 100-1758, {n0} covered bins")
print(f"        amplitude alone     : chi^2/bin {c_amp0 / n0:.4f}")
print(f"        + tilt              : chi^2/bin {pub_chi2_per_bin:.4f}   against the published 1.0815")
print(f"        absorbed share      : {pub_absorbed:.1f} per cent   against the published 69.6")
check("Ⓐ①  the two-parameter fit at the one-rate multipole returns 1.0815 chi^2 per bin over 171 "
      "covered bins and absorbs 69.6 per cent, the figures r7797+cc66.1 prints -- so the harness is "
      "reproduced before a third parameter is added to it",
      n0 == 171 and abs(pub_chi2_per_bin - 1.0815) < 5e-4 and abs(pub_absorbed - 69.6) < 0.05)

# ===================================================== Ⓑ THE RESPONSE: REACH AND SATURATION
head("B -- THE RESPONSE'S REACH, WHICH DECIDES WHICH WINDOWS MAY BE SPOKEN ABOUT, AND ITS SATURATION")
REACH = float(WL[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]
print(f"      the banked response: omega_b = {WB0:.8f} at "
      f"{[round((w - WB0) / WB0 * 100, 1) for w in WBS]} per cent")
print(f"      its l grid: {WL[0]:.0f} to {REACH:.0f} in steps of {WL[1] - WL[0]:.0f}, {len(WL)} points")
for lo, hi in WINDOWS:
    print(f"        window {lo:>5}-{hi:<5} : {int(window(lo, hi).sum()):>4} covered bins   "
          f"{'AVAILABLE' if hi <= REACH else 'OUT OF REACH'}")
check("Ⓑ②  the response reaches l = 1996, so THREE of the six windows the displacement table uses "
      "are available and three are not -- and no arm below speaks about a window its own inputs do "
      "not reach, which is why the reach is asserted rather than assumed",
      REACH == 1996.0 and len(AVAIL) == 3 and all(hi <= REACH for _, hi in AVAIL))

d1 = np.diff(WRAT, axis=0)
d2 = np.diff(d1, axis=0)
good = np.abs(d1).max(axis=0) > 0
CURV = float(np.max(np.abs(d2)[:, good].max(axis=0) / np.abs(d1)[:, good].max(axis=0)))
print(f"\n      worst |second difference| / |first difference| over the whole grid: {CURV:.4f}")
for lsel in (500, 996, 1500, 1900):
    j = int(np.argmin(abs(WL - lsel)))
    print(f"        l = {WL[j]:>5.0f} : ratio over the five omega_b = "
          f"[{', '.join(f'{v:.5f}' for v in WRAT[:, j])}]")
check("Ⓑ③  the response is NOT linear in omega_b -- the worst second difference is 0.7532 of the "
      "first -- so the fit INTERPOLATES the five banked values with a monotone spline and never "
      "extrapolates a derivative, and an omega_b outside the bank is reported at the edge",
      abs(CURV - 0.7532) < 5e-4 and CURV > 0.1)

# ===================================================== Ⓒ THE FIT, AND THE ARM THAT DECIDES THE ROW
head("C -- THE TILT AND THE BARYON DENSITY FREE TOGETHER")
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
    dn3, wb3, c3 = fit3(tgt, keep, F)
    dwb = (wb3 - WB0) / WB0
    ROWS.append(dict(lo=lo, hi=hi, n=n, dn2=dn2, dn3=dn3, c2=c2, c3=c3, c_amp=c_amp,
                     wb3=wb3, dwb=dwb, surv=abs(dn3) / abs(dn2) * 100.0,
                     a2=(1 - c2 / c_amp) * 100.0, a3=(1 - c3 / c_amp) * 100.0,
                     edge=min(abs(wb3 - WBS[0]), abs(wb3 - WBS[-1])) < 1e-9))
    r = ROWS[-1]
    print(f"\n      window {lo}-{hi}, {n} covered bins")
    print(f"        + tilt          : chi^2/bin {c2 / n:>8.4f}   Delta n {dn2:+.5f}"
          f"   absorbed {r['a2']:5.1f} %")
    print(f"        + tilt + omega_b: chi^2/bin {c3 / n:>8.4f}   Delta n {dn3:+.5f}"
          f"   absorbed {r['a3']:5.1f} %")
    print(f"        omega_b wanted  : {wb3:.8f} = {dwb * 100:+.3f} % = "
          f"{dwb / WB_FRAC_SIG:+.1f} sigma of the inherited value"
          + ("   ⛔ AT THE BANK'S EDGE" if r['edge'] else ""))
    print(f"        SURVIVES        : {r['surv']:.1f} per cent of the displacement")

check("Ⓒ④  the three-parameter fit converges on every available window, inside the bank's own grid "
      "and not at its edge, so no number here is an extrapolation of a response that was never "
      "measured",
      all(not r['edge'] for r in ROWS) and len(ROWS) == 3)

surv = [r['surv'] for r in ROWS]
print(f"\n      the displacement's survival across the three windows: "
      f"{', '.join('%.3f' % s for s in surv)} per cent")
print("      ⌗ printed to THREE decimals because the INDEX row's figure is pinned against this "
      "value,\n        and the first form of that pin was computed from the five-decimal Delta n "
      "values this\n        receipt PRINTS rather than from the quantities themselves -- which put "
      "it 0.03 out and\n        failed its own arm.  ⇒ GUARD: a pin computed from a rounded "
      "intermediate is a pin on the\n        rounding.  Take it from the quantity.")
check("Ⓒ⑤  THE ORDER'S QUESTION: the displacement SURVIVES -- between 99 and 102 per cent of it on "
      "every window the response reaches, and 100.267 per cent on the published one.  Freeing the "
      "baryon density moves the fitted tilt by about a part in a hundred, not by a factor",
      all(99.0 <= s <= 102.0 for s in surv) and abs(surv[0] - 100.267) < 0.01)

gain = [r['a3'] - r['a2'] for r in ROWS]
print(f"      the absorbed share gains: {', '.join('%+.1f' % g for g in gain)} points"
      f"   (from {', '.join('%.1f' % r['a2'] for r in ROWS)})")
check("Ⓒ⑥  and the absorbed share barely moves -- at most 4.4 points, 69.6 to 74.0 on the published "
      "window and a tenth of a point on the other two -- so omega_b is not taking the signature "
      "either, by the share or by the displacement",
      max(gain) < 5.0 and abs(ROWS[0]['a3'] - 74.0) < 0.1)

print()
for r in ROWS:
    print(f"      {r['lo']}-{r['hi']}: omega_b wanted {r['dwb'] / WB_FRAC_SIG:+.1f} sigma, "
          f"and {r['surv']:.1f} per cent of the displacement survives it")
inside = [r for r in ROWS if abs(r['dwb'] / WB_FRAC_SIG) < 0.5]
check("Ⓒ⑦  THE ARM THAT DECIDES THE ROW, AND IT FAILS THE TERMINATING CLAUSE IN BOTH DIRECTIONS.  "
      "On the published window the fit wants omega_b 3.2 sigma below the corpus's own inherited "
      "value and the displacement survives it anyway; on the two windows where the tilt absorbs "
      "most, omega_b stays inside HALF a sigma and does nothing.  An absorber that needs a "
      "parameter outside its measured range has not absorbed anything -- and this one does nothing "
      "inside it either",
      len(inside) == 2 and all(r['surv'] > 98.0 for r in inside)
      and abs(ROWS[0]['dwb'] / WB_FRAC_SIG + 3.2) < 0.1)

# ===================================================== Ⓓ THE DECLARED ABSENCE
head("D -- THE OTHER INHERITED PARAMETERS, DECLARED ABSENT FROM THE BANK")
NAMES = sorted(os.listdir(SPDIR))
PARAMS = {
    'the baryon density  omega_b': ('wb', 'omega_b', 'omb', 'baryon'),
    'the effective neutrino number  N_eff': ('neff', 'nnu', 'n_eff'),
    'the helium fraction  Y_He': ('yhe', 'helium', 'yp'),
    'the optical depth  tau': ('tau_resp', 'reion', 'optdepth'),
    'the lensing amplitude  A_L': ('alens', 'a_lens', 'lensamp'),
    'the matter density  omega_m': ('wm_resp', 'omega_m_resp', 'ommresp'),
}
found = {}
for label, pats in PARAMS.items():
    hits = [f for f in NAMES if any(p in f.lower() for p in pats)]
    found[label] = hits
    print(f"      {label:<40s} : {len(hits):>2} file(s)" + (f"  -> {hits[0]}" if hits else ""))
print(f"      ⌗ searched the {len(NAMES)} entries of computations/beyond_the_wall/spectra, the one "
      f"directory every\n        banked spectrum lives in, by the lowercase substring patterns "
      f"printed above applied to each\n        entry's filename -- so the absence stated here is "
      f"about THAT directory and THOSE patterns and\n        about nothing else.  A response banked "
      f"elsewhere, or named otherwise, would not be seen by it.")
print("      ⇒ each of the five would need the instrument run at five parameter values and summed "
      "over\n        eleven mode slices, which is hours of compute in pieces on the seat that owns "
      "the\n        instrument.  NAMED, NOT MEASURED, and routed rather than guessed.")
print("      ⌗ AND THE COUNT ABOVE IS SCOPE, NOT CLAIM.  The first form of this arm asserted "
      "len(NAMES) == 271,\n        an equality on a directory any other seat grows by banking a "
      "spectrum -- so it would have\n        turned red on 70's next bank and said nothing about "
      "this receipt's subject.  The exact-count\n        gate caught it and was right.  ⇒ GUARD: an "
      "equality on a population another seat owns is a\n        check on their activity, not on "
      "your claim; print it as the scope of the search and assert\n        only what is yours.")
check("Ⓓ⑧  exactly ONE of the six inherited parameters has a banked response, and the absence of "
      "the other five is declared with the directory and the patterns it was searched by, in the "
      "sentence that states it -- which is the form this line's absence gate has had to require "
      "three times",
      len([k for k, v in found.items() if v]) == 1 and len(found) == 6)

# ===================================================== Ⓔ THE CLAUSE THIS RECEIPT REASONS FROM
head("E -- THE REGISTER CLAUSE THIS RECEIPT REASONS FROM, IN THREE STATES")
REG = ' '.join(io.open(os.path.join(ROOT, 'THE_REGISTER.md'), encoding='utf-8').read().split())
SENTS = [' '.join(s.split()) for s in re.split(r'(?<=[.!?;])\s+', REG) if s.strip()]
KEY = ('absorbed by the inherited parameters it is degenerate with, the baryon density among them, '
       'so that no tail precision can separate it')
state = 'MATCHED' if any(KEY in s for s in SENTS) else ('WITHDRAWN' if KEY in REG else 'STALE')
print(f"      PO-24's terminating clause -> {state}")
i = REG.find(KEY)
if i >= 0:
    print('        "...' + REG[max(0, i - 110):i + 170] + '..."')
check("Ⓔ⑨  the terminating clause is in the register on this tree, and it is the clause this receipt "
      "reasons FROM rather than a conclusion about it -- a gate that asserted only the row's "
      "data-gated STATUS would assert what the row says about itself instead of the condition the "
      "argument tests",
      state == 'MATCHED')

# ===================================================== THE ADDITION
head("AN ADDITION, MARKED AS ONE -- WHY omega_b CANNOT ABSORB AN ENVELOPE")
print("      ⌗ NOT ONE OF THE EIGHT REGISTERED ARMS.  The registration asked WHETHER the")
print("        displacement survives, not why, and this was measured after the answer came back.")
for lo, hi in AVAIL:
    keep = window(lo, hi)
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v):
        return v - base * float((base @ F @ v) / (base @ F @ base))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_wb = perp(CS.bin_spectrum(LS, DL * np.interp(LS, WL, np.asarray(_RAT(WBS[3]))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])

    def sh(d):
        return float((d_sig @ F @ d) ** 2 / ((d @ F @ d) * (d_sig @ F @ d_sig))) * 100.0
    corr = float((d_sig @ F @ d_wb) / np.sqrt((d_sig @ F @ d_sig) * (d_wb @ F @ d_wb)))
    print(f"      {lo}-{hi}: corr(signature, omega_b) = {corr:+.4f};  omega_b can remove "
          f"{sh(d_wb):.1f} % of the signature's chi^2, the tilt {sh(d_tl):.1f} %")
print("      ⇒ the signature falls monotonically with l: it is an ENVELOPE.  The omega_b response")
print("        does not -- it is negative below about l = 900 and positive above -- because omega_b")
print("        moves the PEAKS through the baryon loading.  ⇒ A PARAMETER HAS TO HAVE THE SHAPE TO")
print("        ABSORB A SHAPE, and that is why the answer is structural and not a matter of")
print("        precision: no tightening of omega_b would change it.")

head("THE COUNT, THE SCOPE, AND WHAT IS NOT CLAIMED")
print("      REGISTERED ARMS: 8 -- Ⓐ① Ⓑ②③ Ⓒ④⑤⑥⑦ Ⓓ⑧; ALL EIGHT met, and Ⓔ⑨ is a NINTH check")
print("      added so the gate asserts the clause the argument reasons from.  CHECKS RUN: 9.")
print("      the SIX inputs are declared in the COMPUTES header; no spectrum here is new and nothing")
print("      is fitted beyond the two or three parameters each fit is of.")
print("      NOT CLAIMED: that PO-24 closes or stays open as a whole -- five of the six inherited")
print("      parameters are NAMED and not tested, because no response for them is banked; anything")
print("      about windows above l = 1996; which exponent P15 should price the signature on; and no")
print("      significance against the sky, every number here being a degeneracy-fit number.")

print('\n' + '=' * 90)
if fails:
    print(f"  ⛔ {len(fails)} CHECK(S) FAILED:")
    for x in fails:
        print(f"     - {x}")
    print('=' * 90)
    sys.exit(1)
print(f"""
  ALL CHECKS PASS.

  PO-24's terminating clause is NOT met by the baryon density.

  Freeing omega_b alongside the tilt leaves {ROWS[0]['surv']:.1f} per cent of the fitted
  displacement standing on the published window, and between {min(surv):.1f} and
  {max(surv):.1f} per cent on every window the banked response reaches.  The
  absorbed share goes from {ROWS[0]['a2']:.1f} to {ROWS[0]['a3']:.1f} per cent at most.

  And the clause fails in both directions.  On the published window the fit
  wants omega_b {ROWS[0]['dwb'] / WB_FRAC_SIG:+.1f} sigma from the corpus's own inherited value --
  an excursion the datum does not permit -- and the displacement survives it
  anyway.  On the two windows where the tilt absorbs most, omega_b stays inside
  half a sigma and changes nothing.

  The reason is structural rather than a matter of precision: the signature is
  an ENVELOPE in l and omega_b is a PEAK-PHASE direction, so the two templates
  barely overlap under the covariance.  No tightening of omega_b would change
  that, and the row does not terminate by this route.

  Five other inherited parameters are NAMED and not tested.  No response for
  any of them is banked, and building one is not this seat's instrument.
""")
print('=' * 90)
