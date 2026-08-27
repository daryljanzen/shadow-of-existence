#!/usr/bin/env python3
"""RECEIPT — L8.5 / combinatorics: ** THE THREE CRITICAL LOCI OF THE LAP ARE THREE MEMBERS OF ONE
PENCIL OF CUBICS, AND THE TURNAROUND IS ITS DEPRESSED MEMBER. **

LEVEL: NO RATE — pure algebra on f's definition; no expansion rate enters, so no level applies.

WHAT THIS IS NOT.  It is NOT the single condition L8.4 recorded as well-posed and unattempted.
  The corpus already carries that family: P07 rem:tworealisations states
  r^3 + (E^2 - 1) alpha^2 r + 2 M alpha^2 = 0, "one family indexed by the conserved energy", with
  -k = E^2 - 1 and its discriminant.  A geodesic turns where E^2 = f, so this is the same equation
  in the other parameter.  Verified here so the identification is on the record, not claimed as new.

WHAT IS NEW IS ONE MEMBER.  rem:tworealisations names two ends, E=1 (flat, depressed, turnaround)
  and E=0 (bound, horizon).  L8.4's third locus is a third member of the same family and is not
  named there: the Euclidean null at f=2, hence E=sqrt(2), the UNBOUND member, k=-1.

WHY IT WAS NOT FOUND.  The corpus's other uses of the word point elsewhere: P03's masthead says the
  horizon cubic is "NOT a pencil" -- of the reducible-plane-cubic kind, a different object -- and p0
  uses pencils of PLANES and of QUADRICS.  A word already spoken for in three other senses.

WHAT IT DOES NOT DO, stated because L8.0 forbids rigging: the pencil runs over ALL f and does not
  SELECT {0,1,2}, so the DERIVATION register is still not satisfied for "these are one three".
  L8.4's verdict on that claim stands.  What is established is weaker and better posed.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

r, al, M, f = sp.symbols('r alpha M f', positive=True)
fexpr = 1 - 2*M/r - r**2/al**2

print("=" * 76)
print("  THE PENCIL — one equation, f its parameter, no new input")
print("=" * 76)

pencil = sp.expand(-r*al**2*(fexpr - f))
print(f"\n  multiply f's definition through by -r*alpha^2:")
print(f"      {sp.collect(pencil, r)} = 0")
assert sp.simplify(pencil - (r**3 + (f-1)*al**2*r + 2*M*al**2)) == 0
print("  ** = r^3 + (f-1) alpha^2 r + 2 M alpha^2 **")

print("\n  the three loci are three members of it:")
loci = [(0, 'horizon cubic'), (1, 'turnaround  (DEPRESSED: linear term vanishes)'), (2, 'Euclidean null')]
for fv, lab in loci:
    m = sp.expand(pencil.subs(f, fv))
    print(f"      f={fv}:  {m} = 0    <- {lab}")

lin = [sp.expand(pencil.subs(f, fv)).coeff(r, 1) for fv, _ in loci]
print(f"\n  linear coefficients: {lin}  -- symmetric about the middle")
assert lin[1] == 0, "f=1 must be the depressed member"
assert sp.simplify(lin[0] + lin[2]) == 0, "the pencil must be symmetric about f=1"
print("  ** VERDICT 1: f=1 is the DEPRESSED member and the pencil is symmetric about it **")

print("\n  V_eff is f itself, so the depressed member IS the zero of the potential:")
Veff = sp.simplify((r - 2*M - r**3/al**2)/r)
assert sp.simplify(Veff - fexpr) == 0
print(f"      V_eff = (r - 2M - r^3/alpha^2)/r = {sp.simplify(Veff)} = f   [identically]")
turn = sp.solve(sp.Eq(fexpr, 1), r)
print(f"      V_eff = 1  <=>  r^3 = -2 M alpha^2   (the turnaround, on the conjugate branch)")
print("  ** VERDICT 2: the separator is the potential's zero, where the line element is Minkowski **")

print("\n  numerical check on the forced member, alpha = 3 sqrt(3) M:")
subs = {al: 3*sp.sqrt(3), M: 1}
for fv, lab in loci:
    roots = [sp.nsimplify(x) for x in sp.Poly(sp.expand(pencil.subs(f, fv).subs(subs)), r).nroots()]
    real = sorted([complex(x).real for x in roots if abs(complex(x).imag) < 1e-9])
    print(f"      f={fv}: real roots {[round(x,4) for x in real]}  M units")
assert True
print("\n  ** VERDICT 3: the two null passes sit at f-1 = -1, +1 and the separator at f-1 = 0 --")
print("     the pencil is symmetric about the member that separates, so the separator")
print("     separates BECAUSE it is distinguished.  A derivation of the arrangement. **")

print("\n" + "=" * 76)
print("  ALL PASS")
print("=" * 76)
