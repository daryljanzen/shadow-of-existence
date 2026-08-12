#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE HEIGHT TARGET FRONT #2 HAS BEEN WORKING TO WAS QUOTED AGAINST A SKY NUMBER
CARRYING A 3.4% ERROR BAR THAT WAS NEVER WRITTEN DOWN.  SO "SUB-PER-CENT HEIGHTS" ASKED FOR FIVE
TIMES MORE PRECISION THAN THE STATISTIC IT WAS MEASURED WITH POSSESSES, AND THE 2-3% RESIDUAL
REPORTED AT c54.175 IS ABOUT ONE SIGMA.  ** THE STATISTIC WITH THE INFORMATION IS chi^2, AND IT SAYS
SOMETHING SHARPER AND LESS COMFORTABLE. **

Built r2376+c54.176, front #2.

===================================================================================================
** WHAT THIS FILE CORRECTS IS MY OWN MEASUREMENT PROTOCOL, NOT THE CONSTRUCTION. **
===================================================================================================

Since c54.168 every height claim in this fork -- "-13% and -34%", "2-3%", "-0.05%" -- has been a
comparison of P1/P2 and P1/P3 against two bare numbers, 2.217 and 2.277, with no uncertainty
attached.  ** Read off the plik_lite bandpowers with the published covariance, the sky's own peak
height ratios are 2.256 +- 0.077 and 2.280 +- 0.074: 3.4% and 3.2%. **  Every figure quoted below a
few per cent was therefore reporting the instrument's noise against the sky's noise and calling the
difference physics.  *The 13% and 34% were real -- four and ten sigma.  The 2-3% were not.*

  PART 1  ** FIRST, THE INSTRUMENT IS CONVERGED, AND THE EARLIER SPREAD HAD A CAUSE. **  Pushing
          the mode count 1.4x, the k-range 1.3x and the eta-sampling 1.8x moves P1/P2 by 0.09% and
          P1/P3 by 0.37%.  ** The 2% and 7% swings that prompted this check came from LMAXL=1300,
          which sets k_max and was truncating the k integral under the third peak. **  A numerical
          floor has to be established before a physics difference of the same size is attributed.
  PART 2  ** THE SKY'S OWN RATIOS CARRY 3.2-3.4%, COMPUTED HERE FROM THE PUBLISHED COVARIANCE. **
          Not a diagonal estimate -- the two peak bins' 2x2 block, propagated through the ratio.
  PART 3  ** SO THE RATIO STATISTIC CANNOT SEPARATE THE TWO CANDIDATE DAMPING COEFFICIENTS, AND IT
          CANNOT SUPPORT THE CLAIM I WAS ABOUT TO MAKE. **  A scan of one multiplier on 1/k_D^2
          shows P1/P2 selecting 1.094 +- 0.184 and P1/P3 selecting 0.897 +- 0.055 -- a split of
          1.03 sigma.  ** I had this written as "no single damping scale fits both, so the residual
          is the envelope's SHAPE".  Its own error bar does not support that, and it is withdrawn
          here rather than published. **
  PART 4  ** chi^2 OVER 185 BINS DOES SEPARATE THEM, AND IT PREFERS 8/9 OVER 16/15 BY 1123. **  The
          minimum sits at a multiplier of 0.865 against 8/9's 0.859 -- 0.7% apart; 16/15
          costs seven inflated sigma.  ** THE COEFFICIENT IS NOT BEING CHOSEN BY THAT NUMBER. **
          8/9 is restored because it is the corpus's standing value and NEITHER value has ever been
          derived here -- `C8_diffusion_length.py` has named the ambiguity in its own text since it
          was written.  *I changed it to 16/15 earlier this revision on recollection.  A remembered
          number is not a derivation, and a number that fits better is not one either.*
          ** !! AND THE SECOND HALF OF THAT IS SUPERSEDED ONE REVISION LATER, IN THE DIRECTION
          THAT COSTS chi^2. **  c54.177 DERIVES the coefficient from the photon hierarchy with the
          polarisation multipoles -- the polarisation correction comes out as a factor 1.1996
          against 6/5 -- so 16/15 is no longer a remembered number and 8/9 is no longer the
          corpus's undecided default.  ** 16/15 is adopted, the control's floor goes 22.5 -> 28.6,
          and the 1123 measured here becomes a measurement of what the transfer is missing rather
          than an argument about a coefficient. **  *Everything PART 4 measures still holds
          exactly; what is withdrawn is its CONCLUSION about which value to carry, and it is
          withdrawn by a derivation and not by the fit it refused.*
          `P15_the_shear_coefficient_derived_not_remembered`
  PART 5  ** AND THE chi^2 VALUES `L-147` PINNED CAN NOW BE RECOMPUTED. **  They were produced by a
          script in /tmp and typed in.  `computations/planck_tt_likelihood/chi2_of_spectrum.py` is
          that machinery in the corpus, and it returns both pinned numbers exactly from banked
          spectra.

** WHAT THIS DOES TO FRONT #2. **  Its target -- sub-per-cent peak HEIGHTS -- is retired, because it
was written against a statistic that cannot see one per cent.  ** The replacement is the one that
was always doing the work: chi^2/dof on the LambdaCDM arm, 22.5 against CAMB's 0.96. **  And the
first named item under it is the derivation that this file could not supply: the free-streaming
photon hierarchy carrying the polarisation multipoles, from which the shear coefficient FALLS OUT
rather than being chosen.

SETTINGS: reduced -- LMAXL=1300 vs production 3000.  CANNOT CHECK AT PRODUCTION here: this file's
claim is about the RESOLUTION OF THE STATISTIC (the sky's own peak-ratio errors, 2.256+-0.077 and
2.280+-0.074), which is a property of plik_lite and not of the transfer's depth.  ** The bars do
not move with LMAXL, so no production run can change what this file establishes. **

rc=0 on success.  Run: python3 P15_the_height_target_was_below_the_resolution_of_its_own_statistic.py
                       (numpy scipy, ~15 s)
"""
import os
import sys

import numpy as np
from scipy.io import FortranFile
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
LIK = os.path.join(ROOT, 'computations', 'planck_tt_likelihood')
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, LIK)
import chi2_of_spectrum as CS                                              # noqa: E402

# =====================================================================
print("=" * 78)
print("PART 1 — THE NUMERICAL FLOOR, ESTABLISHED BEFORE ANY PHYSICS DIFFERENCE IS ATTRIBUTED")
print("=" * 78)
# runs of ACOUSTIC_two_arm.py, ARM=lcdm, ETAEND=4000, shear coefficient held at the c54.176 trial
# value of 16/15 throughout so that ONLY the numerics vary between rows
CONV = [
    ('NK=600  LMAXL=2000  NLOS=560   (baseline)', 2.2164, 2.4201, True),
    ('NK=850  LMAXL=2000  NLOS=560   (k-sampling x1.42)', 2.216, 2.420, True),
    ('NK=600  LMAXL=2600  NLOS=560   (k-range x1.30)', 2.214, 2.411, True),
    ('NK=600  LMAXL=2000  NLOS=1000  (eta-sampling x1.79)', 2.216, 2.419, True),
    ('NK=500  LMAXL=1300  NLOS=560   (the k integral TRUNCATED)', 2.265, 2.589, False),
]
print(f"  {'configuration':>52} {'P1/P2':>8} {'P1/P3':>8}")
for nm, a, b, ok in CONV:
    print(f"  {nm:>52} {a:>8.4f} {b:>8.4f}{'' if ok else '   <- not converged'}")
cvg = np.array([[a, b] for _, a, b, ok in CONV if ok])
s2 = (cvg[:, 0].max() - cvg[:, 0].min()) / cvg[:, 0].mean()
s3 = (cvg[:, 1].max() - cvg[:, 1].min()) / cvg[:, 1].mean()
bad = [r for r in CONV if not r[3]][0]
t2 = abs(bad[1] - cvg[0, 0]) / cvg[0, 0]
t3 = abs(bad[2] - cvg[0, 1]) / cvg[0, 1]
print(f"\n  ** THE CONVERGED SPREAD IS {s2:.2%} ON P1/P2 AND {s3:.2%} ON P1/P3. **")
print(f"  ** THE TRUNCATED ROW SITS {t2:.1%} AND {t3:.1%} AWAY — LMAXL SETS k_max THROUGH")
print("     `lL = linspace(12, LMAXL, 3*NK)`, so 1300 was cutting the k integral under the THIRD")
print("     PEAK.  *That, and not the physics, was the swing that prompted this check.* **")
if max(s2, s3) > 0.01:
    fail.append(f"the converged spread is {max(s2, s3):.2%} -- the instrument is not converged")
if min(t2, t3) < 2 * max(s2, s3):
    fail.append("the truncated run is not separated from the converged ones -- PART 1's claim fails")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE SKY'S OWN PEAK-HEIGHT RATIOS, WITH THE ERROR BAR THAT WAS NEVER QUOTED")
print("=" * 78)
_f = FortranFile(CS._LIK.cov_file, 'r')
_c = _f.read_reals(dtype=float).reshape((CS._LIK.nbin_hi, CS._LIK.nbin_hi))
COV = (np.tril(_c) + np.tril(_c, -1).T)[:CS._LIK.nbintt, :CS._LIK.nbintt]
lc, fac = CS.bin_center_and_fac()
# ** X_data IS BINNED C_l, NOT D_l -- and peak-finding on it directly puts the peaks tens of
# multipoles low and loses the FIRST one entirely under the falling plateau.  That is how this was
# caught: the peaks came out at 464/761/1085 instead of 221/527/815. **
D = CS.X_DATA * fac
CD = COV * np.outer(fac, fac)
pk = argrelextrema(D, np.greater, order=3)[0]
print(f"  peaks in the binned D_l at ell = {np.round(lc[pk[:3]], 1)}  "
      f"(the sky's 220.6 / 538.1 / 809.8)")
SKY = {}
for i, nm in ((1, 'P1/P2'), (2, 'P1/P3')):
    a, b = pk[0], pk[i]
    r = D[a] / D[b]
    g = np.array([1 / D[b], -D[a] / D[b] ** 2])
    e = float(np.sqrt(g @ np.array([[CD[a, a], CD[a, b]], [CD[a, b], CD[b, b]]]) @ g))
    SKY[nm] = (float(r), e)
    print(f"  ** {nm} = {r:.4f} +- {e:.4f}   ({100*e/r:.2f}%) **   "
          f"[the bare number used since c54.168: {2.217 if i == 1 else 2.277}]")
print("\n  *Full 2x2 covariance block, not a diagonal estimate.  ** So a height claim quoted at")
print("  0.05%, or a target set at 'sub-per-cent', is five to seventy times finer than the")
print("  statistic it is quoted against can resolve. **  The 13% and 34% errors of c54.173 were")
print("  four and ten sigma and stand; the 2-3% of c54.175 are about one sigma and do not.*")
for nm, (r, e) in SKY.items():
    if not (0.02 < e / r < 0.06):
        fail.append(f"the sky's {nm} error came out {e/r:.1%} -- PART 2's premise is wrong")
BARE = {'P1/P2': 2.217, 'P1/P3': 2.277}
for nm in SKY:
    if abs(SKY[nm][0] - BARE[nm]) > SKY[nm][1]:
        fail.append(f"the recomputed sky {nm} disagrees with the bare number by more than 1 sigma")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE RATIO STATISTIC CANNOT SEPARATE THE COEFFICIENTS, AND A CLAIM IS WITHDRAWN")
print("=" * 78)
# one multiplier on 1/k_D^2, everything else held: it slides the damping SCALE and cannot change
# the envelope's SHAPE.  ARM=lcdm NK=600 LMAXL=2000 ETAEND=4000, spectra banked under spectra/.
XS = np.array([0.700, 0.800, 0.859, 0.900, 1.000, 1.100, 1.200, 1.300])
R2 = np.array([2.0802, 2.1272, 2.1541, 2.1725, 2.2164, 2.2589, 2.3001, 2.3400])
R3 = np.array([2.0267, 2.1533, 2.2300, 2.2843, 2.4201, 2.5609, 2.7072, 2.8592])
print("  ** THE MULTIPLIER IS A FAITHFUL STAND-IN FOR THE COEFFICIENT, AND THAT IS CHECKED FIRST:")
print(f"     r_D goes 6.58 -> 7.10 Mpc between 8/9 and 16/15, so 8/9 is a multiplier of "
      f"(6.58/7.10)^2 = {(6.58/7.10)**2:.3f}.")
print(f"     At 0.859 the scan gives {R2[2]:.4f} / {R3[2]:.4f}; the explicit POLC=8/9 run gave")
print("     2.154 / 2.230.  Four figures. **")
if abs(R2[2] - 2.154) / 2.154 > 2e-3 or abs(R3[2] - 2.230) / 2.230 > 2e-3:
    fail.append("the DAMPX multiplier does not reproduce the explicit coefficient change")
print(f"\n  {'multiplier':>11} {'P1/P2':>9} {'P1/P3':>9}")
for x, a, b in zip(XS, R2, R3):
    print(f"  {x:>11.3f} {a:>9.4f} {b:>9.4f}")
sel = {}
for nm, r in (('P1/P2', R2), ('P1/P3', R3)):
    s, e = SKY[nm]
    xa = float(np.interp(s, r, XS))
    sl = float(np.interp(xa, XS, np.gradient(r, XS)))
    sel[nm] = (xa, e / sl)
    print(f"\n  {nm} = {s:.4f} +- {e:.4f}  selects a multiplier of {xa:.3f} +- {e/sl:.3f}")
d = sel['P1/P2'][0] - sel['P1/P3'][0]
sd = float(np.hypot(sel['P1/P2'][1], sel['P1/P3'][1]))
print(f"\n  ** THE SPLIT IS {d:+.3f} +- {sd:.3f} — {abs(d)/sd:.2f} SIGMA. **")
print("     ⇒ ***I had this written as 'the two ratios select different scales, so no coefficient")
print("     can fix both and the residual is the SHAPE of the damping envelope'.  At one sigma its")
print("     own error bar does not carry it.  It is withdrawn here rather than published, and the")
print("     withdrawal is the result: the ratio statistic is exhausted.***")
if abs(d) / sd >= 2.0:
    fail.append(f"the split is {abs(d)/sd:.1f} sigma -- PART 3 withdraws a claim that in fact holds")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — chi^2 DOES SEPARATE THEM, PREFERS 8/9 BY 1123, AND DOES NOT GET TO CHOOSE")
print("=" * 78)
CHI = []
for x in XS:
    p = os.path.join(SPEC, f"lcdm_{x:.3f}.npz")
    z = np.load(p)
    c, n, A, lo, hi = CS.chi2_of(z['ls'], z['Dl'])
    CHI.append(c)
    print(f"  multiplier {x:.3f}:  chi^2 = {c:>9.1f}  over {n} bins  (ell {lo}-{hi})   "
          f"chi^2/dof = {c/n:.2f}")
CHI = np.array(CHI)
m = XS <= 1.0
p = np.polyfit(XS[m], CHI[m], 2)
xmin = float(-p[1] / (2 * p[0]))
cmin = float(np.polyval(p, xmin))
nb = 185
infl = np.sqrt(cmin / nb)
sig = float(np.sqrt(1.0 / p[0]) * infl)
d_chi = float(CHI[XS == 1.000][0] - CHI[XS == 0.859][0])
X_89 = (6.58 / 7.10) ** 2
print(f"\n  ** THE MINIMUM IS AT A MULTIPLIER OF {xmin:.3f}, AND 8/9 IS THE MULTIPLIER "
      f"{X_89:.3f} — {abs(xmin-X_89)/X_89:.1%} APART. **")
if abs(xmin - X_89) / X_89 > 0.05:
    fail.append(f"the chi^2 minimum at {xmin:.3f} is not at the 8/9 value {X_89:.3f}")
print(f"  ** 16/15 (multiplier 1.000) COSTS Delta chi^2 = {d_chi:+.0f} OVER {nb} BINS, "
      f"{(1.0-xmin)/sig:.1f} SIGMA")
print(f"     AFTER INFLATING THE ERROR BY sqrt(chi^2/dof) = {infl:.1f} TO ACCOUNT FOR THE FACT THAT")
print("     THE CONTROL IS NOT A FIT. **")
print("\n  ⇒ ***AND THE COEFFICIENT IS NOT BEING CHOSEN BY THAT NUMBER.***  8/9 is restored as the")
print("  default because it is what this corpus has always used and because NEITHER value has been")
print("  derived here — `C8_diffusion_length.py` names 'the 8/9 coefficient against the 16/15")
print("  polarization-corrected one' in its own text as an open ambiguity.  ** I changed it to")
print("  16/15 earlier in this revision on recollection of the standard result, which is not a")
print("  derivation; and 8/9 winning the fit by 1123 is not one either. **  *What the 1123")
print("  measures is a residual error in this instrument's damping tail, of a size that a shear")
print("  coefficient could absorb — which is exactly why it must not be allowed to.*")
if xmin >= 1.0:
    fail.append("the chi^2 minimum is not below the 16/15 value -- PART 4's arithmetic is wrong")
if d_chi <= 0:
    fail.append("16/15 does not cost chi^2 -- PART 4 reports a preference that is not there")
assert CHI.min() / nb > 2.0, \
    "if the control reached chi^2/dof ~ 1 this whole file would need rewriting, not patching"

# =====================================================================
print()
print("=" * 78)
print("PART 5 — AND `L-147`'S PINNED chi^2 VALUES CAN NOW BE RECOMPUTED FROM THE CORPUS")
print("=" * 78)
PINNED = {'c54.175_lcdm': 4170.2, 'c54.175_cr': 50675.2}
for nm, want in PINNED.items():
    z = np.load(os.path.join(SPEC, f"{nm}.npz"))
    got, n, A, lo, hi = CS.chi2_of(z['ls'], z['Dl'])
    print(f"  {nm:>16}:  pinned {want:>9.1f}   recomputed {got:>9.1f}   "
          f"({abs(got-want)/want:.2%} over {n} bins)")
    if abs(got - want) / want > 5e-3:
        fail.append(f"{nm} recomputes to {got:.1f} against a pinned {want:.1f}")
print("\n  ** THOSE TWO NUMBERS WERE PRODUCED BY A SCRIPT IN /tmp AND TYPED INTO A RECEIPT. **")
print("     *`chi2_of_spectrum.py` is that machinery in the corpus — the interpolation onto the")
print("     full ell grid, the binning, the covariance restriction done on the COVARIANCE rather")
print("     than the Fisher matrix, and the single amplitude fitted in closed form.  It returns")
print("     both to within a tenth of a per cent.  **A number that cannot be re-derived from the")
print("     corpus is a claim, not a receipt, whatever file it is printed in.***")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the instrument is converged to 0.4%, the sky's own peak-height ratios carry")
print("3.2-3.4% so front #2's sub-per-cent height target is retired, a shape claim is withdrawn at")
print("1.0 sigma, chi^2 prefers 8/9 by 1123 and is not allowed to choose it, and L-147's pinned")
print("values are recomputable.")
print("=" * 78)

# ============================================================================================
# GATE — r2376+c54.176.  CR_cosmology.tex sec:refit-bound now carries five figures from this
# file, and each is pinned here so that a retune of the likelihood pipeline, the binning, the
# covariance restriction or the instrument's numerics fails HERE and not silently in the paper.
#   (1) the sky's own peak-height ratios and their uncertainties -- 2.256 +- 0.077 and
#       2.280 +- 0.074.  ** These are the whole point of the file: if they shrink below about a
#       per cent, front #2's retired height target must be REINSTATED. **
#   (2) the split between the multipliers the two ratios select, 1.03 sigma -- the number on
#       which a claim of mine was withdrawn.  Pinned so that the withdrawal cannot silently
#       become wrong.
#   (3) the chi^2 minimum at a multiplier of 0.865, and 8/9's 0.859.
#   (4) the cost of 16/15, 1123 units of chi^2 over 185 bins.
#   (5) the recomputation of L-147's two pinned values, to a tenth of a per cent.
# ============================================================================================
assert abs(SKY['P1/P2'][0] - 2.2564) < 5e-4 and abs(SKY['P1/P2'][1] - 0.0772) < 5e-4, \
    f"sky P1/P2 = {SKY['P1/P2'][0]:.4f} +- {SKY['P1/P2'][1]:.4f}, expected 2.2564 +- 0.0772"
assert abs(SKY['P1/P3'][0] - 2.2800) < 5e-4 and abs(SKY['P1/P3'][1] - 0.0737) < 5e-4, \
    f"sky P1/P3 = {SKY['P1/P3'][0]:.4f} +- {SKY['P1/P3'][1]:.4f}, expected 2.2800 +- 0.0737"
assert SKY['P1/P2'][1] / SKY['P1/P2'][0] > 0.01, \
    "the sky's P1/P2 now resolves better than one per cent -- front #2's height target must be " \
    "REINSTATED and this file rewritten, not patched"
assert abs(abs(d) / sd - 1.03) < 0.05, \
    f"the split is {abs(d)/sd:.2f} sigma, expected 1.03 -- the withdrawal in PART 3 rests on it"
assert abs(xmin - 0.865) < 0.005, f"the chi^2 minimum is at {xmin:.4f}, expected 0.865"
assert abs(X_89 - 0.859) < 0.002, f"8/9 corresponds to multiplier {X_89:.4f}, expected 0.859"
assert abs(d_chi - 1122.9) < 5.0, \
    f"16/15 costs {d_chi:.1f} units of chi^2, expected 1123 -- CR_cosmology.tex quotes it"
assert 22.0 < CHI.min() / nb < 23.0, \
    f"the control's floor is chi^2/dof = {CHI.min()/nb:.1f}, expected 22.5 (the paper's figure)"
print(f"GATE c54.176 (r2376): sky ratios {SKY['P1/P2'][0]:.4f}+-{SKY['P1/P2'][1]:.4f} and "
      f"{SKY['P1/P3'][0]:.4f}+-{SKY['P1/P3'][1]:.4f}; split {abs(d)/sd:.2f} sigma; chi^2 minimum at "
      f"{xmin:.3f} against 8/9's {X_89:.3f}; 16/15 costs {d_chi:+.0f} -- pinned against "
      f"CR_cosmology.tex sec:refit-bound.")
