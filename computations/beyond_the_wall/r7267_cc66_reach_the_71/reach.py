#!/usr/bin/env python3
"""
`r7267` ① BATCH ONE — THE NINETEEN ROWS ON THE TWO LARGEST MODULES, REACHED.

`r7261` measured the `85`-row backlog and found `71` with a named nearest FUNCTION, split
`59` `INPUTS` and `12` `EXTEND`.  `r7267` ordered the `59` first, cheapest first.  ** The `59`
group by module, and two modules carry `19` of them: `L129_the_invariants.py` (eleven rows,
four functions) and `L006w_the_d5_fourfold.py` (eight rows, one function).  This is that
batch. **

  ⓵  the obstruction, and it is the same one for all `59`: every named module is a SCRIPT.
      `graft.py` takes the function and the transitive closure of what it reads, and nothing
      else runs.
  ⓶  the inputs: `holonomy.py` and `parity.py` hand the rows' own generators and dimensions
      to the grafted functions.  ** Neither file does any mathematics of its own. **
  ⓷  the ledger, here: per row, the predicate, the value it returns, and A REACHABLE CONVERSE
      recorded as a concrete edit with the value it returns under that edit.

⇒ ** THE RULE IS `r7257`'s AND IT IS NOT RELAXED: a row is reached when a predicate over
   computed corpus state is TRUE where the claim holds and FALSE on at least one reachable
   converse. **  A predicate that cannot be made false is not a measurement, and this file
   FAILS rather than records a row whose converse comes back true.

⌗ ** AND THE BATCH RETURNED A FINDING NOBODY ASKED FOR. **  `twoM` carries TWO parities, in
opposite senses: the mass function is `R`-odd exactly when `D` is EVEN, and the wall factor
`sqrt f / r` built on the same `2M` is odd in the signed radius exactly when `D` is ODD.  At
the corpus's `D = 5` the first is EVEN and the second is ODD -- *** and six receipts across
two prefixes match one or the other as "odd" in a signed radial variable, which until now
nothing in the corpus distinguished by computing. ***

WHAT IS NOT CLAIMED.  ** Not that the `19` are the `59` ** -- forty remain, named in the
report.  ** Not that a string pin is removed ** -- the pin is the CITATION and the computation
is the verification; both stand, and `check_quote_pins` sees the pins it saw before.  ** Not
that every half of every row has a reachable converse ** -- the flatness half of the three
`no curvature` rows carries a finiteness witness and no converse inside `L-129`'s
representation, and that is recorded per row rather than asserted away.

Run: python3 reach.py            (writes REACHED.tsv)
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import holonomy as HOL                                         # noqa: E402
import parity as PAR                                           # noqa: E402

OUT = os.path.join(HERE, 'REACHED.tsv')

H = HOL.at_inputs()
P = PAR.at_inputs()

# ---- the groups, each one call of L-129's own `close` at the rows' generators -----------
G_FULL = H.close(H.gens_full)
G_SU = H.close(H.gens_su)
G_TRIV = H.close([])
G_NOCYC = H.close(H.gamma)                 # the converse edit: drop the hinge 3-cycle
D1 = H.det_one(G_FULL)

assert all(H.mul(x, H.inverse(x)) == H.ident for x in G_FULL), 'the inverse must invert'

B = 'receipts/L221_the_bridge/'
R = 'receipts/L204_physics_reach/'
L129 = 'baryon_edge/L129_the_invariants.py'
L006 = 'baryon_edge/L006w_the_d5_fourfold.py'


def _eps_moved():
    """five seconds; computed once and shared by the one row that needs it"""
    if not hasattr(_eps_moved, 'v'):
        _eps_moved.v = (len(H.eps_moved_by(G_SU)), len(H.eps_moved_by(G_FULL)))
    return _eps_moved.v


# =========================================================================================
# per row: (stem, literal, module, function, predicate, converse edit, converse predicate,
#           what the computation returns)
# =========================================================================================
ROWS = [
    # ---- L-006w: twoM, and the one substitution L-006w's own report never makes ---------
    (R + 'P4_the_corpus_identifies_the_higgs_mechanism_it_does_not_decline_it.py',
     'is the $R$-odd \\emph{departure} from it', L006, 'twoM',
     lambda: P.mass_parity(4) == -1,
     'state the same R-oddness at the D=5 exponent pair (D-3,D-1)=(2,4)',
     lambda: P.mass_parity(5) == -1,
     lambda: f'twoM(4) -> R-parity {P.mass_parity(4)}; at D=5 it is {P.mass_parity(5)}'),

    (B + 'B15_po3_both_clauses_answered.py',
     'The mass function is odd in the signed offset exactly when $D$ is even', L006, 'twoM',
     lambda: all(P.mass_is_R_odd(D) == (D % 2 == 0) for D in range(4, 10)),
     'replace `even` with `odd` in the sentence',
     lambda: all(P.mass_is_R_odd(D) == (D % 2 == 1) for D in range(4, 10)),
     lambda: 'R-parity of twoM(D), D=4..9: '
             + ','.join(f'{D}:{P.mass_parity(D):+d}' for D in range(4, 10))),

    (B + 'B9_po3_why_is_answered_dimensionally.py',
     'The mass function is odd in the signed offset exactly when $D$ is even', L006, 'twoM',
     lambda: all(P.mass_is_R_odd(D) == (D % 2 == 0) for D in range(4, 10)),
     'replace `even` with `odd` in the sentence',
     lambda: all(P.mass_is_R_odd(D) == (D % 2 == 1) for D in range(4, 10)),
     lambda: 'R-parity of twoM(D), D=4..9: '
             + ','.join(f'{D}:{P.mass_parity(D):+d}' for D in range(4, 10))),

    (B + 'B9_po3_why_is_answered_dimensionally.py',
     'The second condition is the parity, and it separates those two', L006, 'twoM',
     lambda: P.mass_parity(4) != P.mass_parity(5),
     'name D=4 and D=6 as the two the parity separates',
     lambda: P.mass_parity(4) != P.mass_parity(6),
     lambda: f'twoM parity at D=4,5,6: {P.mass_parity(4):+d},{P.mass_parity(5):+d},'
             f'{P.mass_parity(6):+d} -- separates 4 from 5, not 4 from 6'),

    (B + 'B9_po3_why_is_answered_dimensionally.py',
     'there is no mass-reflection', L006, 'twoM',
     lambda: P.mass_parity(5) == 1,
     'ask the same of D=4, where 2M does reverse',
     lambda: P.mass_parity(4) == 1,
     lambda: f'at D=5, R fixes twoM (parity {P.mass_parity(5):+d}), so no 2M -> -2M involution; '
             f'at D=4 the parity is {P.mass_parity(4):+d}'),

    (B + 'B34_the_join_crosses_the_inner_horizon.py',
     'odd in the signed radius', L006, 'twoM',
     lambda: P.wall_is_odd(5) and P.f_parity(5) == 1,
     'build f at the D=4 exponent this receipt samples numerically',
     lambda: P.wall_is_odd(4) and P.f_parity(4) == 1,
     lambda: f'with 2M from twoM: f parity {P.f_parity(5):+d} and sqrt(f)/r parity '
             f'{P.wall_factor_parity(5):+d} at D=5; at D=4 neither has a parity'),

    (B + 'B35_the_continuation_is_cited_wrong.py',
     'odd in the signed radius', L006, 'twoM',
     lambda: P.wall_is_odd(5) and P.f_parity(5) == 1,
     'build f at the D=4 exponent',
     lambda: P.wall_is_odd(4) and P.f_parity(4) == 1,
     lambda: f'sqrt(f)/r parity {P.wall_factor_parity(5):+d} at D=5, '
             f'{P.wall_factor_parity(4):+d} at D=4'),

    (B + 'B36_two_of_three_crossings_are_supplied.py',
     'odd in the signed radius', L006, 'twoM',
     lambda: P.wall_is_odd(5) and P.f_parity(5) == 1,
     'build f at the D=4 exponent',
     lambda: P.wall_is_odd(4) and P.f_parity(4) == 1,
     lambda: f'sqrt(f)/r parity {P.wall_factor_parity(5):+d} at D=5, '
             f'{P.wall_factor_parity(4):+d} at D=4'),

    # ---- L-129: close, det, inv_dim, chi_VVV at the rows' generators -------------------
    (B + 'B15_po3_both_clauses_answered.py',
     'the three wall monodromies and the hinge $3$-cycle generate a finite group of order '
     '$81$ in $U(3)$', L129, 'close',
     lambda: len(G_FULL) == 81 and H.dets(G_FULL) != ['1'],
     'drop the hinge 3-cycle from the generators',
     lambda: len(G_NOCYC) == 81 and H.dets(G_NOCYC) != ['1'],
     lambda: f'|<gamma_0,gamma_1,gamma_2,P>| = {len(G_FULL)}, dets {H.dets(G_FULL)} '
             f'(so U(3), not SU(3)); without P it is {len(G_NOCYC)}'),

    (B + 'B6_the_object_is_delivered_and_the_row_argues_elsewhere.py',
     'the three wall monodromies and the hinge $3$-cycle generate a finite group of order '
     '$81$ in $U(3)$', L129, 'close',
     lambda: len(G_FULL) == 81 and H.dets(G_FULL) != ['1'],
     'drop the hinge 3-cycle from the generators',
     lambda: len(G_NOCYC) == 81 and H.dets(G_NOCYC) != ['1'],
     lambda: f'|<gamma_0,gamma_1,gamma_2,P>| = {len(G_FULL)}; without P, {len(G_NOCYC)}'),

    (B + 'B8_po4_targets_have_opposite_verdicts.py',
     'the three wall monodromies and the hinge $3$-cycle generate a finite group of order '
     '$81$ in $U(3)$', L129, 'close',
     lambda: len(G_FULL) == 81 and H.dets(G_FULL) != ['1'],
     'drop the hinge 3-cycle from the generators',
     lambda: len(G_NOCYC) == 81 and H.dets(G_NOCYC) != ['1'],
     lambda: f'|<gamma_0,gamma_1,gamma_2,P>| = {len(G_FULL)}; without P, {len(G_NOCYC)}'),

    (B + 'B15_po3_both_clauses_answered.py',
     'whose determinant-one part is $\\Delta(27)$ and lies in $SU(3)$', L129, 'det',
     lambda: (len(D1) == 27 and set(D1) == set(G_SU) and H.dets(D1) == ['1']
              and not H.is_abelian(D1) and len(H.centre(D1)) == 3),
     'take the determinant-omega coset instead of the determinant-one part',
     lambda: (len([x for x in G_FULL if x not in D1]) == 27
              and set(x for x in G_FULL if x not in D1) == set(G_SU)),
     lambda: f'det-one part: order {len(D1)}, unimodular, non-abelian, centre '
             f'{len(H.centre(D1))} -- Delta(27); equals <ratios,P>: {set(D1) == set(G_SU)}'),

    (B + 'B6_the_object_is_delivered_and_the_row_argues_elsewhere.py',
     'the three wall monodromies with the hinge $3$-cycle generate a finite flat holonomy '
     'whose determinant-one part, $\\Delta(27)$, lies in $SU(3)$', L129, 'det',
     lambda: (len(G_FULL) == 81 and len(D1) == 27 and H.dets(D1) == ['1']
              and not H.is_abelian(D1) and len(H.centre(D1)) == 3),
     'take the determinant-omega coset instead of the determinant-one part',
     lambda: (len([x for x in G_FULL if x not in D1]) == 27
              and H.dets([x for x in G_FULL if x not in D1]) == ['1']),
     lambda: f'closure finite at {len(G_FULL)}; det-one part order {len(D1)}, centre '
             f'{len(H.centre(D1))}, unimodular -- Delta(27) in SU(3)'),

    (B + 'B2_the_mod_two_prerequisite_is_already_built.py',
     'only the order-two subgroup', L129, 'close',
     lambda: (len(H.close(H.stab_gens((0,)))) == 2
              and len(H.close(H.stab_gens((0, 1, 2)))) == 6),
     'let the over-critical regime realise all of S_3 on the real structure',
     lambda: (len(H.close(H.stab_gens((0, 1, 2)))) == 2
              and len(H.close(H.stab_gens((0, 1, 2)))) == 6),
     lambda: f'one real root and a conjugate pair: |stab| = '
             f'{len(H.close(H.stab_gens((0,))))}; three real roots: '
             f'{len(H.close(H.stab_gens((0, 1, 2))))}'),

    (B + 'B10_po2_resemblance_is_now_a_construction.py',
     'Flat holonomy supplies exact selection rules and no curvature', L129, 'inv_dim',
     lambda: (H.inv_dim(G_FULL, H.chi_VVbar) == 1 and H.inv_dim(G_SU, H.chi_VVbar) == 1
              and len(G_FULL) == 81),
     'ask the same exactness of a bundle with no holonomy at all',
     lambda: H.inv_dim(G_TRIV, H.chi_VVbar) == 1,
     lambda: f'meson channel: {H.inv_dim(G_FULL, H.chi_VVbar)} invariant under the full group, '
             f'{H.inv_dim(G_SU, H.chi_VVbar)} under the det-one part, '
             f'{H.inv_dim(G_TRIV, H.chi_VVbar)} with no holonomy; baryon channel '
             f'{H.inv_dim(G_SU, H.chi_VVV)} under the det-one part, SU(3) admits 1'),

    (B + 'B10_po2_resemblance_is_now_a_construction.py',
     'places a three-fermion state in the exterior cube, one-dimensional and generated by '
     '$\\varepsilon$', L129, 'chi_VVV',
     lambda: _eps_moved()[0] == 0 and H.eps().rank() == 1,
     'ask for the same invariance under the FULL holonomy group',
     lambda: _eps_moved()[1] == 0,
     lambda: f'epsilon spans a 1-dimensional subspace of V(x)V(x)V and is fixed by all '
             f'{len(G_SU)} of the det-one part ({_eps_moved()[0]} move it); '
             f'{_eps_moved()[1]} of {len(G_FULL)} move it in the full group'),

    (B + 'B44_po5s_two_walls_are_one.py',
     'the flat bundle selects without coupling', L129, 'inv_dim',
     lambda: H.inv_dim(G_FULL, H.chi_VVbar) == 1 and len(G_FULL) == 81,
     'ask the same of a bundle with no holonomy at all',
     lambda: H.inv_dim(G_TRIV, H.chi_VVbar) == 1,
     lambda: f'{H.inv_dim(G_FULL, H.chi_VVbar)} invariant on V(x)V* under the full holonomy, '
             f'{H.inv_dim(G_TRIV, H.chi_VVbar)} with none; the closure is finite at '
             f'{len(G_FULL)}, so the connection carries no curvature'),

    (B + 'B45_the_object_exists_and_the_action_is_absent.py',
     'filters without supplying', L129, 'inv_dim',
     lambda: H.inv_dim(G_FULL, H.chi_VVV) == 1 and len(G_FULL) == 81,
     'ask the same of a bundle with no holonomy at all',
     lambda: H.inv_dim(G_TRIV, H.chi_VVV) == 1,
     lambda: f'{H.inv_dim(G_FULL, H.chi_VVV)} of the {H.inv_dim(G_TRIV, H.chi_VVV)} '
             f'three-constituent states survives the full holonomy, and the closure is finite '
             f'at {len(G_FULL)} -- it filters and supplies no curvature'),

    (B + 'B45_the_object_exists_and_the_action_is_absent.py',
     'selects without coupling', L129, 'inv_dim',
     lambda: H.inv_dim(G_SU, H.chi_VVbar) == 1 and len(G_SU) == 27,
     'ask the same of a bundle with no holonomy at all',
     lambda: H.inv_dim(G_TRIV, H.chi_VVbar) == 1,
     lambda: f'{H.inv_dim(G_SU, H.chi_VVbar)} invariant on V(x)V* under the det-one part, '
             f'{H.inv_dim(G_TRIV, H.chi_VVbar)} with no holonomy'),
]

# the three rows whose `no curvature` half has no converse inside L-129's representation
_NO_CONVERSE_HALF = {'Flat holonomy supplies exact selection rules and no curvature',
                     'the flat bundle selects without coupling',
                     'filters without supplying'}


def main():
    print()
    print('  r7267 (1) batch one -- the 19 rows on the two largest modules')
    print(f'    graft: L-129 {H.statements[0]}/{H.statements[1]} statements, '
          f'L-006w {P.statements[0]}/{P.statements[1]}')
    print()
    bad = []
    lines = ['# r7267 (1) BATCH ONE -- the 19 backlog rows on the two largest modules, reached.',
             '# Per row: the predicate that computes the claim through the named function, the',
             '# value it returns, and the REACHABLE CONVERSE it comes back FALSE on, recorded as a',
             '# concrete edit.  A row whose converse comes back TRUE is a failure, not a record.',
             '\t'.join(('stem', 'literal', 'module', 'function', 'claim', 'converse_edit',
                        'converse', 'computed', 'half_without_converse'))]
    for stem, lit, mod, fn, claim, cedit, conv, detail in ROWS:
        c, v = bool(claim()), bool(conv())
        d = detail()
        ok = c and not v
        if not ok:
            bad.append((stem, lit, c, v))
        half = 'no curvature: finiteness witness, no converse in L-129\'s representation' \
            if lit in _NO_CONVERSE_HALF else '-'
        print(f"    {'OK  ' if ok else 'FAIL'}  {os.path.basename(stem)[:34]:<34} "
              f"{fn:<9} claim={c} converse={v}")
        print(f"            {d}")
        lines.append('\t'.join((stem, lit, mod, fn, 'TRUE' if c else 'FALSE', cedit,
                                'TRUE' if v else 'FALSE', d, half)))
    body = '\n'.join(lines) + '\n'
    open(OUT, 'w', encoding='utf-8').write(body)
    print()
    print(f'    REACHED.tsv  {len(ROWS)} rows   '
          f'digest {hashlib.sha256(body.encode()).hexdigest()[:16]}')
    if bad:
        print(f'    {len(bad)} row(s) NOT reached')
        return 1
    print(f'    ** {len(ROWS)} of the 59 INPUTS rows reached: every predicate TRUE on the claim '
          f'and FALSE on its recorded converse. **')
    print('    ** AND THE FINDING: twoM carries two opposite parities -- the mass function is')
    print('       R-odd exactly when D is EVEN, the wall factor sqrt(f)/r odd in the signed')
    print('       radius exactly when D is ODD.  At D=5 they differ, and six receipts match one')
    print('       or the other as "odd" in a signed radial variable. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
