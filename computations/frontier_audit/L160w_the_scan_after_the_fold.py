#!/usr/bin/env python3
"""
L-160w — THE FIRST SWEEP OF FOLDED ITEMS THE SUPERSESSION SCAN PUT AT THE TOP, worked in one file
because they are one finding and three dispositions.

The fold (c54.90) put twenty-seven map items into the register, and the scan's first pass against
the corpus's receipts flagged six of them.  Read:

  `L-160` (map `J·8`)  CPT as the operator triple — *"likely SEMIDIRECT"*, its open half being
                       *"the semidirect seat⋊operator structure"*.
  `L-159` (map `J·7`)  the threes → SM via a geometric Higgs, *GATED on the fermion sector*.
  `L-161` (map `J·9`)  the exit-branch correspondence at the branch point.
  `L-142` (map `C·7`)  the A/B-generators ↔ ellipse-foci bridge.
  `L-136` (map `A2`)   beyond the wall.
  `L-154` (map `J·2`)  horizons as interaction vertices.

** THE HEADLINE IS `L-160`, AND IT IS DECIDABLE RATHER THAN SPECULATIVE: THERE IS NO SEMIDIRECT
OPTION.  Every semidirect product of the seat $S_3$ by an operator $\\mathbb{Z}_2$ IS the direct
product, because every automorphism of $S_3$ is inner.  The conjecture is not refuted by a fact
about this geometry; it is empty at the level of groups. **

  PART 1  ** `L-160`: the group theory, and there is nothing else the interlock could be. **
  PART 2  And the corpus's two operator $\\mathbb{Z}_2$s are both direct, with reasons.
  PART 2b ** AND THE SAME THEOREM DEFLATES A STANDING READING: the directness of
          $\\mathrm{Aut}(A_2)$ is FORCED, so it cannot be evidence for the marriage. **
  PART 3  ** `L-159`: its gate is LIFTED and a harder bound replaces it. **
  PART 4  `L-161`, and the one thing the corpus now has that it wants.
  PART 5  `L-142`, `L-136`, `L-154` — one amendment and two honest false positives.

Run: python3 L160w_the_scan_after_the_fold.py
"""
import itertools

print(__doc__.split("Run:")[0])

S3 = list(itertools.permutations(range(3)))
E = (0, 1, 2)


def mul(p, q):
    return tuple(p[q[i]] for i in range(3))


def inv(p):
    r = [0]*3
    for i, x in enumerate(p):
        r[x] = i
    return tuple(r)


# =====================================================================
print("=" * 78)
print("PART 1 — `L-160`: THERE IS NO SEMIDIRECT OPTION")
print("=" * 78)
for s in [
 "`J·8` sets the seat-threes (roots / pivots / families) against the operator-three (the discrete",
 "orientation $\\mathbb{Z}_2$s of $CPT$), proposes the interlock is ** \"likely SEMIDIRECT\" **, and",
 "carries as its open half *\"the semidirect seat⋊operator structure\"*.",
 "",
 "** THE QUESTION IS DECIDABLE WITHOUT ANY GEOMETRY, AND THE ANSWER IS THAT THE FORK DOES NOT",
 "EXIST. **  A semidirect product $S_3 \\rtimes_\\varphi \\mathbb{Z}_2$ is fixed by a homomorphism",
 "$\\varphi:\\mathbb{Z}_2\\to\\mathrm{Aut}(S_3)$; and ** every automorphism of $S_3$ is INNER **, so",
 "$\\varphi$ is conjugation by some $c\\in S_3$ with $c^2=e$.  Then",
 "",
 "        $\\Psi(s,a) = (s\\,c^{a},\\,a)$",
 "",
 "is an isomorphism onto the DIRECT product.  Computed rather than quoted:",
]:
    print("  " + s)
print()
cands = [p for p in S3 if mul(p, p) == E]


def semidirect(c):
    els = [(s, a) for s in S3 for a in (0, 1)]

    def m(x, y):
        s1, a = x
        s2, b = y
        ca = c if a == 1 else E
        return (mul(mul(mul(s1, ca), s2), inv(ca)), (a + b) % 2)
    return els, m


D_els = [(s, a) for s in S3 for a in (0, 1)]


def D_m(x, y):
    return (mul(x[0], y[0]), (x[1] + y[1]) % 2)


def orderstats(els, m):
    ident = (E, 0)
    out = {}
    for x in els:
        y = x
        k = 1
        while y != ident:
            y = m(y, x)
            k += 1
        out[k] = out.get(k, 0) + 1
    return tuple(sorted(out.items()))


ref = orderstats(D_els, D_m)
print(f"  the direct product $S_3\\times\\mathbb{{Z}}_2$, order statistics: {ref}")
print()
print(f"  {'c (the inner automorphism)':>28} {'order statistics':>34} {'Psi a homomorphism?':>21} "
      f"{'bijective?':>11}")
ok = True
for c in cands:
    els, m = semidirect(c)
    os_ = orderstats(els, m)

    def Psi(x, c=c):
        return (mul(x[0], c if x[1] == 1 else E), x[1])
    homo = all(Psi(m(x, y)) == D_m(Psi(x), Psi(y)) for x in els for y in els)
    bij = len({Psi(x) for x in els}) == len(els)
    ok &= (os_ == ref) and homo and bij
    print(f"  {str(c):>28} {str(os_):>34} {str(homo):>21} {str(bij):>11}")
assert ok and len(cands) == 4
print()
for s in [
 "⇒⇒ ** ALL FOUR CANDIDATE ACTIONS GIVE THE DIRECT PRODUCT, WITH THE ISOMORPHISM EXHIBITED AND",
 "   CHECKED ON EVERY PAIR.  SO `J·8`'s 'likely semidirect' is not a rival structure that the",
 "   geometry might or might not realise -- THERE IS NO OTHER GROUP FOR IT TO BE. **",
 "",
 "⌗ *That is a stronger disposal than a refutation and a cheaper one.  ** The clause was not wrong",
 "about this geometry; it was asking for a distinction that does not exist for these two",
 "factors. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND BOTH OF THE CORPUS'S OPERATOR Z_2s ARE DIRECT, WITH REASONS")
print("=" * 78)
print(f"  {'the operator Z_2':>26} {'how it sits':>30} {'the reason, and where':>34}")
for a, b, c in [
    ("R, the ruling swap", "INSIDE Aut(A_2) = S_3 x Z_2", "on/tangent are independent (L8.3)"),
    ("the charge Z_2", "ADJOINED, independent of it", "P3 sec:charge, 'rather than within'"),
]:
    print(f"  {a:>26} {b:>30} {c:>34}")
print()
for s in [
 "⌗ ** AND c54.93 SUPPLIED THE REASON THE SECOND ONE *MUST* BE ADJOINED RATHER THAN INTERNAL: the",
 "   involution exchanging $uud$ and $udd$ is AFFINE, $w\\mapsto\\tfrac13-w$, and $\\mathrm{Aut}(A_2)$",
 "   acts LINEARLY -- a map with a non-zero offset cannot lie in it. **  *So the adjunction is",
 "   forced, not stylistic, and the exchange exists only because of it.*",
 "",
 "⇒ ** TWO OPERATOR $\\mathbb{Z}_2$s, BOTH DIRECT, EACH WITH A STATED REASON -- AND A THEOREM",
 "   SAYING NO THIRD OPTION EXISTS FOR THE FIRST. **  *What `J·8` still carries is its other half:",
 "   whether substrate orientation auto-yields $CPT$ with $C$ closing.  That is untouched here.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2b — AND THE SAME THEOREM DEFLATES A STANDING READING, WHICH IS OWED")
print("=" * 78)
for s in [
 "** THE THEOREM OF PART 1 DOES NOT ONLY DISPOSE OF A GERM CLAUSE.  IT ALSO SAYS THAT",
 "   $\\mathrm{Aut}(A_2) = S_3 \\times \\mathbb{Z}_2$ BEING A *DIRECT* PRODUCT IS FORCED. **",
 "   $\\mathrm{Aut}$ of the $A_2$ root system is the Weyl group extended by the diagram",
 "   automorphism -- an $S_3$ and a $\\mathbb{Z}_2$ -- and by PART 1 no semidirect alternative",
 "   exists.  ** So the directness is a fact about $S_3$, not a fact about this substrate. **",
 "",
 "⚠ ** THAT IS OWED AGAINST `L8.3`'s MARRIAGE, WHICH PUTS WEIGHT ON THE DIRECTNESS: its own guard",
 "   reads *'its ENTIRE CONTENT is a DIRECT PRODUCT: two independent relations to one circle.'* **",
 "   *The group-level directness would have held whatever the two relations were, so it cannot be",
 "   evidence that they are independent.*",
 "",
 "✔ ** WHAT SURVIVES IS THE WHOLE OF WHAT THE MARRIAGE ACTUALLY SAYS, AND IT SURVIVES INTACT: WHICH",
 "   RELATION EACH FACTOR IS -- the three roots ON the circle against the two rulings TANGENT to",
 "   it -- AND THAT THE TWO DIFFER IN KIND, a ruling being a motion of the substrate (gauged) and",
 "   a root labelling a different cut (global). **  *Neither of those is a group fact, and neither",
 "   follows from the directness.*",
 "",
 "⇒ ** SO THE READING IS RIGHT AND ONE OF ITS STATED GROUNDS IS NOT LOAD-BEARING.  The correction",
 "   is to stop citing the directness as though it were evidence, and to cite the two relations",
 "   and the difference in kind, which are. **  *A reading that keeps a ground it does not need is",
 "   a reading that will be attacked at its weakest point rather than its strongest.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — `L-159`: THE GATE IS LIFTED AND A HARDER BOUND REPLACES IT")
print("=" * 78)
for s in [
 "`J·7`'s recorded verdict: *SPECULATIVE and bounded ... **GATED on the fermion sector (`A·5`)**",
 "and held strictly inside P14's bound.*",
 "",
 "✔ ** THE GATE IS LIFTED: `A·5` was rewritten at c54.63 and the fermion sector is BUILT. **",
 "⚠ ** AND WHAT REPLACES IT IS HARDER THAN THE GATE WAS. **  c54.91-92 establish the sector's",
 "   uniform ceiling: ** the discrete opening supplies CHARACTERS, and characters are",
 "   one-dimensional -- they LABEL and they do not MULTIPLET. **",
 "",
 "⇒ ** SO A GEOMETRIC HIGGS CANNOT COME FROM THE DISCRETE STRUCTURE, and the reason is not that",
 "   the fermion sector is unbuilt (it is built) but that the structure has no representation",
 "   content in which a mass could live. **  *`J·7`'s 'symmetry breaking = the bead conjugating",
 "   outward onto the real leg' would have to be a statement about the CONTINUOUS side -- the",
 "   flat bundle's missing curvature -- rather than about the threes.*",
 "",
 "⌗ *The item stays open as a germ, with its gate replaced by a bound: **it is not blocked on work",
 "the corpus has not done; it is bounded by work the corpus HAS done.** That is a better place for",
 "a speculative item to sit, and it is where the fold put it.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — `L-161`, AND THE ONE THING THE CORPUS NOW HAS THAT IT WANTS")
print("=" * 78)
for s in [
 "`J·9` proposes a NATURALNESS ordering on the conjugate lap's exits at the seam -- continue",
 "(parsimonious) / hop-dual (kink cost) / turn-back (rejected) -- as the seed of interaction",
 "branches with probabilities.  ** The scan matched it on 'branch / conjugate / rejected', and the",
 "match is a false positive on the words. **  *P14 rejects the conjugate branch $\\chi_-$ at the",
 "wall because it GROWS as $\\cosh^{+a}$ -- a normalizability rejection, not a naturalness one.*",
 "",
 "⌗⌗ ** BUT THERE IS A REAL POINTER UNDER THE FALSE POSITIVE, AND IT IS WORTH THE ROW. **  `J·9`",
 "   wants branch selection at $r=0$ decided by a weighting; ** the corpus now has exactly one",
 "   case where a branch choice at $r=0$ is settled by a COMPUTATION -- the zero mode's",
 "   normalizability -- and no case where one is settled by naturalness. **  *That is the template",
 "   the item should be held to: a selection rule earns its place by being forced, and the sector",
 "   has one worked example of what forcing looks like.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — `L-142`, `L-136`, `L-154`")
print("=" * 78)
print(f"  {'lead':>7} {'map':>6} {'disposal':>16} {'why':>44}")
for a, b, c, d in [
    ("L-142", "C·7", "** AMENDED **", "the ellipse side is banked TWICE, independently"),
    ("L-136", "A2", "false positive", "the prop:wall collision, fixed at c54.94"),
    ("L-154", "J·2", "false positive", "shared vocabulary, no shared content"),
]:
    print(f"  {a:>7} {b:>6} {c:>16} {d:>44}")
print()
for s in [
 "⌗ ** `L-142`: the item cites `bseries_C6_C7` for the ellipse side -- semi-axes $\\sqrt2$ and",
 "   $\\sqrt{2/3}$, foci at $\\pm2/\\sqrt3$ coinciding with the Nariai offset.  The scan put it",
 "   against `P03_ellipse_foci`, which reaches the same by eigenvalues $\\tfrac12,\\tfrac32$ and the",
 "   axis ratio $\\sqrt3$. **  *Two independent routes to one identity, and the item knew of one.*",
 "   ** The A/B-generator cross-plane identification is untouched and stays open: it is a P8-side",
 "   step and the ellipse side was never what was missing. **",
 "",
 "⌗ ** `L-136`'s hit is now fully explained and is the fold's own first catch: its text says 'by",
 "   **P11** prop:wall' and the scan matched **P14**'s prop:wall, two different propositions",
 "   wearing one label.  Renamed at c54.94, with a gate added. **  *The lead is untouched.*",
 "",
 "⚠ ** THREE OF SIX FLAGGED PAIRS WERE FALSE POSITIVES OR NEAR ONES, WHICH IS THE SCAN'S ADVERTISED",
 "   RATE AND SHOULD BE RECORDED AS SUCH. **  *It matches WORDS; leads and receipts about the same",
 "   objects share a vocabulary.  ** What it buys is an ordering of where to look, and on this pass",
 "   the ordering found a decidable germ clause, a lifted gate, a doubly-banked identity and a",
 "   label collision -- none of which any single-paper check could see. ***",
]:
    print("  " + s)
