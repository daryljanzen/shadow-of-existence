#!/usr/bin/env python3
"""
`r7283` ② BATCH NINE — **THE LAST TWO `EXTEND` ROWS, BOTH TAKEN. THE `12` ARE CLOSED AND SO IS
THE `71`-ROW SUBJECT, EXCEPT FOR THE `7` `INPUTS` THAT ARE A FILED LIMIT.**

  ⓵ `probe1: Gamma`     -> `P1`,  *the shear of the ruling congruence*
  ⓶ `CR_acoustic: D_M`  -> `P15`, *the distance slice's curvature and the recovered expansion
                                   law*

** ⛭⛭⛭ THE RULINGS ARE SHEAR-FREE BECAUSE THE SUBSTRATE HAS NO WEYL TENSOR. **  *By the Sachs
equation -- a STATED input -- the shear of a null geodesic congruence is driven by the Weyl
tensor and by nothing else.*  `Gamma` extended to Riemann and then to Weyl returns **all `256`
components zero** on the substrate, with `R = 12/alpha^2` and `Ric = (R/4) g` exactly.
  ⌈ *And the converse is `probe1`'s OWN module-level metric: the chiral plane wave has `16`
  non-zero Weyl components, so there the Sachs term is live.*  ⌊ *Batch four computed that the
  rulings are straight null lines, so their INITIAL shear is zero; this batch supplies the
  obstruction that could have grown one, and it is absent.*

⚠ ** AND ONE OF THE `256` NEEDED MORE THAN `simplify`. **  `W[1][3][3][2]` comes back as
`r (sin 2t tan t + cos 2t - 1)/(2 tan t)`, which `sympy.simplify` returns UNCHANGED and which is
identically zero.  *** A simplify that stops short reads exactly like a non-zero component. ***
*The predicate simplifies the survivors HARDER, through `expand_trig`, before counting them.*

** ⓶ AND `D_M` RECOVERS THE EXPANSION LAW EXACTLY. **  *`D_M` is `int c/H dz`, so
differentiating it must return `c/H(z)` -- and it does, to `1e-8` relative at three redshifts
spanning two decades, which is quadrature precision.  The converse is the other rate at the same
`H0`: `1e-4` to `9e-4`, four orders worse.*

Run: python3 reach_b9.py            (writes REACHED_B9.tsv)
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import extensions_b9 as Y                                          # noqa: E402

OUT = os.path.join(HERE, 'REACHED_B9.tsv')

R_ = 'receipts/L204_physics_reach/'
P_ = 'receipts/P15_CR_cosmology/'
PROBE1 = 'beyond_the_wall/probe1.py'
ACOUSTIC = 'CR_acoustic_scale_and_hubble.py'

_P1 = (R_ + 'P1_the_petrov_interval_is_complete_because_the_substrate_is_doubly_ruled.py')
_P15RATE = (P_ + 'P15_the_rate_rule_reaches_the_projection_only_through_the_identification_'
            'because_P7_gives_the_lapse_the_rate_and_the_shift_the_appearance_as_distance.py')


def _shear_detail():
    sub = Y.curvature_of('substrate')
    pw = Y.curvature_of('plane_wave')
    return (f'the substrate in the paper\'s own static chart has {sub["weyl_nonzero"]} non-zero '
            f'WEYL components of 256, with R = {Y.substrate_scalar_curvature()} and '
            f'Ric = (R/4) g exactly (Einstein: {sub["einstein"]}); probe1\'s OWN chiral plane '
            f'wave has {pw["weyl_nonzero"]} of 256. By the Sachs equation the shear of a null '
            f'geodesic congruence is driven by the Weyl tensor alone, and batch four computed '
            f'the rulings to be straight NULL lines, so their initial shear is zero -- with no '
            f'Weyl tensor there is nothing to grow one. One component of the 256 needed '
            f'expand_trig to show it was zero, a simplify stopping short reading exactly like a '
            f'real component')


def _recovery_detail():
    rows = Y.recovery_residuals()
    bad = Y.recovery_residuals(rate='cr', zs=(0.5, 5.0))
    return ('differentiating the comoving distance returns the rate exactly: '
            + '; '.join(f'at z={z:g}, dD_M/dz = {g:.4f} against c/H = {w:.4f}, rel {r:.1e}'
                        for z, g, w, r in rows)
            + f' -- quadrature precision. Against the OTHER rate at the same H0 the same '
              f'derivative misses by {bad[0][3]:.1e} and {bad[1][3]:.1e}, four orders worse, so '
              f'the agreement is that rate\'s own. And the distance slice is exactly flat, '
              f'Ricci and scalar and Kretschmann all zero (batch four, cited): '
              f'{Y.the_distance_slice_is_flat()}')


ROWS = [
    (_P1, 'the substrate\'s null rulings are shear-free', PROBE1, 'Gamma', 'EXTEND',
     Y.weyl_vanishes, 'substrate',
     'rebind the same function to `probe1`\'s OWN module-level metric -- the chiral plane wave '
     '-- where the Weyl tensor does NOT vanish and the Sachs term is live',
     'plane_wave', _shear_detail),

    (_P15RATE, 'the flatness of the distance slice together with the exact recovery of the '
     'expansion law', ACOUSTIC, 'D_M', 'EXTEND',
     Y.rate_is_recovered, 'std',
     'compare the same derivative against the OTHER rate at the same H0, where it misses by '
     'four orders more, so the agreement is that rate\'s own and not the integrator\'s',
     'cr', _recovery_detail),
]

for _r in ROWS:
    _pred, _a, _b = _r[5], _r[6], _r[8]
    assert callable(_pred), _r[0]
    assert isinstance(_pred(_a), bool) and isinstance(_pred(_b), bool), (_r[0], _pred)
    assert type(_a) is type(_b), (_r[0], 'the two inputs must be the same KIND of object')


def main():
    print()
    print('  r7283 (2) batch nine -- the last 2 EXTEND rows, 2 taken; the 12 are closed')
    print()
    bad, lines = [], [
        '# r7283 (2) BATCH NINE -- the last two EXTEND rows, both TAKEN.  One predicate per',
        '# row, called at TWO inputs of the same kind.  P1 is settled by the substrate having',
        '# NO Weyl tensor, which by the Sachs equation is the only thing that could grow shear',
        '# in a congruence of straight null lines; the converse is probe1 own plane wave, 16 of',
        '# 256 non-zero.  P15 is settled by differentiating the comoving distance and getting',
        '# the rate back to quadrature precision, against four orders worse on the other rate.',
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
    print(f'    REACHED_B9.tsv  {len(ROWS)} rows   '
          f'digest {hashlib.sha1(body.encode()).hexdigest()[:16]}')
    if bad:
        print(f'    {len(bad)} row(s) NOT reached')
        return 1
    print(f'    ** {len(ROWS)} taken, every predicate TRUE on the claim and FALSE on its '
          f'recorded converse. **')
    print('    ** THE 12 EXTEND ROWS ARE CLOSED: 4 + 6 + 2.  Of the 71-row subject, 64 are')
    print('       landed and the 7 that remain are all INPUTS -- 4 the nested-function limit')
    print('       C73 gated the decision NOT to build a capability for, and 3 refusing on a')
    print('       module-level name nothing graftable binds. **')
    print('    ⛭⛭ ** AND THE SHEAR ROW IS SETTLED BY AN ABSENCE: the substrate has NO Weyl')
    print('       tensor, which by the Sachs equation is the only thing that could grow shear in')
    print('       a congruence of straight null lines.  probe1 own plane wave has 16 of 256')
    print('       non-zero, so the obstruction exists elsewhere and is absent here. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
