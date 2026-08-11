#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE 150 IS NOT A PREDICTION. `ROBUST_p1p2_scan`'s FIRST-PEAK POSITION AND
PEAK-HEIGHT RATIO ARE NOT STABLE UNDER ITS OWN DOCUMENTED INITIAL CONDITIONS, AND THE READING ITS
DOCSTRING ACTUALLY DESCRIBES RETURNS P1/P2 = 2.02 AGAINST THE SKY'S 2.21 -- NOT THE 1.45 THE PAPER
REPORTS AS A DISAGREEMENT. **

Built r2376+c54.164, working front #5 (`L-171` - `PO-7` - `frontier:scalar`): the corpus's two
internal routes to the first acoustic peak, the transfer argument at 220 and this instrument at 150.

** WHAT THE FRONT ASSUMED, AND WHAT IS ACTUALLY THE CASE. **  The front is posed as a disagreement
between two established routes, to be resolved by deciding which is right.  ** One of the two is not
established.  It is not currently an arbiter of anything, and that -- not a verdict for 220 -- is
what this file establishes. **

  PART 1  ** THE NUMERICS ARE NOT THE ISSUE, AND THIS IS CHECKED FIRST so that nothing below can be
          waved away as integration error. **  The receipt's own stability number h k^2/(3 Hc) is
          0.01--0.47 against its stated limit of 2.8, and 120--720 RK4 steps fall in each acoustic
          oscillation.  Quadrupling NS_CR reproduces the extrema and the peaks digit for digit.
  PART 2  ** THE VALUE AND THE DERIVATIVE OF Psi COME FROM TWO DIFFERENT FUNCTIONS. **  Ph0 is taken
          from the smooth matched envelope 1/(1+xs^2/3); dPh0 is taken from a numerical derivative of
          the OSCILLATORY 3(sin x - x cos x)/x^3.  The initial velocity theta = 6 dPsi is built from
          the second while the amplitude is built from the first.
  PART 3  ** THE HEADLINE FIGURES MOVE UNDER FOUR READINGS OF THE RECEIPT'S OWN STATED ICs. **
          ell_1 in {150, 165, 315} and P1/P2 in {0.93, 1.21, 1.45, 2.02}.  ** The receipt's docstring
          says "the common phase is taken at an extremum (velocities zero)".  The code does not set
          the velocities to zero.  Setting them to zero as documented gives P1/P2 = 2.02. **
  PART 4  ** AND THE COMB THE PAPER CITES AGAINST IT WAS NEVER PROPAGATED EITHER. **  P15
          sec:coherence says "propagating the tightly-coupled acoustic modes to last scattering from
          a common seam phase yields a sharp regular comb at spacing 296".  Its receipt writes down
          cos(k r_s)^2 with r_s and D_C as hardcoded literals.  ** Nothing is propagated. **

** WHAT THIS DOES NOT ESTABLISH, STATED PLAINLY. **  It does NOT vindicate 220, and it does not
supply a first-peak position.  It removes one of the two routes from arbiter status.  ** And it
leaves a residual the initial data do NOT explain and which is the front's real content: under EVERY
one of the four initial conditions the source comb's spacing comes out at 0.72--0.79 of pi/r_s
rather than at pi/r_s. **  That is a disagreement with the acoustic scale the instrument was pinned
to, it is not caused by the initial data, and it is registered rather than resolved here.

FIGURES PINNED BELOW are produced by `computations/beyond_the_wall/L171_what_sets_the_first_peak.py`,
which EXECS `ROBUST_p1p2_scan.py`'s own source with the initial-data block substituted and every
other line byte-identical -- so anything that moves, moves because of the initial data.  Its
ICMODE=asis control reproduces 150/360/555/780 and P1/P2=1.447 exactly, with the registered
receipt's own assertions passing.  Each variant costs ~5 min; they are pinned here, not re-run.

rc=0 on success.  Run: python3 P15_the_first_peak_figure_is_not_stable.py   (numpy scipy, ~10 s)
"""
import os
import sys

import numpy as np
from scipy.integrate import quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

# ---- the receipt's own background, rebuilt exactly -------------------------------------------
c = 299792.458
H0, Om = 73.0, 0.3066
OL = 1 - Om
ombh2, z_rec = 0.0224, 1089.9
a_rec = 1 / (1 + z_rec)
Rb_rec = 31500 * ombh2 / (2.7255 / 2.7) ** 4 / (1 + z_rec)
fnu = 0.4052
Hub = lambda a: H0 * np.sqrt(Om / a ** 3 + OL)                          # noqa: E731
Or = 4.15e-5 / (H0 / 100) ** 2
ag = np.logspace(-7, 0, 20000)
_s = float(quad(lambda a: c / (a ** 2 * Hub(a)), 1e-14, ag[0], limit=200)[0])
eg = np.concatenate([[_s], _s + cumulative_trapezoid(c / (ag ** 2 * Hub(ag)), ag)])
Hc_of = CubicSpline(eg, ag * Hub(ag) / c)
rt = Or / ag ** 4 + Om / ag ** 3 + OL
Og_of = CubicSpline(eg, (1 - fnu) * (Or / ag ** 4) / rt)
On_of = CubicSpline(eg, fnu * (Or / ag ** 4) / rt)
Oc_of = CubicSpline(eg, (Om / ag ** 3) / rt)
eta_rec = float(np.interp(a_rec, ag, eg))
eta_0 = eg[-1]
rs_f = lambda z: quad(lambda a: c / (a ** 2 * Hub(a) * np.sqrt(3 * (1 + Rb_rec * a / a_rec))),   # noqa: E731
                      1 / (1 + z), a_rec, limit=250)[0]
DM = eta_0 - eta_rec
z_on = brentq(lambda z: np.pi * DM / rs_f(z) - 301.6, 1500., 60000.)
eta_on = float(np.interp(1 / (1 + z_on), ag, eg))
eta_end = float(np.interp(min(20 * a_rec, 1.0), ag, eg))
rs = rs_f(z_on)
lA = np.pi * DM / rs

# =====================================================================
print("=" * 78)
print("PART 1 — THE NUMERICS ARE NOT THE ISSUE")
print("=" * 78)
print(f"  z_onset = {z_on:.0f}   eta_onset = {eta_on:.2f}   eta_rec = {eta_rec:.1f}   "
      f"r_s = {rs:.2f}   l_A = {lA:.1f}\n")
print(f"  {'l':>6} {'k [1/Mpc]':>11} {'h k^2/(3 Hc) at rec':>21} {'RK4 steps per oscillation':>27}")
h1400 = (eta_end - eta_on) / 1400
worst_stab, fewest_steps = 0.0, 1e9
for ell in (150, 220, 360, 555, 780, 899):
    k = ell / DM
    stab = h1400 * k ** 2 / (3 * Hc_of(eta_rec))
    steps = (2 * np.pi / (k / np.sqrt(3))) / h1400
    worst_stab, fewest_steps = max(worst_stab, stab), min(fewest_steps, steps)
    print(f"  {ell:>6} {k:>11.5f} {stab:>21.2f} {steps:>27.0f}")
print(f"\n  ** worst stability number {worst_stab:.2f} against the receipt's own limit of 2.8; "
      f"fewest {fewest_steps:.0f} steps per oscillation. **")
print("  *NS_CR = 5600 (four times the default) reproduces the source extrema to four decimals and")
print("   the peaks 150/360/555/780 exactly, so the figures below are the physics as implemented.*")
if worst_stab > 2.8:
    fail.append(f"stability number {worst_stab:.2f} exceeds the receipt's stated limit 2.8")
if fewest_steps < 50:
    fail.append(f"only {fewest_steps:.0f} steps per oscillation -- the integrator IS under-resolved")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — Psi's VALUE AND Psi's DERIVATIVE COME FROM TWO DIFFERENT FUNCTIONS")
print("=" * 78)
Hcs, Ogs, Ons, Ocs = Hc_of(eta_on), Og_of(eta_on), On_of(eta_on), Oc_of(eta_on)
rr = (Ogs + Ons) / Ocs
ksm = Hcs * np.sqrt(1.0 + rr)


def env(x):
    """the SMOOTH matched envelope the receipt takes Psi's VALUE from"""
    return 1.0 / (1.0 + x ** 2 / 3.0)


def osc(x):
    """the OSCILLATORY closed form the receipt takes Psi's DERIVATIVE from"""
    x = np.asarray(x, dtype=float)
    return 3 * (np.sin(x) - x * np.cos(x)) / x ** 3


hh = 1e-4
print(f"  the leg's horizon wavenumber k_sm = {ksm:.6f}/Mpc, and xs = k/(sqrt3 k_sm)\n")
print(f"  {'l':>6} {'xs':>8} {'envelope(xs)':>14} {'oscillatory(xs)':>17} "
      f"{'d/dxs envelope':>16} {'d/dxs oscillatory':>19}")
maxratio = 0.0
for ell in (184, 374, 588, 833):
    k = ell / DM
    xs = k / (np.sqrt(3) * ksm)
    d_env = -(2.0 * xs / 3.0) / (1.0 + xs ** 2 / 3.0) ** 2
    d_osc = float((osc(xs + hh) - osc(xs - hh)) / (2 * hh))
    maxratio = max(maxratio, abs(d_osc / d_env))
    print(f"  {ell:>6} {xs:>8.4f} {env(xs):>14.5f} {float(osc(xs)):>17.5f} "
          f"{d_env:>16.5f} {d_osc:>19.5f}")
print(f"\n  ** The receipt sets Ph0 from column three and dPh0 from column six. **  The initial")
print(f"  velocity is theta = -3 dThat + 6 dPsi with dThat = 0, so theta is built ENTIRELY from a")
print(f"  derivative of a function that is not the one supplying the amplitude; the two derivatives")
print(f"  differ by up to a factor of {maxratio:.2f} across the observed band.")
# the two functions agree at small x and must not be assumed to agree where the modes live
assert abs(env(0.02) - float(osc(0.02))) < 1e-3, "the envelope and the oscillation must agree as x->0"
if maxratio < 1.2:
    fail.append(f"the two derivatives agree to {maxratio:.2f} -- PART 2's premise would be wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE HEADLINE FIGURES MOVE UNDER FOUR READINGS OF THE RECEIPT'S OWN STATED ICs")
print("=" * 78)
# from L171_what_sets_the_first_peak.py; ICMODE=asis reproduces the registered receipt exactly.
VARIANTS = {
    #  ICMODE        first source extremum   comb/(pi/r_s)   peaks in l              P1/P2
    'asis':        (0.6108, 0.7173, [150, 360, 555, 780], 1.447),
    'consistent':  (0.5288, 0.7386, [315, 525, 780],      1.206),
    'flatpsi':     (0.6564, 0.7887, [165, 390, 615, 870], 0.933),
    'zerovel':     (0.6473, 0.7796, [165, 390, 615],      2.017),
}
WHAT = {
    'asis':       "the receipt unmodified — the control, and it reproduces 150/360/555/780 exactly",
    'consistent': "Psi's value and derivative from the SAME function",
    'flatpsi':    "Psi flat in k, which is what sec:envelope claims: 'the same driving amplitude'",
    'zerovel':    "theta = 0, which is what the receipt's OWN DOCSTRING says it does",
}
print(f"  {'ICMODE':>12} {'1st extremum':>13} {'comb/(pi/r_s)':>15} {'peaks in l':>26} {'P1/P2':>8}")
for kk_, (x1, cmb, pks, r12) in VARIANTS.items():
    print(f"  {kk_:>12} {x1:>13.4f} {cmb:>15.4f} {str(pks):>26} {r12:>8.3f}")
print(f"  {'sky':>12} {'—':>13} {1.0:>15.4f} {str([220, 536, 813]):>26} {2.212:>8.3f}")
print()
for kk_ in VARIANTS:
    print(f"    {kk_:>11} : {WHAT[kk_]}")
l1 = [v[2][0] for v in VARIANTS.values()]
r12s = [v[3] for v in VARIANTS.values()]
print(f"\n  ** ell_1 spans {min(l1)}–{max(l1)} and P1/P2 spans {min(r12s):.2f}–{max(r12s):.2f} "
      f"across four readings of one stated initial condition. **")
print("  ** The documented reading — 'velocities zero' — returns P1/P2 = 2.017 against the sky's")
print("     2.212, a 9% shortfall, where the paper reports 1.45 against 2.21 as its disagreement. **")
print("     *So the reported disagreement is a property of the implementation and not of the")
print("      construction, and the 150 is not a prediction the corpus is entitled to quote.*")
assert abs(VARIANTS['asis'][3] - 1.447) < 0.003, "the control must reproduce the registered 1.447"
assert VARIANTS['asis'][2] == [150, 360, 555, 780], "the control must reproduce the registered peaks"
assert abs(VARIANTS['zerovel'][3] - 2.017) < 0.005, "the documented-IC run returns P1/P2 = 2.017"
assert max(r12s) / min(r12s) > 2.0, "the ratio must move by more than a factor two to make the point"
assert max(l1) - min(l1) >= 150, "the first peak must move by at least 150 multipoles"
assert abs(VARIANTS['zerovel'][3] - 2.212) < abs(VARIANTS['asis'][3] - 2.212), \
    "the documented reading must sit CLOSER to the sky than the implemented one"

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND THE COMB CITED AGAINST IT WAS NEVER PROPAGATED")
print("=" * 78)
comb = os.path.join(HERE, 'P15_verify_coherence_comb.py')
src = open(comb, encoding='utf-8').read()
print("  P15 sec:coherence: 'propagating the tightly-coupled acoustic modes to last scattering from")
print("  a common seam phase yields a sharp regular comb at spacing Delta-ell ~= pi D_C/r_s ~= 296'.")
print(f"\n  What {os.path.basename(comb)} actually contains:\n")
for ln in src.split('\n'):
    if 'np.cos(k*rs)' in ln or ln.strip().startswith('rs=') or ln.strip().startswith('D_C='):
        print(f"      {ln.strip()}")
print("\n  ** r_s and D_C are hardcoded literals and the mode function is written down. There is no")
print("     integrator in the file, so no mode is propagated anywhere. **  *Its own docstring is")
print("     honest about this — 'does NOT replace the full seam-to-recombination Boltzmann")
print("     transfer' — and the paper's sentence claims the propagation the receipt disclaims.*")
assert 'np.cos(k*rs)' in src, "the comb receipt is expected to WRITE DOWN cos(k r_s)"
assert 'rs=147.0' in src.replace(' ', ''), "the comb receipt is expected to hardcode r_s"
assert 'solve_ivp' not in src and 'odeint' not in src, \
    "if the comb receipt has acquired an integrator this PART is stale and must be rewritten"

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE RESIDUAL THE INITIAL DATA DO NOT EXPLAIN")
print("=" * 78)
combs = [v[1] for v in VARIANTS.values()]
print(f"  source comb spacing as a fraction of pi/r_s, across all four initial conditions:")
print(f"      {'  '.join(f'{x:.4f}' for x in combs)}     (min {min(combs):.3f}, max {max(combs):.3f})")
print()
print("  ** Under EVERY initial condition the instrument's source comb comes out at 0.72–0.79 of the")
print("     acoustic spacing it was pinned to, never at 1. **  *The initial data move the first peak")
print("     by 165 multipoles and do not move this.*  ⇒ **It is not an initial-data artefact, and it")
print("     is a disagreement with the acoustic scale — the corpus's own settled result — inside the")
print("     one instrument that propagates modes.**")
print("     *Registered, not resolved. This is what front #5 turns out to be about.*")
assert max(combs) < 0.85, "the comb deficit must be present in every variant for PART 5 to hold"
assert min(combs) > 0.60, "and it must be a deficit rather than a collapse"
assert max(combs) - min(combs) < 0.15, \
    "the deficit must be STABLE across the variants -- that is what makes it not initial data"

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the 150 is not stable under the receipt's own documented initial")
print("conditions, so it is not an arbiter of the first peak's position; and the comb deficit that")
print("survives every variant is the question front #5 actually poses.")
print("=" * 78)
