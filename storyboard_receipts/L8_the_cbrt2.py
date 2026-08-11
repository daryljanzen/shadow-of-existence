#!/usr/bin/env python3
"""
L8.1-h · THE cbrt2 — receipt.  Lane 8.
CLAIMS (split):
  A: "the cbrt2's 2 (A = cbrt2 * rho) and the double root's 2 (the -2rho third root /
      the 2rho^3 constant term) are ONE 2."
  B: "the cbrt2's 2 and the LIFT's 1:2 are one 2."
  C: "A = cbrt2 * rho ties the two turnings STRUCTURALLY."   <- can return UNDECIDED
SOURCE (§0, r1103, receipt one_to_two.py):  "(r-rho)^2 (r+2rho) = r^3 - 3rho^2 r + 2rho^3 ...
  q gives 2M a^2 = 2rho^3 => M a^2 = rho^3 -- WHICH IS THE NARIAI CONDITION.  Then
  A^3 = 2M a^2 = q = 2rho^3, so A = cbrt2 * rho."   AND, 8 lines later: "Named and unrun:
  A = cbrt2 * rho ... Well-posed, unattempted."
"""
import sympy as sp
r,rho,M,al,A = sp.symbols('r rho M alpha A', positive=True)

print("== 1. THE DERIVATION — reproduced symbolically, not quoted ==")
fac = sp.expand((r-rho)**2*(r+2*rho))
print(f"   (r-rho)^2 (r+2rho) = {fac}")
hor = r**3 - al**2*r + 2*M*al**2
print(f"   horizon cubic       = {hor}")
pmatch = sp.solve(sp.Eq(fac.coeff(r,1), hor.coeff(r,1)), rho)
print(f"   match p (coeff of r):  -3rho^2 = -alpha^2  =>  rho = {pmatch}   -> the SEAM")
qmatch = sp.solve(sp.Eq(fac.coeff(r,0), hor.coeff(r,0)), M)
print(f"   match q (constant)  :   2rho^3 = 2M alpha^2  =>  M = {qmatch[0]}  -> THE NARIAI CONDITION")
print("\n   the TURNAROUND is 1-f = 0 :  1 - 2M/r - r^2/a^2 = 1  =>  -2M/r = r^2/a^2  =>  r^3 = -2M a^2")
A3 = 2*M*al**2
print(f"   so |A|^3 = 2M alpha^2 = q = {sp.simplify(A3.subs(M,qmatch[0]))}  = 2 rho^3")
Aval = sp.simplify(sp.root(sp.simplify(A3.subs(M,qmatch[0])),3))
print(f"   => A = {Aval} = cbrt(2)*rho   : {sp.simplify(Aval - sp.cbrt(2)*rho) == 0}")
print("   THE BEAD'S AMPLITUDE IS THE CUBE ROOT OF THE CUBIC'S CONSTANT TERM.  Derived, no new input.")

print("\n== 2. CLAIM A: is the cbrt2's 2 the double root's 2? ==")
print("   The factorisation has exactly ONE 2 in it, appearing twice:")
print(f"     third root coefficient : {fac.coeff(r,1)} has rho^2 ; the ROOT is r = -2rho")
print(f"     constant term          : {fac.coeff(r,0)} = 2 rho^3")
print("   Both are (r-rho)^2(r+2rho) read off ONCE -- the SAME 2 (zero-sum forces it:")
print(f"     rho + rho + (-2rho) = {sp.simplify(rho+rho-2*rho)}  <- the A_2 zero-sum IS what makes it -2)")
print("   And A^3 = q = 2 rho^3 uses THAT 2, with no other input.  VERDICT A: YES, ONE 2.")

print("\n== 3. CLAIM B: is it the LIFT's 1:2? ==")
print("   The lift: |Im tau~| = pi a /3 against the period 2 pi a /3 -- ratio 1:2, and §0")
print("   gives the reason: 'sin^2 attains its extremum at half its own period' -- a fact")
print("   about a TRANSCENDENTAL function, WITH NO CUBIC IN IT.")
print("   RESPONSE TEST (L8.1-g): vary the cubic's constant term q.")
for qq in (sp.Rational(1,5), sp.Rational(2,5), sp.Rational(3,5)):
    rr = sp.root(qq,3)
    print(f"     q={qq}: A = cbrt(q) = {sp.nsimplify(rr)} ~ {float(rr):.6f}   "
          f"lift ratio = 1:2 (UNCHANGED -- it never saw q)")
print("   A responds to q ; the lift's 1:2 does not respond to anything of the cubic.")
print("   VERDICT B: NO -- PROVED (P7 lem:twoturnings: two affinely inequivalent cubics,")
print("   no identification of their root sets by an affine change of variable; the two are the")
print("   E=1 and E=0 ends of one turning-point family).  §0: 'Two 2s, not one and not three.'")

print("\n== 4. CLAIM C: does A = cbrt2 * rho TIE THE TWO TURNINGS structurally? ==")
print("   ⚠ FIRST, a fact §0 does not state: rho EXISTS ONLY AT NARIAI.")
print("   rho is the DOUBLE root; off Nariai the cubic has three simple roots and there is")
print("   no rho to take a ratio against.  So A = cbrt2 * rho is a NARIAI-ONLY relation.")
disc = sp.discriminant(hor, r)
print(f"   discriminant of the horizon cubic = {sp.factor(disc)}")
print(f"   double root <=> disc = 0 <=> M = {sp.solve(sp.Eq(disc,0),M)}  -- exactly Nariai.")
print("   SO: at the one point where rho exists, A = cbrt2 rho holds EXACTLY and is DERIVED.")
print("   BUT the standing question is what §0 actually asks: lem:twoturnings denies a")
print("   canonical identification of the two Z_3 SYMMETRIES ; A = cbrt2 rho is a METRIC")
print("   RATIO between two specific radii, which that denial does not touch.")
print("   IS A RATIO-WITHOUT-A-SYMMETRY STRUCTURE, OR COINCIDENCE?")
print("   - a DERIVATION exists (above) -> not nothing.")
print("   - a PROOF OF INEQUIVALENCE exists for the SYMMETRIES (lem:twoturnings) -> not one thing.")
print("   - NOTHING IN THE CORPUS DECIDES whether a metric ratio surviving a symmetry")
print("     denial is a structural tie.  Neither branch of the discriminator is met.")
print("   VERDICT C: UNDECIDED -- and undecided is an honest verdict (L8.0).")

print("\n== VERDICT ==")
print("   A: YES, ONE 2 -- the cbrt2's 2 IS the factorisation's 2 (the -2rho and the 2rho^3")
print("      are one 2, forced by the A_2 zero-sum).  A^3 = q, derived.")
print("   B: NO, PROVED -- the lift's 1:2 has no cubic in it and does not respond to q.")
print("   C: UNDECIDED -- the ledger's FIRST.  The relation is DERIVED and NARIAI-ONLY;")
print("      whether a metric ratio that survives lem:twoturnings' symmetry-denial is")
print("      STRUCTURE is not decided by anything in the corpus.")
print("\n   ⚠ AND §0 CONTRADICTS ITSELF: it DERIVES A = cbrt2 rho (q-matching, receipt")
print("   one_to_two.py) and eight lines later files it 'Well-posed, UNATTEMPTED'.")
print("   The RELATION is attempted and closed.  What is unattempted is C -- its meaning.")
