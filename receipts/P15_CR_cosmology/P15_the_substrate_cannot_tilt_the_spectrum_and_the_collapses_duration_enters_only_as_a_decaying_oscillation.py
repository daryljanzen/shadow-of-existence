"""
P15_the_substrate_cannot_tilt_the_spectrum_and_the_collapses_duration_enters_only_as_a_decaying_oscillation
==========================================================================================================

Object under test -- node 66's order (2) in `FOR_60`, `PO-31` one step in.  `r6812` closed the leg as a
source of the tilt, so the tilt is the progenitor's vacuum, and the order asks what the SUBSTRATE ALONE
constrains about that vacuum BEFORE any interior is modelled.  Its own framing: the substrate is maximally
symmetric and carries one length, a vacuum on a maximally symmetric space has no preferred scale, and a
scale-free vacuum spectrum is n_s = 1 exactly -- ** so what breaks it, and in which direction? **  Three
candidates are named and each is to be answered rather than surveyed: the progenitor's own mass, the finite
duration of the collapse, and the substrate's curvature radius itself.

** THE ANSWER: ONE OF THE THREE CAN ENTER AT ALL, AND WHAT IT PRODUCES IS NOT A TILT.  THE SUBSTRATE ALONE
GIVES n_s = 1 EXACTLY, SO A CONSTANT TILT REQUIRES THE INTERIOR -- WHICH IS THE NEGATIVE THE ORDER SAID
WOULD ITSELF BE THE ANSWER. **  Four findings.

** (1) THE CURVATURE RADIUS CANNOT ENTER, AND THE REASON IS EXACT RATHER THAN SMALL. **  In conformal time
the substrate's mode equation for a massless minimally coupled field is

      u'' + (k^2 - 2/eta^2) u = 0

and ** alpha does not appear in it at all. **  The one length in the geometry has already been used up in
the map eta -> t; what governs the modes is the single dimensionless variable k*eta, and with the vacuum set
at eta -> -infinity the whole k-dependence is the normalisation 1/sqrt(2k).  So P(k) = (H/2*pi)^2 =
1/(4*pi^2*alpha^2): ** alpha fixes A_s and cannot reach n_s, for EVERY alpha, not for large alpha. **  A
scale absent from the equation cannot tilt what the equation produces.

** (2) THE PROGENITOR'S MASS CANNOT ENTER EITHER, AND ON THIS CONSTRUCTION THAT IS A THEOREM AND NOT AN
ESTIMATE. **  The forced member is Nariai, Lambda*M^2 = 1/9 with Lambda = 3/alpha^2, so

      M = sqrt(3)*alpha/9 = alpha/(3*sqrt3),      M/alpha = 0.192450...  a PURE NUMBER

** the progenitor's mass is not an independent length on this construction -- it IS the curvature radius up
to a pure number. **  So the two candidates are one candidate, and (1) disqualifies both together.  *This is
the part that is specific to this construction rather than generic: on a member where M were free, M/alpha
would be a knob; on the forced member it is arithmetic.*

** (3) ONLY THE FINITE DURATION CAN ENTER -- AND IT ENTERS AS A DECAYING OSCILLATION WITH NO SIGN. **  A
finite duration means the vacuum is set at a finite eta_0 rather than at eta -> -infinity, which is the one
way a genuinely new dimensionless variable x = k*|eta_0| appears.  Matching the substrate modes to the
instantaneous positive-frequency data at eta_0 gives Bogoliubov coefficients in closed form,

      alpha_k = 1 - i/x - 1/(2x^2),     beta_k = -exp(2ix)/(2x^2),     |alpha_k|^2 - |beta_k|^2 = 1 exactly

and the ratio of the late-time power to the scale-free one is exact and elementary:

      R(x) = |alpha_k - beta_k|^2 = 1 + cos(2x)/x^2 - sin(2x)/x^3 + (1 - cos(2x))/(2x^4)

** Its log-derivative is d ln R / d ln k = -2 sin(2x)/x + O(1/x^2): an OSCILLATION whose envelope decays,
not a constant. **  It changes sign 24 times over x in [1,40]; its envelope is under 0.2 beyond x = 10; and its
band averages DISAGREE WITH ONE ANOTHER across four consecutive octaves -- -0.095, +0.002, +0.020, -0.002,
differing in sign -- while each band's internal spread exceeds its own mean by more than a factor ten.  *A tilt is a band-independent
number; this is the opposite of one, and by the corpus's own operational test -- a kernel carries a scale
exactly when the tilt one fits to it depends on which band one fits (`P15` §transmission,
Remark "the leg does not tilt it either") -- this IS a scale, which is why it shows up as band dependence
and not as a tilt.*

** (4) SO THE ONE CHANNEL THAT COULD GIVE A CONSTANT TILT IS AN EFFECTIVE MASS, AND ITS SIGN IS THE ANSWER
TO THE ORDER'S SECOND HALF. **  For a field of effective mass m on the substrate the late-time spectrum is
an exact power law, P ~ k^(3-2nu) with nu = sqrt(9/4 - m^2*alpha^2), so

      n_s - 1 = 3 - 2*sqrt(9/4 - m^2*alpha^2) = (2/3)*m^2*alpha^2 + (2/27)*(m^2*alpha^2)^2 + ...

** A positive effective mass-squared gives a BLUE tilt. **  And that is the direction worth reporting,
because the measured target on this construction's own background is n_s = 0.995 -- nearer unity than the
standard model's 0.965 by an order of magnitude in 1 - n_s -- but it is nearer unity FROM BELOW.  Reaching
it needs

      m^2*alpha^2 = -1201/160000 = -0.00750625      slightly TACHYONIC, and it is a requirement, not a result

  ⌗ SO THE ROW MOVES IN AGAIN AND THE FRONTIER IS NAMED.  ** The substrate constrains the vacuum completely
  and the constraint is n_s = 1 exactly: two of the three candidates are disqualified by the same argument
  and the third produces a running rather than a tilt. **  A constant tilt therefore needs content the
  substrate does not have -- an effective mass-squared on the perturbation, which is interior physics -- and
  the frontier begins exactly there, with its sign fixed in advance: blue if that mass-squared is positive,
  so the measured value requires it slightly negative.  *Stated as the order asked: a possibility about
  where the data may already be pointing, and not a result.*

COMPUTES: scope -- what this settles and what it must not be read as.
  * The Nariai constants are ESTABLISHED (`P15` Fig. f(r), `r6804`) and are re-run here as the calibration
    rather than re-derived.  ** If Lambda*M^2 = 1/9 and r_N = alpha/sqrt3 do not reproduce, nothing below
    may be read, because (2) rests entirely on them. **
  * ⚠ ** THE ONE MODELLING STEP IS NAMED AND IT IS THE STANDARD ONE: ** the corpus's scalar perturbation is
    treated on the substrate as a massless minimally coupled field, which is what makes `u'' + (k^2 -
    2/eta^2)u = 0` the mode equation.  Findings (1) and (2) are robust to that choice -- they are statements
    about which LENGTHS appear, and no length appears for any mass -- but the exact value n_s = 1 in the
    massless case is not: (4) is precisely the statement that a mass moves it.
  * ⚠ ** (3) computes the effect of a SHARP initial time, the one prescription that is unambiguous. **  A
    smooth onset changes the envelope's power and the phase; it cannot change the sign alternation, which
    follows from the vacuum being set at a definite phase of each mode.  The receipt claims the SHAPE
    (oscillation, decaying, sign-alternating) and not the coefficient.
  * ⚠ This bounds what the SUBSTRATE supplies.  It says nothing about A_s, whose fixed-point route the
    entropy monotone closed, and nothing about the interior beyond the one requirement in (4).
  * ⚠ ** Nothing is tuned to 0.995. **  The target enters once, at the end, and only to be inverted into a
    requirement on a quantity this receipt does not compute.  `PO-7` is untouched.

ORIGIN: node 66's order (2) in `FOR_60` (`r6825`), taken directly after `r6812` answered order (1).  The
order's own stopping rule applies -- "if the three candidates all fail to enter, that is the answer" -- and
it is reached, so (4) is reported beyond it because the sign is the half of the order that survives the
negative.
"""
import sys

import numpy as np
import sympy as sp

_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

eta, k, al, x = sp.symbols('eta k alpha x', positive=True)
mu = sp.Symbol('mu', real=True)                 # mu = m^2 alpha^2 = m^2/H^2, the only dimensionless mass

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — THE CALIBRATION: THE SUBSTRATE'S BANKED CONSTANTS, AND THE MODE THAT SOLVES IT")
print("=" * 94)
print("""
  Two things must reproduce before anything below may be read: the Nariai constants, on which finding (2)
  rests entirely, and the fact that the Bunch--Davies mode solves the substrate's mode equation, on which
  (1), (3) and (4) all rest.
""")
M, Lam = sp.symbols('M Lambda', positive=True)
nariai = sp.solve([sp.Eq(Lam * M ** 2, sp.Rational(1, 9)), sp.Eq(Lam, 3 / al ** 2)], [M, Lam], dict=True)[0]
M_N = sp.simplify(nariai[M])
r_N = al / sp.sqrt(3)
print(f"    Lambda = 3/alpha^2  and  Lambda M^2 = 1/9   =>   M = {M_N}")
print(f"    r_N    = alpha/sqrt3 = {float(r_N / al):.6f} alpha      the degenerate double root")
check("the Nariai mass reproduces M = sqrt(3) alpha / 9 (established, r6804)",
      sp.simplify(M_N - sp.sqrt(3) * al / 9) == 0)
check("and it satisfies Lambda M^2 = 1/9 on substitution, not by assertion",
      sp.simplify((3 / al ** 2) * M_N ** 2 - sp.Rational(1, 9)) == 0)
f_sds = 1 - 2 * M_N / r_N - r_N ** 2 / al ** 2
fp_sds = sp.diff(1 - 2 * M_N / sp.Symbol('r', positive=True) - sp.Symbol('r', positive=True) ** 2 / al ** 2,
                 sp.Symbol('r', positive=True)).subs(sp.Symbol('r', positive=True), r_N)
print(f"    f(r_N)  = {sp.simplify(f_sds)}        f'(r_N) = {sp.simplify(fp_sds)}")
check("f and f' vanish together at r_N — the root is degenerate, which is what forces the member",
      sp.simplify(f_sds) == 0 and sp.simplify(fp_sds) == 0)

u_bd = (1 / sp.sqrt(2 * k)) * (1 - sp.I / (k * eta)) * sp.exp(-sp.I * k * eta)
mode_eq_lhs = sp.diff(u_bd, eta, 2) + (k ** 2 - 2 / eta ** 2) * u_bd
check("the Bunch--Davies mode solves u'' + (k^2 - 2/eta^2) u = 0 exactly",
      sp.simplify(mode_eq_lhs) == 0)
wronskian = sp.simplify(u_bd * sp.conjugate(sp.diff(u_bd, eta)) - sp.conjugate(u_bd) * sp.diff(u_bd, eta))
print(f"    Wronskian u u*' - u* u' = {wronskian}      (the normalisation, i and not a free constant)")
check("the mode is correctly normalised — the Wronskian is i, so the amplitudes below are not rescalable",
      sp.simplify(wronskian - sp.I) == 0)

# =========================================================================================
print()
print("=" * 94)
print("PART 2 (CANDIDATE c) — THE SUBSTRATE'S CURVATURE RADIUS: IT CANNOT ENTER, FOR EVERY alpha")
print("=" * 94)
print("""
  The claim is not that alpha's effect is small.  It is that alpha is absent from the equation that governs
  the modes, so there is nothing for it to tilt.
""")
mode_eq_general = sp.diff(sp.Function('u')(eta), eta, 2) + (k ** 2 - 2 / eta ** 2) * sp.Function('u')(eta)
print(f"    the mode equation's free symbols: {sorted(str(s) for s in mode_eq_general.free_symbols)}")
check("⚑ alpha does not appear in the substrate's mode equation at all — the one length drops out of it",
      al not in mode_eq_general.free_symbols)

# the whole k-dependence is the normalisation: k^3 |u|^2 eta^2 is k-free
amp2 = sp.expand(u_bd * sp.conjugate(u_bd))
growing = sp.simplify(sp.limit(amp2 * k ** 3 * eta ** 2, eta, 0))
print(f"    k^3 eta^2 |u_k|^2  ->  {growing}   as eta -> 0     (no k, so the spectrum is flat exactly)")
check("the late-time combination that forms the spectrum is exactly k-independent",
      k not in sp.simplify(growing).free_symbols)

# and alpha reappears only as a prefactor: P = H^2/(4 pi^2) = 1/(4 pi^2 alpha^2)
P_dS = 1 / (4 * sp.pi ** 2 * al ** 2)
ns_minus_1_massless = sp.simplify(k * sp.diff(P_dS, k) / P_dS)
print(f"    P(k) = 1/(4 pi^2 alpha^2)      d ln P / d ln k = {ns_minus_1_massless}")
check("⚑ so alpha sets A_s and reaches n_s not at all: d ln P / d ln k = 0 identically, for every alpha",
      ns_minus_1_massless == 0)
check("and the dependence on alpha is genuinely there in the AMPLITUDE, so this is a division of labour "
      "and not a claim that alpha is absent from the physics", al in P_dS.free_symbols)

# =========================================================================================
print()
print("=" * 94)
print("PART 3 (CANDIDATE a) — THE PROGENITOR'S MASS: THE FORCED MEMBER LOCKS IT TO alpha")
print("=" * 94)
print("""
  A mass is a length, so on its face it is a second scale.  On the forced member it is not: the Nariai
  condition is one equation relating M to alpha, and it leaves a pure number.
""")
ratio = sp.simplify(M_N / al)
print(f"    M/alpha = {ratio} = {float(ratio):.9f}        a pure number, with no room for a k")
check("M/alpha is a dimensionless constant carrying neither alpha nor k",
      al not in ratio.free_symbols and k not in ratio.free_symbols and ratio.is_number)
check("M/alpha = 1/(3 sqrt3) exactly", sp.simplify(ratio - 1 / (3 * sp.sqrt(3))) == 0)
print("""
    ⇒ so the progenitor's mass is the curvature radius up to 0.192450, and Part 2 disqualifies it by the
      same argument: a scale absent from the mode equation cannot tilt the spectrum, and M brings no length
      the mode equation did not already fail to contain.
""")
# the honest counterfactual: on a NON-forced member M/alpha would be a free knob
M_free = sp.Symbol('M_free', positive=True)
knob = sp.simplify(M_free / al)
check("the disqualification is specific to the forced member — off it, M/alpha is a free knob and this "
      "argument would not run", M_free in knob.free_symbols and al in knob.free_symbols)

# =========================================================================================
print()
print("=" * 94)
print("PART 4 (CANDIDATE b) — THE FINITE DURATION: IT CAN ENTER, AND IT ENTERS AS AN OSCILLATION")
print("=" * 94)
print("""
  A finite duration sets the vacuum at a finite eta_0, which is the one way a new dimensionless variable
  x = k|eta_0| appears.  Match the substrate modes to instantaneous positive-frequency data there and read
  off what the late-time spectrum does.
""")
xx = sp.Symbol('xx', positive=True)
a_, b_ = 1 / xx, 1 / xx ** 2 - 1
p_, q_ = 1 + sp.I * a_, a_ + sp.I * b_          # u(eta_0) and u'(eta_0) stripped of common factors
D = sp.simplify(p_ * sp.conjugate(q_) - sp.conjugate(p_) * q_)
alpha_k = sp.simplify(sp.expand((sp.conjugate(q_) + sp.I * sp.conjugate(p_)) / D))
beta_k = sp.simplify((-sp.I * p_ - q_) / D) * sp.exp(2 * sp.I * xx)
print(f"    the matching determinant is {D} — constant, so the coefficients are elementary")
print(f"    alpha_k = {alpha_k}")
print(f"    beta_k  = {sp.simplify(beta_k)}")
check("the Bogoliubov normalisation |alpha|^2 - |beta|^2 = 1 holds EXACTLY, so the matching is a change of "
      "vacuum and not a loss of the state",
      sp.simplify(sp.expand(sp.Abs(alpha_k) ** 2 - sp.Abs(beta_k) ** 2)) == 1)
check("beta_k is non-zero, so the finite duration genuinely enters rather than cancelling",
      sp.simplify(beta_k) != 0)

R_closed = 1 + sp.cos(2 * xx) / xx ** 2 - sp.sin(2 * xx) / xx ** 3 + (1 - sp.cos(2 * xx)) / (2 * xx ** 4)
_z = alpha_k - beta_k                            # the late-time growing-mode coefficient
R_direct = sp.expand(sp.expand_complex(_z * sp.conjugate(_z)))
check("⚑ the power ratio is the closed form R(x) = 1 + cos2x/x^2 - sin2x/x^3 + (1-cos2x)/2x^4",
      sp.simplify(R_direct - R_closed) == 0)
check("and the same identity holds on the real and imaginary parts taken separately, so it is not an "
      "artefact of one simplification route",
      sp.simplify(sp.expand(sp.re(_z) ** 2 + sp.im(_z) ** 2 - R_closed)) == 0)
check("and it returns to the scale-free answer as the duration grows: R -> 1 as x -> oo",
      sp.limit(R_closed, xx, sp.oo) == 1)

tilt = sp.simplify(xx * sp.diff(R_closed, xx) / R_closed)
lead = -2 * sp.sin(2 * xx) / xx
print(f"""
    d ln R / d ln k = x R'(x)/R(x), with leading asymptotic -2 sin(2x)/x:

      {'x':>6} {'R(x)':>12} {'dlnR/dlnk':>12} {'-2sin2x/x':>12}""")
agree = []
for X in (1, 2, 5, 10, 30, 100, 300):
    t, l = float(tilt.subs(xx, X)), float(lead.subs(xx, X))
    print(f"      {X:>6} {float(R_closed.subs(xx, X)):>12.8f} {t:>+12.6f} {l:>+12.6f}")
    if X >= 10:
        agree.append(abs(t - l))
check("the leading asymptotic -2 sin(2x)/x tracks the exact log-derivative beyond x = 10 "
      f"(max residual {max(agree):.4f})", max(agree) < 0.02)

f_tilt = sp.lambdify(xx, tilt, 'numpy')
grid = np.linspace(1.0, 40.0, 4001)
vals = np.array([f_tilt(v) for v in grid])
sgn = np.sign(vals)
n_changes = int(np.sum(sgn[1:] * sgn[:-1] < 0))
print(f"\n    sign changes of d ln R / d ln k over x in [1,40]: {n_changes}")
check("⚑ the sign ALTERNATES rather than being red or blue — a tilt has one sign and this has many",
      n_changes >= 20)
env = float(np.max(np.abs([f_tilt(v) for v in np.linspace(10, 40, 3001)])))
print(f"    envelope of |d ln R / d ln k| beyond x = 10: {env:.4f}")
check("the envelope decays — the effect is a feature near the cutoff scale, not a property of the spectrum",
      env < 0.2)

print("\n    and the operational test the corpus already uses — does the fitted tilt depend on the band?")
means = []
for lo, hi in ((2, 4), (4, 8), (8, 16), (16, 32)):
    band = np.array([f_tilt(v) for v in np.linspace(lo, hi, 2001)])
    means.append(band.mean())
    print(f"      band x in [{lo:2},{hi:2}]   mean {band.mean():+.6f}   min {band.min():+.6f}   "
          f"max {band.max():+.6f}")
check("⚑ the four band means do not agree with one another and do not even share a sign, so there is no "
      f"constant for a tilt fit to return ({', '.join(f'{m:+.4f}' for m in means)})",
      min(means) < 0 < max(means))
_ptp = [float(np.ptp(np.array([f_tilt(v) for v in np.linspace(lo, hi, 2001)])))
        for lo, hi in ((2, 4), (4, 8), (8, 16), (16, 32))]
print(f"      within-band spread / |band mean|: "
      f"{', '.join(f'{t / abs(m):.1f}' for t, m in zip(_ptp, means))}")
check("and in every band the within-band spread exceeds that band's own mean by more than a factor ten — "
      "which is what band dependence looks like, and the opposite of a tilt",
      all(t > 10 * abs(m) for t, m in zip(_ptp, means)))

# =========================================================================================
print()
print("=" * 94)
print("PART 5 — THE ONE CHANNEL THAT GIVES A CONSTANT TILT, AND THE SIGN IT COMES WITH")
print("=" * 94)
print("""
  None of the three candidates delivers a tilt, so the order's stopping rule is reached.  What survives it
  is the sign question, and it has an exact answer through the only quantity that CAN produce a constant
  log-derivative on a maximally symmetric background: an effective mass.
""")
nu = sp.sqrt(sp.Rational(9, 4) - mu)
ns_minus_1 = sp.simplify(3 - 2 * nu)
print(f"    nu = sqrt(9/4 - m^2 alpha^2),   n_s - 1 = {ns_minus_1}")
print(f"    series about the massless point: {sp.series(ns_minus_1, mu, 0, 3)}")
check("the massless limit returns the scale-free spectrum exactly, joining Part 2",
      ns_minus_1.subs(mu, 0) == 0)
check("the leading coefficient is +2/3, so a POSITIVE effective mass-squared gives a BLUE tilt",
      sp.limit(ns_minus_1 / mu, mu, 0) == sp.Rational(2, 3))
check("and the map is monotonic in m^2 over the light-field range, so the sign statement is not local to "
      "the origin",
      all(float(sp.diff(ns_minus_1, mu).subs(mu, v)) > 0 for v in (-1, sp.Rational(-1, 100), 0, 1, 2)))

TARGET = sp.Rational(-5, 1000)                   # n_s - 1 = -0.005, the refit's preference (r6805)
mu_needed = sp.solve(sp.Eq(ns_minus_1, TARGET), mu)[0]
print(f"""
    the measured target on this construction's own background is n_s = 0.995, i.e. n_s - 1 = -0.005:

      m^2 alpha^2 = {mu_needed} = {float(mu_needed):+.8f}       => slightly TACHYONIC
""")
check("reaching the measured tilt requires a NEGATIVE effective mass-squared — the data want red and a "
      "positive mass gives blue", float(mu_needed) < 0)
check("and the requirement is small, |m^2 alpha^2| < 0.01, so it is a light-field statement and the "
      "expansion above applies to it", abs(float(mu_needed)) < sp.Rational(1, 100))
check("the inversion is exact rather than fitted: substituting it back returns -0.005 identically",
      sp.simplify(ns_minus_1.subs(mu, mu_needed) - TARGET) == 0)
# and the standard model's own tilt, for the comparison the order names
mu_sm = sp.solve(sp.Eq(ns_minus_1, sp.Rational(-35, 1000)), mu)[0]
print(f"    for comparison, the standard model's 1 - n_s = 0.035 would need m^2 alpha^2 = "
      f"{float(mu_sm):+.8f}")
check("the target on this background is nearer the scale-free point than the standard model's by roughly "
      "an order of magnitude, which is the possibility the order asked to have stated",
      abs(float(mu_needed)) < abs(float(mu_sm)) / 4)

# =========================================================================================
print()
print("=" * 94)
print("VERDICT")
print("=" * 94)
print(f"""
  ⚑ OF THE THREE CANDIDATES, TWO CANNOT ENTER AND THE THIRD DOES NOT PRODUCE A TILT.

    the substrate's curvature radius alpha   CANNOT ENTER   absent from the mode equation; sets A_s alone
    the progenitor's mass M                  CANNOT ENTER   locked to alpha by Lambda M^2 = 1/9, a pure
                                                            number ({float(ratio):.6f}), so no new length
    the finite duration of the collapse      ENTERS         but as R(x) above: an oscillation decaying as
                                                            1/x, sign alternating {n_changes} times on [1,40],
                                                            band means disagreeing in sign

  ⇒ SO THE SUBSTRATE ALONE FIXES n_s = 1 EXACTLY, AND A CONSTANT TILT NEEDS THE INTERIOR.  The only
    quantity that can produce a band-independent log-derivative on a maximally symmetric background is an
    effective mass, exactly n_s - 1 = 3 - 2 sqrt(9/4 - m^2 alpha^2), BLUE for m^2 > 0 -- so the measured
    n_s = 0.995 requires m^2 alpha^2 = {float(mu_needed):+.8f}, slightly tachyonic.

  ⌗ That is a requirement on the interior and not a result about it, and it is the frontier's new edge:
    the row is no longer "what does the progenitor supply" in general but "what gives the perturbation a
    small negative effective mass-squared on the substrate".
""")
print(f"  {sum(_checks)}/{len(_checks)} checks passed.")
sys.exit(0 if all(_checks) else 1)
