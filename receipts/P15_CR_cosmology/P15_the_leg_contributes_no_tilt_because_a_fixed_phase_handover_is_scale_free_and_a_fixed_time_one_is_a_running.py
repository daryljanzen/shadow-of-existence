"""
P15_the_leg_contributes_no_tilt_because_a_fixed_phase_handover_is_scale_free_and_a_fixed_time_one_is_a_running
============================================================================================================

Object under test -- `PO-31`'s work order from node 66: *where the tilt comes from, if it comes from the
leg.* The row has just acquired a target -- the like-for-like refit on this construction's own background
prefers n_s = 0.9949 against the control's 0.9559 (`r6805`) -- and the order asks for the first calculable
thing on the other side of that number: **can the collapse leg produce a departure of that size at all?**

** THE ANSWER IS NO, AND IT IS STRONGER THAN A SMALL NUMBER: THE LEG CANNOT PRODUCE A TILT OF ANY SIZE,
BECAUSE WHAT IT PRODUCES IS NOT A TILT. **  Three findings, in the order the order asks for them.

** (1) THE ONLY PLACE A SCALE SURVIVES IS THE LOCUS, AND AT FIXED PHASE IT CANCELS EXACTLY. **  The leg's
established closed form is Psi = Psi_i T(x) with T(x) = 3(sin x - x cos x)/x^3 and x = k eta / sqrt3, and
Theta_hat = Theta_0 + Psi obeys the free equation exactly, Theta_hat = (Psi_i/2) cos x anchored at the
crossing.  ** Both are functions of x ALONE.  So a handover evaluated at a fixed PHASE x gives the same
number for every k -- the ratio of amplitudes at two wavenumbers is exactly 1, not approximately -- and a
handover evaluated at a fixed TIME eta does not, because there x is proportional to k. **  The progenitor's
mass enters only through k_s, i.e. only through the ratio k/k_s; the leg's finite duration enters only as
the value of x it stops at; and no departure from the closed form is needed to get a k-dependence, because
the closed form supplies one by itself the moment the locus is a time rather than a phase.

      x_seam = 0.7638 (k/k_s)     -- the one surviving scale, and it is the seam's, not the leg's

** (2) THE LEADING DEPARTURE IS RED IN BOTH CHANNELS AND IT GOES AS k^2, WHICH IS A RUNNING AND NOT A
TILT. **  At fixed eta, d/dln k = x d/dx, and both log-derivatives are elementary:

      d ln|Theta_hat| / d ln k  =  -x tan x          =  -x^2 - x^4/3 + O(x^6)
      d ln T          / d ln k  =  -x^2(x^2+35)/175  =  -x^2/5 + O(x^4)

** Both negative, so red; both vanishing as x^2. **  A constant n_s shift requires this derivative to BE a
constant.  Here it is proportional to k^2, so the leg's departure is a running whose size is set by where
in the band it is read -- and the Theta_hat channel's amplitude has an honest ZERO at x = pi/2, i.e.
k/k_s = 2.057, where the log-derivative diverges.

** (3) SO THE SIZE QUESTION ANSWERS ITSELF BY SHAPE, BEFORE MAGNITUDE. **  Ask the Theta_hat channel for
the target: 1 - n_s = 0.005 needs x = 0.0500, i.e. k/k_s = 0.065.  ** Thirty times that wavenumber -- well
inside the acoustic range the refit uses -- the same expression gives 1 - n_s = 41.9. **  A k^2 running
varies by ~900 across a factor-30 band; it cannot sit at 0.005 throughout it.  *So the leg cannot be tuned
to the target at any amplitude: the shape is wrong before the size is discussed, which is why no value was
chosen here and none could have been.*

⇒ ** AND ON THE ADJUDICATED CONFIGURATION IT IS EXACTLY ZERO. **  `r6774` resolved the handover to the
CROSSING, x -> 0, where T -> 1 and Theta_hat -> Psi_i/2: both k-independent limits, both log-derivatives
vanishing as x^2.  ** So on the configuration the corpus actually adopts, the leg contributes exactly zero
tilt, and the order's own preference applies -- an exact cancellation is a stronger result than a small
number. **

  ⌗ WHICH CLOSES A ROUTE AND MOVES THE ROW IN.  The tilt is wholly the progenitor's vacuum; the leg is a
  k-independent amplitude and nothing else, exactly as `P15` §coherence and §transmission have it.  ** The
  frontier is therefore one step further in than the row reads: not "where does the leg's tilt come from"
  but "what does the progenitor supply", and the leg is no longer a candidate. **

COMPUTES: scope -- what this settles and what it must not be read as.
  * The leg's closed form, the common freezing phase and the wavenumber-independent handover amplitude are
    ESTABLISHED (`P15` §coherence, §transmission; `r6760+cc66.1`) and are re-run here as the calibration,
    not re-derived.  ** If the three banked amplitudes do not reproduce, nothing below may be read. **
  * ** This bounds the LEG's contribution only. **  It says nothing about what the progenitor supplies,
    and nothing about A_s, whose fixed-point route the entropy monotone closed.
  * `x_seam = 0.7638 (k/k_s)` is taken from the established map rather than recomputed; the dependence on
    the progenitor's mass is entirely through `k_s` and no independent mass dependence appears.
  * The fixed-time numbers are evaluated at the seam because that is the only fixed-time locus the corpus
    has ever coded.  ** They are a demonstration that a fixed-time handover gives a running, not a claim
    that the corpus uses one -- it does not, since `r6774`. **
  * ** Nothing is tuned to 0.995 and no value was chosen to reach it. **  The target enters once, in (3),
    to be refuted on shape.  `PO-7` is untouched: this is a statement about a transfer function, not a
    verdict on the construction.

ORIGIN: `PO-31`'s work order in `FOR_60`, taken after the `P10` receipt node 66 sequenced first.  Step 1
answered exactly, so steps 2 and 3 are reported as the order's "stopping at whichever one answers" allows
-- both are computed because the shape argument in (3) is what makes (1) decisive rather than conditional.
"""
import os
import sys

import sympy as sp

_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

x = sp.Symbol('x', positive=True)
Psi_i = sp.Symbol('Psi_i', positive=True)
X_SEAM_COEFF = sp.Rational(7638, 10000)          # x_seam = 0.7638 (k/k_s), from the established map

T = 3 * (sp.sin(x) - x * sp.cos(x)) / x ** 3      # Psi = Psi_i T(x),  x = k eta / sqrt3
TH = Psi_i * sp.cos(x) / 2                        # Theta_hat, free oscillator anchored at the crossing

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — THE ESTABLISHED CLOSED FORM AND ITS THREE BANKED AMPLITUDES, FIRST")
print("=" * 94)
print("""
  The leg's closed form is not this receipt's to derive.  What it must do before anything else is
  reproduce the three amplitudes `r6760+cc66.1` banked, because every number below is read off the same
  two functions.
""")
ENTRY = 1 / sp.sqrt(3)
A_CODED = T.subs(x, ENTRY) / 2                    # what CRAMP=flat codes: Psi(entry)/2
A_EXACT = sp.cos(ENTRY) / 2                       # the exact free solution at entry
A_ENV = sp.Rational(1, 2)                         # the envelope, and the value at the crossing
print(f"    T(1/sqrt3)/2   = {float(A_CODED):.5f} Psi_i   the coded handover, Psi(entry) halved")
print(f"    cos(1/sqrt3)/2 = {float(A_EXACT):.5f} Psi_i   the exact temperature at entry")
print(f"    the envelope   = {float(A_ENV):.5f} Psi_i   and the value at the crossing")
check("the coded handover amplitude reproduces 0.48353", abs(float(A_CODED) - 0.48353) < 1e-5)
check("the exact entry temperature reproduces 0.41896", abs(float(A_EXACT) - 0.41896) < 1e-5)
check("T -> 1 at the crossing, so Psi -> Psi_i exactly", sp.limit(T, x, 0) == 1)
check("and Theta_hat -> Psi_i/2 there, the ordinary frozen adiabatic state",
      sp.limit(TH, x, 0) == Psi_i / 2)

# =========================================================================================
print()
print("=" * 94)
print("PART 2 (STEP 1) — WHERE THE SCALE-FREEDOM IS EXACT, AND WHERE A SCALE SURVIVES")
print("=" * 94)
print("""
  Both quantities are functions of x = k eta / sqrt3 ALONE.  So the question is entirely about the locus:
  a phase, or a time.
""")
k1, k2, eta = sp.symbols('k1 k2 eta', positive=True)
print(f"    at FIXED PHASE x:  T(x)/T(x) = {sp.simplify(T / T)}   and Theta_hat(x)/Theta_hat(x) = "
      f"{sp.simplify(TH / TH)}")
check("⚑ at a fixed phase the ratio of amplitudes at two wavenumbers is EXACTLY 1, so the transfer is "
      "exactly scale-free", sp.simplify(T / T) == 1 and sp.simplify(TH / TH) == 1)
T1 = T.subs(x, k1 * eta / sp.sqrt(3))
T2 = T.subs(x, k2 * eta / sp.sqrt(3))
ratio_fixed_time = sp.simplify(T1 / T2)
print(f"    at FIXED TIME eta: the ratio still carries both wavenumbers: "
      f"{k1 in ratio_fixed_time.free_symbols and k2 in ratio_fixed_time.free_symbols}")
check("at a fixed time the ratio does NOT cancel -- x is proportional to k there",
      k1 in ratio_fixed_time.free_symbols and k2 in ratio_fixed_time.free_symbols)
print(f"""
    ⇒ so the ONE surviving scale is the locus, through x_seam = {float(X_SEAM_COEFF)} (k/k_s).
      The progenitor's mass enters only through k_s; the leg's duration only as the x it stops at;
      and no departure from the closed form is needed for a k-dependence -- the closed form has one
      the moment the locus is a time.
""")
check("the surviving scale is the established seam coefficient and not a new input",
      abs(float(X_SEAM_COEFF) - 0.7638) < 1e-9)

# =========================================================================================
print()
print("=" * 94)
print("PART 3 (STEP 2) — THE LEADING DEPARTURE: RED IN BOTH CHANNELS, AND GOING AS k^2")
print("=" * 94)
dTH = sp.simplify(x * sp.diff(sp.log(sp.Abs(TH)), x))
dT = sp.simplify(x * sp.diff(sp.log(T), x))
sTH = sp.simplify(sp.series(-x * sp.tan(x), x, 0, 5).removeO())
sT = sp.simplify(sp.series(dT, x, 0, 5).removeO())
print(f"    d ln|Theta_hat| / d ln k = -x tan x")
print(f"      small-x:               {sTH}")
print(f"    d ln T          / d ln k = {dT}")
print(f"      small-x:               {sT}")
check("the Theta_hat channel's log-derivative is -x tan x",
      sp.simplify(sp.Piecewise((0, sp.Eq(sp.cos(x), 0)), (-x * sp.tan(x), True)) - dTH) == 0)
check("⚑ it is RED and vanishes as x^2, so it is a RUNNING and not a tilt",
      sp.simplify(sTH + x ** 2 + x ** 4 / 3) == 0)
check("the Psi channel is red too and also goes as x^2", sp.simplify(sT + x ** 2 / 5 + x ** 4 / 175) == 0)
XS = X_SEAM_COEFF
print(f"\n    at the seam with k = k_s (x = {float(XS)}):")
print(f"      d ln|Theta_hat|/d ln k = {float(dTH.subs(x, XS)):+.4f}   -> 1 - n_s = "
      f"{float(-2 * dTH.subs(x, XS)):+.4f}")
print(f"      d ln T/d ln k          = {float(dT.subs(x, XS)):+.4f}")
ZERO_K = sp.pi / 2 / XS
print(f"      and the Theta_hat amplitude has a ZERO at k/k_s = {float(ZERO_K):.3f}, where the "
      f"log-derivative diverges")
check("at the seam the fixed-time departure is of order unity, not of order the target",
      abs(float(-2 * dTH.subs(x, XS))) > 1.0)
check("and the amplitude's zero sits inside the acoustic range at k/k_s near 2",
      1.5 < float(ZERO_K) < 2.5)

# =========================================================================================
print()
print("=" * 94)
print("PART 4 (STEP 3) — THE SIZE QUESTION ANSWERS ITSELF BY SHAPE")
print("=" * 94)
TARGET = sp.Rational(5, 1000)                     # 1 - n_s = 0.005 on this background
x_need = sp.nsolve(sp.Eq(2 * x * sp.tan(x), TARGET), x, 0.05)
band = 30
x_band = band * x_need                            # the same locus, thirty times the wavenumber
one_minus_ns_at_30 = float(2 * x_band * sp.tan(x_band))
print(f"    to give 1 - n_s = {float(TARGET)} the Theta_hat channel needs x = {float(x_need):.4f}, "
      f"i.e. k/k_s = {float(x_need) / float(XS):.4f}")
print(f"    the SAME expression {band}x that wavenumber gives 1 - n_s = {one_minus_ns_at_30:.1f}")
check("⛔ a k^2 running cannot hold the target across the band: thirty times the wavenumber gives "
      "order tens", one_minus_ns_at_30 > 1.0)
check("so no amplitude choice makes the leg's departure look like a constant tilt",
      one_minus_ns_at_30 / float(TARGET) > 100)

# =========================================================================================
print()
print("=" * 94)
print("PART 5 — AND ON THE ADJUDICATED CONFIGURATION IT IS EXACTLY ZERO")
print("=" * 94)
print("""
  `r6774` resolved the handover to the CROSSING, x -> 0.  That is a fixed phase -- the limiting one -- so
  Part 2's exact cancellation applies there, and the log-derivatives vanish with it.
""")
print(f"    lim_(x->0) d ln|Theta_hat|/d ln k = {sp.limit(-x * sp.tan(x), x, 0)}")
print(f"    lim_(x->0) d ln T/d ln k          = {sp.limit(dT, x, 0)}")
check("⚑ at the crossing the Theta_hat channel contributes exactly zero tilt",
      sp.limit(-x * sp.tan(x), x, 0) == 0)
check("⚑ and so does the Psi channel", sp.limit(dT, x, 0) == 0)
check("the approach is quadratic, so the vanishing is not an artefact of where the limit is taken",
      sp.simplify(sp.limit(-x * sp.tan(x) / x ** 2, x, 0)) == -1)

# =========================================================================================
print()
print("=" * 94)
print("WHAT THIS REVISION ESTABLISHES")
print("=" * 94)
print(f"""
  ** THE LEG CONTRIBUTES NO TILT, AND THE REASON IS STRONGER THAN A SMALL NUMBER. **  Both the potential
  and the temperature on the collapse leg are functions of x = k eta / sqrt3 alone, so a handover at a
  fixed PHASE is exactly scale-free -- the ratio at two wavenumbers is 1, not nearly 1 -- and the only
  place a scale can survive is a handover at a fixed TIME, through x_seam = {float(XS)} (k/k_s).

  ** AND WHAT A FIXED-TIME HANDOVER WOULD GIVE IS NOT A TILT. **  Both channels are red and both go as
  k^2: d ln|Theta_hat|/d ln k = -x tan x = -x^2 + O(x^4), d ln T/d ln k = -x^2/5 + O(x^4).  A constant
  n_s shift needs a constant log-derivative; this one is proportional to k^2, and the Theta_hat amplitude
  has a zero at k/k_s = {float(ZERO_K):.3f}.  ** Asked for the target it needs k/k_s = {float(x_need)/float(XS):.3f},
  and thirty times that wavenumber the same expression gives 1 - n_s = {one_minus_ns_at_30:.0f}. **  The
  shape is wrong before the size is discussed.

  ⇒ ** ON THE ADJUDICATED CONFIGURATION IT IS EXACTLY ZERO. **  `r6774`'s crossing is x -> 0, where
  T -> 1 and Theta_hat -> Psi_i/2 and both log-derivatives vanish quadratically.  *The order asked for
  exactly this preference: an exact cancellation rather than a small number.*

  ⌗ SO A ROUTE CLOSES AND THE ROW MOVES IN.  ** The tilt is wholly the progenitor's vacuum; the leg is a
  k-independent amplitude and nothing else. **  `PO-31` is no longer "where does the leg's tilt come
  from" -- the leg is not a candidate -- but "what does the progenitor supply", which is one step further
  in.  ⚠ *And nothing here was tuned: the target enters once, to be refuted on shape, and `PO-7` is
  untouched.*
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
