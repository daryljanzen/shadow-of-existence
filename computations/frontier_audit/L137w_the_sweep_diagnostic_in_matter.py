#!/usr/bin/env python3
"""
L-137w — `A·3`, "THE SWEEP DIAGNOSTIC IN NON-VACUUM".  ITS ANSWER IS A COROLLARY IN P9's BODY, STATED
AS A THEOREM AND PROVED, AND THE ITEM'S OWN TEXT IS STALE IN BOTH OF ITS TWO FACTUAL CLAIMS.

`A·3`: *"What 'apparent-dynamics-is-the-shadow-of-the-sweep' becomes once matter is present.
(P4 abstract close.)  [reading: rides on `A·1` (now BUILT, r565) -- gate cleared, ready.]"*

** THE ANSWER: the sweep reading survives matter EXACTLY as far as matter carries a continuous
symmetry to anchor a sweep, and fails EXACTLY at inhomogeneity -- which is the wall.  P9's
`cor:wall` is that statement: *"A geometry with no Killing symmetry is precisely one whose matter is
genuinely inhomogeneous.  The boundary of the range and the emergence of dynamical (inhomogeneous)
matter are therefore one statement read two ways."*  There is no separate non-vacuum diagnostic to
build; the diagnostic's DOMAIN in non-vacuum is the range, and the range's boundary is the wall. **

  PART 1  ** THE TWO FACTUAL CLAIMS IN THE ITEM'S OWN TEXT, BOTH CHECKED AND BOTH STALE. **
  PART 2  ** WHERE THE ANSWER LIVES: `cor:wall` and `cor:radiation`, in P9's body. **
  PART 3  Why this is a disposal and not a dissolution -- what the answer costs and what it buys.
  PART 4  ** `L-137` STRUCK, residue to `L-136`. **

Run: python3 L137w_the_sweep_diagnostic_in_matter.py
"""
import os
import re

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))


def body(name):
    t = open(os.path.join(ROOT, 'corpus', name), encoding='utf-8', errors='replace').read()
    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
    return t.split(r'\begin{thebibliography}')[0]


P9 = body('range_paper.tex')
P4 = body('modern_parallax.tex')
MAP = open(os.path.join(ROOT, 'OPEN_PROBLEMS_MAP.md'), encoding='utf-8').read()

# =====================================================================
print("=" * 78)
print("PART 1 — THE ITEM'S TWO FACTUAL CLAIMS, CHECKED")
print("=" * 78)
n_sweep_p4 = len(re.findall(r'sweep', P4, re.I))
print(f"  ① the item cites its home as ** (P4 abstract close) **")
print(f"     occurrences of 'sweep' anywhere in P4 `modern_parallax`: ** {n_sweep_p4} **")
assert n_sweep_p4 == 0
print(f"     ⇒ ** THE HOME IS WRONG.  P4 is the empirical-forcing paper and does not use the word. **")
print()
a1 = re.search(r'- \*\*`?A·1`?[^\n]*', MAP)
built = 'ADVANCED, NOT resolved' in (a1.group(0) if a1 else '')
print(f"  ② the item's reading says ** 'rides on A·1 (now BUILT, r565)' **")
print(f"     the map's own `A·1` row says 'ADVANCED, NOT resolved': ** {built} **")
assert built
print(f"     ⇒ ** THE GATE IT REPORTS CLEARED WAS NEVER CLEARED. **  A·1's general matter dynamics")
print(f"        is *characterized but not crossed*; only the confined/reducible case is built.")
print()
for s in [
 "⌗ ** TWO FACTUAL CLAIMS, BOTH WRONG, IN AN ITEM OF THREE SENTENCES -- and neither was load-bearing",
 "   for the answer, which is the useful part. **  *A row can be wrong about where it lives and",
 "   wrong about what it waits on and still be a real question; what the fold gave the map was a",
 "   place where those two things get CHECKED rather than carried.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHERE THE ANSWER LIVES")
print("=" * 78)
CHECKS = [
 ("P9 states the wall as a labelled corollary",
  r'\\begin\{corollary\}\[The wall is inhomogeneity\]\\label\{cor:wall\}'),
 ("...and it is about MATTER, not only geometry",
  r'A geometry with no Killing symmetry is precisely one whose matter is genuinely\s+inhomogeneous'),
 ("...and it says the two boundaries are ONE statement",
  r'The boundary of the range and the emergence of dynamical \(inhomogeneous\)\s+matter are therefore one statement read two ways'),
 ("P9 states the geometry-side face as a second corollary",
  r'\\begin\{corollary\}\[The wall is free gravitational radiation\]\\label\{cor:radiation\}'),
 ("...with the sweep named as what fails there",
  r'admits no sweep-subgroup of \$?\\so\$? to anchor the construction; the operator has nothing to grip'),
 ("...and the mechanism given, not asserted",
  r'a sweep generates a deformation of \\emph\{fixed\} orientation'),
]
print(f"  {'check':>62} {'':>10}")
for what, pat in CHECKS:
    hit = bool(re.search(pat, P9))
    print(f"  {what:>62} {('** yes **' if hit else 'NO'):>10}")
    assert hit, what
print()
for s in [
 "⇒⇒ ** SO THE NON-VACUUM QUESTION IS ANSWERED IN THE FORM A QUESTION LIKE THIS CAN BE ANSWERED: not",
 "   by a second diagnostic for the matter case, but by the DOMAIN of the one diagnostic. **",
 "",
 "   *The sweep reading holds wherever a sweep can be anchored.  Matter does not weaken that: what",
 "   weakens it is the loss of the last continuous isometry, and a geometry with no Killing symmetry",
 "   is exactly one whose matter is genuinely inhomogeneous.*  ** So 'the sweep diagnostic in",
 "   non-vacuum' has the range for its domain and the wall for its boundary, and the question",
 "   'what does it become once matter is present' has the answer 'the same thing, for as long as",
 "   the matter carries a symmetry, and nothing at all past that'. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT THE ANSWER COSTS AND WHAT IT BUYS")
print("=" * 78)
for s in [
 "⚠ ** IT COSTS SOMETHING AND THE STRIKE SHOULD SAY SO. **  *A reader hoping that the perspectival",
 "   reading of apparent dynamics would extend to matter generally does not get that.  It extends",
 "   to the symmetry-reducible sector and stops, and the stopping is sharp rather than gradual --",
 "   `cor:radiation` gives the mechanism: a sweep generates a deformation of FIXED orientation, so a",
 "   confined wave stays self-consistent only while it propagates transverse to that orientation,",
 "   and the last confining isometry's loss is exactly where the polarization must reorient from",
 "   place to place.*",
 "",
 "✔ ** AND IT BUYS THE THING THE CORPUS ACTUALLY WANTS, which is a boundary with a positive",
 "   identity on both sides. **  *Not 'the reading fails somewhere out there' but: it fails exactly",
 "   at the onset of free gravitational radiation, read from the geometry side, and exactly at the",
 "   onset of genuinely inhomogeneous matter, read from the matter side -- and those are one",
 "   surface.*  ** A diagnostic whose failure locus is a named theorem is in better shape than one",
 "   whose domain was never asked about. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — `L-137` STRUCK")
print("=" * 78)
for s in [
 "✔ ** THE QUESTION: answered by `cor:wall` and `cor:radiation`, in P9's body, as labelled",
 "   corollaries with a mechanism rather than as remarks. **",
 "⌗ ** THE ITEM'S HOME AND ITS GATE: both stale, and both corrected in the strike. **",
 "⇒ ** THE RESIDUE -- what the apparent dynamics IS past the wall, where the sweep no longer",
 "   grips -- is `A2` = `L-136`, registered and open, and it is the same residue `C·3` was sent to",
 "   at c54.100. **  *Two items now converge on that row, which is a fact about the row and worth",
 "   its weight: `L-136` is where the matter sector's remaining conceptual debt has collected.*",
 "",
 "⚠ *A strike here means the item's question is answered, not that the physics past the wall is.*",
]:
    print("  " + s)
