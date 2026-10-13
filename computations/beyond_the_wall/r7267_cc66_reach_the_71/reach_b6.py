#!/usr/bin/env python3
"""
`r7283` ① BATCH SIX — **SIX ROWS, SIX TAKEN. FIVE ARE ORDINARY `INPUTS` ROWS AND THE SIXTH IS
WRONG-KIND FOR A SHARPER REASON THAN BATCH FIVE'S FOUR: A RESIDUAL TEST HAS THE WRONG
QUANTIFIER.**

Of the `13` rows outstanding after batch five, these `6` name a function that grafts on its own:

  ⓵ `L091x: irrep_dims_abelian_check` -> `B41`   ⓸ `CR_acoustic: D_M`   -> `P15` (rate rule)
  ⓶ `L128: routes`                    -> `B42`   ⓹ `CR_acoustic: ell_A` -> `P15` (one ground)
  ⓷ `L130: chi_meson`                 -> `B6`    ⓺ `probe2: killing_residual` -> `B7`

⚠ ⛭⛭⛭ ** `B7` IS THE SAME CLAIM `P11` CARRIES, AND ITS FUNCTION IS WRONG FOR A DIFFERENT REASON
   THAN `lie_g` WAS. **  `B7`'s own source says so: *the compact-face route is walled by
localisation and by `su(3)` being no isometry of the non-compact substrate.*
  ⇒ *** `killing_residual` HAS THE WRONG QUANTIFIER. ***  *A residual test is
  existential-refuting -- it settles ONE candidate field at a time, exactly, as the table below
  shows.  `su(3) is no isometry` is a NON-EXISTENCE over every embedding of an eight-dimensional
  algebra, and no finite number of non-vanishing residuals establishes one.*
  ⌈ ** So `lie_g` could not express `P11`'s claim at all, while `killing_residual` can express
  the NEGATION of `B7`'s one candidate at a time and still never reach the claim. **  ⌊ *Two
  different defects wearing one code, and the sharper one is this.*

⌗ ** THE EMPTY-CONTAINER REFUSAL FIRED IN REAL USE ONE BATCH AFTER IT WAS WRITTEN: ** `L091x`
binds `GROUPS = []` and fills it with top-level `.append(...)` calls, so the loader refused it by
name rather than returning an empty list.  *The row does not need it -- the function takes its
table as an ARGUMENT -- so the tables are supplied and the change of inputs is a call.*

WHAT IS NOT CLAIMED.  ** Not that `and no force` is settled by a converse ** -- it is the
FINITENESS of the holonomy group, `|G| = 27`, and `inv_dim`'s average is a finite sum so a
positive-dimensional group cannot be fed to it at all: a stated limit, not a false case.  ** Not
that `L091x` computes the irrep dimensions ** -- its body returns only whether the table is
abelian, and the dimensions follow from the identity its own docstring states, which is reported
rather than papered over.  ** Not that the acoustic pipeline is a power-spectrum fit. **  ** Not
that any pin moves. **

Run: python3 reach_b6.py            (writes REACHED_B6.tsv)
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import selection_and_scale as S                                    # noqa: E402

OUT = os.path.join(HERE, 'REACHED_B6.tsv')

B_ = 'receipts/L221_the_bridge/'
P_ = 'receipts/P15_CR_cosmology/'
L091X = 'baryon_edge/L091x_deck_symmetry_is_not_horizontal.py'
L128 = 'baryon_edge/L128_three_walls_or_one_radius.py'
L130 = 'baryon_edge/L130_statistics_not_gauge.py'
ACOUSTIC = 'CR_acoustic_scale_and_hubble.py'
PROBE2 = 'beyond_the_wall/probe2.py'
WRONG_KIND = 'FUNCTION-IS-THE-WRONG-KIND'

_P15RATE = (P_ + 'P15_the_rate_rule_reaches_the_projection_only_through_the_identification_'
            'because_P7_gives_the_lapse_the_rate_and_the_shift_the_appearance_as_distance.py')
_P15GROUND = (P_ + 'P15_the_one_ground_admits_exactly_one_independent_second_support_and_it_is_'
              'disqualified_because_the_rays_that_carry_the_flat_length_carry_a_blueshift.py')


def _deck_detail():
    return (f'the deck Z_3 is abelian ({S.deck_is_abelian()}), so its irreducibles are '
            f'{S.deck_irrep_dims()} -- three one-dimensional characters whose squares sum to '
            f'the order 3; the walls\' S_3 is NOT abelian and its dimensions are 1, 1, 2, so '
            f'not all one. Exactly ONE irreducible is trivial for either group, so triviality '
            f'does not discriminate and the DIMENSIONS are what the quantity turns on')


def _routes_detail():
    t = S.route_table()
    return (f'the three hinge pairs give {len(t)} x 2 = {2*len(t)} routes: '
            + '; '.join(f'{k} short {s} long {l}' for k, (s, l) in sorted(t.items()))
            + f' -- the two arcs partition the three walls at every pair '
              f'({S.routes_partition_the_walls()}) and every pair is a 1-2 split; at 4 and 5 '
              f'hinges the splits are {sorted(S._split_sizes_at(4))} and '
              f'{sorted(S._split_sizes_at(5))}, so the 1-2 structure is a fact about THREE')


def _colour_detail():
    rows = {nm: S.selection_rules(nm) for nm in ('G_full', 'G_su', 'G_rigid')}
    return ('baryon/diquark/meson invariant dimensions: '
            + '; '.join(f'{nm} |G|={v[0]} -> {v[1]},{v[2]},{v[3]}' for nm, v in rows.items())
            + f' -- exactly 1, 0, 1 on G_su and 1, 0, 3 on G_rigid, so `exact` is a fact about '
              f'G_su; and `no force` is the finiteness |G| = {rows["G_su"][0]}')


def _distance_detail():
    a, b = S.distance_by_the_two_routes()
    cr = S.acoustic_at(S.H0_CMB, rate='cr')[0]
    return (f'D_M at H0 = {S.H0_CMB} by its own quadrature is {a:.4f} Mpc and recovered from '
            f'ell_A r_s / pi is {b:.4f} Mpc -- the two routes name the same number to better '
            f'than 1e-9 relative; on the OTHER rate at the same H0 it is {cr:.2f} Mpc, so `the '
            f'same distance` is a statement about one rate')


def _scale_detail():
    dm, rs, la = S.acoustic_at(S.H0_CMB)
    dm2, rs2, la2 = S.acoustic_at(S.H0_LOCAL)
    return (f'flat LambdaCDM at H0 = {S.H0_CMB} gives r_s = {rs:.2f} Mpc and ell_A = {la:.2f} '
            f'against the module\'s own observed {S._acoustic()["ELL_A_OBS"]}; forcing the local '
            f'H0 = {S.H0_LOCAL} leaves r_s pinned at {rs2:.2f} and misses the scale at '
            f'{la2:.2f}')


def _killing_detail():
    return (f'of probe2\'s 4 coordinate fields exactly '
            f'{len(S.coordinate_fields_that_are_killing())} satisfies the Killing equation '
            f'({S.coordinate_fields_that_are_killing()}), and d/du is refuted exactly -- so the '
            f'equation has a solution and a candidate can be killed one at a time; but B7\'s '
            f'literal is su(3) being no isometry, which is the containment P11 carries '
            f'({S.b7_is_the_su3_claim()}), a NON-EXISTENCE over every embedding that no finite '
            f'number of residuals reaches')


ROWS = [
    (B_ + 'B41_the_isospin_structure_is_finite.py', 'that are trivial on the deck',
     L091X, 'irrep_dims_abelian_check', 'INPUTS',
     lambda: (S.deck_is_abelian() and S.deck_irrep_dims() == [1, 1, 1]
              and S.triviality_does_not_discriminate()),
     'hand the same function the walls\' S_3 table instead of the deck\'s, which is a change of '
     'the argument and nothing else',
     S.s3_is_abelian, _deck_detail),

    (B_ + 'B42_the_route_was_taken_and_p14_is_the_work.py',
     'is the single geometric opening the wall leaves', L128, 'routes', 'INPUTS',
     lambda: S.routes_partition_the_walls() and S.every_pair_is_a_one_two_split(),
     'build the same hinge and wall tables at FOUR hinges instead of three and ask the same '
     'function for the two arcs of every pair',
     lambda: S.one_two_split_at(4), _routes_detail),

    (B_ + 'B6_the_object_is_delivered_and_the_row_argues_elsewhere.py',
     'supplies colour\'s exact selection rules and no force', L130, 'chi_meson', 'INPUTS',
     S.exact_selection_rules,
     'ask the same characters of L130\'s own G_rigid instead of G_su, which is a change of the '
     'group argument and nothing else',
     S.rigid_converse, _colour_detail),

    (_P15RATE, 'The rate rule reaches the same distance by naming $D_M$', ACOUSTIC, 'D_M',
     'INPUTS', S.two_routes_agree,
     'take the OTHER rate at the same H0 -- radiation out of the expansion rate -- and ask the '
     'same function for the distance',
     S.other_rate_converse, _distance_detail),

    (_P15GROUND,
     'the same flat-$\\Lambda$CDM observable that places the acoustic scale at '
     '$\\ell_A\\approx301$', ACOUSTIC, 'ell_A', 'INPUTS',
     S.acoustic_scale_is_301,
     'force the LOCAL H0 instead of the CMB one, which is a change of the rate function handed '
     'to the same call',
     S.local_H0_converse, _scale_detail),

    (B_ + 'B7_two_unbuilt_sectors_not_one.py',
     'being no isometry of the non-compact substrate to begin with', PROBE2,
     'killing_residual', WRONG_KIND,
     S.a_residual_test_has_the_wrong_quantifier,
     'ask the containment ONE DIMENSION UP, in so(6), which is where the claim actually lives '
     'and where it fails',
     lambda: not S.b7_is_the_su3_claim(), _killing_detail),
]

# ⚠ ** TWO SLOTS HERE ARE LAMBDAS AND BOTH CALL WHAT THEY NAME. **  Batch five wrote
#   `lambda: not GC.<fn>` WITHOUT the call, which returns `False` for every input -- exactly
#   what a converse must return -- so the row passed for the wrong reason.  *The guard below
#   does not forbid a lambda; it forbids a slot that does not return a `bool`, and a slot whose
#   value does not change when the claim it names is negated is caught by the ledger's own
#   claim-TRUE / converse-FALSE rule.*
for _r in ROWS:
    for _slot in (_r[5], _r[7]):
        assert callable(_slot), _r[0]
        assert isinstance(_slot(), bool), (_r[0], _slot)


def main():
    print()
    print('  r7283 (1) batch six -- 6 rows, 6 taken; 5 INPUTS and 1 wrong-kind')
    print()
    bad, lines = [], [
        '# r7283 (1) BATCH SIX -- six rows on six functions, all six TAKEN.  Per row: the',
        '# predicate computed through the named function, and the REACHABLE CONVERSE it comes',
        '# back FALSE on, recorded as a concrete edit.  `code` is the classification AFTER the',
        '# read: five are ordinary INPUTS rows; `B7` is FUNCTION-IS-THE-WRONG-KIND because a',
        '# residual test settles one candidate field at a time while its claim is a',
        '# non-existence over every embedding -- the wrong QUANTIFIER, not the wrong object.',
        '\t'.join(('stem', 'literal', 'module', 'function', 'code', 'claim', 'converse_edit',
                   'converse', 'computed'))]
    for stem, lit, mod, fn, code, claim, cedit, conv, detail in ROWS:
        c, v = bool(claim()), bool(conv())
        d = detail()
        ok = c and not v
        if not ok:
            bad.append(stem)
        print(f"    {'OK  ' if ok else 'FAIL'}  {os.path.basename(stem)[:34]:<34} "
              f"{fn:<24} claim={c} converse={v}")
        print(f"            {d[:150]}")
        lines.append('\t'.join((stem, lit, mod, fn, code, 'TRUE' if c else 'FALSE', cedit,
                                'TRUE' if v else 'FALSE', d)))
    body = '\n'.join(lines) + '\n'
    open(OUT, 'w', encoding='utf-8').write(body)
    print()
    print(f'    REACHED_B6.tsv  {len(ROWS)} rows   '
          f'digest {hashlib.sha1(body.encode()).hexdigest()[:16]}')
    if bad:
        print(f'    {len(bad)} row(s) NOT reached')
        return 1
    print(f'    ** {len(ROWS)} taken, every predicate TRUE on the claim and FALSE on its '
          f'recorded converse. **')
    print('    ** AND B7 IS THE SAME CLAIM P11 CARRIES, with a function that is wrong for a')
    print('       SHARPER reason than lie_g was: a residual test is existential-refuting and')
    print('       settles ONE candidate field at a time -- exactly, as the table shows -- while')
    print('       `su(3) is no isometry` is a NON-EXISTENCE over every embedding.  lie_g could')
    print('       not express P11\'s claim at all; killing_residual can express the negation of')
    print('       B7\'s one candidate at a time and still never reach the claim. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
