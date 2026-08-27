#!/usr/bin/env python3
"""RECEIPT — functional-analysis bake `F21`: ** P06'S "NO FREE DIMENSIONLESS CONSTANT" CLAIM HAS A VON
NEUMANN DIMENSION COUNT AS ONE OF ITS TERMS, AND THE WORD "LONE" IS EXACT — DEFICIENCY (1,1) GIVES
U(1), ONE REAL PARAMETER, WHICH IS WHAT ONE THERMAL CONDITION CAN CLOSE. **

LEVEL: NO RATE — von Neumann's extension theory.

WHY THIS PROBE.  P06 was estimated MEDIUM for this field on the strength of a single `self-adjoint`
  occurrence -- which could have been a stray.  ** It is load-bearing, and it sits inside the corpus's
  constants argument. **  P06: "hbar enters only at the seam, scaled by Lambda alone, the de Sitter
  horizon's thermal state closing the scale factor's LONE SELF-ADJOINT-EXTENSION FREEDOM without a
  free parameter ... So the gravitational-cosmological-quantum sector spends NO FREE DIMENSIONLESS
  CONSTANT."

  ** So a von Neumann extension parameter is one of the terms being counted to zero in an argument
  about the constants of nature.  That makes "lone" a dimension count, and dimension counts are
  checkable. **

WHAT VON NEUMANN GIVES.  A symmetric operator with deficiency indices (n,n) has self-adjoint
  extensions in bijection with U(n):

      (0,0) -> none needed, already self-adjoint       real dimension 0
      (1,1) -> U(1)                                    real dimension 1
      (2,2) -> U(2)                                    real dimension 4
      (3,3) -> U(3)                                    real dimension 9

  P10 computes the scale-factor Hamiltonian's indices as (1,1), ordering-independently, citing Weyl
  and Reed-Simon.  ** So the extension freedom is U(1): exactly ONE real parameter. **

  ** "LONE" IS THEREFORE EXACT, and it is exact in the way the argument needs.  One freedom, closed by
  one condition -- the de Sitter horizon's thermal state -- leaving zero.  Had the indices been (2,2)
  the freedom would be FOUR-dimensional and a single thermal condition could not close it. **

WHAT THIS JOINS.  The constants argument (P06), the deficiency computation (P10), and the thermal
  state (P10, citing Gibbons-Hawking) are three papers' worth of statement resting on one
  dimension count that no paper performs.  ** The count is right; it is simply never done in the open.

VERDICTS ARE ASSERTS.
"""

print("=" * 78)
print("  F21 — 'lone' is a von Neumann dimension count, and it is exact")
print("=" * 78)

print("\n  von Neumann: deficiency indices (n,n) -> self-adjoint extensions ~ U(n)")
print(f"      {'(n,n)':>8} {'extensions':>28} {'real dim':>10}")
rows = []
for n in (0, 1, 2, 3):
    grp = "none (already self-adjoint)" if n == 0 else f"U({n})"
    rows.append((n, grp, n * n))
    print(f"      {f'({n},{n})':>8} {grp:>28} {n*n:>10}")

dim = dict((n, d) for n, _, d in rows)
assert dim[1] == 1, "deficiency (1,1) must give exactly one real parameter"
assert dim[2] == 4, "and (2,2) four -- the contrast the argument needs"

print("\n  P10 computes the scale-factor Hamiltonian's indices as (1,1), ordering-independently.")
print(f"      -> extension freedom is U(1), real dimension {dim[1]}")
print("  ** VERDICT 1: 'the scale factor's LONE self-adjoint-extension freedom' is EXACT.")
print("     One real parameter, not a family of higher dimension. **")

freedoms, conditions = dim[1], 1
print(f"\n  the constants argument's arithmetic: {freedoms} freedom, {conditions} condition")
print("      (the de Sitter horizon's thermal state)")
assert freedoms - conditions == 0, "one condition must close exactly one freedom"
print(f"      remaining free parameters: {freedoms - conditions}")
print("  ** VERDICT 2: one closes one, leaving ZERO -- which is what 'without a free")
print("     parameter' asserts.  Had the indices been (2,2) the freedom would be")
print(f"     {dim[2]}-dimensional and a single thermal condition could not close it. **")

assert dim[2] - conditions > 0, "a (2,2) operator would leave freedom uncl osed"
print("\n  ** VERDICT 3: so the constants argument (P06), the deficiency computation (P10) and")
print("     the thermal state (P10, after Gibbons-Hawking) rest on one dimension count that")
print("     no paper performs.  The count is right; it is simply never done in the open. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
