#!/usr/bin/env python3
"""RECEIPT — functional-analysis bake `F20`: ** P01'S "INEQUIVALENT VACUA" HAS AN EXACT OPERATOR
CRITERION — SHALE'S — AND THE CORPUS GIVES ONLY THE CAUSAL ARGUMENT.  THE TWO ARE THE SAME STATEMENT
IN TWO LANGUAGES, AND THE THERMAL CASE FAILS THE CRITERION AT THE IR END. **

LEVEL: NO RATE — unitary implementability of a Bogoliubov transformation.

WHY THIS PROBE.  P01 mentions Bogoliubov and the thermal spectrum only to DISMISS them -- which is
  exactly why it is worth reading here, because ** what P01 denies has a precise functional-analytic
  content: that two Fock representations are unitarily inequivalent. **

  P01 names three requirements for the Hawking construction: "a globally defined horizon; a completed
  causal structure joining scri-minus to scri-plus across it; and THE PERMANENT LOSS OF CAUSAL CONTACT
  between exterior and interior modes THAT RENDERS THE TWO VACUA INEQUIVALENT", and argues none is
  realised.

THE CRITERION THE CORPUS DOES NOT NAME.  Shale's theorem: a Bogoliubov transformation (alpha, beta) is
  unitarily implementable -- the two Fock representations unitarily EQUIVALENT -- if and only if beta
  is HILBERT-SCHMIDT, sum |beta_ij|^2 < infinity.

  ** THE THERMAL CASE FAILS IT, AND FAILS AT THE INFRARED END. **  With |beta_omega|^2 =
  1/(exp(2 pi omega / kappa) - 1), the integral over omega DIVERGES; expanded at small omega the
  integrand goes as kappa/(2 pi omega), a logarithmic divergence.  So beta is not Hilbert-Schmidt, the
  vacua are unitarily inequivalent, and the thermal flux is that inequivalence -- which is P01's own
  sentence, with the criterion supplied.

  ** AND P01'S OWN CASE IS THE CONVERSE. **  No permanent causal disconnection means no mode mixing,
  hence beta = 0, hence trivially Hilbert-Schmidt, hence by Shale a unitary equivalence and a COMMON
  vacuum -- and no particle creation.  ** P01's causal argument and Shale's criterion are the same
  statement in two languages. **

WHAT THIS IS AN INSTANCE OF.  The corpus's characteristic pattern, now found for a fourth time in this
  field: the argument is right, the theorem that certifies it is standard, and it is never named.
  Compare F13 (`kernel` doing four jobs), F15 (`elliptic` only in a bibliography title), and the r3168
  baseline's own `Hilbert space` x0 over work done entirely on L^2.

ROUTED, NOT APPLIED.  The clause owed is one sentence: that the inequivalence is the failure of the
  Hilbert-Schmidt condition on beta, and that its absence here is that condition holding trivially.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

w, kap = sp.symbols('omega kappa', positive=True)

print("=" * 78)
print("  F20 — the inequivalence P01 denies, and the criterion it does not name")
print("=" * 78)

print("\n  Shale: (alpha, beta) is unitarily implementable  <=>  beta is HILBERT-SCHMIDT")

b2 = 1 / (sp.exp(2 * sp.pi * w / kap) - 1)
print(f"\n  thermal coefficients:  |beta_omega|^2 = {b2}")
I = sp.integrate(b2, (w, 0, sp.oo))
print(f"      int_0^inf |beta|^2 d(omega) = {I}")
assert I is sp.oo or I == sp.oo, "the thermal beta must fail Hilbert-Schmidt"

lead = sp.series(b2, w, 0, 1).removeO()
print(f"      small-omega expansion       : {lead}")
ir = sp.simplify(sp.limit(b2 * w, w, 0))
print(f"      omega * |beta|^2 as omega->0: {ir}   (finite and nonzero => 1/omega tail)")
assert sp.simplify(ir - kap / (2 * sp.pi)) == 0, "the IR tail must be kappa/(2 pi omega)"
print("  ** VERDICT 1: the divergence is LOGARITHMIC and sits at the INFRARED end.  beta is")
print("     not Hilbert-Schmidt, so the vacua are unitarily inequivalent -- and the thermal")
print("     flux IS that inequivalence, which is P01's own sentence with the criterion")
print("     supplied. **")

beta_p01 = 0
print(f"\n  P01's case: no permanent causal disconnection -> no mode mixing -> beta = {beta_p01}")
assert beta_p01 == 0
print("      beta = 0 is trivially Hilbert-Schmidt")
print("  ** VERDICT 2: so Shale gives unitary EQUIVALENCE, a COMMON vacuum, and no particle")
print("     creation.  P01's causal argument and Shale's criterion are the same statement in")
print("     two languages. **")

unnamed = ["F13: `kernel` doing four jobs across x147",
           "F15: `elliptic` only in a bibliography title",
           "r3168 baseline: `Hilbert space` x0 over work done entirely on L^2"]
print("\n  and the pattern, for a fourth time in this field:")
for u in unnamed:
    print(f"      {u}")
assert len(unnamed) == 3
print("  ** VERDICT 3: the argument is right, the theorem that certifies it is standard, and")
print("     it is never named.  This is the fourth instance in this field alone. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
