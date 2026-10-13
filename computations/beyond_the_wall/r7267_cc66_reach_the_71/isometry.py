#!/usr/bin/env python3
"""
`r7267` ① BATCH TWO — THE INPUTS THE ISOMETRY ROWS NEED, HANDED TO `A2`'s OWN `lie_g`.

`r7261`'s backlog named `beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py: lie_g` as
the function nearest five rows across four receipts, with the gap `INPUTS`.  `lie_g(xi)` returns
the Lie derivative of the metric along `xi` -- the Killing test -- and it reads the METRIC and
the COORDINATES from module level, where `A2` has bound them to its own chiral plane wave.

⇒ ** SO THE CHANGE OF INPUTS IS A REBINDING AND NOT AN ARGUMENT: hand the grafted namespace a
   different `g` and `Xc`, and `A2`'s own Killing test answers about a different geometry. **
That is what `graft.py` returning the NAMESPACE rather than the function is for.

⚠ ** AND GETTING `A2`'s METRIC OUT AT ALL COST THE LOADER A REPAIR, which is worth recording
because it is `r7275`'s ruling ① one level down. **  `A2` builds its metric by ELEMENT
ASSIGNMENT -- `g = sp.zeros(4, 4)` then `g[0, 1] = g[1, 0] = 1` and three more.  The loader read
a subscript target as a BINDING, so it kept the last element assignment as the definition of
`g` and dropped the `sp.zeros` that creates it: the graft raised `NameError: name 'g' is not
defined`.  *** A matrix built by element assignment is a reachability question nobody had
asked, and several modules in this corpus build theirs that way. ***  Subscript and attribute
targets are now MUTATIONS, retained with the binding in source order.

WHAT IS NOT CLAIMED.  ** No claim that the generators below are complete ** -- they are six
whose Killing property is COMPUTED, which establishes the algebra's dimension as at least six
and its product structure; `A2`'s own method for counting an algebra exactly is a hand-derived
`ODE` system for its own metric and does not transport.  ** No claim about the geometry beyond
the static patch ** -- the chart is `-(1-chi^2) dtau^2 + dchi^2/(1-chi^2)` times the unit
two-sphere, and `chi = ±1` is its edge.
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                        # noqa: E402

MODULE = 'beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py'

TAU, CHI, THETA, PHI = sp.symbols('tau chi theta phi', real=True)


class Isometry:
    """`A2`'s own `lie_g`, with the metric and coordinates rebound to the row's geometry."""

    def __init__(self):
        g = graft(MODULE, 'lie_g', extra=('g', 'Xc'))
        self._g = g
        self.lie_g = g['lie_g']
        self.plane_wave = g['g']                 # what `A2` itself binds, kept for the converse
        self.statements = (g['_STATEMENTS'], g['_OF'])

    # ---- the rebinding, which is the change of inputs ------------------------------
    def at(self, metric, coords):
        self._g['g'], self._g['Xc'] = metric, list(coords)
        return self

    def nariai(self):
        """`dS_2 x S^2` with equal unit radii, static chart -- the `Nariai` member"""
        f = 1 - CHI**2
        return self.at(sp.diag(-f, 1 / f, sp.Integer(1), sp.sin(THETA)**2),
                       (TAU, CHI, THETA, PHI))

    def is_killing(self, xi):
        return sp.simplify(sp.expand_trig(sp.simplify(self.lie_g(list(xi))))) == sp.zeros(4, 4)

    # ---- the generators, DERIVED from the embedding rather than quoted -------------
    @staticmethod
    def so21_static():
        """the three `so(2,1)` generators of `dS_2` in the static chart.

        Derived, not quoted: `dS_2` is `-T^2+X^2+Y^2 = 1` with
        `T = sqrt(1-chi^2) sinh tau`, `X = sqrt(1-chi^2) cosh tau`, `Y = chi`.  Each ambient
        generator is pushed forward by solving TWO rows of `J xi = v` and VERIFYING the third."""
        s = sp.sqrt(1 - CHI**2)
        Z = sp.Matrix([s * sp.sinh(TAU), s * sp.cosh(TAU), CHI])
        J = Z.jacobian([TAU, CHI])
        amb = {'K_TX': sp.Matrix([Z[1], Z[0], 0]),
               'K_TY': sp.Matrix([Z[2], 0, Z[0]]),
               'J_XY': sp.Matrix([0, -Z[2], Z[1]])}
        a, b = sp.symbols('a b')
        out = {}
        for nm, v in amb.items():
            sol = sp.solve([sp.Eq((J * sp.Matrix([a, b]))[i], v[i]) for i in (0, 1)],
                           [a, b], dict=True)
            assert sol, f'{nm}: the first two rows do not determine the pushforward'
            xa = sp.simplify(sp.trigsimp(sol[0][a]))
            xb = sp.simplify(sp.trigsimp(sol[0][b]))
            third = sp.simplify(sp.trigsimp((J * sp.Matrix([xa, xb]))[2] - v[2]))
            assert third == 0, f'{nm}: the third embedding row does not verify ({third})'
            out[nm] = [xa, xb, 0, 0]
        return out

    @staticmethod
    def so3_sphere():
        """the three `so(3)` generators of the unit two-sphere, in `(theta, phi)`"""
        return {'L_z': [0, 0, 0, sp.Integer(1)],
                'L_x': [0, 0, sp.cos(PHI), -sp.cot(THETA) * sp.sin(PHI)],
                'L_y': [0, 0, -sp.sin(PHI), -sp.cot(THETA) * sp.cos(PHI)]}

    def generators(self):
        d = dict(self.so21_static())
        d.update(self.so3_sphere())
        return d

    @staticmethod
    def converses():
        """vector fields a reader might take for isometries and which are NOT -- the row's
        predicate must come back FALSE on these or it is an assertion"""
        return {'chi d_tau': [CHI, 0, 0, 0],
                'd_chi': [0, sp.Integer(1), 0, 0],
                'd_theta': [0, 0, sp.Integer(1), 0]}


def at_inputs():
    return Isometry()


def _selftest():
    I = at_inputs().nariai()
    print('  isometry.py -- A2 grafted, lie_g called at the Nariai metric')
    print(f"    grafted {I.statements[0]} of {I.statements[1]} top-level statements")
    gens = I.generators()
    for nm, xi in gens.items():
        print(f"    {nm:6} Killing: {I.is_killing(xi)}")
    assert all(I.is_killing(x) for x in gens.values())
    for nm, xi in I.converses().items():
        k = I.is_killing(xi)
        print(f"    converse {nm:10} Killing: {k}")
        assert not k
    print('    6 generators, 3 and 3 -- so(2,1) + so(3), dimension at least six, and three')
    print('    reachable converses come back FALSE.')
    return 0


if __name__ == '__main__':
    sys.exit(_selftest())
