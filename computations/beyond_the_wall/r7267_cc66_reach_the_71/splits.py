#!/usr/bin/env python3
"""
`r7267`/`r7281` ① BATCH THREE — THE INPUTS THREE MODULES NEED, EACH HANDED TO ITS OWN FUNCTION.

Three `(module, function)` pairs carry nine rows between them, and all three functions are
top-level and graft clean.  ** One file rather than three, because the pattern is established
and none of the three needs a rebinding: each takes its inputs as ARGUMENTS, so the change of
inputs is a call. **

  `L012w: roots_at(v)`     the horizon cubic's roots at `r_0 = v`, as (designated, the pair)
  `L127: omega_power(z)`   the exact discrete log base omega, and it RAISES off the cube roots
  `bead_conjugate: r_of_tau(t)`   the collapse radius at proper time `t`

⇒ ⛭ ** AND `roots_at` ANSWERS TWO ROWS AT ONCE IN A WAY `L-012w`'s OWN REPORT DOES NOT PRINT. **
`L-012w` tabulates eleven values of `r_0` with their designated root and pair.  *Asked instead
at the three values the hinges sit at, it returns the SAME ROOT SET every time and differs only
in WHICH member is designated* -- which is exactly what `B14` asserts and `B13` builds on, and
the identity of the sets is the half neither receipt could check.

⚠ ** `omega_power` CARRIES ITS OWN CONVERSE, which is worth saying because most do not: ** it
`raise`s `ValueError` on anything that is not a cube root of unity, so `is this value a pure
power of omega` has a built-in false case and the three rows that ask it need no constructed
edit to fail on.

WHAT IS NOT CLAIMED.  ** No claim about `r_of_tau` off the real axis ** -- it is `numpy` and
complex-valued, and the rows ask about proper time on the real branch.  ** No claim that the
cubic's roots are the hinge positions ** -- `roots_at` is asked AT values this file supplies
and the correspondence to hinges is the receipts' own, pinned there and unchanged.
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                        # noqa: E402

L012 = 'baryon_edge/L012w_the_two_splits.py'
L127 = 'baryon_edge/L127_the_bundle.py'
BEAD = 'bead_conjugate.py'


class Splits:
    """`L-012w`'s own `roots_at`, at the values its report does not tabulate together."""

    def __init__(self):
        g = graft(L012, 'roots_at', extra=('r0', 'pair'))
        self.roots_at, self.r0, self.pair = g['roots_at'], g['r0'], g['pair']
        self.statements = (g['_STATEMENTS'], g['_OF'])

    def triple(self, v):
        """all three roots at `r_0 = v`, designated first"""
        a, rest = self.roots_at(v)
        return [a] + list(rest)

    def designated(self, v):
        return self.roots_at(v)[0]

    def root_set(self, v):
        """the three roots as an unordered set of simplified values"""
        return frozenset(sp.nsimplify(sp.simplify(x)) for x in self.triple(v))

    def sets_agree(self, vs):
        """TRUE when every value in `vs` gives the SAME root set -- `B14`'s `distinguished only
        by which root each takes`"""
        return len({self.root_set(v) for v in vs}) == 1

    def designations_differ(self, vs):
        return len({sp.nsimplify(self.designated(v)) for v in vs}) == len(list(vs))

    def vanishes_at_roots(self, v):
        """the horizon cubic, evaluated at its own roots -- `B34`'s `vanishes at the horizons`"""
        return [sp.simplify(sp.Poly(self.cubic(), sp.Symbol('r')).eval(x))
                for x in self.triple(v)]

    def cubic(self):
        """the horizon cubic `r**3 - r + 2M` with `2M` at the designated offset, in `r`"""
        r = sp.Symbol('r')
        return sp.expand((r - self.triple(1)[0]) * (r - self.triple(1)[1])
                         * (r - self.triple(1)[2]))


class Omega:
    """`L-127`'s own `omega_power`, which carries its own converse by raising."""

    def __init__(self):
        g = graft(L127, 'omega_power', extra=('w',))
        self.omega_power, self.w = g['omega_power'], g['w']
        self.statements = (g['_STATEMENTS'], g['_OF'])

    def powers(self):
        return [self.omega_power(sp.simplify(self.w**k)) for k in range(3)]

    def is_pure_power(self, z):
        try:
            self.omega_power(z)
        except ValueError:
            return False
        return True

    def quantises(self):
        """every cube root is a pure power and the exponents exhaust `Z/3` -- `quantises`"""
        return sorted(self.powers()) == [0, 1, 2]


class Bead:
    """`bead_conjugate`'s own `r_of_tau`, at the proper times three rows name."""

    def __init__(self):
        g = graft(BEAD, 'r_of_tau', extra=('A',))
        self.r_of_tau, self.A = g['r_of_tau'], g['A']
        self.statements = (g['_STATEMENTS'], g['_OF'])

    def radius(self, t):
        return complex(self.r_of_tau(t)).real

    def branch_point_at_zero(self, tol=1e-15):
        """`r = 0` exactly at proper time zero -- the branch point the cosmology begins at"""
        return abs(self.radius(0.0)) <= tol

    def nonzero_away(self, ts=(0.25, 0.5, 1.0)):
        return all(abs(self.radius(t)) > 1e-6 for t in ts)


def at_inputs():
    return Splits(), Omega(), Bead()


def _selftest():
    S, O, B = at_inputs()
    print('  splits.py -- three modules grafted, each function called at the rows\' inputs')
    print(f"    L-012w {S.statements[0]}/{S.statements[1]}   "
          f"L-127 {O.statements[0]}/{O.statements[1]}   "
          f"bead_conjugate {B.statements[0]}/{B.statements[1]}")
    HINGE = ('1', '-1', '0')
    for v in HINGE:
        print(f"    roots_at({v:>3}): designated {S.designated(v)!s:>3}   "
              f"all three {[str(x) for x in S.triple(v)]}")
    print(f"    ** the root SET is the same at all three: {S.sets_agree(HINGE)}, and the "
          f"designations all differ: {S.designations_differ(HINGE)} **")
    assert S.sets_agree(HINGE) and S.designations_differ(HINGE)
    print(f"    the cubic at its own roots: {S.vanishes_at_roots('1')}")
    assert all(x == 0 for x in S.vanishes_at_roots('1'))
    print(f"    omega_power on the three cube roots: {O.powers()}   quantises: {O.quantises()}")
    print(f"    and it RAISES off them -- is_pure_power(2) = {O.is_pure_power(sp.Integer(2))}")
    assert O.quantises() and not O.is_pure_power(sp.Integer(2))
    print(f"    r_of_tau(0) = {B.radius(0.0)}  -> branch point at zero: "
          f"{B.branch_point_at_zero()}; nonzero away: {B.nonzero_away()}")
    assert B.branch_point_at_zero() and B.nonzero_away()
    print('  OK')
    return 0


if __name__ == '__main__':
    sys.exit(_selftest())
