#!/usr/bin/env python3
"""
`r7267` ① — THE INPUTS THE `L221` ROWS NEED, HANDED TO `L-129`'s OWN FUNCTIONS.

`r7261`'s backlog named `baryon_edge/L129_the_invariants.py` as the module nearest to eleven
rows across seven receipts of the bridge prefix, with the gap `INPUTS` on four of its
functions -- `close`, `det`, `inv_dim`, `chi_VVV`.  ** This supplies the inputs and nothing
else: it builds no mathematics of its own. **  Every number a caller gets back comes out of a
function grafted from `L-129`, called here at generators the rows name rather than at the
ones `L-129`'s own report happens to print.

  `gens_full`   the three wall monodromies and the hinge 3-cycle  ->  `close` -> the order
  `gens_su`     the monodromy RATIOS and the hinge 3-cycle        ->  `close` -> the det-one part
  `stab(...)`   a stabiliser of a real structure in `S_3`          ->  `close` -> its order
  `chi_VVV`, `chi_VVbar`                                          ->  `inv_dim` -> the invariants

⚠ ** THE CALLER MAKES THE CALL. **  What comes back from `at_inputs()` is the grafted function
itself and the generators to hand it, not a precomputed answer -- so a receipt that uses this
is a receipt that calls `L-129`'s `close` on `L-129`'s own monomial representation, which is
what `INPUTS` meant.

WHAT IS NOT CLAIMED.  ** No claim that `L-129` is reimplemented here ** -- it is grafted, and
a drift in `L-129` moves every number a caller reads.  ** No claim about epsilon's invariance
beyond what the grafted `mat` computes ** -- that check costs five seconds and is behind
`eps_moved_by()`, not in the constructor.
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                        # noqa: E402

MODULE = 'baryon_edge/L129_the_invariants.py'
_FUNCS = ('close', 'det', 'inv_dim', 'chi_VVV', 'chi_VVbar', 'mul', 'trace', 'mat', 'sgn', 'W')


class Holonomy:
    """`L-129`'s functions, plus the generators the `L221` rows name.  Nothing computed eagerly."""

    def __init__(self, lam=1):
        g = graft(MODULE, *_FUNCS, extra=('ID', 'CYC'))
        self._g = g
        for nm in _FUNCS:
            setattr(self, nm, g[nm])
        self.ID, self.CYC = g['ID'], g['CYC']
        self.ident = (self.ID, (0, 0, 0))
        # a wall monodromy is diagonal, omega^(-lam) in its own slot -- `L-128`'s inputs
        self.gamma = [(self.ID, tuple((-lam) % 3 if i == c else 0 for i in range(3)))
                      for c in range(3)]
        self.P = (self.CYC, (0, 0, 0))                          # the hinge 3-cycle
        self.gens_full = self.gamma + [self.P]
        self.gens_su = [self.mul(self.gamma[a], self.inverse(self.gamma[b]))
                        for a, b in ((0, 1), (1, 2))] + [self.P]
        self.grafted = g['_GRAFTED']
        self.statements = (g['_STATEMENTS'], g['_OF'])

    def inverse(self, x):
        s, d = x
        si = tuple(s.index(i) for i in range(3))
        return (si, tuple((-d[s.index(i)]) % 3 for i in range(3)))

    # ---- the S_3 inputs B2's row needs: a stabiliser of a real structure -------------
    def perm(self, s):
        return (tuple(s), (0, 0, 0))

    def stab_gens(self, real_roots):
        """generators of the subgroup of `S_3` preserving a partition of the three roots into
        `real_roots` real ones and the rest a conjugate pair.  Over-critically all three roots
        are real and the whole of `S_3` acts; over-critically one is real and only the swap of
        the pair does."""
        rest = [i for i in range(3) if i not in real_roots]
        gens = []
        if len(rest) == 2:
            a, b = rest
            s = list(range(3))
            s[a], s[b] = s[b], s[a]
            gens.append(self.perm(s))
        if len(real_roots) == 3:
            gens.append(self.perm((1, 0, 2)))
            gens.append(self.P)
        return gens

    # ---- the derived objects, each one call of a grafted function --------------------
    def group(self, gens):
        return self.close(gens)

    def det_one(self, G):
        import sympy as sp
        return [x for x in G if sp.simplify(self.det(x) - 1) == 0]

    def centre(self, G):
        return [x for x in G if all(self.mul(x, y) == self.mul(y, x) for y in G)]

    def is_abelian(self, G):
        return all(self.mul(x, y) == self.mul(y, x) for x in G for y in G)

    def dets(self, G):
        import sympy as sp
        return sorted({str(sp.nsimplify(sp.simplify(self.det(x)))) for x in G})

    def eps(self):
        import sympy as sp
        e = sp.zeros(27, 1)
        for pm in itertools.permutations(range(3)):
            e[pm[0] * 9 + pm[1] * 3 + pm[2]] = self.sgn(pm)
        return e

    def rep3(self, x):
        import sympy as sp
        M = self.mat(x)
        return sp.Matrix(sp.kronecker_product(M, M, M))

    def eps_moved_by(self, G):
        """how many elements of `G` move epsilon.  FIVE SECONDS -- call it deliberately."""
        import sympy as sp
        e = self.eps()
        z = sp.zeros(27, 1)
        return [x for x in G if sp.simplify(sp.expand_complex(self.rep3(x) * e - e)) != z]


def at_inputs(lam=1):
    return Holonomy(lam)


def _selftest():
    h = at_inputs()
    print('  holonomy.py -- L-129 grafted, called at the rows\' inputs')
    print(f"    grafted {h.statements[0]} of {h.statements[1]} top-level statements")
    Gf, Gs = h.group(h.gens_full), h.group(h.gens_su)
    print(f"    |<gamma_0,gamma_1,gamma_2,P>| = {len(Gf)}   dets {h.dets(Gf)}")
    print(f"    |<ratios,P>|                 = {len(Gs)}   dets {h.dets(Gs)}")
    d1 = h.det_one(Gf)
    print(f"    det-one part of the full group: {len(d1)}   == <ratios,P>: {set(d1) == set(Gs)}")
    print(f"    its centre: {len(h.centre(Gs))}   abelian: {h.is_abelian(Gs)}")
    print(f"    inv_dim(full, chi_VVbar)  = {h.inv_dim(Gf, h.chi_VVbar)}")
    print(f"    inv_dim(su,   chi_VVbar)  = {h.inv_dim(Gs, h.chi_VVbar)}")
    print(f"    inv_dim(full, chi_VVV)    = {h.inv_dim(Gf, h.chi_VVV)}")
    print(f"    inv_dim(su,   chi_VVV)    = {h.inv_dim(Gs, h.chi_VVV)}")
    print(f"    |stab(3 real roots)| = {len(h.group(h.stab_gens((0, 1, 2))))}  "
          f"|stab(1 real root)| = {len(h.group(h.stab_gens((0,))))}")
    return 0


if __name__ == '__main__':
    sys.exit(_selftest())
