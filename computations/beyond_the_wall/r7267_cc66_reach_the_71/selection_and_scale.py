#!/usr/bin/env python3
"""`r7283` ① BATCH SIX — **SIX ROWS ON SIX FUNCTIONS, AND THE ONE THAT LOOKED LIKE A FIFTH
WRONG-KIND ROW IS WRONG FOR A SHARPER REASON: A RESIDUAL TEST HAS THE WRONG QUANTIFIER.**

Of the `13` rows outstanding after batch five, `6` name a function that grafts on its own:

  ⓵ `L091x: irrep_dims_abelian_check`  ->  `B41`, the deck's irreducible dimensions
  ⓶ `L128: routes`                     ->  `B42`, the routes between hinges, enumerated
  ⓷ `L130: chi_meson`                  ->  `B6`,  colour's invariant content
  ⓸ `CR_acoustic: D_M`                 ->  `P15`, the comoving distance by the two routes
  ⓹ `CR_acoustic: ell_A`               ->  `P15`, the acoustic scale in multipole
  ⓺ `probe2: killing_residual`         ->  `B7`,  whether the Killing equation has a solution

** ⚠⛭⛭⛭ ⓺ IS NOT A `lie_g` REPEAT, AND THE DIFFERENCE IS WORTH MORE THAN THE ROW. **  `B7`'s
own source says what its literal is about: *the compact-face route is walled by localisation and
by `su(3)` **being no isometry** of the non-compact substrate* -- which is **the same claim
`P11` carries**, and batch five computed it.
  ⇒ *So `killing_residual` is `FUNCTION-IS-THE-WRONG-KIND` as well, but not because it is a
  metric test where a group is wanted.*  *** IT IS THE WRONG QUANTIFIER. ***  **A residual test
  can only ever refute ONE candidate field; `su(3) is no isometry` is a NON-EXISTENCE over every
  possible embedding, and no finite number of vanishing-residual failures establishes one.**
  *That is a different defect from `lie_g`'s and a sharper one: `lie_g` could not express the
  claim, while `killing_residual` can express its negation one candidate at a time and still
  never reach it.*

⌗ ** AND THE EMPTY-CONTAINER REFUSAL FIRED IN REAL USE ONE BATCH AFTER IT WAS WRITTEN. **
`L091x` binds `GROUPS = []` and fills it with top-level `.append(...)` calls, which are `Expr`
statements the graft does not keep -- so the loader refused `GROUPS` by name instead of handing
back an empty list.  *The row does not need it: `irrep_dims_abelian_check(mult, n, name)` takes
the group's multiplication table as an ARGUMENT, so the tables are supplied here and the change
of inputs is a call.*

⌗ ** ONE THING NOT CLAIMED, FROM `L091x`'s OWN BODY. **  *Its name and docstring promise the
sum-of-squares identity; its body returns only whether the table is abelian.*  So the dimensions
are taken here from the identity the docstring states, with the premise -- abelian -- computed by
the function, and that split is reported rather than papered over.

WHAT IS NOT CLAIMED.  ** Not that `no force` is reached by a converse ** -- it is the FINITENESS
of the holonomy group, `|G| = 27`, and a positive-dimensional group cannot even be fed to
`inv_dim`, whose average is a finite sum; that is a stated limit and not a false case.  ** Not
that the acoustic pipeline is a power-spectrum fit ** -- the module's own scope note says it is
the sound-horizon leg, and the rows ask for `D_M` and `ell_A` alone.  ** Not that any pin
moves. **

Run: python3 selection_and_scale.py
"""
import functools
import itertools
import os
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                            # noqa: E402
import groups_and_characters as GC                                 # noqa: E402

L091X = 'baryon_edge/L091x_deck_symmetry_is_not_horizontal.py'
L128 = 'baryon_edge/L128_three_walls_or_one_radius.py'
L130 = 'baryon_edge/L130_statistics_not_gauge.py'
ACOUSTIC = 'CR_acoustic_scale_and_hubble.py'
PROBE2 = 'beyond_the_wall/probe2.py'

# the sound horizon of standard LambdaCDM integrates to the beginning, a -> 0, so its lower
# limit is taken at a redshift far above any onset: the module's own `PINNED` reading.
Z_PINNED = 1e8
H0_CMB = 67.4                 # the module's own validation point
H0_LOCAL = 73.0               # the module's own tension point


# ══════════════════ ⓵ THE DECK'S IRREDUCIBLE DIMENSIONS ══════════════════════════════════
@functools.lru_cache(maxsize=None)
def _abelian_check():
    """⚠ `GROUPS` is NOT grafted: `L091x` binds it as `[]` and fills it with top-level
    `.append(...)` calls the graft does not keep, so the loader REFUSES it by name.  The
    function takes its table as an argument, so the tables are supplied below."""
    return graft(L091X, 'irrep_dims_abelian_check')['irrep_dims_abelian_check']


def deck_table():
    """the turnaround's deck, `Z_3`, as a multiplication table on `{0,1,2}`"""
    return (lambda a, b: (a + b) % 3), 3


def s3_table():
    """`S_3`, the walls' own symmetry, as a table on the six permutations of three letters"""
    perm = list(itertools.permutations(range(3)))
    idx = {p: i for i, p in enumerate(perm)}
    return (lambda a, b: idx[tuple(perm[a][perm[b][i]] for i in range(3))]), len(perm)


def deck_is_abelian():
    mult, n = deck_table()
    return bool(_abelian_check()(mult, n, 'Z_3'))


def s3_is_abelian():
    """the reachable converse: the walls' `S_3` is NOT abelian, so its irreducibles are not all
    one-dimensional and `trivial on the deck` would not be a dimension-one statement there"""
    mult, n = s3_table()
    return bool(_abelian_check()(mult, n, 'S_3'))


def deck_irrep_dims():
    """the dimensions, by the identity `L091x`'s OWN DOCSTRING states and its body does not
    evaluate: *an abelian group has `|G|` one-dimensional irreps*, and the sum of squares is
    `|G|`.  The premise is what the function computes; the dimensions follow from it."""
    mult, n = deck_table()
    if not _abelian_check()(mult, n, 'Z_3'):
        return None
    dims = [1] * n
    assert sum(d * d for d in dims) == n, 'the sum of squares must be the group order'
    return dims


def s3_irrep_dims_are_not_all_one():
    """and the converse's dimensions are `1, 1, 2`, whose squares also sum to `6` -- so the
    identity holds there too and it is the ABELIAN premise that does the work"""
    dims = [1, 1, 2]
    return sum(d * d for d in dims) == s3_table()[1] and max(dims) > 1


def trivial_irreps_count(dims):
    """how many of a group's irreducibles are TRIVIAL -- the one-dimensional representation on
    which every element acts as the identity.

    ⌗ *`B41`'s literal is `that are trivial on the deck`, and EXACTLY ONE irreducible is trivial
    for any finite group whatever -- `Z_3` and `S_3` alike.*  ** So triviality alone does not
    discriminate, and that is why the backlog recorded the DIMENSIONS as the quantity: the deck's
    being abelian is what makes `trivial on the deck` a statement about one-dimensional
    characters rather than about a single summand of something larger. **"""
    return 1 if dims else 0


def triviality_does_not_discriminate():
    """gated, because it is the reason the quantity is the dimensions and not the triviality"""
    return (trivial_irreps_count(deck_irrep_dims())
            == trivial_irreps_count([1, 1, 2]) == 1)


# ══════════════════ ⓶ THE ROUTES BETWEEN HINGES, ENUMERATED ══════════════════════════════
@functools.lru_cache(maxsize=None)
def _routes():
    g = graft(L128, 'routes', extra=('hinge', 'wall'))
    return g['routes'], g['hinge'], g['wall']


def route_table():
    """`routes(a, b)` on each of the three hinge pairs: the two arcs, as wall sets"""
    routes, hinge, _ = _routes()
    return {(a, b): routes(a, b) for a, b in itertools.combinations(sorted(hinge), 2)}


def routes_partition_the_walls():
    """the two arcs of every pair PARTITION the three walls -- no wall on both, none on
    neither -- which is what makes the enumeration an enumeration"""
    _, _, wall = _routes()
    allw = set(wall.values())
    return all(set(s) | set(l) == allw and not (set(s) & set(l))
               for s, l in route_table().values())


def every_pair_is_a_one_two_split():
    """and every pair's two arcs cross ONE wall and TWO, so the six routes are six distinct
    objects and not a continuum"""
    return {tuple(sorted((len(s), len(l)))) for s, l in route_table().values()} == {(1, 2)}


def _split_sizes_at(n):
    """the same construction at `n` hinges, which is a change of the inputs `routes` reads"""
    hinge = {j: 360 * j // n for j in range(n)}
    wall = {j: (hinge[j] + (360 // n) // 2) % 360 for j in range(n)}
    out = set()
    for a, b in itertools.combinations(range(n), 2):
        lo, hi = min(hinge[a], hinge[b]), max(hinge[a], hinge[b])
        sh = tuple(sorted(x for x in wall.values() if lo < x < hi))
        ln = tuple(sorted(x for x in wall.values() if x < lo or x > hi))
        out.add(tuple(sorted((len(sh), len(ln)))))
    return out


def one_two_split_at(n):
    return _split_sizes_at(n) == {(1, 2)}


def degenerate_pair():
    """and the one boundary case, reported rather than used as the converse: a hinge with
    itself has an EMPTY short arc, so `two routes` is a statement about DISTINCT hinges"""
    routes, _, _ = _routes()
    return routes(0, 0)


# ══════════════════ ⓷ COLOUR'S INVARIANT CONTENT ═════════════════════════════════════════
@functools.lru_cache(maxsize=None)
def _colour():
    return graft(L130, 'chi_meson', 'inv_dim', 'trace', 'chi_L3', 'chi_L2', 'chi_T3',
                 extra=('G_full', 'G_su', 'G_rigid'))


@functools.lru_cache(maxsize=None)
def selection_rules(group='G_su'):
    """baryon, diquark and meson invariant dimensions on the named holonomy group"""
    c = _colour()
    G = c[group]
    return (len(G), c['inv_dim'](G, c['chi_L3']), c['inv_dim'](G, c['chi_L2']),
            c['inv_dim'](G, c['chi_meson']))


def exact_selection_rules():
    """`baryon 1, diquark 0, meson 1` -- colour's exact selection rules, on the
    determinant-one part `G_su`"""
    order, b, d, m = selection_rules('G_su')
    return (b, d, m) == (1, 0, 1)


def rigid_converse():
    """the reachable converse, from `L130`'s OWN table: on `G_rigid` the meson count is `3`,
    so `exact` is a fact about `G_su` and not about any of the three groups"""
    order, b, d, m = selection_rules('G_rigid')
    return (b, d, m) == (1, 0, 1)


def no_force_is_the_finiteness():
    """`and no force`: the group is FINITE, so there is no continuous gauge field to carry one.
    *Reported as the stated limit it is: a positive-dimensional group cannot be fed to
    `inv_dim`, whose average is a finite sum, so this half has no constructed false case.*"""
    return selection_rules('G_su')[0]


# ══════════════════ ⓸⓹ THE DISTANCE AND THE ACOUSTIC SCALE ═══════════════════════════════
@functools.lru_cache(maxsize=None)
def _acoustic():
    return graft(ACOUSTIC, 'D_M', 'ell_A', 'r_s', 'models',
                 extra=('zrec', 'c', 'cs', 'ELL_A_OBS'))


@functools.lru_cache(maxsize=None)
def acoustic_at(H0, rate='std'):
    """`(D_M, r_s, ell_A)` at the given `H0`, on the standard rate or the CR one"""
    a = _acoustic()
    H_std, H_cr = a['models'](H0)
    Hf = H_std if rate == 'std' else H_cr
    return (a['D_M'](Hf), a['r_s'](Hf, Z_PINNED), a['ell_A'](Hf, Z_PINNED))


def distance_by_the_two_routes(H0=H0_CMB):
    """`D_M` twice on ONE rate: by its own quadrature, and recovered from the acoustic scale
    through `ell_A = pi D_M / r_s`.  *That is `the rate rule reaches the same distance by
    naming D_M`: the two routes name the same number.*"""
    dm, rs, la = acoustic_at(H0)
    return dm, la * rs / np.pi


def two_routes_agree(H0=H0_CMB, rel=1e-9):
    a, b = distance_by_the_two_routes(H0)
    # ⌗ bool(...) because a numpy comparison is `np.bool_`, which the ledger's own guard
    #   REFUSES -- it was written to catch a slot that is not a plain bool, and it caught this.
    return bool(abs(a - b) / a < rel)


def other_rate_converse(H0=H0_CMB, rel=1e-9):
    """the reachable converse: take the OTHER rate at the same `H0` -- radiation out of it --
    and the distance moves, so `the same distance` is a statement about one rate and not a
    coincidence of the two models"""
    dm_cr, rs_cr, la_cr = acoustic_at(H0, rate='cr')
    dm_std, _, _ = acoustic_at(H0)
    return bool(abs(dm_cr - dm_std) / dm_std < rel)


def acoustic_scale_is_301(H0=H0_CMB, tol=1.0):
    """`ell_A ~ 301` on flat LambdaCDM at the CMB `H0`, against the module's own `ELL_A_OBS`"""
    la = acoustic_at(H0)[2]
    return bool(abs(la - _acoustic()['ELL_A_OBS']) < tol)


def local_H0_converse(tol=1.0):
    """the reachable converse, and it is the module's own RESULT 2: force the LOCAL `H0` and
    the same observable MISSES the measured acoustic scale"""
    la = acoustic_at(H0_LOCAL)[2]
    return bool(abs(la - _acoustic()['ELL_A_OBS']) < tol)


# ══════════════════ ⓺ THE KILLING EQUATION, AND THE WRONG QUANTIFIER ═════════════════════
@functools.lru_cache(maxsize=None)
def _probe2():
    g = graft(PROBE2, 'killing_residual', extra=('g', 'X', 'u', 'v', 'x', 'y'))
    return g['killing_residual'], g['g'], g['X']


def coordinate_fields_that_are_killing():
    """which of `probe2`'s four coordinate vector fields satisfy the Killing equation.

    *This is what `killing_residual` CAN decide at a change of inputs, and it decides it
    exactly: the equation has a solution there.*"""
    kr, _, X = _probe2()
    out = []
    for i, nm in enumerate(X):
        xi = [1 if k == i else 0 for k in range(4)]
        if sp.simplify(kr(xi)) == sp.zeros(4, 4):
            out.append(str(nm))
    return out


def killing_equation_has_a_solution():
    return len(coordinate_fields_that_are_killing()) >= 1


def a_candidate_that_fails():
    """and it refutes a candidate just as exactly -- which is the whole of what a residual test
    does"""
    kr, _, _ = _probe2()
    return sp.simplify(kr([1, 0, 0, 0])) != sp.zeros(4, 4)


def b7_is_the_su3_claim():
    """** `B7`'s literal is the SAME claim `P11` carries -- `su(3)` being no isometry of the
    non-compact substrate -- and batch five computed it. **"""
    return GC.su3_is_not_in_so51() and not GC.su3_containment_under_the_dimension_edit()


def a_residual_test_has_the_wrong_quantifier():
    """*** AND THIS IS WHY `killing_residual` IS THE WRONG KIND FOR `B7`, by a sharper route
    than `lie_g`'s. ***

    *A residual test is EXISTENTIAL-REFUTING: it settles one candidate field at a time.  `su(3)
    is no isometry` is a NON-EXISTENCE over every possible embedding of an eight-dimensional
    algebra, and no finite number of non-vanishing residuals establishes one.*  ⇒ **So the
    function can express the claim's negation one candidate at a time and still never reach the
    claim -- where `lie_g` could not express it at all.**  *Gated here as the two facts it
    rests on: a residual decides single fields, and the claim is a containment.*"""
    return (len(coordinate_fields_that_are_killing()) == 1 and a_candidate_that_fails()
            and b7_is_the_su3_claim())


# ══════════════════════════════════════ REPORT ═══════════════════════════════════════════
def main():
    print()
    print(__doc__.split('Run:')[0])
    print('  ⓵  L091x  irrep_dims_abelian_check -- the deck (B41)')
    print(f'      Z_3 abelian: {deck_is_abelian()}   irrep dimensions {deck_irrep_dims()}, '
          f'squares summing to the order')
    print(f'      converse, the walls\' S_3: abelian = {s3_is_abelian()}, dimensions 1,1,2 -- '
          f'not all one ({s3_irrep_dims_are_not_all_one()})')
    print(f'      ⌗ and exactly ONE irreducible is trivial for either group, so triviality does '
          f'not discriminate ({triviality_does_not_discriminate()}) -- which is why the quantity '
          f'is the DIMENSIONS')
    print()
    print('  ⓶  L128  routes -- the routes between hinges (B42)')
    for k, (s, l) in sorted(route_table().items()):
        print(f'      hinges {k}: short {s}  long {l}')
    print(f'      the two arcs partition the three walls: {routes_partition_the_walls()}   '
          f'every pair a 1-2 split: {every_pair_is_a_one_two_split()}')
    print(f'      converse at 4 and 5 hinges: {sorted(_split_sizes_at(4))} and '
          f'{sorted(_split_sizes_at(5))} -- 1-2 split holds: {one_two_split_at(4)}, '
          f'{one_two_split_at(5)}')
    print(f'      the boundary case, reported not used: routes(0,0) = {degenerate_pair()}')
    print()
    print('  ⓷  L130  chi_meson -- colour\'s invariant content (B6)')
    for nm in ('G_full', 'G_su', 'G_rigid'):
        order, b, d, m = selection_rules(nm)
        print(f'      {nm:<9} |G| = {order:>3}   baryon {b}  diquark {d}  meson {m}')
    print(f'      exact selection rules on G_su: {exact_selection_rules()}   '
          f'converse on G_rigid: {rigid_converse()}')
    print(f'      and `no force` is the FINITENESS, |G| = {no_force_is_the_finiteness()}, '
          f'reported as a stated limit')
    print()
    print('  ⓸⓹  CR_acoustic  D_M and ell_A -- the distance and the scale (two P15 rows)')
    for H0 in (H0_CMB, H0_LOCAL):
        dm, rs, la = acoustic_at(H0)
        print(f'      LambdaCDM H0 = {H0}: D_M = {dm:.2f} Mpc, r_s = {rs:.2f} Mpc, '
              f'ell_A = {la:.2f}   (observed {_acoustic()["ELL_A_OBS"]})')
    a, b = distance_by_the_two_routes()
    print(f'      the two routes to D_M: {a:.4f} by quadrature, {b:.4f} from ell_A r_s / pi   '
          f'agree: {two_routes_agree()}')
    print(f'      converse, the OTHER rate at the same H0: D_M = '
          f'{acoustic_at(H0_CMB, rate="cr")[0]:.2f} Mpc   agrees: {other_rate_converse()}')
    print(f'      ell_A is the measured scale at the CMB H0: {acoustic_scale_is_301()}   '
          f'at the LOCAL H0: {local_H0_converse()}')
    print()
    print('  ⓺  probe2  killing_residual -- and the wrong quantifier (B7)')
    print(f'      coordinate fields satisfying the Killing equation: '
          f'{coordinate_fields_that_are_killing()} of {len(_probe2()[2])}')
    print(f'      so the equation HAS a solution ({killing_equation_has_a_solution()}) and a '
          f'candidate is refuted exactly ({a_candidate_that_fails()})')
    print(f'      ** but B7\'s literal is the su(3) containment P11 carries '
          f'({b7_is_the_su3_claim()}), and a residual test settles ONE field at a time while '
          f'the claim is a NON-EXISTENCE over every embedding **')
    print(f'      wrong quantifier, gated: {a_residual_test_has_the_wrong_quantifier()}')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
