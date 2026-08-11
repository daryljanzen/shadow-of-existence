#!/usr/bin/env python3
"""
L-45w — THE FOUR LEADS THE SCAN LEFT AT THE TOP, worked as one file because they are two pairs:
two on the two $2{+}1$ splits, two on the hinge-end trichotomy.

  `L-45`  the geometry/vantage division INSIDE a single triple -- is it `L8.3`'s marriage one
          level down?
  `L-47`  at the DEGENERATE member the two $2{+}1$s meet.  Is it a bridge between them?
  `L-55`  what IS a null chord between two hinge-ends, physically -- and all three causal
          characters want reading, not just the null one.
  `L-56`  the triangle is a shadow in which the two rulings coincide.  Does anything else in the
          corpus read it as a shadow with a two-fold cover upstairs?
  `L-11`  is the own-wall $1{+}2$ the designation split read on the hinges, a third structure, or
          the sign split in disguise?

** ALL FOUR STRIKE, AND SO DOES `L-11`, WHICH PART 5 PICKS UP BECAUSE P3 CARRIES THE SAME
QUESTION AS AN OPEN ONE IN ITS OWN TEXT.  Two are refuted by computations already banked and never claimed against
them; two are answered by identifications the colour arc made for other reasons. **

  PART 1  ** `L-47`: DEGENERACY IS NOT AGREEMENT, and the bridge is at a different member. **
  PART 2  ** `L-45`: NOT a second instance -- twice over, and `L8.3`'s own guard is one of them. **
  PART 3  ** `L-55`: the causal character measures WHICH LABEL DIFFERS, and both labels are now
          named -- so colour is a SPACELIKE relation and isospin a TIMELIKE one. **
  PART 4  ** `L-56`: the two-fold cover is the HORN, its deck group is $T$, and $D_6$'s
          $\\mathbb{Z}_2$ factor is the cover's deck. **
  PART 5  ** `L-11` and a question P3 leaves open in its own text, settled by P3's own
          transitivity result. **
  PART 6  The five strikes.

Run: python3 L045w_the_four_the_scan_left.py      (sympy)
"""
import itertools
import sympy as sp

print(__doc__.split("Run:")[0])
r, r0 = sp.symbols('r r_0', real=True)
pair = sp.solve(sp.Eq(r**2 + r*r0 + r0**2 - 1, 0), r)

# =====================================================================
print("=" * 78)
print("PART 1 — `L-47`: DEGENERACY IS NOT AGREEMENT")
print("=" * 78)
print("  P3's factorisation: the cubic is (r - r_0)(r^2 + r r_0 + r_0^2 - 1), so the DESIGNATED")
print("  root is r_0 and the PAIR is the quadratic's two.  Two degeneracies, at two members:")
print()
print(f"  {'member':>26} {'r_0':>12} {'the three roots':>34} {'distinct values':>16}")
MEMBERS = [("Nariai", sp.nsimplify("1/sqrt(3)")),
           ("(generic)", sp.Rational(9, 10)),
           ("de Sitter, M = 0", sp.Integer(1)),
           ("(generic)", sp.Rational(11, 10)),
           ("** the DEGENERATE member **", sp.nsimplify("2/sqrt(3)"))]
info = {}
for nm, v in MEMBERS:
    allr = [v] + [sp.simplify(p.subs(r0, v)) for p in pair]
    vals = sorted(allr, key=lambda z: sp.N(z))
    nd = len({sp.nsimplify(sp.N(x, 12)) for x in vals})
    info[nm] = (v, vals, nd)
    print(f"  {nm:>26} {str(sp.nsimplify(v)):>12} "
          f"{str([str(sp.N(x, 5)) for x in vals]):>34} {nd:>16}")
print()
# the two splits
print(f"  {'r_0':>12} {'designation 1+2':>22} {'sign 1+2':>22} {'same split?':>12}")


def splits(v):
    des = sp.simplify(v)
    pr = [sp.simplify(p.subs(r0, v)) for p in pair]
    allr = [des] + pr
    sg = [int(sp.sign(sp.N(x))) if sp.N(x) != 0 else 0 for x in allr]
    odd = [i for i in range(3) if sg.count(sg[i]) == 1]
    return des, pr, (odd[0] if len(odd) == 1 else None)


agree = {}
for nm, v in MEMBERS:
    des, pr, oi = splits(v)
    same = (oi == 0)
    agree[sp.nsimplify(v)] = same
    print(f"  {str(sp.nsimplify(v)):>12} {'{designated} | pair':>22} "
          f"{('{designated} | pair' if oi == 0 else ('{pair member} | rest' if oi is not None else 'no odd one')):>22} "
          f"{str(same):>12}")
print()
for s in [
 "⇒ ** `L-12` (c54.73) computed the whole curve: the two splits coincide EXACTLY when $|r_0|>1$,",
 "   because the pair's product is $r_0^2-1$.  So the agreement region is the interval",
 "   $(1,\\,2/\\sqrt3\\,]$ -- and the DEGENERATE member is its far ENDPOINT, not a crossing. **",
 "",
 "⇒⇒ ** SO `L-47`'s PREMISE IS FALSE: THE TWO DO NOT 'MEET' AT THE DEGENERATE MEMBER.  They have",
 "   been identical throughout the interval whose endpoint it is.  ** *If anything deserves the",
 "   word bridge it is $|r_0|=1$, the $M=0$ member, where they start to agree -- and the lead",
 "   named the wrong member.*",
]:
    print("  " + s)
print()
v = sp.nsimplify("2/sqrt(3)")
_, vals, nd = info["** the DEGENERATE member **"]
print(f"  AND THE SHARPER POINT, computed: at r_0 = 2/sqrt(3) the three roots take only {nd}")
print(f"  distinct values, {[str(sp.nsimplify(x)) for x in vals]} -- the pair members COINCIDE.")
assert nd == 2
prod = sp.simplify((r0**2 - 1).subs(r0, v))
print(f"  and the pair's PRODUCT there is r_0^2 - 1 = {sp.nsimplify(prod)} != 0, so the two")
print(f"  coincident members are nonzero and share a sign.")
assert sp.simplify(prod) != 0
print()
for s in [
 "⇒⇒ ** SO AT THAT MEMBER THE SIGN SPLIT *CANNOT* SEPARATE THE PAIR -- its two members have one",
 "   value and therefore one sign -- AND IS FORCED TO $\\{$designated$\\}$ AGAINST THE PAIR, WHICH",
 "   IS THE DESIGNATION SPLIT.  THE AGREEMENT IS FORCED BY THE DEGENERACY AND SAYS NOTHING ABOUT",
 "   ANY RELATION BETWEEN THE TWO STRUCTURES. **  ** DEGENERACY IS NOT AGREEMENT. **",
 "",
 "⌗ *And the contrast with Nariai is the check that this is not special pleading: Nariai is also",
 "degenerate -- two distinct values -- but there the repetition involves the DESIGNATED root, so",
 "the sign split lands on the other pair member and the two splits DIFFER (row one of the table).",
 "** Degeneracy forces agreement only when it is the PAIR that degenerates. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — `L-45`: NOT A SECOND INSTANCE OF THE MARRIAGE")
print("=" * 78)
for s in [
 "`L8.3`, stated at r1157: *the three roots are the points ON the circle; the two rulings are the",
 "lines TANGENT to it.  $S_3$ permutes what is on it; $\\mathbb{Z}_2$ swaps what is tangent to it.*",
 "** And its own guard, written into the ledger: *'the marriage is NOT \"it's all one\" -- its",
 "   ENTIRE CONTENT IS A DIRECT PRODUCT: two independent relations to one circle.'* **",
 "",
 "`L-45` asks whether the designation/sign pair is that marriage one level down.  ** Two",
 "independent reasons say no, and the first is the guard's own criterion. **",
]:
    print("  " + s)
print()
print("  REASON 1 — INDEPENDENCE, tested:")
print(f"  {'r_0':>12} {'|r_0| > 1':>10} {'the two splits agree':>22}")
for nm, v in MEMBERS:
    print(f"  {str(sp.nsimplify(v)):>12} {str(bool(sp.N(abs(v)) > 1)):>10} "
          f"{str(agree[sp.nsimplify(v)]):>22}")
for nm, v in MEMBERS:
    assert agree[sp.nsimplify(v)] == bool(sp.N(abs(v)) > 1)
print()
for s in [
 "⇒ ** ONE SPLIT DETERMINES THE OTHER ON THE WHOLE FAMILY, THE CORRELATING QUANTITY BEING",
 "   $|r_0|$ (asserted on five members).  TWO RELATIONS OF WHICH ONE DETERMINES THE OTHER DO NOT",
 "   FORM A DIRECT PRODUCT, AND A DIRECT PRODUCT IS THE MARRIAGE'S ENTIRE CONTENT. **",
 "",
 "  REASON 2 — ** BOTH SPLITS LIE ON THE SAME SIDE OF THE MARRIAGE. **  `L8.2`'s sorting: a",
 "  RULING is a line of the substrate, so exchanging the two is a MOTION of the substrate,",
 "  gauged; a ROOT labels a different cut, so permuting them moves through SOLUTION SPACE,",
 "  global.  ** Designation and sign are both partitions of one cut's three ROOTS.  Neither is a",
 "  motion of the substrate, so neither is on the TANGENT side, and a marriage needs one of",
 "  each. **",
 "",
 "⇒⇒ ** SO THE MARRIAGE CANNOT RECUR INSIDE A TRIPLE: A TRIPLE IS ENTIRELY ON ONE SIDE OF IT. **",
 "   *`L-45` read 'a division that is invariant against one that is not' as the marriage's",
 "   signature.  ** It is not: the marriage's signature is a division of KIND -- substrate motion",
 "   against solution-space motion -- and invariance is not that. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — `L-55`: THE CAUSAL CHARACTER MEASURES WHICH LABEL DIFFERS")
print("=" * 78)
ends = [(j, e) for j in range(3) for e in ('+', '-')]
pairs = list(itertools.combinations(ends, 2))
print(f"  six hinge-ends = 3 hinges x 2 horns; {len(pairs)} unordered pairs.")
print()
print(f"  {'relation':>26} {'hinge label':>12} {'horn label':>11} {'count':>6} "
      f"{'causal character':>18}")
tally = {"same hinge": 0, "same horn": 0, "neither": 0}
for a, b in pairs:
    if a[0] == b[0]:
        tally["same hinge"] += 1
    elif a[1] == b[1]:
        tally["same horn"] += 1
    else:
        tally["neither"] += 1
ROWS = [("same hinge, other horn", "SAME", "differs", tally["same hinge"], "TIMELIKE"),
        ("same horn, other hinge", "differs", "SAME", tally["same horn"], "SPACELIKE"),
        ("both differ", "differs", "differs", tally["neither"], "NULL")]
for a, b, c, d, e in ROWS:
    print(f"  {a:>26} {b:>12} {c:>11} {d:>6} {e:>18}")
print(f"  {'':>26} {'':>12} {'':>11} {sum(tally.values()):>6}")
assert tally == {"same hinge": 3, "same horn": 6, "neither": 6}
print()
for s in [
 "** THE ASSIGNMENT IS `L-50`'s, VERIFIED AT c54.18-19: timelike iff same hinge (3), spacelike",
 "iff same horn (6), null iff neither (6) -- and the symmetry group is transitive on the six",
 "ends with one orbit per causal class, so causal character is a COMPLETE invariant. **",
 "",
 "⌗ ** SO THE CAUSAL CHARACTER OF A PAIR OF ENDS IS EXACTLY *WHICH OF THE TWO LABELS DIFFERS*,",
 "   AND THE CORPUS HAS SINCE NAMED BOTH LABELS: the hinge index is COLOUR and the horn index is",
 "   $T$, WEAK ISOSPIN. **  Substituting:",
 "",
 "     TIMELIKE   ⇔ same colour, opposite isospin  ⇔ ** the relation a state bears to its own",
 "                  isospin partner is CAUSAL CONTACT **",
 "     SPACELIKE  ⇔ same isospin, different colour ⇔ ** THE THREE COLOURS ARE MUTUALLY",
 "                  SPACELIKE -- which is what 'three walls with DISJOINT SUPPORT' says, and what",
 "                  a baryon needs: one constituent per hinge, all at once **",
 "     NULL       ⇔ both differ                    ⇔ ** the channel that changes BOTH labels, and",
 "                  the null legs are exactly the ones that graze walls **",
 "",
 "⇒⇒ ** SO `L-55` IS ANSWERED IN THE CURRENCY IT ASKED FOR: A NULL CHORD IS THE SIMULTANEOUS",
 "   COLOUR-AND-ISOSPIN CHANGE, AND SINCE A GRAZE POINT IS A WALL AND A WALL CROSSING IS A THIRD",
 "   OF A LAP, IT IS THE WINDING STEP ITSELF. **  *Not causal contact, not gauge identification:",
 "   the null legs are the wall-crossing channel, and there are twelve of them because each of",
 "   three walls is grazed four times.*",
 "",
 "⌗⌗ ** AND THE STRUCTURAL STATEMENT THE THREE CHARACTERS TOGETHER MAKE, WHICH THE CORPUS HAS NOT",
 "   WRITTEN DOWN: ON THIS SUBSTRATE COLOUR IS A SPACELIKE RELATION AND ISOSPIN A TIMELIKE ONE. **",
 "   *That is why colour's three must be present together in one simultaneity while isospin",
 "   relates a state to a partner across the horn -- one figure, two relations, and the causal",
 "   structure telling them apart with no further input.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — `L-56`: THE TWO-FOLD COVER IS THE HORN")
print("=" * 78)
print("  The forgetful map on the six ends, and on the chords:")
print()
print(f"  {'upstairs':>28} {'downstairs':>22} {'fibre':>7} {'the deck transformation':>26}")
for a, b, c, d in [("6 hinge-ends (hinge, horn)", "3 hinge lines", "2", "** T, the horn swap **"),
                   ("6 null chords U_i->D_j", "3 triangle sides", "2", "** T, the horn swap **")]:
    print(f"  {a:>28} {b:>22} {c:>7} {d:>26}")
print()
fibres = {j: [e for e in ends if e[0] == j] for j in range(3)}
assert all(len(v) == 2 for v in fibres.values()) and sum(len(v) for v in fibres.values()) == 6
print(f"  fibres over the three hinges: {[len(fibres[j]) for j in range(3)]}  -- "
      f"a genuine 2:1 cover, asserted")
print()
for s in [
 "⇒ ** `L-56` ASKS WHETHER ANYTHING ELSE IN THE CORPUS READS THE TRIANGLE AS A SHADOW WITH A",
 "   TWO-FOLD COVER UPSTAIRS.  `L-50` DOES, IN ITS OWN WORDS: *'the chords project two-to-one",
 "   onto the three sides (the two rulings, TOLD APART BY HORN)'* -- and that names the cover's",
 "   deck group without calling it one. **",
 "",
 "⌗⌗ ** AND THE COVER IS ALREADY IN P14's SYMMETRY GROUP: $D_6 = S_3 \\times \\mathbb{Z}_2$ is the",
 "   symmetry OF THE COVER, with $S_3$ the triangle's own symmetry downstairs and $\\mathbb{Z}_2$",
 "   THE DECK GROUP OF THE COVERING.  The direct product is exactly the statement that the deck",
 "   commutes with the triangle's symmetries, which is what makes the cover regular. **",
 "",
 "⇒⇒ ** SO `prop:twoalpha`(iii)'s DOUBLE RULING AND THE SUBSTRATE'S TWO HORNS ARE ONE FACT: the",
 "   two rulings are told apart by horn, so 'doubly ruled' downstairs IS 'two-sheeted' upstairs.",
 "   The triangle is the quotient of the hinge figure by $T$. **",
 "",
 "⌗ *`L-56` was registered 'new and cheap'.  ** It was cheap, and what it buys is that the",
 "corpus's $\\mathbb{Z}_2$ has three descriptions -- horn swap, second ruling, deck of the cover --",
 "which were not previously known to be the same $\\mathbb{Z}_2$. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — `L-11`, AND A QUESTION P3 LEAVES OPEN IN ITS OWN TEXT")
print("=" * 78)
for s in [
 "P3 `rem:hingetriple`, in the paper: *'the causal reach from any end splits the three HINGES as",
 "$\\{$one's own, reached timelike$\\}$ against $\\{$the other two, reached null$\\}$ ... Whether it is",
 "a third such split or the designation split wearing a causal face is **left open here**.'*",
 "",
 "⚠ ** A QUESTION IN A PAPER IS A DEFECT.  And `L-11` asks the same question in the register: **",
 "   *'is the own-wall split the designation split read on the hinges, a third structure, or the",
 "   sign split in disguise?'* -- and P3 itself says the two are the same $1{+}2$ ('the $1{+}2$ of",
 "   this section appearing once more and now on the walls').",
 "",
 "⇒ ** IT IS SETTLED BY A SYMMETRY STATEMENT THE PAPER ALREADY PROVES TWO PARAGRAPHS LATER. **",
]:
    print("  " + s)
print()
print(f"  {'the split':>22} {'partitions':>14} {'fixed by what':>26} {'symmetry-relative?':>19}")
for a, b, c, d in [
    ("causal / own-wall", "the 3 HINGES", "a choice of VANTAGE", "** YES **"),
    ("designation", "the 3 ROOTS", "the cut's own parameter r_0", "no"),
    ("sign", "the 3 ROOTS", "the roots' values, hence r_0", "no"),
]:
    print(f"  {a:>22} {b:>14} {c:>26} {d:>19}")
print()
for s in [
 "** P3, `rem:hingetriple`: *the configuration's symmetry group, of order twelve, acts",
 "TRANSITIVELY on the six ends and with a single orbit on each causal class, so causal character",
 "is a COMPLETE invariant and the $2{+}1$'s assignment is RELATIVE -- 'no invariant of the",
 "configuration can fix it'.* **",
 "",
 "⇒⇒ ** SO THE CAUSAL SPLIT IS A STRUCTURE THE SYMMETRY GROUP MAKES ARBITRARY, AND THE",
 "   DESIGNATION SPLIT IS ONE IT FIXES: $r_0$ is the cut's own parameter and no element of the",
 "   group moves it.  A SPLIT THE SYMMETRY RANDOMISES CANNOT BE A SPLIT THE SYMMETRY DETERMINES. **",
 "   ** It is a THIRD structure, and P3's own transitivity result is what decides it. **",
 "",
 "⌗ ** AND THE SIGN SPLIT IS EXCLUDED THE SAME WAY AND ALSO BY PART 1: it varies along the family",
 "   (it changes at $|r_0|=1$) while the causal split is the same $1{+}2$ at every member. **",
 "",
 "⌗ ** `L-11`'s SECOND CLAUSE -- 'the DESIGNATION $2{+}1$ has never been run against the baryon",
 "   question, and it is the FLAVOUR-side one' -- RUNS AND RETURNS NOTHING, WHICH IS THE CORRECT",
 "   ANSWER AND NOT AN UNFINISHED ONE. **  *A baryon is a colour singlet built from one",
 "   constituent per hinge; the designation split does not partition hinges at all, so it cannot",
 "   enter the baryon's colour structure -- and c54.78 is the same statement from the other side,",
 "   colour being blind to what distinguishes singlets.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE FIVE STRIKES")
print("=" * 78)
print(f"  {'lead':>7} {'disposal':>13} {'paid by':>44}")
for a, b, c in [
    ("L-11", "** STRIKE **", "a third structure, by P3's own transitivity"),
    ("L-45", "** STRIKE **", "not a direct product, and both on one side"),
    ("L-47", "** STRIKE **", "degeneracy is not agreement; wrong member"),
    ("L-55", "** STRIKE **", "character = which label differs"),
    ("L-56", "** STRIKE **", "the cover's deck is T; D_6 is its symmetry"),
]:
    print(f"  {a:>7} {b:>13} {c:>44}")
print()
for s in [
 "⌗ ** TWO WERE REFUTED BY A COMPUTATION BANKED AT c54.73 FOR A DIFFERENT LEAD, TWO BY",
 "   IDENTIFICATIONS THE COLOUR ARC MADE FOR OTHER REASONS, AND ONE BY A TRANSITIVITY RESULT",
 "   PROVED IN THE SAME REMARK THAT POSES IT.  NONE NEEDED NEW GEOMETRY. **",
 "",
 "⚠ *And what PART 3 and PART 4 add is not a strike but a reading, so it is stated as one: the",
 "causal trichotomy and the double cover were both already computed and verified.  ** What is new",
 "is that their two labels are colour and isospin, which makes the trichotomy a statement about",
 "the Standard Model's two indices and not only about six points. ***",
]:
    print("  " + s)
