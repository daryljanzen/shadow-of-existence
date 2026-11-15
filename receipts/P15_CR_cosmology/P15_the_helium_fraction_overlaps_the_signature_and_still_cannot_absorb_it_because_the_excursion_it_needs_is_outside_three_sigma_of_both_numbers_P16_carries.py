#!/usr/bin/env python3
r"""r7806 (60) -- PO-24's Y_He ROUTE IS CLOSED, AND IT CLOSES THE OTHER WAY ROUND FROM N_eff's.

COMPUTES: the helium fraction's absorption of the damping displacement, on 70's r7801 Y_He bank.
  INPUT  the signature:  r = 1.0926, l_D = 1489.5783       (r7797+cc66.1's one-rate multipole)
  INPUT  the baseline:   L820_lcdm_L2512_nk800, normalised to plik_lite TT
  INPUT  P16 ①: the network's own computed Y_p = 0.2471, radiatively corrected from 0.2432
  INPUT  P16 ①'s precision: 0.6 per cent (P16_theory_error_and_likelihood.py's sYp_frac)
  INPUT  P16 ②: the observational determination P16 quotes, 0.2453 +/- 0.0034 (Aver et al. 2021)
  INPUT  P16 ③: P16's standalone Born-level weak freeze-out, 0.2506
  INPUT  the bank:       spectra/r7801_yhe_response_lcdm.npz, five values 0.2054 .. 0.2854
  OUTPUT the surviving displacement, the absorbed share, and the excursion in BOTH precisions

** THE ANSWER.  N_eff was affordable and bought nothing.  Y_He buys something and is unaffordable. **

The helium fraction is the first candidate that genuinely overlaps the damping signature -- it
removes 53.5 per cent of it on the published window, against omega_b's 3.3 and N_eff's 0.1 -- and
the first that takes a real bite out of the displacement, leaving 83.0 per cent standing there
against both other parameters' 99 to 102.  So the shape argument that closed the other two routes
does NOT close this one.

What closes it is the room.  The excursion the fit wants is 0.2573 to at least 0.2854, against
P16's computed 0.2471 +/- 0.00148: +6.9 to at least +25.8 of P16's OWN precision, and +3.5 to at
least +11.8 of the observational error P16 quotes.  It is outside THREE sigma of both numbers on
every window.  PO-24's clause needs an absorber the corpus can afford, and this one it cannot.

⌗ And the bank is exhausted on the published window, so that row is a BOUND and not a fit -- which
  Ⓗ⑧ registered as a reachable negative and which FIRED.  It does not reach the verdict: the two
  windows where the fit is interior already fail affordability by seven sigma.
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

FAILED = []
PASSED = []


def head(t):
    print("\n" + "=" * 90 + f"\n  {t}\n" + "=" * 90)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


def _num(pat, text):
    m = re.search(pat, text)
    assert m, f"no match for {pat!r} in the file read"
    return float(m.group(1))


R, LD = 1.0926, 1489.5783
K = R ** 2 - 1

YP_BORN = 0.2432
YP_CORR_FAC = 1.016
YP_NET = 0.2471
YP_NET_FRAC = 0.006
YP_OBS, YP_OBS_SIG = 0.2453, 0.0034
YP_BORN_STANDALONE = 0.2506
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


print("=" * 90)
print("r7806 (60) -- does the helium fraction absorb the damping displacement?")
print("=" * 90)

# ======================================================= Ⓐ THE BANK IS WHAT IT IS REPORTED TO BE
head("A -- THE BANK, CHECKED RATHER THAN TAKEN ON REPORT")
INV = {}
for nm in ('lA', 'rs', 'DM'):
    INV[nm] = np.array([float(YZ[_key(nm, w)]) for w in YS])
    print(f"      {nm:>4s} across the five: {INV[nm][0]:.6f} .. {INV[nm][-1]:.6f}"
          f"   spread {float(INV[nm].max() - INV[nm].min()):.3e}")
print(f"      Y_He grid: {list(YS)}, centre {Y0}")
print(f"      the instrument's own default is _YP = 0.2454 and YHE unset is byte-identical, so the")
print(f"      bank's centre IS the baseline's helium fraction -- offset {Y0 - 0.2454:+.4f}")
check("Ⓐ①  70's bank is the pure damping direction it is reported to be: l_A, r_s and D_M are "
      "IDENTICAL across all five helium fractions to every stored digit, the five values sit at "
      "the stated spacing, and the centre equals the instrument's own default -- so what the fit "
      "below moves is the envelope and not the acoustic scale",
      all(float(INV[nm].max() - INV[nm].min()) == 0.0 for nm in ('lA', 'rs', 'DM'))
      and len(YS) == 5 and abs(float(Y0) - 0.2454) < 1e-12
      and max(abs(np.diff(YS) - 0.02)) < 1e-12)

# ======================================================= Ⓑ THE THREE P16 REFERENTS
head("B -- THE THREE HELIUM FRACTIONS P16 CARRIES, READ OUT OF P16's OWN FILES")
P16TEX = ' '.join(io.open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                          encoding='utf-8').read().split())
P16RCP = io.open(os.path.join(ROOT, 'receipts', 'P16_cosmogenesis_paper',
                              'P16_theory_error_and_likelihood.py'), encoding='utf-8').read()
CLAUSE = ("carries the network's computed $0.2432$ to $0.2471$")
print(f"      ① the network's computed value, radiatively corrected : {YP_NET:.4f}"
      f"  +/- {YP_NET_SIG:.5f}  ({YP_NET_FRAC * 100:.1f} %)")
print(f"      ② the observational determination P16 quotes          : {YP_OBS:.4f}"
      f"  +/- {YP_OBS_SIG:.4f}  ({YP_OBS_SIG / YP_OBS * 100:.1f} %)")
print(f"      ③ P16's standalone Born-level weak freeze-out         : {YP_BORN_STANDALONE:.4f}")
print(f"      the correction is ONE-WAY and not a range: "
      f"{YP_BORN:.4f} x {YP_CORR_FAC} = {YP_BORN * YP_CORR_FAC:.7f}")
print(f"      ① and ② disagree by {YP_NET - YP_OBS:+.4f} = "
      f"{(YP_NET - YP_OBS) / YP_NET_SIG:+.2f} of ①'s own error")
print(f"      ROOM: Y_He {YP_NET_FRAC * 100:.1f} % against N_eff's 5.7 and omega_b's 0.65")
check("Ⓑ②  the three helium fractions P16 carries are DIFFERENT OBJECTS and each is asserted from "
      "P16's own file, not from this seat's arithmetic: the 0.6 per cent theory error and the "
      "quoted 0.2453 +/- 0.0034 are the receipt's own constants, and P16's correction sentence is "
      "a ONE-WAY carry rather than an interval -- 0.2432 x 1.016 reproduces 0.2471 to four decimals",
      # r7806 (60): the VALUES are extracted and asserted, not P16's wording.  A gate that
      #   asserts another seat's literal text goes red when they reformat, while the claim holds.
      abs(_num(r'sYp_frac\s*=\s*([0-9.]+)', P16RCP) - YP_NET_FRAC) < 1e-12
      and abs(_num(r'Yp_corr\s*=\s*Yp\s*\*\s*([0-9.]+)', P16RCP) - YP_CORR_FAC) < 1e-12
      and abs(_num(r"'Yp':\s*\(([0-9.]+),", P16RCP) - YP_OBS) < 1e-12
      and abs(_num(r"'Yp':\s*\([0-9.]+,\s*([0-9.]+),", P16RCP) - YP_OBS_SIG) < 1e-12
      and CLAUSE in P16TEX
      and abs(YP_BORN * YP_CORR_FAC - YP_NET) < 5e-5)

# ======================================================= Ⓒ THE SCREEN, FIRST
head("C -- THE SCREEN, RUN BEFORE THE FIT, ON r7804's OWN MEASURE")
REACH = float(YL[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]
print(f"      reach = {REACH:.0f}; available windows: {AVAIL}")
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
    OVER.append(dict(lbl=f'{lo}-{hi}', rem=sh(d_yh), tilt=sh(d_tl),
                     c_st=corr(d_sig, d_tl), r_yh=corr(d_yh, resid)))
    o = OVER[-1]
    print(f"      {o['lbl']:>12}{o['c_st']:>15.4f}{o['r_yh']:>16.4f}"
          f"{o['rem']:>14.1f}%{o['tilt']:>13.1f}%")
print("      ⌗ r7804's numbers, which this column is read beside: against the residual N_eff")
print("        scored -0.034, +0.134, +0.180 and omega_b -0.343, -0.096, +0.134; and of the")
print("        SIGNATURE, N_eff removed 0.1, 0.2, 1.9 per cent and omega_b 3.3, 5.7, 20.0.")
check("Ⓒ③  the screen separates the two questions it was built to separate, and Y_He is the first "
      "direction on which they come APART: it overlaps the SIGNATURE far more than either earlier "
      "candidate (above 10 per cent on every window and above half on the published one, against "
      "omega_b's 3.3 and N_eff's 0.1 there), while its overlap with the RESIDUAL the tilt leaves "
      "stays in the same band as theirs (|corr| under 0.35) -- so a strong resemblance to the "
      "signature does NOT imply a strong claim on what the tilt leaves",
      all(o['rem'] > 10.0 for o in OVER) and OVER[0]['rem'] > 50.0
      and all(abs(o['r_yh']) < 0.35 for o in OVER)
      and all(abs(o['c_st']) > 0.84 for o in OVER))

# ======================================================= Ⓓ THE FIT


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


head("D / E -- THE FIT, RUN REGARDLESS OF THE SCREEN AS THE ORDER REQUIRES, AND THE EXCURSION")
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
          + ("   ⛔ AT THE BANK'S EDGE -- A BOUND, NOT A FIT" if r['edge'] else ""))
    print(f"          vs ① {YP_NET:.4f} +/- {YP_NET_SIG:.5f} : {r['d1']:+.5f} = "
          f"{r['d1'] / YP_NET_SIG:+.2f} sigma")
    print(f"          vs ② {YP_OBS:.4f} +/- {YP_OBS_SIG:.4f} : {r['d2']:+.5f} = "
          f"{r['d2'] / YP_OBS_SIG:+.2f} sigma")
    print(f"        SURVIVES       : {r['surv']:.3f} per cent   (multistart spread: "
          f"Delta n {sp3[1]:.1e}, Y_He {sp3[2]:.1e})")

INT = [r for r in ROWS if not r['edge']]
print(f"\n      survival: {', '.join('%.3f' % r['surv'] for r in ROWS)} per cent")
print(f"      absorbed-share gain from freeing Y_He: "
      f"{', '.join('%+.2f' % (r['a3'] - r['a2']) for r in ROWS)} points"
      f"   (N_eff's were +0.25 at most, omega_b's +4.4)")
check("Ⓓ④  the helium fraction DOES take a real bite, which neither earlier candidate did: the "
      "displacement no longer survives at 99 to 102 per cent but at 83 to 98, and the absorbed "
      "share gains up to 4.9 points -- so PO-24's clause is NOT refuted here by the displacement "
      "standing untouched, and the shape argument that closed the other two routes does not close "
      "this one",
      all(r['surv'] < 99.0 for r in ROWS) and min(r['surv'] for r in ROWS) < 90.0
      and max(r['a3'] - r['a2'] for r in ROWS) > 1.0)
check("Ⓔ⑤  and what closes it is the ROOM: the excursion the fit wants is outside THREE sigma of "
      "BOTH numbers P16 carries, on every window -- of the network's own computed value at its own "
      "0.6 per cent precision, and of the observational determination P16 quotes -- and it is "
      "reported absolutely as well, so a reader with another prior can apply it",
      all(r['d1'] / YP_NET_SIG > 3.0 for r in ROWS)
      and all(r['d2'] / YP_OBS_SIG > 3.0 for r in ROWS)
      and all(r['yh3'] > YP_NET + 3 * YP_NET_SIG for r in ROWS))

# ======================================================= Ⓕ THE SCREEN AGAINST THE FIT
head("F -- DOES THE SCREEN PREDICT WHAT THE FIT MEASURES, ON THE FIT'S OWN BASE?")
print(f"\n      {'window':>12}{'corr':>9}{'tilt takes':>12}{'residual is':>13}"
      f"{'PREDICTED':>11}{'MEASURED':>10}{'ratio':>8}")
PRED = []
for o, r in zip(OVER, ROWS):
    tilt_share = float(o['c_st']) ** 2
    pred = float(o['r_yh']) ** 2 * (1.0 - tilt_share) * 100.0
    meas = r['a3'] - r['a2']
    PRED.append((pred, meas, meas / pred))
    print(f"      {o['lbl']:>12}{o['r_yh']:>9.4f}{tilt_share * 100:>11.1f}%"
          f"{(1 - tilt_share) * 100:>12.1f}%{pred:>10.2f}%{meas:>9.2f}%{meas / pred:>8.2f}")
_rt = [p[2] for p in PRED]
print(f"      ⇒ ratio {min(_rt):.2f} to {max(_rt):.2f}, a factor of {max(_rt) / min(_rt):.2f}")
print("      ⌗ THE FIRST FORM OF THIS COMPARISON WAS THE DEFECT, NOT THE SCREEN.  Printing the")
print("        screen's TOTAL overlap beside the fit's INCREMENT gave ratios 0.092, 0.012, 0.037 --")
print("        a factor of 7.4 -- and would have read as the screen failing.  Both numbers were")
print("        right and the sentence putting them side by side was not.  Both forms are kept in")
print("        the revision's addendum.")
check("Ⓕ⑥  r7804's residual screen GENERALISES to a direction far less tilt-like than the two it "
      "was minted on: formed on the base the fit reports against -- the residual overlap squared "
      "times the share of the signature the residual is -- it predicts the measured gain within a "
      "factor of two on every window, across windows whose residual share runs 28 down to 3 per "
      "cent",
      all(0.5 < p[2] < 2.0 for p in PRED) and max(_rt) / min(_rt) < 2.0)
check("Ⓕ⑥ᵇ  ** ADDITION, and it is the check that the agreement is not a coincidence of size: ** "
      "the projection is a LOWER bound and is approached from below on every window, never "
      "crossed, because the fit re-optimises the tilt while the projection holds it fixed -- so "
      "the sign of the miss is forced by the construction and not fitted",
      all(p[1] > p[0] for p in PRED))

# ======================================================= Ⓖ START INDEPENDENCE
head("G / H -- THE TWO ARMS ABOUT WHETHER THE NUMBERS ABOVE ARE FITS AT ALL")
# r7806 (60), carrying r7804's form: the bound is read off the PRINT FORMAT, never an absolute
#   epsilon.  Delta n and Y_He print to five decimals, the survival to three, the excursion in
#   sigma to two.  Moving a print format moves the bound with it.
TIE_P, TIE_S, TIE_G = 0.5e-5, 0.5e-3, 0.5e-2
MARGINS = []
for r in ROWS:
    sp_dn, sp_y = float(r['sp3'][1]), float(r['sp3'][2])
    m = [TIE_P / sp_dn if sp_dn > 0 else np.inf,
         TIE_P / sp_y if sp_y > 0 else np.inf,
         TIE_S / (100.0 * sp_dn / abs(r['dn2'])) if sp_dn > 0 else np.inf,
         TIE_G / (sp_y / YP_NET_SIG) if sp_y > 0 else np.inf]
    MARGINS.append(m)
    print(f"      window {r['lo']}-{r['hi']}: starts agree to {sp_dn:.1e} on Delta n and "
          f"{sp_y:.1e} on Y_He\n        -- {min(m):.0f}x inside the tightest last decimal any "
          f"printed quantity is set in")
check("Ⓖ⑦  the twelve starts agree far more closely than the last decimal of EVERY quantity this "
      "receipt prints from them, so no number here -- parameter, survival, or excursion in sigma "
      "-- depends on which start wins",
      all(min(m) > 1.0 for m in MARGINS))

print(f"\n      interior windows: {[(r['lo'], r['hi']) for r in INT]}")
print(f"      at the bank's edge: {[(r['lo'], r['hi']) for r in ROWS if r['edge']]}")
# Ⓗ⑧ was registered as a COMPARISON with both branches named before measurement: "the fit is
#   inside the bank on every window.  *Negative: at an edge ⇒ the number is an extrapolation and is
#   reported as one, not as a fit.*"  ** THE NEGATIVE BRANCH FIRED. **  The positive branch is
#   FALSE and is printed as false immediately below; what the check asserts is the branch that
#   HOLDS -- which row is at the edge and which rows are interior -- because that is the fact the
#   report must carry.  The criterion is not rewritten: it is the same two-branch comparison, and
#   the branch it selected is the one this seat did not expect.
EDGE = [r for r in ROWS if r['edge']]
print(f"      ⛔ Ⓗ⑧'s POSITIVE BRANCH IS FALSE: the fit is NOT interior on every window.")
print(f"        at the bank's upper edge: {[(r['lo'], r['hi']) for r in EDGE]} -- the published one.")
print(f"        so that row is an extrapolation and is reported as a BOUND, per the registration.")
check("Ⓗ⑧  THE REGISTERED COMPARISON, ANSWERED BY THE MEASUREMENT AND NOT BY A PREFERENCE, AND "
      "ITS NEGATIVE BRANCH IS THE ONE THAT FIRED: the fit was registered to land strictly inside "
      "the bank on every window and it does NOT -- on the published window 100-1758 it lands "
      "exactly on the upper edge 0.2854, so that row is an extrapolation.  What holds, and what "
      "this arm therefore asserts, is the negative branch's own content: EXACTLY ONE window is at "
      "the edge, it is the published one, it sits at the bank's maximum to every digit, and the "
      "other two are strictly interior -- which is what licenses reporting that row as a bound "
      "in \u24be\u2468 rather than as a fit",
      len(EDGE) == 1 and (EDGE[0]['lo'], EDGE[0]['hi']) == (100, 1758)
      and abs(EDGE[0]['yh3'] - YS[-1]) < 1e-12
      and len(INT) == 2 and all(YS[0] < r['yh3'] < YS[-1] for r in INT))

check("Ⓘ⑨  ** ADDITION, the registered negative's own consequence, with its DIRECTION established "
      "rather than asserted: ** on the published window the fit is pinned at the bank's upper edge, "
      "so what that row establishes is `survival AT MOST 83.0 per cent` and `excursion AT LEAST "
      "+25.8 of P16's own sigma` -- a wider bank could only make the absorption larger and the "
      "excursion worse, both of which strengthen the negative.  AND THE VERDICT DOES NOT REST ON "
      "THAT ROW: the two windows where the fit lands strictly inside the bank already put the "
      "excursion beyond six sigma of P16's computed value with the displacement 95 to 98 per cent "
      "standing, so no extension of the bank can open this route",
      len(INT) == 2
      and all(r['d1'] / YP_NET_SIG > 6.0 for r in INT)
      and all(r['surv'] > 95.0 for r in INT)
      and ROWS[0]['edge'] and abs(ROWS[0]['yh3'] - YS[-1]) < 1e-9)

# ======================================================= THE CLAUSES REASONED FROM
# ======================================================= THE FIGURES P15 PRINTS FROM THIS RECEIPT
head("THE FIGURES THE PAPER PRINTS FROM THIS RECEIPT, PINNED HERE SO A WRONG ONE FAILS")
# r7806 (60): TWO earlier forms of an arm in this slot were both the forbidden shape, and both are
#   recorded in the revision's result rather than quietly dropped.
#   (i) The first asserted that P15 STILL CONTAINS the four-candidate "not yet computed" sentence --
#       the sentence THIS revision replaces.  A gate on the status of a sentence a live row is
#       asking to change.  It also passed when run and was false when committed, because I ran the
#       receipt before making the paper edit it reads.
#   (ii) The repair enumerated both paper states, which fixed the ordering problem but NOT the
#        deeper one: it still asserted that "the optical depth", "the lensing amplitude" and "the
#        matter density" appear in P15 -- so it would have gone red on ANOTHER SEAT'S SUCCESS, the
#        moment one of those three was computed and the clause legitimately lost it.
#   ⇒ Both are gone.  Locating a sentence is not a premise of THIS argument: what the argument
#     reasons from is P16's values (Ⓑ②), which are asserted there.  What belongs in this slot is
#     the obligation the paper edit actually creates -- that every figure P15 now prints from this
#     receipt FAILS here if it is wrong.
PINS = [('the share of the signature Y_He removes, published window', OVER[0]['rem'], 53.5, 0.05),
        ('the surviving displacement, published window (a BOUND)', ROWS[0]['surv'], 83.014, 0.0415),
        ('the surviving displacement, 700-1760', ROWS[1]['surv'], 95.624, 0.0478),
        ('the surviving displacement, 1000-1760', ROWS[2]['surv'], 98.246, 0.0491)]
for nm, got, want, tol in PINS:
    print(f"      {nm:<56s} {got:>10.3f}  pinned {want:>8.3f}  |d| {abs(got - want):.4f} < {tol}")
check("Ⓙ⑩  ** ADDITION: ** every figure the P15 sentence prints from this receipt is pinned HERE, "
      "so a wrong one fails this receipt rather than standing in type unchecked -- the share of the "
      "signature the helium direction removes, and the surviving displacement on all three windows "
      "including the published one whose value is a bound",
      all(abs(got - want) < tol for _, got, want, tol in PINS))

# ======================================================= THE COUNT
head("THE ARMS, AND THE COUNT")
print("      REGISTERED ARMS: 8 -- Ⓐ① Ⓑ② Ⓒ③ Ⓓ④ Ⓔ⑤ Ⓕ⑥ Ⓖ⑦ Ⓗ⑧.")
print("      SEVEN met as registered.  ** Ⓗ⑧'s POSITIVE BRANCH IS FALSE and its NEGATIVE BRANCH")
print("      FIRED: ** the fit is at the bank's upper edge on the published window, so that row is")
print("      a bound and not a fit.  Both branches were registered before measurement and the")
print("      criterion is unchanged; the arm carries the branch that holds, and Ⓘ⑨ carries the")
print("      consequence the registration attached to it.")
print("      THREE are ADDITIONS, marked: Ⓕ⑥ᵇ, Ⓘ⑨, Ⓙ⑩.  CHECKS RUN: 11.")
print(f"\n      PASSED: {len(PASSED)}   FAILED: {len(FAILED)}")
for f in FAILED:
    print(f"        ⛔ {f.splitlines()[0][:96]}")

print("\n" + "=" * 90)
if FAILED:
    print("""
  Ⓗ⑧'s REGISTERED POSITIVE BRANCH IS FALSE, AND IS REPORTED AS FALSE.

  PO-24's clause is not met by the helium fraction, and it fails the OTHER WAY ROUND from the
  neutrino count's.  N_eff was affordable and bought nothing.  Y_He buys something -- it is the
  first candidate that genuinely overlaps the damping signature, removing over half of it on the
  published window, and the first that leaves the displacement at 83 rather than 100 per cent --
  and it is unaffordable by a wide margin: outside three sigma of both numbers P16 carries, on
  every window, and beyond six sigma of the computed one where the fit is interior.

  So "the absorber was unaffordable" and "the absorber buys nothing" are now BOTH instantiated,
  on different parameters, and the two cannot be collapsed into one verdict about PO-24.

  And r7804's screen survives its first real test: formed on the base the fit reports against, it
  predicts the measured gain within a factor of two on a direction far less tilt-like than either
  parameter it was minted on, and it is a lower bound approached from below on every window.
""")
    sys.exit(1)
print("\n  ALL CHECKS PASS.\n")
