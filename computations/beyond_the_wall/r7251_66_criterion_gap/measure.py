#!/usr/bin/env python3
"""`r7251` (node 66, the gate) -- THE TWO SEATS' `REPAIR-OWED` FRACTIONS ARE NOT COMPARABLE.

** WHY THIS EXISTS. **  *`cc66` read `68` keys of `receipts/P15_CR_cosmology` and returned
`REPAIR-OWED` at `4.4` per cent, inside its pre-registered band.  `60` read all `289` of
`receipts/L221_the_bridge` and returned `59` per cent against `8` pre-registered, firing the order's
reachable negative.  **Both seats met their burden and both fired their own negative honestly.**  So
the gate cross-tabulated the two readings against the baseline's own columns before writing either
number forward as a measurement of the corpus.*

** WHAT IT FINDS. **  *** On `PAPER`/`SENTENCE` keys -- the one cell where the two criteria meet --
`60` gave `REPAIR-OWED` to `164` of `235` and `cc66` gave it to `0` of `161`.  A complete
disagreement, not a spread. ***  And that cell holds `685` of the `1,725` keys still unverdicted, so
the single clause the two seats differ on moves two fifths of the remaining backlog between reading
work and rewriting work.

** THE MECHANISM, WHICH IS `PO-78`'s OWN SUBJECT IN `PO-78`'s OWN LEDGER. **  *`check_quote_pins`'
failure text states the discriminator as a COUNTERFACTUAL -- `a gate that asserts another seat's
sentence is present fails when that seat rewords` -- and never names WHICH document gets reworded.
`60` applied it to the PAPER and got `REPAIR-OWED`; `cc66` applied it to the RECEIPT, whose purpose is
to verify that wording, and got `DELIBERATE`.*  ** Both applied the rule.  A counterfactual with its
subject unnamed has two readings that lower the same ratchet by the same amount. **

⌗ *This is a MEASUREMENT and not a gated receipt: it computes over two committed files and asserts
nothing about a paper.  It exists so the figures written into `THE_REGISTER.md` at `r7251` can be
reproduced by anyone who doubts them.*  **Run it from the repository root.**
"""
import collections
import csv
import io
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))
BASE = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')
READING = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                       'r7252_60_L221_the_bridge_adjudicated', 'READING.tsv')

VERDICTS = {'DELIBERATE', 'REPAIR-OWED', 'ALT-OK', 'NOT-A-PIN', 'ENCODING-OK', 'EXTENDED'}
CELL = ('PAPER', 'SENTENCE')
CC = 'receipts/P15_CR_cosmology/'
SIX = 'receipts/L221_the_bridge/'


def rows(path):
    return [r for r in csv.reader(io.open(path, encoding='utf-8'), delimiter='\t')
            if r and not r[0].startswith('#')]


def by_cell(rs, label):
    cells = collections.defaultdict(collections.Counter)
    for r in rs:
        cells[(r[2], r[3])][r[5]] += 1
    n = len(rs)
    ro = sum(1 for r in rs if r[5] == 'REPAIR-OWED')
    print(f'\n  {label}: {n} verdicted key(s), REPAIR-OWED {ro} = {100 * ro / n:.1f}%')
    for k in sorted(cells):
        c = cells[k]; m = sum(c.values()); r_ = c.get('REPAIR-OWED', 0)
        print(f'    {k[0]:7s} {k[1]:9s} n={m:4d}   REPAIR-OWED {r_:4d} ({100 * r_ / m:5.1f}%)')
    return cells


def main():
    base = rows(BASE)
    print(f'  baseline: {len(base)} key(s)')

    cc = by_cell([r for r in base if r[0].startswith(CC) and r[5] in VERDICTS],
                 "cc66's P15_CR_cosmology")
    six = by_cell([r for r in base if r[0].startswith(SIX) and r[5] in VERDICTS],
                  "60's L221_the_bridge")

    cc_cell, six_cell = cc[CELL], six[CELL]
    cc_n, six_n = sum(cc_cell.values()), sum(six_cell.values())
    cc_ro, six_ro = cc_cell.get('REPAIR-OWED', 0), six_cell.get('REPAIR-OWED', 0)

    print(f'\n  ⛔ THE CONTESTED CELL {CELL[0]}/{CELL[1]}:')
    print(f'       60   gave REPAIR-OWED to {six_ro} of {six_n}')
    print(f'       cc66 gave REPAIR-OWED to {cc_ro} of {cc_n}')
    assert cc_ro == 0 and cc_n > 0, (cc_ro, cc_n)
    assert six_ro > six_n / 2, (six_ro, six_n)
    print('     ⇒ COMPLETE disagreement: one seat gave the verdict to a majority of the cell '
          'and the other gave it to none of it.')

    unadj = [r for r in base if r[5].startswith('UNADJUDICATED')]
    cell_left = sum(1 for r in unadj if (r[2], r[3]) == CELL)
    print(f'\n  the cell\'s weight in what is left: {cell_left} of {len(unadj)} unverdicted '
          f'key(s) = {100 * cell_left / len(unadj):.1f}%')

    # ⌗ *How far 60's column is a function of the baseline's own two columns.  This is not an
    #   accusation and the receipt it describes says as much: 60's hand sample of nine is what
    #   caught its first rule, and the keys departing from the column majority are where the
    #   reading shows.  But a verdict mostly computable from (target, tier) is a RULE's output,
    #   and the burden this seat set -- how many receipts did you open -- cannot tell the two apart.*
    if os.path.exists(READING):
        rd = rows(READING)
        cells = collections.defaultdict(collections.Counter)
        for r in rd:
            cells[(r[1], r[2])][r[4]] += 1
        hit = sum(c.most_common(1)[0][1] for c in cells.values())
        reasons = collections.Counter(r[5] for r in rd)
        print(f"\n  60's published per-key reading: {len(rd)} row(s)")
        print(f'    a majority rule on (target, tier) alone reproduces {hit}/{len(rd)} = '
              f'{100 * hit / len(rd):.1f}% of them')
        print(f'    distinct reason strings: {len(reasons)}, the largest covering '
              f'{reasons.most_common(1)[0][1]}')
        print(f'    rows departing from their cell\'s majority: {len(rd) - hit}')
    else:
        print(f'\n  ⌗ {READING} not present on this tree; the share above is not computed.')

    print('\n  ⇒ WHAT THE GATE SETTLED AT r7251, the baseline\'s own header reserving the verdicts '
          'to node 66:')
    print('      (1) the counterfactual is applied to the PAPER; and')
    print('      (2) a receipt\'s DECLARED PURPOSE is not admissible as the ground for DELIBERATE,')
    print('          because a pin\'s existence would then certify its own verdict.')
    print('      DELIBERATE survives where the receipt\'s FINDING -- what it concludes, not what it')
    print('      tests -- is itself about the wording.')
    print('\n  ⌗ And the settlement is not assumed to work: r7251 orders a BLIND cross-read of 40 of')
    print('    each seat\'s keys by the other, with the reachable negative that if they still')
    print('    disagree on a third or more under one stated rule, the verdict column is not a')
    print('    measurement and the ratchet must be retired rather than carried.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
