#!/usr/bin/env python3
"""r7639+cc66.23: THE SEVEN BAND RATIOS ON EVERY READING -- the one row three receipts reproduce.

`cc66.46`'s seven band ratios are the reproduction target of `the_term_mix_has_the_shape`,
`the_two_channels_compose` and `the_windows_phase_spread`: each recomputes `band_std(cr) /
band_std(lcdm)` from `r6941_fine_*` and asserts it matches `cc66.46`'s published row to `5e-4`, which
is how those receipts show they RECOMPUTE the excess rather than quote it.

** ON THE ARM OF RECORD THAT TARGET MOVES, SO ALL THREE GO RED ON A LITERAL. **  The row they need is
the arm of record's, and the question is which arm-of-record row:

  ⒜ UNCARRIED, it BEATS -- band 6 collapses to `1.0141` between two bands above `1.08` while band 7
    reaches `1.1617`.  That is the alternation `r7637+70` measured and `r7639`'s ruling names: two
    combs of different period have their 0.70-wide bands cut over different parts of the cycle.
  ⒝ CARRIED, it is smooth and it is 70's OWN-COMB ROW TO FOUR DECIMALS -- computed by a different
    seat through a different code path.

⇒ *** So the target is the CARRIED row, and it is not this seat's number alone: two implementations
and two seats agree on it. ***

** VALIDATED BEFORE USE, TWICE. **  `main()` exits 1 unless
  * the NAMESAKE uncarried row reproduces `cc66.46`'s published literals -- the receipts' own
    assertion, so this file is demonstrably computing their statistic and not a lookalike; and
  * the arm-of-record CARRIED row reproduces `r7637+70`'s own-comb row as `r7639+cc66.8` recorded it.

⌗ *`cc66.46` ITSELF cannot be re-pointed: it reads `r6941_fine_cr_visleaf` and `r6929_scan_cr`, both
in the bank-gap list, and `r6929_geometry`, whose arm is a KEY with no arm-of-record entry.  Its
published row therefore stays the namesake arm's, which is why the three receipts must assert against
a row measured HERE rather than against a figure quoted from a receipt that cannot move.*
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7637_70_own_comb_statistic'))
sys.path.insert(0, HERE)
import own_comb as OC                                                          # noqa: E402
import own_comb_kinds as OCK                                                   # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
PUBLISHED = np.array([1.0215, 1.0574, 1.0519, 1.0606, 1.0748, 1.0659, 1.0762])
SEVENTY = 1.0 + np.array([0.0295, 0.0595, 0.0610, 0.0639, 0.0777, 0.0728, 0.0795])
NAMESAKE, AOR = 'r6941_fine_cr', 'r6941_fine_cr_leafrec1'


def fine(tag):
    d = np.load(os.path.join(SP, tag + '.npz'))
    return d['ls'].astype(float) / float(d['l_A']), np.asarray(d['Dl'], float)


def banks(arm):
    return {'lcdm': fine('r6941_fine_lcdm'), 'cr': fine(arm)}


def row(arm, carried):
    """`band_std(arm) / band_std(control)` over the seven bands -- the receipts' own statistic"""
    if carried:
        return OCK.band_excess_own_kind(banks(arm), 'mean', QE) + 1.0
    return OC.band_excess_shared(banks(arm), QE) + 1.0


def main():
    rows = [('namesake, uncarried -- `cc66.46`\'s published reading', row(NAMESAKE, False)),
            ('arm of record, UNCARRIED -- beats', row(AOR, False)),
            ('arm of record, CARRIED -- the target', row(AOR, True)),
            ('namesake, carried -- for completeness', row(NAMESAKE, True))]
    for name, v in rows:
        print(f'  {name:52s} ' + '  '.join(f'{x:.4f}' for x in v))
    print(f'  {"`cc66.46`s published literals":52s} ' + '  '.join(f'{x:.4f}' for x in PUBLISHED))
    print(f'  {"`r7637+70`s own-comb row":52s} ' + '  '.join(f'{x:.4f}' for x in SEVENTY))

    d_pub = float(np.max(np.abs(rows[0][1] - PUBLISHED)))
    d_70 = float(np.max(np.abs(rows[2][1] - SEVENTY)))
    unc = rows[1][1]
    print(f'\n  VALIDATION ⓵ the namesake row reproduces the published literals to {d_pub:.1e} '
          f'(the receipts assert 5e-4)')
    print(f'  VALIDATION ⓶ the carried row reproduces 70\'s own-comb row to {d_70:.1e}')
    print(f'\n  ⛔ AND THE UNCARRIED ARM-OF-RECORD ROW IS WHY THE CARRY IS NEEDED: band 6 reads '
          f'{unc[5]:.4f} between bands of {unc[4]:.4f} and {unc[6]:.4f} -- a collapse of '
          f'{100 * (1 - (unc[5] - 1) / (unc[4] - 1)):.0f} per cent in the excess between neighbours, '
          f'which is the alternation and not a feature.')
    if d_pub > 5e-4 or d_70 > 5e-5:
        print('\n⛔ THIS INSTRUMENT DOES NOT MEASURE: it fails its own reproduction check.')
        return 1
    print('\n⛭ Both reproductions hold, so the carried row is the target the three receipts assert '
          'against -- a row two seats and two code paths agree on.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
