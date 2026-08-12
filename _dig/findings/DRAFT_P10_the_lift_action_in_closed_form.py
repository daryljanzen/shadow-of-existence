"""
DRAFT_P10_the_lift_action_in_closed_form.py -- P10 sec:deparam / P7 sec:lift-quantum:
** THE LIFT'S GRAVITATIONAL EUCLIDEAN ACTION IS S_E = -M alpha / 4G EXACTLY. **
The integral is elementary, the integrand has no endpoint singularity, and the action is LINEAR
IN THE PROGENITOR MASS -- which the quoted single number cannot show.

WHAT THE CORPUS HAS.  P10 eq:grav-action derives
    S_E^grav = (3/4pi) INT ds  r r'^2 = (3/4pi) INT ds  r [f(r) - 1]
and says: "** The integral converges rapidly and gives S_E^grav = -0.0481 alpha^2/G on the forced
member. **"  P7 sec:lift-quantum quotes the same number.  `LIFT_gravitational_action` evaluates it
by quadrature from three lower cutoffs (1e-4, 1e-6, 1e-8) and returns -0.048113.

WHAT IS ADDED.  The integrand collapses.  On the lift
    r(s) = -A |sin(3s/2 alpha)|^{2/3},     A = (2 M alpha^2)^{1/3},     0 <= s <= pi alpha/3,
so with A^3 = 2 M alpha^2,

    ** r (f - 1) = -2M - r^3/alpha^2 = -2M + 2M sin^2(3s/2 alpha) = -2M cos^2(3s/2 alpha). **

A pure cosine-squared.  Over the segment's full extent that is a QUARTER PERIOD:

    INT_0^{pi alpha/3} -2M cos^2(3s/2 alpha) ds = -2M (2 alpha/3)(pi/4) = -M pi alpha/3,

    ** S_E^grav = (3/4pi)(-M pi alpha/3) = -M alpha / 4    (G = 1). **

Three things follow that the number alone does not carry.

① ** THE ACTION IS LINEAR IN THE PROGENITOR MASS. **  The quoted -0.0481 alpha^2/G is the value at
   the forced member M = alpha/(3 sqrt 3) -- and P10 says "on the forced member", so nothing is
   misstated.  But a reader who wants the lift's weight for ANY progenitor needs the scaling, and
   S_E = -M alpha/4G gives it in one symbol.  ** The beginning's Euclidean weight is proportional
   to the mass of the hole it came through. **

② ** THERE IS NO ENDPOINT SINGULARITY, so the cutoff ladder is measuring nothing. **  r ~ s^{2/3}
   and (f-1) ~ s^{-2/3} near s = 0; the product is -2M cos^2, bounded and smooth on the CLOSED
   segment, with r(f-1) -> -2M exactly at the branch-point end.  The receipt's convergence study
   from 1e-4 / 1e-6 / 1e-8 is a study of a removable factorisation, not of the integral.  ** And
   "converges rapidly" understates the result: it does not converge rapidly, it closes. **

③ ** THE HARTLE-HAWKING COMPARISON BECOMES EXACT AND MASS-DEPENDENT. **  P10 compares to the
   no-boundary de Sitter action, which it gives as -alpha^2/8G in its convention, and says the
   lift's value is "the same sign and the same order, smaller by a factor of order two".  With
   the closed form the ratio is exact:
       S_E^lift / S_E^dS = (M alpha/4) / (alpha^2/8) = ** 2M/alpha **,
   which at the forced member is 2/(3 sqrt 3) = 0.3849 -- ** a factor of alpha/2M = 3 sqrt 3/2 =
   2.598 smaller, not "of order two". **  And the factor is not a constant: it is the
   construction's own dimensionless mass 2M/alpha, the same combination the horizon cubic runs on.
   ⚠ *This item takes P10's -alpha^2/8G at its word; it is a statement ABOUT the ratio, not an
   independent check of the de Sitter value in that convention.*

AND ONE LABELLING SLIP, in a sibling receipt.  `LIFT_instanton_action.py` prints
    "lift: s in (0, pi a/3];  r(0)= -A = -0.727416 (turnaround) -> r(pi a/3)=0 (branch point)"
while its own r_of gives r(0) = 0 and r(pi a/3) = -A.  ** The endpoints are swapped in the
sentence, and the table printed two lines below shows the correct behaviour. **  The action is an
integral over the segment and is unchanged by the orientation, so nothing computed is affected --
including the sign, which P10 correctly traces to the segment lying on the r < 0 branch rather
than to a direction of travel.  It is a one-line fix in a receipt whose table already refutes it.

HONEST WEIGHT.  ** No new physics. **  This is P10's own integral, done in closed form.  Every
value below agrees with `LIFT_gravitational_action`'s quadrature to six figures.  What is claimed
is that the closed form carries three things the number cannot: the mass scaling, the absence of
the singularity the cutoff study is guarding against, and an exact ratio where the paper has
"of order two".

STATED FOR REVERSAL.  If -M alpha/4G is written somewhere I did not find, strike this.  Searched
`M\\alpha/4`, `linear in M`, `linear in the mass`, `proportional to M`, `0.0481` across corpus/,
receipts/, computations/ and storyboard_receipts/.
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad

print(__doc__)

# ============================================================================
print("=" * 78)
print("PART 1 — THE INTEGRAND COLLAPSES TO A COSINE-SQUARED")
print("=" * 78)
al, M, s = sp.symbols('alpha M s', positive=True)
A = (2 * M * al**2)**sp.Rational(1, 3)
r = -A * sp.sin(3 * s / (2 * al))**sp.Rational(2, 3)
f = 1 - 2 * M / r - r**2 / al**2

expr = sp.simplify(sp.powsimp(sp.expand(r * (f - 1)), force=True))
target = -2 * M * sp.cos(3 * s / (2 * al))**2
resid = sp.simplify(sp.trigsimp(sp.expand_trig(sp.simplify(expr - target))))
print(f"  r (f - 1)                     = {sp.simplify(expr)}")
print(f"  residual against -2M cos^2(3s/2a) : {resid}")
assert resid == 0

print()
print("  ⌗ *the cancellation, in one line: r(f-1) = -2M - r^3/alpha^2, and r^3 = -A^3 sin^2")
print("     = -2M alpha^2 sin^2, so r(f-1) = -2M(1 - sin^2) = -2M cos^2.*")
print(f"  value at the branch-point end s = 0 : {sp.simplify(expr.subs(s, 0))}   (finite)")
print(f"  value at the turnaround   s = pi a/3: {sp.simplify(expr.subs(s, sp.pi*al/3))}   (finite)")
assert sp.simplify(expr.subs(s, 0) + 2*M) == 0
assert sp.simplify(expr.subs(s, sp.pi*al/3)) == 0

# ============================================================================
print()
print("=" * 78)
print("PART 2 — THE ACTION, IN CLOSED FORM")
print("=" * 78)
I = sp.integrate(target, (s, 0, sp.pi * al / 3))
S = sp.simplify(sp.Rational(3, 4) / sp.pi * I)
print(f"  INT_0^{{pi a/3}} r(f-1) ds = {sp.simplify(I)}")
print(f"  S_E^grav = (3/4pi) x that = {S}")
assert sp.simplify(S + M * al / 4) == 0
print()
print("  ** S_E^grav = - M alpha / 4     (G = 1) **")
print("  ⌗ *the pi cancels: the quarter-period of cos^2 supplies pi/4 and the prefactor 3/4pi")
print("     removes it, which is why the answer is rational in M and alpha.*")

# ============================================================================
print()
print("=" * 78)
print("PART 3 — AGAINST THE CORPUS'S QUADRATURE")
print("=" * 78)
a_ = 1.0
M_forced = a_ / (3 * np.sqrt(3))
A_ = (2 * M_forced * a_**2)**(1. / 3)
fn = lambda x: 1 - 2 * M_forced / x - x * x / a_**2
r_of = lambda t: -A_ * np.abs(np.sin(1.5 * t / a_))**(2. / 3)
integ = lambda t: (3.0 / (4 * np.pi)) * r_of(t) * (fn(r_of(t)) - 1.0)
smax = np.pi * a_ / 3
print(f"  forced member: M = alpha/(3 sqrt3) = {M_forced:.9f},  A = (2M a^2)^(1/3) = {A_:.6f}")
print()
print(f"  {'lower cutoff':>16} {'quadrature':>16} {'closed form -M a/4':>22} "
      f"{'difference':>13} {'predicted 3M eps/2pi':>21}")
closed = -M_forced * a_ / 4
for lo in (1e-4, 1e-6, 1e-8, 0.0):
    val, _ = quad(integ, lo, smax, limit=800, points=[0] if lo == 0 else None)
    lbl = 'none (full)' if lo == 0 else f'{lo:.0e}'
    pred = (3.0 / (4 * np.pi)) * 2 * M_forced * lo          # the truncated cos^2 ~ 1 near s=0
    print(f"  {lbl:>16} {val:>16.9f} {closed:>22.9f} {val-closed:>13.2e} {pred:>21.2e}")
    assert abs((val - closed) - pred) < max(1e-9, 0.02 * pred)
print()
print("  ** the cutoff ladder is not regularising a singularity -- it is TRUNCATING a regular")
print("     integral, and the missing piece is exactly (3/4pi)(2M)eps, linear in the cutoff. **")
print("     The predicted column above is that formula; it reproduces the shortfall at every eps.")
print()
print(f"  ** the corpus's printed value  : -0.048113 **")
print(f"  ** the closed form at M forced : {closed:.9f} = -alpha^2/(12 sqrt3 G) **")
print(f"     -1/(12 sqrt 3) = {-1/(12*np.sqrt(3)):.9f}")
assert abs(closed - (-1 / (12 * np.sqrt(3)))) < 1e-12
print("  ⌗ *so the quoted -0.0481 alpha^2/G is exactly -alpha^2/(12 sqrt3 G).*")

# ============================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE SCALING SAYS, AND THE RATIO THE PAPER GIVES AS 'OF ORDER TWO'")
print("=" * 78)
print(f"  {'2M/alpha':>10} {'M (alpha=1)':>13} {'S_E = -M a/4':>15} {'S_E / (-a^2/8)':>16}")
for x in (0.05, 0.1, 0.2, 2 / (3 * np.sqrt(3)), 0.5, 0.6):
    Mv = x / 2
    tag = '   <-- forced member (Nariai)' if abs(x - 2 / (3 * np.sqrt(3))) < 1e-12 else ''
    print(f"  {x:>10.5f} {Mv:>13.6f} {-Mv/4:>15.7f} {(-Mv/4)/(-1/8):>16.5f}{tag}")
print()
print("  ** S_E^lift / S_E^dS = (M a/4)/(a^2/8) = 2M/alpha exactly. **")
print(f"     at the forced member 2M/a = 2/(3 sqrt3) = {2/(3*np.sqrt(3)):.6f},")
print(f"     i.e. smaller by a factor a/2M = 3 sqrt3/2 = {3*np.sqrt(3)/2:.4f} -- not 'of order two'.")
print("  ⚠ *this takes P10's own -alpha^2/8G for the no-boundary value; it is a statement about")
print("     the RATIO, not an independent check of that number in that convention.*")

# ============================================================================
print()
print("=" * 78)
print("PART 5 — THE ENDPOINT LABELS IN `LIFT_instanton_action` ARE SWAPPED")
print("=" * 78)
print("  that receipt prints:")
print("     'lift: s in (0, pi a/3];  r(0)= -A = -0.727416 (turnaround) -> r(pi a/3)=0 (branch point)'")
print()
print(f"  {'s':>10} {'r_of(s)':>12}")
for t in (0.0, 0.2, 0.5, smax):
    print(f"  {t:>10.5f} {r_of(t):>12.6f}")
print()
print(f"  ** r(0) = {r_of(0.0):.6f}, not -A;  r(pi a/3) = {r_of(smax):.6f} = -A, not 0. **")
assert abs(r_of(0.0)) < 1e-12 and abs(r_of(smax) + A_) < 1e-9
print("  ⌗ *the table two lines below that sentence already shows it (r grows in magnitude with s).")
print("     Nothing computed is affected: the action is an integral over the segment and is")
print("     orientation-independent, and P10 traces the SIGN to the segment lying on the r < 0")
print("     branch, not to a direction of travel.  A one-line fix.*")

print()
print("=" * 78)
print("NOT CLAIMED")
print("=" * 78)
for line in [
 "· No new physics.  This is P10 eq:grav-action's own integral, evaluated in closed form.",
 "· No claim that -0.0481 is wrong: it is exactly -1/(12 sqrt3) and the paper attaches it to the",
 "  forced member, which is correct.",
 "· No independent check of the -alpha^2/8G de Sitter comparison value in P10's convention.",
 "· Nothing about the quantum status of the lift, which P10 is explicit is not established, nor",
 "  about the adiabatic correction, which is a different receipt.",
 "· No closure on any registered item.",
]:
    print("  " + line)
