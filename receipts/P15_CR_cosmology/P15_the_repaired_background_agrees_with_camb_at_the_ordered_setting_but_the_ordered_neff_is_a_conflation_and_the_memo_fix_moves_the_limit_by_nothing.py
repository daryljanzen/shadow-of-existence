#!/usr/bin/env python3
"""P15, r7865+cc66, on 69's order r7865 items ③ and ⑦.

COMPUTES: nothing of its own.  Every cosmological parameter is the control's, 60's instrument's or
`r7853`'s profile's, and every figure is read from `background_read.json` and `exact_memo_read.json`
rather than derived beside the assertion.  No parameter is pinned as this receipt's own.

** ⛭ 60's REPAIRED BACKGROUND AGREES WITH CAMB AT THE ORDERED SETTING ON ALL FOUR BANDS -- AND THE
ORDERED N_eff IS A CONFLATION, THE TRUE GAP BEING 0.044 AND NOT 0.0293.  ⛔ AT THE CORRECT FIGURE
THE DENSITY AND H(z) BOTH IMPROVE WHILE THE DRAG RULER CROSSES BELOW CAMB's AT THE TWO LOWEST SUMS,
SO N_eff ALONE DOES NOT ACCOUNT FOR THE RESIDUAL.  ⛭ AND DROPPING THE ROUNDED MEMO MOVES 54.00 meV
BY NOTHING AT THE ARM OF RECORD'S OWN RESOLUTION, WHILE MAKING THAT ARM RE-DERIVABLE FOR THE FIRST
TIME. **

Bands Ⓐ-Ⓖ were registered at `r7865+cc66.1` (`467ab3d8a`) BEFORE either computation existed.  All
seven hold; the two findings above are not band failures but things the bands were built to expose.
Item ⑧ waits on 60 publishing its per-bin `dchi2/dSum`.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
WORK = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7865_cc66_the_repaired_background_checked_and_the_rounded_memo_dropped')
B = json.load(open(os.path.join(WORK, 'background_read.json')))
M = json.load(open(os.path.join(WORK, 'exact_memo_read.json')))
S = B['settings']
ORD, UNS, MEA = S['ordered_0.0293'], S['unset'], S['measured_0.044']
RAN, FAILED = [], []


def check(label, ok, got=''):
    RAN.append(label)
    print('    %-5s %s%s' % ('OK' if ok else 'FAIL', label, ('   (got %s)' % got) if got else ''))
    if not ok:
        FAILED.append(label)


print(__doc__)
print('=' * 99)
print('** ③ THE REPAIRED BACKGROUND AGAINST CAMB, AT THREE SETTINGS OF THE CORRECTION **')
print('=' * 99)
print()
print('  setting            rho rel     H worst     at z     ruler        worst gap   below')
for name, d in (('DNEFF unset', UNS), ('+0.0293 ORDERED', ORD), ('+0.044 measured', MEA)):
    print('  %-17s %.3e   %.3e   %6d   %-10s   %.3e   %d'
          % (name, d['rho_rel'], d['H_worst'], d['H_worst_at_z'],
             'all above' if d['all_above'] else 'TWO BELOW', d['worst_abs_gap'], d['n_below']))
print()

check('Ⓐ① ** Ⓐ HOLDS EXACTLY: the CAMB leg built in this revision\'s own file reproduces 60\'s '
      'recorded reference column to `0.000e+00` at all four sums ** -- the band allowed `1e-05`, and '
      'this is what makes every comparison below a reproduction rather than two unrelated numbers',
      B['worst_rel_vs_sixty_camb'] == 0.0,
      '%.3e' % B['worst_rel_vs_sixty_camb'])

check('Ⓑ② ** Ⓑ HOLDS at the ordered setting: the instrument\'s drag ruler sits ABOVE CAMB\'s at all '
      'four sums and the gap is monotone in the sum **',
      ORD['all_above'] and ORD['monotone'] and ORD['n_below'] == 0,
      'above %s monotone %s' % (ORD['all_above'], ORD['monotone']))

check('Ⓒ③ ** Ⓒ HOLDS: the worst gap at the ordered setting is `2.366e-03` against the `5e-03` the '
      'other seat registered ** -- so the repair passes its own gate at the setting the control is '
      'to be run at, and not only at the one it was developed on',
      abs(ORD['worst_abs_gap'] - 2.366e-03) < 5e-07 and ORD['worst_abs_gap'] < 5.0e-03,
      '%.3e' % ORD['worst_abs_gap'])

check('Ⓓ④ ** Ⓓ HOLDS ON BOTH LIMBS: `H(z)` agrees to `5.531e-04` at worst, inside the registered '
      '`2e-03`, AND the worst point is the earliest one ** -- a background error smallest early and '
      'largest late would be a different defect from the one this repair addresses',
      ORD['H_worst'] < 2.0e-03 and ORD['H_worst_at_z'] == 1100
      and abs(ORD['H_worst'] - 5.531e-04) < 5e-07,
      '%.3e at z=%d' % (ORD['H_worst'], ORD['H_worst_at_z']))

check('Ⓔ⑤ ** Ⓔ HOLDS: the correction is worth a factor `4.49` on the density, against a registered '
      'three, and lands at `2.760e-03` inside `5e-03` ** -- and both legs are measured HERE, because '
      'a diagnosis checked only by the seat that made it is not checked',
      B['rho_improvement_ordered'] > 3.0 and ORD['rho_rel'] < 5.0e-03
      and abs(B['rho_improvement_ordered'] - 4.49) < 5e-03,
      'x%.3f to %.3e' % (B['rho_improvement_ordered'], ORD['rho_rel']))

# -- the order's own figure, measured --------------------------------------------------------------
print()
O = B['order_figure']
print('  the order says the reference uses %.4f; the object it builds reports:' % O['order_says'])
print('    N_eff %.6f    num_massless %.6f    massive %d    massless + 1 = %.6f'
      % (O['N_eff'], O['num_massless'], O['num_massive'], O['massless_plus_integer']))
print()

check('Ⓕ⑥ ⛔ ** THE ORDERED `N_eff` FIGURE IS A CONFLATION, AND THE ARITHMETIC NAMES IT: the ordered '
      'value equals the EFFECTIVE massless count plus the INTEGER massive count, where the massive '
      'neutrino contributes `1.0147` in those units and not `1` ** -- which is exactly why the '
      'massless figure is not two',
      abs(O['massless_plus_integer'] - O['order_says']) < 5e-05
      and abs(O['N_eff'] - O['massless_plus_integer']) > 1e-02
      # the pieces pinned two-sidedly, since the sum is what hides a conflation of them
      and abs(O['num_massless'] - 2.029333) < 5e-07
      and abs(O['massless_plus_integer'] - 3.029333) < 5e-07
      and abs(O['N_eff'] - O['num_massless'] - 1.0147) < 5e-05,
      'massless %.6f + 1 = %.6f, the massive one worth %.6f, and N_eff %.6f'
      % (O['num_massless'], O['massless_plus_integer'],
         O['N_eff'] - O['num_massless'], O['N_eff']))

check('Ⓕ⑦ ⇒ ** so the gap from the other seat\'s three is `0.044000` and the ordered correction '
      'leaves `0.0147` unaccounted **',
      abs(O['gap_to_three'] - 0.044) < 5e-07
      and abs(O['gap_to_three'] - O['order_says'] + 3.0 - 0.0147) < 5e-05,
      '%.6f, leaving %.6f' % (O['gap_to_three'], O['gap_to_three'] - O['order_says'] + 3.0))

check('Ⓕ⑧ ⛭ ** AND THE CORRECT FIGURE IS NOT UNIFORMLY BETTER, WHICH IS THE FINDING RATHER THAN THE '
      'CORRECTION: at `+0.044` the density improves to a factor `5.97` and `H` at the earliest point '
      'to `3.122e-04`, both monotone in the correction and so corroborating it -- BUT the ruler '
      'CROSSES BELOW CAMB\'s at the two lowest sums, where the ordered figure leaves it uniformly '
      'above **',
      B['rho_improvement_measured'] > B['rho_improvement_ordered']
      and MEA['H_worst'] < ORD['H_worst'] and MEA['n_below'] == 2 and not MEA['all_above']
      and abs(B['rho_improvement_measured'] - 5.97) < 5e-03
      and abs(MEA['H_worst'] - 3.122e-04) < 5e-08,
      'x%.2f and %.3e, with %d sums below' % (B['rho_improvement_measured'], MEA['H_worst'],
                                              MEA['n_below']))

check('Ⓕ⑨ ⇒ ** so a residual remains that the neutrino count alone does not account for **, since '
      'no single value of the correction makes the density, the expansion rate and the ruler all '
      'best at once -- the ordered one is best on the ruler and the measured one on the other two',
      ORD['all_above'] and not MEA['all_above']
      and MEA['rho_rel'] < ORD['rho_rel'] and MEA['H_worst'] < ORD['H_worst'],
      'ordered keeps the ruler above; measured wins rho and H')

# -- item ⑦ ---------------------------------------------------------------------------------------
print()
print('=' * 99)
print('** ⑦ THE ROUNDED MEMO DROPPED: DOES 54.00 meV MOVE? **')
print('=' * 99)
print()
print('  crossing grid        step meV      landed       exact       moved')
for k in ('published_20001', 'fine_400001'):
    g = M['grids'][k]
    print('  %-18s   %.4f    %9.5f   %9.5f   %+.5f'
          % (k, g['step_meV'], g['landed'], g['exact'], g['moved']))
print()

_pub = M['grids']['published_20001']
check('Ⓖ⑩ ** Ⓕ HOLDS IN THE STRONGEST FORM THE QUESTION ADMITS: on the arm of record\'s OWN crossing '
      'resolution the limit does not move at all ** -- `54.00000` before and after, where the band '
      'allowed half a milli-electronvolt',
      abs(_pub['moved']) < 1e-09 and abs(_pub['landed'] - 54.0) < 5e-06
      and abs(_pub['exact'] - 54.0) < 5e-06,
      'landed %.5f, exact %.5f, moved %+.5f' % (_pub['landed'], _pub['exact'], _pub['moved']))

_fine = M['grids']['fine_400001']
check('Ⓖ⑪ ⌗ and a grid twenty times finer BOUNDS any movement that resolution could have hidden at '
      '`0.001` meV, which is reported because the coarse grid alone would hide the bound and the '
      'fine grid alone would understate the answer',
      abs(abs(_fine['moved']) - 0.001) < 5e-06 and _fine['step_meV'] < _pub['step_meV'],
      '%+.5f meV at a %.4f meV step' % (_fine['moved'], _fine['step_meV']))

_w = M['rederive_worst']
check('Ⓖ⑫ ⛭⛭ ** Ⓖ HOLDS EXACTLY, AND IT IS THE SHARP ONE: re-scoring each NEWLY banked point at its '
      'own recorded five parameters reproduces its recorded total to ZERO on every term and on the '
      'total, at all eight sums ** -- so the minimised arm of record is re-derivable from its own '
      'recorded parameters for the first time',
      all(v == 0.0 for v in _w.values()),
      'worst over 5 quantities: %s' % max(_w.values()))

check('Ⓖ⑬ ⌗ and the worst single-point move in total is `0.005558`, INSIDE the `6.185e-03` residue '
      'this seat attributed to the rounded key BEFORE re-running -- so the diagnosis predicted the '
      'size of its own repair\'s effect, which is the only independent check available on it',
      M['worst_move_in_total'] < M['residue_attributed']
      and abs(M['worst_move_in_total'] - 0.005558) < 5e-07,
      '%.6f against %.6f' % (M['worst_move_in_total'], M['residue_attributed']))

check('Ⓖ⑭ ⌗ and every one of the eight re-run points is INTERIOR to the box, so none of this is a '
      'boundary artefact',
      M['all_interior'], '%s' % M['all_interior'])

print()
check('Ⓗ⑮ ** fourteen arms ran before this one and every one was adjudicated **, the count read off '
      'the list the check function itself appends rather than typed beside them',
      len(RAN) == 14 and len(set(RAN)) == 14, '%d arms, %d distinct' % (len(RAN), len(set(RAN))))

print()
print('=' * 99)
print('  ✔ ** ALL SEVEN REGISTERED BANDS HOLD. **  The repaired background agrees with CAMB at the')
print('    ordered setting on the ruler, H(z) and the density, and dropping the rounded memo moves')
print('    54.00 meV by nothing while making the minimised arm re-derivable for the first time.')
print('  ⛔ ** AND TWO THINGS THE BANDS WERE BUILT TO EXPOSE: the ordered N_eff is 2.0293 + 1 and')
print('    the true gap is 0.044; and at that correct figure the density and H both improve while')
print('    the ruler crosses below CAMB at the two lowest sums -- so N_eff alone does not account')
print('    for the residual, and no single value is best on all three at once. **')
print('=' * 99)
if FAILED:
    print('  %d FAILED: %s' % (len(FAILED), FAILED))
    raise SystemExit(1)
print('  ALL CHECKS PASS')
