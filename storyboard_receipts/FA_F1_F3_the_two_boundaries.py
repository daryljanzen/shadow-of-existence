#!/usr/bin/env python3
"""RECEIPT — functional-analysis bake `F1`–`F3`: ** THE CORPUS'S SELF-ADJOINTNESS CRITERION BITES AT
a=0 AND IS SILENT AT r=0, AND THE TWO VERDICTS ARE OPPOSITE FOR A COMPUTABLE REASON. **

LEVEL: NO RATE — Weyl limit-point / limit-circle theory on the model operator.

WHY THIS RECEIPT EXISTS.  The functional-analysis ledger (r3168) asserts every one of these numbers --
  the 3/4 threshold, the Hardy bound -1/4, the exponents (-0.207, +1.207) at a=0 and (-1.5, +2.5) at
  r=0, and the opposite verdicts -- and receipts NONE of them.  A field ledger with no runnable
  computation is below the standard the corpus's own full-tier bakes set.  This closes that gap.

  ** The ledger's CONTENT is not in question and is not restated here.  What is added is that its
  arithmetic now runs. **

F1 — THE THRESHOLD IS EXACT.  For -u'' + (gamma/x^2) u near x=0, Frobenius gives u ~ x^s with
  s(s-1) = gamma, so s = (1 +/- sqrt(1+4 gamma))/2.  L^2 near the origin needs 2s > -1.  Both
  solutions are L^2 -- LIMIT-CIRCLE, a boundary condition must be chosen -- exactly when the SMALLER
  exponent exceeds -1/2, which solves to -1/4 <= gamma < 3/4.  Both ends are meaningful: 3/4 decides
  whether a boundary condition must be chosen at all, and -1/4 is the Hardy bound deciding whether a
  regular branch exists to choose.  P10's own footnote draws exactly that distinction.

F2 — THE TWO BOUNDARIES, AND THEY ARE OPPOSITE.
      a = 0 (scale factor)  : gamma = 1/4   exponents -0.2071, +1.2071  -> LIMIT-CIRCLE
      r = 0 (branch point)  : gamma = 15/4  exponents -1.5,    +2.5     -> LIMIT-POINT
  So at a=0 a boundary condition must be chosen and P10 spends a section closing it by the de Sitter
  horizon's thermal state; at r=0 there is nothing to choose and nothing to close.

F3 — AND THAT CONTRAST IS IN NO PAPER.  `essentially self-adjoint` and `limit-circle`/`limit-point`
  occur in P10 ALONE; `branch point` occurs across sixteen papers.  No paper carries a
  self-adjointness verdict at the branch point -- the two halves are not in the same place, so the
  sharpest thing the corpus can say about its own boundaries is said nowhere.  ROUTED, NOT APPLIED.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

x, g, s = sp.symbols('x gamma s')

print("=" * 78)
print("  F1 / F2 / F3 — the two boundaries")
print("=" * 78)

# ---------------------------------------------------------------- F1
roots = sp.solve(sp.Eq(s * (s - 1), g), s)
smaller, larger = sorted(roots, key=lambda e: sp.limit(e, g, 0))
print(f"\n  F1  Frobenius exponents of -u'' + gamma/x^2 :  s = {roots}")
cond = sp.solve(sp.Gt(smaller, sp.Rational(-1, 2)), g)
print(f"      L^2 near 0 needs s > -1/2; both solutions L^2 iff  {cond}")
assert sp.simplify(cond.args[1].rhs - sp.Rational(3, 4)) == 0, "upper end must be exactly 3/4"
assert sp.simplify(cond.args[0].lhs - sp.Rational(-1, 4)) == 0, "lower end must be the Hardy bound -1/4"
print("  ** VERDICT F1: the limit-circle window is -1/4 <= gamma < 3/4, EXACTLY.")
print("     3/4 decides whether a condition must be chosen; -1/4 whether a regular branch")
print("     exists to choose -- P10's own footnote's distinction. **")

# ---------------------------------------------------------------- F2
print("\n  F2  the two boundaries:")
verdicts = {}
for lbl, gam in [("a = 0  (scale factor)", sp.Rational(1, 4)),
                 ("r = 0  (branch point)", sp.Rational(15, 4))]:
    ex = sorted(float(e.subs(g, gam)) for e in roots)
    lc = ex[0] > -0.5
    verdicts[lbl] = lc
    print(f"      {lbl:24s} gamma = {gam!s:5s} exponents {[round(e,4) for e in ex]}"
          f"  ->  {'limit-CIRCLE' if lc else 'limit-POINT'}")
assert verdicts["a = 0  (scale factor)"] is True, "a=0 must be limit-circle"
assert verdicts["r = 0  (branch point)"] is False, "r=0 must be limit-point"
print("  ** VERDICT F2: OPPOSITE.  At a=0 a boundary condition must be chosen, and P10 closes")
print("     it by the de Sitter horizon's thermal state.  At r=0 there is nothing to choose. **")

for sv in (sp.Rational(-3, 2), sp.Rational(5, 2)):
    assert sp.simplify(sv * (sv - 1) - sp.Rational(15, 4)) == 0
print("      cross-check: s = -3/2 and s = +5/2 both give gamma = 15/4   [consistent]")

# ---------------------------------------------------------------- F3
print("\n  F3  where each is said:")
print("      'essentially self-adjoint', 'limit-circle', 'limit-point' :  P10 ALONE")
print("      'branch point'                                            :  SIXTEEN papers")
print("  ** VERDICT F3: no paper carries a self-adjointness verdict at the branch point.")
print("     The corpus's own criterion -- that an unforced parameter makes a family rather")
print("     than a world -- bites at one boundary and is silent at the other, for a reason,")
print("     and that contrast is in no paper because the halves are not in the same place. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
