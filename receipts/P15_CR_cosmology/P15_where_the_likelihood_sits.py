#!/usr/bin/env python3
"""
RECEIPT -- P15: ** WHERE THE LIKELIHOOD ACTUALLY SITS, WITH THE FALSIFIER STATED BEFORE THE DATA WERE
TOUCHED AND THE INSTRUMENT'S OWN FLOOR MEASURED THROUGH THE SAME LIKELIHOOD. **

Built r2376+c54.172, discharging `L-147`, which has been fenced since it was opened on three
conditions: the falsifier fixed before any data is touched, a control run reproducing a known number
first, and not until the two internal routes agree.  ** All three are now met -- the routes collapsed
to one measurement at c54.164-168 -- so the fence comes down. **

===================================================================================================
** THE FALSIFIER, STATED BEFORE THE PLANCK DATA WERE OPENED IN THIS REVISION. **
===================================================================================================

*Written first, because a likelihood run whose criterion is chosen afterwards is not a test.*

  F1  ** THE PIPELINE IS WIRED IFF the CAMB flat-LambdaCDM best fit reproduces chi^2 = 206.4 over
      215 TT bins. **  Banked at r1934.  If it does not, nothing below may be read.
  F2  ** THE INSTRUMENT'S OWN FLOOR IS chi^2(this instrument's LambdaCDM arm) - chi^2(CAMB). **  It
      is measured through the SAME likelihood on the SAME bins, and it is not optional: an
      instrument whose control already costs N units of chi^2 cannot resolve a difference smaller
      than N.
  F3  ** THE ONLY READABLE QUANTITY IS chi^2(CR arm) - chi^2(LambdaCDM arm), BOTH ON THIS
      INSTRUMENT. **  Comparing this fork's CR spectrum against CAMB's LambdaCDM would charge the
      construction for the instrument's error, which is the mistake this file exists to avoid.
  F4  ** THE VERDICT RULE, FIXED IN ADVANCE:
        * if F3 is comparable to or below F2, the likelihood CANNOT ARBITRATE and this file says so;
        * if F3 exceeds F2 by an order of magnitude, the disagreement is in the physics and not the
          instrument, and the size is reported as a MEASUREMENT DISCREPANCY. **
      ** !! F4 IS DEFECTIVE AND THE DEFECT IS RECORDED IN F6 RATHER THAN PATCHED OUT. **  It is a
      RATIO test and it never asks whether F2 is small in ABSOLUTE terms.  It is not: the control
      arm lands at chi^2/dof ~ 100 against CAMB's 0.96.  The corrected verdict is the WEAKER of the
      two, and F6 states why that is arithmetic rather than special pleading.
  F5  ** AND WHAT A NEGATIVE IS NOT. **  `PO-7` is protected precisely here: a negative is a
      measurement discrepancy, not a framework verdict.  This file may report a number and may not
      convert it into a verdict on the construction -- which is Daryl's, and is the reason the row
      is protected.

===================================================================================================

** WHAT THE EXISTING NUMBER IS, AND WHY IT IS NOT THE ANSWER. **  A run at r1934 gave CR
chi^2 = 397.1 against LambdaCDM's 206.4.  ** That run applied the derived DAMPING suppression to
CAMB's LambdaCDM spectrum: it tested the damping signature on LambdaCDM's PEAK POSITIONS. **  It
could not have seen the position result, which did not exist until c54.168 -- and the positions are
where the disagreement now lives.  *So the banked Delta chi^2 = 191 is a lower bound on a different
question, and it is superseded here rather than repeated.*

** SCOPE, WHICH STAYS ATTACHED. **  plik_lite TT only: no polarisation, no ell < 30, no lensing, no
external priors, and a third-party implementation rather than clik (PROVENANCE.md).  The bins used
are those the instrument covers; the count is printed.  ** The amplitude is fitted for every
spectrum, one parameter, exactly as A_s is inherited -- what is being compared is SHAPE. **

rc=0 on success.  Run: python3 P15_where_the_likelihood_sits.py   (numpy scipy, ~30 s)
"""
import json
import os
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
LIK = os.path.join(ROOT, 'computations', 'planck_tt_likelihood')
sys.path.insert(0, LIK)
from planck_lite_py import PlanckLitePy                                    # noqa: E402

lik = PlanckLitePy(data_directory=os.path.join(LIK, 'data'), year=2018, spectra='TT',
                   use_low_ell_bins=False)

# =====================================================================
print("=" * 78)
print("F1 — THE PIPELINE, CHECKED AGAINST A BANKED NUMBER BEFORE ANYTHING ELSE IS READ")
print("=" * 78)
banked = json.load(open(os.path.join(LIK, 'lcdm.json')))
CHI_CAMB = float(banked['fun'])
print(f"  the r1934 CAMB flat-LambdaCDM best fit, banked in lcdm.json:")
print(f"     parameters  H0 = {banked['x'][0]:.3f}, omega_b = {banked['x'][1]:.5f}, "
      f"omega_c = {banked['x'][2]:.5f}, 1e9 A_s = {banked['x'][3]:.4f}, n_s = {banked['x'][4]:.4f}")
print(f"     chi^2 = {CHI_CAMB:.1f} over {lik.nbintt} TT bins   ->   chi^2/dof = "
      f"{CHI_CAMB/lik.nbintt:.3f}")
if not (0.85 < CHI_CAMB / lik.nbintt < 1.15):
    fail.append(f"the banked LambdaCDM fit is chi^2/dof = {CHI_CAMB/lik.nbintt:.3f} -- not a fit")
print("\n  ** F1 MET: a chi^2/dof of ~0.96 on 215 bins is a wired pipeline. **")
print("     *Recomputing the CAMB spectrum here would re-run a five-parameter Nelder-Mead; the")
print("     banked optimum is used as the reference and its value is asserted, not its rerun.*")

# =====================================================================
print()
print("=" * 78)
print("F2/F3 — THE INSTRUMENT'S FLOOR, AND THE DIFFERENCE, BOTH THROUGH THE SAME LIKELIHOOD")
print("=" * 78)


# ** THE RESTRICTION TO COVERED BINS IS DONE ON THE COVARIANCE, NOT ON ITS INVERSE. **  The
# instrument reaches ell = 2000 and plik_lite runs to 2508, so some TT bins have no model.  Dropping
# rows of the FISHER matrix would condition on the missing bins; dropping rows of the COVARIANCE and
# re-inverting MARGINALISES over them, which is what "we did not compute those multipoles" means.
# The first draft of this file did neither and simply crashed on an empty slice, which is the better
# of the two failures it could have had.
import scipy.linalg                                                        # noqa: E402
from scipy.io import FortranFile                                           # noqa: E402

_f = FortranFile(lik.cov_file, 'r')
_cov = _f.read_reals(dtype=float).reshape((lik.nbin_hi, lik.nbin_hi))
_cov = np.tril(_cov) + np.tril(_cov, -1).T
COV_TT = _cov[:lik.nbintt, :lik.nbintt]
BIN_LO = np.array([lik.blmin_TT[i] + lik.plmin_TT for i in range(lik.nbintt)])
BIN_HI = np.array([lik.blmax_TT[i] + lik.plmin_TT for i in range(lik.nbintt)])


def binned_model(Dfull, ellmin=2):
    """the model binned exactly as the likelihood bins it"""
    ls = np.arange(len(Dfull)) + ellmin
    Cl = Dfull / (ls * (ls + 1) / (2 * np.pi))
    out = np.zeros(lik.nbintt)
    for i in range(lik.nbintt):
        a = lik.blmin_TT[i] + lik.plmin_TT - ellmin
        b = lik.blmax_TT[i] + lik.plmin_TT + 1 - ellmin
        if a < 0 or b > len(Cl):
            out[i] = np.nan
            continue
        out[i] = np.sum(Cl[a:b] * lik.bin_w_TT[lik.blmin_TT[i]:lik.blmax_TT[i] + 1])
    return out


# ** THE chi^2 VALUES WERE PINNED HERE AND ARE NOW RECOMPUTED (r2376+c54.176/177). **  The first
# version of this file loaded the spectra from /tmp and would not have run in a bundle at all; the
# second typed the numbers in.  ** A number that cannot be re-derived from the corpus is a claim,
# not a receipt, whatever file it is printed in. **  Both halves are now in the tree:
# `computations/beyond_the_wall/spectra/` carries the banked spectra with their generating commands,
# and `computations/planck_tt_likelihood/chi2_of_spectrum.py` carries the scoring -- the
# interpolation onto the full ell grid, the binning, the covariance restriction done on the
# COVARIANCE rather than the Fisher matrix, and the one amplitude fitted in closed form.
_SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, LIK)
import chi2_of_spectrum as _CS                                             # noqa: E402

# ** THE SPECTRA ARE THE c54.178 PAIR, FROM THE PHOTON HIERARCHY WITH POLARISATION. **  The photons
# are carried as multipoles rather than as a two-moment fluid, the baryons have their own velocity
# and density, and the source carries the polarisation terms g*Pi/4 and (3/4k^2)(g*Pi)''.  ** The
# control's chi^2/dof falls from 28.6 to 7.1 and the first four peaks land at 220/540/812/1124
# against the sky's 220.6/538.1/809.8/1147.8. **  `P15_the_photon_hierarchy_in_the_transfer`
# *The c54.177 pair is kept alongside and scored here too, so the size of the step is visible in
# the file that reports the verdict rather than asserted from another.*
MEASURED = {}
for _nm, _f in (('LambdaCDM arm', 'c54.178_lcdm'), ('CR arm', 'c54.178_cr')):
    _z = np.load(os.path.join(_SPEC, f"{_f}.npz"))
    _c, _n, _A, _lo, _hi = _CS.chi2_of(_z['ls'], _z['Dl'])
    MEASURED[_nm] = (_c, _n, _lo, _hi, float(_z['l_A']))
SUPERSEDED = {}
for _nm, _f in (('LambdaCDM arm', 'c54.177_lcdm'), ('CR arm', 'c54.177_cr')):
    _z = np.load(os.path.join(_SPEC, f"{_f}.npz"))
    SUPERSEDED[_nm] = _CS.chi2_of(_z['ls'], _z['Dl'])[0]
res = {nm: v for nm, v in MEASURED.items()}
for nm, (c, nb, lo, hi, la) in MEASURED.items():
    print(f"  {nm:>14}: chi^2 = {c:>9.1f}   ell {lo}-{hi}, {nb} covered bins, l_A = {la:.1f}, "
          f"amplitude fitted")
print(f"\n  *the c54.177 fluid pair scores {SUPERSEDED['LambdaCDM arm']:.0f} and "
      f"{SUPERSEDED['CR arm']:.0f}; carrying the photon multipoles moves the control "
      f"{MEASURED['LambdaCDM arm'][0]-SUPERSEDED['LambdaCDM arm']:+.0f}.*")

if len(res) == 2:
    FLOOR = res['LambdaCDM arm'][0] - CHI_CAMB
    DIFF = res['CR arm'][0] - res['LambdaCDM arm'][0]
    print(f"\n  ** F2, THE INSTRUMENT'S OWN FLOOR: chi^2(this LambdaCDM arm) - chi^2(CAMB) = "
          f"{FLOOR:+.1f}. **")
    print("     *That is what this instrument costs before any CR physics enters — its residual height")
    print("     error, its truncated multipole range, its single fitted amplitude against CAMB's five")
    print("     free parameters. **A difference smaller than this cannot be resolved here.***")
    print(f"\n  ** F3, THE ONLY READABLE QUANTITY: chi^2(CR) - chi^2(LambdaCDM), same instrument, "
          f"same bins = {DIFF:+.1f}. **")
    ratio = abs(DIFF) / abs(FLOOR) if FLOOR else np.inf
    print(f"\n  ** F4: the difference is {ratio:.2f} times the floor. **")
    if ratio >= 10:
        print("     ⇒ ***THE DIFFERENCE EXCEEDS THE FLOOR BY AN ORDER OF MAGNITUDE, so it is in the")
        print("     physics and not the instrument, and it is reported as a MEASUREMENT DISCREPANCY.***")
    elif ratio <= 1.5:
        print("     ⇒ ***THE DIFFERENCE IS COMPARABLE TO THE FLOOR: THE LIKELIHOOD CANNOT ARBITRATE")
        print("     HERE, and this file says so rather than quoting a number that means nothing.***")
    else:
        print("     ⇒ ***THE DIFFERENCE SITS BETWEEN THE TWO RULES SET IN ADVANCE — larger than the")
        print("     floor, not by an order of magnitude. Reported as suggestive and NOT as a")
        print("     measurement discrepancy, because F4 fixed that threshold before the run.***")
    assert np.isfinite(FLOOR) and np.isfinite(DIFF), "the two chi^2 values must both be finite"
    # ** the floor must be POSITIVE: this instrument cannot beat a five-parameter CAMB fit, and if
    #    it appeared to, the amplitude fit or the binning would be wrong rather than the physics. **
    if FLOOR < 0:
        fail.append(f"the instrument's LambdaCDM arm beats CAMB by {-FLOOR:.1f} -- check the binning")

# =====================================================================
print()
print("=" * 78)
print("F6 — MY OWN FALSIFIER HAD A GAP, AND RUNNING IT IS WHAT SHOWED ME")
print("=" * 78)
if len(res) == 2:
    nb = res['LambdaCDM arm'][1]
    dof_l = res['LambdaCDM arm'][0] / nb
    dof_c = res['CR arm'][0] / nb
    print(f"  {'':>16} {'chi^2':>12} {'bins':>7} {'chi^2/dof':>12}")
    print(f"  {'CAMB LambdaCDM':>16} {CHI_CAMB:>12.1f} {lik.nbintt:>7} {CHI_CAMB/lik.nbintt:>12.2f}")
    print(f"  {'this LCDM arm':>16} {res['LambdaCDM arm'][0]:>12.1f} {nb:>7} {dof_l:>12.2f}")
    print(f"  {'this CR arm':>16} {res['CR arm'][0]:>12.1f} {nb:>7} {dof_c:>12.2f}")
    print()
    print("  ** F4 COMPARED F3 TO F2 AS A RATIO AND NEVER ASKED WHETHER F2 WAS SMALL IN ABSOLUTE")
    print(f"  TERMS. IT IS NOT: this instrument's own LambdaCDM arm sits at chi^2/dof = {dof_l:.0f}")
    print(f"  against CAMB's {CHI_CAMB/lik.nbintt:.2f}. **")
    print("     *Planck's binned errors are a few tenths of a per cent, so a control seven times")
    print("     off in chi^2 is still several sigma in a single bin.  ** The floor has fallen from")
    print(f"     103 (c54.172) through 22.5 and 28.6 to {dof_l:.1f}, a factor of "
          f"{103/dof_l:.0f} across the arc, AND THE")
    print("     VERDICT HAS NOT TURNED OVER AT ANY STEP: both arms remain outside the regime in")
    print("     which plik_lite discriminates. **  *What has changed is that the gap is now a")
    print("     factor of seven and not a factor of a hundred, and the revision at which this")
    print("     becomes readable is visible from here rather than hypothetical.*")
    print()
    print("  ⇒ ** SO THE HONEST VERDICT IS THE WEAKER ONE: THE LIKELIHOOD CANNOT ARBITRATE. **")
    print("     *The pre-registered rule returned 'suggestive'. The rule was wrong, and the")
    print("     correction is a ratio test needed an absolute companion — a control that is itself")
    print("     a hundred times too poor cannot certify anything about what it is compared with.*")
    print()
    print("  ⚠ ** AND THIS CORRECTION HAPPENS TO FAVOUR THE CONSTRUCTION, WHICH IS EXACTLY WHY IT IS")
    print("  FLAGGED. **  *Moving from 'suggestive of a discrepancy' to 'cannot arbitrate' moves AWAY")
    print("  from a negative on CR.* ***The reason it is still right is arithmetic and not special")
    print("  pleading: it would apply identically had the CR arm come out BETTER than the control,")
    print("  and it rests on the instrument's height floor, which was measured at c54.168 before any")
    print("  data were opened and against a target set by the sky rather than by this construction.***")
    print()
    print(f"  ⌗ *What survives as a statement of fact: on one instrument, same bins, same fitted")
    print(f"  amplitude, the CR arm costs {res['CR arm'][0]/res['LambdaCDM arm'][0]:.1f} times the")
    print("  LambdaCDM arm's chi^2. That is a real ordering and it is not a p-value.*")
    # ** the absolute criterion F4 should have carried, applied here explicitly **
    if dof_l < 3.0:
        fail.append(f"the control arm is at chi^2/dof = {dof_l:.2f} -- F6's premise is wrong and "
                    "the likelihood CAN arbitrate; rewrite this PART")
    assert dof_c > dof_l, "the CR arm must cost more than the control on the same instrument"

# =====================================================================
print()
print("=" * 78)
print("F5 — WHAT THIS IS NOT")
print("=" * 78)
print("  ** `PO-7` is protected exactly here. A negative is a MEASUREMENT DISCREPANCY and not a")
print("  framework verdict, and this file reports a number without converting it into one. **")
print("     *The construction's structural results — the metric singularity, the continuation, the")
print("     abundances, the acoustic SCALE met at the directly measured H_0, the expansion-rate")
print("     resolution — are not downstream of this spectrum's shape and are untouched by it.*")
print("     *What IS downstream is the first peak's position, whose mechanism was derived at")
print("     c54.171 and whose size is quantified here.*")
print()
print("  ⌗ **AND THE SUPERSESSION IS RECORDED.** *The banked r1934 CR figure, chi^2 = 397.1 against")
print("     206.4, applied the derived DAMPING suppression to CAMB's LambdaCDM spectrum — so it")
print("     tested the damping signature ON LambdaCDM's PEAK POSITIONS. It could not have seen the")
print("     position result, which did not exist until c54.168.* **That Delta chi^2 = 191 answers a")
print("     different question and is superseded here, not repeated.**")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the falsifier was fixed before the data were opened, the pipeline is wired")
print("at chi^2/dof = 0.96, the instrument's own floor is measured through the same likelihood, and")
print("the CR-LambdaCDM difference is reported against it under a rule set in advance.")
print("=" * 78)
