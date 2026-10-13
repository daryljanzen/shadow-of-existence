#!/usr/bin/env python3
"""`r7283` ② BATCH SEVEN — **THE FIRST FOUR `EXTEND` ROWS, AND BOTH EXTENSIONS RETURN MORE THAN
THE CLAIM ASKED FOR.**

`EXTEND` means *a short extension of the named function*.  Two functions carry four rows:

  ⓵ `L129: close` -> `B13` (*whether two generated groups are isomorphic*), `B6` and `B8`
     (*the centre of the determinant-one part*)
  ⓶ `bead_contour: f` -> `B36` (*the tortoise integral of `1/f` to the horizon*)

** ⛭⛭⛭ ⓵ AND THE CORPUS'S OWN GENERATORS SUPPLY THE EXACT PAIR `B13` NEEDS. **  `close(gam)` and
`close(ratios + [P])` are BOTH of order `27` and BOTH of exponent `3` -- identical element-order
multisets, `1` identity and `26` elements of order three -- and they are **NOT ISOMORPHIC**: the
first is abelian `Z_3^3` with `27` conjugacy classes, the second is `Delta(27)` with `11`.
  ⇒ *** So `is not a second group resembling the substrate's own` is exact: resemblance by order
  AND by exponent is not isomorphism, and no choice of mine supplies the counterexample --
  `L129`'s own two generator sets do. ***

** ⛭⛭ ⓶ AND `M2` IS EXACTLY `2/(3 sqrt 3)`, SO THE HORIZON IS A DOUBLE ROOT. **  `bead_contour`
is written at the Nariai value, where the two horizons have merged -- so `1/f` has a DOUBLE pole
and the tortoise integral diverges as `1/eps` rather than as `log(1/eps)`.
  ⌈ *** And the divergence carries an exact coefficient rather than only a sign: ***
  `eps * I -> 2/f''(r_h) = -1/3`, measured at four decades of `eps` and matching
  `f''(1/sqrt3) = -6` in closed form.  ⌊ ⌗ *`infinite tortoise distance` is the claim; the DEGREE
  and the COEFFICIENT are what the extension adds.*

WHAT IS NOT CLAIMED.  ** Not that the degenerate horizon is the generic case ** -- it is the
Nariai member, which is where `bead_contour` is written, and a non-degenerate member would
diverge logarithmically instead: still infinite, by a weaker power.  ** Not that the
fingerprint decides isomorphism in general ** -- it is a sufficient test for NON-isomorphism, and
it is reported as that: two groups it separates are certainly different, two it does not separate
are not thereby the same.  ** Not that any pin moves. **

Run: python3 extensions.py
"""
import functools
import os
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                            # noqa: E402

L129 = 'baryon_edge/L129_the_invariants.py'
BEAD_CONTOUR = 'bead_contour.py'
IDENT = ((0, 1, 2), (0, 0, 0))


# ══════════════════ ⓵ TWO GENERATED GROUPS, AND WHETHER THEY ARE ISOMORPHIC ══════════════
@functools.lru_cache(maxsize=None)
def _groups():
    return graft(L129, 'close', 'mul', 'det', 'mat',
                 extra=('gam', 'Pgen', 'ratios', 'G_full', 'G_su', 'ID', 'CYC'))


@functools.lru_cache(maxsize=None)
def generated(which):
    """a group `close` generates, from `L129`'s OWN generator sets and no others"""
    g = _groups()
    if which == 'diag':
        return tuple(g['close'](g['gam']))                     # the three wall monodromies
    if which == 'su':
        return tuple(g['G_su'])                                # the ratios with the 3-cycle
    if which == 'full':
        return tuple(g['G_full'])
    if which == 'su_other_order':
        return tuple(g['close'](list(g['ratios'])[::-1] + [g['Pgen']]))
    raise KeyError(which)


def _order_of(x):
    mul = _groups()['mul']
    y, n = x, 1
    while y != IDENT:
        y = mul(y, x)
        n += 1
        if n > 1000:
            raise ValueError('not of finite order')
    return n


def _inverse(h, G):
    mul = _groups()['mul']
    for k in G:
        if mul(h, k) == IDENT:
            return k
    raise KeyError('no inverse in the group')


@functools.lru_cache(maxsize=None)
def fingerprint(which):
    """`(order, element-order multiset, conjugacy-class sizes, abelian?)`.

    ** A SUFFICIENT TEST FOR NON-ISOMORPHISM AND NOTHING MORE. **  *Two groups it separates are
    certainly different; two it does not separate are not thereby the same, and that is reported
    rather than glossed.*"""
    G = generated(which)
    mul = _groups()['mul']
    orders = tuple(sorted(Counter(_order_of(x) for x in G).items()))
    classes, seen = [], set()
    for x in G:
        if x in seen:
            continue
        orb = frozenset(mul(mul(h, x), _inverse(h, G)) for h in G)
        classes.append(len(orb))
        seen |= set(orb)
    abelian = all(mul(a, b) == mul(b, a) for a in G for b in G)
    return len(G), orders, tuple(sorted(classes)), abelian


def same_order_and_exponent(a, b):
    """the two groups AGREE on order and on element orders -- the `resembling` half"""
    fa, fb = fingerprint(a), fingerprint(b)
    return fa[0] == fb[0] and fa[1] == fb[1]


def not_isomorphic(a, b):
    """and they DISAGREE on the conjugacy-class sizes, so they are not isomorphic"""
    fa, fb = fingerprint(a), fingerprint(b)
    return fa[2] != fb[2] or fa[3] != fb[3]


def the_resembling_pair_is_not_isomorphic():
    """`B13`: `close(gam)` and `close(ratios + [P])` resemble each other by order AND exponent
    and are NOT isomorphic"""
    return same_order_and_exponent('diag', 'su') and not_isomorphic('diag', 'su')


def the_test_can_also_say_same():
    """and the test is not vacuously `different`: the same group from the generators in the
    other order fingerprints IDENTICALLY"""
    return fingerprint('su') == fingerprint('su_other_order')


# ══════════════════ THE CENTRE OF THE DETERMINANT-ONE PART ═══════════════════════════════
@functools.lru_cache(maxsize=None)
def centre(which):
    G = generated(which)
    mul = _groups()['mul']
    return tuple(z for z in G if all(mul(z, x) == mul(x, z) for x in G))


@functools.lru_cache(maxsize=None)
def the_lap():
    """the equatorial lap: the product of the three wall monodromies, in `L129`'s own
    presentation"""
    g = _groups()
    gam, mul = g['gam'], g['mul']
    return mul(mul(gam[0], gam[1]), gam[2])


def lap_is_the_centre():
    """`B6` and `B8`: `with the lap as its centre` -- the lap lies in the centre of the
    determinant-one part AND GENERATES it, so `its centre` is exact and not an inclusion"""
    g = _groups()
    c = centre('su')
    return (the_lap() in c and len(c) == 3
            and tuple(g['close']([the_lap()])) == tuple(sorted(c)))


def lap_is_unimodular():
    import sympy as sp
    return sp.simplify(_groups()['det'](the_lap()) - 1) == 0


def the_three_cycle_is_the_centre():
    """the reachable converse: name the hinge 3-cycle as the centre instead of the lap.  It
    generates a subgroup of the same ORDER THREE and is not central at all."""
    g = _groups()
    P = g['Pgen']
    sub = tuple(g['close']([P]))
    return len(sub) == 3 and tuple(sorted(sub)) == tuple(sorted(centre('su')))


# ══════════════════ ⓶ THE TORTOISE INTEGRAL TO THE HORIZON ═══════════════════════════════
@functools.lru_cache(maxsize=None)
def _contour():
    g = graft(BEAD_CONTOUR, 'f', extra=('M2', 'al'))
    return g['f'], g['M2'], g['al']


def nariai_value():
    """`bead_contour`'s own `M2` against `2/(3 sqrt 3)`, the value at which the two horizons
    merge -- which is WHY the pole below is double"""
    _, M2, al = _contour()
    return M2, 2.0 / (3.0 * 3.0 ** 0.5), al


def is_at_the_nariai_value(tol=1e-12):
    M2, nar, _ = nariai_value()
    return bool(abs(M2 - nar) < tol)


def horizon_radius():
    """the merged horizon, `1/sqrt(3)` in units of `alpha`"""
    _, _, al = _contour()
    return al / 3.0 ** 0.5


def f_at_and_around_the_horizon(h=1e-6):
    """`f`, and its first and second derivatives, at the horizon -- a DOUBLE root has `f` and
    `f'` both zero and `f''` not"""
    f, _, _ = _contour()
    rh = horizon_radius()
    return (float(f(rh)), float((f(rh + h) - f(rh - h)) / (2 * h)),
            float((f(rh + h) - 2 * f(rh) + f(rh - h)) / h ** 2))


def horizon_is_a_double_root(tol=1e-8):
    v, d1, d2 = f_at_and_around_the_horizon()
    return bool(abs(v) < tol and abs(d1) < 1e-5 and abs(d2) > 1.0)


def tortoise(a, b, n=2000000):
    """the tortoise integral `int dr / f` over `[a, b]`, which is the extension: `f` alone
    returns a value, and the row asks for its integral"""
    f, _, _ = _contour()
    r = np.linspace(a, b, n)
    return float(np.trapezoid(1.0 / f(r), r))


def divergence_coefficients(eps=(1e-2, 1e-3, 1e-4, 1e-5)):
    """`eps * I(eps)` as `eps` shrinks.  At a DOUBLE pole this tends to a constant; at a simple
    pole it would tend to zero, because the integral would only grow like `log(1/eps)`."""
    rh = horizon_radius()
    return [(e, tortoise(rh + e, rh + 0.1), e * tortoise(rh + e, rh + 0.1)) for e in eps]


def tortoise_distance_is_infinite():
    """`B36`: the magnitude grows without bound as the horizon is approached, and the growth is
    the `1/eps` of a double pole"""
    rows = divergence_coefficients()
    mags = [abs(i) for _, i, _ in rows]
    return bool(all(b > 3 * a for a, b in zip(mags, mags[1:])))


def pole_coefficient():
    """and the coefficient it converges to, against `2/f''(r_h)` in closed form"""
    rows = divergence_coefficients()
    _, _, d2 = f_at_and_around_the_horizon()
    return rows[-1][2], 2.0 / d2


def coefficient_matches_the_closed_form(tol=1e-3):
    got, want = pole_coefficient()
    return bool(abs(got - want) < tol)


def away_from_the_root_it_is_finite():
    """the reachable converse: the same integral over an interval that does not reach a root of
    `f` is finite, so `infinite` is a statement about the APPROACH and not about the integral"""
    rh = horizon_radius()
    return bool(abs(tortoise(rh + 0.2, rh + 0.3)) < 10.0)



# ══ ⒞ ONE PREDICATE PER ROW, CALLED AT TWO INPUTS -- AND THE REASON IS A MISTAKE I HAVE NOW
#      MADE FOUR TIMES. ══════════════════════════════════════════════════════════════════
#  ⚠ Twice at batch five and twice again here, a converse was written as a TRUE FACT ABOUT THE
#    EDIT (`the integral away from the root is finite`) instead of as THE CLAIM RE-EVALUATED
#    UNDER THE EDIT (`is the integral infinite THERE?`).  Both readings are true sentences;
#    only the second is what a converse is, and the polarity flips between them.
#  ⇒ *** The fix is structural rather than careful: ONE predicate per row, called at the claim's
#    inputs and at the edit's.  A single function cannot disagree with itself about polarity,
#    and `reach_b7` gates that both slots of a row ARE the same object. ***

def groups_not_isomorphic(pair):
    """the predicate `B13` turns on, at a PAIR of `L129`-generated groups"""
    a, b = pair
    return bool(not_isomorphic(a, b))


def generates_the_centre(element):
    """the predicate `B6` and `B8` turn on, at one group element: does it lie in the centre of
    the determinant-one part AND generate it?"""
    g = _groups()
    c = centre('su')
    return bool(element in c and len(c) == 3
                and tuple(g['close']([element])) == tuple(sorted(c)))


def the_hinge_three_cycle():
    return _groups()['Pgen']


def tortoise_diverges(point, width=0.1):
    """the predicate `B36` turns on, at the POINT the lower limit is walked toward: does
    `int dr/f` grow without bound as the limit closes on `point` from above?

    ⚠ ** THE FIRST VERSION OF THIS TOOK AN `(offset, width)` INTERVAL AND WAS WRONG, not in its
    polarity but in its geometry: it shrank the OFFSET, so the `away` interval walked toward the
    horizon too and diverged as well. **  *A predicate is only one predicate if both its inputs
    are the same KIND of object, and `an interval 0.2 from the horizon` was not the same kind of
    object as `an interval at the horizon`.  The point approached is.*"""
    mags = [abs(tortoise(point + e, point + width)) for e in (1e-2, 1e-3, 1e-4)]
    return bool(all(b > 3 * a for a, b in zip(mags, mags[1:])))


def the_horizon():
    """the double root itself -- a root of `f`"""
    return horizon_radius()


def a_point_that_is_not_a_root():
    """and the converse's input: a point of the same kind, which `f` does not vanish at"""
    return horizon_radius() + 0.2

# ══════════════════════════════════════ REPORT ═══════════════════════════════════════════
def main():
    print()
    print(__doc__.split('Run:')[0])
    print('  ⓵  L129  close -- two generated groups, and the centre (B13, B6, B8)')
    for nm, lab in (('diag', 'close(gam)        = Z_3^3'),
                    ('su', 'close(ratios+[P]) = Delta(27)'),
                    ('full', 'close(gam+[P])     = Gamma_full')):
        o, orders, cls, ab = fingerprint(nm)
        print(f'      {lab:<32} |G| = {o:<3} element orders {list(orders)}  '
              f'{len(cls)} classes  abelian={ab}')
    print(f'      the two of order 27 agree on order AND exponent: '
          f'{same_order_and_exponent("diag", "su")}   and are NOT isomorphic: '
          f'{not_isomorphic("diag", "su")}')
    print(f'      and the test can also say SAME -- the generators in the other order: '
          f'{the_test_can_also_say_same()}')
    print(f'      the lap = {the_lap()}, unimodular: {lap_is_unimodular()}')
    print(f'      centre(Delta(27)) = {centre("su")}')
    print(f'      the lap IS the centre and GENERATES it: {lap_is_the_centre()}   '
          f'converse, the 3-cycle instead: {the_three_cycle_is_the_centre()}')
    print()
    print('  ⓶  bead_contour  f -- the tortoise integral to the horizon (B36)')
    M2, nar, al = nariai_value()
    print(f'      M2 = {M2:.16f}   2/(3 sqrt 3) = {nar:.16f}   at the Nariai value: '
          f'{is_at_the_nariai_value()}')
    v, d1, d2 = f_at_and_around_the_horizon()
    print(f'      at r_h = {horizon_radius():.6f}: f = {v:.3e}, f\' = {d1:.3e}, f\'\' = {d2:.6f}'
          f'   -> a DOUBLE root: {horizon_is_a_double_root()}')
    for e, i, ei in divergence_coefficients():
        print(f'      eps = {e:<8g} integral = {i:>14.3f}   eps*I = {ei:.6f}')
    got, want = pole_coefficient()
    print(f'      the coefficient converges to {got:.6f} against 2/f\'\'(r_h) = {want:.6f}   '
          f'match: {coefficient_matches_the_closed_form()}')
    print(f'      infinite tortoise distance: {tortoise_distance_is_infinite()}   '
          f'converse, away from the root it is finite: {away_from_the_root_it_is_finite()}')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
