#!/usr/bin/env python3
"""
L-48w — THE `R3` CLUSTER, FINISHED.  Three leads thrown off by `L-10`'s naming, all on the same
row of `FIGURE_THEOREM_LEDGER`, worked together because the third needs the first two.

  `L-48`  what IS $1+(D{-}2)$ at $D=5$?  The designation split generalises; at five it is $1+3$.
          ** Is $1+3$ anything? **
  `L-46`  is P14's "flavour-breaking structure" the HIERARCHY, or something else?  P14 names it
          and explicitly declines to claim it, and ** nobody has asked what else it could be. **
  `L-49`  `R3`'s two targets may pair with its two objects the OTHER WAY ROUND from how the row
          reads.

** THE FIRST HAS A COMPUTATION NOBODY RAN AND IT PAYS THREE WAYS; THE SECOND IS DECIDED BY A
PROPERTY THE CORPUS ALREADY RECORDS; AND THE THIRD IS NOT A RE-ORDERING BUT A MISSING OBJECT. **

  PART 1  ** `L-48`: the horizon polynomial at general $D$, factorised.  $-r_0$ IS A ROOT EXACTLY
          AT ODD $D$, so at five the $1{+}3$ is really $1{+}1{+}2$. **
  PART 2  ** AND THAT IS THE PARITY AGAIN: at odd $D$ the $R$-image is INTERNAL to one geometry's
          own root set.  One computation, and it is WHY five is vector-like. **
  PART 3  ** `L-46`: it cannot be the hierarchy, and the reason is that one is indexical and the
          other absolute. **
  PART 4  ** `L-49`: the row is not mis-ORDERED, it is missing an OBJECT -- and the horn supplies
          a better-typed candidate for the target it cannot place. **
  PART 5  The three strikes, and what is registered rather than claimed.

Run: python3 L048w_the_r3_cluster.py      (sympy)
"""
import itertools
import sympy as sp

print(__doc__.split("Run:")[0])
r, r0 = sp.symbols('r r_0', real=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE HORIZON POLYNOMIAL AT GENERAL D, FACTORISED")
print("=" * 78)
print("  P14, gauge alpha = 1: the D-dimensional mass factor is 2M = r_0^(D-3) - r_0^(D-1), so")
print("  the horizon condition with the slicing's own root substituted is")
print()
print("     P_D(r) = r^(D-1) - r^(D-3) + r_0^(D-3) - r_0^(D-1) = 0")
print()
print(f"  {'D':>3} {'(r - r_0) divides?':>19} {'the cofactor':>44} {'-r_0 a root?':>13}")
cof = {}
for D in range(4, 9):
    P = sp.expand(r**(D-1) - r**(D-3) + r0**(D-3) - r0**(D-1))
    q, rem = sp.div(P, r - r0, r)
    assert sp.simplify(rem) == 0
    f = sp.factor(q)
    neg = (sp.simplify(P.subs(r, -r0)) == 0)
    cof[D] = (f, neg)
    print(f"  {D:>3} {'yes':>19} {str(f)[:44]:>44} {str(neg):>13}")
print()
assert cof[4][1] is False and cof[5][1] is True
assert cof[6][1] is False and cof[7][1] is True
for s in [
 "⇒⇒ ** $-r_0$ IS A ROOT OF THE HORIZON POLYNOMIAL EXACTLY AT ODD $D$, asserted at four values. **",
 "   *Substituting $r=-r_0$ gives $2(r_0^{D-3}-r_0^{D-1}) = 2\\cdot 2M$ at even $D$ and $0$ at odd.*",
 "",
 "⇒ ** SO AT $D=5$ THE '$1{+}3$' IS NOT IRREDUCIBLE.  The cofactor is $(r+r_0)(r^2+r_0^2-1)$ --",
 "   A LINE AND A CIRCLE -- so the three break further as $1{+}2$, the extra ONE being $-r_0$",
 "   itself. **  ** `L-48`'s question has an answer and it is: $1+3$ is $1+1+2$. **",
 "",
 "⌗ *And it confirms `PO-1a`'s recorded 'a CONIC cofactor only at $D=4$' by exhibiting what",
 "replaces it: at four the cofactor is $r^2+rr_0+r_0^2-1$, a genuine conic with a cross term; at",
 "five it is a line times a circle; at six and eight it does not factor at all over the rationals.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND THAT IS THE PARITY AGAIN")
print("=" * 78)
print(f"  {'D':>3} {'2M(r_0) odd in r_0?':>21} {'-r_0 in the root set?':>23} {'gamma^5 exists?':>16}")
for D in range(4, 9):
    twoM = sp.expand(r0**(D-3) - r0**(D-1))
    odd = sp.simplify(twoM.subs(r0, -r0) + twoM) == 0
    print(f"  {D:>3} {str(odd):>21} {str(cof[D][1]):>23} {str(odd):>16}")
    assert odd != cof[D][1]
print()
for s in [
 "⇒⇒ ** THE TWO COLUMNS ARE EXACT COMPLEMENTS, ASSERTED AT FIVE DIMENSIONS: $-r_0$ IS IN THE ROOT",
 "   SET PRECISELY WHEN THE MASS IS *NOT* ODD -- i.e. precisely when there is no $\\gamma^5$. **",
 "",
 "⌗⌗ ** AND THAT IS THE MECHANISM, NOT A CORRELATION.  At EVEN $D$ the $R$-image of a geometry is",
 "   a DIFFERENT MEMBER of the family -- $r_0 \\mapsto -r_0$ carries mass $2M$ to $-2M$ -- so $R$",
 "   relates two geometries and can serve as a matter/antimatter parity.  At ODD $D$ the",
 "   $R$-image root sits INSIDE THE SAME GEOMETRY'S OWN ROOT SET, so $R$ moves nothing: the",
 "   geometry is its own image. **",
 "",
 "⇒ ** SO 'FIVE IS VECTOR-LIKE' IS NOT A SEPARATE FACT FROM 'FIVE'S CONJUGATE IS ITSELF'.  The",
 "   parity has nowhere to act because its image is already present. **  *`L-6w` reached the same",
 "   conclusion from the mass function's Fourier content; this reaches it from the root set, and",
 "   the two routes share no step.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — `L-46`: IT CANNOT BE THE HIERARCHY")
print("=" * 78)
for s in [
 "P14 names the slicing's singling-out of one root against the ellipse pair a **flavour-breaking",
 "structure** and explicitly declines to claim it is the physical hierarchy.  ** `L-46` asks what",
 "else it could be.  The corpus's own record of the object decides it. **",
 "",
 "`PO-1a`, naming the object at c54.17: *'$\\{$the designated root$\\}$ against $\\{$the ellipse",
 "pair$\\}$ -- a property of the **VANTAGE**, THREE PER GEOMETRY, permuted by $S_3$.'*",
]:
    print("  " + s)
print()
print(f"  {'':>26} {'determined by':>26} {'same for every reader?':>23}")
for a, b, c in [("the designation 1+2", "the cut -- which root r_0 is", "** NO -- three per geometry **"),
                ("the physical hierarchy", "the Lagrangian's Yukawas", "** YES -- absolute **")]:
    print(f"  {a:>26} {b:>26} {c:>23}")
print()
for s in [
 "⇒⇒ ** ONE GEOMETRY CARRIES THREE DESIGNATION SPLITS, ONE PER CUT, AND THE $S_3$ PERMUTES THEM.",
 "   THE HIERARCHY CARRIES NO SUCH MULTIPLICITY: the third family is the heavy one for everybody.",
 "   AN INDEXICAL STRUCTURE CANNOT BE AN ABSOLUTE ONE. **",
 "",
 "⇒ ** SO WHAT IT IS, STATED POSITIVELY: the designation $1{+}2$ is the flavour-side INDEXICAL --",
 "   'the generation this cut is' against the other two -- and P3 names the designated side in",
 "   exactly those words, 'MY HORIZON'. **  *A splitting that says which one is MINE is not a",
 "   splitting that says which one is HEAVY.*",
 "",
 "⌗ ** AND READING THE HIERARCHY OFF IT WOULD BE THE ERROR `PO-1d` PROTECTS AGAINST, ONE OBJECT",
 "   OVER: asserting an absolute distinction where the geometry supplies a relative one. **",
 "   *P14's declining to claim it was right, and the reason it did not state is now available.*",
 "",
 "⚠ *This NARROWS `PO-1a` and does not close it: its question is what the designation split is a",
 "candidate FOR, and generations/flavour remains the candidate side.  ** What is removed is one",
 "reading of that side -- the hierarchy -- and nothing else. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — `L-49`: NOT MIS-ORDERED, MISSING AN OBJECT")
print("=" * 78)
for s in [
 "`R3`'s row reads *'$1{+}2 \\to uud$ / generations'* -- TWO targets -- and `L-49` suspects the",
 "pairing runs the other way from how the row reads.",
 "",
 "⌗ ** FIRST, THE RE-ORDERING IS ALREADY THE CORPUS'S RECORDED READING and the lead can be",
 "   credited with it rather than owed it: `PO-1a` lists the designation split's natural",
 "   candidate side as GENERATIONS, and `PO-1b` lists the sign split's as SPECIES. **  *The row",
 "   is stale, not undecided.*",
 "",
 "⚠⚠ ** BUT NEITHER PAIRING CAN BE RIGHT AS STATED, AND THAT IS THE PART THE LEAD DID NOT SEE:",
 "   ONE OF THE TWO TARGETS IS NOT ON OFFER TO EITHER OBJECT. **",
]:
    print("  " + s)
print()
print(f"  {'target':>14} {'what kind of index it is':>34} {'which object partitions that index':>36}")
for a, b, c in [
    ("generations", "the turnaround's deck Z_3 (flavour)", "the DESIGNATION split -- roots"),
    ("uud", "isospin within a baryon (T, the horn)", "** NEITHER -- both split ROOTS **"),
]:
    print(f"  {a:>14} {b:>34} {c:>36}")
print()
for s in [
 "⇒⇒ ** SO `R3` PAIRS TWO OBJECTS AGAINST TWO TARGETS AND ONE TARGET BELONGS TO A THIRD OBJECT",
 "   THE ROW DOES NOT CONTAIN.  The correction is not a re-ordering; it is an ADDITION. **",
]:
    print("  " + s)
print()
print("  ** AND THE THIRD OBJECT IS AVAILABLE, BETTER-TYPED THAN THE ONE `PO-1c` CURRENTLY NAMES.")
print("     A baryon is one constituent per HINGE (colour); each constituent sits at a hinge END;")
print("     and the end carries one further bit, the HORN, which the corpus reads as ISOSPIN.")
print("     ** So a baryon's isospin content IS its horn assignment: **")
print()
assign = list(itertools.product('ud', repeat=3))
print(f"  {'horn assignment of the 3 ends':>32} {'split by horn':>15} {'reads as':>12}")
by_shape = {}
for a in assign:
    n = a.count('u')
    shape = f"{max(n,3-n)}+{min(n,3-n)}"
    by_shape.setdefault(shape, []).append(''.join(a))
for shape in sorted(by_shape, reverse=True):
    for w in by_shape[shape]:
        print(f"  {w:>32} {shape:>15} {('Delta' if shape=='3+0' else 'nucleon'):>12}")
print()
print(f"  total assignments = 2^3 = {len(assign)}, of which {len(by_shape['3+0'])} are 3+0 and "
      f"{len(by_shape['2+1'])} are 2+1")
assert len(assign) == 8 and len(by_shape['3+0']) == 2 and len(by_shape['2+1']) == 6
print()
for s in [
 "⇒ ** $uud$ IS THE $2{+}1$ BY HORN, AND $uuu$ / $ddd$ ARE THE $3{+}0$ -- BOTH OF WHICH THE",
 "   STANDARD MODEL HAS ($\\Delta^{++}$, $\\Delta^{-}$).  The exchanging relation `PO-1c` says is",
 "   what is really owed is then $T$ ITSELF, the horn swap, which is exactly the operation that",
 "   carries $u$ to $d$. **",
 "",
 "⚠⚠ ** AT HONEST WEIGHT, AND THE COUNT IS THE CHEAP PART. **  *Eight assignments is $2^3$ and",
 "   any three binary labels give eight; the $4\\oplus2\\oplus2$ the Standard Model reads there",
 "   needs each $\\mathbb{Z}_2$ PROMOTED TO AN $SU(2)$, which this construction does not do -- $T$",
 "   is a discrete horn swap and no continuous group is derived anywhere.*  ** What is NOT cheap",
 "   is the TYPE: $uud$ is a partition by the very index the corpus independently reads as",
 "   isospin, and neither of `R3`'s two objects partitions that index at all. **",
 "",
 "⚠ ** REGISTERED AS A CANDIDATE, NOT CLAIMED, AND `PO-1c` STAYS OPEN. **  *Its currently named",
 "candidate is the causal $2{+}1$ on the hinges -- which c54.81 identified as a partition of",
 "COLOUR, so it is mis-typed for a flavour target.  ** Removing a candidate and offering a",
 "better-typed one leaves the question more open, not less, and that is the honest direction. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE THREE STRIKES")
print("=" * 78)
print(f"  {'lead':>7} {'disposal':>13} {'answer':>46}")
for a, b, c in [
    ("L-46", "** STRIKE **", "not the hierarchy: indexical vs absolute"),
    ("L-48", "** STRIKE **", "1+3 is 1+1+2, the extra one being -r_0"),
    ("L-49", "** STRIKE **", "not mis-ordered; missing a third object"),
]:
    print(f"  {a:>7} {b:>13} {c:>46}")
print()
for s in [
 "⌗ ** WHAT THE CLUSTER LEAVES BEHIND IS ONE NEW RESULT AND TWO CORRECTIONS. **  *The result is",
 "   PART 2: at odd $D$ the geometry's own root set already contains its $R$-image, which is why",
 "   the parity has nothing to do -- a second and independent derivation of P14's dimension",
 "   argument's odd-$D$ exclusion.*  ** The corrections are that `R3`'s row is stale and",
 "   under-populated, and that `PO-1c`'s named candidate is mis-typed. **",
 "",
 "⚠ *Three PROTECTED items are touched and none is closed: `PO-1a` narrowed, `PO-1b` untouched,",
 "`PO-1c` left more open than it was.*",
]:
    print("  " + s)
