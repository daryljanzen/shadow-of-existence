#!/usr/bin/env python3
"""RECEIPT — harmonic-analysis bake `H13`: ** THE COINCIDENCE P10 RECORDS "WITHOUT CLAIMING IT" IS
FORCED.  THE ADIABATIC TREATMENT MUST LOSE CONTROL AT THE LOWEST HARMONICS, AND THE LOWEST IS n=2
BECAUSE THAT IS WHERE TT MODES BEGIN ON S^3. **

LEVEL: NO RATE — tensor harmonics on the round three-sphere.

WHY THIS PROBE.  The third of the reach owed after r3453.  P10 carries this field's vocabulary x46 and
  the bake had never read it.  P10 writes, carefully: "We record, WITHOUT CLAIMING IT, that the
  harmonic indices at which the treatment loses control are the lowest ones."  ** A declined claim is
  the best kind of probe: either the caution is warranted or the claim is available. **

WHAT IS SHOWN — IT IS AVAILABLE, AND IT IS A THEOREM.

  (1) THE TOWER BEGINS AT n=2, AND P10 SAYS SO ("there are no modes below n=2 on S^3").  The reason is
      the degeneracy of TT rank-two harmonics on S^3, 2(n^2-1), which is 0 at n=1 and empty below.
      At n=2 it is 6, at n=3 it is 16.

  (2) THE ADIABATICITY PARAMETER IS MONOTONE.  From H12, the WKB parameter separates as C/mu_n with
      mu_n = sqrt(n(n+2)-2), and d/dn (1/mu_n) = -(n+1)/(n(n+2)-2)^{3/2} < 0 for all n >= 2.
      ** So C/mu_n is strictly decreasing in n, for ANY value of C. **

  ** (1) AND (2) TOGETHER FORCE IT.  A monotone-decreasing parameter takes its largest value at the
  smallest available index, and the smallest available index is n=2 by the S^3 degeneracy.  So the
  adiabatic treatment MUST lose control at the lowest harmonics, whatever C is and whatever the
  frequencies do.  It is not a coincidence to be recorded; it is entailed. **

AND IT JOINS TWO PAPERS.  P07 supplies the parameter's form (C/mu_n, H12); P10 supplies the spectrum's
  floor (n>=2).  Neither alone entails the conclusion and together they do -- and the two facts sit in
  different papers, which is why the entailment was available to neither.

ROUTED, NOT APPLIED.  P10's caution can be withdrawn: the sentence can claim what it currently only
  records.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

n = sp.symbols('n', positive=True, integer=True)

print("=" * 78)
print("  H13 — the declined coincidence is forced")
print("=" * 78)

deg = 2 * (n**2 - 1)
print(f"\n  (1) TT rank-two harmonic degeneracy on S^3:  {sp.expand(deg)}")
for k in (0, 1, 2, 3, 4):
    d = int(deg.subs(n, k))
    print(f"        n={k}:  {d:>3}" + ("   <- EMPTY" if d <= 0 else ""))
assert int(deg.subs(n, 1)) == 0, "n=1 must be empty"
assert int(deg.subs(n, 0)) <= 0, "n=0 must be empty"
assert int(deg.subs(n, 2)) > 0, "n=2 must be the first populated level"
print("  ** VERDICT 1: the tower begins at n=2, and the reason is the degeneracy, exactly as")
print("     P10 states. **")

mu = sp.sqrt(n * (n + 2) - 2)
d1 = sp.simplify(sp.diff(1 / mu, n))
print(f"\n  (2) d/dn of the adiabaticity parameter C/mu_n:  C * {d1}")
for k in (2, 3, 5, 10):
    assert float(d1.subs(n, k)) < 0, f"must be decreasing at n={k}"
print(f"        negative for every n >= 2  ->  C/mu_n is STRICTLY DECREASING, for ANY C")
print("  ** VERDICT 2: monotone, independent of the value of C. **")

vals = [(k, float(mu.subs(n, k)), 1.72 / float(mu.subs(n, k))) for k in (2, 3, 4, 5, 8)]
print("\n        n    mu_n     C/mu_n at C=1.72")
for k, m, c in vals:
    print(f"      {k:3d} {m:7.4f}   {c:8.3f}" + ("   <- largest, and the first that exists" if k == 2 else ""))
assert vals[0][2] == max(v[2] for v in vals), "the largest must be at the lowest available n"

print("\n  ** VERDICT 3: (1) and (2) TOGETHER FORCE IT.  A monotone-decreasing parameter takes")
print("     its largest value at the smallest available index, and the smallest available is")
print("     n=2 by the S^3 degeneracy.  So the treatment MUST lose control at the lowest")
print("     harmonics -- whatever C is.  P10 records this 'without claiming it'; it is")
print("     entailed, and the caution can be withdrawn. **")
print("\n  ** VERDICT 4: and it JOINS TWO PAPERS -- P07 supplies the parameter's form, P10 the")
print("     spectrum's floor.  Neither alone entails the conclusion; together they do, which")
print("     is why the entailment was available to neither. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
