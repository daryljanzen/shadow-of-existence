#!/usr/bin/env python3
"""C4_the_reality_grid_and_the_pencil.py -- R-M station C, probe C4: the queue's last live entry.

THE QUEUE ENTRY, verbatim from this ledger's 4c: "The same question on sinh.  X2r gives its single
period i pi; ** its reality set is the analogous grid, and the turnaround sits somewhere on it. **"

** THE PREMISE IS WRONG AND THE CORRECTION IS THE RESULT.  sinh's reality set is NOT an analogous
grid. **

    Im sin(x+iy)  = cos(x) sinh(y)   ->  vanishes on  y = 0  OR  x = pi/2 + k pi
                                         ** one horizontal PLUS infinitely many verticals: a GRID,
                                            and it has CROSSINGS. **
    Im sinh(x+iy) = sin(y) cosh(x)   ->  vanishes on  y = k pi   only, since cosh x never vanishes
                                         for real x
                                         ** a PENCIL of parallel horizontals: NO crossings at all. **

X3r's whole result was that ** the seam is where two reality-lines of sin CROSS, at a critical point **
-- one fact giving four of P3's seam properties.  ** sinh has no crossings, so no analogue of X3r can
exist on the clock. **  The queue asked for the analogue of a structure the other function does not
have.

AND THE CORPUS USES sinh^2, NOT sinh, WHICH CHANGES THE ANSWER AGAIN AND FOR THE BETTER:

    Im sinh^2(x+iy) = sin(2y) sinh(2x) / 2   ->  reality lines at  y = k pi/2

    ** HALF the spacing of sinh's own. **  And on the two lowest lines, with u = 3 tau / 2 alpha:

        Im u = 0     :  sinh^2 = + sinh^2 x   >= 0     ->  r^3 >= 0,  the EXPANDING branch
        Im u = pi/2  :  sinh^2 = - cosh^2 x   <= -1    ->  r^3 <= 0,  the CONJUGATE (r<0) branch

    and ** Im u = pi/2 is exactly the bead's bound |Im tau| = pi alpha/3 ** (L-209, r2391: the bound
    is half the 2 pi i alpha/3 period).

⇒ THE RESULT.  ** The two lowest reality lines of sinh^2 ARE the bead's two branches. **  P3 already
says the mechanism -- "half that period carries sinh^2 -> -cosh^2, placing the conjugate collapse" --
and this says what that IS in the field's own terms: the expanding leg and the collapse leg are the
two lowest members of the reality set of the function the corpus solves with, and the bead's bound is
not a bound but ** the next reality line up **.

⇒ AND THE ASYMMETRY IS THE STRUCTURAL POINT, not a curiosity: sin's grid has crossings and carries a
SEAM; sinh^2's pencil has none and carries a BRANCH SEPARATION.  ** Two three-nesses, two reality
sets, two kinds of feature -- which is C1/C2's disjointness seen a third way. **

WHAT IS NOT SHOWN: that no other structure of sinh matters, or that the turnaround is at a special
point of the pencil.  ** The turnaround sits ON Im u = pi/2 (P3: the bound is reached there and held
along the collapse leg), not at a distinguished point of it. **  The queue's "sits somewhere on it"
was right about position and wrong about the set.

Written r2413.  Stated for reversal.
"""
import sympy as sp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C4 -- is sinh's reality set 'the analogous grid'?")
    print()
    x, y = sp.symbols('x y', real=True)

    # ---- sin: a grid, with crossings -----------------------------------------
    im_sin = sp.simplify(sp.im(sp.expand_complex(sp.sin(x + sp.I*y))))
    check("Im sin(x+iy) = cos(x) sinh(y)",
          sp.simplify(im_sin - sp.cos(x)*sp.sinh(y)) == 0)
    check("sin: the real axis y=0 is a reality line",
          sp.simplify(im_sin.subs(y, 0)) == 0)
    check("sin: the vertical x=pi/2 is a reality line (so the set has CROSSINGS)",
          sp.simplify(im_sin.subs(x, sp.pi/2)) == 0)

    # ---- sinh: a pencil, no crossings ----------------------------------------
    im_sinh = sp.simplify(sp.im(sp.expand_complex(sp.sinh(x + sp.I*y))))
    check("Im sinh(x+iy) = sin(y) cosh(x)",
          sp.simplify(im_sinh - sp.sin(y)*sp.cosh(x)) == 0)
    check("sinh: cosh(x) has no real zero, so no vertical line can be a reality line",
          sp.solve(sp.Eq(sp.cosh(x), 0), x) == [])
    check("sinh: the reality set is exactly y = k pi (a PENCIL, no crossings)",
          all(sp.simplify(im_sinh.subs(y, k*sp.pi)) == 0 for k in (0, 1, 2, -1)))

    # ---- sinh^2: half the spacing, and the two branches ----------------------
    s2 = sp.expand_complex(sp.sinh(x + sp.I*y)**2)
    im2 = sp.simplify(sp.im(s2))
    check("Im sinh^2 = sin(2y) sinh(2x)/2",
          sp.simplify(im2 - sp.sin(2*y)*sp.sinh(2*x)/2) == 0)
    check("sinh^2: reality lines at y = k pi/2 -- HALF sinh's spacing",
          all(sp.simplify(im2.subs(y, k*sp.pi/2)) == 0 for k in (0, 1, 2, 3)))
    check("on Im u = 0: sinh^2 = +sinh^2(x) >= 0  (the EXPANDING branch, r^3 >= 0)",
          sp.simplify(s2.subs(y, 0) - sp.sinh(x)**2) == 0)
    check("on Im u = pi/2: sinh^2 = -cosh^2(x) <= -1  (the CONJUGATE branch, r^3 <= 0)",
          sp.simplify(s2.subs(y, sp.pi/2) + sp.cosh(x)**2) == 0)

    # ---- the bead's bound IS that line ---------------------------------------
    # u = 3 tau / (2 alpha);  |Im tau| <= pi alpha/3  <=>  |Im u| <= pi/2
    a = sp.Symbol('alpha', positive=True)
    check("|Im tau| = pi.alpha/3  maps to  |Im u| = pi/2, the second reality line of sinh^2",
          sp.simplify(sp.Rational(3, 2)/a * (sp.pi*a/3) - sp.pi/2) == 0)

    print()
    if FAILED:
        print(f"  {len(FAILED)} check(s) FAILED")
        return 1
    print("  VERDICT: the queue's premise was wrong.  sin's reality set is a GRID with CROSSINGS --")
    print("  which is what X3r's seam result rests on -- while sinh's is a PENCIL of parallels with")
    print("  NO crossings, because cosh has no real zero.  ** So no analogue of X3r can exist on the")
    print("     clock: the queue asked for the analogue of a structure the other function lacks. **")
    print("  But the corpus solves with sinh^2, whose reality lines sit at HALF the spacing -- and")
    print("  ** the two lowest ARE the bead's two branches: Im u = 0 carries r^3 >= 0 (expanding),")
    print("     Im u = pi/2 carries r^3 <= 0 (conjugate), and pi/2 is exactly the bead's bound. **")
    print("  P3 gives the mechanism ('half that period carries sinh^2 -> -cosh^2'); this says what")
    print("  it IS: the bead's bound is not a bound but the next reality line up.")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
