"""
LEVEL: exact symbolic throughout, with a CONTROL that must make the signed-radius
reading give the wrong answer for two other species.

WHY THIS PROBE EXISTS.  PO-88's discharge condition is a concrete model's stress-energy
carried THROUGH the branch point as a dynamical problem rather than a transmitted datum.
`r7465+cc66.5` fixed the depth and the clock -- the regulated peak is rho_Planck/(6 pi),
the approach from the horizon lasts 4.364 Gyr of proper time -- and integrated no flow.
What was left is the crossing itself: the approach has gigayears of freedom, so does any
of it reach the other side, and in what form?

WHAT IS CLAIMED.
  (1) THE TWO CONTINUATIONS THE CORPUS USES AGREE, AND THEY AGREE ON ODD.  P3 sec:lap
      rides through r=0 onto the negative branch, where r = alpha sin(theta) is odd in
      theta.  P2's law r^3 = 2 M alpha^2 sinh^2(3 tau / 2 alpha) is EVEN under a
      reflection in tau -- but that reflection never leaves the forward branch, because
      sinh^2 >= 0 for real tau.  Under the continuation P2 actually uses, the imaginary
      offset at the conjugate critical point, r^3 becomes NEGATIVE, equal to
      -2 M alpha^2 at the critical point itself.  Both therefore carry r through zero.
  (2) THE NAIVE DUST DENSITY 3 M /(4 pi r^3) IS ODD IN r, hence changes sign across the
      branch point, which is not a state matter can be in.
  (3) THE DENSITY IS EVEN ON THE UNSIGNED RADIUS.  The denominator is a VOLUME, and P3
      states the areal radius is a SIGNED coordinate with g_thth = r^2 insensitive to
      its sign, so the volume goes as |r|^3.  On |r| the density is even.
  (4) THE AREAL RATE RELATIVE TO THE MATTER's OWN OUTWARD DIRECTION IS ODD:
      d|r|/dtheta flips sign through the branch point, so infall becomes outflow.
  (5) THE CROSSING IS AN INVOLUTION, hence a bijection on the state space:
      (rho(l), v(l)) -> (rho(-l), -v(-l)) applied twice is the identity.  So nothing is
      lost and nothing is added, and the crossing is not a filter.

WHAT IS NOT CLAIMED.  Nothing about a model WITH PRESSURE.  Dust has only a density and
a radial rate to carry a parity; T^r_r and T^theta_theta are not carried across here,
and P16's own interior is dust PLUS radiation.  Nothing about what the evolution does
with the freedom on the approach -- only that the crossing transmits it bijectively.  And
no claim that the involution is a symmetry of anything beyond these components.

WHAT WOULD FALSIFY IT.  The two continuations disagreeing on whether r changes sign; the
naive density turning out even; the unsigned density turning out odd; the areal rate not
flipping; the map failing to be its own inverse; or -- the discriminator -- the CONTROL
failing, i.e. the signed-radius reading giving the SAME parity for radiation and stiff
matter as for dust.  It must not: on the signed radius the parity follows the exponent's
parity (3 odd, 4 and 6 even), which is not a physical distinction, and that is the tell
that the signed radius is the wrong variable for a density.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print("=" * 78)
print("  P16 / PO-88 -- THE CROSSING IS AN INVOLUTION, AND THE DENSITY IS EVEN")
print("  ON THE UNSIGNED RADIUS")
print("=" * 78)

alpha, M, Mb = sp.symbols('alpha M M_b', positive=True)
theta, tau = sp.symbols('theta tilde_tau', real=True)
r = sp.Symbol('r', real=True)

# ---- (1) the two continuations ---------------------------------------------
r_P3 = alpha * sp.sin(theta)
check("P3's arc-length radius is ODD through the branch point theta = 0",
      sp.simplify(r_P3.subs(theta, -theta) + r_P3) == 0,
      sp.simplify(r_P3.subs(theta, -theta)))

r3 = 2 * M * alpha**2 * sp.sinh(3 * tau / (2 * alpha))**2
check("P2's law is EVEN under a reflection in proper time",
      sp.simplify(r3.subs(tau, -tau) - r3) == 0)
# â A first draft of this check ended in `or True`, which cannot fail -- the
#   exact class this family has now measured four times, written by the seat that
#   measured it.  Replaced with a real assertion: the set of real proper times at
#   which the law is negative must be EMPTY.
neg_set = sp.solveset(r3 < 0, tau, sp.S.Reals)
check("but that reflection cannot leave the forward branch: the set of real proper "
      "times with r^3 < 0 is EMPTY",
      neg_set == sp.S.EmptySet, f"solveset gave {neg_set}")
# the continuation P2 uses: the imaginary offset at the conjugate critical point
r3_cont = sp.simplify(sp.expand_trig(r3.subs(tau, -sp.I * sp.pi * alpha / 3 + tau)))
check("under P2's imaginary offset the law becomes -2 M alpha^2 cosh^2, i.e. NEGATIVE",
      sp.simplify(r3_cont + 2 * M * alpha**2 * sp.cosh(3 * tau / (2 * alpha))**2) == 0,
      r3_cont)
check("and at the conjugate critical point itself r^3 = -2 M alpha^2 exactly",
      sp.simplify(r3_cont.subs(tau, 0) + 2 * M * alpha**2) == 0,
      sp.simplify(r3_cont.subs(tau, 0)))
check("⇒ THE TWO CONTINUATIONS AGREE: both carry r through zero onto a negative branch",
      sp.simplify(r_P3.subs(theta, -theta) + r_P3) == 0
      and sp.simplify(r3_cont.subs(tau, 0) + 2 * M * alpha**2) == 0)

# ---- (2) and (3) the density ----------------------------------------------
rho_naive = 3 * Mb / (4 * sp.pi * r**3)
check("the naive dust density on the SIGNED radius is ODD, so it changes sign",
      sp.simplify(rho_naive.subs(r, -r) + rho_naive) == 0,
      sp.simplify(rho_naive.subs(r, -r)))
rho_true = 3 * Mb / (4 * sp.pi * sp.Abs(r)**3)
check("the density on the UNSIGNED radius is EVEN, as a density must be",
      sp.simplify(rho_true.subs(r, -r) - rho_true) == 0,
      sp.simplify(rho_true.subs(r, -r)))

# ---- (4) the areal rate ----------------------------------------------------
dr = sp.diff(r_P3, theta)
check("the SIGNED areal rate dr/dtheta is EVEN in theta",
      sp.simplify(dr.subs(theta, -theta) - dr) == 0, dr)
dabs = sp.simplify(sp.diff(sp.Abs(r_P3), theta))
check("but the rate relative to the matter's own outward direction, d|r|/dtheta, is ODD "
      "-- infall becomes outflow",
      sp.simplify(sp.simplify(dabs.subs(theta, -theta)) + dabs) == 0)

# ---- (5) the involution ----------------------------------------------------
l = sp.Symbol('l', real=True)
R = sp.Function('R')          # an arbitrary even density history
V = sp.Function('V')          # an arbitrary odd rate history
# the crossing map: (rho(l), v(l)) -> (rho(-l), -v(-l))
def crossing(pair):
    f, g = pair
    return (f.subs(l, -l), -g.subs(l, -l))
pair0 = (R(l), V(l))
once = crossing(pair0)
twice = crossing(once)
check("the crossing map applied twice is the identity -- an INVOLUTION, hence a "
      "bijection on the state space",
      sp.simplify(twice[0] - pair0[0]) == 0 and sp.simplify(twice[1] - pair0[1]) == 0,
      f"{twice}")

# ---- the CONTROL -----------------------------------------------------------
print()
print("  CONTROL -- on the SIGNED radius the parity must follow the exponent, giving")
print("  radiation and stiff matter the OPPOSITE answer to dust.  If it does not, the")
print("  EVEN result above came from arithmetic and not from the volume being a volume.")
for label, expo, want_odd in (("dust      r^-3", 3, True),
                              ("radiation r^-4", 4, False),
                              ("stiff     r^-6", 6, False)):
    f_signed = r**(-expo)
    is_odd = sp.simplify(f_signed.subs(r, -r) + f_signed) == 0
    check(f"CONTROL signed: {label} is {'ODD' if want_odd else 'EVEN'}",
          is_odd == want_odd, f"odd={is_odd}")
    f_abs = sp.Abs(r)**(-expo)
    check(f"CONTROL unsigned: {label} is EVEN, as every density must be",
          sp.simplify(f_abs.subs(r, -r) - f_abs) == 0)

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  The two continuations the corpus uses agree and both carry")
print("  r through zero onto a negative branch, so the crossing is a parity map and not")
print("  a reflection within one leg.  The dust density is ODD on the signed radius --")
print("  which would be a negative mass density -- and EVEN on the unsigned radius,")
print("  which is the one a volume uses; the rate relative to the matter's own outward")
print("  direction is ODD, so infall becomes outflow.  The resulting map is its own")
print("  inverse, hence a bijection: the crossing is NOT a filter, nothing is lost and")
print("  nothing is added, and PO-88's 'transmitted datum' is the whole approach.  The")
print("  control confirms the EVEN answer comes from the volume and not the arithmetic.")
print("  ⛔ NO PRESSURE IS CARRIED ACROSS: dust only.")
print("=" * 78)
