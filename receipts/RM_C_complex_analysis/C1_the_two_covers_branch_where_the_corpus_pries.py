#!/usr/bin/env python3
"""C1_the_two_covers_branch_where_the_corpus_pries.py -- R-M station C, re-entry, probe C1.

THE OPENING QUESTION, from the corpus and not from the field (the bake form's rule).  The corpus
carries TWO three-fold structures and P14 sec:whichthree distinguishes them:

  COVER A -- the HORIZON root cover.  2M |-> {r : r^3 - alpha^2 r + 2M alpha^2 = 0}, three sheets,
             monodromy the Weyl S_3 permuting the roots.  ** It moves 2M: that is its base. **
  COVER B -- the TURNAROUND deck.  tau |-> tau + 2 pi i alpha/(D-1) leaves r^{D-1} invariant while
             sending r |-> e^{2 pi i/(D-1)} r; a cyclic Z_3 action.  ** It FIXES 2M ** (L-212, r2404).

P7's `lem:twoturnings` says no affine change of variable identifies the horizon roots with the
turnaround's.  That is a statement about ROOTS.  ** The complex-analytic question is about the
COVERS: where does each branch? **

THE RESULT, and it is the reason this probe was worth throwing:

    COVER A branches where its discriminant vanishes:  disc(r^3 - r + 2M) = -4(27 M^2 - 1),
        so at 2M = +- 2/(3 sqrt 3), where the roots collide at ** r = -+ alpha/sqrt3 **
        -- the NARIAI merged-horizon areal radius.
    COVER B branches where its deck has a fixed point:  omega r = r, i.e. ** r = 0 **
        -- the BRANCH POINT.

** THE TWO BRANCH SETS ARE DISJOINT, AND THEY ARE EXACTLY THE TWO LOCI THE CORPUS INSISTS ON PRYING
APART. **  P7: "alpha (the throat 3-sphere's SIZE) versus alpha/sqrt3 (the merged horizon's AREAL
RADIUS) -- quantities never to be conflated", and "conflating the two reads a discontinuity into what
is one smooth curve".  The pry-apart census carries both as entries (r2388): alpha vs alpha/sqrt3,
and the dynamical turnaround vs r=0.

So the naming guard the corpus enforces by discipline is, on the complex-analytic side, ** the
statement that its two three-fold covers have disjoint branch loci **.  A conflation of the loci is a
conflation of the covers, and that is why it produces a spurious discontinuity: it identifies a point
where one cover is branched with a point where the other is.

WHAT THIS DOES NOT SHOW, and must not be read in: that the two covers are unrelated as spaces -- only
that ** they do not branch at the same places **, which is what makes the corpus's insistence on
keeping the loci apart a structural fact rather than a notational preference.

Written r2408.  Stated for reversal.
"""
import sympy as sp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C1 -- where do the corpus's two three-fold covers branch?")
    print()
    r, M = sp.symbols('r M')
    w = sp.exp(2*sp.pi*sp.I/3)

    # ---- COVER A: the horizon root cover -------------------------------------
    disc = sp.discriminant(r**3 - r + 2*M, r)
    check("disc(r^3 - r + 2M) = -4(27 M^2 - 1)",
          sp.simplify(sp.expand(disc + 4*(27*M**2 - 1))) == 0)

    brs = sorted(sp.solve(sp.Eq(disc, 0), M), key=lambda x: sp.re(x))
    check("cover A branches at exactly two values of 2M", len(brs) == 2)
    check("those values are 2M = +- 2/(3 sqrt 3)",
          sp.simplify(sp.Abs(2*brs[0]) - 2/(3*sp.sqrt(3))) == 0)

    # at each branch value the roots collide, and the collision radius is the Nariai one
    # ** sp.solve DEDUPLICATES roots, so it cannot see a double root at all.  The first run of
    # this probe used it and the check failed with an IndexError -- ** a check that cannot find the
    # thing it is looking for is not a negative result, it is a broken check **, and it failed
    # loudly, which is what a receipt that can fail is for.  sp.roots() carries multiplicities. **
    for b in brs:
        mult = sp.roots(sp.Poly(r**3 - r + 2*b, r))
        dbl = [x for x, m in mult.items() if m >= 2]
        check(f"2M={sp.nsimplify(2*b)}: a double root exists (multiplicity read, not deduplicated)",
              len(dbl) == 1)
        check(f"2M={sp.nsimplify(2*b)}: the double root sits at |r| = alpha/sqrt3",
              sp.simplify(sp.Abs(dbl[0]) - 1/sp.sqrt(3)) == 0)

    # ---- COVER B: the turnaround deck ----------------------------------------
    fixed = sp.solve(sp.Eq(w*r, r), r)
    check("cover B's deck has exactly one fixed point", len(fixed) == 1)
    check("that fixed point is r = 0 -- the branch point", sp.simplify(fixed[0]) == 0)

    # and the deck genuinely fixes 2M (the L-212 fact this probe rests on)
    tau, a = sp.symbols('tau alpha', positive=True)
    r3 = 2*M*a**2*sp.sinh(3*tau/(2*a))**2
    r3s = 2*M*a**2*sp.sinh(3*(tau + 2*sp.pi*sp.I*a/3)/(2*a))**2
    check("the deck shift leaves r^3 -- and hence 2M -- invariant",
          sp.simplify(sp.expand_trig(r3s - r3)) == 0)

    # ---- THE JOINT: the branch sets are disjoint ------------------------------
    A_branch = {sp.simplify(1/sp.sqrt(3)), sp.simplify(-1/sp.sqrt(3))}
    B_branch = {sp.Integer(0)}
    check("the two branch sets are DISJOINT",
          not (A_branch & B_branch))
    check("cover A's branch radius is alpha/sqrt3, cover B's is 0 -- the two loci the corpus"
          " insists on prying apart",
          sp.simplify(min(sp.Abs(x) for x in A_branch) - 1/sp.sqrt(3)) == 0
          and sp.simplify(list(B_branch)[0]) == 0)

    print()
    if FAILED:
        print(f"  {len(FAILED)} check(s) FAILED")
        return 1
    print("  VERDICT: cover A (horizon roots, S_3, moves 2M) branches at r = -+ alpha/sqrt3 -- the")
    print("  Nariai merged-horizon areal radius.  Cover B (turnaround deck, Z_3, FIXES 2M) branches")
    print("  at r = 0 -- the branch point.  ** The branch sets are disjoint, and they are exactly")
    print("     the two loci the corpus insists on prying apart. **  The naming guard is, on this")
    print("  side, the statement that the two three-fold covers do not branch in the same place --")
    print("  which is why conflating the loci 'reads a discontinuity into what is one smooth curve'.")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
