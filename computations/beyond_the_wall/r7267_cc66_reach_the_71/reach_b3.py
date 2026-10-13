#!/usr/bin/env python3
"""
`r7267`/`r7281` ① BATCH THREE — **NINE ROWS, ALL NINE TAKEN, AND `roots_at` SETTLES THE HALF
`B13` AND `B14` COULD NOT CHECK.**

`r7281` order ①: "The remaining `36`, in batches as you have been scheduling them from the
syntax tree."  Three `(module, function)` pairs carry nine rows and all three functions are
top-level, so unlike batch two this batch has nothing to hold: ** `9` scheduled, `9` taken. **

  ⓵ `L012w: roots_at`  ->  `B13`, `B14`, `B34`
  ⓶ `L127: omega_power` ->  `B29`, `B44`, `B45`
  ⓷ `bead_conjugate: r_of_tau` -> `P9`, `B9`, and `P15`'s branch-point row

⇒ ⛭⛭ ** AND THE ONE WORTH READING IS `roots_at`, BECAUSE IT ANSWERS A CLAIM NEITHER HOLDER
   COULD CHECK. **  `L-012w`'s own report tabulates eleven values of `r_0` with the designated
root and its pair.  *Asked instead at the three values the hinges sit at, it returns the SAME
ROOT SET every time -- `{1, -1, 0}` -- and differs only in WHICH member is designated.*
  *** `B14` asserts `distinguished only by which root each takes as its hole`.  The `only` is
  the load-bearing word and it is a statement about the sets being IDENTICAL, which no string
  match can see and which `L-012w` never prints side by side. ***  Computed here: the sets
  agree, the designations all differ, and the cubic evaluates to `0` at each of its own roots.

⚠ ** `omega_power` CARRIES ITS OWN CONVERSE, which is rare enough to say: ** it `raise`s on
anything that is not a cube root of unity, so `quantises` and `is a pure power of omega` have a
built-in false case and need no constructed edit to fail on.

WHAT IS NOT CLAIMED.  ** Not that the cubic's roots ARE the hinge positions ** -- `roots_at` is
asked at values this batch supplies, and the correspondence to hinges is the receipts' own,
pinned there and unchanged.  ** Not anything about `r_of_tau` off the real axis ** -- it is
complex-valued and the rows ask about proper time on the real branch.  ** Not that the pins
move ** -- the pin is the citation and the computation the verification, as in both earlier
batches.

Run: python3 reach_b3.py            (writes REACHED_B3.tsv)
"""
import hashlib
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import splits as SPL                                           # noqa: E402

OUT = os.path.join(HERE, 'REACHED_B3.tsv')
S, O, B = SPL.at_inputs()

HINGE = ('1', '-1', '0')          # the three values the designation runs over
B_ = 'receipts/L221_the_bridge/'
R_ = 'receipts/L204_physics_reach/'
P_ = 'receipts/P15_CR_cosmology/'
L012 = 'baryon_edge/L012w_the_two_splits.py'
L127 = 'baryon_edge/L127_the_bundle.py'
BEAD = 'bead_conjugate.py'

_P15 = (P_ + 'P15_the_corpus_places_every_perturbation_source_before_the_branch_point_and_'
        'everything_after_it_is_transfer_so_nothing_already_built_supplies_anisotropic_'
        'content_on_the_expansion_leg.py')
_P9 = (R_ + 'P9_the_resolution_is_the_baby_universe_one_and_it_is_never_named.py')


def _sets_detail():
    return (f'roots_at at r_0 = {", ".join(HINGE)} returns the SAME root set '
            f'{sorted(str(x) for x in S.root_set("1"))} every time, with the designation '
            f'differing each time ({", ".join(str(S.designated(v)) for v in HINGE)})')


ROWS = [
    (B_ + 'B13_po2_identification_is_stated.py',
     'each hinge designates one of the three roots of the horizon cubic as its own '
     'black-hole horizon', L012, 'roots_at',
     lambda: (all(len(S.triple(v)) == 3 for v in HINGE)
              and S.designations_differ(HINGE)
              and all(S.designated(v) in S.triple(v) for v in HINGE)),
     'let two of the three values designate the same root',
     lambda: not S.designations_differ(HINGE),
     lambda: f'three roots at each of {len(HINGE)} values, each designating a DIFFERENT one: '
             + ", ".join(f'{v}->{S.designated(v)}' for v in HINGE)),

    (B_ + 'B14_identical_in_content_is_po2s_reason.py',
     'distinguished only by which root each takes as its hole', L012, 'roots_at',
     lambda: S.sets_agree(HINGE) and S.designations_differ(HINGE),
     'add a value whose root SET differs, so the designation is no longer the only difference',
     lambda: S.sets_agree(tuple(HINGE) + ('1/sqrt(3)',)),
     _sets_detail),

    (B_ + 'B34_the_join_crosses_the_inner_horizon.py',
     'vanishes at the horizons', L012, 'roots_at',
     lambda: all(x == 0 for x in S.vanishes_at_roots('1')),
     'evaluate the same cubic a step off its roots',
     lambda: all(sp.simplify(sp.Poly(S.cubic(), sp.Symbol('r')).eval(x + sp.Rational(1, 7)))
                 == 0 for x in S.triple('1')),
     lambda: f'the horizon cubic at each of its own three roots: {S.vanishes_at_roots("1")}; '
             f'a seventh off each root it is '
             f'{[sp.simplify(sp.Poly(S.cubic(), sp.Symbol("r")).eval(x + sp.Rational(1, 7))) for x in S.triple("1")]}'),
]

for _stem, _lit in ((B_ + 'B29_the_two_walls_are_one.py', 'it quantises and does not couple'),
                    (B_ + 'B44_po5s_two_walls_are_one.py', 'is a pure power of'),
                    (B_ + 'B45_the_object_exists_and_the_action_is_absent.py',
                     'quantises without measuring')):
    ROWS.append((
        _stem, _lit, L127, 'omega_power',
        lambda: O.quantises() and all(O.is_pure_power(sp.simplify(O.w**k)) for k in range(3)),
        'ask the same of a value that is not a cube root of unity',
        lambda: O.is_pure_power(sp.Integer(2)),
        lambda: f'omega_power on the three cube roots returns {O.powers()}, exhausting Z/3; '
                f'off them it RAISES, so is_pure_power(2) is '
                f'{O.is_pure_power(sp.Integer(2))}'))

for _stem, _lit in ((_P9, 'does not end as a thermal remnant whose purity must be explained'),
                    (B_ + 'B9_po3_why_is_answered_dimensionally.py',
                     'the collapse does occur, at scale'),
                    (_P15, 'the cosmology it seeds begins at the branch point')):
    ROWS.append((
        _stem, _lit, BEAD, 'r_of_tau',
        lambda: B.branch_point_at_zero() and B.nonzero_away(),
        'ask for the branch point at a proper time away from zero',
        lambda: abs(B.radius(0.5)) <= 1e-15,
        lambda: f'r_of_tau(0) = {B.radius(0.0)} exactly -- the branch point at proper time '
                f'zero -- while r_of_tau(0.5) = {B.radius(0.5):.6f} and '
                f'r_of_tau(1.0) = {B.radius(1.0):.6f}'))


def main():
    print()
    print('  r7267/r7281 (1) batch three -- 9 scheduled, 9 taken, nothing held')
    print(f'    graft: L-012w {S.statements[0]}/{S.statements[1]}, '
          f'L-127 {O.statements[0]}/{O.statements[1]}, '
          f'bead_conjugate {B.statements[0]}/{B.statements[1]}')
    print()
    bad, lines = [], [
        '# r7267/r7281 (1) BATCH THREE -- nine rows on three modules, all nine TAKEN.  Per row:',
        '# the predicate computed through the named function, and the REACHABLE CONVERSE it comes',
        '# back FALSE on, recorded as a concrete edit.  Nothing is held: all three functions are',
        '# top-level and each takes its inputs as arguments, so the change of inputs is a call.',
        '\t'.join(('stem', 'literal', 'module', 'function', 'claim', 'converse_edit',
                   'converse', 'computed'))]
    for stem, lit, mod, fn, claim, cedit, conv, detail in ROWS:
        c, v = bool(claim()), bool(conv())
        d = detail()
        ok = c and not v
        if not ok:
            bad.append(stem)
        print(f"    {'OK  ' if ok else 'FAIL'}  {os.path.basename(stem)[:36]:<36} {fn:<12} "
              f"claim={c} converse={v}")
        print(f"            {d}")
        lines.append('\t'.join((stem, lit, mod, fn, 'TRUE' if c else 'FALSE', cedit,
                                'TRUE' if v else 'FALSE', d)))
    body = '\n'.join(lines) + '\n'
    open(OUT, 'w', encoding='utf-8').write(body)
    print()
    print(f'    REACHED_B3.tsv  {len(ROWS)} rows   '
          f'digest {hashlib.sha1(body.encode()).hexdigest()[:16]}')
    if bad:
        print(f'    {len(bad)} row(s) NOT reached')
        return 1
    print(f'    ** {len(ROWS)} taken, every predicate TRUE on the claim and FALSE on its '
          f'recorded converse. **')
    print('    ** AND roots_at SETTLES THE HALF B13 AND B14 COULD NOT CHECK: asked at the three')
    print('       values the hinges sit at it returns the SAME ROOT SET every time and differs')
    print('       only in WHICH member is designated.  B14\'s `only` is a statement about the')
    print('       sets being IDENTICAL -- which no string match can see and which L-012w never')
    print('       prints side by side. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
