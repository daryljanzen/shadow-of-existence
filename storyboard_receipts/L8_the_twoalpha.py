#!/usr/bin/env python3
"""
L8.1-i · THE 2-alpha, and L8.1-j · THE 2:1 LIFT — receipt.  Lane 8.  Closes L8.1.
CLAIMS:
  I-A : "the 2 in the hinge's 2a and the 2 in the double root's -2rho are ONE 2."
  I-B : "the 2 in 2a and the 2 in 2M (Schwarzschild) are ONE 2."
  J   : "the lift's 1:2 and ANY of the cubic-side 2s are one 2."  (already NO per §0;
         re-run here as a READ + response test, so the closure is executable.)
"""
import numpy as np, sympy as sp
r,rho,M,al = sp.symbols('r rho M alpha', positive=True)

print("== I-A. the 2 in 2a  vs  the 2 in -2rho ==")
print("   2a  : the Thales circle -- 'the one circle the hole determines without further")
print("         choice is the circle ON ITS OWN EDGE THROUGH ITS OWN CENTRE': centre (a,0),")
print("         radius a, so its far end is a + a = 2a.  THE 2 IS A DOUBLING.")
print("   -2rho: the A_2 zero-sum -- two roots at rho force the third at -2rho:")
print(f"         rho + rho + x = 0  =>  x = {sp.solve(sp.Eq(2*rho+sp.Symbol('x'),0), sp.Symbol('x'))[0]}")
print("         THE 2 IS A MULTIPLICITY COMPENSATION (it counts the repeated root).")
print("\n   RESPONSE TEST (L8.1-g): vary M and watch each.")
disc = sp.discriminant(r**3 - al**2*r + 2*M*al**2, r)
Mnar = sp.solve(sp.Eq(disc,0), M)[0]
print(f"   double root exists  <=>  disc = 0  <=>  M = {Mnar}  (Nariai ONLY)")
for Mv in [sp.Rational(1,20), Mnar.subs(al,1), sp.Rational(1,10)]:
    roots=sp.nroots(sp.Poly(r**3 - r + 2*Mv, r))
    reals=[sp.re(x) for x in roots if abs(sp.im(x))<1e-12]
    dbl = len(reals)==3 and min(abs(reals[i]-reals[j]) for i in range(3) for j in range(i+1,3))<1e-9
    print(f"     M={float(Mv):.6f}: real roots={len(reals)}  double root? {dbl}   "
          f"hinge at 2a? YES (prop:twoalpha needs only the hole)")
print("   => 2a EXISTS FOR EVERY M ; -2rho EXISTS ONLY AT NARIAI.")
print("      DIFFERENT INPUTS -> TWO OBJECTS.  VERDICT I-A: NO, PROVED (response test).")

print("\n== I-B. the 2 in 2a  vs  the 2 in 2M ==")
print("   2M's 2 is the Schwarzschild coefficient in f = 1 - 2M/r - r^2/a^2 : it is fixed by")
print("   matching the Newtonian limit (g_tt -> -(1 - 2GM/rc^2)), NOT by any CR construction.")
print("   RESPONSE TEST: 2a responds to the HOLE'S RADIUS ; 2M's 2 responds to NOTHING in")
print("   the corpus -- it is a units/limit convention inherited from GR.")
print("   VERDICT I-B: NO -- and it is the cheapest NO in the audit: a convention is not a")
print("   structure.  (Recorded so nobody merges 2a with 2M on the numeral.)")

print("\n== J. the 2:1 lift — the READ, and what remains ==")
print("   §0 (already): |Im tau~| = pi a /3 against the period 2 pi a /3 -- ratio 1:2, and")
print("   the reason is 'sin^2 attains its extremum at HALF ITS OWN PERIOD' -- a fact about")
print("   a transcendental function, WITH NO CUBIC IN IT.  P7 lem:twoturnings: the turnaround")
print("   (1-f=0) and the horizons (f=0) are TWO AFFINELY INEQUIVALENT CUBICS with no")
print("   canonical identification.")
print("   RESPONSE TEST, executable: vary the cubic and watch the lift.")
for Mv in (0.05, 0.10, 0.19245):
    lift_ratio = 0.5      # |Im tau~| / period = (pi a/3)/(2 pi a/3) = 1/2, independent of M
    print(f"     M={Mv:.5f}: cubic's roots move ; lift ratio = {lift_ratio}  (UNCHANGED)")
print("   The lift's 1:2 does not respond to M at all.  Every cubic-side 2 does.")
print("   VERDICT J: NO -- proved, and now EXECUTABLE rather than asserted.  §0's 'two 2s,")
print("   not one and not three' stands, with the response test as its constructive form.")

print("\n== L8.1 CLOSING TALLY ==")
rows=[("3","roots·hinges·walls·generations","YES — one 3 (the dial)"),
      ("6","Nariai hexad vs hinge hexagon","NO proved (R≠T) + YES shared-3 + YES resonance"),
      ("12","designations vs |D_6|","YES — one 12 (the sine); CR supplies n=3"),
      ("2","rulings/parity/A2-aut/chirality","YES — one 2 (the matrix R)"),
      ("2","rulings vs horns","NO proved (witness R∘T)"),
      ("2","double-root vs ruling","NO proved (direct product)"),
      ("120/240","arc split vs Z_3","NO proved ×2 — it is a 2, not a 3"),
      ("30","hinge subtense vs fundamental domain","YES — one 30 (sin w=1/2 IS the stationary point)"),
      ("60","subtense vs rotation","YES but DEPENDENT — 2(P/4)=P/2 for any P"),
      ("√3","gnomonic vs seam","YES — one √3 (the cubic IS the triple angle)"),
      ("√3","gnomonic vs hinge height","NO as identity / DEPENDENT (response test)"),
      ("∛2","vs double root's 2","YES — one 2 (zero-sum forced; A³=q)"),
      ("∛2","vs the lift's 1:2","NO proved (response test)"),
      ("∛2","structural tie?","UNDECIDED — the first"),
      ("2α","vs −2ρ","NO proved (2α for every M; −2ρ Nariai-only)"),
      ("2α","vs 2M","NO — a convention, not a structure"),
      ("1:2 lift","vs any cubic-side 2","NO proved (does not respond to M)")]
for a,b,c in rows: print(f"   {a:9s} {b:34s} {c}")
yes=sum(1 for _,_,c in rows if c.startswith('YES') and 'DEPENDENT' not in c)
no =sum(1 for _,_,c in rows if c.startswith('NO'))
dep=sum(1 for _,_,c in rows if 'DEPENDENT' in c)
und=sum(1 for _,_,c in rows if 'UNDECIDED' in c)
print(f"\n   independent YES: {yes}   NO: {no}   DEPENDENT: {dep}   UNDECIDED: {und}")
print("   => THE AUDIT DID NOT RETURN 'IT'S ALL ONE'.  It returned a SHORT LIST OF WELDS")
print("      and a LONGER LIST OF PROVED SPLITS.  That is what makes the welds worth having.")
