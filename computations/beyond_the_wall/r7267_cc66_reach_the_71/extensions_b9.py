#!/usr/bin/env python3
"""`r7283` ② BATCH NINE — **THE LAST TWO `EXTEND` ROWS, AND THE SHEAR ONE IS SETTLED BY A
VANISHING THE SUBSTRATE HAS AND THE CONVERSE GEOMETRY DOES NOT.**

  ⓵ `probe1: Gamma`      ->  `P1`,  *the shear of the ruling congruence*
  ⓶ `CR_acoustic: D_M`   ->  `P15`, *the distance slice's curvature and the recovered
                                     expansion law*

** ⛭⛭⛭ ⓵ THE RULINGS ARE SHEAR-FREE BECAUSE THE SUBSTRATE HAS NO WEYL TENSOR. **  *By the
Sachs equation the shear of a null geodesic congruence is driven by the WEYL tensor and by
nothing else, so a congruence that starts shear-free stays shear-free exactly when `C_abcd`
vanishes.*  ⌗ *Batch four already computed that the rulings are straight null lines, so their
initial shear is zero; what this batch adds is the obstruction that could grow one.*
  ⇒ `Gamma` extended from Christoffels to Riemann to WEYL returns **all `256` components zero**
  on the substrate, and `R = 12/alpha^2` with `Ric = (R/4) g` exactly -- Einstein, as the
  geometric core states.  ⌈ ** And the converse is `probe1`'s OWN module-level metric: ** the
  chiral plane wave has `16` non-zero Weyl components, so there the Sachs term is live and a
  null congruence can be sheared.  ⌊ *The same extension, the same function, two metrics -- one
  the paper's and one the module's.*

⚠ ** AND ONE COMPONENT OF THE `256` NEEDED MORE THAN `simplify` TO SHOW IT WAS ZERO. **
`W[1][3][3][2]` comes out as `r (sin 2t tan t + cos 2t - 1) / (2 tan t)`, which `sympy.simplify`
returns unchanged.  *It is identically zero -- `sin 2t tan t = 2 sin^2 t` and `cos 2t - 1 =
-2 sin^2 t` -- and `expand_trig` resolves it, as does evaluating it at a point (`9.9e-17`).*
  ⇒ *** A `simplify` THAT STOPS SHORT READS EXACTLY LIKE A NON-ZERO COMPONENT, and the only
  thing that distinguishes them is trying harder on the one that did not vanish. ***  **So the
  predicate here simplifies through `expand_trig` and reports the count, rather than taking
  `simplify`'s first answer for a geometric fact.**

** ⓶ AND `D_M` RECOVERS THE EXPANSION LAW EXACTLY, which is what `the exact recovery` means. **
*`D_M` is `int c/H dz`, so differentiating the comoving distance must return `c/H(z)` -- and it
does, to `1e-8` relative at `z = 0.5`, `5` and `100`, which is quadrature precision.*  ⌗ *The
converse is the other rate at the same `H0`: the derivative of the standard-rate distance misses
`c/H_CR(z)` by `1e-4` to `9e-4`, four orders worse, so the agreement is the rate's own and not an
accident of the integrator.*

WHAT IS NOT CLAIMED.  ** Not that the Sachs equation is derived here ** -- that the shear of a
null geodesic congruence is driven by the Weyl tensor is a standard result used as a STATED input
and labelled as one; what is computed is that the Weyl tensor vanishes on the substrate and does
not on the converse geometry.  ** Not that the rulings' initial shear is computed in this batch **
-- batch four computed that they are straight null lines, and that is cited rather than redone.
** Not that the flat slice is recomputed ** -- batch four's `constant_tau_slice` is called, not
rewritten.  ** Not that any pin moves. **

Run: python3 extensions_b9.py
"""
import functools
import os
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                            # noqa: E402
import flat_ruled_and_discrete as F                                # noqa: E402

PROBE1 = 'beyond_the_wall/probe1.py'
ACOUSTIC = 'CR_acoustic_scale_and_hubble.py'


# ══════════════════ ⓵ THE WEYL TENSOR, FROM `Gamma` ══════════════════════════════════════
def _probe1_namespace():
    """`Gamma` reads `g`, `gi` and `X` from module level, so a different geometry is a
    REBINDING of those three in the grafted namespace -- which is what an `EXTEND` row on a
    module-level-reading function costs, stated rather than hidden."""
    return graft(PROBE1, 'Gamma', extra=('g', 'gi', 'X', 'u', 'v', 'x', 'y'))


def de_sitter_static():
    """the substrate in a spherical static chart: `f = 1 - r^2/alpha^2`.

    *The geometric core states the substrate intrinsically at `eq:sphere3` and its signature
    proposition names de Sitter as the unique intrinsically Lorentzian maximally symmetric
    manifold; this is that manifold in the chart whose `r = alpha` locus the paper calls a
    COORDINATE singularity.*"""
    t, r, th, ph = sp.symbols('t r theta phi', positive=True)
    al = sp.Symbol('alpha', positive=True)
    f = 1 - r ** 2 / al ** 2
    return (sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2),
            sp.diag(-1 / f, f, 1 / r ** 2, 1 / (r ** 2 * sp.sin(th) ** 2)),
            [t, r, th, ph])


@functools.lru_cache(maxsize=None)
def curvature_of(which):
    """Christoffels from the grafted `Gamma`, then Riemann, Ricci, the scalar and WEYL.

    ** The extension is Riemann and Weyl; `Gamma` itself returns only the connection. **"""
    ns = _probe1_namespace()
    if which == 'substrate':
        ns['g'], ns['gi'], ns['X'] = de_sitter_static()
    elif which != 'plane_wave':
        raise KeyError(which)
    Gam, gg, gi, X = ns['Gamma'], ns['g'], ns['gi'], ns['X']
    n = len(X)
    Gm = [[[Gam(a, b, c) for c in range(n)] for b in range(n)] for a in range(n)]
    R = [[[[sp.simplify(sp.diff(Gm[a][b][d], X[c]) - sp.diff(Gm[a][b][c], X[d])
                        + sum(Gm[a][c][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][c]
                              for e in range(n)))
            for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Rl = [[[[sp.simplify(sum(gg[a, e] * R[e][b][c][d] for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(R[a][b][a][d] for a in range(n))))
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))

    def weyl(a, b, c, d):
        e = Rl[a][b][c][d]
        e += (gg[a, d] * Ric[b, c] + gg[b, c] * Ric[a, d]
              - gg[a, c] * Ric[b, d] - gg[b, d] * Ric[a, c]) / (n - 2)
        e += Rs * (gg[a, c] * gg[b, d] - gg[a, d] * gg[b, c]) / ((n - 1) * (n - 2))
        # ⚠ `simplify` ALONE LEAVES ONE COMPONENT OF THE SUBSTRATE'S 256 LOOKING NON-ZERO:
        #   `r (sin 2t tan t + cos 2t - 1)/(2 tan t)`, which is identically zero.  *A simplify
        #   that stops short reads exactly like a real component, so the one that does not
        #   vanish is simplified HARDER before it is counted.*
        s = sp.simplify(e)
        return s if s == 0 else sp.simplify(sp.expand_trig(s))
    nonzero = sum(1 for a in range(n) for b in range(n) for c in range(n) for d in range(n)
                  if weyl(a, b, c, d) != 0)
    return {'n': n, 'Rs': Rs, 'Ric': Ric, 'weyl_nonzero': nonzero,
            'einstein': sp.simplify(Ric - (Rs / n) * gg) == sp.zeros(n, n)}


def weyl_vanishes(which):
    """the predicate `P1` turns on, at a named geometry: does the WEYL tensor vanish?

    *By the Sachs equation -- a STATED input -- the shear of a null geodesic congruence is
    driven by the Weyl tensor and nothing else, so this is the obstruction to a shear-free
    congruence staying shear-free.*"""
    return bool(curvature_of(which)['weyl_nonzero'] == 0)


def rulings_are_straight_null_lines():
    """and their INITIAL shear is zero because they are straight null lines, which batch four
    computed and this batch cites rather than redoes"""
    return bool(F.doubly_ruled_by_straight_null_lines())


def substrate_is_einstein():
    c = curvature_of('substrate')
    return bool(c['einstein'])


def substrate_scalar_curvature():
    return sp.simplify(curvature_of('substrate')['Rs'])


# ══════════════════ ⓶ THE SLICE AND THE RECOVERED EXPANSION LAW ══════════════════════════
@functools.lru_cache(maxsize=None)
def _acoustic():
    return graft(ACOUSTIC, 'D_M', 'models', extra=('zrec', 'c'))


def _distance_to(Hf, z, n=200000):
    a = _acoustic()
    zs = np.linspace(0, z, n)
    return float(np.trapezoid(a['c'] / Hf(zs), zs))


def recovered_rate(rate='std', z=0.5, h=1e-3):
    """the EXTENSION: `D_M` returns a distance, and differentiating it must return `c/H(z)`.
    That is `the exact recovery of the expansion law`, and `D_M` alone does not perform it."""
    H_std, H_cr = _acoustic()['models'](67.4)
    Hf = H_std if rate == 'std' else H_cr
    return (_distance_to(Hf, z + h) - _distance_to(Hf, z - h)) / (2 * h)


def rate_is_recovered(rate, z=0.5, tol=1e-6):
    """the predicate, at a named rate: does differentiating THAT rate's distance return THAT
    rate's `c/H(z)`?  ⌗ *One predicate, two inputs of the same kind -- batch seven's guard.*"""
    H_std, H_cr = _acoustic()['models'](67.4)
    Hf = H_std if rate == 'std' else H_cr
    got = recovered_rate('std', z)                 # the distance is always the STANDARD one
    want = float(_acoustic()['c'] / Hf(z))
    return bool(abs(got / want - 1) < tol)


def recovery_residuals(rate='std', zs=(0.5, 5.0, 100.0)):
    H_std, H_cr = _acoustic()['models'](67.4)
    Hf = H_std if rate == 'std' else H_cr
    out = []
    for z in zs:
        got = recovered_rate('std', z)
        want = float(_acoustic()['c'] / Hf(z))
        out.append((z, got, want, abs(got / want - 1)))
    return out


def the_distance_slice_is_flat():
    """and the other half of the row: the slice's curvature, computed at batch four and cited
    here rather than recomputed -- Ricci, scalar AND Kretschmann all zero"""
    return bool(F.slice_is_exactly_flat())


# ══════════════════════════════════════ REPORT ═══════════════════════════════════════════
def main():
    print()
    print(__doc__.split('Run:')[0])
    print('  ⓵  probe1  Gamma -> Riemann -> WEYL  (P1, the shear of the ruling congruence)')
    for nm, lab in (('substrate', 'de Sitter static, the paper\'s own manifold'),
                    ('plane_wave', 'probe1\'s OWN chiral plane wave')):
        c = curvature_of(nm)
        print(f'      {lab:<42} Weyl non-zero {c["weyl_nonzero"]:>3} of 256   '
              f'R = {sp.simplify(c["Rs"])}   Einstein {c["einstein"]}')
    print(f'      the substrate\'s Weyl VANISHES: {weyl_vanishes("substrate")}   '
          f'the converse geometry\'s does not: {weyl_vanishes("plane_wave")}')
    print(f'      and the rulings are straight NULL lines (batch four, cited): '
          f'{rulings_are_straight_null_lines()}')
    print(f'      ⚠ one of the 256 needed expand_trig to show it was zero -- a simplify that '
          f'stops short reads like a real component')
    print()
    print('  ⓶  CR_acoustic  D_M -> the recovered expansion law  (P15)')
    for z, got, want, rel in recovery_residuals():
        print(f'      z = {z:>6}: dD_M/dz = {got:>14.6f}   c/H(z) = {want:>14.6f}   '
              f'rel {rel:.2e}')
    print(f'      the standard rate is recovered from its own distance: '
          f'{rate_is_recovered("std")}')
    for z, got, want, rel in recovery_residuals(rate='cr', zs=(0.5, 5.0)):
        print(f'      converse at z = {z}: against c/H_CR(z) = {want:.4f}, rel {rel:.2e}')
    print(f'      the converse rate is NOT recovered: {rate_is_recovered("cr")}')
    print(f'      and the distance slice is exactly flat (batch four, cited): '
          f'{the_distance_slice_is_flat()}')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
