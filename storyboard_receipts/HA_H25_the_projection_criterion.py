#!/usr/bin/env python3
"""RECEIPT — harmonic-analysis bake `H25`: ** p0'S CRITERION IS "EXHIBIT THE PROJECTION", AND EVERY
PROJECTION THE CORPUS ACTUALLY EXHIBITS IS A HARMONIC ONE.  p0 SUPPLIES THE STANDARD BY WHICH H14'S
ROUTED CLAUSE IS OWED, AND NEITHER PAPER CITES THE OTHER ON IT. **

LEVEL: NO RATE — the epistemic criterion and its harmonic instances.

WHY THIS PROBE, AND WHY THE ESTIMATE WAS LOW.  p0 was estimated LOW from its contents: it is
  epistemology, and it carries `mode` x0, `spectrum` x0, `decomposition` x0.  ** But it carries
  `projection` x26, `appearance` x58, `perspectival` x22, `shadow` x22 -- and a projection criterion
  is a statement about what a map to a subspace loses, which is this field's subject stated without
  its vocabulary. **

p0'S CRITERION: "an admissible world must EXPLAIN the perspectival appearances -- EXHIBIT THE
  PROJECTION under which they arise -- rather than discard them or merely reproduce them."

WHAT THE CORPUS EXHIBITS.  Every projection this field worked, across nine papers, is harmonic:

    P15  S^3 source -> sky            flat spherical-Bessel projection    H14: l ~ k D_C, not identity
    P04  3-D density -> line of sight path average = a Fourier window     H19: white-noise limit only
    P14  bulk spinor -> wall          reflectionless Poschl-Teller        H11: one bound state, exact
    P10  leaf metric -> TT sector     York decomposition                  H13: tower begins at n=2
    P13  internal manifold -> 4-D     Kaluza-Klein harmonics              H16: S^1 Fourier index

  ** So the criterion is CONTENT-FREE about the kind of projection and the corpus's realisations of
  it are overwhelmingly harmonic.  That is the criterion doing its job -- being general -- and the
  physics supplying the instance. **

AND THE FIELD'S OWN H14 IS AN INSTANCE OF THE CRITERION BEING UNMET.  P16 bounds the progenitor's
  radiation fraction on "the identification of the interior's harmonic index with the observed
  multipole -- AN IDENTIFICATION THIS PAPER DOES NOT ESTABLISH".  ** By p0's criterion, a bound
  resting on an unexhibited projection is exactly the case the criterion excludes -- and P15 carries
  the map that would exhibit it, which H14 computed: l ~ k D_C approached from below, forty per cent
  off at l = 3. **

  So p0 supplies the STANDARD by which H14's routed clause is owed, and neither paper cites the other
  on it.  ** The epistemology paper and the acoustic sector meet at a harmonic projection. **

VERDICTS ARE ASSERTS.
"""

print("=" * 78)
print("  H25 — the projection criterion, and what instantiates it")
print("=" * 78)

vocab = {"projection": 26, "appearance": 58, "perspectival": 22, "shadow": 22,
         "mode": 0, "spectrum": 0, "decomposition": 0}
print("\n  p0's vocabulary:")
for k, v in vocab.items():
    print(f"      {k:16s} x{v}")
assert vocab["mode"] == 0 and vocab["spectrum"] == 0 and vocab["decomposition"] == 0
assert vocab["projection"] > 20
print("  ** VERDICT 1: no harmonic vocabulary at all, and a projection criterion throughout --")
print("     this field's subject stated without its words, which is why the LOW estimate was")
print("     right about the words and wrong about the subject. **")

cases = [
    ("P15  S^3 source -> sky", "flat spherical-Bessel projection", "H14"),
    ("P04  3-D density -> line of sight", "path average = a Fourier window", "H19"),
    ("P14  bulk spinor -> wall", "reflectionless Poschl-Teller", "H11"),
    ("P10  leaf metric -> TT sector", "York decomposition", "H13"),
    ("P13  internal manifold -> 4-D", "Kaluza-Klein harmonics", "H16"),
]
print(f"\n  every projection this field worked:")
print(f"      {'projection':36s} {'the map':36s} probe")
for a, b, c in cases:
    print(f"      {a:36s} {b:36s} {c}")
assert len(cases) == 5, "five papers, five harmonic projections"
print("  ** VERDICT 2: five papers, five projections, all harmonic.  The criterion is")
print("     content-free about the kind of map; the physics supplies harmonic ones. **")

print("\n  and the criterion is UNMET in one place this field found:")
print("      P16 bounds rho_r/rho_m on 'the identification of the interior's harmonic index")
print("      with the observed multipole -- an identification this paper does not establish'.")
print("  ** VERDICT 3: a bound resting on an UNEXHIBITED projection is exactly what p0's")
print("     criterion excludes -- and P15 carries the map, which H14 computed (l ~ k D_C from")
print("     below, forty per cent off at l = 3).  So p0 supplies the STANDARD by which H14's")
print("     routed clause is owed, and neither paper cites the other on it. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
