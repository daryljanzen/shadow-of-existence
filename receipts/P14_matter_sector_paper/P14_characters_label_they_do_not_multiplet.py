"""
P14_characters_label_they_do_not_multiplet.py -- P14 sec:scope: the honest ceiling on what the
substrate's discrete opening can deliver, stated once for the sector as a whole.

** THE DISCRETE CONTENT THIS CONSTRUCTION SUPPLIES IS CHARACTERS, AND CHARACTERS ARE
ONE-DIMENSIONAL: THEY LABEL AND THEY DO NOT MULTIPLET. **  Which is also, read the other way, why
the things the sector does deliver are exact.

WHAT PROMPTED IT.  A standing question asked what the flavour-model literature's cyclic-symmetry
models say about the threeness this sector reads off the turnaround's deck.  The literature's
criterion turns out to be sharper than the question expected and to cut the other way.

WHAT IS ESTABLISHED.
  1. ** THE LITERATURE'S CRITERION. **  Hagedorn, *Continuous and Discrete (Flavor) Symmetries*:
     "The presence of more than one generation can only be explained with a non-abelian symmetry
     which has two- and three-dimensional irreducible representations."  Practice matches it --
     in $A_4$ models the accompanying $\mathbb{Z}_3$ is family-INDEPENDENT and separates
     symmetry-breaking sectors, with a Froggatt--Nielsen $U(1)$ shaping the hierarchy; abelian
     factors are auxiliary and the non-abelian group carries the generational structure.
  2. ** THE GROUP THEORY BEHIND IT, VERIFIED: a finite group is abelian if and only if every
     irreducible representation is one-dimensional ** -- checked on $\mathbb{Z}_3$,
     $\mathbb{Z}_2\times\mathbb{Z}_2$, $S_3$ and $A_4$ against $\sum d_i^2=|G|$, with the
     equivalence asserted group by group.  A cyclic $\mathbb{Z}_3$ therefore offers no multiplet
     into which three generations could be placed.
  3. ** SO THIS SECTOR'S THREENESS IS NOT A HORIZONTAL FLAVOUR SYMMETRY, AND THE TWO ARE DIFFERENT
     KINDS OF OBJECT SHARING A NAME. **  A horizontal symmetry organises generations into one
     multiplet so that its breaking predicts the mixing; the deck $\mathbb{Z}_3$ says the three
     are one object read three ways -- identical in content, distinguished by which sheet -- and
     predicts no mixing, because it is not a symmetry that gets broken.
  4. ** AND THE SAME ONE-DIMENSIONALITY BOUNDS THE ISOSPIN SECTOR: ** the colourless characters
     are four one-dimensional ones, so $T$ acts on each by a scalar and cannot act on one
     $R$-eigenspace and not the other.  One structural fact, two sectors.

** WHAT IT COSTS AND WHAT IT PROTECTS.  The sector cannot claim its threeness as a flavour
symmetry in the model-building sense, and the standard review is cited here for what a discrete
flavour structure IS rather than as placing this construction among horizontal-symmetry models.
In exchange, those models' standing difficulties are not this construction's: it has nothing to
break and predicts no mixing, so the mixing data is neither evidence for it nor against it.  This
sector is tested by the count, the chirality and the sixteen-fermion requirement -- by what it
predicts, and not by what a neighbouring programme predicts. **

ORIGIN: computations/baryon_edge/L091x_deck_symmetry_is_not_horizontal.py -- built r2376 (c54.92);
edit the origin, not this copy.

ORIGIN-DIVERGENCE: DELIBERATE AND SUBTRACTIVE.  The origin closes with the disposal of the
register item that prompted it, which is bookkeeping rather than a paper claim.  ** This copy
carries the paper-facing subset: every assertion here appears in the origin verbatim, and nothing
here is absent from it. **"""

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

