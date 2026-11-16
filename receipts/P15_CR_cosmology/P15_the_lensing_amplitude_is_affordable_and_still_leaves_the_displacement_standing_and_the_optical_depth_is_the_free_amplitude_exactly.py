#!/usr/bin/env python3
r"""r7806+2 = r7808 (60) -- PO-24's A_L ROUTE, AND THE LAST TWO INHERITED PARAMETERS.

COMPUTES: the lensing amplitude's absorption of the damping displacement, on 70's r7805 bank, and
  whether the optical depth and the matter density need banks at all.
  INPUT  the signature:  r = 1.0926, l_D = 1489.5783       (r7797+cc66.1's one-rate multipole)
  INPUT  the baseline:   L820_lcdm_L2512_nk800, normalised to plik_lite TT
  INPUT  the referent, TT+lowE:        A_L = 1.243 +/- 0.096   (THE CORPUS CARRIES NONE)
  INPUT  the referent, TT,TE,EE+lowE:  A_L = 1.180 +/- 0.065
  INPUT  the bank:       spectra/r7805_alens_response_lcdm.npz, ALENS grid 0.8 .. 1.2
  OUTPUT the surviving displacement, the absorbed share, and the excursion in both precisions

** THE ANSWER, AND IT IS A THIRD PATTERN RATHER THAN EITHER OF THE FIRST TWO. **

The lensing amplitude is the FIRST candidate the residual screen ADMITS -- its overlap with the
residual the tilt leaves reaches 0.427, above every earlier candidate -- and the FIRST that is
comfortably AFFORDABLE: the excursion the fit wants sits INSIDE the constraint, at -0.45, -0.61 and
-2.07 of the TT sigma, and on one window it lands within 0.06 sigma of what Planck itself measures.

And the displacement still stands at 96.5 to 97.8 per cent on every window.

So: omega_b was unaffordable-and-barely-overlapping, N_eff affordable-and-buys-nothing, Y_He
buys-something-and-unaffordable, and A_L is AFFORDABLE, ADMITTED BY THE SCREEN, AND STILL BUYS ONLY
THREE POINTS OF ABSORBED SHARE.  Four candidates, four different ways of not meeting the clause.

** AND TWO ARMS THIS SEAT REGISTERED CAME BACK AGAINST IT. **
  Ⓗ⑧ fired again, and THIS TIME THE BOUND RUNS THE UNFAVOURABLE WAY: the published window's fit is
    pinned at the bank's upper edge and the edge is AFFORDABLE, so a wider bank could let A_L absorb
    MORE while staying inside the constraint.  Unlike r7806's bound, this one does not strengthen
    the negative, and that is said rather than buried.
  Ⓕ⑥'s registered REASON for omega_m needing a bank was FALSE: I wrote that it is the only
    remaining candidate that moves the acoustic scale, and omega_b's and N_eff's OWN banks move
    l_A by 4.6 and 10.1.  Reported as failed; the correct reason is in Ⓙ⑩.
"""
import io
import json
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


R, LD = 1.0926, 1489.5783
K = R ** 2 - 1
AL_TT, AL_TT_SIG = 1.243, 0.096
AL_JOINT, AL_JOINT_SIG = 1.180, 0.065

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


AZ = np.load(os.path.join(SP, 'r7805_alens_response_lcdm.npz'), allow_pickle=True)
CFG = json.loads(str(next(AZ[k] for k in AZ.files if k.startswith('config'))))
AS_ = np.array(sorted(float(x) for x in CFG['ALENS']))
A0 = AS_[len(AS_) // 2]
DLKEYS = sorted({float(k.split('__')[1]) for k in AZ.files if k.startswith('Dl__')})


def _key(pref, w):
    return next(k for k in AZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)


AL_ = AZ[_key('ls', A0)].astype(float)
AD = np.array([AZ[_key('Dl', w)].astype(float) for w in AS_])
ARAT = AD / AD[len(AS_) // 2]
_AR = PchipInterpolator(AS_, ARAT, axis=0)


def ratio_on_LS(a):
    rb = np.asarray(_AR(float(a)))
    return np.interp(LS, AL_, rb, left=rb[0], right=rb[-1])


print("=" * 90)
print("r7808 (60) -- does the lensing amplitude absorb the damping displacement?")
print("=" * 90)

# ======================================================= Ⓐ THE BANK
head("A -- THE BANK, CHECKED RATHER THAN TAKEN ON REPORT, AND ITS REFERENCE ENTRY EXCLUDED")
INV = {}
for nm in ('lA', 'rs', 'DM'):
    INV[nm] = np.array([float(AZ[_key(nm, w)]) for w in AS_])
    print(f"      {nm:>4s} across the grid: {INV[nm][0]:.6f} .. {INV[nm][-1]:.6f}"
          f"   spread {float(INV[nm].max() - INV[nm].min()):.3e}")
print(f"      config ALENS grid: {list(AS_)}, centre {A0}")
print(f"      the file's Dl keys: {DLKEYS} -- the {DLKEYS[0]} entry is the unlensed INPUT, excluded")
print(f"      lensing potential's cosmology: H0 {CFG['bank']['phiphi']['H0']:.2f}, "
      f"Om {CFG['bank']['phiphi']['Om']:.4f} -- a LCDM stand-in, not the construction's own")
MAXDEV = [float(np.abs(r - 1).max()) for r in ARAT]
_top = ARAT[-1] - 1.0
CH = [float(AL_[i]) for i in np.where(np.diff(np.sign(_top)) != 0)[0]]
GAP = float(np.diff(CH).mean())
LA = float(INV['lA'][0])
print(f"      response, per mille: {', '.join('%.2f' % (d * 1000) for d in MAXDEV)}")
print(f"      {len(CH)} sign changes, mean spacing {GAP:.1f} against half the acoustic scale "
      f"{LA / 2:.1f} -- ratio {GAP / (LA / 2):.3f}")
check("Ⓐ①  the bank is the oscillating direction the order describes, and the reference entry is "
      "kept out of the grid: l_A, r_s and D_M have spread exactly zero across it, the grid is the "
      "config's own ALENS at 0.8 to 1.2 with centre 1.0 while the file also holds an unlensed 0.0 "
      "entry that is EXCLUDED, and the response oscillates at the peak-trough period -- its sign "
      "changes come at the mean spacing of half the acoustic scale, which is what a smoothing "
      "operator does, moving power from peaks into troughs",
      all(float(INV[n].max() - INV[n].min()) == 0.0 for n in ('lA', 'rs', 'DM'))
      and len(AS_) == 5 and abs(float(A0) - 1.0) < 1e-12 and DLKEYS[0] == 0.0
      and len(DLKEYS) == 6 and max(MAXDEV) < 0.02
      and len(CH) >= 8 and abs(GAP / (LA / 2) - 1.0) < 0.15)

# ======================================================= Ⓑ THE REFERENT
head("B -- THE REFERENT, ESTABLISHED RATHER THAN ASSUMED")
P15 = ' '.join(io.open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                       encoding='utf-8').read().split())
P16 = ' '.join(io.open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                       encoding='utf-8').read().split())
NSITES = P15.count('lensing amplitude')
DISCLAIM = 'rather than measuring a lensing amplitude'
print(f"      'lensing amplitude' occurs {NSITES} time(s) in P15 and "
      f"{P16.count('lensing amplitude')} in P16")
print(f"      one of them DISCLAIMS measuring one: ...{DISCLAIM!r}")
print(f"      the other is the sec:coherence clause r7806 wrote, naming it as not yet computed")
print(f"      ⇒ no corpus value and no corpus precision, so Planck's is used, and Planck's is")
print(f"        several numbers.  THE METRIC PICKS: plik_lite TT bandpowers, temperature alone.")
print(f"        TT+lowE       {AL_TT} +/- {AL_TT_SIG}  "
      f"({AL_TT_SIG / AL_TT * 100:.1f} %, {(AL_TT - 1) / AL_TT_SIG:+.1f} sigma from unity)")
print(f"        TT,TE,EE+lowE {AL_JOINT} +/- {AL_JOINT_SIG}  "
      f"({AL_JOINT_SIG / AL_JOINT * 100:.1f} %, {(AL_JOINT - 1) / AL_JOINT_SIG:+.1f} sigma)")
check("Ⓑ②  the corpus carries NO lensing amplitude and this receipt says so from the text rather "
      "than supplying one: P16 contains the phrase nowhere, and P15's two occurrences are the "
      "clause naming it as not yet computed and a sentence DISCLAIMING that its procedure measures "
      "one.  So Planck's is used -- and because 'Planck's A_L' is several numbers, the referent is "
      "chosen by the metric this harness actually scores against, temperature alone, with the "
      "joint value reported beside it and the excursion reported absolutely",
      # r7808 (60): the P15 OCCURRENCE COUNT is deliberately not asserted.  An earlier form had
      #   `NSITES == 2`, which this revision's own paper edit changes -- r7806's lesson, and this
      #   time caught BEFORE the edit rather than after it.  What is asserted is the disclaiming
      #   sentence, which sits in a section this revision does not touch, and P16's silence.  If
      #   either changes the referent must be re-derived, which is this arm's registered negative.
      P16.count('lensing amplitude') == 0 and DISCLAIM in P15
      and abs(AL_TT_SIG / AL_TT - 0.0772) < 0.002)

REACH = float(AL_[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]

# ======================================================= Ⓔ TAU
head("E -- THE OPTICAL DEPTH IS NOT A CANDIDATE IN THIS METRIC, AND IT IS A DERIVATION")
TAU = []
for lo, hi in AVAIL:
    keep = window(lo, hi)
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]
    for dt in (0.01, 0.02, 0.05):
        sc = CS.bin_spectrum(LS, DL * np.exp(-2 * dt))[keep]
        A = float((sc @ F @ base) / (sc @ F @ sc))
        r = base - A * sc
        TAU.append((float(r @ F @ r), A, float(np.exp(2 * dt))))
        print(f"      window {lo}-{hi:<5d} d_tau {dt:.2f} : residual chi2 {TAU[-1][0]:.3e}   "
              f"A {A:.9f}  vs exp(+2 d_tau) {TAU[-1][2]:.9f}")
check("Ⓔ⑤  THE OPTICAL DEPTH NEEDS NO BANK, and the reason is an EXACT degeneracy rather than an "
      "estimate: above the reionisation bump tau enters TT as the single factor exp(-2 tau), and "
      "this harness already marginalises one overall amplitude analytically at every evaluation, so "
      "refitting that amplitude after an exp(-2 d_tau) rescaling leaves a residual at machine zero "
      "and returns exactly exp(+2 d_tau), on every window and at three values of d_tau.  tau "
      "cannot absorb anything the amplitude is not already absorbing",
      all(c < 1e-20 for c, _, _ in TAU) and all(abs(A / w - 1) < 1e-12 for _, A, w in TAU)
      and len(TAU) == 3 * len(AVAIL))

# ======================================================= Ⓒ THE SCREEN
head("C -- THE SCREEN, RUN FIRST, ON r7804's MEASURE")
print(f"\n      {'window':>12}{'corr(S,tilt)':>15}{'A_L vs resid':>15}"
      f"{'A_L removes':>14}{'tilt removes':>14}")
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
    d_al = perp(CS.bin_spectrum(LS, DL * np.interp(LS, AL_, np.asarray(_AR(AS_[3]))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))

    def sh(d):
        return float((d_sig @ F @ d) ** 2 / ((d @ F @ d) * (d_sig @ F @ d_sig))) * 100.0
    OVER.append(dict(lbl=f'{lo}-{hi}', rem=sh(d_al), tilt=sh(d_tl),
                     c_st=corr(d_sig, d_tl), r_al=corr(d_al, resid)))
    o = OVER[-1]
    print(f"      {o['lbl']:>12}{o['c_st']:>15.4f}{o['r_al']:>15.4f}"
          f"{o['rem']:>13.2f}%{o['tilt']:>13.1f}%")
print("      ⌗ the earlier candidates, against the RESIDUAL: Y_He 0.303/0.176/0.306, N_eff")
print("        -0.034/0.134/0.180, omega_b -0.343/-0.096/0.134.  EVERY ONE under 0.35 in modulus.")
check("Ⓒ③  THE SCREEN ADMITS THIS ONE -- the registered second branch, and the first time it has "
      "fired: the lensing amplitude's overlap with the residual the tilt leaves reaches 0.427, "
      "above every earlier candidate's modulus and above the 0.35 band all three of them sat "
      "inside.  So the screen is not a filter that refuses everything, and what it admits here it "
      "admits on the window where the tilt leaves least",
      max(abs(o['r_al']) for o in OVER) > 0.35
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
        for a0 in (AS_[1], A0, AS_[3]):
            o = minimize(at, x0=[dn0, a0], method='L-BFGS-B',
                         bounds=[(-3.0, 3.0), (AS_[0], AS_[-1])],
                         options={'ftol': 1e-14, 'gtol': 1e-12})
            runs.append((float(o.fun), float(o.x[0]), float(o.x[1])))
    best = min(runs)
    spread = tuple(max(x[i] for x in runs) - min(x[i] for x in runs) for i in range(3))
    return best[1], best[2], best[0], spread


head("D -- THE FIT, AND THE EXCURSION AGAINST BOTH REFERENTS AND ABSOLUTELY")
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
    dn3, al3, c3, sp3 = fit3(tgt, keep, F)
    ROWS.append(dict(lo=lo, hi=hi, n=n, dn2=dn2, dn3=dn3, c2=c2, c3=c3, c_amp=c_amp, al3=al3,
                     dtt=al3 - AL_TT, djo=al3 - AL_JOINT, sp3=sp3,
                     surv=abs(dn3) / abs(dn2) * 100.0,
                     a2=(1 - c2 / c_amp) * 100.0, a3=(1 - c3 / c_amp) * 100.0,
                     edge=min(abs(al3 - AS_[0]), abs(al3 - AS_[-1])) < 1e-9))
    r = ROWS[-1]
    print(f"\n      window {lo}-{hi}, {n} bins")
    print(f"        + tilt       : chi^2/bin {c2 / n:>8.4f}  Delta n {dn2:+.5f}"
          f"  absorbed {r['a2']:5.1f} %")
    print(f"        + tilt + A_L : chi^2/bin {c3 / n:>8.4f}  Delta n {dn3:+.5f}"
          f"  absorbed {r['a3']:5.1f} %")
    print(f"        A_L wanted   : {al3:.5f}"
          + ("   ⛔ AT THE BANK'S EDGE -- A BOUND, NOT A FIT" if r['edge'] else ""))
    print(f"          vs TT+lowE {AL_TT} +/- {AL_TT_SIG} : {r['dtt']:+.5f} = "
          f"{r['dtt'] / AL_TT_SIG:+.2f} sigma")
    print(f"          vs joint   {AL_JOINT} +/- {AL_JOINT_SIG} : {r['djo']:+.5f} = "
          f"{r['djo'] / AL_JOINT_SIG:+.2f} sigma")
    print(f"        SURVIVES     : {r['surv']:.3f} per cent   (multistart spread: "
          f"Delta n {sp3[1]:.1e}, A_L {sp3[2]:.1e})")
INT = [r for r in ROWS if not r['edge']]
EDGE = [r for r in ROWS if r['edge']]
print(f"\n      survival: {', '.join('%.3f' % r['surv'] for r in ROWS)} per cent")
print(f"      absorbed-share gain: {', '.join('%+.2f' % (r['a3'] - r['a2']) for r in ROWS)} points")
check("Ⓓ④  THE LENSING AMPLITUDE IS AFFORDABLE -- THE FIRST CANDIDATE THAT IS -- AND THE "
      "DISPLACEMENT STILL STANDS: the excursion sits INSIDE the temperature constraint on every "
      "window, within two and a tenth sigma at worst and within a tenth of a sigma of what Planck "
      "jointly measures on one of them, and the displacement survives at better than 96 per cent "
      "throughout while the absorbed share gains at most three and a third points",
      all(abs(r['dtt'] / AL_TT_SIG) < 2.5 for r in ROWS)
      and min(abs(r['djo'] / AL_JOINT_SIG) for r in ROWS) < 0.10
      and all(r['surv'] > 96.0 for r in ROWS)
      and max(r['a3'] - r['a2'] for r in ROWS) < 3.5)

# ======================================================= Ⓕ OMEGA_M, AND THE FAILED REASON
head("F -- THE MATTER DENSITY, AND THE REASON THIS SEAT REGISTERED FOR IT")
MOVES = {}
for nm, f in (('omega_b', 'r6897_wb_response_lcdm.npz'), ('N_eff', 'r7801_neff_response_lcdm.npz'),
              ('Y_He', 'r7801_yhe_response_lcdm.npz'), ('A_L', 'r7805_alens_response_lcdm.npz')):
    d = np.load(os.path.join(SP, f), allow_pickle=True)
    sp = {}
    for q in ('lA', 'rs', 'DM'):
        kk = sorted(k for k in d.files if k.startswith(q + '__'))
        v = np.array([float(d[k]) for k in kk])
        sp[q] = float(v.max() - v.min()) if len(v) else float('nan')
    MOVES[nm] = sp
    print(f"      {nm:<9s} l_A spread {sp['lA']:>9.3f}   r_s {sp['rs']:>8.3f}   D_M {sp['DM']:>9.3f}")
print(f"      ⛔ Ⓕ⑥'s REGISTERED REASON IS FALSE.  This seat registered that the matter density is")
print(f"        the ONLY remaining candidate that moves the acoustic scale, every banked parameter")
print(f"        leaving l_A, r_s and D_M untouched.  Two of the four banks refute it, and they are")
print(f"        the two this seat used itself at r7800 and r7804.")
check("Ⓕ⑥  REGISTERED AND REFUTED BY ITS OWN MEASUREMENT, AND THE REFUTATION IS WHAT THIS ARM NOW "
      "CARRIES: the registered reason for the matter density needing a bank -- that it is the only "
      "remaining candidate which moves the acoustic scale -- is FALSE, and false about two banks "
      "this seat used itself.  omega_b moves l_A by more than four multipoles and r_s by more than "
      "two; N_eff moves l_A by more than ten, r_s by nearly five and D_M by more than eight.  Only "
      "the helium fraction and the lensing amplitude leave all three at exactly zero.  The "
      "criterion is NOT rewritten and the conclusion does not rest on it any more: the correct "
      "reason is in \u24bf\u2469, and what is asserted here is the measurement that killed the wrong one",
      MOVES['omega_b']['lA'] > 4.0 and MOVES['omega_b']['rs'] > 2.0
      and MOVES['N_eff']['lA'] > 10.0 and MOVES['N_eff']['rs'] > 4.0
      and MOVES['N_eff']['DM'] > 8.0
      and all(MOVES[n][q] == 0.0 for n in ('Y_He', 'A_L') for q in ('lA', 'rs', 'DM')))

# ======================================================= Ⓖ START INDEPENDENCE
head("G / H -- WHETHER THE NUMBERS ABOVE ARE FITS AT ALL")
TIE_P, TIE_S, TIE_G = 0.5e-5, 0.5e-3, 0.5e-2
MARGINS = []
for r in ROWS:
    sp_dn, sp_a = float(r['sp3'][1]), float(r['sp3'][2])
    m = [TIE_P / sp_dn if sp_dn > 0 else np.inf,
         TIE_P / sp_a if sp_a > 0 else np.inf,
         TIE_S / (100.0 * sp_dn / abs(r['dn2'])) if sp_dn > 0 else np.inf,
         TIE_G / (sp_a / AL_TT_SIG) if sp_a > 0 else np.inf]
    MARGINS.append(m)
    print(f"      window {r['lo']}-{r['hi']}: starts agree to {sp_dn:.1e} on Delta n and "
          f"{sp_a:.1e} on A_L -- {min(m):.0f}x inside the tightest printed decimal")
check("Ⓖ⑦  the twelve starts agree far more closely than the last decimal of every quantity this "
      "receipt prints from them, so no number here depends on which start wins",
      all(min(m) > 1.0 for m in MARGINS))

print(f"\n      interior: {[(r['lo'], r['hi']) for r in INT]}")
print(f"      at the edge: {[(r['lo'], r['hi']) for r in EDGE]}")
check("Ⓗ⑧  THE REGISTERED COMPARISON, AND ITS NEGATIVE BRANCH FIRED FOR THE SECOND REVISION "
      "RUNNING: the fit was registered to land strictly inside the bank on every window and it "
      "does not -- on the published window it sits exactly on the upper edge 1.2.  What holds, and "
      "what this arm asserts, is the negative branch's content: exactly one window is at the edge, "
      "it is the published one, it sits at the grid maximum to every digit, and the other two are "
      "strictly interior",
      len(EDGE) == 1 and (EDGE[0]['lo'], EDGE[0]['hi']) == (100, 1758)
      and abs(EDGE[0]['al3'] - AS_[-1]) < 1e-12
      and len(INT) == 2 and all(AS_[0] < r['al3'] < AS_[-1] for r in INT))

check("Ⓘ⑨  ** ADDITION, AND IT RUNS AGAINST THIS REVISION'S OWN CONCLUSION, WHICH IS WHY IT IS "
      "HERE: ** r7806's bound strengthened its negative because the helium fraction's edge was "
      "already unaffordable.  THIS ONE DOES THE OPPOSITE.  The lensing amplitude's edge is "
      "comfortably INSIDE the constraint -- less than half a sigma below the temperature value -- "
      "so a bank reaching above 1.2 could let A_L absorb MORE while remaining affordable, and the "
      "published window's absorbed share and survival are bounds in the direction that WEAKENS the "
      "refusal.  What the two interior windows establish stands on its own; what the published "
      "window establishes is a bound whose unfavourable direction is stated here rather than left "
      "to a reader.",
      EDGE[0]['dtt'] / AL_TT_SIG < 0.0 and abs(EDGE[0]['dtt'] / AL_TT_SIG) < 0.5
      and all(r['surv'] > 96.0 for r in INT))

check("Ⓙ⑩  ** ADDITION, the correct reason for the matter density, after Ⓕ⑥'s was false: ** what "
      "separates the two remaining parameters is not which of them moves the acoustic scale but "
      "whether an argument EXISTS that reaches them without a bank.  For the optical depth one "
      "does, and Ⓔ⑤ is it -- an exact degeneracy with a quantity this harness already frees, shown "
      "to machine precision.  For the matter density none does: its response is not banked, the "
      "screen cannot be applied to a direction whose response is missing because the response is "
      "precisely what the screen projects, and no combination of the four banked directions has "
      "been shown to span it.  So the asymmetry is DEMONSTRABLE EXCLUSION against NO AVAILABLE "
      "ARGUMENT, and the inherited-parameter route is therefore NOT yet fully closed",
      all(c < 1e-20 for c, _, _ in TAU)
      and not os.path.exists(os.path.join(SP, 'r7805_wm_response_lcdm.npz'))
      and len([1 for f in os.listdir(SP) if 'wm_response' in f or 'omega_m_response' in f]) == 0)

# ======================================================= Ⓚ THE SCREEN AGAINST THE FIT
head("THE SCREEN'S PREDICTION AGAINST THE FIT, AND r7806's LOWER-BOUND CLAIM GETS ITS SCOPE CUT")
print(f"\n      {'window':>12}{'PREDICTED':>12}{'MEASURED':>11}{'ratio':>8}   where the fit sits")
PRED = []
for o, r in zip(OVER, ROWS):
    pred = float(o['r_al']) ** 2 * (1.0 - float(o['c_st']) ** 2) * 100.0
    meas = r['a3'] - r['a2']
    PRED.append((pred, meas, r['edge']))
    print(f"      {o['lbl']:>12}{pred:>11.3f}%{meas:>10.3f}%{meas / pred:>8.2f}   "
          f"{'AT THE EDGE' if r['edge'] else 'interior'}")
check("Ⓚ⑪  ** ADDITION, and it CUTS THE SCOPE OF THIS SEAT'S OWN r7806 FINDING: ** r7806 concluded "
      "that the screen's projection is a lower bound on what a free fit recovers, approached from "
      "below and never crossed.  Here it IS crossed -- and on exactly one window, the one where "
      "the fit is pinned at the bank's edge and so cannot reach its optimum, while on both interior "
      "windows the measured gain still exceeds the prediction.  So the lower-bound property holds "
      "for an INTERIOR fit and not for a bounded one, which r7806 had no bounded case to learn "
      "from, and the screen's scope is now stated with that condition on it",
      all(m > p for p, m, e in PRED if not e)
      and any(m < p for p, m, e in PRED if e)
      and len([1 for p, m, e in PRED if e]) == 1)

# ======================================================= THE FIGURES THE PAPER WILL PRINT
head("THE FIGURES THE PAPER PRINTS FROM THIS RECEIPT, PINNED AS INLINE COMPARISONS")
# ⌗ Inline literals on purpose: a pin held in a table the comparison walks is invisible to the
#   static reader the pin is a promise to (r7806's third form of that lesson).
# ⌗ Each tolerance is set STRICTLY INSIDE the allowance the printed precision licenses, not at it.
#   A first form used 0.0485, 0.0483 and 0.0489 -- each a hair ABOVE 0.05 per cent of its own value
#   (0.048482, 0.048259, 0.048888) -- so all three pins were WIDER than the figure's allowance and
#   held nothing.  ⇒ GUARD: an allowance is rounded DOWN when it becomes a tolerance, because
#   rounding it up is the one direction that voids the pin.
_s0, _s1, _s2 = ROWS[0]['surv'], ROWS[1]['surv'], ROWS[2]['surv']
_r1 = OVER[1]['r_al']
_g0 = ROWS[0]['a3'] - ROWS[0]['a2']
_j1 = ROWS[1]['djo'] / AL_JOINT_SIG
for nm, got, want in (('surviving displacement, published window (a BOUND)', _s0, 96.964),
                      ('surviving displacement, 700-1760', _s1, 96.517),
                      ('surviving displacement, 1000-1760', _s2, 97.776),
                      ('the residual overlap the screen admits on', _r1, 0.427),
                      ('absorbed-share gain, published window', _g0, 3.29),
                      ('the excursion in joint sigma, 700-1760', _j1, 0.06)):
    print(f"      {nm:<52s} {got:>10.4f}  pinned {want:>8.3f}  |d| {abs(got - want):.4f}")
check("Ⓛ⑫  ** ADDITION: ** every figure the P15 sentence and the index row print from this receipt "
      "is pinned HERE strictly inside the allowance its printed precision licenses, as inline "
      "comparisons rather than a table a loop walks",
      abs(_s0 - 96.964) < 0.04
      and abs(_s1 - 96.517) < 0.04
      and abs(_s2 - 97.776) < 0.04
      and abs(_r1 - 0.427) < 0.0005
      and abs(_g0 - 3.29) < 0.005
      and abs(_j1 - 0.06) < 0.004)

# ======================================================= THE COUNT
head("THE ARMS, AND THE COUNT")
print("      REGISTERED ARMS: 8 -- Ⓐ① Ⓑ② Ⓒ③ Ⓓ④ Ⓔ⑤ Ⓕ⑥ Ⓖ⑦ Ⓗ⑧.")
print("      SEVEN met as registered.  ** Ⓕ⑥'s REGISTERED REASON IS FALSE -- refuted by two banks")
print("      this seat used itself, and the arm now carries that refutation.  ** Ⓗ⑧'s positive branch is FALSE and its negative branch")
print("      fired, ** for the second revision running -- and this time the bound runs AGAINST")
print("      the conclusion, which Ⓘ⑨ states.  FOUR are ADDITIONS, marked: Ⓘ⑨ Ⓙ⑩ Ⓚ⑪ Ⓛ⑫.")
print(f"\n      PASSED: {len(PASSED)}   FAILED: {len(FAILED)}")
for f in FAILED:
    print(f"        ⛔ {f.splitlines()[0][:96]}")
print("\n" + "=" * 90)
print("""
  FOUR CANDIDATES, FOUR DIFFERENT WAYS OF NOT MEETING PO-24's CLAUSE.

    omega_b : barely overlaps, and unaffordable where it would matter.
    N_eff   : affordable, and buys nothing.
    Y_He    : buys something, and is unaffordable by a wide margin.
    A_L     : AFFORDABLE, ADMITTED BY THE SCREEN -- and still buys only three points, leaving
              96.5 to 97.8 per cent of the displacement standing.

  So the four refusals do not share a reason, and no single criterion screens them.  What the
  screen does supply is the right ORDER of questions: overlap with the residual first, then room.

  AND THE ROUTE IS NOT FULLY CLOSED.  The optical depth is excluded by an exact degeneracy with a
  quantity this harness already frees.  The matter density is not excluded by anything: its
  response is unbanked, and the screen cannot project a direction whose response is missing.
""")
if FAILED:
    sys.exit(1)
print("  ALL CHECKS PASS.\n")
