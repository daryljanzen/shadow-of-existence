#!/usr/bin/env python3
"""
`r7283` ② BATCH SEVEN — **THE FIRST FOUR `EXTEND` ROWS, FOUR TAKEN, AND BOTH EXTENSIONS RETURN
MORE THAN THEIR CLAIM ASKED FOR.**

`EXTEND_PREDICTION.md` (digest pinned before any of the `12` was computed) split the class and
put these four first as the clean ones.  Two functions, four rows, **nothing held**.

  ⓵ `L129: close`        -> `B13`, `B6`, `B8`
  ⓶ `bead_contour: f`    -> `B36`

** ⛭⛭⛭ `B13` IS SETTLED BY `L129`'s OWN TWO GENERATOR SETS AND BY NO CHOICE OF MINE. **
`close(gam)` and `close(ratios + [P])` are both of order `27` and both of exponent `3` --
identical element-order multisets -- and are **NOT ISOMORPHIC**: `Z_3^3` abelian with `27`
conjugacy classes against `Delta(27)` with `11`.
  ⇒ *** `is not a second group resembling the substrate's own` is therefore exact rather than
  rhetorical: resemblance by order AND by exponent is not isomorphism. ***  ⌗ *And the test is
  not vacuously `different`: the same group from the generators in the other order fingerprints
  IDENTICALLY, so it can say `same` as well as `different`.*

** ⛭⛭ AND `bead_contour`'s `M2` IS EXACTLY `2/(3 sqrt 3)`, THE NARIAI VALUE, so the horizon is a
   DOUBLE root. **  `1/f` has a double pole and the tortoise integral diverges as `1/eps`, not as
`log(1/eps)`.
  ⌈ *** The extension returns a COEFFICIENT and not only a divergence: `eps * I -> -0.333337`
  against `2/f''(r_h) = -0.333341` in closed form, measured across four decades. ***  ⌊ ⌗ *`B36`
  asserts `infinite tortoise distance`; the DEGREE and the COEFFICIENT are what the extension
  adds to it.*

WHAT IS NOT CLAIMED.  ** Not that the fingerprint decides isomorphism in general ** -- it is a
sufficient test for NON-isomorphism, reported as that: two groups it separates are certainly
different, two it does not separate are not thereby the same.  ** Not that the degenerate horizon
is the generic case ** -- it is the Nariai member, which is where `bead_contour` is written; a
non-degenerate member diverges logarithmically instead, still infinite by a weaker power.  ** Not
that any pin moves. **

Run: python3 reach_b7.py            (writes REACHED_B7.tsv)
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import extensions as E                                             # noqa: E402

OUT = os.path.join(HERE, 'REACHED_B7.tsv')

B_ = 'receipts/L221_the_bridge/'
L129 = 'baryon_edge/L129_the_invariants.py'
BEAD_CONTOUR = 'bead_contour.py'


def _iso_detail():
    fd, fs = E.fingerprint('diag'), E.fingerprint('su')
    return (f'close(gam) gives order {fd[0]} with element orders {list(fd[1])}, '
            f'{len(fd[2])} conjugacy classes, abelian={fd[3]}; close(ratios+[P]) gives order '
            f'{fs[0]} with the SAME element orders {list(fs[1])} but {len(fs[2])} classes and '
            f'abelian={fs[3]} -- so they resemble each other by order and exponent and are NOT '
            f'isomorphic; and the test says SAME for the generators in the other order '
            f'({E.the_test_can_also_say_same()}), so it is not vacuously `different`')


def _centre_detail():
    return (f'the lap is {E.the_lap()}, unimodular ({E.lap_is_unimodular()}), and the centre of '
            f'the determinant-one part is the three scalars {E.centre("su")} -- so the lap lies '
            f'in it AND generates it, which makes `its centre` exact rather than an inclusion; '
            f'naming the hinge 3-cycle instead gives a subgroup of the same order THREE that is '
            f'not central at all ({E.the_three_cycle_is_the_centre()})')


def _tortoise_detail():
    M2, nar, al = E.nariai_value()
    v, d1, d2 = E.f_at_and_around_the_horizon()
    rows = E.divergence_coefficients()
    got, want = E.pole_coefficient()
    return (f'M2 = {M2:.10f} is exactly 2/(3 sqrt 3) = {nar:.10f}, the Nariai value, so at '
            f'r_h = {E.horizon_radius():.6f} both f = {v:.1e} and f\' = {d1:.1e} vanish while '
            f'f\'\' = {d2:.4f} -- a DOUBLE root. The integral runs '
            f'{", ".join(f"{i:.1f} at eps={e:g}" for e, i, _ in rows)}, growing as 1/eps, and '
            f'eps*I converges to {got:.6f} against 2/f\'\'(r_h) = {want:.6f}; over an interval '
            f'that reaches no root it is {E.tortoise(E.horizon_radius()+0.2, E.horizon_radius()+0.3):.6f}, finite')


# ⚠ ** EACH ROW CARRIES ONE PREDICATE AND TWO INPUTS, not two predicates. **  Four times now --
#   twice at batch five, twice in this file's first draft -- a converse was written as a TRUE
#   FACT ABOUT THE EDIT instead of THE CLAIM RE-EVALUATED UNDER IT.  Both are true sentences and
#   the polarity flips between them.  *** One function cannot disagree with itself, and the
#   guard below gates that both slots of a row ARE the same object. ***
ROWS = [
    (B_ + 'B13_po2_identification_is_stated.py',
     'is not a second group resembling the substrate\'s own', L129, 'close', 'EXTEND',
     E.groups_not_isomorphic, ('diag', 'su'),
     'ask the same of ONE group against itself, generated from the same generators in the other '
     'order, so the predicate must come back FALSE and is not vacuously `different`',
     ('su', 'su_other_order'), _iso_detail),

    (B_ + 'B6_the_object_is_delivered_and_the_row_argues_elsewhere.py',
     'whose determinant-one part is $\\Delta(27)$ and lies in $SU(3)$, with the lap as its '
     'centre', L129, 'close', 'EXTEND',
     E.generates_the_centre, E.the_lap(),
     'hand the same predicate the hinge 3-cycle instead of the lap -- an element of the same '
     'order three, which generates a subgroup that is not central at all',
     E.the_hinge_three_cycle(), _centre_detail),

    (B_ + 'B8_po4_targets_have_opposite_verdicts.py',
     'whose determinant-one part is $\\Delta(27)$ and lies in $SU(3)$, with the lap as its '
     'centre', L129, 'close', 'EXTEND',
     E.generates_the_centre, E.the_lap(),
     'hand the same predicate the hinge 3-cycle instead of the lap -- an element of the same '
     'order three, which generates a subgroup that is not central at all',
     E.the_hinge_three_cycle(), _centre_detail),

    (B_ + 'B36_two_of_three_crossings_are_supplied.py', 'infinite tortoise distance',
     BEAD_CONTOUR, 'f', 'EXTEND',
     E.tortoise_diverges, E.the_horizon(),
     'walk the same integral toward a point of the same kind that f does NOT vanish at, so the '
     'predicate comes back FALSE and `infinite` is seen to be about the ROOT and not the integral',
     E.a_point_that_is_not_a_root(), _tortoise_detail),
]

for _r in ROWS:
    _pred, _a, _b = _r[5], _r[6], _r[8]
    assert callable(_pred), _r[0]
    assert isinstance(_pred(_a), bool) and isinstance(_pred(_b), bool), (_r[0], _pred)
    assert type(_a) is type(_b), (_r[0], 'the two inputs must be the same KIND of object')


def main():
    print()
    print('  r7283 (2) batch seven -- the first 4 EXTEND rows, 4 taken, nothing held')
    print()
    bad, lines = [], [
        '# r7283 (2) BATCH SEVEN -- the first four EXTEND rows, all four TAKEN.  Per row: the',
        '# predicate computed through a short EXTENSION of the named function, and the',
        '# REACHABLE CONVERSE it comes back FALSE on.  B13 is settled by L129\'s own two',
        '# generator sets: two groups of order 27 and exponent 3 that are not isomorphic.',
        '# B36\'s horizon is a DOUBLE root because bead_contour sits at the Nariai value, so',
        '# the tortoise integral diverges as 1/eps with the coefficient 2/f\'\'(r_h).',
        '# Each row carries ONE predicate called at TWO inputs of the same kind, so a converse',
        '# cannot disagree with its claim about polarity.',
        '\t'.join(('stem', 'literal', 'module', 'function', 'code', 'claim', 'converse_edit',
                   'converse', 'computed'))]
    for stem, lit, mod, fn, code, pred, arg, cedit, carg, detail in ROWS:
        c, v = bool(pred(arg)), bool(pred(carg))
        d = detail()
        ok = c and not v
        if not ok:
            bad.append(stem)
        print(f"    {'OK  ' if ok else 'FAIL'}  {os.path.basename(stem)[:34]:<34} "
              f"{fn:<8} claim={c} converse={v}")
        print(f"            {d[:150]}")
        lines.append('\t'.join((stem, lit, mod, fn, code, 'TRUE' if c else 'FALSE', cedit,
                                'TRUE' if v else 'FALSE', d)))
    body = '\n'.join(lines) + '\n'
    open(OUT, 'w', encoding='utf-8').write(body)
    print()
    print(f'    REACHED_B7.tsv  {len(ROWS)} rows   '
          f'digest {hashlib.sha1(body.encode()).hexdigest()[:16]}')
    if bad:
        print(f'    {len(bad)} row(s) NOT reached')
        return 1
    print(f'    ** {len(ROWS)} taken, every predicate TRUE on the claim and FALSE on its '
          f'recorded converse. **')
    print('    ** AND B13 IS SETTLED BY L129\'s OWN TWO GENERATOR SETS: close(gam) and')
    print('       close(ratios+[P]) are both order 27 and both exponent 3 -- identical')
    print('       element-order multisets -- and NOT isomorphic, Z_3^3 abelian with 27 classes')
    print('       against Delta(27) with 11.  `Resembling` by order and exponent is not')
    print('       isomorphism, and no choice of mine supplies the counterexample. **')
    print('    ** AND bead_contour sits at EXACTLY the Nariai value 2/(3 sqrt 3), so its')
    print('       horizon is a DOUBLE root: the tortoise integral diverges as 1/eps rather')
    print('       than log(1/eps), with eps*I converging to 2/f\'\'(r_h) across four decades. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
