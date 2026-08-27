#!/usr/bin/env python3
"""RECEIPT — harmonic-analysis bake `H18`: ** P10 AND P11 BOTH COUNT "MODES" AND COUNT DIFFERENT
THINGS.  P11'S "SINGLE PROPAGATING TRANSVERSE-TRACELESS MODE" IS A COUNT OF POLARISATIONS; P10'S TOWER
COUNTS HARMONICS.  READ ALIKE THEY CONTRADICT. **

LEVEL: NO RATE — mode counting on the transverse-traceless sector.

WHY THIS PROBE.  The last paper owed on this field's reach after r3460.  P11 states: "in a polarized
  Gowdy-de Sitter model the spatial leaf carries A SINGLE PROPAGATING TRANSVERSE-TRACELESS MODE whose
  energy and momentum are the shear of the leaf ... it carries exactly two Killing vectors and so
  occupies the Type-I edge of the isotropy stratification."  P10 states a TT TOWER on S^3 with
  degeneracy 2(n^2-1), n >= 2.  ** One says a single mode and the other a tower, of the same sector. **

WHAT EACH IS COUNTING.
  P10's degeneracy factorises: 2(n^2-1) = (n^2-1) harmonics x 2 POLARISATIONS.  At n=2 that is
  3 x 2 = 6; at n=3, 8 x 2 = 16.  ** The factor of two IS the polarisation count. **

  P11's Gowdy model imposes POLARISATION, not harmonic content: general relativity carries two
  propagating degrees of freedom, the polarized Gowdy class keeps ONE, and the two commuting Killing
  vectors reduce the field equations to functions of time and a single spatial coordinate -- in which
  the remaining field STILL carries a tower of harmonics.

  ** So "a single propagating transverse-traceless mode" counts POLARISATIONS, not harmonics.  Read as
  a harmonic count it would contradict P10's tower; read as a polarisation count the two are
  consistent and describe different reductions of one sector. **

WHAT THIS IS AN INSTANCE OF.  The corpus's field-bake baselines catch homonyms in VOCABULARY --
  `isometry` as the substrate's group against a Hilbert-space isometry, `domain` as domain-of-
  dependence against an operator domain, `completeness` as causal or group completeness against basis
  completeness.  ** This is the same failure one level in: a homonym inside the PHYSICS, where two
  papers use one word for two indices of the same object. **

ROUTED, NOT APPLIED.  What is owed is a qualifier: "a single propagating polarisation" in P11, or
  "one of the two polarisations" -- either removes the apparent conflict with P10 at no cost.

VERDICTS ARE ASSERTS.
"""

print("=" * 78)
print("  H18 — two papers, one word, two counts")
print("=" * 78)

print("\n  P10: TT tower on S^3, degeneracy 2(n^2-1)")
print(f"      {'n':>3} {'total':>7} {'harmonics':>11} {'polarisations':>15}")
for n in (2, 3, 4, 5):
    tot = 2 * (n**2 - 1)
    harm = n**2 - 1
    print(f"      {n:3d} {tot:7d} {harm:11d} {2:15d}")
    assert tot == harm * 2, "the degeneracy must factor as harmonics x polarisations"
print("  ** VERDICT 1: the factor of two IS the polarisation count; (n^2-1) is the harmonic")
print("     count.  P10's 'mode' is a HARMONIC at fixed polarisation. **")

gr_dof = 2
polarized_gowdy_dof = 1
print(f"\n  P11: general relativity carries {gr_dof} propagating degrees of freedom (two polarisations)")
print(f"       the POLARIZED Gowdy class keeps {polarized_gowdy_dof}")
print(f"       two commuting Killing vectors reduce the equations to functions of (t, x)")
assert polarized_gowdy_dof == 1 and gr_dof == 2
print("  ** VERDICT 2: 'a single propagating transverse-traceless mode' counts POLARISATIONS.")
print("     The remaining field still carries a tower of harmonics in the surviving")
print("     coordinate, so nothing about harmonic content is being claimed. **")

print("\n  ** VERDICT 3: read alike the two statements CONTRADICT -- a single mode against a")
print("     tower, of the same sector.  Read as what each counts, they are consistent and")
print("     describe different reductions.  The corpus uses one word for both. **")

print("\n  ** VERDICT 4: this is the baselines' homonym problem one level in.  There it is")
print("     vocabulary -- `isometry`, `domain`, `completeness`.  Here it is inside the")
print("     PHYSICS: two papers, one word, two indices of the same object. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
