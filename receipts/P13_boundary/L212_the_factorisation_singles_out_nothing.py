#!/usr/bin/env python3
"""L212_the_factorisation_singles_out_nothing.py -- the first move on L-212, and it returns a NEGATIVE.

L-212 asks whether the R-odd fermion mass inherits the cubic's three-fold form, and its stated lever
was P13's remark that the cubic FACTORS,

    2M = r0 - r0^3   (gauge alpha = 1),   r^3 - r + 2M = (r - r0)(r^2 + r*r0 + r0^2 - 1),

"singling out r0 -- the mass-carrier -- against the fundamental pair".  The lever is the claim that
the factorisation makes a 1+2 split, so that one root is distinguished and could carry a mass while
the other two form an ellipse pair.

** THE FACTORISATION IS EXACT AND THE SINGLING-OUT IS NOT. **  Every root of the cubic satisfies
2M = r - r^3, because that IS the cubic; so taking ANY of the three as r0 reproduces the same
factorisation with the other two as the quadratic factor.  The 1+2 split is a CHOICE OF WHICH ROOT
IS THE HOLE, not a distinction the cubic makes.

That is exactly what the corpus says elsewhere in its own voice -- "identical in content, every root
returning the same 2M, and distinguished by which root each takes as its hole" (P14/P7, the three
walls as one object read three ways) -- so ** the negative is not a surprise to the corpus; it is a
surprise to the LEAD **, and it is worth a receipt because it removes the lever without touching the
question.

WHAT SURVIVES.  L-212's question stands: whether the R-odd mass departure carries a three-fold form.
What does not survive is the route through the factorisation's asymmetry, because there is no
asymmetry: the S_3 that permutes the roots permutes the choice of r0 with them.

Written r2403.  Stated for reversal.
"""
import numpy as np

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  L-212 FIRST MOVE -- does the cubic's factorisation single out a root?")
    print()

    # the factorisation is an identity in r0
    r0 = 0.37
    a = np.poly1d([1, 0, -1, r0 - r0**3])           # r^3 - r + 2M with 2M = r0 - r0^3
    b = np.poly1d([1, -r0]) * np.poly1d([1, r0, r0**2 - 1])
    check("(r-r0)(r^2+r*r0+r0^2-1) == r^3 - r + (r0 - r0^3), identically",
          np.allclose(a.coefficients, b.coefficients))

    # ** the crux **: every root reproduces it
    for twoM in (0.2, -0.35, 0.9, 1.0e-3):
        rts = np.roots([1, 0, -1, twoM])
        rts = np.sort(rts[np.abs(rts.imag) < 1e-9].real)
        if len(rts) != 3:
            continue
        check(f"2M={twoM:+.4f}: all three roots return the same 2M via r - r^3",
              np.allclose([x - x**3 for x in rts], twoM))
        for x in rts:
            other = np.sort(np.roots([1, x, x*x - 1]).real)
            rest = np.sort(np.array([y for y in rts if abs(y - x) > 1e-9]))
            check(f"2M={twoM:+.4f}: taking r0={x:+.6f} leaves exactly the other two",
                  np.allclose(other, rest))

    # and the R-odd map carries the whole configuration, not one root
    twoM = 0.2
    rts = np.sort(np.roots([1, 0, -1, twoM]).real)
    neg = np.sort(np.roots([1, 0, -1, -twoM]).real)
    check("R: 2M -> -2M sends the root SET to its negation (no root is fixed as special)",
          np.allclose(neg, np.sort(-rts)))

    print()
    if FAILED:
        print(f"  {len(FAILED)} check(s) FAILED")
        return 1
    print("  VERDICT: the factorisation is exact and singles out NOTHING.  Any root serves as r0,")
    print("  so the 1+2 split is a choice of which root is the hole -- which is the corpus's own")
    print("  reading of the three walls as one object read three ways.")
    print("  ** L-212's question survives; its lever does not. **")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
