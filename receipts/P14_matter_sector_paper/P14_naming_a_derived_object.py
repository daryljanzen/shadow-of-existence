"""
P14_naming_a_derived_object.py -- P14 sec:chirality (convention footnote): "the wall" is used in
the bare singular 180 times against 17 plurals, for an object this construction places THREE of
-- and that ratio is the proximate cause of the sector's largest reading drift.

WHAT PROMPTED IT.  A standing lead asked where else the corpus "names a derived object after its
source and then reasons on the name", the known instance being "the six hinges" for what are
three LINES piercing twice.  It named two places to sweep: walls vs wall-loci, roots vs
designations.

WHAT IS ESTABLISHED.
  1. THE CENSUS, across the papers with appendices excluded.  "the wall" 180 : 17; "the branch
     point" -- the same locus under its other name -- 142 : 8; "the hinge" 75 : 6; "the vantage"
     59 : 6; "the root" 65 : 32; "the leg" 13 : 5; "the horn" 8 : 4; "the ruling" 7 : 16.
  2. ** THE CENSUS IS NOT A DEFECT LIST. **  A bare singular is correct when it means "the wall
     of the hinge under discussion".  The defect is the singular used AND REASONED ON as though
     the object were unique.
  3. ** AND THAT IS THE PROXIMATE CAUSE OF THIS SECTOR'S LARGEST DRIFT. **  The winding
     computations wrote "near the wall $r^3=\tfrac92 M\ell^2$, so a crossing sends
     $r\mapsto\omega r$" and "each graze-point crossing sends $r\mapsto\omega r$".  Read with a
     unique wall those say there is ONE radial function branching at three places -- cyclic
     cover, abelian monodromy, $Z_3$, no colour.  Read with three walls they say each vantage's
     own radius branches at its own wall -- diagonal monodromy, non-abelian, $SU(3)$.  ** The
     whole colour result is that difference, and the definite article hid it. **
  4. ** THE SWEEP NARROWS RATHER THAN SPREADS. **  One locus carries the defect, under both its
     names.  The lead's second candidate -- roots vs designations -- does NOT show it: 65 : 32
     is a corpus talking about three things.
  5. ** AND THE FIRST DIAGNOSTIC PROPOSED HERE WAS WRONG, WHICH THE CENSUS CAUGHT IN THE SAME
     RUN. **  "Ratio above 10:1" flags the hinge (12:1) and the vantage (10:1), both already
     cleared.  The rule needs two conditions: a high ratio AND a BARE rather than RELATIONAL
     singular.  "The hinge" means the one being swung about and "the vantage" the one looking --
     each carries its index inside the phrase; "the wall" carries none and says nothing about
     whose.  ** That is why the wall is at risk at 11:1 while the hinge is safe at 12:1. **
  6. ** THE FIX IS NOT FIND-AND-REPLACE **: 180 sites, most correct, and mass-editing correct
     sentences to guard a misreading is the wrong trade.  It is a STATED CONVENTION, in the form
     this paper already uses for the R/P/T parities -- and condition (5)(ii) is exactly what the
     convention supplies: it makes the bare form relational by fiat, moving the object out of the
     at-risk column without touching a sentence.

** THE CLASS, STATED SO IT CAN BE RECOGNISED: an object of multiplicity N>1 whose natural
sentences are about one at a time, so the plural almost never appears -- until some later result
needs all N at once, by which time the singular has been reasoned on for hundreds of sentences
and reads as uniqueness.  The pathology is a function of what the object is USED for, not of
carelessness. **

ORIGIN: computations/baryon_edge/L060w_naming_a_derived_object.py -- built r2376 (c54.70); edit
the origin, not this copy."""
print(__doc__.split("Run:")[0])

# counts measured across the seventeen papers, appendices excluded (see the revision's commit)
CENSUS = [
    # object,            multiplicity, singular, plural, verdict
    ("the wall",              3, 180, 17, "AT RISK -- flagship"),
    ("the branch point",      3, 142,  8, "AT RISK -- same object"),
    ("the hinge",             3,  75,  6, "safe by construction"),
    ("the vantage",           3,  59,  6, "safe by construction"),
    ("the root",              3,  65, 32, "healthy ratio"),
    ("the leg",              12,  13,  5, "healthy ratio"),
    ("the horn",              2,   8,  4, "healthy ratio"),
    ("the ruling",            2,   7, 16, "plural-dominant, fine"),
]

# =====================================================================
print("=" * 78)
print("PART 1 — THE CENSUS")
print("=" * 78)
print(f"  {'object':>20} {'mult.':>6} {'singular':>9} {'plural':>7} {'ratio':>7}  verdict")
for o, m, s, p, v in CENSUS:
    r = f"{s/max(p,1):.0f}:1"
    print(f"  {o:>20} {m:>6} {s:>9} {p:>7} {r:>7}  {v}")
print()
print("  ** The census is not itself a defect list.  A singular definite is perfectly correct when")
print("     it means 'the wall of the hinge under discussion'.  ** The defect is the singular used")
print("     ** AND REASONED ON ** as though the object were unique. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE FLAGSHIP, AND IT IS THE MOST EXPENSIVE DEFECT OF THIS SESSION")
print("=" * 78)
for s in [
 "** 'the wall' -- 180 singular against 17 plural, for an object the matter construction places",
 "   THREE of. **  And 'the branch point' is the same locus counted again, 142 : 8.",
 "",
 "⌗ ** AND THIS IS NOT A STYLE OBSERVATION.  IT IS THE PROXIMATE CAUSE OF THE c54.52 FORK. **",
 "   The winding computations wrote:",
 "",
 "     'near THE WALL r^3 = (9/2) M l^2, so a crossing sends r -> omega r'",
 "     'EACH graze-point crossing sends r -> omega r'",
 "",
 "   ** Read with a unique wall, those two sentences say there is ONE radial function branching",
 "   at THREE places -- the cyclic cover, abelian monodromy, Z_3 and no colour.  Read with three",
 "   walls, they say each vantage's own radius branches at its own wall -- diagonal monodromy,",
 "   non-abelian, SU(3). **  The entire colour result is the difference, and the difference was",
 "   invisible because the definite article hid it.",
 "",
 "⚠ ** SO `L-60`'s CLASS OF ERROR PRODUCED THE SESSION'S LARGEST SINGLE DRIFT, and `L-60` was",
 "   sitting open in the register the whole time naming exactly that class and exactly that",
 "   candidate ('walls vs wall-loci'). **  ** A lead that names the class of a defect you are",
 "   about to commit is worth more than a lead that names a defect, and nothing in the register",
 "   surfaces it at the moment of committing. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHICH OF THE OTHERS ARE AT RISK")
print("=" * 78)
for s in [
 "** SAFE BY CONSTRUCTION -- 'the hinge' and 'the vantage'. **  Both are relational: the whole",
 "vacuum construction is *one door swung about one hinge*, so 'the hinge' means 'the one being",
 "swung about' and there is nothing to hide.  ** The reader supplies the index because the",
 "sentence is already about a chosen one. **",
 "",
 "** HEALTHY -- 'the root', 'the leg', 'the horn'. **  Plural usage is frequent enough that a",
 "reader meets the multiplicity early and often.  ** `L-60`'s second named candidate, 'roots vs",
 "designations', does NOT show the pathology: 65 : 32 is a corpus talking about three things. **",
 "",
 "⌗ ** SO THE SWEEP NARROWS RATHER THAN SPREADS, WHICH IS THE USEFUL OUTCOME. **  One locus --",
 "the wall, under both its names -- carries the defect, and it carries it because it is the one",
 "multiplied object the corpus almost never has occasion to mention in the plural: you write",
 "about a mode at *a* wall, never about all three at once, until the moment the group structure",
 "makes you.  ** The pathology is a function of what the object is USED for, not of carelessness. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE FIX")
print("=" * 78)
for s in [
 "⛔ ** NOT find-and-replace. **  180 sites, most of them correct, and 'the wall of the hinge",
 "   about which the slicing plane swings' cannot be written 180 times without wrecking the",
 "   prose.  ** Mass-editing correct sentences to guard against a misreading is the wrong trade. **",
 "",
 "✔ ** A STATED CONVENTION, in the paper that owns the object, in the form the corpus already",
 "   uses for exactly this purpose. **  P14 carries a footnote reading 'Corpus convention (fixed",
 "   at r968): R is the orientation/mass-reflection parity ... P is the areal spatial parity ...",
 "   T is the time reflection', precisely because those three were being confused.  ** The wall",
 "   needs the same treatment and has never had it. **",
 "",
 "⇒ ** THE CONVENTION TO STATE: 'the wall' and 'the branch point' denote THE WALL OF THE HINGE",
 "   UNDER DISCUSSION.  There are three, one per hinge, at distinct points of the throat circle",
 "   with disjoint support; each vantage's signed areal radius vanishes at its own and at neither",
 "   other.  A sentence that would be false if there were three is a sentence about one vantage",
 "   and must name it. **",
 "",
 "⌗ *That last clause is the operative one: it gives a reader a TEST rather than a definition.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE CLASS, STATED SO IT CAN BE RECOGNISED")
print("=" * 78)
for s in [
 "`L-60` asked where else the corpus names a derived object after its source and reasons on the",
 "name.  ** The sweep says: the risk is not naming, it is naming plus SCARCITY OF PLURAL USE. **",
 "",
 "   * an object with multiplicity N > 1;",
 "   * whose natural sentences are about ONE of them at a time;",
 "   * so that the plural almost never appears;",
 "   * until some later result needs all N at once -- ** and by then the singular has been",
 "     reasoned on for hundreds of sentences and reads as uniqueness. **",
 "",
 "⚠ ** AND MY FIRST DIAGNOSTIC WAS WRONG, WHICH THE CENSUS ITSELF CAUGHT. **  I proposed 'ratio",
 "   above about 10:1' -- but the table shows the hinge at 12:1 and the vantage at 10:1, both of",
 "   which I had already marked SAFE.  ** A rule that flags the objects I had just cleared is not",
 "   a rule, and the table refuted it in the same run that produced it. **",
 "",
 "⇒ ** THE DIAGNOSTIC NEEDS TWO CONDITIONS, AND THE SECOND IS THE ONE THAT DISCRIMINATES: **",
 "     (i)  a high singular-to-plural ratio -- the multiplicity is rarely met; AND",
 "     (ii) the singular form is BARE rather than RELATIONAL.",
 "   ** 'the hinge' means 'the one being swung about' and 'the vantage' means 'the one looking' --",
 "   each carries its own index inside the phrase, so a reader cannot mistake it for a unique",
 "   object.  'the wall' and 'the branch point' carry NO index and say nothing about whose. **",
 "   That is why the wall is at risk at 11:1 while the hinge is safe at 12:1.",
 "",
 "⌗ *And condition (ii) is also what the FIX supplies: the convention makes the bare form",
 "relational by fiat -- 'the wall' shall MEAN 'the wall of the hinge under discussion' -- which",
 "moves the object from the first column to the second without touching a single sentence.*",
 "",
 "⌗ *Registered as a diagnostic rather than built as a gate: it needs a list of multiplied objects",
 "that only a reader can supply, and a gate that needs hand-fed input is a checklist wearing a",
 "gate's clothes.*  ** The census belongs in the fermion-sector document, where the objects are",
 "enumerated already. **",
]:
    print("  " + s)

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# NOTE ON SCOPE.  The CENSUS above is a TYPED table, not a measurement -- this file opens no
# document -- so the counts themselves are not pinned here as facts about the corpus; the row
# in receipts/INDEX.md records that defect (c54.154).  What IS computed here, and is pinned
# below, is the ARGUMENT the table carries: the printed ratios, and the refutation of the
# one-condition 'ratio above 10:1' diagnostic BY THE TABLE'S OWN counter-example.
_ratio = {o: float(f"{s/max(p,1):.0f}") for o, m, s, p, v in CENSUS}
assert _ratio["the wall"] == 11 and _ratio["the hinge"] == 12 and _ratio["the vantage"] == 10, \
    "the printed ratios are 11:1 (wall), 12:1 (hinge), 10:1 (vantage)"
assert _ratio["the branch point"] == 18 and _ratio["the ruling"] == 0, \
    "the printed ratios are 18:1 (branch point) and 0:1 (the ruling, plural-dominant)"
# THE PUNCHLINE, which only holds if the ratio ORDER runs the wrong way round: the object the
# receipt marks AT RISK has a LOWER ratio than one it marks safe.  A one-condition rule
# therefore cannot separate them, whatever the threshold.
assert _ratio["the wall"] < _ratio["the hinge"], \
    "the wall is at risk at 11:1 while the hinge is safe at 12:1 -- ratio alone cannot discriminate"
_flagged = {o for o, r in _ratio.items() if r >= 10}
_at_risk = {o for o, m, s, p, v in CENSUS if v.startswith("AT RISK")}
assert _flagged == {"the wall", "the branch point", "the hinge", "the vantage"}, \
    "the 10:1 threshold flags exactly these four rows"
assert _at_risk == {"the wall", "the branch point"}, \
    "the table marks exactly two rows AT RISK -- one locus under both its names"
assert len(_flagged - _at_risk) == 2, \
    "the one-condition rule produces exactly two FALSE POSITIVES (hinge, vantage), refuting itself"
# and the sweep NARROWS: the at-risk pair is one object, and both entries carry multiplicity 3
assert all(m == 3 for o, m, s, p, v in CENSUS if o in _at_risk), \
    "both at-risk names denote the same multiplicity-3 locus"
assert "the root" not in _at_risk and _ratio["the root"] == 2, \
    "the lead's second candidate (roots vs designations) does NOT show the pathology at 2:1"
assert len(CENSUS) == 8, "the census tabulates eight objects"
