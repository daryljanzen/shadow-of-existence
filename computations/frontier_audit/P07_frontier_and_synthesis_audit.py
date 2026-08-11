#!/usr/bin/env python3
"""
P7's FRONTIER SECTION, AUDITED — has it SHRUNK, and has what left it FED THE SYNTHESIS AT WEIGHT?

** THE ANSWER IS: IT HAS SHRUNK IN SUBSTANCE AND NOT ON THE PAGE; WHAT LEFT IT REACHED THE
SYNTHESIS IN TWO PLACES AND NOT IN THE THIRD; AND THE AUDIT TURNS UP A DEFECT OF THE SAME KIND
THE c54.60 SWEEP WAS RUN TO FIX, IN THE ONE PLACE THAT SWEEP DID NOT LOOK. **

  PART 1  The seven frontier items, each against what the corpus now holds.
  PART 2  ** THE WITHDRAWN IDENTIFICATION, STILL LIVE IN TWO PLACES -- and one of them is P14's
          OWN ABSTRACT, which contradicts the title of P14's own section. **
  PART 3  ** THE SYNTHESIS CARRIES THE PRE-ARC READING OF $\\su(3)$. **
  PART 4  A sentence in P14 that its own section answered twenty lines earlier.
  PART 5  What is owed, itemised, and in what order.

Run: python3 P07_frontier_and_synthesis_audit.py
"""
import os
import re

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))


def body(name):
    p = os.path.join(ROOT, 'corpus', name)
    return '\n'.join(l for l in open(p, encoding='utf-8', errors='replace').read().split('\n')
                     if not l.lstrip().startswith('%'))


P7 = body('CR_framework.tex')
P14 = body('matter_sector_paper.tex')
P3 = body('SdS-slicing-curve_v2.tex')

# =====================================================================
print("=" * 78)
print("PART 1 — THE SEVEN FRONTIER ITEMS, AGAINST WHAT THE CORPUS NOW HOLDS")
print("=" * 78)
ITEMS = [
    (1, "the matter branch-point crossing dynamics",
     "OPEN, and correctly", "well-posed, isotropising, scale-free, with a concrete "
     "matter model in P16; the worldline-and-field dynamics is genuinely unbuilt"),
    (2, "inherited boundary data, derived rather than measured",
     "OPEN, and correctly", "the composition half is met; the derivation of eta must reach a "
     "conserved charge, which is stated and not done"),
    (3, "the classification of causal reassignments",
     "** MOSTLY DISCHARGED **", "the reducible sector is settled IN THE SYNTHESIS "
     "(sec:general-reach); only the irreducible interior remainder is left, gated on matter"),
    (4, "the scalar perturbation sector, to a verdict",
     "** MOSTLY DISCHARGED **", "the transfer is run; what remains is a parameter refit and "
     "the odd/even height pattern, which is ordinary content physics"),
    (5, "the Standard-Model fermion and gauge sector",
     "** SUBSTANTIALLY DISCHARGED AND THE ITEM DOES NOT SAY SO **",
     "the item still calls a propagating fermion sector 'the framework's largest unbuilt "
     "undertaking' and says the gauge content 'stays the ordinary route'"),
    (6, "the quantum sector: the interacting theory's definition",
     "OPEN, and correctly", "the ambiguity is closed without a free parameter; the interacting "
     "tower's definition is the same wall any interacting QFT meets"),
    (7, "the structure of the lap and the physics of the lift",
     "** RESOLVED, AND STILL LISTED AS A FRONTIER **",
     "the item marks itself 'resolved; see sec:lift-initial-rate' in its own title"),
]
print(f"  {'#':>2} {'item':>46} {'status':>46}")
for n, name, status, why in ITEMS:
    print(f"  {n:>2} {name:>46} {status:>46}")
print()
for n, name, status, why in ITEMS:
    if status.startswith('**'):
        print(f"   ⌗ item {n}: {why}")
print()
open_correct = sum(1 for _, _, s, _ in ITEMS if not s.startswith('**'))
print(f"  ** {open_correct} of 7 items are open and correctly so; {7-open_correct} have moved and "
      f"the section does not fully register the movement. **")
assert open_correct == 3
print()
for s in [
 "⌗⌗ ** SO THE FRONTIER HAS SHRUNK IN SUBSTANCE AND NOT ON THE PAGE. **  *Items 3 and 4 say",
 "   inside themselves that most of their content is settled; item 7 says in its own title that",
 "   it is resolved; item 5 has been overtaken twice over.* ** A frontier list is a promise about",
 "   where the work is, and a list that grows text while its items empty is a list a reader can",
 "   no longer use to choose what to work. **",
 "",
 "⌗ *And the one thing the section does right and should keep doing: item 7 was not DELETED when",
 "it resolved, it was marked resolved in place with a pointer to where the answer went.  ** That",
 "is the correct treatment and the argument below is that it should now finish -- a resolved item",
 "belongs in the record of what closed, not in the map of where to go next. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE WITHDRAWN IDENTIFICATION, STILL LIVE IN TWO PLACES")
print("=" * 78)
WITHDRAWN = [
    (r'three generations one object read three ways',
     'generations = the three hinges'),
    (r'the generations are \\emph\{one object read three ways\}',
     'generations = the three hinges'),
    (r'which wall each binds at', 'generations = the three walls'),
]
# a revision marker within this many characters AFTER the hit counts as adjacent
MARKER = re.compile(r'(has since been revised|withdraw|follows the revision|not the hinges|'
                    r'within-state|turnaround\'s deck)', re.I)
WINDOW = 900
print(f"  {'paper':>26} {'hits':>6} {'with an adjacent revision marker':>34}")
findings = []
for nm, txt in (('CR_framework (P7)', P7), ('matter_sector_paper (P14)', P14),
                ('SdS-slicing-curve (P3)', P3)):
    hits = 0
    bare = 0
    for pat, what in WITHDRAWN:
        for m in re.finditer(pat, txt, re.I):
            hits += 1
            if not MARKER.search(txt[m.end():m.end() + WINDOW]):
                bare += 1
                findings.append((nm, what, m.start()))
    print(f"  {nm:>26} {hits:>6} {hits - bare:>34}")
print()
print(f"  ** OCCURRENCES WITH NO REVISION MARKER WITHIN {WINDOW} CHARACTERS AFTER: "
      f"{len(findings)} **")
for nm, what, pos in findings:
    print(f"     {nm:>26}   ({what})")
assert findings, "the audit's own premise: this scan must find the two known cases"
print()
absidx = P14.find(r'\begin{abstract}')
absend = P14.find(r'\end{abstract}')
in_abstract = [f for f in findings if 'P14' in f[0] and absidx < f[2] < absend]
print(f"  ⚠⚠ ** AND {len(in_abstract)} OF THEM IS IN P14's ABSTRACT. **")
sec = re.search(r'\\subsection\{([^}]*)\}\\label\{sec:whichthree\}', P14)
print(f"     P14's own section is titled: \"{sec.group(1)}\"")
assert in_abstract and sec
print()
for s in [
 "⇒⇒ ** P14's ABSTRACT ASSERTS THE IDENTIFICATION P14's OWN SECTION IS TITLED AFTER DENYING. **",
 "   *The c54.31 revision seated the generations on the turnaround's deck $\\mathbb{Z}_3$ and made",
 "   the walls' $S_3$ a within-state index; the c54.60 sweep propagated that to five companion",
 "   papers.* ** It did not look at the abstract of the paper that made the revision. **",
 "",
 "⇒ ** AND P7's FRONTIER ITEM 5 DOES BOTH IN ONE PARAGRAPH: it states the revision -- 'which",
 "   three that is the matter sector has since revised' -- and then, three sentences later,",
 "   restates the withdrawn reading as current. **  *That is worse than missing the propagation:",
 "   the correction and the error are adjacent, so the paragraph contradicts itself.*",
 "",
 "⌗ *P3 carries the phrase twice and follows each with 'this paper follows the revision'.  ** The",
 "scan's marker test is what tells the three apart, and it is the test a gate should run. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE SYNTHESIS CARRIES THE PRE-ARC READING OF su(3)")
print("=" * 78)
m = re.search(r'And the internal gauge algebra[^.]*\.', P7)
print("  P7 sec:unification-scope, as it stands:")
print(f"     \"{m.group(0)[:300]}...\"")
print()
compact_only = ('compact face' in m.group(0)) and ('monodrom' not in m.group(0))
print(f"  names the compact-face route only?  ** {compact_only} **")
assert compact_only
print()
for s in [
 "⚠ ** THAT WAS THE CORPUS'S ONLY $\\su(3)$ ROUTE UNTIL c54.42, AND IT IS NO LONGER. **  The",
 "   colour arc reaches $SU(3)$ on the LORENTZIAN side and by a different mechanism entirely:",
 "     ① every ambient candidate bundle is REAL, and a real bundle's complexified holonomy lands",
 "        in the real form -- so no ambient bundle can carry $\\su(3)$ and the module is the",
 "        BRANCHING itself;",
 "     ② the wall is a wall OF A HINGE, so there are three signed radii and three wall",
 "        monodromies rather than one, and the monodromy is non-abelian;",
 "     ③ the smallest connected group containing the three wall monodromies and the hinge",
 "        3-cycle is $SU(3)$, with the lap as its centre;",
 "     ④ second quantisation on the wall kernel returns baryon 1, diquark 0, meson 1 and",
 "        SELECTS the configuration group uniquely.",
 "",
 "⇒⇒ ** SO THE SYNTHESIS'S THIRD CLAUSE IS NOT WRONG BUT IS NOW ONE OF TWO ROUTES, AND IT NAMES",
 "   THE WEAKER ONE. **  *The compact-face statement says where a continuous $\\su(3)$ could live;",
 "   the arc says what the discrete structure ENTAILS, on the real Lorentzian substrate, without",
 "   any isometry at all.*",
 "",
 "⌗ ** AND THE SYNTHESIS MUST ALSO CARRY WHAT THE ARC DOES NOT GIVE, or it will overclaim: the",
 "   bundle is FLAT.  No curvature, no coupling, no force.  The geometry quantises and does not",
 "   couple, and that is walled three independent ways. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — A SENTENCE P14 ANSWERS TWENTY LINES EARLIER")
print("=" * 78)
i_arc = P14.find('smallest connected group containing the three wall monodromies')
i_open = P14.find('the bundle question is left open')
print(f"  position of the arc's conclusion (smallest connected group ... is SU(3)):  {i_arc}")
print(f"  position of 'the bundle question is left open':                            {i_open}")
print(f"  ** the second comes AFTER the first: {i_open > i_arc} **")
assert i_arc > 0 and i_open > i_arc
print()
for s in [
 "⚠ ** THE SENTENCE READS: *'the source is closed by exhaustion and not by inspection, and the",
 "   bundle question is left open, which is the honest description of where this sector stands'*",
 "   -- and it sits after the section that answers the bundle question. **",
 "",
 "⌗ ** IT IS NOT SIMPLY STALE: TWO DIFFERENT QUESTIONS ARE BEING CALLED 'THE BUNDLE QUESTION'. **",
 "     (a) *which ambient bundle carries colour* -- ANSWERED: none, and the module is the",
 "         branching;",
 "     (b) *what supplies the TOWER's multiplicity* -- genuinely open, and the paragraph's real",
 "         subject.",
 "   ** The defect is the clause 'which is the honest description of where this sector stands',",
 "   which promotes (b) to a verdict on the whole sector. **  *The fix is to name which question,",
 "   not to delete the sentence.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT IS OWED, IN ORDER")
print("=" * 78)
OWED = [
 ("①", "P14's ABSTRACT", "carries the withdrawn identification; the paper's own section is "
  "titled after denying it", "highest -- a paper contradicting itself in its front matter"),
 ("②", "P7 frontier item 5", "states the revision and then restates the withdrawn reading; and "
  "calls a built sector 'the largest unbuilt undertaking'", "high"),
 ("③", "P7 sec:unification-scope", "names the compact-face route for su(3) only, and does not "
  "carry the flatness bound", "high -- it is the paper's summary claim"),
 ("④", "P14's 'bundle question is left open'", "name which question", "medium"),
 ("⑤", "P7 frontier item 7", "resolved in its own title; belongs in the record of what closed",
  "medium -- a hygiene move, not a correction"),
 ("⑥", "a GATE for withdrawn claims", "the marker test of PART 2, run corpus-wide",
  "the reason this recurred"),
]
print(f"  {'':>3} {'where':>34} {'weight':>52}")
for tag, where, what, weight in OWED:
    print(f"  {tag:>3} {where:>34} {weight:>52}")
    print(f"      {what}")
print()
for s in [
 "⌗⌗ ** THE PATTERN ACROSS ①, ② AND ③ IS ONE PATTERN: A RESULT LANDED IN THE SECTION THAT",
 "   PRODUCED IT AND DID NOT REACH THE PLACES THAT SUMMARISE. **  *Abstracts, frontier lists and",
 "   synthesis sections are exactly the places a reader goes FIRST and exactly the places a",
 "   working node edits LAST.*  ** The c54.60 sweep fixed five bodies and no summaries. **",
 "",
 "⇒ ** WHICH IS WHY ⑥ IS ON THE LIST AND IS THE ONLY ITEM THAT PREVENTS A THIRD OCCURRENCE. **",
]:
    print("  " + s)
