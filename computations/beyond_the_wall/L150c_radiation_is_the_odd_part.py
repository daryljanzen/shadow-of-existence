#!/usr/bin/env python3
"""
`L-150`.  ** THE PROGENITOR INTERIOR, WRITTEN DOWN — AND THE FIRST THING IT DOES IS SUPPLY THE ODD
PART `L-170` SAID WOULD BE NEEDED.  RADIATION IS THAT ODD PART, EXACTLY. **

c54.125 reclassified this row: a modelling problem, not a derivation — write down a progenitor
interior with composition.  c54.124 closed `L-170` with a bound stated in the same breath: *the leg
is exactly even because it is the marginally-bound geodesic of an exactly VACUUM exterior; a
progenitor with real matter content would not be, and that is where a mixing term would have to come
from.*  ** This writes the interior down at leading order and finds the two halves are one object. **

  PART 1  ** THE INTERIOR: closed FRW with dust and radiation, solved exactly in conformal time. **
  PART 2  ** ITS PARITY: the dust term is EVEN, the radiation term is ODD, exactly. **
  PART 3  ** AND RADIATION WINS AT THE BRANCH POINT, so the odd part is not a correction there —
          it is the leading behaviour. **
  PART 4  ** SO THE PARAMETER THAT DECIDES THE MODE MIXING IS $\\rho_r/\\rho_m$ — WHICH IS THE
          INHERITED DATUM THIS ROW OWES.  The two halves of `L-150` are one. **

Run: python3 L150c_radiation_is_the_odd_part.py      (sympy, numpy)
"""
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
eta, A, B = sp.symbols('eta A B', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE INTERIOR, SOLVED EXACTLY")
print("=" * 78)
print("  The Oppenheimer-Snyder interior the corpus's E=1 geodesic bounds is a closed FRW ball.")
print("  With dust AND radiation -- which the corpus REQUIRES, since it runs BBN on this leg --")
print("  the Friedmann equation in conformal time is")
print("     (da/deta)^2 = A a + B - a^2 ,   A ~ rho_m,0 a0^3 ,   B ~ rho_r,0 a0^4 .")
a = (A / 2) * (1 - sp.cos(eta)) + sp.sqrt(B) * sp.sin(eta)
lhs = sp.simplify(sp.diff(a, eta)**2)
rhs = sp.simplify(A * a + B - a**2)
print(f"\n  claim:  a(eta) = (A/2)(1 - cos eta) + sqrt(B) sin eta")
print(f"     residual (da/deta)^2 - (A a + B - a^2) = {sp.simplify(lhs - rhs)}")
assert sp.simplify(lhs - rhs) == 0
print("  ** exact, and it is the standard closed dust+radiation solution. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — ITS PARITY")
print("=" * 78)
even = sp.simplify((a + a.subs(eta, -eta)) / 2)
odd = sp.simplify((a - a.subs(eta, -eta)) / 2)
print(f"  even part of a(eta) : {even}")
print(f"  odd  part of a(eta) : {odd}")
assert sp.simplify(even - (A / 2) * (1 - sp.cos(eta))) == 0
assert sp.simplify(odd - sp.sqrt(B) * sp.sin(eta)) == 0
print()
print(f"  {'component':>26} {'term in a(eta)':>26} {'parity':>10}")
for x, y, z in [("dust", "(A/2)(1 - cos eta)", "EVEN"), ("radiation", "sqrt(B) sin eta", "** ODD **")]:
    print(f"  {x:>26} {y:>26} {z:>10}")
print()
for s in [
 "⇒⇒ ** THE SPLIT IS EXACT AND IT IS BY SPECIES.  The dust content is the even part of the",
 "   background; the radiation content IS the odd part. **  *Not 'contributes an odd term' — it is",
 "   the odd part, with no even piece at all.*",
 "",
 "⌗⌗ ** AND `L-170` NAMED EXACTLY THIS OBJECT WITHOUT KNOWING WHAT IT WAS.  It closed on: *mixing",
 "   requires a background correction ODD in the time, the vacuum leg has none on any determination,",
 "   and a progenitor with real matter content would not be even.* **  *The matter content that",
 "   breaks the evenness is not 'pressure, dissipation, anything with an arrow' in the vague sense",
 "   that row allowed itself — **it is radiation, and its coefficient is $\\sqrt{B}$.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND RADIATION WINS AT THE BRANCH POINT")
print("=" * 78)
ser = sp.series(a, eta, 0, 4).removeO()
print(f"  a(eta) near the branch point:  {sp.expand(ser)}")
print(f"     leading term: sqrt(B) eta   -- RADIATION, linear")
print(f"     next term:    (A/4) eta^2   -- dust, quadratic")
assert sp.simplify(sp.expand(ser).coeff(eta, 1) - sp.sqrt(B)) == 0
assert sp.simplify(sp.expand(ser).coeff(eta, 2) - A / 4) == 0
print()
print("  and the density ratio confirms it, with no expansion needed:")
rho_ratio = sp.symbols('a_scale', positive=True)
print("     rho_r / rho_m  ~  (a^-4) / (a^-3)  =  1/a  ->  INFINITY as a -> 0")
print()
for s in [
 "⇒⇒ ** SO THE ODD PART IS NOT A CORRECTION AT THE BRANCH POINT — IT IS THE LEADING BEHAVIOUR. **",
 "   *An interior with ANY radiation at all is radiation-dominated in its last moments, because",
 "   $\\rho_r/\\rho_m\\propto1/a$ diverges.  **The vacuum leg's $a\\propto\\tau^{2/3}$, on which",
 "   c54.122's scale invariance and c54.124's evenness both rest, is the DUST law — and dust is",
 "   exactly what does NOT dominate there.***",
 "",
 "⚠ ** THIS DOES NOT OVERTURN c54.122 OR c54.124; IT LOCATES THEM. **  *Both are statements about",
 "   the marginally-bound VACUUM geodesic, which is what the corpus's $r^3=2M\\alpha^2\\sinh^2$ is.",
 "   They hold of that object exactly.  **What this shows is that the object is not the progenitor",
 "   interior once the interior has the radiation the corpus's own BBN requires.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE TWO HALVES OF THIS ROW ARE ONE OBJECT")
print("=" * 78)
print("  The odd part's size relative to the even part, at conformal time eta:")
ratio = sp.simplify(odd / even)
print(f"     odd / even = {ratio}")
print(f"  near the branch point this diverges as 2 sqrt(B) / (A eta) -- the radiation term dominates")
lim = sp.limit(sp.simplify(ratio * eta), eta, 0)
print(f"     lim_(eta->0) eta * (odd/even) = {sp.simplify(lim)}")
print()
print("  and sqrt(B)/A is fixed by the composition:  B/A^2 ~ rho_r/rho_m at the reference epoch.")
print()
print(f"  {'quantity':>34} {'what sets it':>34}")
for x, y in [("the odd part's coefficient sqrt(B)", "the radiation content"),
             ("the even part's coefficient A", "the dust content"),
             ("their ratio", "** rho_r / rho_m -- THE INHERITED DATUM **")]:
    print(f"  {x:>34} {y:>34}")
print()
for s in [
 "⇒⇒⇒ ** SO THE PARAMETER THAT DECIDES WHETHER THE CONTINUATION MIXES THE MODES IS THE VERY DATUM",
 "   THIS ROW OWES.  `L-150` asked for $\\rho_r/\\rho_m$ and `L-170` asked for an odd part, and they",
 "   are the same question asked from two ends. **",
 "",
 "✔ ** WHICH IS THE RESULT: the row is not two problems (derive the composition; explain the",
 "   spectrum) but one, and the link is exact rather than thematic. **  *A progenitor with more",
 "   radiation has a larger odd part, hence more mode mixing, hence more of the contracting leg's",
 "   scale-invariant spectrum reaching the observer.*",
 "",
 "⚑ ** AND THAT IS A CONSTRAINT RUNNING THE OTHER WAY, WHICH IS WHAT THE ROW HAS LACKED: the",
 "   OBSERVED spectrum constrains the mixing, the mixing constrains the odd part, and the odd part",
 "   IS the radiation content. **  *So the composition is not only an input to be derived from the",
 "   collapse — it is an output constrained by the sky.  **The row acquires a second boundary",
 "   condition, and it comes from the direction the corpus was not looking.***",
 "",
 "⚠ ** BOUND, AND IT IS LARGE: this is the interior at LEADING ORDER — closed FRW, dust plus",
 "   radiation, no anisotropy, no dissipation, and matched to the exterior only in the sense that",
 "   the OS construction does. **  *What is established is the PARITY STRUCTURE and its species",
 "   assignment, which is robust because it follows from the exact solution's form.  The SIZE of",
 "   the resulting mixing is not computed here and is the next step.*",
]:
    print("  " + s)
