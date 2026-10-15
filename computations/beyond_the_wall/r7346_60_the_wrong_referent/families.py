#!/usr/bin/env python3
"""r7346+60 -- THE TWO FAMILIES, EACH COMPUTED FROM ITS OWN METRIC.

** WHY THIS RUNS AT ALL, GIVEN THE ORDER SAYS `do not re-derive it`. **  `r7341` ① settles the
polynomial and this file does not re-settle it.  *What it establishes is a DIFFERENT fact the order
does not contain: `S10` names `diag(-2 sigma, sigma, sigma)` with the invariant `6 sigma^2`, which is
`71`'s family and not `Q1`'s, and asserts `Q1`'s polynomial beside it.*  ⇒ ** So `71` did not supply
an arbitrary family.  It used the one `S10` HANDED it, and the `-48 H sigma^3` term it reported is
exactly what that family gives. **  The defect is a WRONG referent, not an absent one.

⌗ ** Both families are computed with `L549/Q1`'s OWN curvature routines, imported from its file, so
nothing here is a second implementation of the thing the order says not to re-derive. **

** COMPUTES: ** `Weyl^2` and `sigma_ab sigma^ab` for the two Bianchi~I shear families -- `Q1`'s
PLANAR one, rates `(1, 1+sigma, 1-sigma)`, and `71`'s AXISYMMETRIC one, rates
`(H-2 sigma, H+sigma, H+sigma)` (corrected r7350 on `r7349` ③) -- the
involution that forces one of them to be even in `sigma`, and the normalisation that reconciles them.
No paper quantity.
"""
import importlib.util
import os

import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))
Q1 = os.path.join(ROOT, 'receipts', 'L549_coupled_counterterms',
                  'Q1_the_degeneracy_is_conformal_flatness_not_maximal_symmetry_so_no_scale_factor'
                  '_can_break_it.py')

#: the two shear eigenvalue triples, as each source states them
TRIPLES = {'Q1': (0, 1, -1), 'S10-as-written': (-2, 1, 1)}


def q1_module():
    """`L549/Q1` itself -- its top level is imports and definitions, so importing runs no checks"""
    spec = importlib.util.spec_from_file_location('L549_Q1', Q1)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def metric(triple, t, sig):
    """a Bianchi~I metric: isotropic expansion `H = 1` plus a trace-free shear.

    ** Either family, and only the triple differs -- which is why neither this helper nor its callers
    may call the result axisymmetric: `(0, s, -s)` is PLANAR, all three rates differing, and only
    `(-2s, s, s)` is axisymmetric. **
    """
    return sp.diag(-1, *[sp.exp(2 * (t + c * sig * t)) for c in triple])


def weyl(triple, mod, t, sig, x):
    Rs, ric2, riem2 = mod.invariants(metric(triple, t, sig), x)
    return sp.simplify(sp.expand(mod.weyl_sq(Rs, ric2, riem2)))


def shear_invariant(triple, sig):
    return sp.simplify(sum((c * sig) ** 2 for c in triple))


if __name__ == '__main__':
    mod = q1_module()
    t = sp.Symbol('t', real=True)
    sig = sp.Symbol('sigma', real=True)
    x = [t] + list(sp.symbols('x y z', real=True))
    print()
    print('  r7346+60 -- THE TWO FAMILIES, FROM THEIR METRICS')
    print()
    out = {}
    for name, tri in TRIPLES.items():
        C2 = weyl(tri, mod, t, sig, x)
        inv = shear_invariant(tri, sig)
        out[name] = (C2, inv)
        print(f'    {name:16s} eigenvalues {tri}  trace {sum(tri)}')
        print(f'                     sigma_ab sigma^ab = {inv}')
        print(f'                     Weyl^2            = {sp.factor(C2)}')
        print(f'                     even in sigma?    = '
              f'{sp.simplify(C2.subs(sig, -sig) - C2) == 0}')
    print()
    print(f'    Q1\'s polynomial on S10\'s named family: '
          f'{sp.simplify(out["S10-as-written"][0] - sig**2*(4 + sp.Rational(16, 3)*sig**2)) == 0}')
    print(f'    leading coefficients at H = 1: '
          f'{[sp.simplify(sp.series(out[k][0], sig, 0, 3).removeO()/sig**2) for k in TRIPLES]}')
    print(f'    ratio of the shear invariants: '
          f'{sp.simplify(out["S10-as-written"][1]/out["Q1"][1])}')
    print()
    #: the involution: on (0, sigma, -sigma) the relabelling y <-> z carries the family to itself, so
    #: no odd power of sigma can appear.  ** That is a SYMMETRY and not a claim that could have been
    #: wrong -- which is why the even polynomial was never in doubt and the referent always was. **
    gQ = metric(TRIPLES['Q1'], t, sig)
    swapped = sp.diag(gQ[0, 0], gQ[1, 1], gQ[3, 3], gQ[2, 2])
    print(f'    the involution, Q1 family: g(sigma -> -sigma) is g with y,z swapped = '
          f'{sp.simplify(gQ.subs(sig, -sig) - swapped) == sp.zeros(4, 4)}')
    g71 = metric(TRIPLES['S10-as-written'], t, sig)
    print('    and the same relabelling on S10\'s named family: '
          f'{[sp.simplify(g71.subs(sig, -sig) - sp.diag(g71[0, 0], *p)) == sp.zeros(4, 4) for p in ((g71[1, 1], g71[2, 2], g71[3, 3]), (g71[1, 1], g71[3, 3], g71[2, 2]), (g71[2, 2], g71[1, 1], g71[3, 3]), (g71[2, 2], g71[3, 3], g71[1, 1]), (g71[3, 3], g71[1, 1], g71[2, 2]), (g71[3, 3], g71[2, 2], g71[1, 1]))].count(True)} of 6 permutations')
    print()
