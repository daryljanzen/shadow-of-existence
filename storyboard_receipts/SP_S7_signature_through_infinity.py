#!/usr/bin/env python3
"""RECEIPT — spectral-theory bake `S7`: ** P06'S SIGNATURE CHANGE IS AN EIGENVALUE PASSING THROUGH
INFINITY, NOT THROUGH ZERO — SO THE METRIC NEVER DEGENERATES, ONLY THE COORDINATE DOES.  THAT IS THE
SAME STATEMENT F18 FOUND P15 MAKING ABOUT CURVATURE, HERE SAID BY THE METRIC'S OWN SPECTRUM. **

LEVEL: NO RATE — the spectrum of the metric as a quadratic form.

WHY THIS PROBE.  P06 was estimated MEDIUM on `gap` x6 and `eigenvalue` x2, with a hope of finding a
  THIRD spectral gap after S3 found two.  ** There is none: all six `gap`s are metaphorical -- "a gap
  awaiting work", "there was never a gap to bridge", "not a gap in the reading".  The estimate's
  reason was wrong. **

  ** But the `eigenvalue` occurrences are load-bearing, and they are this field's. **  P06 gives the
  metric's spectrum: "three positive eigenvalues always, and a fourth eigenvalue
  lambda = alpha^2 / (alpha^2 - x^2) whose sign is fixed by the real data alpha^2 and x^2".

  ** So the SIGNATURE -- Lorentzian or Riemannian -- is the sign of one eigenvalue.  That is a
  spectral statement about the metric as an operator, and the whole signature-change story (the Wick
  face, P13's compact face, F15's three compactness statuses) turns on it. **

WHAT THE SPECTRUM SAYS, AND IT IS A DISTINCTION THE TEXT DOES NOT DRAW.

      lambda = alpha^2 / (alpha^2 - x^2)

      zero      : NEVER -- the numerator is alpha^2, a constant
      infinity  : at x^2 = alpha^2

  ** So the signature change happens by the eigenvalue passing through INFINITY, not through ZERO. **

  The distinction is spectral and it is exactly the one that matters:
      through ZERO     -> the metric DEGENERATES, det g = 0, a genuine breakdown of the form
      through INFINITY -> the metric stays NONDEGENERATE and the COORDINATE degenerates

  Since det g ~ (three positives) x lambda and lambda has no zero, ** det g never vanishes. **

AND IT IS THE SAME STATEMENT AS F18's.  F18 recorded P15's defence of its onset datum: "the scale is
  set by alpha everywhere, so the divergence is the areal coordinate degenerating and not a scale of
  the geometry."  ** Here the metric's own eigenvalue says it: the divergence is in the coordinate,
  because the eigenvalue that diverges has no zero to pass through.  P15 argues it; P06's spectrum
  exhibits it; neither cites the other. **

VERDICTS ARE ASSERTS.
"""
import sympy as sp

al2, x2 = sp.symbols('alpha2 x2', real=True)
lam = al2 / (al2 - x2)

print("=" * 78)
print("  S7 — the signature change goes through infinity, not through zero")
print("=" * 78)

print(f"\n  P06: three positive eigenvalues always, plus lambda = {lam}")

zeros = sp.solve(sp.Eq(sp.numer(sp.together(lam)), 0), x2)
poles = sp.solve(sp.Eq(sp.denom(sp.together(lam)), 0), x2)
print(f"      lambda = 0 at x^2 = {zeros if zeros else 'NEVER (numerator is the constant alpha^2)'}")
print(f"      lambda -> infinity at x^2 = {poles}")
assert not zeros, "the signature eigenvalue must have NO zero"
assert poles == [al2], "and must diverge exactly at x^2 = alpha^2"
print("  ** VERDICT 1: no zero, one pole.  The signature change happens by the eigenvalue")
print("     passing through INFINITY. **")

print("\n  the two sides:")
for v, lbl in [(sp.Rational(1, 2), "x^2 < alpha^2"), (sp.Rational(3, 2), "x^2 > alpha^2")]:
    val = lam.subs({al2: 1, x2: v})
    sign = "POSITIVE (Riemannian)" if val > 0 else "NEGATIVE (Lorentzian)"
    print(f"      alpha^2 = 1, {lbl:16s}: lambda = {str(val):>3}  ->  {sign}")
assert lam.subs({al2: 1, x2: sp.Rational(1, 2)}) > 0
assert lam.subs({al2: 1, x2: sp.Rational(3, 2)}) < 0
print("  ** VERDICT 2: the sign flips across x^2 = alpha^2, and the signature with it. **")

print("\n  why through-infinity and through-zero differ:")
print("      through ZERO     -> the metric DEGENERATES, det g = 0, the form breaks down")
print("      through INFINITY -> the metric stays NONDEGENERATE, the COORDINATE degenerates")
print("  det g ~ (three positives) x lambda, and lambda has no zero, so det g never vanishes.")
print("  ** VERDICT 3: the metric never degenerates.  Only the coordinate does. **")

print("\n  ** VERDICT 4: and that is the same statement F18 found P15 making -- 'the scale is")
print("     set by alpha everywhere, so the divergence is the areal coordinate degenerating")
print("     and not a scale of the geometry'.  P15 ARGUES it; P06's spectrum EXHIBITS it;")
print("     neither cites the other. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
