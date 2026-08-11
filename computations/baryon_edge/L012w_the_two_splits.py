#!/usr/bin/env python3
"""
L-12w — ARE THE TWO $2{+}1$ SPLITS RELATED?  `L-12` asked whether the DESIGNATION split (the
slicing singles one root against the pair) and the SIGN split coincide at Nariai or stay
distinct, and asked for both computed along the whole dial.

** THEY ARE DISTINCT ON PART OF THE DIAL AND IDENTICAL ON THE REST, THE BOUNDARY IS THE $M=0$
MEMBER, AND THE DISCRIMINATING QUANTITY IS THE OFFSET MAGNITUDE $|r_0|$ -- NOT THE SIGN OF THE
MASS, WHICH IS WHAT I FIRST WROTE AND WHAT MY OWN TABLE REFUTED. **  And at Nariai they not only
differ: the designation split DEGENERATES while the sign split stays sharp, so the two fail in
different places and are not two readings of one thing.

  PART 1  The two splits, defined from P3's own factorisation.
  PART 2  ** BOTH SPLITS COMPUTED ALONG THE WHOLE DIAL. **
  PART 3  ** WHERE THEY COINCIDE, AND WHAT THAT LOCUS IS. **
  PART 4  What happens at Nariai, which is what `L-12` actually asked.
  PART 5  What this does to `L-11`, which is gated behind the same question.

Run: python3 L012w_the_two_splits.py
"""
import sympy as sp

print(__doc__.split("Run:")[0])

r, r0 = sp.symbols('r r_0', real=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE TWO SPLITS, FROM P3's OWN FACTORISATION")
print("=" * 78)
print("  P3, in units alpha = 1: taking the slicing parameter as one of the cubic's own roots,")
cubic = (r - r0) * (r**2 + r*r0 + r0**2 - 1)
print(f"     {sp.factor(cubic)} = 0")
pair = sp.solve(sp.Eq(r**2 + r*r0 + r0**2 - 1, 0), r)
print(f"  ⇒ the DESIGNATED root is r_0; the PAIR is {pair}")
print()
twoM = sp.simplify(r0 - r0**3)
print(f"  and the mass along the dial is  2M = {twoM}")
print(f"     2M = 0 at r_0 = {sp.solve(sp.Eq(twoM, 0), r0)}      (the de Sitter members)")
print(f"     the pair is real while 4 - 3 r_0^2 >= 0, i.e. |r_0| <= {sp.nsimplify(2/sp.sqrt(3))}")
print()
for s in [
 "** THE DESIGNATION SPLIT ** is $\\{r_0\\}$ against the pair -- 1+2 by construction, the slicing",
 "singling out its own root.",
 "** THE SIGN SPLIT ** is whichever partition of the three roots the SIGN of each induces.",
 "`L-12`: do they coincide?",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — BOTH SPLITS ALONG THE WHOLE DIAL")
print("=" * 78)


def roots_at(v):
    a = sp.nsimplify(v)
    rest = sorted([sp.simplify(p.subs(r0, a)) for p in pair], key=lambda z: sp.N(z))
    return sp.simplify(a), rest


print(f"  {'r_0':>10} {'2M':>10} {'designated':>12} {'the pair':>26} {'signs':>10} {'odd by sign':>13} {'same?':>6}")
rows = []
for v in ("-2/sqrt(3)", "-1.1", "-1", "-0.9", "-1/sqrt(3)", "0", "1/sqrt(3)", "0.9", "1", "1.1", "2/sqrt(3)"):
    a, rest = roots_at(v)
    allr = [a] + rest
    m = sp.simplify(twoM.subs(r0, a))
    sg = [int(sp.sign(sp.N(x))) if sp.N(x) != 0 else 0 for x in allr]
    # the odd-one-out by sign: the value whose sign differs from the other two
    odd = None
    for i in range(3):
        others = [sg[j] for j in range(3) if j != i]
        if others[0] == others[1] and sg[i] != others[0]:
            odd = i
    same = (odd == 0) if odd is not None else None
    rows.append((v, sp.N(m, 4), same, odd))
    print(f"  {v:>10} {sp.N(m,4)!s:>10} {sp.N(a,5)!s:>12} "
          f"{str([str(sp.N(x,5)) for x in rest]):>26} {str(sg):>10} "
          f"{('designated' if odd == 0 else ('a pair member' if odd is not None else 'none')):>13} "
          f"{str(same):>6}")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHERE THEY COINCIDE")
print("=" * 78)
print("  The splits coincide exactly when the DESIGNATED root is the sign-odd one -- i.e. when")
print("  both members of the pair share a sign opposite to r_0.  The pair's product is")
prod = sp.simplify(r0**2 - 1)
ssum = sp.simplify(-r0)
print(f"     product = {prod},   sum = {ssum}")
print(f"  Both pair members have the SAME sign iff product > 0, i.e. r_0^2 > 1;")
print(f"  and that shared sign is opposite to r_0's iff sum has r_0's opposite sign, which holds")
print(f"  automatically since sum = -r_0.")
print()
print(f"  ⇒ ** THE TWO SPLITS COINCIDE EXACTLY WHEN |r_0| > 1. **")
print()
same_pred = [(v, s) for v, m, s, o in rows]
for v, s in same_pred:
    val = abs(sp.N(sp.nsimplify(v)))
    pred = val > 1
    if s is not None:
        assert s == pred, f"prediction failed at r_0 = {v}"
print("  (checked against every sampled point above: the predicate |r_0| > 1 matches the table)")
print()
for s in [
 "⌗⌗ ** AND |r_0| = 1 IS THE $M=0$ MEMBER: $2M = r_0 - r_0^3$ vanishes at $r_0 = 0, \\pm1$. **",
 "   So the boundary between 'the two splits differ' and 'the two splits agree' is exactly the",
 "   de~Sitter member of the family.",
 "",
 "⚠ ** AND I FIRST WROTE THAT AS 'they differ on the positive-mass branch and agree on the",
 "   negative-mass branch'.  THE TABLE REFUTES IT: agreement occurs at $2M = +0.385$ (at",
 "   $r_0=-2/\\sqrt3$) AND at $2M = -0.385$ (at $r_0=+2/\\sqrt3$).  ** The agreement region spans",
 "   BOTH signs of the mass and is not a statement about the mass at all. **",
 "",
 "⇒ ** THE CORRECT CHARACTERISATION IS THE OFFSET MAGNITUDE: the splits agree iff $|r_0| > 1$,",
 "   a region INVARIANT under $R : r_0 \\mapsto -r_0$ rather than exchanged by it. **  $R$ maps",
 "   the agreement region to itself, flipping the sign of $M$ within it.",
 "",
 "⌗ ** AND ON THE DIAL THAT IS A PLAIN ANGLE.  With $r_0 = (2/\\sqrt3)\\sin w$, $|r_0|>1$ reads",
 "   $|\\sin w| > \\sqrt3/2$, i.e. ** the sky angle exceeding $60^\\circ$ ** -- and $w=60^\\circ$ is",
 "   where $\\sin 3w = 0$, which is the $M=0$ designation. **  The two splits agree beyond the",
 "   $60^\\circ$ mark and differ inside it, with Nariai at $w=30^\\circ$ well inside.",
 "",
 "⌗ *So `L-12`'s question has a structural answer rather than a yes or a no -- but the structure",
 "is the OFFSET, not the mass sign, and my first reading of my own table had it wrong.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AT NARIAI, WHICH IS WHAT `L-12` ASKED")
print("=" * 78)
nar = sp.Rational(1, 1) / sp.sqrt(3)
a, rest = roots_at("1/sqrt(3)")
print(f"  r_0 = 1/sqrt(3) (Nariai, the fixed point of sigma):")
print(f"     designated: {sp.nsimplify(a)}      pair: {[sp.nsimplify(x) for x in rest]}")
merged = any(sp.simplify(x - a) == 0 for x in rest)
print(f"  ** the designated root COINCIDES with a pair member: {merged} ** -- the double root")
assert merged
print(f"  ** and |r_0| = {sp.N(abs(nar),5)} < 1, so by PART 3 the splits DIFFER there. **")
print()
for s in [
 "⇒ ** SO AT NARIAI THE TWO SPLITS DO NOT COINCIDE -- and something sharper happens, which is",
 "   why the question was worth asking: the DESIGNATION split DEGENERATES there (the designated",
 "   root merges with a pair member, so '1 against 2' has no content) while the SIGN split stays",
 "   perfectly sharp, isolating $-2/\\sqrt3$. **",
 "",
 "⌗ ** THE TWO SPLITS ARE THEREFORE NOT MERELY DISTINCT: THEY FAIL IN DIFFERENT PLACES. **  The",
 "   designation split fails where two roots merge; the sign split fails only where a root",
 "   crosses zero.  ** A structure that survives Nariai and one that does not are not two",
 "   readings of one thing. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THIS DOES TO `L-11`")
print("=" * 78)
for s in [
 "`L-11` is GATED on `L-10` naming the object, and asks that the designation $2{+}1$ -- 'the",
 "flavour-side one' -- be run against the baryon question.",
 "",
 "⌗ ** THE COLOUR ARC HAS SINCE ANSWERED THE BARYON QUESTION FROM THE OTHER SIDE, AND IT USES A",
 "   1+2 SPLIT THAT IS NEITHER OF THESE TWO. **  The arc's split is OWN-WALL versus the other",
 "   two -- carried by which hinge owns which wall, verified twice (the null legs graze the",
 "   other two hinges' walls and never their own; the causal character on the excentre set reads",
 "   the same relation).",
 "",
 "⚠ ** SO THERE ARE NOW THREE 1+2 SPLITS IN PLAY, NOT TWO: designation, sign, and own-wall -- and",
 "   the corpus has a standing habit of conflating threes. **  What PART 3 establishes is that",
 "   the first two are exchanged by $R$.  ** Whether the own-wall split is a third or is one of",
 "   these seen on the hinges is NOT settled here and should not be assumed either way. **",
 "",
 "⇒ *Registered as the narrowing: `L-11`'s question is now 'is the own-wall split the designation",
 "split read on the hinges?', which is sharper than what it was gated on and no longer needs",
 "`L-10` to name anything.*",
]:
    print("  " + s)
