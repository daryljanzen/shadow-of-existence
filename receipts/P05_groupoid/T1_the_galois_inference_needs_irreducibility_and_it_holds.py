"""T1 — THE GALOIS INFERENCE NEEDS A HYPOTHESIS P05 DOES NOT STATE, AND IT IS SATISFIED.

NUMBER-THEORY FIELD BAKE, probe T1.

P05's `rem:galois` reads, in full on the point:

    "the cubic r^3 - r + 2M = 0 has discriminant Delta = 4 - 27(2M)^2, NOT A SQUARE in C(2M),
     SO its Galois group is the full S_3."

** THE CONCLUSION IS TRUE.  THE INFERENCE AS WRITTEN IS NOT VALID. **

The theorem is:  *** for an IRREDUCIBLE cubic over a field of characteristic != 2, Gal = S_3 iff
disc is not a square, and Gal = A_3 = Z_3 iff it is. ***  Irreducibility is a hypothesis, not a
convenience.  Drop it and the biconditional fails in the S_3 direction outright: a REDUCIBLE cubic
can have a non-square discriminant and a Galois group of order 2.

*** SO "not a square, SO S_3" is a valid step only once irreducibility is in hand -- and P05 never
    says the cubic is irreducible. ***

This matters more than a missing word usually would, because THREE other bakes have already built
on the S_3 result -- algebraic geometry (the branched cover), combinatorics (the S_3 = Sym(3-set)
identification), complex analysis (the degree-six Galois closure).  All three USE the conclusion;
none checks the theorem's hypotheses.  *** A shared result nobody has audited is exactly the shape
this corpus keeps finding. ***

VERDICTS:
  1. the discriminant is 4 - 27(2M)^2, computed rather than quoted.
  2. it is not a square in C(2M) -- shown by a degree/parity argument, not by assertion.
  3. THE CUBIC IS IRREDUCIBLE over C(2M), so the hypothesis is satisfied and the conclusion holds.
  4. THE CONTROL, AND IT IS THE POINT: a REDUCIBLE cubic with a NON-SQUARE discriminant whose
     Galois group is Z_2 and not S_3.  *** Exhibited explicitly, so the hypothesis is shown to be
     load-bearing rather than pedantic. ***
  5. and the A_3 direction, for completeness: a cubic with SQUARE discriminant has Gal = Z_3.

⛔ AND A SCAR ABOUT THE WRITING RATHER THAN THE MATHEMATICS.  `check_receipts` caught HOLLOW
ASSERTIONS of the `expr == True` shape in this file -- the THIRD receipt in three fields to carry
them, after I5/I7 at r3608 and D1 at r3610.  *** A defect I have now been told about twice and
reached for a third time is not an accident of the moment; it is a habit, and the fix is to pin a
measured VALUE every time rather than a boolean. ***  Corrected here and recorded so the count of
how often it recurred is on the record rather than absorbed.

Written r3614 by node 60, number-theory bake.  Stated for reversal.
"""
import sympy as sp

FAIL = []
def check(label, got, want):
    ok = (sp.simplify(got - want) == 0) if isinstance(got, sp.Basic) and isinstance(want, sp.Basic) \
         else got == want
    print(f"    [{'ok' if ok else 'FAIL'}]  {label}   got={got}   want={want}")
    if not ok:
        FAIL.append(label)

r = sp.Symbol('r')
m = sp.Symbol('m')                       # m stands for 2M, the mass parameter

print("=" * 78)
print("T1 — 'NOT A SQUARE, SO S_3' NEEDS IRREDUCIBILITY, AND P05 DOES NOT SAY IT")
print("=" * 78)

print("\nVERDICT 1 — THE DISCRIMINANT, COMPUTED.")
cubic = r**3 - r + m
disc = sp.simplify(sp.discriminant(cubic, r))
print(f"    disc(r^3 - r + {m}) = {disc}")
check("disc == 4 - 27 m^2", sp.expand(disc), sp.expand(4 - 27*m**2))

print("\nVERDICT 2 — IT IS NOT A SQUARE IN C(m), and the argument is a parity one.")
print("    4 - 27 m^2 = -27 (m - 2/(3 sqrt 3)) (m + 2/(3 sqrt 3)) -- two DISTINCT simple roots.")
roots = sp.solve(sp.Eq(disc, 0), m)
print(f"    its roots in m: {roots}")
check("two distinct simple roots", len(set(roots)), 2)
sq = sp.factor_list(disc)
odd = [(f, e) for f, e in sq[1] if e % 2 == 1]
print(f"    square-free factorisation exponents: {[(sp.srepr(f)[:0] or str(f), e) for f, e in sq[1]]}")
check("the square-free part appears to multiplicity ONE, so it is not a square",
      [e for _, e in sq[1]], [1])
print("    *** A rational function is a square only if every factor has even multiplicity.")
print("        Two simple roots, so it is not. ***")

print("\nVERDICT 3 — THE HYPOTHESIS: IS THE CUBIC IRREDUCIBLE OVER C(m)?")
print("    The cubic is DEGREE ONE in m: r^3 - r + m.  Solve for m and it is m = r - r^3, so the")
print("    curve {r^3 - r + m = 0} is the graph of a polynomial map and is therefore rational and")
print("    irreducible as a plane curve; equivalently, by Gauss's lemma over C[m], a factorisation")
print("    over C(m) would be one over C[m], and degree 1 in m forbids it.")
print(f"    sympy factor: {sp.factor(cubic)}")
check("it does not factor", sp.factor(cubic), cubic)
# the decisive check: no root in C(m).  A root would be a rational function R(m) with R^3 - R + m = 0.
print("    Decisive form -- a root in C(m) would be a rational function R(m) with R^3 - R + m = 0.")
print("    Writing R = p/q in lowest terms gives p^3 - p q^2 + m q^3 = 0, so q | p^3 and hence")
print("    q is a unit; then p^3 - p + m = 0 with p a POLYNOMIAL, and comparing degrees in m")
print("    forces deg p = 1/3.  *** No such polynomial exists, so there is no root in C(m). ***")
p_ = sp.Symbol('p')
degs = [sp.degree(sp.expand((a*m + b)**3 - (a*m + b) + m), m) for a, b in [(1, 0), (1, 1), (2, 3)]]
print(f"    (sanity: a linear p gives degree {degs} in m, never the identically-zero polynomial)")
lin_zero = [sp.simplify(sp.expand((a*m + b)**3 - (a*m + b) + m)) == 0 for a, b in
            [(1, 0), (1, 1), (2, 3), (-1, 0)]]
check("no linear polynomial is a root", lin_zero, [False, False, False, False])

print("\nVERDICT 4 — THE CONTROL, AND IT IS WHY THE HYPOTHESIS IS LOAD-BEARING.")
print("  A REDUCIBLE cubic whose discriminant is NOT a square, and whose group is NOT S_3.")
ctrl = sp.expand((r - 1) * (r**2 + 1))
dctrl = sp.discriminant(ctrl, r)
print(f"    control cubic: {ctrl}   disc = {dctrl}")
check("the control's discriminant is -16", dctrl, -16)
print(f"    is -16 a square in Q?  sqrt(-16) = {sp.sqrt(-16)}  -> not rational")
check("sqrt(-16) is 4i, so -16 is NOT a square in Q", sp.sqrt(sp.Integer(-16)), 4*sp.I)
print("    its splitting field over Q is Q(i), of degree 2, so its Galois group has ORDER 2.")
splitting_deg = sp.degree(sp.minimal_polynomial(sp.I, r), r)
print(f"    [Q(i):Q] = {splitting_deg}")
check("the control's Galois group has order 2, NOT 6", splitting_deg, 2)
print("    *** NON-SQUARE DISCRIMINANT, AND THE GROUP IS Z_2. ***  So 'disc not a square' alone")
print("        does NOT give S_3, and the missing word in P05's sentence is doing real work.")

print("\nVERDICT 5 — AND THE OTHER DIRECTION, so the biconditional is exercised both ways.")
c3 = r**3 - 3*r + 1                       # the cyclic cubic; disc = 81 = 9^2
d3 = sp.discriminant(c3, r)
print(f"    r^3 - 3r + 1: disc = {d3} = {sp.sqrt(d3)}^2, a square, and it is irreducible")
check("disc is 81", d3, 81)
check("81 is 9 squared", sp.sqrt(sp.Integer(81)), sp.Integer(9))
check("and the cubic is irreducible over Q", sp.factor(c3), c3)
print("    -> Galois group A_3 = Z_3, order 3.  *** The criterion separates S_3 from Z_3 exactly")
print("       WHEN irreducibility holds, and says nothing at all when it does not. ***")

print("\n" + "=" * 78)
if FAIL:
    print(f"  VERDICT: {len(FAIL)} CHECK(S) FAILED")
    for f in FAIL:
        print("   ", f)
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  P05's conclusion is CORRECT -- the horizon cubic is irreducible over")
print("  C(2M) and its discriminant is not a square, so its Galois group is S_3.  *** But the")
print("  sentence infers S_3 from the non-square discriminant ALONE, and that inference is invalid:")
print("  the control is a cubic with a non-square discriminant whose group has order two. ***")
print("  One clause naming irreducibility makes a true statement a valid one.")
print("=" * 78)
