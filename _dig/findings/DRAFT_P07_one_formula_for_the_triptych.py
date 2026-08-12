"""
DRAFT_P07_one_formula_for_the_triptych.py -- P7 fig:F-triptych / sec:lift-initial-rate:
** ONE CLOSED FORM GIVES THE ACCELERATION AT ALL FOUR MARKED LOCI OF THE LAP, and it turns the
   paper's 'order of contact' distinction between the two seams into a one-line identity. **

WHAT THE CORPUS HAS.  The triptych caption is already excellent and already carries the
organising structure:
  * "every unit-speed locus is a root of f(f-2)=0, ** one cubic family r^3 - c r + 2M = 0 in
    c = 1-f **: c=+1 gives the three-root Weyl triple whose real members are the seams, c=0 the
    turnaround, and c=-1 the Euclidean null."
  * the turnaround corner IN CLOSED FORM: "the acceleration jumps sign through a finite corner,
    -+ (3/2)(2 M alpha^2)^{1/3}".
  * the two seams distinguished "not by the presence or absence of a feature but by ** order of
    contact **" -- the front seam tangential with the acceleration vanishing, the back seam
    transversal with acceleration "(-1.299)".
  * the Euclidean null "transversal with acceleration (+1.969)".

So three of the four accelerations are quoted as decimals beside a family that is already
written down as a cubic.  ** They all follow from it. **

THE FORMULA.  The marginal congruence obeys (dr/dtau~)^2 = 1 - f.  Differentiating,
2 r' r'' = -f'(r) r', so on the REAL segments r'' = -f'/2 = r/alpha^2 - M/r^2.  On the LIFT
tau~ = is, so (dr/ds)^2 = f - 1 and the sign flips: r'' = +f'/2.  Eliminating M with the locus's
own cubic r^3 - c alpha^2 r + 2 M alpha^2 = 0 gives

    ** r'' = eps (3 r^2 - c alpha^2) / (2 r alpha^2),     eps = +1 real segments, -1 on the lift **

and that single expression returns every marked value:

    front seam      c=+1, r=+alpha/sqrt3     ->  ** 0 EXACTLY **        (paper: "vanishing")
    back seam       c=+1, r=-2alpha/sqrt3    ->  ** -3 sqrt3/(4 alpha) = -1.299038 **
    turnaround      c= 0, r=-(2M alpha^2)^{1/3} -> ** -(3/2)(2M alpha^2)^{1/3}/alpha^2 **
    Euclidean null  c=-1, r = the real root  ->  ** -(3r^2+alpha^2)/(2 r alpha^2) = +1.969138 **

** AND THE 'ORDER OF CONTACT' BECOMES AN IDENTITY. **  The numerator vanishes exactly when
3 r^2 = c alpha^2.  At c = +1 that is r = +- alpha/sqrt3 -- and the front seam sits at
+alpha/sqrt3 while the back seam sits at -2alpha/sqrt3.  ** So the front seam is tangential
BECAUSE its radius is the one that solves 3r^2 = alpha^2, which is the Nariai radius; the back
seam is transversal because -2alpha/sqrt3 does not. **  The paper's distinction between the two
seams -- the point of that passage -- is the question of which root of the seam cubic also solves
3 r^2 = alpha^2, and only one of the three does.

⌗ *And that reads back: the seam cubic's three roots at Nariai are -2alpha/sqrt3 and the doubled
+alpha/sqrt3.  ** It is the DOUBLED root that is tangential. **  The order of contact of the
contour with the null level is the multiplicity of the root -- the same doubling that makes the
member Nariai.*

HONEST WEIGHT.  ** No new physics and no number changes. **  Every value below agrees with the
caption.  What is claimed: the caption states a cubic family and then quotes three decimals that
the family determines; one formula supplies all four, gives the front seam's zero as a
consequence rather than an observation, and identifies the order-of-contact distinction with root
multiplicity.

STATED FOR REVERSAL.  If this formula is written somewhere I did not find, strike this.  Searched
`-1.299`, `1.969`, `order of contact`, `f'/2`, `-f'/2`, `3r^2` across corpus/, receipts/,
computations/ and storyboard_receipts/, and read F_triptych.py.
"""
import numpy as np
import sympy as sp

print(__doc__)

al, M, r, c = sp.symbols('alpha M r c', positive=False)
al = sp.Symbol('alpha', positive=True)
M = sp.Symbol('M', positive=True)
r = sp.Symbol('r', nonzero=True)
c = sp.Symbol('c')

f = 1 - 2 * M / r - r**2 / al**2

# ============================================================================
print("=" * 78)
print("PART 1 — THE ACCELERATION FROM THE FIRST INTEGRAL")
print("=" * 78)
fp = sp.simplify(sp.diff(f, r))
acc_real = sp.simplify(-fp / 2)
print(f"  f  = {f}")
print(f"  f' = {fp}")
print(f"  (dr/dtau~)^2 = 1 - f   ->   r'' = -f'/2 = {acc_real}      [real segments]")
print(f"  (dr/ds)^2    = f - 1   ->   r'' = +f'/2 = {sp.simplify(fp/2)}      [the lift]")
assert sp.simplify(acc_real - (r / al**2 - M / r**2)) == 0

print()
print("  eliminate M with the locus's own cubic  r^3 - c alpha^2 r + 2 M alpha^2 = 0 :")
Msol = sp.solve(sp.Eq(r**3 - c * al**2 * r + 2 * M * al**2, 0), M)[0]
print(f"     M = {sp.simplify(Msol)}")
acc_c = sp.simplify(acc_real.subs(M, Msol))
target = (3 * r**2 - c * al**2) / (2 * r * al**2)
print(f"     r'' = {sp.simplify(acc_c)}")
print(f"     residual against (3r^2 - c alpha^2)/(2 r alpha^2) : "
      f"{sp.simplify(sp.together(acc_c - target))}")
assert sp.simplify(acc_c - target) == 0
print()
print("  ** r'' = eps (3 r^2 - c alpha^2) / (2 r alpha^2),   eps = +1 real, -1 on the lift **")

# ============================================================================
print()
print("=" * 78)
print("PART 2 — THE FOUR MARKED LOCI, FROM THE ONE FORMULA")
print("=" * 78)
A = (2 * M * al**2)**sp.Rational(1, 3)
M_N = al / (3 * sp.sqrt(3))                      # the Nariai / forced member


def accel(rv, cv, eps):
    return sp.simplify(eps * (3 * rv**2 - cv * al**2) / (2 * rv * al**2))


rows = [
    ("front seam      (tangential)", al / sp.sqrt(3), 1, +1),
    ("back seam       (transversal)", -2 * al / sp.sqrt(3), 1, +1),
    ("turnaround      (corner)", -A.subs(M, M_N), 0, +1),
]
print(f"  {'locus':<32} {'c':>3} {'r':>22} {'r'' (exact)':>26} {'numeric':>11}")
for name, rv, cv, eps in rows:
    a = sp.simplify(accel(rv, cv, eps).subs(M, M_N))
    print(f"  {name:<32} {cv:>3} {str(sp.simplify(rv.subs(M, M_N))):>22} "
          f"{str(sp.nsimplify(sp.radsimp(a))):>26} {float(a.subs(al, 1)):>11.6f}")

# the front seam is exactly zero
a_front = sp.simplify(accel(al / sp.sqrt(3), 1, 1))
assert a_front == 0
# the back seam is -3 sqrt3 / (4 alpha)
a_back = sp.simplify(sp.radsimp(accel(-2 * al / sp.sqrt(3), 1, 1)))
assert sp.simplify(a_back + 3 * sp.sqrt(3) / (4 * al)) == 0
print()
print(f"  ** front seam : EXACTLY 0        (paper: 'the acceleration vanishing') **")
print(f"  ** back seam  : -3 sqrt3/(4 alpha) = {float(-3*np.sqrt(3)/4):.6f}   (paper: -1.299) **")

# the turnaround corner, against the caption's own closed form
a_TA = sp.simplify(accel(-A, 0, 1))
print(f"  ** turnaround : {sp.simplify(a_TA)} "
      f"= -(3/2)(2M alpha^2)^(1/3)/alpha^2   (the caption's own form) **")
assert sp.simplify(a_TA + sp.Rational(3, 2) * A / al**2) == 0

# the Euclidean null: the real root of r^3 + alpha^2 r + 2 M alpha^2 = 0
print()
print("  the Euclidean null (c = -1) needs its root; the cubic is r^3 + alpha^2 r + 2M alpha^2 = 0")
rEN = [s for s in sp.solve(sp.Eq(r**3 + r + 2 * M_N.subs(al, 1), 0), r) if s.is_real][0]
rEN_n = float(rEN)
aEN = -(3 * rEN_n**2 + 1) / (2 * rEN_n)
print(f"     real root r = {rEN_n:.6f} alpha        (paper: -0.3441 alpha)")
print(f"     r'' = -(3r^2 + alpha^2)/(2 r alpha^2) = {aEN:.6f}   (paper: +1.969)")
print(f"     discriminant -4 alpha^6 - 27(2M alpha^2)^2 = "
      f"{float(-4 - 27*(2*M_N.subs(al,1))**2):.6f} < 0  -> the root is unique (the caption's own check)")
assert abs(rEN_n + 0.3441) < 5e-4 and abs(aEN - 1.969) < 5e-4

# ============================================================================
print()
print("=" * 78)
print("PART 3 — THE ORDER OF CONTACT IS THE ROOT MULTIPLICITY")
print("=" * 78)
print("  the numerator 3r^2 - c alpha^2 vanishes iff r = +- alpha sqrt(c/3).")
print("  at c = +1 that is r = +- alpha/sqrt3, and the seam cubic at the forced member is")
cub = sp.factor(sp.expand((r**3 - al**2 * r + 2 * M_N * al**2)))
print(f"     r^3 - alpha^2 r + 2 M alpha^2 = {cub}")
roots = sp.roots(sp.Poly(sp.expand(r**3 - al**2 * r + 2 * M_N * al**2), r))
print(f"     roots with multiplicity: "
      f"{ {sp.simplify(k): v for k, v in roots.items()} }")
print()
for line in [
 "** so the three roots are +alpha/sqrt3 (DOUBLED) and -2alpha/sqrt3 (simple) **",
 "",
 "   · the DOUBLED root +alpha/sqrt3 is exactly the one that also solves 3r^2 = alpha^2,",
 "     so the numerator vanishes there and the contact is TANGENTIAL;",
 "   · the simple root -2alpha/sqrt3 does not, so the contact is TRANSVERSAL.",
 "",
 "⇒ ** THE PAPER'S 'ORDER OF CONTACT' DISTINCTION BETWEEN THE TWO SEAMS IS THE MULTIPLICITY OF",
 "   THE ROOT -- the same doubling that makes the member Nariai. **  Stated as an identity it",
 "   needs no numbers at all: 3r^2 = alpha^2 is r = alpha/sqrt3 is the Nariai radius is the",
 "   double root.",
]:
    print("  " + line)
assert roots[al / sp.sqrt(3)] == 2 or any(sp.simplify(k - al/sp.sqrt(3)) == 0 and v == 2
                                          for k, v in roots.items())

# ============================================================================
print()
print("=" * 78)
print("PART 4 — NUMERICAL CONTROL, STRAIGHT OFF THE CONGRUENCE")
print("=" * 78)
a_ = 1.0
Mn = a_ / (3 * np.sqrt(3))
An = (2 * Mn) ** (1 / 3)
fn = lambda x: 1 - 2 * Mn / x - x * x / a_**2


def acc_numeric(x, eps):
    """r'' from finite differences of the first integral, independent of PART 1's algebra"""
    h = 1e-6
    g = lambda y: np.sqrt(abs(1 - fn(y))) if eps > 0 else np.sqrt(abs(fn(y) - 1))
    # r'' = d/dr (1/2 (r')^2) = eps * -f'/2 ; do it as a derivative of the first integral
    q = lambda y: 0.5 * (1 - fn(y)) if eps > 0 else 0.5 * (fn(y) - 1)
    return (q(x + h) - q(x - h)) / (2 * h)


print(f"  {'locus':<32} {'r':>12} {'formula':>12} {'from d/dr of the first integral':>34}")
for name, rv, cv, eps in [("front seam", 1 / np.sqrt(3), 1, +1),
                          ("back seam", -2 / np.sqrt(3), 1, +1),
                          ("turnaround", -An, 0, +1),
                          ("Euclidean null", rEN_n, -1, -1)]:
    fml = eps * (3 * rv**2 - cv) / (2 * rv)
    num = acc_numeric(rv, eps)
    print(f"  {name:<32} {rv:>12.6f} {fml:>12.6f} {num:>34.6f}")
    assert abs(fml - num) < 1e-5

print()
print("=" * 78)
print("NOT CLAIMED")
print("=" * 78)
for line in [
 "· No new physics.  The cubic family is the caption's own; this is its consequence.",
 "· No number changes: -1.299 is -3 sqrt3/4 to the digits quoted, +1.969 is the c=-1 root's",
 "  value to the digits quoted, and the turnaround's closed form is already in the caption.",
 "· Nothing about what the lift GOVERNS, which P7 marks as worked in sec:lift-initial-rate and",
 "  which this receipt does not touch.",
 "· s/P = 0.78899 is a path-length fraction and is NOT addressed here -- it needs the arclength",
 "  integral, not the cubic.",
 "· No closure on any registered item.",
]:
    print("  " + line)
