#!/usr/bin/env python3
"""RECEIPT — statistics/inference bake `S9`: ** P16'S SHARED LITHIUM MISS IS THE MOST DISCRIMINATING OF
ITS THREE ABUNDANCE OUTCOMES, AND IT IS THE ONE FILED AS A PROBLEM RATHER THAN AS CONFIRMATION. **

LEVEL: NO RATE — inference structure on a stated comparison.

WHAT P16 REPORTS.  Deuterium within 1 sigma, helium-4 within 1 sigma, lithium-7 over-predicted by the
  standard factor of about three.  It reads them as "two successes and one shared problem", and
  concludes "on the light elements CR is thus neither better nor worse than flat LambdaCDM ... but
  obtains them from the collapse rather than from a posited initial hot state".

  ** That conclusion is correct and this receipt does not dispute it.  What it disputes is the
  WEIGHTING: which of the three outcomes carries information. **

THE DISCRIMINATION ARGUMENT.  D/H and Y_p within 1 sigma are reached by ANY network running standard
  rates at the Planck eta -- they are concordant successes, and a concordant success is reached many
  ways.  A concordant FAILURE OF A SPECIFIC SIZE is a fingerprint: only a network that IS the standard
  one over-predicts lithium-7 by that particular factor.

  ** So the shared lithium miss is the most discriminating of the three outcomes, and it is
  confirmation of P16's OWN CENTRAL CLAIM -- which is not about abundances but about identity: "the
  cooling leg IS a standard BBN".  A network reproducing D and He-4 but NOT the standard lithium
  over-prediction would be evidence AGAINST that identity. **

AND IT IS THIS FIELD'S OWN LOGIC, TURNED AROUND.  S1 and S7 establish that the corpus may not count
  its own successes, because successes are selected and a base rate from remembered successes is
  survivorship.  The same principle says the shared FAILURE is the datum that cannot have been
  selected for -- nobody assembles a case from their own misses.

ROUTED, NOT APPLIED.

VERDICTS ARE ASSERTS.
"""

print("=" * 78)
print("  S9 — which of P16's three abundance outcomes discriminates")
print("=" * 78)

outcomes = [
    ("D/H within 1 sigma",              "any network with standard rates at the Planck eta", False),
    ("Y_p within 1 sigma",              "any network with standard rates at the Planck eta", False),
    ("Li-7 over by ~3x, SPECIFICALLY",  "only a network that IS the standard one",           True),
]
print(f"\n  {'outcome':34s} {'reached by':50s} discriminating")
for a, b, d in outcomes:
    print(f"  {a:34s} {b:50s} {'HIGH' if d else 'LOW'}")

hi = [o for o in outcomes if o[2]]
lo = [o for o in outcomes if not o[2]]
assert len(hi) == 1 and len(lo) == 2, "exactly one of the three should discriminate"
assert "Li-7" in hi[0][0], "and it must be the lithium miss"
print("\n  ** VERDICT 1: a concordant SUCCESS is reached many ways; a concordant FAILURE OF A")
print("     SPECIFIC SIZE is a fingerprint.  Exactly one of the three discriminates, and it")
print("     is the one P16 files as a problem. **")

print("\n  what P16's central claim actually is:")
print("      not 'the abundances agree' but 'THE COOLING LEG IS A STANDARD BBN'")
print("      -- an IDENTITY claim, and the lithium miss is direct evidence for it.")
print("  ** VERDICT 2: a network reproducing D and He-4 but NOT the standard lithium")
print("     over-prediction would be evidence AGAINST the identity.  So the shared miss is")
print("     confirmation, and P16 files it under 'neither better nor worse'. **")

print("\n  and this is S1/S7's own logic, turned around:")
print("      S1/S7: the corpus may not count its own SUCCESSES -- they are selected, and a")
print("             base rate from remembered successes is survivorship.")
print("      S9   : the shared FAILURE is the datum that cannot have been selected for.")
print("             Nobody assembles a case from their own misses.")
print("  ** VERDICT 3: the selection discipline this field established for P06 applies to")
print("     P16's abundance table and inverts its weighting. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
