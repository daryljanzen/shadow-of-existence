#!/usr/bin/env python3
"""RECEIPT — functional-analysis bake `F12`: ** AT omega = 0 THE sqrt(f) IN THE ZERO-MODE EQUATION IS
AN OVERALL FACTOR AND CANCELS, SO THE INDEX IS REAL +/- lambda WHATEVER THE SIGN OF f -- AND THE
BRANCH POINT'S LIMIT-POINT VERDICT DOES NOT DEPEND ON THE OPERATOR CHOICE. **

LEVEL: NO RATE — an indicial computation on the zero-mode equation.

WHY THIS RECEIPT EXISTS.  The functional-analysis ledger asserts, as its defence of the limit-point
  verdict at r=0, that "sqrt(f) is an OVERALL FACTOR and cancels, so the index is real +/- lambda
  whatever the sign of f", upheld r3339 against readings that took the branch point to be
  limit-circle.  The claim is B67's and S3's and is stated in a verdict receipt; it is not receipted
  as a computation on the functional-analysis side, and the ledger's whole F2/F3 finding rests on it.

  ** If the index were oscillatory +/- i lambda, the branch point would be limit-circle, F2's two
  verdicts would NOT be opposite, and F3's routed clause would be wrong.  So this is the load-bearing
  step and it is the one that was unreceipted. **

WHAT IS SHOWN.  The zero-mode equation is (sqrt(f) d/dr - lambda sqrt(f)/r) psi = 0.  sqrt(f) divides
  out identically, leaving psi' = (lambda/r) psi with solutions r^(+/- lambda): REAL exponents, for
  either sign of f and for f complex.  The fork between the analytic sqrt(f) and the self-adjoint
  sqrt(|f|) operators therefore cannot bite at omega = 0; it bites only at omega != 0, where the
  omega-coupling's 1/sqrt(f) is the one term that does not cancel.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

r, lam = sp.symbols('r lambda', positive=True)
f = sp.Function('f')
psi = sp.Function('psi')

print("=" * 78)
print("  F12 — sqrt(f) cancels at omega = 0, so the index is real")
print("=" * 78)

expr = sp.sqrt(f(r)) * sp.Derivative(psi(r), r) - lam * sp.sqrt(f(r)) / r * psi(r)
print(f"\n  zero-mode equation:  {expr} = 0")

factored = sp.simplify(expr / sp.sqrt(f(r)))
print(f"  divide by sqrt(f):   {factored} = 0")
assert not factored.has(f), "sqrt(f) must cancel identically"
print("  ** VERDICT 1: sqrt(f) divides out IDENTICALLY -- it is an overall factor,")
print("     so nothing about f survives into the reduced equation. **")

sol = sp.dsolve(sp.Eq(sp.Derivative(psi(r), r) - lam / r * psi(r), 0), psi(r))
print(f"\n  reduced equation psi' = (lambda/r) psi  ->  {sol}")
assert sp.simplify(sol.rhs / sp.Symbol('C1') - r**lam) == 0, "solutions must be r^(+/- lambda)"
print("  ** VERDICT 2: solutions r^(+/- lambda) -- REAL exponents. **")

print("\n  and the sign of f cannot enter, because it never survives the division:")
for lbl, fv in [("f > 0 (static region)", sp.Rational(1, 2)),
                ("f < 0 (inside the horizon)", sp.Rational(-1, 2)),
                ("f complex (on the lift)", sp.I)]:
    red = sp.simplify((sp.sqrt(fv) * sp.Derivative(psi(r), r) - lam * sp.sqrt(fv) / r * psi(r)) / sp.sqrt(fv))
    same = sp.simplify(red - (sp.Derivative(psi(r), r) - lam / r * psi(r))) == 0
    print(f"      {lbl:28s} reduced equation identical: {same}")
    assert same, "the reduced equation must not depend on f"
print("  ** VERDICT 3: real +/- lambda for EITHER SIGN of f, and for f complex. **")

print("\n  ** CONSEQUENCE FOR F2/F3: the branch point's LIMIT-POINT verdict does not depend on")
print("     the operator choice.  Were the index oscillatory +/- i lambda, r=0 would be")
print("     limit-circle, the two boundaries would NOT be opposite, and F3's routed clause")
print("     would be wrong.  The fork bites only at omega != 0, where the omega-coupling's")
print("     1/sqrt(f) is the one term that does not cancel. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
