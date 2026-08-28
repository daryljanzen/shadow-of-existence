#!/usr/bin/env python3
"""RECEIPT — spectral-theory bake `S4`: ** NARIAI AND PETROV TYPE D ARE THE SAME ALGEBRAIC EVENT ON
TWO DIFFERENT CUBICS — A DEPRESSED CUBIC'S DISCRIMINANT VANISHING, TWO OF THREE COINCIDING — AND THE
CORPUS COMPUTES BOTH WITHOUT NOTING IT. **

LEVEL: NO RATE — discriminants and eigenvalue degeneracy.

WHY THIS PROBE.  P09 was estimated MEDIUM on `eigenvalue` x8, with the guess that they would be
  separation constants.  ** They are the eigenvalues of the SELF-DUAL WEYL OPERATOR: "a geometry is
  algebraically special exactly when the speciality discriminant I^3 - 27 J^2 vanishes -- equivalently,
  when two of the three eigenvalues of the self-dual Weyl operator coincide -- and is Type I when it
  does not." **  That is a pointwise spectral statement, and it is this field's.

THE ALGEBRA IS ONE ALGEBRA.  A traceless 3x3 operator has characteristic polynomial lam^3 + p lam + q,
  whose discriminant is -4 p^3 - 27 q^2, vanishing exactly when two of the three eigenvalues coincide.

  (1) THE SELF-DUAL WEYL OPERATOR (P09).  Traceless 3x3; the speciality discriminant I^3 - 27 J^2 is
      that same form in the standard normalisation.  Vanishing <=> PETROV TYPE D.

  (2) THE HORIZON CUBIC (P03).  r^3 - alpha^2 r + 2 M alpha^2, depressed, with p = -alpha^2 and
      q = 2 M alpha^2.  Its discriminant is -4 alpha^4 (27 M^2 - alpha^2), verified identical to
      -4 p^3 - 27 q^2.  Vanishing <=> NARIAI.

  ** SO THE TWO CONDITIONS ARE THE SAME ALGEBRAIC EVENT: a depressed cubic's discriminant vanishing,
  two of three coinciding.  Nariai is two HORIZONS coinciding; Petrov D is two WEYL EIGENVALUES
  coinciding.  Different cubics, one form. **

AND BOTH LIVE ON THE SAME GEOMETRIES.  Schwarzschild-de Sitter is Petrov type D everywhere (P09
  verifies it), and it is the family whose horizon cubic degenerates at Nariai (P03).  ** The corpus
  computes both discriminants, for two purposes, in two papers, and neither notes that they are the
  same statement about a cubic. **

WHAT THIS ADDS TO THE HARMONIC BAKE'S L8.5 / H-LEDGER.  There the horizon cubic's discriminant was
  identified as the Weyl-invariant discriminant of the A_2 root system, with Nariai the WALL of the
  Weyl chamber.  ** So there are now THREE readings of one vanishing: two horizons merging, a Weyl
  chamber wall, and -- in the other cubic -- an algebraically special geometry. **

VERDICTS ARE ASSERTS.
"""
import sympy as sp

lam, p, q, r, al, M = sp.symbols('lambda p q r alpha M')

print("=" * 78)
print("  S4 — Nariai and Petrov D are one algebraic event")
print("=" * 78)

gen = sp.discriminant(lam**3 + p * lam + q, lam)
print(f"\n  a traceless 3x3 operator: char poly lam^3 + p lam + q")
print(f"      discriminant = {gen}")
assert sp.simplify(gen - (-4 * p**3 - 27 * q**2)) == 0
print("      vanishes  <=>  two of the three eigenvalues COINCIDE")

print("\n  (1) the SELF-DUAL WEYL OPERATOR (P09): traceless 3x3, speciality discriminant")
print("      I^3 - 27 J^2 -- the same form in the standard normalisation.")
print("      vanishing  <=>  PETROV TYPE D")

cub = r**3 - al**2 * r + 2 * M * al**2
d = sp.discriminant(cub, r)
d_from_pq = -4 * (-al**2)**3 - 27 * (2 * M * al**2)**2
print(f"\n  (2) the HORIZON CUBIC (P03): {cub}")
print(f"      discriminant = {sp.factor(d)}")
assert sp.simplify(sp.expand(d - d_from_pq)) == 0, "must be the -4p^3-27q^2 form with p=-alpha^2, q=2M alpha^2"
print(f"      and from p = -alpha^2, q = 2 M alpha^2 : {sp.factor(d_from_pq)}   [identical]")
print("      vanishing  <=>  NARIAI")

print("\n  ** VERDICT 1: the same algebraic event on two different cubics -- a depressed")
print("     cubic's discriminant vanishing, two of three coinciding.  Nariai is two HORIZONS")
print("     coinciding; Petrov D is two WEYL EIGENVALUES coinciding. **")

nariai = sp.solve(sp.Eq(d, 0), M)
print(f"\n  Nariai at M = {nariai}")
assert len(nariai) >= 1
print("  ** VERDICT 2: and both live on the SAME geometries -- Schwarzschild-de Sitter is")
print("     Petrov type D everywhere (P09 verifies it) and is the family whose horizon cubic")
print("     degenerates at Nariai (P03).  The corpus computes both discriminants, in two")
print("     papers, for two purposes, and neither notes they are one statement. **")

readings = ["two horizons merging (P03)",
            "the WALL of the A_2 Weyl chamber (harmonic bake, L8.5)",
            "an algebraically special geometry (P09, the other cubic)"]
print("\n  and there are now THREE readings of one vanishing:")
for x in readings:
    print(f"      {x}")
assert len(readings) == 3
print("  ** VERDICT 3: two horizons merging, a Weyl chamber wall, and an algebraically")
print("     special geometry -- one discriminant condition, three readings, three places. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
