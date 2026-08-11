#!/usr/bin/env python3
"""
L-91x — THE FLAVOUR-LITERATURE READ, RUN. AND IT CONFIRMS THE LEAD'S "DIFFERENT PHYSICS" BY
NAMING WHAT THE DIFFERENCE IS.

`L-91`'s owed action: *"read the flavour literature's $\\mathbb{Z}_3$ models against what the deck
action supplies."*  Its claim: **the split predicts flavour carries $\\mathbb{Z}_3$, not $S_3$ —
and an $S_3$ and a $\\mathbb{Z}_3$ family symmetry are different physics.**

** THE LITERATURE'S OWN CRITERION IS SHARPER THAN THE LEAD EXPECTED AND CUTS THE OTHER WAY: a
CYCLIC group cannot organise generations into a multiplet at all, so the corpus's threeness is
not a horizontal flavour symmetry in the model-building sense.  IT IS A DECK SYMMETRY, AND THE
TWO ARE DIFFERENT KINDS OF OBJECT SHARING A NAME. **

  PART 1  The literature's criterion, and the group theory behind it.
  PART 2  ** WHAT THE CORPUS'S $\\mathbb{Z}_3$ IS, AND WHY IT CANNOT BE HORIZONTAL. **
  PART 3  ** THE SAME STRUCTURAL FACT ANSWERED `L-110` YESTERDAY, IN THE ISOSPIN SECTOR. **
  PART 4  What this costs the corpus, and what it protects it from.
  PART 5  `L-91` struck.

Run: python3 L091x_deck_symmetry_is_not_horizontal.py
"""
import itertools

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE LITERATURE'S CRITERION, AND THE GROUP THEORY BEHIND IT")
print("=" * 78)
for s in [
 "** Hagedorn, *Continuous and Discrete (Flavor) Symmetries*, stated flatly: **",
 '   *“The presence of more than one generation can only be explained with a non-abelian',
 '   symmetry which has two- and three-dimensional irreducible representations.”*',
 "",
 "*And the review literature's practice matches it: the $A_4$ models carry a family-INDEPENDENT",
 "$\\mathbb{Z}_3$ alongside the non-abelian group, where the $\\mathbb{Z}_3$ separates",
 "symmetry-breaking sectors and a Froggatt--Nielsen $U(1)$ shapes the hierarchy.* ** Abelian",
 "factors are AUXILIARY -- shaping and sector-separating; the non-abelian group is what carries",
 "the generational structure. **",
]:
    print("  " + s)
print()
print("  And the group-theoretic reason, which is elementary and is what makes the criterion hard:")
print()


def irrep_dims_abelian_check(mult, n, name):
    """Sum of squares of irrep dimensions = |G|; an abelian group has |G| one-dim irreps."""
    els = list(range(n))
    abelian = all(mult(a, b) == mult(b, a) for a in els for b in els)
    return abelian


GROUPS = []
# Z_3
GROUPS.append(("Z_3", 3, lambda a, b: (a + b) % 3, [1, 1, 1]))
# Z_2 x Z_2
pairs = [(i, j) for i in range(2) for j in range(2)]
idx = {p: k for k, p in enumerate(pairs)}
GROUPS.append(("Z_2 x Z_2", 4,
               lambda a, b: idx[((pairs[a][0]+pairs[b][0]) % 2, (pairs[a][1]+pairs[b][1]) % 2)],
               [1, 1, 1, 1]))
# S_3
S3 = list(itertools.permutations(range(3)))
s3i = {p: k for k, p in enumerate(S3)}
GROUPS.append(("S_3", 6, lambda a, b: s3i[tuple(S3[a][S3[b][i]] for i in range(3))], [1, 1, 2]))
# A_4
A4 = [p for p in itertools.permutations(range(4))
      if sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j]) % 2 == 0]
a4i = {p: k for k, p in enumerate(A4)}
GROUPS.append(("A_4", 12, lambda a, b: a4i[tuple(A4[a][A4[b][i]] for i in range(4))],
               [1, 1, 1, 3]))
print(f"  {'group':>12} {'order':>6} {'abelian?':>10} {'irrep dims':>16} "
      f"{'has a dim>1 irrep?':>19} {'can carry a generation multiplet?':>34}")
for name, n, mult, dims in GROUPS:
    ab = irrep_dims_abelian_check(mult, n, name)
    assert sum(d*d for d in dims) == n, name
    big = any(d > 1 for d in dims)
    assert ab == (not big), name          # abelian <=> every irrep is one-dimensional
    print(f"  {name:>12} {n:>6} {str(ab):>10} {str(dims):>16} {str(big):>19} "
          f"{str(big):>34}")
print()
for s in [
 "⇒ ** A FINITE GROUP IS ABELIAN IF AND ONLY IF EVERY IRREDUCIBLE REPRESENTATION IS",
 "   ONE-DIMENSIONAL, verified above on four groups against the order formula",
 "   $\\sum d_i^2 = |G|$. **  So a cyclic $\\mathbb{Z}_3$ has three one-dimensional irreps and",
 "   ** no multiplet into which three generations could be placed. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — SO THE CORPUS'S THREE IS NOT A HORIZONTAL SYMMETRY")
print("=" * 78)
DECKHDR = "the corpus's deck Z_3"
print(f"  {'':>34} {'a HORIZONTAL flavour symmetry':>34} {DECKHDR:>30}")
ROWS = [
 ("what it is", "a group acting on generation space", "the deck group of a covering"),
 ("the generations are", "components of ONE multiplet", "SHEETS of one cover"),
 ("what its breaking predicts", "mixing angles, mass ratios", "nothing -- it is not broken"),
 ("needs a dim>1 irrep?", "YES -- that is the criterion", "NO -- it has none to offer"),
 ("can be abelian?", "no", "** yes, and it is **"),
]
for a, b, c in ROWS:
    print(f"  {a:>34} {b:>34} {c:>30}")
print()
for s in [
 "⇒⇒ ** THE TWO ARE DIFFERENT KINDS OF OBJECT SHARING A NAME. **  *A horizontal symmetry organises",
 "   generations INTO a multiplet so that its breaking predicts the mixing; the corpus's",
 "   $\\mathbb{Z}_3$ says the three generations are **one object read three ways** -- identical in",
 "   content, distinguished by which sheet -- and predicts no mixing because it is not a symmetry",
 "   that gets broken.*",
 "",
 "⌗ ** AND THE CORPUS ALREADY SAYS SO WITHOUT SAYING IT THIS WAY: P14 delivers the COUNT, the",
 "   CHIRALITY and the relating symmetry, and explicitly does NOT deliver the mass spectrum. **",
 "   *The literature's criterion is about exactly the thing P14 declines to deliver, so the two",
 "   are not in competition -- but a reader coming from the flavour-model literature will read",
 "   'family $\\mathbb{Z}_3$' as a horizontal symmetry and object at once that it cannot work.*",
 "",
 "⇒ ** SO `L-91`'s PREDICTION IS CONFIRMED AND ITS FRAMING NEEDS ONE WORD: the split does predict",
 "   a CYCLIC three rather than an $S_3$, and that IS different physics -- but the difference is",
 "   not 'a different family symmetry'.  It is **not a family symmetry of that kind at all**. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND IT IS THE SAME FACT THAT ANSWERED `L-110`")
print("=" * 78)
print(f"  {'sector':>12} {'the group':>22} {'the consequence of one-dimensionality':>44}")
for a, b, c in [
    ("isospin", "S_3 x Z_2, deck-trivial part", "T acts by a scalar on each character, so it"),
    ("", "= four ONE-dim characters", "cannot act on one R-eigenspace and not the other"),
    ("flavour", "the deck Z_3, abelian", "no multiplet, so no horizontal symmetry and no"),
    ("", "= three ONE-dim characters", "mixing prediction"),
]:
    print(f"  {a:>12} {b:>22} {c:>44}")
print()
for s in [
 "⇒⇒ ** ONE STRUCTURAL FACT, TWO SECTORS, TWO REVISIONS APART -- AND IT IS THE SAME BOUND EACH",
 "   TIME: the discrete content this construction supplies is CHARACTERS, and characters are",
 "   one-dimensional, so they LABEL and do not MULTIPLET. **",
 "",
 "⌗ *Stated once and for the sector as a whole, that is the honest ceiling on what the discrete",
 "opening can deliver: exact selection rules, exact counts, exact gradings -- and no representation",
 "content in which mixing, coupling or mass could live.* ** Which is also, read the other way, why",
 "the things it DOES deliver are exact. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT IT COSTS, AND WHAT IT PROTECTS")
print("=" * 78)
for s in [
 "⚠ ** THE COST: the corpus cannot claim its threeness as a flavour symmetry in the sense the",
 "   flavour-model literature uses the term, and should not cite that literature as though it",
 "   were building in it. **  *P14 cites the standard review for 'the discrete flavour structure';",
 "   the citation is fine for what a discrete flavour structure IS and would be an overclaim if it",
 "   were read as placing this sector among horizontal-symmetry models.*",
 "",
 "✔ ** WHAT IT PROTECTS: the sector is not in the business those models are in, so their standing",
 "   difficulties are not its difficulties. **  *A horizontal model must break its group and get",
 "   the mixing right; this construction has nothing to break and predicts no mixing, so the",
 "   mixing data is neither evidence for it nor against it.*  ** That is a smaller claim and a",
 "   safer one, and it is the claim the corpus actually makes. **",
 "",
 "⌗ *And the falsifier moves with it: this sector is tested by the COUNT and the CHIRALITY and by",
 "the sixteen-fermion requirement, not by mixing angles.  ** A construction should be falsified by",
 "what it predicts and not by what a neighbouring programme predicts. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — `L-91` STRUCK")
print("=" * 78)
for s in [
 "✔ ** THE OWED ACTION IS RUN: the literature has been read against the deck action, and it",
 "   returns a criterion — *more than one generation can only be explained with a NON-ABELIAN",
 "   symmetry having two- and three-dimensional irreps* — which the corpus's cyclic three cannot",
 "   and need not meet. **",
 "",
 "⌗ ** THE LEAD'S TWO CLAUSES, DISPOSED: ** *the first — the transpositions belong to colour — was",
 "   confirmed by an independent route at c54.67. The second — flavour keeps only the 3-cycle —",
 "   was corrected there and is now COMPLETED: flavour keeps only the 3-cycle, and that makes it a",
 "   deck symmetry rather than a horizontal one.*",
 "",
 "⌗⌗ *`L-91` predicted the colour arc before any of it was computed, and its last clause turns out",
 "to predict a boundary on the sector rather than a feature of it.  ** Both are the same lead",
 "doing the same thing: reading what a split IMPLIES rather than what it resembles. ***",
]:
    print("  " + s)
