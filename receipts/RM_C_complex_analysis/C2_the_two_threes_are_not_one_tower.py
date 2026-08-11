#!/usr/bin/env python3
"""C2_the_two_threes_are_not_one_tower.py -- R-M station C, probe C2.

THE QUESTION, from the corpus and from C1.  The first pass of this bake (`X1r`) established that
Aut(A_2) = S_3 x Z_2 IS A TWO-STOREY TOWER OF COVERS: the dial (6-to-1 onto the 2M-plane, deck D_6,
branched at the six Nariai CRESTS) sits over the root cover (3 sheets over the 2M-plane, deck S_3,
branched at the two Nariai VALUES), ** and the dial is a double cover of the root cover with covering
involution R **.

Then L-212 (r2404) and C1 (r2408) put a THIRD three-fold in play: the turnaround deck Z_3, which
FIXES 2M and branches at r = 0.  Nobody has asked how it sits with the tower.  ** A three-fold that
fixes the tower's base is either a further storey, a parallel cover, or unrelated -- and the three
possibilities are distinguishable. **

THE RESULT.

    The turnaround deck fixes 2M, so it acts within a fibre of the root cover -- IF it acts on that
    fibre at all.  It does not.  With r a root of r^3 - r + 2M,

        (w r)^3 - (w r) + 2M  =  r^3 + 2M - w r  =  r - w r  =  r (1 - w),

    using r^3 = r - 2M.  ** That vanishes only at r = 0. **  So w.r is a root of the same cubic only
    at the branch point, and nowhere else.

⇒ ** THE TURNAROUND DECK IS NOT A DECK TRANSFORMATION OF THE ROOT COVER, IN ANY STOREY. **  It fixes
the base and does not permute the fibre; it is not a further storey of X1r's tower, and the tower
does not extend to it.  The two three-nesses are covers of DIFFERENT BASES with DIFFERENT FIBRES:

    ROOT cover        base = the 2M-plane   fibre = the cubic's roots    deck S_3   branch 2M = +-2/(3 sqrt3)
    TURNAROUND cover  base = the r^3-plane  fibre = the cube roots       deck Z_3   branch r = 0

** WHAT THIS ADDS TO THE CORPUS.  P7's lem:twoturnings says no affine change of variable identifies
the horizon roots with the turnaround's -- a statement about ROOTS.  This is the statement about
COVERS, and it is strictly stronger: not merely that no affine map identifies the two triples, but
that ** neither three's deck acts on the other's fibre at all **, so they cannot be related by any
covering-space construction over the 2M-plane. **

AND IT IS WHY P14 sec:whichthree'S MOVE WAS AVAILABLE.  Seating the generations on the turnaround
rather than on the hinges required the two threes to be genuinely different objects; had the
turnaround deck been a storey of the root tower, the "which index is it" question would have had no
room to move.  ** The move P14 made is licensed by a fact nobody had computed. **

WHAT IS NOT SHOWN, and must not be read in: that the two covers share no structure whatever.  They
share the variable r and the parameter 2M, and both count three because f = 0 has degree D-1 -- which
P14 states and this does not touch.  ** What is shown is that they are not related AS COVERS. **

Written r2410.  Stated for reversal.
"""
import sympy as sp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C2 -- is the turnaround deck a further storey of the root tower?")
    print()
    r, M = sp.symbols('r M')
    w = sp.exp(2*sp.pi*sp.I/3)

    # ---- the deck fixes the root cover's BASE ---------------------------------
    tau, a = sp.symbols('tau alpha', positive=True)
    r3 = 2*M*a**2*sp.sinh(3*tau/(2*a))**2
    r3s = 2*M*a**2*sp.sinh(3*(tau + 2*sp.pi*sp.I*a/3)/(2*a))**2
    check("the turnaround deck fixes 2M -- the root cover's base coordinate",
          sp.simplify(sp.expand_trig(r3s - r3)) == 0)

    # ---- but it does NOT act on the root cover's FIBRE ------------------------
    # on the cubic, r^3 = r - 2M; substitute and see what survives
    residual = sp.simplify(sp.expand((w*r)**3 - w*r + 2*M).subs(r**3, r - 2*M))
    check("(w.r)^3 - w.r + 2M reduces to r(1 - w) on the cubic",
          sp.simplify(residual - r*(1 - w)) == 0)
    zeros = sp.solve(sp.Eq(residual, 0), r)
    check("that vanishes at exactly one point", len(zeros) == 1)
    check("and that point is r = 0 -- the branch point, not a generic fibre point",
          sp.simplify(zeros[0]) == 0)

    # numeric confirmation on a generic fibre: no root maps to a root
    import numpy as np
    ww = complex(sp.N(w))
    for twoM in (0.2, -0.35, 0.61):
        rts = np.roots([1, 0, -1, twoM])
        moved = [ww*x for x in rts]
        hit = any(min(abs(m - y) for y in rts) < 1e-9 for m in moved)
        check(f"2M={twoM:+.2f}: no root of the cubic is carried to a root by w",
              not hit)

    # ---- and it IS a deck transformation of its own cover ---------------------
    check("the deck has order 3 on its own cover (w^3 = 1)", sp.simplify(w**3 - 1) == 0)
    check("its branch locus is r = 0 (omega r = r only there)",
          sp.solve(sp.Eq(w*r, r), r) == [0])

    # ---- the root cover's own branch locus, for the disjointness statement ----
    disc = sp.discriminant(r**3 - r + 2*M, r)
    brs = sp.solve(sp.Eq(disc, 0), M)
    dbl = []
    for b in brs:
        mult = sp.roots(sp.Poly(r**3 - r + 2*b, r))
        dbl += [x for x, m in mult.items() if m >= 2]
    check("the root cover branches at |r| = alpha/sqrt3, disjoint from r = 0",
          all(sp.simplify(sp.Abs(x) - 1/sp.sqrt(3)) == 0 for x in dbl) and dbl)

    print()
    if FAILED:
        print(f"  {len(FAILED)} check(s) FAILED")
        return 1
    print("  VERDICT: the turnaround deck FIXES the root cover's base and does NOT permute its")
    print("  fibre -- w.r is a root of the same cubic only at r = 0.  ** So it is not a further")
    print("  storey of X1r's tower, in any storey: the two three-nesses are covers of DIFFERENT")
    print("  BASES with DIFFERENT FIBRES. **")
    print("  This is lem:twoturnings' statement about ROOTS, raised to a statement about COVERS,")
    print("  and it is strictly stronger -- and it is what licensed P14 sec:whichthree's move of")
    print("  the generations off the hinges and onto the turnaround.")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
