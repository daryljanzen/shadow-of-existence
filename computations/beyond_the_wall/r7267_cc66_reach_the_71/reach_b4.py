#!/usr/bin/env python3
"""
`r7283` ① BATCH FOUR — **NINE ROWS ON FOUR FUNCTIONS, ALL NINE TAKEN, AND THE LOADER GREW A
REFUSAL BECAUSE THIS BATCH FOUND A WAY FOR IT TO PASS WHILE SAYING NOTHING.**

`r7283` order ①: "The remaining `27`, in batches as you have been scheduling them from the
syntax tree."  Four `(module, function)` pairs carry nine rows: ** `9` scheduled, `9` taken. **

  ⓵ `L128b: diag_at`   ->  `B29`, `B44`
  ⓶ `L50b: key_of + apply` -> `B38`, `B41`, `B13`
  ⓷ `r7111/geometry: curvature` -> the two `P15` rows
  ⓸ `panelA_reassign: ruling` -> the two `P1` rows

⚠ ⛭⛭ ** THE PART THAT IS NOT A ROW COUNT: `graft.py` COULD HAND BACK AN EMPTY TABLE AND
   NOTHING SAID SO. **  `L50b` binds `ends = {}` and `L128b` binds `leg_wall = {}` at top
level and fill them in a `for` loop, which is not a graftable statement kind.  *The loader saw
the binding, kept it, dropped the loop, and returned an EMPTY dict* -- so a row taken through
`ends` would have been **VACUOUS RATHER THAN WRONG**, which is the worse failure because it
passes.  ⇒ `graft.py` now REFUSES a kept binding to an empty container that a non-graftable
statement fills, naming the name and the line.
  ⌗ ** AND THE MEASUREMENT THAT SAYS NOT TO BUILD THE LOOP-KEEPING CAPABILITY INSTEAD: of the
  `30` rows still outstanding, the named function grafts ON ITS OWN in `27`, and the other `3`
  fail on an unrelated cause.  NOT ONE of the `30` needs a filled container. **  *The six ends
  are rebuilt here from `L50b`'s own `theta`, `A` and `sq3` and GATED on `L50b`'s own substrate
  equation `-X0^2 + X1^2 + X2^2 = A^2`, so the rebuild is checked and not trusted.*

⚠ ** AND ONE PREDICATE WAS SHARPENED BY ITS OWN CONVERSE, WHICH IS WHY THE CONVERSE RULE
   EARNS ITS KEEP. **  `The constant-tau slice is exactly flat` read off the SCALAR curvature
would have **PASSED on the Schwarzschild spatial slice**, whose `Rs` is `0` and whose
Kretschmann is `6 r_s^2/r^6`.  *A reachable converse found the predicate reading a quantity
that does not separate flat from Ricci-flat.*  The predicate here reads the Kretschmann
invariant, and that slice is recorded as the converse that exposed it.

⌗ ** TWO DOUBTS CHECKED BEFORE THE ROWS WERE TAKEN, because batch two's `B39` taught that the
backlog can name a function one notch off the quantity. **  ⒜ `key_of` keys MATRICES while
`B38`/`B41` assert about a map of the SIX ENDS -- resolved in the rows' favour: with `apply` it
reaches both halves, the swap as three 2-cycles AND its order `2` inside a group of order `12`.
⒝ `ruling(phi, sign)` looked like a plotting parameterisation -- resolved in the rows' favour
too: it is the quadric's two straight-line families, and the module's own docstring names the
converse (`a=b=alpha => null rulings = light cone`), so `b != 1` is an edit the module itself
supplies.

WHAT IS NOT CLAIMED.  ** Not that the plaquette is the only form of flatness ** -- it is the
form a connection given by monodromies has, and the winding-one holonomy is reported beside it
so that `flat` is visibly not `trivial`.  ** Not that the hinge count is three for a reason
computed here ** -- the `5`-station converse shows `a hop to a NEIGHBOURING hinge` is a fact
about there being three stations, and that is reported as the converse, not as a new claim.
** Not that the pins move ** -- the pin is the citation and the computation the verification,
as in all three earlier batches.

Run: python3 reach_b4.py            (writes REACHED_B4.tsv)
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import flat_ruled_and_discrete as F                                # noqa: E402

OUT = os.path.join(HERE, 'REACHED_B4.tsv')

B_ = 'receipts/L221_the_bridge/'
R_ = 'receipts/L204_physics_reach/'
P_ = 'receipts/P15_CR_cosmology/'
L128B = 'baryon_edge/L128b_leg_and_arc.py'
L50B = 'baryon_edge/L50b_three_hinges_six_ends.py'
GEOM = 'beyond_the_wall/r7111_70_layer_geometry_audit/geometry.py'
PANELA = 'synthesis_figure/panelA_reassign.py'

_P1 = (R_ + 'P1_the_petrov_interval_is_complete_because_the_substrate_is_doubly_ruled.py')
_P15SEAM = (P_ + 'P15_the_corpus_places_every_perturbation_source_before_the_branch_point_and_'
            'everything_after_it_is_transfer_so_nothing_already_built_supplies_anisotropic_'
            'content_on_the_expansion_leg.py')
_P15FLAT = (P_ + 'P15_the_rate_rule_reaches_the_projection_only_through_the_identification_'
            'because_P7_gives_the_lapse_the_rate_and_the_shift_the_appearance_as_distance.py')


def _flat_detail():
    import sympy as sp
    return (f'the plaquette round walls 0 and 1 in both orders is the identity and the '
            f'zero-winding class is the identity, so the holonomy is a function of the '
            f'winding numbers alone; on a winding-ONE loop it is '
            f'{sp.nsimplify(F.holonomy((1, 0, 0))[0, 0])}, so the bundle is flat and NOT '
            f'trivial')


def _swap_detail():
    return (f'the horn swap on the six ends is {F.horn_swap_on_ends()} -- a fixed-point-free '
            f'involution whose three 2-cycles each join ONE hinge\'s two ends, of order '
            f'{F.horn_swap_order()} inside a group of order {F.group_order_under_key_of()}')


def _disc_detail():
    return (f'the swap has order {F.horn_swap_order()} and the group it generates with the '
            f'other two isometries closes at {F.group_order_under_key_of()} elements under '
            f'key_of\'s exact keying; the same keying on a one-parameter rotation gives '
            f'{F.continuous_converse()} distinct keys in 12 steps and no closure')


def _hop_detail():
    s3, h3 = F.transposition_hop(3)
    s5, h5 = F.transposition_hop(5)
    return (f'the root transposition sends {s3} at three stations, every moved hinge one step '
            f'away ({h3}); at five stations the same transposition sends {s5} with hops {h5}, '
            f'so a moved hinge is TWO steps away and `neighbouring` fails')


def _slice_detail():
    import sympy as sp
    C = F.constant_tau_slice()
    rs_, k_ = F.ricci_flat_converse()
    return (f'the constant-tau slice of r7111\'s own metric has Ric = 0, Rs = '
            f'{sp.simplify(C["Rs"])} and Kretschmann = {sp.simplify(C["K"])} with '
            f'{F.slice_christoffels_nonzero()} of 27 Christoffels non-zero; the S^3 slice has '
            f'Rs = {F.sphere_converse()} and the Schwarzschild spatial slice has Rs = {rs_} '
            f'with K = {k_}, which Rs alone would have called flat')


def _seam_detail():
    K, Rs, _ = F.seam_invariants()
    seam, at_seam, at_zero = F.seam_is_finite_and_the_origin_is_not()
    return (f'the SdS exterior has K = {K} and Rs = {Rs}; at the horizon seam, the positive '
            f'root r = {seam:.6f} of f at r_s = 1/10, alpha = 1, K = {at_seam:.4g} is FINITE, '
            f'while at r -> 0 the same invariant goes to {at_zero}')


def _ruled_detail():
    onq, straight, norm = F.ruling_residuals()
    _, _, nb = F.ruling_residuals(b=1.5)
    return (f'both families at nine azimuths lie on x^2+y^2-z^2=1 to {onq:.1e}, have tangents '
            f'constant to {straight:.1e} and Minkowski tangent norm to {norm:.1e} -- straight '
            f'and null; on the non-equilateral quadric b=1.5 the module\'s own docstring names, '
            f'the tangent norm is {nb:.4f} and the lines are no longer null')


def _inherit_detail():
    z = F.crossings_per_line(2, 0.5)
    x = F.crossings_per_line(0, 0.5)
    return (f'every line of BOTH families meets each z = const slice exactly once '
            f'(crossings {min(z)}..{max(z)} over 18 lines), so the at-rest slicing inherits '
            f'both rulings as congruences; slicing instead by x = const gives '
            f'{min(x)}..{max(x)}, because a line with sin(phi) = 0 LIES IN one slice rather '
            f'than meeting it once')


ROWS = [
    (B_ + 'B29_the_two_walls_are_one.py', 'the bundle above is flat', L128B, 'diag_at',
     F.bundle_is_flat,
     'give one wall a non-diagonal monodromy of the same order 3, as a non-abelian vantage '
     'bundle would have',
     F.nonabelian_converse, _flat_detail),

    (B_ + 'B44_po5s_two_walls_are_one.py', 'the bundle above is flat', L128B, 'diag_at',
     F.bundle_is_flat,
     'give one wall a non-diagonal monodromy of the same order 3, as a non-abelian vantage '
     'bundle would have',
     F.nonabelian_converse, _flat_detail),

    (B_ + 'B38_the_ledger_is_discrete.py', 'is a discrete horn swap', L50B, 'key_of',
     lambda: (F.ends_are_on_the_substrate() and F.swap_is_three_two_cycles()
              and F.horn_swap_order() == 2 and F.group_order_under_key_of() == 12),
     'key a ONE-PARAMETER rotation the same way, so the ledger is a continuous motion instead '
     'of a swap',
     lambda: F.continuous_converse() < 12, _swap_detail),

    (B_ + 'B41_the_isospin_structure_is_finite.py', 'is a discrete horn swap', L50B, 'key_of',
     lambda: (F.horn_swap_order() == 2 and F.group_order_under_key_of() == 12
              and F.swap_is_three_two_cycles()),
     'key a ONE-PARAMETER rotation the same way, so the structure is continuous instead of '
     'finite',
     lambda: F.continuous_converse() < 12, _disc_detail),

    (B_ + 'B13_po2_identification_is_stated.py',
     'a transposition of roots is a hop to a neighbouring hinge', L50B, 'apply',
     lambda: F.every_moved_hinge_is_a_neighbour(3),
     'build theta from FIVE stations instead of three, which is a change of inputs and '
     'nothing else, and ask the same transposition where it sends each hinge',
     lambda: F.every_moved_hinge_is_a_neighbour(5), _hop_detail),

    (_P15FLAT, 'The constant-$\\tau$ slice is exactly flat', GEOM, 'curvature',
     lambda: F.slice_is_exactly_flat() and F.slice_christoffels_nonzero() > 0,
     'take the Schwarzschild spatial slice instead -- Ricci-flat, so a predicate reading the '
     'SCALAR curvature passes it, and only the Kretschmann invariant separates them',
     lambda: F.ricci_flat_converse()[1] == 0, _slice_detail),

    (_P15SEAM, 'seeded at the finite-curvature horizon seam, never at a curvature singularity',
     GEOM, 'curvature',
     lambda: (F.seam_is_finite_and_the_origin_is_not()[1] < float('inf')
              and F.seam_is_finite_and_the_origin_is_not()[2] == float('inf')),
     'seed it at r = 0 instead of at the root of f, where the same invariant diverges',
     lambda: F.seam_is_finite_and_the_origin_is_not()[2] != float('inf'), _seam_detail),

    (_P1, 'doubly ruled by straight null lines', PANELA, 'ruling',
     F.doubly_ruled_by_straight_null_lines,
     'scale the second axis so the quadric is no longer equilateral, which the module\'s own '
     'docstring names as what makes the rulings null',
     lambda: F.ruling_residuals(b=1.5)[2] < 1e-12, _ruled_detail),

    (_P1, 'inherits both rulings', PANELA, 'ruling',
     lambda: F.slicing_inherits_both_rulings(2, 0.5),
     'slice by x = const instead of z = const, so a line with sin(phi) = 0 lies IN a slice '
     'rather than meeting it once',
     lambda: F.slicing_inherits_both_rulings(0, 0.5), _inherit_detail),
]


def main():
    print()
    print('  r7283 (1) batch four -- 9 scheduled, 9 taken, nothing held')
    print()
    bad, lines = [], [
        '# r7283 (1) BATCH FOUR -- nine rows on four modules, all nine TAKEN.  Per row: the',
        '# predicate computed through the named function, and the REACHABLE CONVERSE it comes',
        '# back FALSE on, recorded as a concrete edit.  The loader grew an EMPTY-CONTAINER',
        '# refusal in this batch: two of these modules bind a table as `{}` and fill it in a',
        '# `for` loop, and the graft was handing back an empty dict with nothing to say so.',
        '\t'.join(('stem', 'literal', 'module', 'function', 'claim', 'converse_edit',
                   'converse', 'computed'))]
    for stem, lit, mod, fn, claim, cedit, conv, detail in ROWS:
        c, v = bool(claim()), bool(conv())
        d = detail()
        ok = c and not v
        if not ok:
            bad.append(stem)
        print(f"    {'OK  ' if ok else 'FAIL'}  {os.path.basename(stem)[:36]:<36} {fn:<10} "
              f"claim={c} converse={v}")
        print(f"            {d}")
        lines.append('\t'.join((stem, lit, mod, fn, 'TRUE' if c else 'FALSE', cedit,
                                'TRUE' if v else 'FALSE', d)))
    body = '\n'.join(lines) + '\n'
    open(OUT, 'w', encoding='utf-8').write(body)
    print()
    print(f'    REACHED_B4.tsv  {len(ROWS)} rows   '
          f'digest {hashlib.sha1(body.encode()).hexdigest()[:16]}')
    if bad:
        print(f'    {len(bad)} row(s) NOT reached')
        return 1
    print(f'    ** {len(ROWS)} taken, every predicate TRUE on the claim and FALSE on its '
          f'recorded converse. **')
    print('    ** AND THE LOADER NOW REFUSES AN EMPTY CONTAINER IT USED TO RETURN SILENTLY:')
    print('       `ends = {}` and `leg_wall = {}` are filled by `for` loops the graft drops, so')
    print('       a row taken through either would have been VACUOUS RATHER THAN WRONG.  Of the')
    print('       30 rows still outstanding, NOT ONE needs a filled container -- so the refusal')
    print('       is the whole of the fix and the loop-keeping capability is not built. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
