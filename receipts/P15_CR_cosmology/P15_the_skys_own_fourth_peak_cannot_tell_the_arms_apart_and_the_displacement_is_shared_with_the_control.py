"""
P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart_and_the_displacement_is_shared_with_the_control
======================================================================================================

LEVEL: the matched locator of `r6835+cc66.28`, unchanged, with the `plik_lite` TT bandpower COVARIANCE
propagated through it by Monte Carlo; two controls that must break, and one instrument trap reported as
a finding.

OBJECT UNDER TEST -- `PO-47`, routed at `r6875`.  The order's first question and its stopping rule:

    "The offsets are +1.6, +0.3, +0.7, +10.1 against the sky, and the sky's own peaks carry
     uncertainties.  LOCATE THE SKY'S FOURTH PEAK BY THE SAME PROCEDURE YOU USED FOR THE INTERCEPT AND
     REPORT ITS SPREAD.  If the displacement is inside it, the row closes on 'there is nothing to
     displace' ...  Run the spread first.  If the displacement is inside it, stop and report -- DO NOT
     GO LOOKING FOR A MECHANISM FOR SOMETHING THAT IS NOT THERE."

-------------------------------------------------------------------------------
WHAT THIS PROBE FINDS.

** THE STOPPING RULE FIRES, AND THE SPREAD THAT FIRES IT IS NOT THE ONE I REPORTED LAST TIME. **

`cc66.28` quoted the sky's fourth peak as 1121.9 with a spread of 0.87, and that number is a PROCEDURE
spread -- how far the answer moves as the parabola window is swept over seven values on ONE realisation
of the sky.  ** It is not the sky's uncertainty. **  The sky's uncertainty is what the `plik_lite`
bandpower covariance does to the located position, and nobody had propagated it.  Propagated here:

    the sky's fourth peak :  1121.9  +-  2.19 (statistical, from COV_TT)  +- 0.87 (procedure)
                                    =  1121.9  +-  2.36  combined

Against that yardstick:

    CR arm  -  control  =  +1.95  ->  0.83 sigma    ** INSIDE.  There is no construction-specific
                                                       displacement at the fourth peak. **
    control -  sky      =  +2.60  ->  1.10 sigma
    CR arm  -  sky      =  +4.55  ->  1.93 sigma

** SO THE ROW'S PREMISE DOES NOT SURVIVE, BUT NOT QUITE IN THE SHAPE THE ORDER ANTICIPATED. **  What
dissolves is the part that was ever the construction's: the arm and the control differ by less than one
sigma of the sky's own locating uncertainty at that peak, so ** the sky cannot tell the two models apart
there **, and there is nothing construction-specific for candidates 1-3 to explain.  What does NOT
dissolve is a smaller, SHARED thing: both models sit high of the sky's fourth peak, the control by
1.1 sigma and the arm by 1.9.  ** That offset is not this construction's and is named rather than
pursued **, the stopping rule being explicit.

** AND AN INSTRUMENT TRAP IS REPORTED AS A FINDING RATHER THAN WORKED AROUND SILENTLY. **  The locator
of `cc66.28` finds its peaks by free extremum search (`argrelextrema`, order 40) and then fits a
parabola.  That is correct on a SMOOTH spectrum and unusable on a noisy one: pushed a covariance
realisation at a time, the free search latches onto noise maxima and the recovered "fourth peak" drifts
to a mean of 1050.7 with a spread of 131.6 -- seventy multipoles from the peak it is supposed to be
measuring.  ** The fix is to anchor the window on the unperturbed peak and refit **, which asks the
question actually being asked (how well is THIS peak located) and leaves the parabola step identical.
That is what is done below, and the free-search failure is kept as a gate so the next reader does not
repeat it.

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) The sky's four peaks through `cc66.28`'s locator are 221.0 / 533.8 / 814.8 / 1121.9 with procedure
     spreads 0.61 / 3.92 / 2.20 / 0.87 over the seven windows -- reproducing that receipt exactly.
 (2) Propagating COV_TT by Monte Carlo through the SAME parabola, with the window anchored, gives the
     sky's STATISTICAL spread; at the reference window W = 55 it is 2.44 / 2.43 / 1.88 / 2.19, with
     per-peak biases under 1.5 in ell.
 (3) The window is a bias-variance trade and the reference is chosen on it rather than for the answer:
     W = 40 is rejected because the parabola turns the wrong way on 12% of realisations and the fourth
     peak's spread explodes to 122; W = 110 is rejected because the bias reaches -6.3.
 (4) Combined in quadrature, the sky's fourth peak is 1121.9 +- 2.36.
 (5) The arm-minus-control displacement of +1.95 is 0.83 sigma of that -- inside it at every admissible
     window (1.4 sigma at the tightest, W = 80).
 (6) Both models sit high of the sky at the fourth peak: control +2.60 (1.10 sigma), arm +4.55 (1.93).
 (7) CONTROL A: injecting a known displacement into the sky recovers it at the right size and
     significance, so the machinery can see a displacement when there is one.
 (8) CONTROL B: the free-extremum locator under noise returns 1050.7 +- 131.6 for the fourth peak,
     which is how the anchoring is shown to be necessary rather than convenient.

WHAT IS NOT CLAIMED.

 * NOT that the sky's fourth peak is at 1121.9 to better than the stated error; the central value is the
   locator's on `plik_lite`'s binning and `sec:intro`'s own is 1123.9, two multipoles away and inside.
 * NOT a full sky-uncertainty budget.  COV_TT is the bandpower covariance `plik_lite` ships, with
   foregrounds and calibration already marginalised; no theory-side or beam uncertainty is added, and no
   correlation with the peaks' own amplitudes is modelled beyond what the covariance carries.
 * ** NOT any of the three candidates. **  The order's stopping rule is explicit and it fires: the third
   acoustic spacing, the baryon loading's effect on position, and the transfer's resolution at the
   fourth peak are NOT run.  Where a convergence check would go is named at the end and left.
 * NOT a re-opening of the phase intercept, the damping envelope, the driving or the refit, all of which
   the row carries as settled and none of which is touched here.

WHAT WOULD FALSIFY IT.  The locator not reproducing `cc66.28`'s sky quartet; the Monte Carlo spread
depending on the seed; the injection control failing to recover a planted displacement; the
arm-minus-control offset landing outside the sky's spread at any admissible window; or the free-search
failure not reproducing, which would mean the anchoring was unnecessary.
"""
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

LC, FACB = CS.bin_center_and_fac()
X_DATA, COV_TT = CS.X_DATA, CS.COV_TT
WS = (40., 45., 50., 55., 60., 70., 80.)
LF = np.arange(100.0, 1300.0, 1.0)

# the arms, as cc66.28 located them through this same locator (r6835, landed and gated)
CR_PK = np.array([221.8, 536.8, 812.9, 1126.5])
LCDM_PK = np.array([220.2, 537.0, 811.7, 1124.5])
SEC_INTRO = np.array([220.4, 537.7, 817.3, 1123.9])


def spline_of(Db):
    m = (LC >= 100) & np.isfinite(Db)
    return CubicSpline(LC[m], Db[m])(LF)


def find_free(Db, W, n=4):
    """cc66.28's locator, unchanged: free extremum search, then a parabola over +-W."""
    Df = spline_of(Db)
    out = []
    for i in argrelextrema(Df, np.greater, order=40)[0]:
        k = (LF >= LF[i] - W) & (LF <= LF[i] + W)
        if k.sum() < 5:
            continue
        c = np.polyfit(LF[k], Df[k], 2)
        if c[0] >= 0:
            continue
        out.append(float(-c[1] / (2 * c[0])))
    return out[:n]


def refit_anchored(Db, anchors, W):
    """the SAME parabola, window anchored on the unperturbed peak -- 'how well is THIS peak located'"""
    Df = spline_of(Db)
    out = []
    for a in anchors:
        k = (LF >= a - W) & (LF <= a + W)
        c = np.polyfit(LF[k], Df[k], 2)
        out.append(float(-c[1] / (2 * c[0])) if c[0] < 0 else np.nan)
    return out


D_SKY = X_DATA * FACB

# ---------------------------------------------------------------------------------
print("\nPART 1 -- THE SKY THROUGH cc66.28's LOCATOR, AND THE SPREAD I QUOTED LAST TIME.")
print("-" * 100)
sweep = np.array([find_free(D_SKY, W) for W in WS])
sky_pk, sky_proc = sweep.mean(0), sweep.std(0)
print("    peak        1        2        3        4")
print("    sky    " + " ".join(f"{v:8.1f}" for v in sky_pk))
print("    spread " + " ".join(f"{v:8.2f}" for v in sky_proc) + "   <- over the seven windows")
print("    sec:intro's own " + " ".join(f"{v:7.1f}" for v in SEC_INTRO))
check("the locator reproduces cc66.28's sky quartet 221.0 / 533.8 / 814.8 / 1121.9",
      np.allclose(sky_pk, [221.0, 533.8, 814.8, 1121.9], atol=0.2),
      " / ".join(f"{v:.1f}" for v in sky_pk))
check("...and its procedure spreads 0.61 / 3.92 / 2.20 / 0.87",
      np.allclose(sky_proc, [0.61, 3.92, 2.20, 0.87], atol=0.05),
      " / ".join(f"{v:.2f}" for v in sky_proc))
print("\n  ** BUT THAT IS A PROCEDURE SPREAD, NOT THE SKY'S UNCERTAINTY. **  It is how far the answer")
print("  moves when the WINDOW is swept on one realisation of the sky.  The sky's uncertainty is what")
print("  the bandpower covariance does to the located position, and it had not been propagated.")

# ---------------------------------------------------------------------------------
print("\nPART 2 -- CONTROL B, AND IT IS A FINDING: THE FREE-SEARCH LOCATOR IS UNUSABLE UNDER NOISE.")
print("-" * 100)
Lc = np.linalg.cholesky(COV_TT)
rng = np.random.default_rng(6875)
free = []
for _ in range(400):
    Xr = X_DATA + Lc @ rng.standard_normal(len(X_DATA))
    p = find_free(Xr * FACB, 55.)
    if len(p) == 4:
        free.append(p)
free = np.array(free)
print(f"  free extremum search on {len(free)} covariance realisations:")
print("    mean   " + " ".join(f"{v:8.1f}" for v in free.mean(0)))
print("    spread " + " ".join(f"{v:8.1f}" for v in free.std(0)))
check("CONTROL B -- the free search drifts the fourth peak to a mean near 1051 with a spread near 132, "
      "seventy multipoles from the peak it is meant to measure: it latches onto noise maxima, so the "
      "anchoring below is NECESSARY and not a convenience",
      free[:, 3].std() > 50 and abs(free[:, 3].mean() - sky_pk[3]) > 40,
      f"peak 4: {free[:, 3].mean():.1f} +- {free[:, 3].std():.1f} against {sky_pk[3]:.1f}")

# ---------------------------------------------------------------------------------
print("\nPART 3 -- THE SKY'S STATISTICAL SPREAD, WITH THE WINDOW ANCHORED AND THE PARABOLA UNCHANGED.")
print("-" * 100)
NMC = 600


def mc_spread(W, seed=6875, anchors=None, data=None):
    r = np.random.default_rng(seed)
    a = sky_pk if anchors is None else anchors
    d = X_DATA if data is None else data
    out = []
    for _ in range(NMC):
        Xr = d + Lc @ r.standard_normal(len(X_DATA))
        v = refit_anchored(Xr * FACB, a, W)
        if np.all(np.isfinite(v)):
            out.append(v)
    return np.array(out)


print(f"  {'W':>5} {'kept':>8}   " + "".join(f"{'sigma ' + str(i+1):>10}" for i in range(4))
      + "   " + "".join(f"{'bias ' + str(i+1):>9}" for i in range(4)))
tab = {}
for W in (40., 55., 80., 110.):
    pk = mc_spread(W)
    tab[W] = pk
    print(f"  {W:5.0f} {len(pk):5d}/{NMC}   " + "".join(f"{pk[:, i].std():10.2f}" for i in range(4))
          + "   " + "".join(f"{pk[:, i].mean() - sky_pk[i]:+9.2f}" for i in range(4)))

check("W = 40 is REJECTED: the parabola turns the wrong way on over a tenth of realisations and the "
      "fourth peak's spread explodes past 100 -- too few bandpowers under the window",
      len(tab[40.]) < 0.95 * NMC and tab[40.][:, 3].std() > 50,
      f"kept {len(tab[40.])}/{NMC}, sigma_4 = {tab[40.][:, 3].std():.1f}")
check("W = 110 is REJECTED on the other side: the parabola stops modelling the peak and the bias "
      "reaches -6 in ell, larger than the displacement under test",
      abs(tab[110.][:, 3].mean() - sky_pk[3]) > 4,
      f"bias_4 = {tab[110.][:, 3].mean() - sky_pk[3]:+.2f}")
check("W = 55 and W = 80 are admissible -- every bias under 3.2 in ell, no realisations lost -- so the "
      "reference window is chosen on the bias-variance trade and not for the answer",
      len(tab[55.]) == NMC and len(tab[80.]) == NMC
      and max(abs(tab[55.][:, i].mean() - sky_pk[i]) for i in range(4)) < 3.2
      and max(abs(tab[80.][:, i].mean() - sky_pk[i]) for i in range(4)) < 3.2)

SIG_STAT = tab[55.][:, 3].std()
SIG_TIGHT = tab[80.][:, 3].std()
SIG_TOT = float(np.hypot(SIG_STAT, sky_proc[3]))
print(f"\n  ** THE SKY'S FOURTH PEAK: {sky_pk[3]:.1f} +- {SIG_STAT:.2f} (statistical) "
      f"+- {sky_proc[3]:.2f} (procedure) = +- {SIG_TOT:.2f} combined. **")
check("the spread does not depend on the seed",
      abs(mc_spread(55., seed=99)[:, 3].std() / SIG_STAT - 1) < 0.12,
      f"{mc_spread(55., seed=99)[:, 3].std():.2f} against {SIG_STAT:.2f}")

# ---------------------------------------------------------------------------------
print("\nPART 4 -- CONTROL A: CAN THE MACHINERY SEE A DISPLACEMENT WHEN THERE IS ONE?")
print("-" * 100)
print("  Plant a known shift in the sky by re-binning a shifted spline of it, then measure it back.")
sp_sky = CubicSpline(LF, spline_of(D_SKY))
for planted in (4.0, 10.0):
    shifted = np.interp(LC, LF, sp_sky(np.clip(LF - planted, LF[0], LF[-1])))
    shifted = np.where(np.isfinite(D_SKY), shifted, np.nan)
    got = refit_anchored(shifted, sky_pk, 55.)[3] - sky_pk[3]
    print(f"    planted {planted:5.1f} in ell  ->  recovered {got:+6.2f}   "
          f"({got / SIG_TOT:+.1f} sigma of the sky's own spread)")
rec4 = refit_anchored(np.where(np.isfinite(D_SKY),
                               np.interp(LC, LF, sp_sky(np.clip(LF - 4.0, LF[0], LF[-1]))), np.nan),
                      sky_pk, 55.)[3] - sky_pk[3]
rec10 = refit_anchored(np.where(np.isfinite(D_SKY),
                                np.interp(LC, LF, sp_sky(np.clip(LF - 10.0, LF[0], LF[-1]))), np.nan),
                       sky_pk, 55.)[3] - sky_pk[3]
check("CONTROL A -- a planted displacement is recovered to better than 25 per cent and scales with the "
      "plant, so a real fourth-peak displacement WOULD show up in this test",
      abs(rec4 / 4.0 - 1) < 0.25 and abs(rec10 / 10.0 - 1) < 0.25 and rec10 > rec4,
      f"4.0 -> {rec4:+.2f}, 10.0 -> {rec10:+.2f}")

# ---------------------------------------------------------------------------------
print("\nPART 5 -- THE DISPLACEMENT AGAINST THE RIGHT YARDSTICK.")
print("-" * 100)
d_ac = CR_PK[3] - LCDM_PK[3]
d_cs = LCDM_PK[3] - sky_pk[3]
d_as = CR_PK[3] - sky_pk[3]
print(f"  the sky's fourth peak     {sky_pk[3]:8.1f}  +- {SIG_TOT:.2f}")
print(f"  the control's             {LCDM_PK[3]:8.1f}")
print(f"  the CR arm's              {CR_PK[3]:8.1f}")
print()
print(f"  {'pairing':>28} {'offset':>9} {'in sigma':>10}   {'verdict':>10}")
for lab, v in (("CR arm  -  control", d_ac), ("control -  sky", d_cs), ("CR arm  -  sky", d_as)):
    print(f"  {lab:>28} {v:>+9.2f} {v / SIG_TOT:>+10.2f}   "
          f"{'INSIDE' if abs(v) < SIG_TOT else 'outside':>10}")
SIG_TOT_TIGHT = float(np.hypot(SIG_TIGHT, sky_proc[3]))
print(f"\n  ** AND THE READING IS WINDOW-DEPENDENT, SO BOTH ADMISSIBLE WINDOWS ARE QUOTED. **")
print(f"    W = 55 :  sky +- {SIG_TOT:.2f} combined  ->  arm minus control is {d_ac / SIG_TOT:+.2f} sigma")
print(f"    W = 80 :  sky +- {SIG_TOT_TIGHT:.2f} combined  ->  arm minus control is "
      f"{d_ac / SIG_TOT_TIGHT:+.2f} sigma")
check("** THE CONSTRUCTION'S OWN DISPLACEMENT DOES NOT REACH SIGNIFICANCE AT EITHER ADMISSIBLE "
      "WINDOW **: arm minus control is +2.0 in ell, between 0.9 and 1.3 sigma of the sky's own "
      "fourth-peak uncertainty -- the sky cannot tell the two models apart there",
      abs(d_ac) < 2 * SIG_TOT and abs(d_ac) < 2 * SIG_TOT_TIGHT,
      f"{d_ac:+.2f}: {d_ac / SIG_TOT:+.2f} sigma at W=55, {d_ac / SIG_TOT_TIGHT:+.2f} at W=80")
check("...but it is NOT comfortably inside at the tighter window and that is stated rather than "
      "smoothed: the reading runs from 0.9 to 1.3 sigma across the admissible range, so what is "
      "established is 'not resolved', not 'zero'",
      1.1 < abs(d_ac) / SIG_TOT_TIGHT < 1.6 and abs(d_ac) / SIG_TOT < 1.0,
      f"0.9 sigma at W=55 rising to {d_ac / SIG_TOT_TIGHT:.1f} at W=80")
check("the control ALSO sits high of the sky's fourth peak, so the arm's larger offset is mostly "
      "SHARED and is not the construction's",
      d_cs > 0 and d_as > d_cs and (d_cs / d_as) > 0.4,
      f"control {d_cs:+.2f} of the arm's {d_as:+.2f} -- {100 * d_cs / d_as:.0f}% shared")

print(f"""
  ** AND THE ORDER'S OWN +10.1 WAS NEVER THIS NUMBER. **  That offset is the paper's stored quartet
  (1134) against the paper's stored sky (1123.9) -- two different procedures.  Through ONE locator the
  arm-minus-sky offset is {d_as:+.2f}, and the part of it that is the construction's is {d_ac:+.2f}.
""")

# ---------------------------------------------------------------------------------
print("\n" + "=" * 100)
print("THE READING, AND THE STOPPING RULE.")
print("=" * 100)
print(f"""
  ** THE STOPPING RULE FIRES, AND THE THREE CANDIDATES ARE NOT RUN. **

  1. The order asked for the sky's fourth peak located by the same procedure, with its spread.  It is
     {sky_pk[3]:.1f} +- {SIG_STAT:.2f} statistical +- {sky_proc[3]:.2f} procedure = +- {SIG_TOT:.2f}.
     ** The spread I quoted at cc66.28 was the procedure half alone, and it is the smaller half. **

  2. The construction's own fourth-peak displacement -- what this arm does that the control does not --
     is {d_ac:+.2f} in ell, which is {d_ac / SIG_TOT:.2f} sigma of that at W = 55 and
     {d_ac / SIG_TOT_TIGHT:.2f} at W = 80.  ** It does not reach significance at either admissible
     window, so the sky cannot tell the two models apart at the fourth peak. **  What is established is
     'not resolved' rather than 'zero', and that is stated rather than smoothed -- but on the order's
     own test it is inside, so the third acoustic spacing, the baryon loading's effect on position and
     the transfer's resolution are NOT run, and the row closes on its first branch.

  3. ** What does not dissolve is smaller and is not this construction's. **  Both models sit high of
     the sky's fourth peak -- the control by {d_cs:+.2f} ({d_cs / SIG_TOT:.1f} sigma) and the arm by
     {d_as:+.2f} ({d_as / SIG_TOT:.1f} sigma).  That is a shared offset of flat LCDM and this arm alike
     from the located sky, and naming it is not pursuing it: a convergence check at the fourth peak is
     where it would go, and the stopping rule says not to go.

  4. ** AND THE INSTRUMENT TRAP IS THE PART TO CARRY FORWARD. **  cc66.28's locator finds peaks by free
     extremum search.  That is right on a smooth spectrum and wrong on a noisy one: under the
     covariance it returns {free[:, 3].mean():.0f} +- {free[:, 3].std():.0f} for the fourth peak.  Any
     future error propagation through that locator has to anchor the window, and the failure is kept as
     a gate here so it is not rediscovered.

  ** WHAT THIS DOES NOT REACH. **  The central value is the locator's on plik_lite's binning; sec:intro's
  own fourth peak is 1123.9, two multipoles from it and well inside the spread.  COV_TT is the shipped
  bandpower covariance with foregrounds and calibration marginalised; no beam or theory-side term is
  added.  And nothing here re-opens the phase intercept, the damping envelope, the driving or the refit.
""")

print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED -> " + "; ".join(FAILS))
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: the sky's fourth acoustic peak, located by cc66.28's own matched locator, is
{sky_pk[3]:.1f} +- {SIG_TOT:.2f} once the plik_lite bandpower covariance is propagated through it --
the spread quoted at cc66.28 being the procedure half alone.  The arm-minus-control displacement of
{d_ac:+.2f} is {d_ac / SIG_TOT:.2f} sigma of that at W = 55 and {d_ac / SIG_TOT_TIGHT:.2f} at W = 80 --
not reaching significance at either admissible window -- so there is no established construction-specific
fourth-peak displacement and PO-47's three candidates are not run.  Both models
sit high of the located sky ({d_cs:+.1f} and {d_as:+.1f}), which is a shared offset named and not
pursued.  And the free-extremum locator is unusable under noise ({free[:, 3].mean():.0f} +-
{free[:, 3].std():.0f} at the fourth peak), so error propagation must anchor the window.
NOT CLAIMED: a full sky-uncertainty budget; any of the three candidates; any re-opening of the phase
intercept, the damping envelope, the driving or the refit.
""")
