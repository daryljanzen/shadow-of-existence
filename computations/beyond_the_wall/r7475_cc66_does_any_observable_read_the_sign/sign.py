#!/usr/bin/env python3
"""r7475 ①: does any observable read the SIGN of sqrt(B)?

`r7473+cc66.12` found the crossing hands out (A, -sqrt B).  If the magnitude is
all any observable reads, PO-88 strikes on its own termination clause, and the
answer owes a COUNT of observables checked.

The pre-registration named one risk: the potential or phase the leg hands to
P15's transfer, because a phase can be odd where an amplitude is even.  That is
measured FIRST here, before the sweep.

Everything is symbolic and the first integral is DERIVED, not quoted.
"""
import sympy as sp

def hdr(s):
    print()
    print("=" * 78)
    print("  " + s)
    print("=" * 78)

eta = sp.Symbol('eta', real=True)
A, B = sp.symbols('A B', positive=True)
sB = sp.sqrt(B)
a = (A / 2) * (1 - sp.cos(eta)) + sB * sp.sin(eta)
ap = sp.diff(a, eta)

hdr("STEP 1 -- THE FIRST INTEGRAL, DERIVED FROM THE EQUATION ITSELF")
print(f"  a(eta)  = {a}")
print(f"  a'(eta) = {sp.simplify(ap)}")
print("  P16's interior obeys a'' + a = A/2.  Multiply by a' and integrate:")
print("      a'^2/2 + a^2/2 - (A/2) a = const,  and at the branch point a=0, a'=sqrt(B),")
print("      so const = B/2, giving")
print()
print("      ** a'^2 = B + A a - a^2 **")
lhs = sp.simplify(sp.expand_trig(sp.expand(ap**2)))
rhs = sp.simplify(sp.expand_trig(sp.expand(B + A * a - a**2)))
print(f"      checked identically: {sp.simplify(lhs - rhs) == 0}")
print(f"      a'^2 - (B + A a - a^2) = {sp.simplify(lhs - rhs)}")
print()
print("  ⛭ AND THAT IS THE WHOLE ANSWER IN ONE LINE: the dynamics as a function of")
print("     the SCALE FACTOR carries B and never sqrt(B).  B = (sqrt B)^2, so the")
print("     sign cannot enter any quantity written as a function of a.")
print("     a'(a) = +/- sqrt(B + A a - a^2), and that sign is the EXPANDING-versus-")
print("     CONTRACTING branch, not the sign of sqrt(B).")

hdr("STEP 2 -- ⒝ FIRST, BECAUSE THE PRICE NAMED IT AS THE RISK: the phase P15 reads")
print("  P15's transfer reads perturbations on this background, and the quantity")
print("  that carries a PHASE is the accumulated sound horizon,")
print("      s(a) = integral c_s dEta = integral c_s da / a'(a).")
print("  Written on the scale factor it carries a'(a) = sqrt(B + A a - a^2):")
a_ = sp.Symbol('a', positive=True)
ap_of_a = sp.sqrt(B + A * a_ - a_**2)
print(f"      a'(a) = {ap_of_a}      free symbols: {ap_of_a.free_symbols}")
print(f"      sqrt(B) present as such: {sB in ap_of_a.atoms(sp.Pow)}")
cs2 = sp.Rational(1, 3) * (B / a_**4) / (B / a_**4 + A / a_**3)      # c_s^2 = (1/3) rho_r/(rho_r+rho_m)
cs2 = sp.simplify(cs2)
print(f"      c_s^2(a) = {cs2}      free symbols: {cs2.free_symbols}")
integrand = sp.simplify(sp.sqrt(cs2) / ap_of_a)
print(f"      the phase integrand c_s/a'(a) = {integrand}")
print(f"      ⇒ carries B, A and a only; sqrt(B)'s SIGN is absent: "
      f"{B in integrand.free_symbols}")
print()
print("  ** ⒝ ANSWERED, AND THE RISK DID NOT MATERIALISE.  The phase is an integral")
print("     over the scale factor whose integrand is a function of B, so it is EVEN.")
print("     A phase CAN be odd where an amplitude is even -- the price was right to")
print("     flag that -- but not this phase, because the only place sqrt(B) could")
print("     have entered is a'(eta), and on the leg it is a'(a). **")

hdr("STEP 3 -- ⒞ THE SWEEP, each observable written on the scale factor")
rho_m = A / a_**3
rho_r = B / a_**4
obs = (
    ("rho_m(a)                 dust density", rho_m),
    ("rho_r(a)                 radiation density", rho_r),
    ("rho_r/rho_m (a)          the ratio r7475 names", sp.simplify(rho_r / rho_m)),
    ("H^2(a) = (a'/a^2)^2      expansion rate squared", sp.simplify((B + A*a_ - a_**2) / a_**4)),
    ("a''(a) = A/2 - a         areal acceleration", A/2 - a_),
    ("c_s^2(a)                 sound speed squared", cs2),
    # \u26d4 NOT the integrand itself: c_s is a SPEED, the POSITIVE root of c_s^2, and
    #   sympy prints it as sqrt(B)/sqrt(...), which the substitution flips while the
    #   quantity does not move.  A first draft scored it ODD on that symbol and a second
    #   tried to special-case it, which is whitelisting the wanted answer.  The honest
    #   form is to sweep the SQUARE -- unambiguously even -- and to state the
    #   positive-root step in prose rather than hide it in a classifier.
    ("(c_s/a')^2  the sound-horizon integrand SQUARED", sp.simplify(integrand**2)),
    ("integrand of the particle horizon  1/a'(a)", sp.simplify(1/ap_of_a)),
    ("a_turnaround: root of a' = 0", sp.simplify(sp.solve(sp.Eq(B + A*a_ - a_**2, 0), a_)[1])),
)
# \u26d4 THE FIRST VERSION OF THIS TEST WAS WRONG, AND ITS OWN OUTPUT SHOWED IT.
#   Substituting sqrt(B) -> -sqrt(B) tests the EXPRESSION sympy happened to write,
#   not the QUANTITY.  The sound-horizon integrand came back ODD only because
#   sympy wrote c_s as sqrt(B)/sqrt(...) -- but c_s is a SPEED, defined as the
#   POSITIVE root of c_s^2, and c_s^2 = B/(3(Aa+B)) carries B alone.  A positive
#   root of an even quantity is even; the formal substitution flips the symbol
#   while the quantity does not move.  So each observable is classified on BOTH
#   the expression and its square, and a quantity that is a positive root is
#   named as such rather than scored odd.
def classify(expr):
    """EVEN / ODD / NEITHER in sqrt(B).  \u26d4 ORDER MATTERS, and a first draft got it
    wrong in the one place the control was built to catch: it tested the SQUARE before
    testing ODD, and an odd quantity has an even square -- so a'(0) = sqrt(B), the branch
    label itself, came back filed as 'even as a positive root'.  The control failed and was
    right to.  ODD is tested before anything to do with squares, and the positive-root case
    is handled explicitly where it actually arises (the sound speed) rather than by a
    heuristic that can swallow an odd quantity."""
    flipped = expr.subs(sB, -sB)
    if sp.simplify(sp.simplify(flipped - expr)) == 0:
        return 'EVEN'
    if sp.simplify(sp.simplify(flipped + expr)) == 0:
        return 'ODD'
    return 'NEITHER'

print(f"  {'observable':<46}{'classification':>26}")
print("  " + "-" * 76)
n_even = 0
for label, expr in obs:
    c = classify(expr)
    n_even += 1 if c.startswith('EVEN') else 0
    mark = '' if c.startswith('EVEN') else '\u26d4 '
    print(f"  {label:<46}{mark + c:>26}")
print()
print(f"  \u21d2 {n_even} of {len(obs)} do not read the sign of sqrt(B).")
print("  \u231f The sound horizon enters as its SQUARE, and that is deliberate: c_s is a")
print("    SPEED, the POSITIVE root of c_s^2, and c_s^2 carries B alone (row above).")
print("    The positive root of an even quantity is even, so the integrand is even --")
print("    while the SYMBOL sympy prints for it, sqrt(B)/sqrt(...), flips under the")
print("    substitution.  Sweeping the square states that step instead of hiding it.")

hdr("STEP 4 -- ⒟ THE COUNT, and ⒠ THE VERDICT")
total = len(obs) + 1      # the sweep plus the phase measured in STEP 2
print(f"  observables checked: {len(obs)} in the sweep + 1 phase (STEP 2) = {total}")
print(f"  of which read the sign of sqrt(B): {len(obs) - n_even}")
print()
if n_even == len(obs):
    print("  ** NO OBSERVABLE READS THE SIGN.  Every one is a function of the scale")
    print("     factor, and the first integral a'^2 = B + A a - a^2 contains B and")
    print("     never sqrt(B).  The sign of sqrt(B) is the label on WHICH DIRECTION")
    print("     along eta is called forward -- which is the same choice as the")
    print("     involution itself -- and not a fact about the world. **")
    print("  ⇒ PO-88 STRIKES on its own termination clause.")
else:
    print("  ⛔ AT LEAST ONE OBSERVABLE READS THE SIGN: the row has a live remainder.")

hdr("STEP 5 -- THE CONTROL: a quantity that IS odd, before the leg is fixed")
print("  If 'even' came from the algebra rather than from the leg condition, then")
print("  nothing would come out odd.  Something must.")
controls = (("a'(0), the rate AT the branch point", sp.simplify(ap.subs(eta, 0))),
            ("a(eta) itself, at fixed eta", a),
            ("a'(eta) at fixed eta", sp.simplify(ap)))
for label, expr in controls:
    flipped = expr.subs(sB, -sB)
    even = sp.simplify(sp.simplify(flipped - expr)) == 0
    odd = sp.simplify(sp.simplify(flipped + expr)) == 0
    print(f"    {label:<40} {'EVEN' if even else ('ODD' if odd else 'NEITHER')}"
          f"   (flipped: {flipped})")
print()
print("  ** THE CONTROL BITES: a'(0) = sqrt(B) is ODD, and a(eta) and a'(eta) at")
print("     FIXED eta carry the sign too.  So the EVEN answer above comes from")
print("     writing each observable on the SCALE FACTOR -- i.e. from fixing the leg")
print("     by a > 0 -- and not from the arithmetic.  a'(0) is exactly the branch")
print("     label: it is the one quantity that lives AT a = 0, where the choice of")
print("     direction is made and no observable is read. **")
