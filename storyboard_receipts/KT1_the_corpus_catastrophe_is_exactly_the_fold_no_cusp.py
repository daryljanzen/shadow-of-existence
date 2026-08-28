#!/usr/bin/env python3
"""RECEIPT — catastrophe bake `KT1`: ** THE CORPUS'S CATASTROPHE CONTENT IS EXACTLY THE FOLD (A_2), AND
NO CUSP (A_3) OR HIGHER IS POSSIBLE.  THE NARIAI DOUBLE ROOT IS A FOLD (h=h'=0, h''!=0); THE DEPRESSED
HORIZON CUBIC WITH ITS FIXED NON-ZERO LINEAR COEFFICIENT ADMITS NO TRIPLE ROOT FOR ANY MASS; AND THE
CYCLOID TURNAROUND IS A NON-DEGENERATE MORSE EXTREMUM (r''=-/+ M != 0), NOT A CUSP. **

LEVEL: NO RATE -- a catastrophe classification and an impossibility.

WHY THIS PROBE.  The catastrophe/singularity bake (one of the three fields never thrown before r3505)
  read all seventeen papers.  Every genuine catastrophe occurrence is a FOLD: the Nariai double root of
  the horizon cubic, where two horizons collide, kappa vanishes, and the discriminant Delta=4-27(2M)^2
  is the bifurcation set (`D4_fold_scaling`, `Q5_nariai_on_the_locus`, `sweep2_discriminant_is_interval`).
  P02 states the sharp negative -- the cycloid turnaround is an ORDINARY non-degenerate Morse maximum,
  NOT a cusp -- and proves it by Morse's lemma.  The bake's own verdict, owed and supplied here, is the
  UNION of these: the corpus's catastrophe is exactly A_2, and A_3 is not merely absent but IMPOSSIBLE
  on the corpus's own cubic.  That impossibility is the checkable content this receipt adds.

THE THREE FACTS, EACH CHECKABLE.
  (1) FOLD at Nariai.  h(r)=r^3-r+2M (gauge alpha=1).  At 2M_c=2/(3 sqrt3) the double root r_c=1/sqrt3
      has h=h'=0 and h''=2 sqrt3 != 0.  h'=0, h''!=0 is exactly the A_2 (fold) normal form; a cusp (A_3)
      would need h''=0 too.
  (2) A_3 IMPOSSIBLE on the corpus's cubic.  A cusp needs a TRIPLE root: h=(r-a)^3.  Matching to the
      depressed cubic r^3 - r + 2M forces the r^2 coefficient -3a=0 => a=0, and then the linear
      coefficient 3a^2 = -1 => 0 = -1, a contradiction.  The linear coefficient is FIXED at -1 (it is
      -alpha^2, never zero), so NO value of M gives a triple root.  The family tops out at the double
      root: A_2 and no higher.
  (3) MORSE, NOT CUSP, at the cycloid turnaround.  r(z)=M(1+cos z): r'=-M sin z vanishes at z in pi Z,
      where r''=-M cos z = -/+ M != 0 -- non-degenerate (Morse).  A cusp there would need r'=r''=0,
      i.e. sin z = cos z = 0 at once, which has no solution.

WHAT IS NOT CLAIMED.  Not that the fold itself is new (it is `D4_fold_scaling`, receipted under P07);
  KT1 claims the CLASSIFICATION IS COMPLETE -- the corpus's catastrophe content is the fold and only the
  fold, because the higher catastrophe is algebraically excluded on its own cubic and its own cycloid.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

print("=" * 78)
print("  KT1 — the corpus's catastrophe is exactly the fold (A_2); no cusp (A_3) is possible")
print("=" * 78)

r, M, z, a = sp.symbols('r M z a', real=True)

# (1) FOLD at Nariai: h=h'=0, h''!=0
h = r**3 - r + 2 * M
rc = 1 / sp.sqrt(3)
Mc = sp.Rational(1, 2) * 2 / (3 * sp.sqrt(3))
h0 = sp.simplify(h.subs({r: rc, M: Mc}))
hp0 = sp.simplify(sp.diff(h, r).subs(r, rc))
hpp0 = sp.simplify(sp.diff(h, r, 2).subs(r, rc))
assert h0 == 0 and hp0 == 0 and hpp0 != 0, "Nariai must be a fold: h=h'=0, h''!=0"
print(f"\n  (1) horizon cubic h=r^3-r+2M at Nariai (2M_c=2/3sqrt3, r_c=1/sqrt3):")
print(f"      h={h0}, h'={hp0}, h''={hpp0}  ->  h'=0 & h''!=0 is the FOLD (A_2) normal form.")

# (2) A_3 impossible: no triple root of the depressed cubic with fixed linear coeff -1
triple = sp.expand((r - a)**3)                    # r^3 - 3a r^2 + 3a^2 r - a^3
p_tri = sp.Poly(triple, r)
# match to r^3 + 0*r^2 - 1*r + 2M : r^2 coeff and r coeff must agree for a triple root
c2 = p_tri.coeff_monomial(r**2)                   # -3a  (must be 0)
c1 = p_tri.coeff_monomial(r)                       # 3a^2 (must be -1)
sol = sp.solve([c2 - 0, c1 - (-1)], a, dict=True)
assert sol == [], "there must be NO real a giving a triple root"
print(f"\n  (2) triple-root test: match (r-a)^3 to r^3 - r + 2M ->  need -3a=0 AND 3a^2=-1.")
print(f"      -3a=0 => a=0, then 3a^2=-1 => 0=-1.  real solutions for a: {sol}")
print("      => NO triple root for ANY M (the linear coeff -alpha^2 is fixed nonzero).  A_3 IMPOSSIBLE.")

# (3) Morse, not cusp, at the cycloid turnaround
rz = M * (1 + sp.cos(z))
rp = sp.diff(rz, z)
rpp = sp.diff(rz, z, 2)
crit = sp.solve(rp, z)                              # sin z = 0
rpp_0 = sp.simplify(rpp.subs(z, 0))
rpp_pi = sp.simplify(rpp.subs(z, sp.pi))
assert rpp_0 != 0 and rpp_pi != 0, "cycloid critical points must be Morse-nondegenerate"
both_zero = sp.solve([sp.sin(z), sp.cos(z)], z)
assert both_zero == [], "a cusp would need sin z = cos z = 0 simultaneously -- impossible"
print(f"\n  (3) cycloid r=M(1+cos z): r'=-M sin z vanishes at z in pi Z;")
print(f"      r''(0)={rpp_0}, r''(pi)={rpp_pi}  (both +/- M != 0) -> non-degenerate MORSE extrema.")
print(f"      a cusp needs r'=r''=0 i.e. sin z=cos z=0 at once: solutions {both_zero} -> NONE.")

print("\n  ** VERDICT: the corpus's catastrophe content is EXACTLY the fold (A_2).  Its central")
print("     object -- the Nariai double root -- is a fold (h'=0, h''!=0), and no cusp (A_3) can")
print("     occur: the depressed horizon cubic with fixed linear coefficient admits no triple root")
print("     for any mass, and the cycloid turnaround is a non-degenerate Morse extremum, not a cusp.")
print("     The classification is complete; the field stops at the fold, and does so provably. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
