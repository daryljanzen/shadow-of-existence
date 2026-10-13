#!/usr/bin/env python3
"""
`r7283` ② BATCH EIGHT — **SIX ROWS, SIX TAKEN, AND MY OWN PINNED CALL IS REFUTED BY MY OWN
REFUTATION CLAUSE: `1` OF `12`, NOT `3`.**

`EXTEND_PREDICTION.md` called `3` of the `12` wrong-kind at `25` per cent, and wrote out the
clause that kills it: *if the corpus already carries a function of the right KIND, the backlog
named the wrong function and the row is an ordinary mis-naming like `B39`'s.*

** ⛔ IT DOES, FOR TWO OF THE THREE I NAMED. **  `B15` and `B8` are reached by `L130`'s OWN
`inv_dim` with `chi_meson`, which the corpus carried all along -- four `inv_dim` functions under
`computations/` with this seat's own directory excluded, against ZERO subalgebra-dimension
functions.  ⇒ *** `1` of `12` = `8.3` per cent against `INPUTS`'s `5` of `59` = `8.5`.  The
shares are the same to within a fifth of a point: `EXTEND` does NOT attract kind errors, and the
call is refuted in number AND direction. ***

** ⛭⛭⛭ AND WHAT REFUTED IT IS WORTH MORE THAN THE CALL WOULD HAVE BEEN. **  *`B15` and `B8`
assert a LIE-GROUP fact and it is reached by a FINITE-GROUP CHARACTER COUNT.*
`inv_dim(G_su, chi_meson) = 1` is Schur's criterion -- the `3` is irreducible -- and an
irreducible `3` sits in no proper connected subgroup of `SU(3)`.  ** The same number batch six
read as `colour's meson selection rule` IS the irreducibility criterion. **

⌗ *`C3` survives as the one kind error, with the qualification stated: the only
subalgebra-dimension functions under `computations/` are the ones this seat wrote at batch five,
so the corpus carries the right kind NOW because I built it and did not when the backlog was
written.  **The verdict is a kind error against the corpus as the backlog found it.***

⌗ *And the three `P_T_of` rows are settled by the function's own SIGNATURE: two parameters, both
properties of the progenitor, and no crossing parameter at all -- which is exactly `a property of
the progenitor's collapse history rather than of the crossing`, because the crossing has zero
duration and cannot act.*

Run: python3 reach_b8.py            (writes REACHED_B8.tsv)
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import extensions_b8 as X                                          # noqa: E402

OUT = os.path.join(HERE, 'REACHED_B8.tsv')

B_ = 'receipts/L221_the_bridge/'
R_ = 'receipts/L204_physics_reach/'
P_ = 'receipts/P15_CR_cosmology/'
A2M = 'beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py'
PROBE2 = 'beyond_the_wall/probe2.py'
L150G = 'beyond_the_wall/L150g_the_tensor_sector_and_the_interiors_adequacy.py'

_P15SEAM = (P_ + 'P15_the_corpus_places_every_perturbation_source_before_the_branch_point_and_'
            'everything_after_it_is_transfer_so_nothing_already_built_supplies_anisotropic_'
            'content_on_the_expansion_leg.py')


def _schur_detail():
    return (f'inv_dim(G_su, chi_meson) = {X.hom_dimension("G_su")}, which is dim Hom(V,V) and so '
            f'by Schur the 3 is IRREDUCIBLE, and the group is non-abelian '
            f'({not X.is_abelian("G_su")}) -- so it sits in no proper connected subgroup of '
            f'SU(3): not the maximal torus, not SU(2)xU(1) which acts as 2+1, and not SO(3) '
            f'whose order-27 subgroups are cyclic. On L130\'s own G_rigid the same number is '
            f'{X.hom_dimension("G_rigid")}, the 3 is reducible and the predicate fails. '
            f'** The backlog named lie_g; the corpus carried inv_dim all along, in 4 modules **')


def _isotropy_detail():
    return (f'the isotropy subalgebra of a symmetric pair of so(5,1) is so(k) + so(6-k), of '
            f'dimension k(k-1)/2 + (6-k)(5-k)/2; over k = 1..5 the SET is '
            f'{X.isotropy_dimensions(6)}, which is exactly P12\'s stated triple {X.P12_TRIPLE}. '
            f'One ambient dimension up, so(6,1) gives {X.isotropy_dimensions(7)} and the triple '
            f'fails. ** The backlog named killing_residual, which settles one field against one '
            f'metric; and the corpus carried NO subalgebra-dimension function when the backlog '
            f'was written **')


def _anisotropy_detail():
    return (f'P_T_of\'s own parameters are {list(X.tensor_parameters())} -- the vacuum density '
            f'and the mass, both properties of the progenitor -- and there is no crossing '
            f'parameter at all, which is what `rather than of the crossing` means when the '
            f'crossing has zero duration. The log-log slopes are exactly '
            f'{X.log_slope("rho_v"):.4f} in the density and {X.log_slope("M_v"):.4f} in the '
            f'mass, so a decade of approach moves the amplitude by 10^6 '
            f'({X.a_decade_of_approach_moves_it_by()}) while the crossing contributes one')


_SMALLEST = ('the smallest connected group containing the ratios together with the hinge '
             'three-cycle is $SU(3)$ itself')

ROWS = [
    (B_ + 'B15_po3_both_clauses_answered.py', _SMALLEST, A2M, 'lie_g', X.MIS_NAMED,
     X.no_proper_connected_subgroup_contains_it, 'G_su',
     'ask the same of `L130`\'s own `G_rigid` instead, whose 3 is reducible, so the predicate '
     'comes back FALSE and the irreducibility is seen to be doing the work',
     'G_rigid', _schur_detail),

    (B_ + 'B8_po4_targets_have_opposite_verdicts.py', _SMALLEST, A2M, 'lie_g', X.MIS_NAMED,
     X.no_proper_connected_subgroup_contains_it, 'G_su',
     'ask the same of `L130`\'s own `G_rigid` instead, whose 3 is reducible, so the predicate '
     'comes back FALSE and the irreducibility is seen to be doing the work',
     'G_rigid', _schur_detail),

    (R_ + 'C3_the_isotropy_citation_runs_in_a_loop.py',
     'The isotropy dimensions are the Killing-vector counts the construction establishes',
     PROBE2, 'killing_residual', X.WRONG_KIND,
     X.triple_matches_the_paper, 6,
     'run the same enumeration one ambient dimension up, on so(6,1), where the symmetric-pair '
     'dimensions are {9,11,15} and the paper\'s triple fails',
     7, _isotropy_detail),

    (_P15SEAM, 'The isotropy is earned on the approach and preserved by the crossing',
     L150G, 'P_T_of', 'EXTEND',
     X.amplitude_depends_on, X.APPROACH,
     'ask the same predicate of the CROSSING instead of the approach -- the crossing has zero '
     'duration and is not a parameter of the function at all, so it comes back FALSE',
     X.CROSSING, _anisotropy_detail),

    (_P15SEAM, 'a property of the progenitor\'s collapse history rather than of the crossing',
     L150G, 'P_T_of', 'EXTEND',
     X.amplitude_depends_on, X.APPROACH,
     'ask the same predicate of the CROSSING instead of the approach -- the crossing has zero '
     'duration and is not a parameter of the function at all, so it comes back FALSE',
     X.CROSSING, _anisotropy_detail),

    (_P15SEAM, 'how much anisotropy survives is fixed by the approach against the leg\'s '
     'duration', L150G, 'P_T_of', 'EXTEND',
     X.amplitude_depends_on, X.APPROACH,
     'ask the same predicate of the CROSSING instead of the approach -- the crossing has zero '
     'duration and is not a parameter of the function at all, so it comes back FALSE',
     X.CROSSING, _anisotropy_detail),
]

# one predicate, two inputs of the same kind -- the guard batch seven put in place
for _r in ROWS:
    _pred, _a, _b = _r[5], _r[6], _r[8]
    assert callable(_pred), _r[0]
    assert isinstance(_pred(_a), bool) or isinstance(_pred(_a), tuple), (_r[0], _pred)
    assert type(_a) is type(_b), (_r[0], 'the two inputs must be the same KIND of object')


def main():
    print()
    print('  r7283 (2) batch eight -- 6 rows, 6 taken; and the pinned call is REFUTED')
    print()
    bad, lines = [], [
        '# r7283 (2) BATCH EIGHT -- six EXTEND rows, all six TAKEN.  Per row: one predicate',
        '# called at TWO inputs of the same kind, TRUE on the claim and FALSE on the edit.',
        '# `code` is the classification after the read: B15 and B8 are FUNCTION-MIS-NAMED,',
        '# because L130\'s own inv_dim with chi_meson reaches their claim and the corpus',
        '# carried it all along; C3 is the one FUNCTION-IS-THE-WRONG-KIND, the corpus having',
        '# carried no subalgebra-dimension function when the backlog was written; the three',
        '# P_T_of rows are ordinary EXTEND work settled by the function\'s own signature.',
        '# ** This REFUTES this seat\'s own pinned call of 3 wrong-kind rows: 1 of 12. **',
        '\t'.join(('stem', 'literal', 'module', 'function', 'code', 'claim', 'converse_edit',
                   'converse', 'computed'))]
    for stem, lit, mod, fn, code, pred, arg, cedit, carg, detail in ROWS:
        rc, rv = pred(arg), pred(carg)
        c = bool(rc) if isinstance(rc, bool) else rc == X.P12_TRIPLE
        v = bool(rv) if isinstance(rv, bool) else rv == X.P12_TRIPLE
        d = detail()
        ok = c and not v
        if not ok:
            bad.append(stem)
        print(f"    {'OK  ' if ok else 'FAIL'}  {os.path.basename(stem)[:32]:<32} "
              f"{code:<27} claim={c} converse={v}")
        print(f"            {d[:150]}")
        lines.append('\t'.join((stem, lit, mod, fn, code, 'TRUE' if c else 'FALSE', cedit,
                                'TRUE' if v else 'FALSE', d)))
    body = '\n'.join(lines) + '\n'
    open(OUT, 'w', encoding='utf-8').write(body)
    print()
    print(f'    REACHED_B8.tsv  {len(ROWS)} rows   '
          f'digest {hashlib.sha1(body.encode()).hexdigest()[:16]}')
    if bad:
        print(f'    {len(bad)} row(s) NOT reached')
        return 1
    a, b = X.the_shares()
    print(f'    ** {len(ROWS)} taken, every predicate TRUE on the claim and FALSE on its '
          f'recorded converse. **')
    print(f'    ⛔ ** AND THE PINNED CALL IS REFUTED BY ITS OWN CLAUSE: {X.MEASURED_WRONG_KIND}')
    print(f'       of {X.EXTEND_N} = {a:.1f} per cent against INPUTS\'s {X.INPUTS_WRONG_KIND} of')
    print(f'       {X.INPUTS_N} = {b:.1f} per cent.  I called {X.CALLED_WRONG_KIND}.  The shares')
    print('       are the same to within a fifth of a point, so EXTEND does not attract kind')
    print('       errors and the direction is dead with the number. **')
    print('    ⛭⛭ ** AND WHAT REFUTED IT IS WORTH MORE: B15 and B8 assert a LIE-GROUP fact and')
    print('       it is reached by a FINITE-GROUP CHARACTER COUNT.  inv_dim(G_su, chi_meson) = 1')
    print('       is Schur\'s criterion, so the 3 is irreducible and sits in no proper connected')
    print('       subgroup of SU(3).  The same number batch six read as colour\'s meson')
    print('       selection rule IS the irreducibility criterion. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
