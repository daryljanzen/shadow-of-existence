#!/usr/bin/env python3
"""
`r7267` ① — THE INPUTS THE PARITY ROWS NEED, HANDED TO `L-006w`'s OWN `twoM`.

`r7261`'s backlog named `baryon_edge/L006w_the_d5_fourfold.py: twoM` as the function nearest
to eight rows across six receipts, with the gap `INPUTS`: `L-006w` calls `twoM` at `D = 4, 5,
6` to print its monomials and never asks the one thing six receipts match as a string -- ITS
PARITY under the substrate's `R`, which is the sign reversal of the signed offset.

  `twoM(D)` returns `r_0**(D-3) - r_0**(D-1)`, so `twoM(D)|_{r_0 -> -r_0} = (-1)**(D-1) twoM(D)`.
  ** The function already holds the answer; nobody had substituted. **

⇒ ** AND IT GIVES TWO OPPOSITE PARITIES, WHICH IS THE PART WORTH HAVING COMPUTED. **  The mass
function is `R`-ODD exactly when `D` is EVEN; the wall factor `sqrt(f)/r` built on the same
`2M` is odd in the signed radius exactly when `D` is ODD.  *** At the corpus's own `D = 5`
those are not the same statement: the mass function is EVEN in the offset and the wall factor
is ODD in the radius, and two receipt prefixes match one or the other as "odd" in a signed
radial variable. ***

WHAT IS NOT CLAIMED.  ** Not that the two parities are in tension ** -- they are parities of
two different functions of two different variables, and this file computes both rather than
inferring one from the other.  ** Not a claim about `f` off the horizon branch ** -- `2M` is
taken from `twoM` at a horizon radius, which is what `twoM` is the solution of.
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                        # noqa: E402

MODULE = 'baryon_edge/L006w_the_d5_fourfold.py'


class Parity:
    """`L-006w`'s `twoM`, plus the one substitution its own report never makes."""

    def __init__(self):
        g = graft(MODULE, 'twoM', extra=('r0',))
        self.twoM, self.r0 = g['twoM'], g['r0']
        self.grafted = g['_GRAFTED']
        self.statements = (g['_STATEMENTS'], g['_OF'])

    def mass_parity(self, D):
        """the sign `twoM(D)` picks up under the substrate's `R`: `r_0 -> -r_0`.

        Returns `-1` (R-odd), `+1` (R-even) or `0` (neither)."""
        e = sp.expand(self.twoM(D))
        r = sp.expand(e.subs(self.r0, -self.r0))
        if sp.simplify(r + e) == 0:
            return -1
        if sp.simplify(r - e) == 0:
            return 1
        return 0

    def mass_is_R_odd(self, D):
        return self.mass_parity(D) == -1

    # ---- the wall factor, on the same 2M -------------------------------------------
    def metric_function(self, D, horizon=sp.Rational(1, 2), alpha=1):
        """`f = 1 - 2M/r**(D-3) - r**2/alpha**2`, with `2M` taken from `twoM` at a horizon."""
        r = sp.Symbol('r')
        M2 = sp.nsimplify(self.twoM(D).subs(self.r0, horizon))
        return r, sp.together(1 - M2 / r**(D - 3) - r**2 / alpha**2), M2

    def f_parity(self, D, **kw):
        r, f, _ = self.metric_function(D, **kw)
        if sp.simplify(sp.together(f.subs(r, -r) - f)) == 0:
            return 1
        if sp.simplify(sp.together(f.subs(r, -r) + f)) == 0:
            return -1
        return 0

    def wall_factor_parity(self, D, **kw):
        """the sign `sqrt(f)/r` picks up under `r -> -r`: `-1` is P14's "odd in the signed radius"."""
        r, f, _ = self.metric_function(D, **kw)
        W = sp.sqrt(f) / r
        if sp.simplify(W.subs(r, -r) + W) == 0:
            return -1
        if sp.simplify(W.subs(r, -r) - W) == 0:
            return 1
        return 0

    def wall_is_odd(self, D, **kw):
        return self.wall_factor_parity(D, **kw) == -1


def at_inputs():
    return Parity()


def _selftest():
    p = at_inputs()
    print('  parity.py -- L-006w grafted, twoM called at the substitution it never makes')
    print(f"    grafted {p.statements[0]} of {p.statements[1]} top-level statements")
    print(f"    {'D':>3} {'2M(r_0)':>18} {'mass parity':>12} {'f parity':>9} {'sqrt(f)/r':>11}")
    for D in (4, 5, 6, 7):
        print(f"    {D:>3} {str(p.twoM(D)):>18} {p.mass_parity(D):>12} "
              f"{p.f_parity(D):>9} {p.wall_factor_parity(D):>11}")
    assert [p.mass_is_R_odd(D) for D in (4, 5, 6, 7)] == [True, False, True, False]
    assert [p.wall_is_odd(D) for D in (4, 5, 6, 7)] == [False, True, False, True]
    print('    the mass function is R-odd exactly when D is EVEN; the wall factor is odd in the')
    print('    signed radius exactly when D is ODD.  Both from one grafted function.')
    return 0


if __name__ == '__main__':
    sys.exit(_selftest())
