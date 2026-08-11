#!/usr/bin/env python3
"""
L-143w — `C·8` CALLS ITS OWN QUESTION UNANSWERABLE FOR WANT OF A MAP. IT IS ANSWERABLE FROM THE
EMBEDDING, BY A DIMENSION COUNT, AND THE RECONCILIATION IT WANTED WAS BANKED SEPARATELY.

`C·8`, promoted at c54.40 from *pedagogical* to **load-bearing**, turns on one sentence:

    *"Whether that $SO(3)$ is the areal 2-sphere's rotation group would reconcile the seat count
    with `L-107`'s infinite tower (seats = invariant sector, tower = the rest) — and it is
    **UNANSWERABLE at present, because the map $\\mathrm{dS}_5\\to$ SdS is asserted three times and
    written nowhere.**"*

** BOTH HALVES ARE ANSWERED.  The $SO(3)$ question needs no map -- both groups are subgroups of
the embedding's own isometry group and their DIMENSIONS differ, so the answer is NO by counting.
And the reconciliation it hoped that answer would buy was obtained by a different route at
c54.42 and landed in P14 at c54.87. **

  PART 1  The objects, from the embedding alone.
  PART 2  ** THE DIMENSION COUNT, AND WHY NO MAP IS NEEDED. **
  PART 3  ** WHAT THE TRANSVERSE $SO(3)$ ACTUALLY IS: an isotropy subgroup. **
  PART 4  The reconciliation `C·8` wanted, obtained elsewhere and already landed.
  PART 5  `L-143` struck, and the promotion reversed with its reason.

Run: python3 L143w_the_transverse_so3_is_an_isotropy.py
"""
import os
import re

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))


def so_dim(n):
    return n*(n-1)//2


# =====================================================================
print("=" * 78)
print("PART 1 — THE OBJECTS, FROM THE EMBEDDING ALONE")
print("=" * 78)
print("  The substrate:   -X_0^2 + X_1^2 + ... + X_5^2 = alpha^2   in R^{5,1}   -- dS_5, dim 5")
print("  The equatorial section:  -X_0^2 + X_1^2 + X_2^2 = alpha^2,  X_3 = X_4 = X_5 = 0")
print()
print(f"  {'object':>36} {'what it is':>26} {'dim':>5}")
ROWS = [
    ("the substrate", "dS_5", 5),
    ("the equatorial section", "** dS_2 **", 2),
    ("its normal bundle in the substrate", "rank 3, on (X_3,X_4,X_5)", 3),
    ("the static patch's areal sphere", "** S^3 **, on (X_2..X_5)", 3),
]
for a, b, c in ROWS:
    print(f"  {a:>36} {b:>26} {c:>5}")
assert 5 - 2 == 3
print()
for s in [
 "⌗ *The section is cut by setting THREE coordinates to zero in a five-dimensional hypersurface,",
 "so it is two-dimensional and its normal bundle has rank three -- which is the corpus's own",
 "'rank-3 normal bundle', arrived at here by subtraction rather than assertion.*",
 "",
 "⌗ ** AND THE AREAL SPHERE OF $\\mathrm{dS}_5$'s STATIC PATCH IS $S^3$, NOT $S^2$: the patch is",
 "   $-f\\,dt^2 + dr^2/f + r^2 d\\Omega_3^2$ with $f = 1-r^2/\\alpha^2$, five dimensions being one",
 "   time, one radius and a THREE-sphere. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE DIMENSION COUNT, AND WHY NO MAP IS NEEDED")
print("=" * 78)
print(f"  {'group':>34} {'acts on':>26} {'dimension':>10}")
for a, b, n in [("the TRANSVERSE SO(3)", "(X_3, X_4, X_5)", so_dim(3)),
                ("the AREAL sphere's rotation group", "S^3, i.e. (X_2..X_5)", so_dim(4))]:
    print(f"  {a:>34} {b:>26} {n:>10}")
print()
print(f"  ** dim SO(3) = {so_dim(3)} and dim SO(4) = {so_dim(4)}: {so_dim(3)} != {so_dim(4)}, "
      f"so they are not the same group. **")
assert so_dim(3) == 3 and so_dim(4) == 6 and so_dim(3) != so_dim(4)
print()
for s in [
 "⇒⇒ ** SO `C·8`'s QUESTION IS ANSWERED *NO*, AND THE ANSWER NEEDS NO MAP $\\mathrm{dS}_5\\to$ SdS.**",
 "   *Both groups are subgroups of the embedding's own isometry group, defined by which",
 "   coordinates they move; their dimensions are read off the embedding and differ.*",
 "",
 "⚠ ** THE ITEM'S PREMISE -- 'UNANSWERABLE at present' -- IS THEREFORE FALSE, and it is worth",
 "   saying why the premise looked true: the item asked the question in terms of the areal",
 "   2-SPHERE, and the substrate's areal sphere is a 3-sphere. **  *A question posed about the",
 "   wrong-dimensional object looks to need more structure than it does.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT THE TRANSVERSE SO(3) ACTUALLY IS")
print("=" * 78)
for s in [
 "The section retains $X_2$ and kills $X_3,X_4,X_5$.  On the areal $S^3$ spanned by",
 "$(X_2,X_3,X_4,X_5)$ that is a choice of POLE -- the direction $X_2$ -- and the subgroup of",
 "$SO(4)$ fixing a vector is $SO(3)$.",
 "",
 "⇒ ** THE TRANSVERSE $SO(3)$ IS THE ISOTROPY SUBGROUP OF THE AREAL SPHERE'S ROTATION GROUP AT",
 "   THE POLE THE SECTION SELECTS. **  *Not the rotation group; the stabiliser of a point in it.*",
 f"   $\\dim SO(4) - \\dim SO(3) = {so_dim(4)} - {so_dim(3)} = {so_dim(4)-so_dim(3)}$, which is"
 " $\\dim S^3$ --",
 "   the orbit-stabiliser count, and it closes.",
]:
    print("  " + s)
assert so_dim(4) - so_dim(3) == 3
print()
for s in [
 "⌗ ** AND THAT IS A BETTER ANSWER THAN THE ONE THE ITEM HOPED FOR, because it says WHY the",
 "   section is totally geodesic without appealing to anything: it is the fixed-point set of a",
 "   subgroup of isometries, and a fixed-point set of isometries is always totally geodesic. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE RECONCILIATION IT WANTED, OBTAINED ELSEWHERE")
print("=" * 78)
idx = open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read()
have = 'P14_tower_is_not_kaluza_klein' in idx
p14 = '\n'.join(l for l in open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                               encoding='utf-8', errors='replace').read().split('\n')
                if not l.lstrip().startswith('%'))
cited = 'P14_tower_is_not_kaluza_klein' in p14
print(f"  the receipt is registered:            ** {have} **")
print(f"  and cited in the paper (landed c54.87): ** {cited} **")
assert have and cited
print()
for s in [
 "*`C·8` wanted the $SO(3)$ answer in order to reconcile the seat count with the infinite tower --",
 "'seats = invariant sector, tower = the rest'.*  ** THAT RECONCILIATION EXISTS AND IS SHARPER: **",
 "",
 "   ① the tower is the ORDINARY ANGULAR DECOMPOSITION of a four-dimensional field, $\\lambda$",
 "     indexing partial waves on the transverse $S^2$ -- not a Kaluza--Klein tower, there being",
 "     no internal space to reduce on, and $2+2=4$ exhausting the cut;",
 "   ② and the RANK-3 NORMAL BUNDLE IS NOT A THIRD THREE: it splits $2+1$, the two being that",
 "     transverse $S^2$ and the one the CUT-NORMAL, the direction $R$ acts along.",
 "",
 "⇒ ** SO THE SEATS AND THE TOWER ARE ALREADY SEPARATED, AND BY THE SPLIT OF THE NORMAL BUNDLE",
 "   RATHER THAN BY AN IDENTIFICATION OF GROUPS. **  *The item's route was not the only one and",
 "   was not taken; the destination was reached at c54.42 and landed in the paper at c54.87.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — `L-143` STRUCK, AND THE PROMOTION REVERSED WITH ITS REASON")
print("=" * 78)
for s in [
 "✔ ** THE $SO(3)$ QUESTION: answered NO, from the embedding, by a dimension count. **",
 "✔ ** THE RECONCILIATION: obtained at c54.42 by the normal bundle's $2+1$ split and landed at",
 "   c54.87. **",
 "⇒ ** SO THE c54.40 PROMOTION FROM *pedagogical* TO *load-bearing* IS REVERSED, and its own",
 "   stated ground is what reverses it: the promotion rested on the question being unanswerable",
 "   without an explicit embedding map, and it is answerable without one. **",
 "",
 "⌗ ** WHAT REMAINS OF `C·8` IS ITS ORIGINAL CONTENT -- draw the bent transit in the embedding",
 "   coordinates -- AT ITS ORIGINAL WEIGHT, which the item itself records: *'the framework",
 "   paper's analysis largely dissolves the NEED for it … its value would be pedagogical.'* **",
 "",
 "⚠ *And one thing the item was right about and stays right about: **the map $\\mathrm{dS}_5\\to$",
 "SdS is asserted and not written**, and the only place it is written is a retired note whose",
 "transverse triple disagrees with the natural one.  ** That is a real gap in the corpus's",
 "exposition.  It is not what made this item load-bearing, and it should not be lost when the",
 "item is struck -- so it is stated here and carried in the strike. ***",
]:
    print("  " + s)
