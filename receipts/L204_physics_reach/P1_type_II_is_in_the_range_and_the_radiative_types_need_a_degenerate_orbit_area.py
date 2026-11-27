#!/usr/bin/env python3
"""P1 -- which Petrov types the range holds, and what keeps the radiative types out.

** THE CLAIM. **  P9 fills each reachable symmetry class with the vacua its field equations admit
(in-class surjectivity), so the types in the range are the types those classes contain, not the
types a cut can take by inheriting the substrate's null rulings.

  * The inheritance fixes D or I.  The de Sitter surface is doubly ruled by straight null lines
    (P17); a cut that takes its principal null directions from the rulings takes both (two
    repeated PNDs, Type D) or neither (shear, Type I).
  * The class fixes the rest.  The stationary axisymmetric class, whose two Killing vectors act
    orthogonally transitively as a sweep requires, contains Type II vacua -- van Stockum's
    (Morisetti--Reina--Treves 1980, GRG 12, 619).  In its canonical form it contains no Type III or
    Type N vacuum (Hoffman 1969, Phys. Rev. 182, 1361; Morisetti--Reina--Treves); its only Type-N
    vacua are Hoffman's noncanonical solutions, on which the Killing orbits' area is constant
    (Hoffman 1969, J. Math. Phys. 10, 953).
  * So the range holds O, D, II and I.

** WHAT KEEPS THE RADIATIVE TYPES OUT, computed here. **  The vantage is read off the structure
function f = g(grad rho, grad rho), rho the square root of the Killing orbits' area: f > 0 reads
rho as a radius (the static face), f < 0 as a time (the cosmological face).  For the plane wave in
Rosen form the two commuting spacelike Killing vectors d_x, d_y have orbit area a(u) b(u), a
function of the retarded time alone, and f vanishes identically -- no vantage.  For the Gowdy form,
the reachable member of the same two-Killing class, f = -e^{-lambda}/(4t) < 0: a time.  And the
noncanonical stationary class has rho constant, so f = 0 there too.

WHAT IS NOT CLAIMED.  Not that types II--N fail to exist with symmetry: they do.  Not that every
two-Killing Lambda-vacuum is classified here: the class the sweep reaches is the orthogonally
transitive one, and the statement is about that class.
"""
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def pub(f):
    raw = open(os.path.join(ROOT, 'corpus', f), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def structure_function(g, coords, rho):
    gi = g.inv()
    grad = [sp.diff(rho, c) for c in coords]
    return sp.simplify(sum(gi[i, j] * grad[i] * grad[j]
                           for i in range(len(coords)) for j in range(len(coords))))


def _r7283():
    """The ruling computation, loaded from its module: both families straight, null, inherited."""
    import sys as _s
    _p = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7267_cc66_reach_the_71')
    if _p not in _s.path:
        _s.path.insert(0, _p)
    import flat_ruled_and_discrete as _F
    return _F


def _r7283b9():
    """The Weyl extension, loaded from its module: zero on the substrate, so the rulings carry no shear."""
    import sys as _s
    _p = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7267_cc66_reach_the_71')
    if _p not in _s.path:
        _s.path.insert(0, _p)
    import extensions_b9 as _Y
    return _Y


def main():
    print()
    print('  P1 -- the Petrov types of the range, and the degenerate orbit area at the wall')
    print()
    p0, p9 = pub('geometric_core_paper.tex'), pub('range_paper.tex')
    view = re.sub(r'\\(?:rcpt|cite)\{[^}]*\}', '', p9)
    view = re.sub(r'\\(?:emph|textit|textbf|texttt|mathrm)\{([^}]*)\}', r'\1', view)

    # the paper's statements
    check('P17 carries the double ruling: "doubly ruled by straight null lines"',
          'doubly ruled by straight null lines' in p0)
    check('P9: the members constructed are of types O, D and I, and type II is in the range as well',
          'The members constructed below are of types~O, D and~I, and type~II is in the range as well' in view)
    check('P9: what fixes the types is the class and not the inheritance',
          'What fixes the types is the class and not the inheritance' in view)
    check('P9: inheriting the rulings gives both (type D) or neither (type I)',
          'takes both, which is type~D, or neither, which is the shear of type~I' in view)
    check("P9: the stationary axisymmetric class contains type II vacua -- van Stockum's",
          "contains type~II vacua---van~Stockum's" in view)
    check('P9 cites Hoffman (both papers) and Morisetti--Reina--Treves for it',
          all(k in p9 for k in ('Hoffman1969a', 'Hoffman1969b', 'MorisettiReinaTreves1980')))
    check('P9 Proposition radiative lists types D and II among the non-radiative kernels',
          'types D and II ($I^{3}=27J^{2}$)' in p9)
    check('P9 abstract: types O, D, II and I are all in the range',
          'Petrov types O, D, II and I are all in the range' in p9)
    check('P9 wall: the plane wave\'s spacelike two-Killing subalgebra fails on the vantage',
          'what fails there is the vantage' in view)

    # the computation: f vanishes identically for the plane wave's spacelike G2
    u, v, x, y = sp.symbols('u v x y', real=True)
    a, b = sp.Function('a')(u), sp.Function('b')(u)
    g_pw = sp.Matrix([[0, -1, 0, 0], [-1, 0, 0, 0], [0, 0, a**2, 0], [0, 0, 0, b**2]])
    rho_pw = sp.sqrt(a * b)
    f_pw = structure_function(g_pw, (u, v, x, y), rho_pw)
    check('plane wave, Rosen form: the d_x, d_y orbit area a(u)b(u) has f = g(grad rho, grad rho) = 0',
          f_pw == 0)

    # contrast: the Gowdy form, same two-Killing class, f < 0
    t, th = sp.symbols('t theta', positive=True)
    lam, P = sp.Function('lam')(t, th), sp.Function('P')(t, th)
    g_gw = sp.diag(-sp.exp(lam), sp.exp(lam), t * sp.exp(P), t * sp.exp(-P))
    rho_gw = sp.sqrt(t)          # orbit area t e^P t e^-P = t^2, so rho^2 = t
    f_gw = structure_function(g_gw, (t, th, x, y), rho_gw)
    check('Gowdy form: orbit area t, f = -e^{-lam}/(4t) < 0 -- rho reads as a time',
          sp.simplify(f_gw + sp.exp(-lam) / (4 * t)) == 0)

    # contrast: the canonical stationary axisymmetric (Papapetrou) form, f > 0
    r_, z = sp.symbols('r z', positive=True)
    U, k, A = sp.Function('U')(r_, z), sp.Function('k')(r_, z), sp.Function('A')(r_, z)
    tt, ph = sp.symbols('tt ph', real=True)
    e2U = sp.exp(2 * U)
    g_pp = sp.zeros(4, 4)
    g_pp[0, 0] = -e2U
    g_pp[0, 1] = g_pp[1, 0] = -e2U * A
    g_pp[1, 1] = -e2U * A**2 + r_**2 / e2U
    g_pp[2, 2] = sp.exp(2 * k - 2 * U)
    g_pp[3, 3] = sp.exp(2 * k - 2 * U)
    det_killing = sp.simplify(-(g_pp[0, 0] * g_pp[1, 1] - g_pp[0, 1]**2))
    check('canonical stationary axisymmetric form: the Killing block has -det = r^2, so rho = r',
          sp.simplify(det_killing - r_**2) == 0)
    f_pp = structure_function(g_pp, (tt, ph, r_, z), r_)
    check('and f = e^{2U-2k} > 0 -- rho reads as a radius',
          sp.simplify(f_pp - sp.exp(2 * U - 2 * k)) == 0)

    # the inheritance, computed rather than cited
    _F = _r7283()
    check('COMPUTED: both ruling families lie on the quadric, are straight and NULL to better than 1e-12, '
          'and every line of both families meets each at-rest slice exactly once -- the cut takes both, '
          'which is type~D; a non-equilateral quadric breaks the nullity and slicing through the axis '
          'breaks the inheritance',
          _F.doubly_ruled_by_straight_null_lines()
          and _F.ruling_residuals(b=1.5)[2] > 1.0
          and _F.slicing_inherits_both_rulings(2, 0.5)
          and not _F.slicing_inherits_both_rulings(0, 0.5))
    _Y = _r7283b9()
    check("COMPUTED: the substrate's null rulings are shear-free -- the Weyl tensor vanishes in all 256 "
          "components on the substrate (and not on a plane wave), the substrate is Einstein, and the "
          "rulings are straight null lines, so by the Sachs equation no shear can grow on them",
          _Y.weyl_vanishes('substrate')
          and not _Y.weyl_vanishes('plane_wave')
          and _Y.substrate_is_einstein()
          and _Y.rulings_are_straight_null_lines())

    # the station's other items
    check("the field equations: P9 leaves GR's dynamics unchanged",
          'the construction leaves the dynamics of general relativity unchanged' in p9)
    check('the catalogue: Kerr, Zipoy--Voorhees, Gowdy, Einstein--Rosen, C-metric',
          all(k in p9 for k in ('Kerr', 'Zipoy', 'Gowdy', 'Einstein--Rosen', 'C-metric')))
    check('and the Carter constant, via the Type-D Killing tensor',
          'Carter' in p9 and 'Killing tensor' in p9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: the range holds types O, D, II and I.  Inheriting the double ruling gives D or I;')
    print('  the class supplies II (van Stockum).  Types III and N do not occur in the canonical')
    print('  stationary axisymmetric class, and where N occurs in a two-Killing class -- the noncanonical')
    print('  solutions, the plane wave -- the orbit area is degenerate, f vanishes, and there is no vantage.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
