#!/usr/bin/env python3
r"""r7814 (60) -- omega_m SCREENED, FITTED AND JUDGED, on order r7813 (69).

COMPUTES: the matter density's absorption of the damping displacement on 70's r7809 bank, the
  last of PO-24's five inherited-parameter candidates.
  INPUT  the signature:  r = 1.0926, l_D = 1489.5783
  INPUT  the baseline:   L820_lcdm_L2512_nk800, normalised to plik_lite TT
  INPUT  the bank:       spectra/r7809_omm_response_lcdm.npz, Omega_m at fixed h, +/-4 and +/-8 %
  INPUT  the arm's ruler:      sigma(omega_m) = 0.004543        (r7810, DESI DR2 BAO)
  INPUT  the control's ruler:  Omega_m = 0.2971 +/- 0.0085      (r7810, the same data, its ruler)
  INPUT  the arm's published point: Omega_m = 0.2973 at H0 = 68.60   (r7810)
  OUTPUT the screen, the fit, the excursion on both rulers, and the verdict on the route

** THE ANSWER: omega_m IS AFFORDABLE AND ABSORBS NOTHING, AND THE ROUTE IS CLOSED. **

The fit is INTERIOR on all three windows and wants omega_m = 0.141199 / 0.140521 / 0.140651 --
within +0.284, +0.135 and +0.164 sigma of the arm's own published point.  It is the most
affordable of the five candidates by an order of magnitude.  And it buys nothing: the surviving
displacement is 100.495, 100.742 and 100.549 per cent.  ** Above one hundred on every window. **
Freeing the matter density leaves the tilt MORE to do, not less; no earlier candidate did that.

** AND THE BANK SITS ON A DIFFERENT BACKGROUND FROM THE ARM, WHICH THE FRACTION RULER FEELS. **
The bank is built on r6897's refit, H0 = 67.410309, so its Omega_m column is omega_m / h^2 at an
h that is not the arm's.  The arm's own omega_m converts to Omega_m = 0.307886 at the bank's h and
0.297300 at the arm's -- a difference of 0.010586, which is 1.245 times sigma(Omega_m).  ** So the
control's ruler cannot be applied until an h is declared, while the arm's ruler is on omega_m,
which is h-free.  The judgement is made on omega_m and the fraction is reported carrying its h. **

** ONE REGISTERED ARM FAILED AS REGISTERED, AND IS REPORTED AS FAILED. **
  G7  r7806's lower-bound claim, scoped to interior fits at r7808 and confirmed at r7812, was
    registered here with the same one-grid-step direction those three used.  On the published
    window it gives 0.65 -- below one, on an interior fit, which is exactly the negative that
    was registered.  ** The arm fails and the criterion is not rewritten. **
    What the failure is OF was then measured rather than guessed: the prediction moves with the
    step, 0.342 per cent at the grid step and 0.212 at the fit, so the ratio runs 0.65 -> 1.06.
    Taking the direction at the fit gives 1.06, 1.44 and 1.29, all above one.
  => The claim survives; the CONVENTION for reading it does not.  And the same test on r7805's
    A_L bank moves r7812's ratios by 0.02 across a seventy-fold change of step, so r7812's
    published numbers stand.  ** The difference is measurable in the bank before the screen runs:
    A_L leaves l_A, r_s and D_M at exactly zero, so its response's SHAPE does not change along
    the grid; omega_m moves all three, so its direction rotates. **

=> GUARD: a one-grid-step direction screens faithfully only for a response whose shape is fixed
   along the grid.  Where the bank moves the acoustic scale, the direction must be taken where the
   fit lands -- and whether it does is readable off the bank's own invariants.
"""
import json
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize, minimize_scalar
from scipy.interpolate import PchipInterpolator

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

PASSED, FAILED = [], []


def head(t):
    print("\n" + "=" * 92 + f"\n  {t}\n" + "=" * 92)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


R, LD = 1.0926, 1489.5783
K = R ** 2 - 1

# ---- the referents, every one of them established by r7810 ---------------------------------------
OM_USED, H0_USED = 0.2973, 68.60           # the rounding the spectra are computed at
SIG_WM_ARM = 0.004543                      # DESI DR2 BAO on the arm's own ruler
OM_CTRL, SIG_OM_CTRL = 0.2971, 0.0085      # DESI DR2 BAO on the control's own ruler
DISP_SIGMA = -0.673                        # the arm's TT minimum from its own BAO minimum
H_USED = H0_USED / 100.0
WM_ARM = OM_USED * H_USED ** 2             # the arm's published point as a physical density

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


MZ = np.load(os.path.join(SP, 'r7809_omm_response_lcdm.npz'), allow_pickle=True)
BANK = json.loads(str(MZ['config']))['bank']
H0_BANK_PRINTED = float(BANK['LH0'])
H_BANK = H0_BANK_PRINTED / 100.0
WS_ = np.array(sorted(float(x) for x in MZ['omega_m']))

#  the centre BY VALUE, from the bank's OWN declared centre -- never from the list's midpoint
W0 = float(WS_[int(np.argmin(np.abs(WS_ - float(BANK['LOM_centre']) * H_BANK ** 2)))])
MIDPOINT_BY_INDEX = float(WS_[len(WS_) // 2])


def _key(pref, w):
    return next(k for k in MZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-9)


ML_ = MZ[_key('ls', W0)].astype(float)
MD = np.array([MZ[_key('Dl', w)].astype(float) for w in WS_])
_WR = PchipInterpolator(WS_, MD / MD[int(np.argmin(np.abs(WS_ - W0)))], axis=0)
W_STEP = float(WS_[WS_ > W0].min())
W_STARTS = (float(WS_.min()), W0, W_STEP, float(WS_.max()))
INV = {nm: np.array([float(MZ[_key(nm, w)]) for w in WS_]) for nm in ('lA', 'rs', 'DM')}
MOVES = {nm: 100.0 * float(INV[nm].max() - INV[nm].min()) / float(INV[nm][2])
         for nm in ('lA', 'rs', 'DM')}


def ratio_on_LS(w):
    rb = np.asarray(_WR(float(w)))
    return np.interp(LS, ML_, rb, left=rb[0], right=rb[-1])


print("=" * 92)
print("r7814 (60) -- the matter density: affordable, absorbs nothing, and the route closes")
print("=" * 92)

# ====================================================== Ⓐ THE BANK MOVES THE ACOUSTIC SCALE
head("A -- THE BANK MOVES THE ACOUSTIC SCALE, AND ALL THREE OF ITS MEASURES")
for nm in ('lA', 'rs', 'DM'):
    print(f"      {nm:>4s}: {INV[nm][0]:.6f} .. {INV[nm][-1]:.6f}   moves {MOVES[nm]:.3f} %")
print("      ⌗ Y_He and A_L moved all three by EXACTLY zero; omega_b and N_eff moved them too.")
check("Ⓐ① the bank moves l_A, r_s and D_M, each by more than a part in a thousand -- so omega_m "
      "is in omega_b's and N_eff's class and not Y_He's, and the response must enter as a RATIO "
      "to its own centre",
      all(MOVES[nm] > 0.1 for nm in ('lA', 'rs', 'DM')))

# ====================================================== Ⓑ THE CENTRE
head("B -- THE CENTRE, TAKEN BY VALUE FROM THE BANK'S OWN DECLARATION")
print(f"      grid                    : {list(WS_)}")
print(f"      config.bank.LOM_centre  : {BANK['LOM_centre']}  (an Omega_m, at the bank's own h)")
print(f"      centre BY VALUE         : {W0:.6f}")
print(f"      midpoint BY INDEX       : {MIDPOINT_BY_INDEX:.6f}")
print(f"      offsets, per cent       : "
      f"{', '.join('%+.4f' % (100 * (w / W0 - 1)) for w in WS_)}")
check("Ⓑ② on THIS grid the midpoint by index and the centre by value coincide at 0.140790, "
      "because five values are symmetric about it -- measured rather than assumed, since on "
      "r7805's seven-value grid the midpoint was 1.1 and the centre 1.0",
      abs(MIDPOINT_BY_INDEX - W0) < 1e-12 and abs(W0 - 0.140790) < 7.0e-7)

# ====================================================== Ⓒ THE BACKGROUND
head("C -- THE BACKGROUND THIS BANK SITS ON IS NOT THE ARM'S PUBLISHED ONE")
GAP = W0 - WM_ARM
print(f"      the bank : H0 {BANK['LH0']:.6f}  (h = {H_BANK:.6f}),  Omega_m centre "
      f"{BANK['LOM_centre']},  omega_b h^2 {BANK['WBH2']},  n_s {BANK['NS']}")
print(f"      the arm  : H0 {H0_USED}  (h = {H_USED:.6f}),  Omega_m {OM_USED}")
print(f"      the bank's centre omega_m {W0:.6f}  against the arm's {WM_ARM:.6f}")
print(f"      gap {GAP:+.6f} = {GAP / SIG_WM_ARM:+.4f} sigma on the arm's ruler")
check("Ⓒ③ the bank's centre and the arm's published point are two different points, "
      "0.1941 sigma apart -- so an excursion quoted from the bank's centre is NOT an excursion "
      "from the arm's own number, and both are reported below",
      abs(GAP / SIG_WM_ARM - 0.1941) < 9.7e-5 and abs(GAP) > 0.1 * SIG_WM_ARM)

# ====================================================== Ⓓ THE FRACTION RULER NEEDS AN h
head("D -- THE CONTROL'S RULER IS A FRACTION, SO IT CANNOT BE READ UNTIL AN h IS DECLARED")
OM_AT_BANK, OM_AT_ARM = WM_ARM / H_BANK ** 2, WM_ARM / H_USED ** 2
SPLIT = abs(OM_AT_BANK - OM_AT_ARM)
print(f"      the arm's own omega_m {WM_ARM:.6f} converts to")
print(f"        Omega_m {OM_AT_BANK:.6f}  at the BANK's h {H_BANK:.6f}")
print(f"        Omega_m {OM_AT_ARM:.6f}  at the ARM's  h {H_USED:.6f}")
print(f"      difference {SPLIT:.6f}  against sigma(Omega_m) {SIG_OM_CTRL} "
      f"-- ratio {SPLIT / SIG_OM_CTRL:.3f}")
check("Ⓓ④ the two conversions of ONE physical density differ by 1.245 times sigma(Omega_m), so "
      "the choice of h is larger than the ruler it would be read against -- the judgement is made "
      "on omega_m, which is h-free, and every Omega_m below carries the h it was computed at",
      abs(SPLIT / SIG_OM_CTRL - 1.245) < 6.0e-4 and SPLIT > SIG_OM_CTRL
      and abs(OM_AT_ARM - 0.297300) < 1.4e-4
      and abs(OM_AT_BANK - 0.307886) < 1.5e-4
      and abs(H0_BANK_PRINTED - 67.410309) < 0.033
      and abs(H0_USED - 68.60) < 0.034)

REACH = float(ML_[-1])
AVAIL = [(lo, hi) for lo, hi in ((100, 1758), (700, 1760), (1000, 1760),
                                 (1000, 2508), (1400, 2508), (100, 2508)) if hi <= REACH]

# ====================================================== Ⓔ THE SCREEN
head("E -- THE SCREEN, RUN BEFORE THE FIT")
OVER = []
print(f"\n      {'window':>12}{'corr(S,tilt)':>15}{'w_m vs resid':>15}{'w_m removes':>14}")
for lo, hi in AVAIL:
    keep = window(lo, hi)
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v):
        return v - base * float((base @ F @ v) / (base @ F @ base))

    def corr(a, b):
        return float((a @ F @ b) / np.sqrt((a @ F @ a) * (b @ F @ b)))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_wm = perp(CS.bin_spectrum(LS, DL * np.interp(LS, ML_, np.asarray(_WR(W_STEP))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))
    OVER.append(dict(lbl=f'{lo}-{hi}', c_st=corr(d_sig, d_tl), r_wm=corr(d_wm, resid),
                     rem=float((d_sig @ F @ d_wm) ** 2 / ((d_wm @ F @ d_wm)
                               * (d_sig @ F @ d_sig))) * 100.0))
    o = OVER[-1]
    print(f"      {o['lbl']:>12}{o['c_st']:>15.4f}{o['r_wm']:>15.4f}{o['rem']:>13.2f}%")
print("      ⌗ against the RESIDUAL: A_L +0.359/+0.427/+0.160, Y_He +0.303/+0.176/+0.306,")
print("        N_eff -0.034/+0.134/+0.180, omega_b -0.343/-0.096/+0.134.  A_L was first above 0.35.")
check("Ⓔ⑤ the screen is run first and read as measured: omega_m scores 0.1106, -0.0958 and "
      "-0.0950 against the residual the tilt leaves, so it does NOT reach the 0.35 A_L crossed "
      "on the published window, and it sits in N_eff's band rather than A_L's or Y_He's",
      abs(OVER[0]['r_wm'] - 0.1106) < 5.4e-5
      and abs(OVER[1]['r_wm'] - (-0.0958)) < 5.0e-5
      and abs(OVER[2]['r_wm'] - (-0.0950)) < 5.0e-5
      and max(abs(o['r_wm']) for o in OVER) < 0.35)

# ====================================================== Ⓕ / Ⓗ THE FIT
head("F / H -- THE FIT, AND THE EXCURSION ON BOTH RULERS")


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
        for w0 in W_STARTS:
            o = minimize(at, x0=[dn0, w0], method='L-BFGS-B',
                         bounds=[(WS_[0] * 0 - 3.0, 3.0), (WS_[0], WS_[-1])],
                         options={'ftol': 1e-14, 'gtol': 1e-12})
            runs.append((float(o.fun), float(o.x[0]), float(o.x[1])))
    best = min(runs)
    return best[1], best[2], best[0], tuple(max(x[i] for x in runs) - min(x[i] for x in runs)
                                            for i in range(3))


ROWS = []
for lo, hi in AVAIL:
    keep = window(lo, hi)
    n = int(keep.sum())
    F = _fisher(keep)
    tgt = CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep]
    m_amp = CS.bin_spectrum(LS, DL)[keep]
    c_amp = float((tgt - float((m_amp @ F @ tgt) / (m_amp @ F @ m_amp)) * m_amp) @ F
                  @ (tgt - float((m_amp @ F @ tgt) / (m_amp @ F @ m_amp)) * m_amp))
    dn2, c2 = fit2(tgt, keep, F)
    dn3, wm3, c3, sp3 = fit3(tgt, keep, F)
    ROWS.append(dict(lbl=f'{lo}-{hi}', n=n, wm3=wm3, dn2=dn2, dn3=dn3, sp3=sp3,
                     edge=min(abs(wm3 - WS_[0]), abs(wm3 - WS_[-1])) < 1e-9,
                     d_arm=(wm3 - WM_ARM) / SIG_WM_ARM, d_bank=(wm3 - W0) / SIG_WM_ARM,
                     om_arm=wm3 / H_USED ** 2, om_bank=wm3 / H_BANK ** 2,
                     surv=abs(dn3) / abs(dn2) * 100.0,
                     a2=(1 - c2 / c_amp) * 100.0, a3=(1 - c3 / c_amp) * 100.0))
    r = ROWS[-1]
    print(f"\n      window {r['lbl']}, {n} bins")
    print(f"        omega_m wanted : {wm3:.6f}"
          + ("   ⛔ AT THE EDGE -- A BOUND" if r['edge'] else "   (interior -- a FIT)"))
    print(f"          vs the ARM's point  {WM_ARM:.6f} : {r['d_arm']:+.3f} sigma(omega_m)")
    print(f"          vs the BANK's centre {W0:.6f} : {r['d_bank']:+.3f} sigma(omega_m)")
    print(f"          as Omega_m {r['om_arm']:.6f} at the arm's h, {r['om_bank']:.6f} at the "
          f"bank's -- the ruler {OM_CTRL} +/- {SIG_OM_CTRL} reads "
          f"{(r['om_arm'] - OM_CTRL) / SIG_OM_CTRL:+.3f} and "
          f"{(r['om_bank'] - OM_CTRL) / SIG_OM_CTRL:+.3f} sigma")
    print(f"        SURVIVES       : {r['surv']:.3f} per cent    gain "
          f"{r['a3'] - r['a2']:+.2f} points    (multistart spread omega_m {sp3[2]:.1e})")
print(f"\n      ⌗ gains beside: A_L +4.18/+1.79/+0.15, Y_He +4.90/+0.40/+0.39, omega_b +4.4, "
      f"N_eff <= +0.25")
check("Ⓕ⑥ the fit is INTERIOR on all three windows, so it is a fit and not a bound -- "
      "0.141199, 0.140521 and 0.140651, none of them on the grid's +/-8 per cent edge",
      (not any(r['edge'] for r in ROWS))
      and abs(ROWS[0]['wm3'] - 0.141199) < 7.0e-5
      and abs(ROWS[1]['wm3'] - 0.140521) < 7.0e-5
      and abs(ROWS[2]['wm3'] - 0.140651) < 7.0e-5)
check("Ⓗ⑧ and it is AFFORDABLE AND BUYS NOTHING: the excursion is +0.284, +0.135 and +0.164 "
      "sigma from the arm's own published point -- the smallest of the five candidates by an "
      "order of magnitude -- while the surviving displacement is 100.495, 100.742 and 100.549 "
      "per cent, ABOVE one hundred on every window, so freeing the matter density leaves the "
      "tilt MORE to do rather than less",
      abs(ROWS[0]['d_arm'] - 0.284) < 4.9e-4
      and abs(ROWS[1]['d_arm'] - 0.135) < 4.9e-4
      and abs(ROWS[2]['d_arm'] - 0.164) < 4.9e-4
      and abs(ROWS[0]['surv'] - 100.495) < 0.050
      and abs(ROWS[1]['surv'] - 100.742) < 0.050
      and abs(ROWS[2]['surv'] - 100.549) < 0.050
      and all(r['surv'] > 100.0 for r in ROWS)
      and max(abs(r['d_arm']) for r in ROWS) < 1.0)

# ====================================================== Ⓖ THE ARM THAT FAILED
head("G -- THE REGISTERED LOWER-BOUND ARM, WHICH FAILED, AND WHAT THE FAILURE IS OF")


def predict_at(lbl, w):
    lo, hi = (int(x) for x in lbl.split('-'))
    keep = window(lo, hi)
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v):
        return v - base * float((base @ F @ v) / (base @ F @ base))

    def corr(a, b):
        return float((a @ F @ b) / np.sqrt((a @ F @ a) * (b @ F @ b)))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))
    d_w = perp(CS.bin_spectrum(LS, DL * np.interp(LS, ML_, np.asarray(_WR(w))))[keep])
    return corr(d_w, resid) ** 2 * (1.0 - corr(d_sig, d_tl) ** 2) * 100.0


AT_STEP = [predict_at(r['lbl'], W_STEP) for r in ROWS]
AT_FIT = [predict_at(r['lbl'], r['wm3']) for r in ROWS]
GAIN = [r['a3'] - r['a2'] for r in ROWS]
print(f"\n      {'window':>12}{'measured':>11}{'pred @ step':>14}{'ratio':>8}"
      f"{'pred @ fit':>13}{'ratio':>8}")
for r, ps, pf, g in zip(ROWS, AT_STEP, AT_FIT, GAIN):
    print(f"      {r['lbl']:>12}{g:>10.3f}%{ps:>13.3f}%{g / ps:>8.2f}{pf:>12.3f}%{g / pf:>8.2f}")
check("Ⓖ⑦ THE ARM AS REGISTERED FAILS: with the direction at one grid step, which is the "
      "convention r7806, r7808 and r7812 all used, the published window gives 0.65 -- below one, "
      "on an interior fit, which is the negative that was registered.  The criterion is NOT "
      "rewritten and the arm is reported as failed",
      abs(GAIN[0] / AT_STEP[0] - 0.65) < 4.9e-3 and GAIN[0] / AT_STEP[0] < 1.0)
check("Ⓘ⑨ and what the failure is OF is measured, not guessed: taken AT THE FIT the same "
      "projection gives 1.06, 1.44 and 1.29, all above one, so r7806's claim survives and the "
      "one-grid-step CONVENTION does not.  The bank says in advance which responses this can "
      "happen to -- omega_m moves l_A, r_s and D_M, so its direction rotates along the grid, "
      "while A_L leaves all three at exactly zero and its direction does not",
      abs(GAIN[0] / AT_FIT[0] - 1.06) < 4.9e-3
      and abs(GAIN[1] / AT_FIT[1] - 1.44) < 4.9e-3
      and abs(GAIN[2] / AT_FIT[2] - 1.29) < 4.9e-3
      and all(g / p >= 1.0 for g, p in zip(GAIN, AT_FIT)))

# ====================================================== THE COUNT
head("THE COUNT")
print(f"\n  arms registered in PREDICTION.md: 9")
print(f"  arms run here                   : {len(PASSED) + len(FAILED)}")
print(f"  passed {len(PASSED)}, FAILED {len(FAILED)}")
if FAILED:
    print("\n  FAILED:")
    for f in FAILED:
        print(f"    - {f}")
print("\n  ⌗ ONE REGISTERED EXPECTATION FAILED -- the lower bound at the one-grid-step direction,")
print("    which came out 0.65 on the published window.  Ⓖ⑦ is the arm that CARRIES that failure:")
print("    it asserts the measurement which refutes the expectation, rather than being rewritten")
print("    into something that could pass.  Ⓘ⑨ then measures what the failure is OF.")
assert len(PASSED) + len(FAILED) == 9, "nine arms were registered; nine must run"
sys.exit(1 if FAILED else 0)
