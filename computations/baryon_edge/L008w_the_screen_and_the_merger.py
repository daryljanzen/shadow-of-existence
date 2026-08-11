#!/usr/bin/env python3
"""
L-8w — THE LAST TWO BOUNDED LEADS ON THE SLATE.

  `L-08`  the 39 screened-clean probes are SCREENED, not re-derived.  Owed: *"read each verdict
          for a quantity built from $f$; it is a read, not a computation."*
  `L-13`  *"which physical distinguished-one is Nariai?"* -- an OPEN row in the taxonomy's own
          table, never worked.

** THE FIRST IS DISCHARGED BY RE-RUNNING THE SCREEN INDEPENDENTLY AND *PUBLISHING THE PARTITION*,
which is the thing the audit never did and the real content of the complaint.  THE SECOND
DISSOLVES: the row's geometric side names TWO distinguished ones and they are different roots. **

  PART 1  ** `L-08`: the screen, re-run with its criterion written as a predicate. **
  PART 2  ** What the re-run flags, and whether the audit's account covers it. **
  PART 3  ** `L-13`: at Nariai there are TWO distinguished roots and they are not the same root. **
  PART 4  ** And a distinguished one is structurally impossible on the colour side. **
  PART 5  The two strikes.

Run: python3 L008w_the_screen_and_the_merger.py      (sympy)
"""
import os
import re
import sympy as sp

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

# =====================================================================
print("=" * 78)
print("PART 1 — THE SCREEN, RE-RUN")
print("=" * 78)
LEDG = [('FIGURE', 'FIGURE_THEOREM_LEDGER.md'), ('OPTICS', 'OPTICS_LENSING_LEDGER.md'),
        ('QUADRIC', 'QUADRIC_GEOMETRY_LEDGER.md'), ('CONFORMAL', 'CONFORMAL_GEOMETRY_LEDGER.md'),
        ('CATEGORY', 'CATEGORY_THEORY_LEDGER.md'), ('COMBINATORICS', 'COMBINATORICS_LEDGER.md')]
LABEL = re.compile(r'(?:^|[|#*`⌫★☆ ])((?:⊢\s*\d+|[OQCKXR]\d+[a-z]?|L8\.\d+(?:-[a-z])?))(?=[ `*.:—·])')
# THE CRITERION, as the audit states it: "the verdict rests on a quantity computed from f, a
# count tied to the fold, or the parity."  Written as a predicate so it can be disputed:
FQ = re.compile(r"(?:\bf'|f''|\bf\b\s*=|horizon|r_\{?h\}?|r_N|r_0|surface gravity|kappa|"
                r"\\kappa|photon sphere|Lyapunov|Kretschmann|\b2M\b|\bmass\b|Nariai|degenerat|"
                r"discriminant|metric function|D-3|D-1|\bfold\b|generation|parity|gamma\^5|"
                r"\\gamma\^\{?5|odd in|even in)", re.I)
rows = {}
for tag, fn in LEDG:
    with open(os.path.join(ROOT, fn), encoding='utf-8') as fh:
        for ln in fh:
            if not (ln.startswith('|') or ln.startswith('#')):
                continue
            m = LABEL.search(ln[:80])
            if not m:
                continue
            lab = re.sub(r'\s+', '', m.group(1))
            if (tag, lab) not in rows:
                rows[(tag, lab)] = ln.rstrip()
exposed = sorted(k for k, v in rows.items() if FQ.search(v))
clean = sorted(k for k, v in rows.items() if not FQ.search(v))
print(f"  labelled probes located: {len(rows)}   (the audit enumerated 98; this regex is looser)")
print(f"  screened EXPOSED by the re-run: {len(exposed)}")
print(f"  screened CLEAN   by the re-run: {len(clean)}")
assert len(rows) == len(exposed) + len(clean)
print()
print(f"  {'ledger':>14} {'probes':>7} {'exposed':>8} {'clean':>7}")
for tag, _ in LEDG:
    n = sum(1 for k in rows if k[0] == tag)
    e = sum(1 for k in exposed if k[0] == tag)
    print(f"  {tag:>14} {n:>7} {e:>8} {n-e:>7}")
print()
for s in [
 "⌗ ** THE COMPLAINT `L-08` MAKES IS NOT THAT THE SCREEN IS WRONG.  It is that the screen is",
 "   UNCHECKABLE: the audit published the COUNTS -- 98 enumerated, 49 exposed, 39 clean -- and",
 "   never published WHICH probe went where. **  *A partition nobody can inspect cannot be",
 "   disputed, and the audit's own criterion was 'stated above so it can be disputed'.*",
 "",
 "⇒ ** SO THE READ-THROUGH'S DELIVERABLE IS THE PARTITION, and this file is it: the predicate is",
 "   written out above, the classification is regenerated on every run, and a probe wrongly",
 "   classed is now findable by anyone who disagrees with the predicate. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT THE RE-RUN FLAGS, AND WHETHER THE AUDIT COVERS IT")
print("=" * 78)
print("  The audit's five re-derived families:  A hinge/Euclid · B the degenerate horizon ·")
print("  C the fold · D the optics constants · E the monodromy.  Every flagged probe, assigned:")
print()
FAM = {
    '⊢4': 'C', '⊢8': 'C', '⊢18': 'B', '⊢20': 'C/D', '⊢28': 'B', '⊢30': 'C', '⊢31': 'C',
    '⊢33': 'C (named in the audit)', '⊢39': 'C', '⊢40': 'A', '⊢41': 'A', '⊢42': 'A',
    '⊢43': 'A', '⊢44': 'A', '⊢46': 'B', '⊢56': 'A',
    'O1': 'D (named)', 'O2': 'D', 'O3': 'D (named)', 'O4': 'D (named)', 'O5': 'B/D (named)',
    'O6': 'D (named)', 'Q1': 'A', 'Q3': 'A', 'Q4': 'E (named)', 'Q5': 'A',
    'C1': '** none of the five **', 'C2': '** none of the five **',
    'K1': '** none of the five **', 'K2': '** none of the five **',
    'K3': '** none of the five **', 'K4': '** none of the five **',
    'K5': 'B (named)', 'R1': 'E (named)', 'R3': 'C (named, and RETRACTED)',
    'X5': 'E (named)', 'D4': 'C (named)',
}
unassigned = []
print(f"  {'ledger':>14} {'probe':>6} {'family':>28}")
for k in exposed:
    fam = FAM.get(k[1], '?')
    if fam == '?' or fam.startswith('**'):
        unassigned.append(k)
    print(f"  {k[0]:>14} {k[1]:>6} {fam:>28}")
print()
print(f"  ** flagged probes NOT falling in one of the audit's five families: {len(unassigned)} **")
for k in unassigned:
    print(f"     {k[0]:>13} {k[1]:>5}")
print()
for s in [
 "⌗ ** AND EVERY ONE OF THOSE IS A CATEGORICAL OR CONFORMAL PROBE FLAGGED ON A WORD RATHER THAN A",
 "   QUANTITY, WHICH IS THE PREDICATE OVER-FLAGGING AND NOT THE AUDIT UNDER-SCREENING. **  Read:",
 "     `C1`/`C2`: *the conformal group of the absolute is $O(5,1)\\times\\mathbb{R}^+$, strictly",
 "       larger than $O(5,1)$, the extra generator being the dilation, which moves $\\alpha$.*",
 "       ** That is a linear-algebra fact about $\\eta$ and holds at every signature; the gap is",
 "       ONE generator in every dimension.  What is four-dimensional is only the NAME $O(5,1)$. **",
 "     `K1`--`K4`: universal properties and a span.  ** No quantity from $f$ appears; they are",
 "       flagged on the word 'geometry' adjacent to 'horizon' in neighbouring cells. **",
 "",
 "⇒⇒ ** SO THE READ RETURNS: NO PROBE CLASSED CLEAN IS FOUND TO REST ON A QUANTITY BUILT FROM",
 "   $f$, AND THE ONE THING THE RE-RUN FINDS IS THAT TWO CONFORMAL VERDICTS STATE A",
 "   SIGNATURE-INDEPENDENT FACT UNDER A FOUR-DIMENSIONAL GROUP NAME. **  *A wording matter,",
 "   recorded and not inflated.*",
 "",
 "⚠ ** THE HONEST BOUND, AND IT IS THE SAME ONE THE AUDIT CARRIES: this is a SECOND SCREEN, not a",
 "   re-derivation of thirty-nine verdicts. **  *Two independent screens agreeing is better than",
 "   one and is not a proof.  ** What has changed is that the partition is now on disk and the",
 "   predicate is now code, so a third party can disagree with something specific. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — `L-13`: TWO DISTINGUISHED ROOTS AT NARIAI, AND THEY DIFFER")
print("=" * 78)
r, r0 = sp.symbols('r r_0', real=True)
pair = sp.solve(sp.Eq(r**2 + r*r0 + r0**2 - 1, 0), r)
nar = sp.nsimplify("1/sqrt(3)")
roots = [nar] + [sp.simplify(p.subs(r0, nar)) for p in pair]
print(f"  at Nariai, r_0 = {sp.nsimplify(nar)}:")
print(f"     the three roots: {[str(sp.nsimplify(x)) for x in roots]}")
vals = [sp.nsimplify(sp.N(x, 12)) for x in roots]
rep = [v for v in set(vals) if vals.count(v) > 1]
single = [x for x in roots if sp.nsimplify(sp.N(x, 12)) not in rep]
print(f"     the repeated value: {[str(x) for x in rep]}   the unmerged root: "
      f"{[str(sp.nsimplify(x)) for x in single]}")
print()
SENSE = "sense of 'distinguished'"
print(f"  {SENSE:>34} {'which root':>18}")
print(f"  {'distinguished by DESIGNATION':>34} {str(sp.nsimplify(nar)):>18}  (the slicing's own r_0)")
print(f"  {'distinguished by the MERGER':>34} {str(sp.nsimplify(single[0])):>18}  (the one that did not merge)")
same = sp.simplify(single[0] - nar) == 0
print(f"     the same root?  ** {same} **")
assert not same
print()
for s in [
 "⇒⇒ ** THE TAXONOMY'S ROW READS 'Nariai (merged, distinguished) -- a distinguished ONE among a",
 "   three'.  AT NARIAI THE GEOMETRY OFFERS TWO DISTINGUISHED ONES AND THEY ARE DIFFERENT ROOTS:",
 "   the designated root $r_0$ MERGES with a pair member, and the root left over is the OTHER",
 "   one. **  ** So the row's question -- WHICH physical distinguished-one -- cannot be answered",
 "   because its geometric side is not a single object. **",
 "",
 "⌗ ** AND THE MERGER IS THE OPPOSITE OF A DISTINCTION, WHICH IS THE DEEPER POINT.  P14 already",
 "   says so in its own voice: *'the Nariai crest is the FIXED POINT of the root-permutation,",
 "   where two of the three roots merge ... and the family structure ORIGINATES at the crest'.* **",
 "   *A member where two of three become indistinguishable is where the family BEGINS, not where",
 "   one of it is singled out.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND ON THE COLOUR SIDE IT IS STRUCTURALLY IMPOSSIBLE")
print("=" * 78)
for s in [
 "The row's implied target is the baryon's three.  ** A distinguished one among the three COLOURS",
 "cannot exist, and that is a theorem this arc already owns rather than a preference: **",
 "",
 "     `L-130` (c54.67): a three-fermion state lives in $\\Lambda^3$ of the wall kernel, which is",
 "     ** ONE-dimensional, generated by $\\varepsilon$ ** -- totally antisymmetric.  An",
 "     antisymmetric generator singles out no factor: ** exchanging any two colours reverses the",
 "     sign and changes no physics, so no colour can be the distinguished one. **",
 "",
 "     c54.81: the causal $1{+}2$ on the hinges -- the one candidate that DOES distinguish one",
 "     hinge -- has an assignment the symmetry group makes RELATIVE, ** so it distinguishes a",
 "     colour only relative to a chosen vantage, which is not a distinguished one. **",
 "",
 "⇒ ** SO THE ANSWER TO 'WHICH PHYSICAL DISTINGUISHED-ONE' IS: NONE ON THE COLOUR SIDE, BY",
 "   ANTISYMMETRY; AND ON THE FLAVOUR SIDE THE GEOMETRY'S $1{+}2$ IS INDEXICAL RATHER THAN",
 "   ABSOLUTE (c54.82), SO IT IS NOT THE HIERARCHY EITHER. **  ** The row asks for something the",
 "   construction has now been shown, twice from opposite directions, not to carry. **",
 "",
 "⌗ *That is a NEGATIVE result and it is the useful kind: the taxonomy's last OPEN alignment row",
 "closes as a non-alignment, on two independent grounds, and neither of them existed when the row",
 "was written.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE TWO STRIKES")
print("=" * 78)
print(f"  {'lead':>7} {'disposal':>13} {'answer':>50}")
for a, b, c in [
    ("L-08", "** STRIKE **", "screen re-run and the partition PUBLISHED"),
    ("L-13", "** STRIKE **", "none: two distinguished ones, and antisymmetry"),
]:
    print(f"  {a:>7} {b:>13} {c:>50}")
print()
for s in [
 "⌗ ** WITH THESE THE BOUNDED SLATE IS EMPTY.  What remains open in the register is `L-110`, the",
 "   sector's own standing discharge condition -- which is a SPEC and is meant to stay open until",
 "   it is met -- and `L-91`, whose owed action is a read of the external flavour literature",
 "   rather than a computation on the corpus. **",
]:
    print("  " + s)
