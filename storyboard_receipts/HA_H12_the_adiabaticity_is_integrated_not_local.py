#!/usr/bin/env python3
"""RECEIPT — harmonic-analysis bake `H12`: ** P07'S ADIABATICITY PARAMETER SEPARATES AS C/mu_n EXACTLY
AS CLAIMED, AND ITS LOCAL VALUE DIVERGES AT THE BRANCH POINT FOR EVERY MODE — SO C MUST BE AN
INTEGRATED QUANTITY, AND THE SENTENCE READS AS A LOCAL ONE. **

LEVEL: NO RATE — WKB on the tower's frequencies along the segment.

WHY THIS PROBE.  The second of the reach owed after r3453.  P07 carries harmonic vocabulary x55 and
  this bake had never read it.  P07 states: "the tower's frequencies diverge at the branch point but
  only as s^{-2/3} ... ITS ADIABATICITY IS CONTROLLED BY THE HARMONIC INDEX ALONE, the parameter being
  C/mu_n with C <= 1.72, which is of order unity only at n=2 and n=3."

WHAT IS CONFIRMED — THE SEPARATION IS REAL.  With omega_n(s) = mu_n f(s), the WKB adiabaticity
  parameter is |omega-dot / omega^2| = (1/mu_n) |f'/f^2|.  ** The mode index factors out exactly, so
  "controlled by the harmonic index alone" is structurally correct and not an approximation. **

WHAT IS NOT SAID — AND IT MATTERS.  With f = s^{-2/3}, |f'/f^2| = (2/3) s^{-1/3}, which DIVERGES as
  s -> 0.  ** So the LOCAL adiabaticity parameter is unbounded at the branch point for EVERY n, not
  merely of order unity at n=2 and n=3. **  The divergence is integrable -- int_0^1 (2/3) s^{-1/3} ds
  = 1 -- which is why P07 can say, correctly, that the adiabatic CORRECTION is finite.

  ** So C <= 1.72 cannot be a local maximum; it must be an integrated quantity.  The sentence "the
  parameter being C/mu_n" reads as a local statement, and locally there is no such bound. **

AND THE CORPUS DOES NOT DISTINGUISH THEM.  storyboard_receipts/LOWL_adiabatic_bearing.py uses
  C = 1.72 as a given constant and neither derives it nor says which quantity it is.

  NOTE ON SCOPE: f = s^{-2/3} is P07's stated leading behaviour, and the numerical value of the
  integral depends on the segment's range and on subleading terms.  ** This receipt asserts the
  DIVERGENCE of the local parameter and the CONVERGENCE of its integral, not a value for C. **

ROUTED, NOT APPLIED.  The clause owed is one word: whether C bounds the local parameter or its
  integral along the segment.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

s, mu = sp.symbols('s mu', positive=True)

print("=" * 78)
print("  H12 — P07's adiabaticity parameter: local or integrated?")
print("=" * 78)

f = s**sp.Rational(-2, 3)
omega = mu * f
local = sp.simplify(sp.Abs(sp.diff(omega, s) / omega**2))
print(f"\n  omega_n(s) = mu_n * s^(-2/3)   (P07's stated leading behaviour)")
print(f"  WKB parameter |omega' / omega^2| = {local}")

sep = sp.simplify(local * mu)
assert not sep.has(mu), "the mode index must factor out exactly"
print(f"  times mu_n  ->  {sep}   (no mu remains)")
print("  ** VERDICT 1: the parameter separates EXACTLY as C/mu_n.  P07's 'controlled by the")
print("     harmonic index alone' is structurally correct, not an approximation. **")

lim = sp.limit(sep, s, 0)
print(f"\n  local factor as s -> 0 (the branch point): {lim}")
assert lim == sp.oo, "the local parameter must diverge at the branch point"
print("  ** VERDICT 2: the LOCAL parameter is UNBOUNDED for EVERY n -- not of order unity at")
print("     n=2,3 and small elsewhere, but divergent at the branch point throughout. **")

I = sp.integrate(sep, (s, 0, 1))
print(f"\n  integral of the local factor over the segment: int_0^1 = {sp.simplify(I)}")
assert I.is_finite, "the divergence must be integrable"
print("  ** VERDICT 3: FINITE.  So the adiabatic CORRECTION is finite, exactly as P07 says --")
print("     and C <= 1.72 must therefore bound the INTEGRATED quantity, not the local one. **")

print("\n  ** VERDICT 4: the sentence 'the parameter being C/mu_n with C <= 1.72' reads as a")
print("     LOCAL statement, and locally no such bound exists.  The corpus's own")
print("     LOWL_adiabatic_bearing.py uses 1.72 as a given and does not distinguish them.")
print("     What is owed is one word. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
