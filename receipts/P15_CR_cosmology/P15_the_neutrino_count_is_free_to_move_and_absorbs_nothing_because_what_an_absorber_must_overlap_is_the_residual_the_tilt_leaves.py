#!/usr/bin/env python3
r"""P15 receipt -- ⛭⛭⛭ THE NEUTRINO COUNT IS FREE TO MOVE AND ABSORBS NOTHING, AND THE TEST THAT
EXPLAINS IT IS OVERLAP WITH THE RESIDUAL THE TILT LEAVES.

** WHAT THIS IS FOR. **  `r7800` found the baryon density is not `PO-24`'s absorber, partly because
the excursion the fit wanted was `3.2` sigma of an inherited datum -- an excursion the datum does not
permit.  `N_eff` was the named next candidate and `70` banked its response, reporting it as "a
monotone tilt across the damping tail, the shape that could absorb an envelope".  ** This receipt runs
that fit, and the answer is a stronger negative than the baryon density's: the excursion IS permitted
-- under a third of the constraint the corpus quotes -- and the displacement still survives entirely.

** SO THE FAILURE IS NOT ABOUT ROOM. **  For `omega_b` one could say the absorber was unaffordable.
Here it is affordable and buys nothing: `100.27` to `100.71` per cent of the displacement survives and
the absorbed share gains at most a quarter of a point.  ** A parameter free to move that changes
nothing is a cleaner refutation of the terminating clause than one forbidden to move. **

** AND `70`'s SHAPE ARGUMENT INVERTS, FOR A REASON THAT GENERALISES. **  `Ⓒ⑦ᵇ` measures what an
absorber must actually overlap.  Not the signature: the signature is almost exactly a tilt
(`|corr| > 0.84`), so the ALREADY-FREE tilt takes `70` to `97` per cent of it.  What is left is the
part no power law removes, and ** that is what a candidate must overlap. **  Against it `N_eff` scores
`-0.03`, `+0.13`, `+0.18` and `omega_b` scores `-0.34`, `-0.10`, `+0.13`: both nearly orthogonal to
the one thing they would have to touch.  ⇒ * The search for an absorber reduces to one cheap
projection, applied before any fit is run. *

** ⛔ AND ONE PREMISE OF THE ORDER IS CORRECTED HERE. **  `r7803` asked for the excursion to be judged
"against the corpus's own inherited value and precision", on the ground that `P16` fixes `N_eff`
through the nucleosynthesis network.  `P16` says the opposite: `N_eff = 3.046` is "adopted here rather
than derived", and "this framework therefore makes no `N_eff` prediction".  There is no corpus-derived
value and no corpus-derived error.  What the corpus supplies is the constraint it quotes itself,
`2.99 +/- 0.17`, "the number a departure would have to move" -- and `Ⓔ⑩` asserts all three clauses,
because they are what the deciding arm reasons FROM.  The excursion is reported in those sigmas AND in
absolute `N_eff`, so another prior can be applied by a reader who disagrees with the choice.

COMPUTES: scope -- what is received and what is derived.  No spectrum here is new; every one is read
from the bank, and nothing is fitted beyond the two or three parameters each fit is of.
  INPUT   r = 1.0926                     -- P15's damping ratio, corpus measured
  INPUT   l_D = 1489.5783                -- the one-rate damping multipole, r7797+cc66.1
  INPUT   N_eff adopted = 3.046          -- the value P16 named as adopted until r7836+60
                                            re-anchored this receipt: P16 now states the network runs
                                            3 exactly and names 3.046 as first evaluated beside the
                                            3.044 the companion quotes, which is r7834's correction
  INPUT   N_eff quoted = 2.99 +/- 0.17   -- the constraint P16 itself quotes for a departure
  INPUT   L820_lcdm_L2512_nk800          -- the banked control arm, the baseline
  INPUT   r7801_neff_response_lcdm       -- 70's banked control at five N_eff, the free direction
  INPUT   r6897_wb_response_lcdm         -- the baryon response, for the Ⓒ⑦ᵇ comparison only
  INPUT   plik_lite TT                   -- the bandpowers, binning and covariance, the metric

** WHAT IT DOES NOT CLAIM. **  It does not close `PO-24`: `Y_He` and three others are named and not
tested, `70`'s `Y_He` bank being next.  It says nothing above `l = 1996`, which the bank does not
reach.  It does not claim `N_eff` is or is not fixed by the corpus -- it reports what `P16` says and
judges against what `P16` quotes.  And it computes no significance against the sky: every number here
is a degeneracy-fit number.

Built r7804 (node 60), on order r7803 from node 69, on 70's r7801 bank.  Stated for reversal.
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
NE_ADOPTED = 3.046
NE_QUOTED, NE_SIG = 2.99, 0.17

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


def load(name):
    """the response as a RATIO to its own centre -- never as an absolute spectrum, because a
    response run is a different configuration from the baseline and a ratio cancels what differs"""
    Z = np.load(os.path.join(SP, name), allow_pickle=True)
    vals = np.array(sorted({float(k.split('__')[1]) for k in Z.files if k.startswith('Dl__')}))
    c = vals[len(vals) // 2]

    def key(p, w):
        return next(k for k in Z.files
                    if k.startswith(p + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)
    L = Z[key('ls', c)].astype(float)
    D = np.array([Z[key('Dl', w)].astype(float) for w in vals])
    rat = D / D[len(vals) // 2]
    return vals, c, L, rat, PchipInterpolator(vals, rat, axis=0)


NS, N0, NL, NRAT, _NR = load('r7801_neff_response_lcdm.npz')
WS, W0, WL, WRAT, _WR = load('r6897_wb_response_lcdm.npz')


def ratio_on_LS(ne):
    rb = np.asarray(_NR(float(ne)))
    return np.interp(LS, NL, rb, left=rb[0], right=rb[-1])


print(f"\n  P16 ADOPTS N_eff = {NE_ADOPTED}, declared there as not derived, and QUOTES "
      f"{NE_QUOTED} +/- {NE_SIG}")
print(f"  that quoted precision is {NE_SIG / NE_QUOTED * 100:.2f} per cent against omega_b's 0.65 "
      f"-- about nine times more room in sigma")

# ======================================================= Ⓐ THE HARNESS REPRODUCED
head("A -- THE PUBLISHED TWO-PARAMETER FIGURE, REPRODUCED BEFORE A THIRD PARAMETER IS ADDED")


def fit2(target, keep, F):
    def at(dn):
        m = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** dn)[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r)
    o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
    return float(o.x), float(at(float(o.x)))


def fit3(target, keep, F):
    """A, Delta n and N_eff together, bounded to the bank's own grid.  The selection is a plain
    deterministic argmin with NO tie-break epsilon -- `r7802`'s form, after the build sweep flagged
    that comparison and two epsilons were tried and both were the wrong shape."""
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
    best = min(runs)
    spread = tuple(max(x[i] for x in runs) - min(x[i] for x in runs) for i in range(3))
    return best[1], best[2], best[0], spread


keep0 = window(100, 1758)
n0 = int(keep0.sum())
F0 = _fisher(keep0)
tgt0 = CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep0]
m0 = CS.bin_spectrum(LS, DL)[keep0]
r0 = tgt0 - float((m0 @ F0 @ tgt0) / (m0 @ F0 @ m0)) * m0
c_amp0 = float(r0 @ F0 @ r0)
dn0_, c0_ = fit2(tgt0, keep0, F0)
print(f"      window 100-1758, {n0} bins: chi^2/bin after the tilt {c0_ / n0:.4f}, absorbed "
      f"{(1 - c0_ / c_amp0) * 100:.1f} per cent")
check("Ⓐ①  the two-parameter fit returns 1.0815 chi^2 per bin over 171 covered bins and absorbs "
      "69.6 per cent, the same figures r7800 reproduced -- so this is that harness with the free "
      "direction swapped and nothing else changed",
      n0 == 171 and abs(c0_ / n0 - 1.0815) < 5e-4
      and abs((1 - c0_ / c_amp0) * 100 - 69.6) < 0.05)

# ======================================================= Ⓑ THE BANK
head("B -- 70's BANK: REACH, CENTRE AND THE OFFSET, AND WHETHER THE RESPONSE IS LINEAR")
REACH = float(NL[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]
print(f"      N_eff values {list(NS)}, centre {N0}, l grid {NL[0]:.0f}-{REACH:.0f} "
      f"step {NL[1] - NL[0]:.0f}")
check("Ⓑ②  the response reaches l = 1996, so THREE of the six windows the displacement table uses "
      "are available and three are not -- the same reach as the baryon bank, and no arm below "
      "speaks about a window its own inputs do not reach",
      REACH == 1996.0 and len(AVAIL) == 3)

print(f"      the bank's centre is {N0} and P16 adopts {NE_ADOPTED}: OFFSET {NE_ADOPTED - N0:+.3f}")
check("Ⓑ③  the bank is centred on 3.0 while the corpus adopts 3.046, so every excursion below is "
      "stated relative to the ADOPTED value with that offset carried -- asserted here because a "
      "0.046 shift reported as physics is exactly what a forgotten offset looks like",
      abs(N0 - 3.0) < 1e-12 and abs(NE_ADOPTED - N0 - 0.046) < 1e-12 and len(NS) == 5)

d1 = np.diff(NRAT, axis=0)
d2 = np.diff(d1, axis=0)
good = np.abs(d1).max(axis=0) > 0
CURV = float(np.max(np.abs(d2)[:, good].max(axis=0) / np.abs(d1)[:, good].max(axis=0)))
print(f"      worst |second difference| / |first| across the grid: {CURV:.4f}")
check("Ⓑ④  the response is NOT linear in N_eff either, so the five banked values are interpolated "
      "with a monotone spline and no derivative is extrapolated",
      CURV > 0.05)

# ======================================================= Ⓒ THE FITS
head("C -- THE TILT AND THE NEUTRINO COUNT FREE TOGETHER")
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
    ROWS.append(dict(lo=lo, hi=hi, n=n, dn2=dn2, dn3=dn3, c2=c2, c3=c3, c_amp=c_amp, ne3=ne3,
                     dne=ne3 - NE_ADOPTED, sp3=sp3, surv=abs(dn3) / abs(dn2) * 100.0,
                     a2=(1 - c2 / c_amp) * 100.0, a3=(1 - c3 / c_amp) * 100.0,
                     edge=min(abs(ne3 - NS[0]), abs(ne3 - NS[-1])) < 1e-9))
    r = ROWS[-1]
    print(f"\n      window {lo}-{hi}, {n} bins")
    print(f"        + tilt         : chi^2/bin {c2 / n:>8.4f}  Delta n {dn2:+.5f}"
          f"  absorbed {r['a2']:5.1f} %")
    print(f"        + tilt + N_eff : chi^2/bin {c3 / n:>8.4f}  Delta n {dn3:+.5f}"
          f"  absorbed {r['a3']:5.1f} %")
    print(f"        N_eff wanted   : {ne3:.5f} = {r['dne']:+.5f} from the adopted "
          f"= {r['dne'] / NE_SIG:+.2f} of the quoted sigma"
          + ("   ⛔ AT THE BANK'S EDGE" if r['edge'] else ""))
    print(f"        SURVIVES       : {r['surv']:.3f} per cent   (multistart spread: "
          f"Delta n {sp3[1]:.1e}, N_eff {sp3[2]:.1e})")

# r7804 (60): the bound below is NOT a chosen epsilon.  The clause this arm reasons FROM is that no
#   number this receipt PRINTS can differ according to which start wins -- so the bound is read off
#   the print format itself: half of the last decimal each quantity is set in type to.  Delta n and
#   N_eff print to five decimals, the survival to three, the offset in sigma to two.  An absolute
#   1e-7 here was the same shape of defect as the tie-break 69 corrected at r7803: measured spreads
#   run 1.2e-9 to 8.8e-9 over two builds x three windows -- a 7.4x observed variation against only
#   11.3x headroom, and the precedent in receipts/TOLERANCE_JUDGED.json declined to judge a flag
#   away at 12.2.  Against the printed decimals the tightest margin MEASURED is 281x (window
#   700-1760, the N_eff spread against the fifth decimal it is printed to), and the bound cannot
#   drift, because moving a print format moves the bound with it.
TIE_P = 0.5e-5                    # Delta n and N_eff are printed to five decimals
TIE_S = 0.5e-3                    # the survival percentage is printed to three
TIE_G = 0.5e-2                    # the excursion in units of the quoted sigma is printed to two
MARGINS = []
for r in ROWS:
    sp_dn, sp_ne = float(r['sp3'][1]), float(r['sp3'][2])
    MARGINS.append((TIE_P / sp_dn, TIE_P / sp_ne,
                    TIE_S / (100.0 * sp_dn / abs(r['dn2'])), TIE_G / (sp_ne / NE_SIG)))
    print(f"      window {r['lo']}-{r['hi']}: the starts agree to {sp_dn:.1e} on Delta n and "
          f"{sp_ne:.1e} on N_eff -- {min(MARGINS[-1]):.0f}x inside the tightest last decimal "
          f"any of the four printed quantities is set in")
check("Ⓒ⑤  the three-parameter fit converges on every available window strictly inside the bank's "
      "grid, and the twelve starts agree far more closely than the last decimal of EVERY quantity "
      "this receipt prints from them, so no number here is an extrapolation and none -- parameter, "
      "survival, or offset in sigma -- depends on which start wins",
      all(not r['edge'] for r in ROWS) and len(ROWS) == 3
      and all(min(m) > 1.0 for m in MARGINS))

surv = [r['surv'] for r in ROWS]
print(f"\n      survival across the three windows: {', '.join('%.3f' % s for s in surv)} per cent")
check("Ⓒ⑥  THE ORDER'S QUESTION: the displacement SURVIVES -- 100.273 per cent on the published "
      "window and over 100 on all three, so freeing the neutrino count moves the fitted tilt by "
      "about a part in three hundred, and in the wrong direction for absorption",
      all(s > 99.5 for s in surv) and abs(surv[0] - 100.273) < 0.01)

gain = [r['a3'] - r['a2'] for r in ROWS]
print(f"      absorbed-share gains: {', '.join('%+.2f' % g for g in gain)} points")
check("Ⓒ⑥ᵇ  and the absorbed share gains at most a quarter of a point on any window, against the "
      "baryon density's 4.4 -- so by the share as well as by the displacement, the neutrino count "
      "takes even less than the parameter r7800 already ruled out.  ⌗ NOT a registered arm",
      max(gain) < 0.3)

print()
print(f"      {'window':>12}{'corr(S, Neff)':>16}{'Neff removes':>14}{'tilt removes':>14}")
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
    d_ne = perp(CS.bin_spectrum(LS, DL * np.interp(LS, NL, np.asarray(_NR(NS[3]))))[keep])
    d_wb = perp(CS.bin_spectrum(LS, DL * np.interp(LS, WL, np.asarray(_WR(WS[3]))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))

    def sh(d):
        return float((d_sig @ F @ d) ** 2 / ((d @ F @ d) * (d_sig @ F @ d_sig))) * 100.0
    OVER.append(dict(lbl=f'{lo}-{hi}', c_sig=corr(d_sig, d_ne), rem=sh(d_ne), tilt=sh(d_tl),
                     c_st=corr(d_sig, d_tl), r_ne=corr(d_ne, resid), r_wb=corr(d_wb, resid)))
    o = OVER[-1]
    print(f"      {o['lbl']:>12}{o['c_sig']:>16.4f}{o['rem']:>13.1f}%{o['tilt']:>13.1f}%")
print("      ⌗ the baryon density scored -0.18, -0.24, -0.45 and removed 3.3, 5.7, 20.0 per cent.")
check("Ⓒ⑦  70's SHAPE CLAIM DOES NOT HOLD: the N_eff direction overlaps the signature even more "
      "weakly than the baryon density did, removing under two and a half per cent of its chi^2 on "
      "every window where the tilt removes seventy or more.  A monotone tilt across the damping "
      "tail is not, on this metric, the shape that absorbs this envelope",
      all(o['rem'] < 2.5 for o in OVER) and all(abs(o['c_sig']) < 0.2 for o in OVER))

print()
print(f"      {'window':>12}{'corr(S, tilt)':>16}{'Neff vs resid':>16}{'wb vs resid':>14}")
for o in OVER:
    print(f"      {o['lbl']:>12}{o['c_st']:>16.4f}{o['r_ne']:>16.4f}{o['r_wb']:>14.4f}")
print("      ⌗ AN ADDITION, MARKED AS ONE, and the arm that explains both results at once.  The")
print("        registration asked whether the displacement survives, not why a tail tilt fails.")
print("        ⌗ AND ITS FIRST FORM WAS WRONG: it compared each direction with the TILT and")
print("          concluded N_eff is 'far more tilt-like than omega_b', which the first table above")
print("          contradicts -- omega_b reaches 0.479 against N_eff's 0.172.  I wrote the sentence")
print("          before reading the numbers.  ⇒ GUARD: a sentence stating a comparison is written")
print("          AFTER the comparison is on the screen.")
print("        ⇒ The signature is almost exactly a tilt, so the ALREADY-FREE tilt takes 70 to 97")
print("          per cent of it.  What an absorber must overlap is therefore neither the signature")
print("          nor the tilt but the RESIDUAL the tilt leaves -- and both parameters measured so")
print("          far are nearly orthogonal to it.  One projection, in place of a fit.")
check("Ⓒ⑦ᵇ  the signature is almost exactly a tilt (|corr| above 0.84 on every window), and BOTH "
      "candidates are nearly orthogonal to the residual the tilt leaves (|corr| under 0.35) -- "
      "which is why neither absorbs it, and which turns the search for an absorber into one "
      "projection rather than a fit.  ⌗ NOT a registered arm",
      all(abs(o['c_st']) > 0.84 for o in OVER)
      and all(abs(o['r_ne']) < 0.35 and abs(o['r_wb']) < 0.35 for o in OVER))

print()
for r in ROWS:
    print(f"      {r['lo']}-{r['hi']}: N_eff wanted {r['dne'] / NE_SIG:+.2f} quoted sigma, "
          f"and {r['surv']:.2f} per cent of the displacement survives it")
check("Ⓒ⑧  THE ARM THAT DECIDES THE ROW, AND IT IS A CLEANER NEGATIVE THAN THE BARYON DENSITY'S.  "
      "The excursion the fit wants is INSIDE the constraint the corpus quotes on every window -- "
      "under half a sigma, so the datum permits it -- and the displacement survives it entirely "
      "anyway.  Where omega_b could be called unaffordable, N_eff is affordable and buys nothing, "
      "so the terminating clause fails on SHAPE and not on room",
      all(abs(r['dne'] / NE_SIG) < 0.5 for r in ROWS) and all(r['surv'] > 99.5 for r in ROWS)
      and abs(ROWS[0]['ne3'] - 2.98850) < 5e-5)

# ======================================================= Ⓓ WHAT IS STILL ABSENT
head("D -- THE INHERITED PARAMETERS STILL WITHOUT A BANKED RESPONSE")
NAMES = sorted(os.listdir(SP))
PARAMS = {
    'the baryon density  omega_b': ('wb_response', 'omega_b_response'),
    'the neutrino count  N_eff': ('neff_response',),
    'the helium fraction  Y_He': ('yhe', 'helium', 'yp_response'),
    'the optical depth  tau': ('tau_response', 'reion'),
    'the lensing amplitude  A_L': ('alens', 'a_lens', 'lensamp'),
    'the matter density  omega_m': ('wm_response', 'omega_m_response'),
}
found = {}
for label, pats in PARAMS.items():
    hits = [f for f in NAMES if any(p in f.lower() for p in pats)]
    found[label] = hits
    print(f"      {label:<36s} : {len(hits):>2} file(s)" + (f"  -> {hits[0]}" if hits else ""))
print(f"      ⌗ searched the {len(NAMES)} entries of computations/beyond_the_wall/spectra, the one "
      f"directory every\n        banked spectrum lives in, by the lowercase substring patterns "
      f"printed above applied to each\n        entry's filename -- so the absence stated here is "
      f"about THAT directory and THOSE patterns and\n        nothing else.")
print("      ⇒ The TWO this receipt FITS -- the baryon density and the neutrino count -- both have")
print("        banks, and that is what this arm asserts.  How many of the other four have banks is")
print("        another seat's activity and not this receipt's claim: 70 reports Y_He settable with")
print("        its bank next, and the printed standing above will move when it lands.  What does NOT")
print("        move is the screen: Ⓒ⑦ᵇ gives it, to apply to each when it lands, before any fit is run.")
check("Ⓓ⑨  the two inherited parameters this receipt actually FITS both have a banked response, "
      "and the standing of the other four is reported with the directory and the patterns it was "
      "searched by, in the sentence that states it",
      # r7804 (60), carrying 69's r7803 guard on this same arm shape in the PO-24 receipt: "exactly
      #   TWO of the six" is a check on another seat's banking -- it turns red the moment 70 lands
      #   Y_He, which the line above itself announces.  What is THIS receipt's is that the two banks
      #   it fits are there; the other four are the declared SCOPE of the search, not an assertion.
      bool(found['the baryon density  omega_b'])
      and bool(found['the neutrino count  N_eff']) and len(found) == 6)

# ======================================================= Ⓔ THE CLAUSES REASONED FROM
head("E -- THE P16 SENTENCES THE DECIDING ARM REASONS FROM, IN THREE STATES")
P16 = ' '.join(io.open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                       encoding='utf-8').read().split())
SENTS = [' '.join(s.split()) for s in re.split(r'(?<=[.!?])\s+', P16) if s.strip()]
# r7827 (69): P16 restated (72, L550 Y10).  The network still carries the Standard Model's 3.046; what
#   the construction adds is a right-handed neutrino whose contribution turns on its mass, which the
#   left-right models set; and Planck's 2.99 +/- 0.17 is still the measurement quoted.  So N_eff is
#   still not fixed by the construction, which is what the deciding arm reasons from.
# ** RE-ANCHORED r7836+60, and the reason is this seat's own correction at r7834 (per r2673's rule:
#    a receipt whose clause the corpus acts on is updated to assert the state it now holds, finding
#    preserved).  r7834's cold read of P16 found that sentence folding the non-instantaneous
#    correction INTO the ratio that omits it: `(4/11)^(1/3)` is the instantaneous ratio, so three
#    species at it give 3 EXACTLY and the 0.044 is what the module leaves out.  P16 now says that,
#    and names both values with their statuses, so the span this key read is gone. **
#   ⇒ ** AND THE CORRECTION VINDICATES THIS RECEIPT'S OWN BANK. **  `r7804` asserted an offset --
#     the response bank centred on `3.0` against P16's then-stated adopted `3.046` -- and flagged it
#     because "a forgotten one looks exactly like physics".  r7834 established that the network
#     really does run `3.0`, so the offset was P16'S ERROR AND NOT THE BANK'S, and the deciding arm
#     below was reasoning from the right centre all along.
#   ⌗ *The finding is untouched: N_eff is still not fixed by the construction, which is what the
#     deciding arm reasons FROM.  What moved is which words P16 says it in.*
KEYS = {
    'the network carries the Standard Model value': 'the count the integration itself runs on '
                                                    'is $3$ exactly',
    'the construction does NOT fix the count': "So the count turns on the state's mass",
    'and Planck\'s measurement is the number quoted': '$N_{\\mathrm{eff}}=2.99\\pm0.17$',
}
states = {}
for label, key in KEYS.items():
    states[label] = ('MATCHED' if any(key in s for s in SENTS)
                     else ('WITHDRAWN' if key in P16 else 'STALE'))
    print(f"      {label:<52s} -> {states[label]}")
check("Ⓔ⑩  all three P16 clauses resolve MATCHED -- that the network carries the Standard Model's "
      "value, that the construction does not fix the count (a light right-handed neutrino's share "
      "turns on its mass, which the right-handed scale sets), and that Planck's measurement is the number "
      "quoted.  These are the clauses the deciding arm reasons FROM: N_eff is free within its "
      "measured error because the construction does not fix it.  "
      "⌗ NOT a registered arm",
      all(v == 'MATCHED' for v in states.values()))

head("THE COUNT, THE SCOPE, AND WHAT IS NOT CLAIMED")
print("      REGISTERED ARMS: 9 -- Ⓐ① Ⓑ②③④ Ⓒ⑤⑥⑦⑧ Ⓓ⑨; ALL NINE met.  THREE are ADDITIONS,")
print("      each marked in its own label: Ⓒ⑥ᵇ the absorbed-share comparison, Ⓒ⑦ᵇ the")
print("      residual-overlap screen, and Ⓔ⑩ the P16 clauses.  CHECKS RUN: 12.")
print("      The EIGHT inputs are declared in the COMPUTES header; no spectrum is new and nothing")
print("      is fitted beyond the two or three parameters each fit is of.")
print("      NOT CLAIMED: that PO-24 closes -- Y_He and three others are named and not tested;")
print("      anything above l = 1996; that N_eff is or is not fixed by the corpus, the receipt")
print("      reporting what P16 says and judging against what P16 quotes; and no significance")
print("      against the sky, every number being a degeneracy-fit number.")

print('\n' + '=' * 90)
if fails:
    print(f"  ⛔ {len(fails)} CHECK(S) FAILED:")
    for x in fails:
        print(f"     - {x}")
    print('=' * 90)
    sys.exit(1)
print(f"""
  ALL CHECKS PASS.

  PO-24's terminating clause is not met by the neutrino count either, and the
  negative is cleaner than the baryon density's.

  The excursion the fit wants is INSIDE the constraint the corpus quotes --
  {ROWS[0]['ne3']:.4f} against an adopted {NE_ADOPTED}, which is {ROWS[0]['dne'] / NE_SIG:+.2f} of the
  quoted sigma -- so the datum permits it.  And the displacement survives it
  entirely: {min(surv):.2f} to {max(surv):.2f} per cent standing, the absorbed share gaining
  at most a quarter of a point.

  So the failure is not about room.  For the baryon density one could say the
  absorber was unaffordable; here it is affordable and buys nothing.

  And 70's shape argument inverts, for a reason that generalises.  The
  signature is almost exactly a tilt, so the already-free tilt takes 70 to 97
  per cent of it.  What a candidate must overlap is the RESIDUAL the tilt
  leaves -- and both parameters measured so far are nearly orthogonal to it.
  That is one projection, not a fit, and it is the screen to apply to Y_He when
  70's bank lands.
""")
print('=' * 90)
