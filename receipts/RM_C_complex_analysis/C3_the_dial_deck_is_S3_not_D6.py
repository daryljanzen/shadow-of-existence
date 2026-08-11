#!/usr/bin/env python3
"""C3_the_dial_deck_is_S3_not_D6.py -- R-M station C, probe C3, and it CORRECTS THIS BAKE'S OWN RECORD.

THE QUESTION.  X1r (r1874) recorded the dial as "6-to-1 over a generic value, deck D_6 (rotation
w+60deg and reflection w -> -w, both sending 2M -> -2M)".  C2 (r2410) closed the tower's outward
question -- the turnaround deck is not a storey of it -- so the tower's own remaining question is
upward: ** what sits above the dial, and is D_6 the top? **

THE ANSWER IS THAT THE QUESTION IS MALFORMED AS ASKED, AND THE REASON IS IN X1r's OWN PARENTHESIS.

    ** A deck transformation of the map (dial -> 2M-plane) must PRESERVE 2M. **  The two generators
    X1r names, w -> w + 60deg and w -> -w, BOTH SEND 2M -> -2M -- X1r says so in the same breath.
    ** So neither is a deck transformation of that covering. **

Computed here: with 2M(w) = (2/3sqrt3) sin 3w,

    PRESERVE 2M:   a: w -> w + 2pi/3   (order 3)      b: w -> pi/3 - w   (order 2)
                   and they satisfy  a^3 = b^2 = 1,  b a b = a^{-1}   ⇒  ** the group is S_3 **
    SEND 2M -> -2M: w -> w + pi/3,  w -> -w,  w -> w + pi   -- the OTHER coset

and the dial is genuinely 6-to-1 (six solutions of sin 3w = c on [0, 2pi), checked numerically).

⇒ ** THE DECK OF THE DIAL OVER THE 2M-PLANE IS S_3, OF ORDER 6, AND THE COVERING IS THEREFORE
   REGULAR (GALOIS): degree 6 with a deck group of order 6. **  D_6 (order 12) is the full symmetry
   of the dial as a figure, not the deck of that map; its index-2 subgroup preserving 2M is the deck,
   and ** the other coset is exactly R -- which is X1r's own second storey, correctly identified
   there and misassigned in the parenthesis. **

WHY THIS MATTERS AND IS NOT PEDANTRY.  A degree-3 covering with monodromy S_3 is NOT regular: its
deck group is trivial, and the regular cover is the degree-6 Galois closure.  ** So "the dial is a
6-to-1 regular cover whose deck is S_3" IS the statement that the dial is the GALOIS CLOSURE of the
root cover ** -- which the corpus already carries, at P5 `rem:galois-closure` ("the sky angle IS the
Galois closure", landed r1882).  ** The two records agree once the group is named correctly, and
disagree while it is not. **

⇒ AND THE TOWER IS THEREFORE COMPLETE AND ITS TOP IS NAMED: dial (Galois closure, deck S_3) -> root
cover (degree 3, non-regular, trivial deck) -> the 2M-plane, with R the involution relating the dial
to its 2M -> -2M image.  ** There is nothing above the dial to find: a Galois closure is by
construction the smallest regular cover, and asking for a further storey over the 2M-plane asks for
a regular cover of a regular cover, which adds no monodromy. **

WHAT IS NOT SHOWN: that D_6 is wrong ABOUT THE DIAL -- it is right, as the dial's own symmetry group
(P3 sec:tour's hexagonal symmetry).  ** What is corrected is which group is the DECK OF WHICH MAP. **

Written r2411.  Stated for reversal.
"""
import sympy as sp
import numpy as np

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C3 -- what is the deck of the dial over the 2M-plane, and is there a storey above it?")
    print()
    w = sp.Symbol('w')
    f = sp.sin(3*w)                      # 2M up to the fixed factor 2/(3 sqrt 3)

    def preserves(g):
        return sp.simplify(sp.expand_trig(f.subs(w, g) - f)) == 0

    def flips(g):
        return sp.simplify(sp.expand_trig(f.subs(w, g) + f)) == 0

    a = w + 2*sp.pi/3
    b = sp.pi/3 - w

    # ---- X1r's two named generators do NOT preserve the base --------------------
    check("X1r's rotation w -> w + pi/3 (60 deg) sends 2M -> -2M, so it is NOT a deck map",
          flips(w + sp.pi/3) and not preserves(w + sp.pi/3))
    check("X1r's reflection w -> -w sends 2M -> -2M, so it is NOT a deck map",
          flips(-w) and not preserves(-w))

    # ---- the actual deck ------------------------------------------------------
    check("a: w -> w + 2pi/3 preserves 2M", preserves(a))
    check("b: w -> pi/3 - w preserves 2M", preserves(b))
    check("a has order 3", sp.simplify(sp.expand_trig(f.subs(w, a.subs(w, a.subs(w, a))) - f)) == 0
          and sp.simplify(a.subs(w, a.subs(w, a)) - (w + 2*sp.pi)) == 0)
    check("b is an involution", sp.simplify(b.subs(w, b) - w) == 0)
    bab = b.subs(w, a.subs(w, b))
    check("b a b = a^{-1}  ⇒  the group generated is S_3, order 6",
          sp.simplify(bab - (w - 2*sp.pi/3)) == 0)

    # ---- the covering is genuinely degree 6 -----------------------------------
    xs = np.linspace(0, 2*np.pi, 2_000_001)
    ys = np.sin(3*xs)
    for c in (1/3, -0.71, 0.05):
        crossings = int(np.sum((ys[:-1] - c)*(ys[1:] - c) < 0))
        check(f"sin 3w = {c:+.2f} has exactly 6 solutions on [0, 2pi)", crossings == 6)

    # ---- degree 6 with deck of order 6 ⇒ regular (Galois) ---------------------
    # ** THE FIRST DRAFT OF THIS CHECK WAS `True and 6 == 6` -- a TAUTOLOGY, and exactly the class
    # the fork's lint_assertions.py was extended twice to catch ("arithmetic dressed as claims").
    # It passed my own check_receipt_asserts, which tests for the PRESENCE of a failure path and not
    # for whether the condition could ever be false -- ** the boundary I wrote into that gate's own
    # docstring at r2394, met in my own receipt three revisions later. **
    # Replaced with the thing actually claimed: the deck's ORDER, counted from the group elements,
    # equals the covering's DEGREE, counted from the fibre.
    deck = set()
    for k in range(3):
        for refl in (False, True):
            g = (sp.pi/3 - w if refl else w) + 2*sp.pi*k/3
            if sp.simplify(sp.expand_trig(f.subs(w, g) - f)) == 0:
                deck.add(sp.simplify(sp.expand_trig(g - w)) if not refl else ('r', k))
    order = len(deck)
    xs0 = np.linspace(0, 2*np.pi, 2_000_001)
    degree = int(np.sum((np.sin(3*xs0[:-1]) - 0.19)*(np.sin(3*xs0[1:]) - 0.19) < 0))
    check(f"the deck's order ({order}) equals the covering's degree ({degree}) ⇒ REGULAR (Galois)",
          order == degree == 6)

    # ---- and the root cover below it is degree 3 with S_3 monodromy ⇒ NOT regular
    r, M = sp.symbols('r M')
    disc = sp.discriminant(r**3 - r + 2*M, r)
    check("the root cover has degree 3 (a cubic in r)",
          sp.degree(sp.Poly(r**3 - r + 2*M, r)) == 3)
    check("its discriminant is non-constant, so the monodromy is non-trivial",
          sp.simplify(sp.diff(disc, M)) != 0)

    print()
    if FAILED:
        print(f"  {len(FAILED)} check(s) FAILED")
        return 1
    print("  VERDICT: the deck of the dial over the 2M-plane is S_3 (order 6), so the covering is")
    print("  REGULAR -- degree 6 with a deck of order 6.  ** D_6 (order 12) is the dial's symmetry")
    print("  as a FIGURE, not the deck of that map; its index-2 subgroup preserving 2M is the deck,")
    print("  and the other coset is exactly R. **  X1r named the right objects and misassigned the")
    print("  group, and said so in its own parenthesis (both generators 'sending 2M -> -2M').")
    print("  ⇒ A degree-3 cover with S_3 monodromy is NOT regular, so the degree-6 regular cover IS")
    print("  the Galois closure -- which the corpus already carries at P5 rem:galois-closure.")
    print("  ** The two records agree once the group is named correctly, and the tower is complete:")
    print("     nothing sits above a Galois closure that adds monodromy. **")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
