#!/usr/bin/env python3
"""`r7283` ① BATCH FOUR — **FOUR FUNCTIONS AT NEW INPUTS, AND A HAZARD THE LOADER WAS SILENT
ABOUT UNTIL THIS BATCH FOUND IT.**

Nine of the remaining `27` `INPUTS` rows are reached here, on four `(module, function)` pairs
the syntax tree put together:

  ⓵ `L128b`'s `diag_at` — the holonomy of the vantage bundle, for `B29` and `B44`.
  ⓶ `L50b`'s `key_of` and `apply` — the horn swap as a map of the six ends and its
     discreteness, for `B38` and `B41`; and where a root transposition sends a hinge, for `B13`.
  ⓷ `r7111`'s `curvature` — the constant-`tau` slice and the invariants at the seam, for the
     two `P15` rows.
  ⓸ `panelA_reassign`'s `ruling` — the two ruling families and what a slicing inherits, for
     the two `P1` rows.

** THE HAZARD, WHICH IS WHY `graft.py` MOVED THIS BATCH. **  Both `L50b` and `L128b` bind a
table as an EMPTY container at top level — `ends = {}`, `leg_wall = {}` — and fill it in a
`for` loop, which is not a graftable statement kind.  *The loader handed back an EMPTY dict
and nothing said so*, so a row taken through `ends` would have been VACUOUS rather than wrong,
which is the worse of the two failures because it passes.  `graft.py` now REFUSES that case by
name.  ⌗ And the measurement that says not to build the capability instead: **of all `30`
remaining rows, the named function grafts on its own in `27` and the other `3` fail on a
different cause entirely — NOT ONE of the `30` needs a filled container.**  The six ends are
rebuilt here from the module's own `theta`, `A` and `sq3`, and GATED on the module's own
substrate equation rather than asserted.

** AND ONE PREDICATE SHARPENED BY ITS OWN CONVERSE. **  `The constant-tau slice is exactly
flat` read off the scalar curvature alone would PASS on the Schwarzschild spatial slice, whose
`Rs` is `0` and whose Kretschmann is `6 r_s^2/r^6`.  *A row checked on `Rs` would have been
checked on a quantity that does not distinguish flat from Ricci-flat*, so the predicate here
reads the Kretschmann invariant and the converse is recorded as the slice that exposes it.

Run: python3 flat_ruled_and_discrete.py
"""
import functools
import os
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                            # noqa: E402

L128B = 'baryon_edge/L128b_leg_and_arc.py'
L50B = 'baryon_edge/L50b_three_hinges_six_ends.py'
GEOM = 'beyond_the_wall/r7111_70_layer_geometry_audit/geometry.py'
PANELA = 'synthesis_figure/panelA_reassign.py'


# ══════════════════════════ ⓵ `diag_at` — IS THE VANTAGE BUNDLE FLAT ══════════════════════
@functools.lru_cache(maxsize=None)
def _monodromies():
    g = graft(L128B, 'diag_at', extra=('w', 'I3'))
    return g['diag_at'], g['w'], g['I3']


def plaquette(subst=None):
    """the holonomy of the smallest closed PLAQUETTE: round wall 0, round wall 1, back round
    wall 0, back round wall 1.

    *This is the lattice form of curvature and the only form flatness has when the connection
    is given by monodromies: the plaquette is the identity exactly when going round two walls
    in either order lands in the same place, so the holonomy of a loop is a function of its
    winding numbers and of NOTHING else about the path.*  `subst` replaces wall `0`'s
    monodromy, which is how the converse is reached."""
    diag_at, _, I3 = _monodromies()
    a = diag_at(0, 1) if subst is None else subst
    b = diag_at(1, 1)
    return sp.simplify(a * b * a.inv() * b.inv())


def holonomy(windings):
    """the holonomy of a loop with the given winding number about each of the three walls"""
    diag_at, _, I3 = _monodromies()
    M = I3
    for c, L in enumerate(windings):
        M = sp.simplify(diag_at(c, L) * M)
    return M


def bundle_is_flat():
    """flat iff the plaquette is the identity AND the zero-winding class is the identity"""
    _, _, I3 = _monodromies()
    return plaquette() == I3 and holonomy((0, 0, 0)) == I3


def flat_is_not_trivial():
    """and the predicate is not vacuous: a winding-ONE loop has NON-identity holonomy"""
    _, _, I3 = _monodromies()
    return holonomy((1, 0, 0)) != I3


def nonabelian_converse():
    """the converse edit: give wall 0 a non-diagonal monodromy OF THE SAME ORDER 3, as a
    non-abelian vantage bundle would have.  The plaquette is then not the identity, so the
    holonomy is path-dependent and the bundle is NOT flat."""
    _, _, I3 = _monodromies()
    cyc = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    assert sp.simplify(cyc ** 3) == I3, 'the converse monodromy must have the same order'
    return plaquette(subst=cyc) == I3                       # FALSE is the point


# ══════════════════════ ⓶ `key_of` AND `apply` — THE SIX ENDS AND DISCRETENESS ═════════════
@functools.lru_cache(maxsize=None)
def _ends_and_group():
    g = graft(L50B, 'key_of', 'apply',
              extra=('C', 'S', 'T', 'theta', 'stations', 'A', 'sq3'))
    return g


@functools.lru_cache(maxsize=None)
def six_ends():
    """the six ends rebuilt by `L50b`'s OWN formula from its OWN grafted `theta`, `A`, `sq3`.

    ** `ends` ITSELF CANNOT BE GRAFTED: the module binds it as `{}` and fills it in a `for`
    loop, and `graft.py` now refuses that rather than handing back an empty dict. **  So the
    table is rebuilt, and `ends_are_on_the_substrate` GATES the rebuild on the module's own
    defining equation instead of trusting the transcription."""
    g = _ends_and_group()
    theta, A, sq3 = g['theta'], g['A'], g['sq3']
    return {f'{e}{k}': sp.Matrix([x0 * A, 2 * A * sp.cos(theta[k]), 2 * A * sp.sin(theta[k])])
            for k in g['stations'] for e, x0 in (('U', sq3), ('D', -sq3))}


def ends_are_on_the_substrate():
    """the gate on the rebuild: every end satisfies -X0^2 + X1^2 + X2^2 = A^2 exactly"""
    g = _ends_and_group()
    A = g['A']
    return all(sp.simplify(-V[0] ** 2 + V[1] ** 2 + V[2] ** 2 - A ** 2) == 0
               for V in six_ends().values())


@functools.lru_cache(maxsize=None)
def horn_swap_on_ends():
    """the horn swap T as a map of the six ends, keyed by `key_of` and applied by `apply`"""
    g = _ends_and_group()
    key_of, ap, T = g['key_of'], g['apply'], g['T']
    ends = six_ends()
    inv = {key_of(V): k for k, V in ends.items()}
    return {k: inv[key_of(ap(T, V))] for k, V in ends.items()}


def swap_is_three_two_cycles():
    """and it is a fixed-point-free involution whose three 2-cycles each join the two ends of
    ONE hinge -- which is what `a map of the six ends` means for a horn swap"""
    p = horn_swap_on_ends()
    return (all(p[p[k]] == k for k in p) and all(p[k] != k for k in p)
            and all(p[k][1:] == k[1:] for k in p))


@functools.lru_cache(maxsize=None)
def group_order_under_key_of():
    """the order of the group the three generators close to, decided by `key_of`'s keying"""
    g = _ends_and_group()
    key_of = g['key_of']
    G = {key_of(sp.eye(3)): sp.eye(3)}
    frontier = [sp.eye(3)]
    while frontier:
        nxt = []
        for M in frontier:
            for gen in (g['C'], g['S'], g['T']):
                N = sp.simplify(gen * M)
                k = key_of(N)
                if k not in G:
                    G[k] = N
                    nxt.append(N)
        frontier = nxt
    return len(G)


def horn_swap_order():
    """the horn swap's own order: `2`, so it is DISCRETE and not a one-parameter motion"""
    g = _ends_and_group()
    key_of, T = g['key_of'], g['T']
    return len({key_of(sp.eye(3)), key_of(T)})


def _rot(a):
    return sp.Matrix([[1, 0, 0],
                      [0, sp.cos(a), -sp.sin(a)],
                      [0, sp.sin(a), sp.cos(a)]])


@functools.lru_cache(maxsize=None)
def continuous_converse(steps=12):
    """the converse edit for `discrete`: feed `key_of` a ONE-PARAMETER rotation instead of the
    swap.  Its powers key to `steps` DISTINCT elements and never close, so the keying that
    makes the horn swap discrete says the rotation is not."""
    g = _ends_and_group()
    key_of = g['key_of']
    return len({key_of(sp.simplify(_rot(sp.Integer(1)) ** n)) for n in range(1, steps + 1)})


@functools.lru_cache(maxsize=None)
def transposition_hop(n_stations=3):
    """where the root transposition S sends each hinge, at `n_stations` stations.

    *`S` is `X2 -> -X2`, the transposition of two of the three roots.  `theta` is built FROM
    `stations`, so changing the number of stations is a change of INPUTS and nothing else.*"""
    g = _ends_and_group()
    key_of, ap, S, A = g['key_of'], g['apply'], g['S'], g['A']
    th = {k: 2 * sp.pi * k / n_stations for k in range(n_stations)}
    pos = {k: sp.Matrix([0, 2 * A * sp.cos(th[k]), 2 * A * sp.sin(th[k])]) for k in th}
    inv = {key_of(V): k for k, V in pos.items()}
    sent = {k: inv.get(key_of(ap(S, V))) for k, V in pos.items()}
    hop = {k: None if v is None else min((v - k) % n_stations, (k - v) % n_stations)
           for k, v in sent.items()}
    return sent, hop


def every_moved_hinge_is_a_neighbour(n_stations=3):
    _, hop = transposition_hop(n_stations)
    return all(v in (0, 1) for v in hop.values())


# ══════════════════════════ ⓷ `curvature` — THE SLICE AND THE SEAM ════════════════════════
@functools.lru_cache(maxsize=None)
def _curv():
    return graft(GEOM, 'curvature')['curvature']


@functools.lru_cache(maxsize=None)
def constant_tau_slice():
    """the intrinsic curvature of the constant-`tau` slice of `r7111`'s OWN metric.

    *`r7111` builds `g = diag(-1, (dr/dchi)^2, r^2, r^2 sin^2 th)` with `r` the paper's
    `eq:scalefac`.  Its constant-`tau` slice is the lower 3x3 block at fixed `tau`, which is a
    change of INPUTS to `curvature` and not an extension of it.*"""
    g = graft(GEOM, 'curvature', extra=('r', 'tau', 'chi', 'th', 'ph'))
    r, chi, th = g['r'], g['chi'], g['th']
    h = sp.diag(sp.diff(r, chi) ** 2, r ** 2, r ** 2 * sp.sin(th) ** 2)
    return g['curvature'](h, [chi, th, g['ph']])


def slice_is_exactly_flat():
    """exactly flat means the KRETSCHMANN invariant vanishes, not just the scalar -- see
    `ricci_flat_converse`, which is why this reads `K` and not `Rs`"""
    C = constant_tau_slice()
    return (sp.simplify(C['K']) == 0 and sp.simplify(C['Rs']) == 0
            and sp.simplify(C['Ric']) == sp.zeros(3, 3))


def slice_christoffels_nonzero():
    """and the flatness is not a coordinate accident: the connection is NOT zero"""
    C = constant_tau_slice()
    return sum(1 for a in range(3) for b in range(3) for c in range(3)
               if sp.simplify(C['Gm'][a][b][c]) != 0)


@functools.lru_cache(maxsize=None)
def sphere_converse():
    """converse ⒜: the at-rest `S^3` slice the corpus's own panel A draws.  `Rs = 6`."""
    chi, th, ph = sp.symbols('chi theta phi', real=True)
    s3 = sp.diag(1, sp.sin(chi) ** 2, sp.sin(chi) ** 2 * sp.sin(th) ** 2)
    return sp.simplify(_curv()(s3, [chi, th, ph])['Rs'])


@functools.lru_cache(maxsize=None)
def ricci_flat_converse():
    """converse ⒝, and the sharper one: the SCHWARZSCHILD spatial slice.  Its scalar curvature
    is `0` and its Kretschmann is `6 r_s^2/r^6`, so a predicate reading `Rs` would call it
    flat.  ** THIS IS WHY THE PREDICATE READS `K`. **"""
    r, rs = sp.symbols('r r_s', positive=True)
    th, ph = sp.symbols('theta phi', real=True)
    f = 1 - rs / r
    C = _curv()(sp.diag(1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2), [r, th, ph])
    return sp.simplify(C['Rs']), sp.simplify(C['K'])


@functools.lru_cache(maxsize=None)
def seam_invariants():
    """the curvature invariants of the static `SdS` exterior, as a function of radius"""
    t, r = sp.symbols('t r', positive=True)
    th, ph = sp.symbols('theta phi', real=True)
    rs, al = sp.symbols('r_s alpha', positive=True)
    f = 1 - rs / r - r ** 2 / al ** 2
    C = _curv()(sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2), [t, r, th, ph])
    return sp.simplify(C['K']), sp.simplify(C['Rs']), (r, rs, al, f)


@functools.lru_cache(maxsize=None)
def seam_is_finite_and_the_origin_is_not():
    """the seam is a ROOT of `f` at finite positive radius, where `K` is finite; at `r -> 0`
    the same invariant diverges.  That is `finite-curvature horizon seam, never a curvature
    singularity`, computed rather than asserted."""
    K, Rs, (r, rs, al, f) = seam_invariants()
    num = {rs: sp.Rational(1, 10), al: 1}
    # the seam is a root of f.  `f = 0` and `r*f = 0` have the same roots away from the
    # origin, and `r*f` is a CUBIC, whose roots are taken numerically rather than as radicals.
    cubic = sp.Poly(sp.expand(r * f.subs(num)), r)
    seam = min(float(sp.re(z)) for z in cubic.nroots()
               if abs(sp.im(z)) < 1e-12 and sp.re(z) > 0)
    at_seam = float(K.subs(num).subs(r, sp.nsimplify(seam, rational=True)))
    at_zero = sp.limit(K.subs(num), r, 0, '+')
    return seam, at_seam, at_zero


# ══════════════════════════ ⓸ `ruling` — THE TWO FAMILIES AND THE SLICING ═════════════════
@functools.lru_cache(maxsize=None)
def _ruling():
    g = graft(PANELA, 'ruling', extra=('t', 'zmax'))
    return g['ruling'], g['t']


_PHIS = np.linspace(0, 2 * np.pi, 10)[:-1]


@functools.lru_cache(maxsize=None)
def ruling_residuals(b=1.0):
    """for both families and nine azimuths: how far off the quadric the line lies, how far
    from straight its tangent is, and the Minkowski norm of that tangent.

    `b` scales the second axis.  ** `panelA_reassign`'s own docstring says `a=b=alpha => null
    rulings = light cone`, so `b != 1` is the converse the module itself names. **"""
    ruling, t = _ruling()
    onq = straight = 0.0
    norms = []
    for s in (+1, -1):
        for ph in _PHIS:
            x, y, z = ruling(ph, s)
            y = b * y
            onq = max(onq, float(np.abs(x ** 2 + (y / b) ** 2 - z ** 2 - 1).max()))
            d = np.diff(np.stack([x, y, z]), axis=1) / np.diff(t)
            straight = max(straight, float(np.abs(d - d[:, :1]).max()))
            norms.append(float(d[0, 0] ** 2 + d[1, 0] ** 2 - d[2, 0] ** 2))
    return onq, straight, max(abs(n) for n in norms)


def doubly_ruled_by_straight_null_lines(tol=1e-12):
    onq, straight, norm = ruling_residuals()
    return onq < tol and straight < tol and norm < tol


@functools.lru_cache(maxsize=None)
def crossings_per_line(coord, c):
    """how many times each line of each family meets the slice `coord = c`"""
    ruling, t = _ruling()
    out = []
    for s in (+1, -1):
        for ph in _PHIS:
            v = np.stack(ruling(ph, s))[coord]
            out.append(int(np.sum(np.abs(np.diff(np.sign(v - c))) > 0)))
    return out


def slicing_inherits_both_rulings(coord=2, c=0.0):
    """a slicing inherits both rulings iff EVERY line of BOTH families meets each slice exactly
    once, so each family descends to a congruence through every point of the slice"""
    return set(crossings_per_line(coord, c)) == {1}


# ══════════════════════════════════════ REPORT ════════════════════════════════════════════
def main():
    print()
    print(__doc__.split('Run:')[0])
    print('  ⓵  L128b  diag_at -- the vantage bundle (B29, B44)')
    _, w, I3 = _monodromies()
    print(f'      plaquette round walls 0 and 1, both ways: '
          f'{"I" if plaquette() == I3 else "NOT I"}   flat: {bundle_is_flat()}')
    print(f'      winding-one holonomy is NOT the identity: {flat_is_not_trivial()}   '
          f'(so flat is not trivial)')
    print(f'      converse, wall 0 given a non-diagonal monodromy of the same order 3: '
          f'plaquette = I is {nonabelian_converse()}')
    print()
    print('  ⓶  L50b  key_of + apply -- the six ends, the swap, the hop (B38, B41, B13)')
    print(f'      the six ends rebuilt and GATED on -X0^2+X1^2+X2^2 = A^2: '
          f'{ends_are_on_the_substrate()}')
    print(f'      the horn swap on the six ends: {horn_swap_on_ends()}')
    print(f'      three 2-cycles, each joining ONE hinge\'s two ends: '
          f'{swap_is_three_two_cycles()}')
    print(f'      order of the swap: {horn_swap_order()}   order of the group it sits in: '
          f'{group_order_under_key_of()}   -> discrete')
    print(f'      converse, a one-parameter rotation keyed the same way: '
          f'{continuous_converse()} distinct keys in 12 steps, no closure')
    for n in (3, 5):
        sent, hop = transposition_hop(n)
        print(f'      the root transposition at {n} stations sends {sent}, hop {hop}   '
              f'every moved hinge a neighbour: {every_moved_hinge_is_a_neighbour(n)}')
    print()
    print('  ⓷  r7111  curvature -- the slice and the seam (two P15 rows)')
    C = constant_tau_slice()
    print(f'      constant-tau slice of r7111\'s own metric: Ric = 0, Rs = '
          f'{sp.simplify(C["Rs"])}, Kretschmann = {sp.simplify(C["K"])}')
    print(f'      exactly flat: {slice_is_exactly_flat()}   with '
          f'{slice_christoffels_nonzero()} of 27 Christoffels NON-zero')
    rs_, k_ = ricci_flat_converse()
    print(f'      converse ⒜ the at-rest S^3 slice: Rs = {sphere_converse()}')
    print(f'      converse ⒝ the Schwarzschild spatial slice: Rs = {rs_}, K = {k_}  '
          f'-- Rs alone would have PASSED it')
    K, Rs, _ = seam_invariants()
    seam, at_seam, at_zero = seam_is_finite_and_the_origin_is_not()
    print(f'      SdS exterior: K = {K}   Rs = {Rs}')
    print(f'      at the horizon seam r = {seam}: K = {at_seam}   '
          f'at r -> 0: K -> {at_zero}')
    print()
    print('  ⓸  panelA_reassign  ruling -- the two families and the slicing (two P1 rows)')
    onq, straight, norm = ruling_residuals()
    print(f'      both families, nine azimuths: off-quadric {onq:.1e}, off-straight '
          f'{straight:.1e}, |tangent norm| {norm:.1e}')
    print(f'      doubly ruled by straight NULL lines: '
          f'{doubly_ruled_by_straight_null_lines()}')
    _, _, nb = ruling_residuals(b=1.5)
    print(f'      converse, the non-equilateral quadric b = 1.5 the module\'s own docstring '
          f'names: |tangent norm| = {nb:.4f}')
    for co, nm in ((2, 'z = const, the at-rest S^3 slicing'),
                   (0, 'x = const, a slicing by planes through the axis')):
        n = crossings_per_line(co, 0.5)
        print(f'      {nm:<46} crossings {min(n)}..{max(n)}   inherits both: '
              f'{slicing_inherits_both_rulings(co, 0.5)}')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
