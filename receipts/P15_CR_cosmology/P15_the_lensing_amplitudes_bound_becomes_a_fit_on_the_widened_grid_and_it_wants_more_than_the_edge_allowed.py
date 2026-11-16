#!/usr/bin/env python3
r"""r7812 (60) -- A_L's PUBLISHED WINDOW REFITTED ON THE WIDENED GRID, on order r7811 (69).

COMPUTES: the lensing amplitude's absorption of the damping displacement on 70's r7805 bank as
  EXTENDED to A_L = 1.4, replacing r7808's bound at the published window with a fit.
  INPUT  the signature:  r = 1.0926, l_D = 1489.5783
  INPUT  the baseline:   L820_lcdm_L2512_nk800, normalised to plik_lite TT
  INPUT  the referent, TT+lowE:        A_L = 1.243 +/- 0.096   (THE CORPUS CARRIES NONE)
  INPUT  the referent, TT,TE,EE+lowE:  A_L = 1.180 +/- 0.065
  INPUT  the bank:       spectra/r7805_alens_response_lcdm.npz, ALENS now 0.8 .. 1.4
  OUTPUT the fit where r7808 had a bound, and the excursion on both rulers

** THE ANSWER: r7808's BOUND WAS RIGHT IN DIRECTION AND UNDERSTATED THE SIZE. **

The published window's fit is now INTERIOR at A_L = 1.37732, so the bound becomes a fit.  It runs
the way r7808 registered -- a wider bank lets A_L absorb MORE -- and it runs FURTHER than the edge
allowed: the surviving displacement falls from the bound's 96.964 to 94.457 per cent, and the
absorbed share gains 4.18 points against the edge's 3.29.

** AND THE EXCURSION CHANGES CHARACTER, WHICH r7808 COULD NOT HAVE SEEN. **
At the old edge the wanted A_L sat 0.45 sigma INSIDE the temperature constraint, and r7808 called
A_L "comfortably affordable".  The real optimum is +1.40 sigma on that ruler and +3.04 sigma on the
joint one -- so it is still affordable on the ruler this metric scores against, and it has LEFT
three sigma of the jointly measured value.  The clause still fails, and "comfortably" no longer
holds.

** TWO OF THIS SEAT'S OWN EARLIER CALLS ARE TESTED HERE AND BOTH SURVIVE. **
  Ⓕ⑥  r7806 claimed the screen's projection is a LOWER bound on a free fit's gain; r7808 found it
    crossed on exactly one window, the edge-pinned one, and cut the claim's scope to INTERIOR fits.
    That window is now interior, and its ratio moves from 0.91 (crossed) to 1.16 (exceeds).  ** The
    scope cut was the right diagnosis, and this is the one case that could have refuted it. **
  Ⓗ⑧  the two windows that were already interior reproduce r7808 to every printed digit, so the
    seven-point interpolation is the same function as the five-point one where they overlap.

⌗ AND ONE TRAP CAUGHT BEFORE IT BIT: r7808 took the centre as the grid's midpoint BY INDEX, which
  was 1.0 only because five values are symmetric about it.  On seven it is 1.1.  Every pick off the
  grid is now by value, and Ⓑ② asserts the midpoint IS 1.1 so the hazard is a number on the record.
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

FAILED, PASSED = [], []


def head(t):
    print("\n" + "=" * 90 + f"\n  {t}\n" + "=" * 90)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


R, LD = 1.0926, 1489.5783
K = R ** 2 - 1
AL_TT, AL_TT_SIG = 1.243, 0.096
AL_JOINT, AL_JOINT_SIG = 1.180, 0.065

# r7808's published-window BOUND, which this revision replaces
R7808_BOUND_SURV, R7808_BOUND_GAIN, R7808_EDGE = 96.964, 3.29, 1.2
R7808_INT = {(700, 1760): (1.18409, 96.517), (1000, 1760): (1.04435, 97.776)}
R7808_RATIOS = {(100, 1758): 0.91, (700, 1760): 1.33, (1000, 1760): 1.90}

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
DLKEYS = sorted({float(k.split('__')[1]) for k in AZ.files if k.startswith('Dl__')})

# ⌗ EVERY PICK OFF THIS GRID IS BY VALUE.  See the docstring: the midpoint by index is 1.1 here.
CENTRE_IDX = int(np.argmin(np.abs(AS_ - 1.0)))
A0 = float(AS_[CENTRE_IDX])
MIDPOINT_BY_INDEX = float(AS_[len(AS_) // 2])
A_STEP = float(AS_[AS_ > A0].min())
A_STARTS = (float(AS_.min()), A0, A_STEP, float(AS_.max()))


def _key(pref, w):
    return next(k for k in AZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)


AL_ = AZ[_key('ls', A0)].astype(float)
AD = np.array([AZ[_key('Dl', w)].astype(float) for w in AS_])
ARAT = AD / AD[CENTRE_IDX]
_AR = PchipInterpolator(AS_, ARAT, axis=0)


def ratio_on_LS(a):
    rb = np.asarray(_AR(float(a)))
    return np.interp(LS, AL_, rb, left=rb[0], right=rb[-1])


print("=" * 90)
print("r7812 (60) -- A_L refitted on the widened grid: the bound becomes a fit")
print("=" * 90)

# ======================================================= Ⓐ / Ⓑ THE BANK AND THE CENTRE
head("A / B -- THE WIDENED BANK, AND THE CENTRE TAKEN BY VALUE")
INV = {nm: np.array([float(AZ[_key(nm, w)]) for w in AS_]) for nm in ('lA', 'rs', 'DM')}
for nm in ('lA', 'rs', 'DM'):
    print(f"      {nm:>4s} across the grid: spread {float(INV[nm].max() - INV[nm].min()):.3e}")
print(f"      config ALENS grid : {list(AS_)}   ({len(AS_)} values)")
print(f"      the file's Dl keys: {DLKEYS}   -- the {DLKEYS[0]} entry is the unlensed INPUT, excluded")
print(f"      l grid: {AL_[0]:.0f} to {AL_[-1]:.0f} step {AL_[1] - AL_[0]:.0f}, {len(AL_)} points")
check("Ⓐ①  the widened bank is the same direction EXTENDED and not a different object: seven grid "
      "values from the config's own list, the unlensed reference entry still present as an eighth "
      "key and still excluded from the interpolation, the three acoustic quantities still at "
      "exactly zero spread across all of them, and the multipole grid unchanged -- so this "
      "revision's numbers are comparable with r7808's",
      len(AS_) == 7 and DLKEYS[0] == 0.0 and len(DLKEYS) == 8
      and all(float(INV[n].max() - INV[n].min()) == 0.0 for n in ('lA', 'rs', 'DM'))
      and len(AL_) == 238 and AL_[0] == 100.0 and AL_[-1] == 1996.0
      and abs(float(AL_[1] - AL_[0]) - 8.0) < 1e-12)

print(f"\n      the ratio base, taken BY VALUE          : {A0}")
print(f"      the grid's MIDPOINT BY INDEX            : {MIDPOINT_BY_INDEX}   <-- r7808's form")
print(f"      difference                              : {MIDPOINT_BY_INDEX - A0:+.1f}")
print(f"      the screen's direction, one step above  : {A_STEP}")
print(f"      the multistart seeds, spanning the grid : {A_STARTS}")
check("Ⓑ②  THE TRAP IS A NUMBER ON THE RECORD RATHER THAN A WARNING IN A COMMENT: this grid's "
      "midpoint BY INDEX is 1.1, not the unlensed-normalised 1.0, because seven values are not "
      "symmetric about their middle entry the way five were.  r7808's code took the centre that "
      "way and would have divided every spectrum by the wrong slice with nothing in its output to "
      "say so.  Every pick off the grid here -- the ratio base, the screen's direction, and the "
      "multistart seeds -- is taken by VALUE",
      abs(MIDPOINT_BY_INDEX - 1.1) < 1e-12 and abs(A0 - 1.0) < 1e-12
      and abs(A_STEP - 1.1) < 1e-12 and A_STARTS[0] == 0.8 and A_STARTS[-1] == 1.4
      and float(np.abs(ARAT[CENTRE_IDX] - 1.0).max()) == 0.0)

REACH = float(AL_[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]


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
        for a0 in A_STARTS:
            o = minimize(at, x0=[dn0, a0], method='L-BFGS-B',
                         bounds=[(-3.0, 3.0), (AS_[0], AS_[-1])],
                         options={'ftol': 1e-14, 'gtol': 1e-12})
            runs.append((float(o.fun), float(o.x[0]), float(o.x[1])))
    best = min(runs)
    spread = tuple(max(x[i] for x in runs) - min(x[i] for x in runs) for i in range(3))
    return best[1], best[2], best[0], spread


# ======================================================= Ⓒ / Ⓓ / Ⓔ THE REFIT
head("C / D / E -- THE REFIT, AND THE BOUND IT REPLACES")
ROWS, OVER = [], []
for lo, hi in AVAIL:
    keep = window(lo, hi)
    n = int(keep.sum())
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v):
        return v - base * float((base @ F @ v) / (base @ F @ base))

    def corr(a, b):
        return float((a @ F @ b) / np.sqrt((a @ F @ a) * (b @ F @ b)))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_al = perp(CS.bin_spectrum(LS, DL * np.interp(LS, AL_, np.asarray(_AR(A_STEP))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))
    OVER.append(dict(lbl=(lo, hi), c_st=corr(d_sig, d_tl), r_al=corr(d_al, resid)))

    tgt = CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep]
    r_amp = tgt - float((base @ F @ tgt) / (base @ F @ base)) * base
    c_amp = float(r_amp @ F @ r_amp)
    dn2, c2 = fit2(tgt, keep, F)
    dn3, al3, c3, sp3 = fit3(tgt, keep, F)
    ROWS.append(dict(lo=lo, hi=hi, n=n, dn2=dn2, dn3=dn3, al3=al3, sp3=sp3,
                     dtt=al3 - AL_TT, djo=al3 - AL_JOINT,
                     surv=abs(dn3) / abs(dn2) * 100.0,
                     a2=(1 - c2 / c_amp) * 100.0, a3=(1 - c3 / c_amp) * 100.0,
                     edge=min(abs(al3 - AS_[0]), abs(al3 - AS_[-1])) < 1e-9))
    r = ROWS[-1]
    print(f"\n      window {lo}-{hi}, {n} bins")
    print(f"        A_L wanted   : {al3:.5f}"
          + ("   ⛔ STILL AT THE EDGE" if r['edge'] else "   (interior)"))
    print(f"          vs TT+lowE {AL_TT} +/- {AL_TT_SIG} : {r['dtt'] / AL_TT_SIG:+.2f} sigma")
    print(f"          vs joint   {AL_JOINT} +/- {AL_JOINT_SIG} : {r['djo'] / AL_JOINT_SIG:+.2f} sigma")
    print(f"        SURVIVES     : {r['surv']:.3f} per cent    gain {r['a3'] - r['a2']:+.2f} points"
          f"   (spread: Delta n {sp3[1]:.1e}, A_L {sp3[2]:.1e})")

PUB = ROWS[0]
INT = [r for r in ROWS if not r['edge']]
check("Ⓒ③  THE REGISTERED QUESTION, ANSWERED: the published window's fit is now INTERIOR, at an "
      "A_L strictly inside the widened grid rather than pinned on its maximum -- so r7808's bound "
      "there becomes a fit and is replaced, which is the whole of what this revision was ordered "
      "to do",
      not PUB['edge'] and AS_[0] < PUB['al3'] < AS_[-1] and len(INT) == 3)

check("Ⓓ④  AND IT RUNS THE WAY r7808 REGISTERED, FURTHER THAN THE EDGE ALLOWED: that revision "
      "stated the published row as a bound of at most 96.964 per cent surviving and said a wider "
      "bank could only let the lensing amplitude absorb MORE.  The refit lands BELOW the bound, "
      "with the absorbed share gaining more than it did at the edge -- so the bound was stated in "
      "the right direction and understated the size",
      PUB['surv'] < R7808_BOUND_SURV
      and (PUB['a3'] - PUB['a2']) > R7808_BOUND_GAIN
      and PUB['al3'] > R7808_EDGE)

print(f"\n      ⌗ r7808's bound: survival at most {R7808_BOUND_SURV}, gain {R7808_BOUND_GAIN:+.2f}, "
      f"at the edge {R7808_EDGE}")
print(f"        the refit      : survival {PUB['surv']:.3f}, gain {PUB['a3'] - PUB['a2']:+.2f}, "
      f"at {PUB['al3']:.5f}")
check("Ⓔ⑤  THE EXCURSION CHANGES CHARACTER, AND THAT IS A CORRECTION TO r7808's WORDING RATHER "
      "THAN A REFINEMENT OF IT: at the old edge the wanted value sat INSIDE the temperature "
      "constraint by nearly half a sigma and r7808 called the lensing amplitude comfortably "
      "affordable.  The real optimum is well over a sigma out on that ruler and beyond THREE on "
      "the jointly measured one -- still inside the ruler this metric scores against, so the "
      "clause still fails on shape rather than on room, but 'comfortably' no longer holds",
      PUB['dtt'] / AL_TT_SIG > 1.0 and PUB['dtt'] / AL_TT_SIG < 2.5
      and PUB['djo'] / AL_JOINT_SIG > 3.0)

# ======================================================= Ⓕ THE SCOPE CUT TESTED
head("F -- THE TEST OF r7808's OWN SCOPE CUT ON r7806's LOWER-BOUND CLAIM")
print(f"\n      {'window':>12}{'PREDICTED':>12}{'MEASURED':>11}{'ratio':>8}{'r7808':>9}  where it sits")
PRED = []
for o, r in zip(OVER, ROWS):
    pred = float(o['r_al']) ** 2 * (1.0 - float(o['c_st']) ** 2) * 100.0
    meas = r['a3'] - r['a2']
    PRED.append((pred, meas, r['edge']))
    print(f"      {str(o['lbl']):>12}{pred:>11.3f}%{meas:>10.3f}%{meas / pred:>8.2f}"
          f"{R7808_RATIOS[o['lbl']]:>9.2f}  {'edge' if r['edge'] else 'interior'}")
check("Ⓕ⑥  r7806's LOWER-BOUND CLAIM AND r7808's SCOPE CUT ON IT ARE BOTH VINDICATED BY THE ONE "
      "CASE THAT COULD HAVE REFUTED THEM: r7806 held the screen's projection to be a lower bound "
      "on a free fit's gain; r7808 found it crossed on exactly one window -- the one pinned at the "
      "grid's edge, where the fit could not reach its optimum while the projection was free -- and "
      "cut the claim's scope to INTERIOR fits rather than abandoning it.  That window is now "
      "interior, and its ratio has moved from below one to above it, so every window exceeds the "
      "prediction and the diagnosis was right",
      all(m > p for p, m, _ in PRED)
      and PRED[0][1] / PRED[0][0] > 1.0 and R7808_RATIOS[(100, 1758)] < 1.0)

# ======================================================= Ⓖ / Ⓗ
head("G / H -- START INDEPENDENCE, AND THE CONTROL THAT MUST NOT MOVE")
TIE_P, TIE_S, TIE_G = 0.5e-5, 0.5e-3, 0.5e-2
MARGINS = []
for r in ROWS:
    sp_dn, sp_a = float(r['sp3'][1]), float(r['sp3'][2])
    m = [TIE_P / sp_dn if sp_dn > 0 else np.inf, TIE_P / sp_a if sp_a > 0 else np.inf,
         TIE_S / (100.0 * sp_dn / abs(r['dn2'])) if sp_dn > 0 else np.inf,
         TIE_G / (sp_a / AL_TT_SIG) if sp_a > 0 else np.inf]
    MARGINS.append(m)
    print(f"      window {r['lo']}-{r['hi']}: {min(m):.0f}x inside the tightest printed decimal")
check("Ⓖ⑦  the sixteen starts -- now spanning the whole widened grid rather than clustering near "
      "its old centre -- agree far more closely than the last decimal of every quantity this "
      "receipt prints from them, so no number here depends on which start wins",
      all(min(m) > 1.0 for m in MARGINS) and len(A_STARTS) == 4)

print()
for r in ROWS[1:]:
    was_al, was_surv = R7808_INT[(r['lo'], r['hi'])]
    print(f"      window {r['lo']}-{r['hi']}: A_L {r['al3']:.5f} vs r7808's {was_al:.5f}   "
          f"survival {r['surv']:.3f} vs {was_surv:.3f}")
check("Ⓗ⑧  THE CONTROL HOLDS, AND IT HAD TEETH: the two windows whose fits were already strictly "
      "inside the old grid reproduce r7808's values to every printed digit.  Extending a grid "
      "upward cannot move a fit that sat inside it, so had these shifted, the seven-point "
      "interpolation would not have been the same function as the five-point one and every "
      "comparison in this receipt with r7808 would have been void",
      all(abs(r['al3'] - R7808_INT[(r['lo'], r['hi'])][0]) < 5e-5
          and abs(r['surv'] - R7808_INT[(r['lo'], r['hi'])][1]) < 5e-3 for r in ROWS[1:]))

# ======================================================= THE FIGURES
head("THE FIGURES THE PAPER AND THE INDEX ROW PRINT, PINNED INLINE")
# ⌗ r7812: the allowance is the COARSER of half the last printed digit and 0.05 per cent of the
#   value, and a first form of this arm used the FINER term on two of the five pins.  That is the
#   mirror of r7808's error rather than a repeat of it: there the tolerances were a hair too WIDE
#   and held nothing, here two were far too TIGHT and a correctly-rounded figure failed its own
#   pin -- the joint-sigma excursion rounds to 3.04 from 3.03562, a gap of 0.0044 inside an
#   allowance of 0.005, which a tolerance of 0.004 rejected.
#   ⇒ GUARD: compute the allowance as the rule states it -- the COARSER of the two terms -- and
#     then sit just inside it.  Taking the finer term is not caution; it is a different rule.
for nm, got, want in (('the refitted A_L, published window', PUB['al3'], 1.37732),
                      ('its surviving displacement', PUB['surv'], 94.457),
                      ('its absorbed-share gain', PUB['a3'] - PUB['a2'], 4.18),
                      ('its excursion, TT ruler, in sigma', PUB['dtt'] / AL_TT_SIG, 1.40),
                      ('its excursion, joint ruler, in sigma', PUB['djo'] / AL_JOINT_SIG, 3.04)):
    print(f"      {nm:<42s} {got:>11.5f}  pinned {want:>9.5f}  |d| {abs(got - want):.2e}")
check("Ⓘ⑨  ** ADDITION: ** every figure this revision puts into the paper or the index row is "
      "pinned here as an inline comparison strictly inside the allowance its printed precision "
      "licenses",
      abs(PUB['al3'] - 1.37732) < 6.0e-4
      and abs(PUB['surv'] - 94.457) < 0.045
      and abs((PUB['a3'] - PUB['a2']) - 4.18) < 0.0045
      and abs(PUB['dtt'] / AL_TT_SIG - 1.40) < 0.0045
      and abs(PUB['djo'] / AL_JOINT_SIG - 3.04) < 0.0045)

head("THE ARMS, AND THE COUNT")
print("      REGISTERED ARMS: 8 -- Ⓐ① Ⓑ② Ⓒ③ Ⓓ④ Ⓔ⑤ Ⓕ⑥ Ⓖ⑦ Ⓗ⑧.  ALL EIGHT met.")
print("      ONE is an ADDITION, marked: Ⓘ⑨, the figure pins.  CHECKS RUN: 9.")
print("      ⛔ omega_m is NOT here: 70 reports 10 of 55 slices.")
print(f"\n      PASSED: {len(PASSED)}   FAILED: {len(FAILED)}")
for f in FAILED:
    print(f"        ⛔ {f.splitlines()[0][:96]}")

# ⌗ r7812: AN EARLIER FORM OF THIS RECEIPT WROTE runs/r7812.npz HERE, and that was a defect of a
#   kind worth naming.  A receipt is run by the suite from arbitrary directories and is re-run by
#   every sweep; writing a TRACKED artefact on each run means any re-run dirties the tree, which
#   makes the validation chain's "dirty at both ends" record impossible to keep and would have put
#   a modified file in front of every later commit.  The path was also built from a fragile pair of
#   `..` hops out of the receipts tree.  The probe in this revision's computation directory already
#   saves its own outputs, which is where a side effect belongs.
#   ⇒ GUARD: a receipt asserts and prints; it does not write.  Anything worth keeping is written by
#     the probe that produced it, in the revision's own directory.

print("\n" + "=" * 90)
print("""
  THE LENSING AMPLITUDE, NOW MEASURED RATHER THAN BOUNDED ON EVERY WINDOW:

    the fit wants       1.37732 on the published window -- interior, where 1.2 was an edge
    the displacement    94.457 per cent standing, against the bound's "at most 96.964"
    the absorbed share  4.18 points, against the edge's 3.29
    the room            +1.40 sigma on the temperature ruler this metric scores against,
                        and +3.04 on the jointly measured one

  So PO-24's clause still fails on this parameter -- the displacement still stands at better than
  94 per cent while the absorber is pushed past three sigma of the joint value -- but r7808's
  "comfortably affordable" was an artefact of the edge and is withdrawn.

  ⌗ What a wider grid bought was not a different verdict but an honest one: the bound ran the way
    r7808 said it would, and it ran further than r7808 could see.
""")
if FAILED:
    sys.exit(1)
print("  ALL CHECKS PASS.\n")
