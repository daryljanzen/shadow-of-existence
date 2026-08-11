"""A5.3 step (ii) — ARE THE INSTANCES THE SAME MOVE?
The criterion is P6's prin:reclass, adopted as the census's test at r1715:
  'an admissible W must EXPLAIN the perspectival appearances -- EXHIBIT THE PROJECTION under which
   they arise and show why they appear as they do -- not discard them, and not merely reproduce them.'
So the test is one question per instance: IS A PROJECTION EXHIBITED?"""
print("="*80); print("A5.3 (ii) — APPLYING prin:reclass TO THE GRADED CENSUS"); print("="*80)
rows=[
 ("TIER 1 · ontology-free","P2's continuation through r=0",
  "r(z)=M(1+cos z); the 'singularity' is the chart LABELLING a non-degenerate critical point 'r=0'","YES"),
 ("","P3's chain-rule artefact",
  "K(z)=48/(M^4(1+cos z)^6); the divergence is the chain rule AT that critical point of r(z)","YES"),
 ("","P3's overcritical continuation",
  "2M=(2/3sqrt3) sin 3w; |2M|>bound has no real w, so the DIAL runs off its own real axis","YES"),
 ("","P5's R-even/R-odd partition",
  "f = (1-r^2/a^2) + (-2M/r); the vantage-swap R exhibits which part is the reading's","YES"),
 ("TIER 2 · costs the layered reading","the horizon-singularity family",
  "the 4-manifold is the layer's RECORD; horizon and singularity are features of the record","YES"),
 ("","problem of time · hole argument · CTCs · GW-energy",
  "same projection: (M,g) represents S_t and does not constitute it","YES"),
 ("TIER 3 · costs the one-scale fact","the horizon problem",
  "the CMB's uniformity is the substrate's maximal symmetry, read through the FLRW appearance","YES"),
 ("","the local-cosmic boundary",
  "K_G = 1/a^2 - M/r^3 changes sign once; the 'boundary' is that flat locus read per structure","YES"),
 ("","*** the cosmological-constant problem ***",
  "rests on premises rejected: the Planck scale is not physical, and there is no bare-Lambda/vacuum SPLIT","-- ?"),
 ("","*** the coincidence problem ***",
  "Omega_m/Omega_Lambda = csch^2 is a CLOCK: we observe at ~one geometry-timescale","YES"),
]
print(f"\n{'tier':32s} {'instance':44s} projection exhibited?")
print("-"*112)
last=""
for t,inst,how,v in rows:
    print(f"{(t if t!=last else ''):32s} {inst[:43]:44s} {v}")
    print(f"{'':32s}   {how[:88]}")
    last=t or last
print("""
READ IT.  Nine of ten exhibit a projection.  The tenth -- the COSMOLOGICAL-CONSTANT problem -- does not,
and the census's own wording says why: it 'rests on two premises the framework rejects'.  Rejecting a
premise is not exhibiting a projection.  Nothing is shown to be the shadow of anything; a QUANTITY that
the standard account computes (the vacuum estimate) is denied the status of a competitor, because there
is no bare-Lambda-versus-vacuum-energy SPLIT for a cancellation to act on and no free dimensionless
constant to tune.
""")
print("*** SO THE INSTANCES ARE NOT ONE MOVE. THEY ARE TWO, AND BOTH ARE P6's OWN: ***")
print("   MOVE A -- RECLASSIFICATION (prin:reclass): exhibit the projection; the appearance is a shadow.")
print("             Nine instances, across all three ontology-cost tiers.")
print("   MOVE B -- LEAST-ARBITRARINESS (R2 in the ontological register): there is no unforced modulus,")
print("             so the problem has no parameter to be a problem ABOUT.  The CC problem, alone.")
print("\n   The two are NOT the same and the difference is checkable: Move A leaves the appearance standing")
print("   and re-reads it; Move B denies that there was a quantity to explain.  An objector to A must")
print("   dispute a projection; an objector to B must produce a second free constant.")

print("\n" + "="*80)
print("AND THAT ANSWERS THE TAXONOMY'S QUESTION -- 'MECHANISM OR COINCIDENCE?' -- BETTER THAN 'ONE MOVE'")
print("="*80)
print("""
  A COINCIDENCE would be: N dissolutions with no shared form, a scorecard.
  ONE MOVE would be: N instances of a single operation.
  WHAT IS THERE: TWO operations, each with a criterion, each stated in P6, and the split is not
  arbitrary -- it tracks WHAT AN OBJECTOR MUST DISPUTE.

  That is a STRONGER answer than 'one move', for the reason A5.3's own step (iii) needs:
  the two moves have INDEPENDENT failure conditions.  Move A fails if a projection cannot be
  exhibited.  Move B fails if a second free dimensionless constant is produced.  Neither failure
  implies the other, so the two families do not stand or fall together --
  *** and a pattern that recurs across TWO independent criteria is better evidence about the frame
      than the same count under one. ***
  A5.3(iii) reads: 'the pattern's reliability across INDEPENDENT problems is a claim about the frame'.
  The independence it needs is now supplied twice over: by ontology-cost (the census's own grading,
  the ontology-free tier presupposing no frame) and now by MOVE-TYPE.
""")
print("  CAVEAT, held: the coincidence problem sits with MOVE A (the csch^2 clock IS a projection),")
print("  so the fine-tuning PAIR is split across the two moves.  The census groups them; this")
print("  separates them, and the separation is the finding.")
print("="*80)

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# Pins the count this receipt's whole conclusion rests on: applying prin:reclass to the graded
# census gives TEN instances, of which exactly NINE exhibit a projection (MOVE A) and exactly ONE
# -- the cosmological-constant problem -- does not (MOVE B, least-arbitrariness).  If a row is
# added, dropped, or re-verdicted, "nine of ten" and "the CC problem, alone" stop being true and
# this fails.
_yes = [row for row in rows if row[3] == "YES"]
_not = [row for row in rows if row[3] != "YES"]
assert len(rows) == 10, f"census is {len(rows)} instances, not the ten the text reads"
assert len(_yes) == 9, f"{len(_yes)} instances exhibit a projection, not the nine the text reads"
assert len(_not) == 1 and "cosmological-constant" in _not[0][1], \
    f"the sole non-projection instance is not the CC problem: {[r[1] for r in _not]}"
# and the graded tiers the independence argument uses are all three, still populated.
assert len({row[0] for row in rows if row[0]}) == 3
