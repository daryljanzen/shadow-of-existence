# -*- coding: utf-8 -*-
"""r7879+cc66 item ⑮ (completion) -- THE SECOND FITTER ON `60`'s FIVE NEWLY BANKED LEGS.

⛔ FIVE, NOT SIX.  `69`'s order says six, "all four of the decomposition plus the two `c_a²` arms".
   `60`'s `parts/` holds `W`, `C`, `E`, `CE` and `A1`, and `60`'s own `refit_parts.json` and
   `leverage.json` both record `arms = ['A1','C','CE','E','W']`: four decomposition legs plus ONE
   `c_a²` arm.  The five that exist are run and named.

⛔ THE SAME INSTRUMENT.  This imports `r7875`'s fitter and CAMB leg through `r7877`'s module rather
   than re-implementing either, and re-derives `r7875`'s four landed amplitudes before any leg is
   read.  The zero leg is the LANDED one, `60`'s choice and their stated reason: `NUFD` is gated on
   a non-zero sum.

⛔ AND THE SEPARATION FLOOR DECIDES WHAT AN AGREEMENT IS WORTH.  At `r7877` the `EE` on-off
   separation fell eighty times below my own interpolation floor, so the `EE` agreement confirmed
   the BANK READING and not the leg.  Every leg pair is checked against that floor here.

    NODE=cc66 python3 legs_five.py
"""
import io
import json
import os
import sys
import itertools

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(_BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
R7877 = os.path.join(_BTW, 'r7877_cc66_the_second_fitter_on_60s_repair_legs')
R7878 = os.path.join(_BTW, 'r7878_60_the_three_changes_decomposed_and_the_exact_adiabatic_'
                           'sound_speed')
sys.path.insert(0, R7877)
import refit_legs as RL                                                     # noqa: E402
AC = RL.AC

PARTS = os.path.join(R7878, 'parts')
OUT = os.path.join(_HERE, 'legs_five.json')
LEGS = ('W', 'C', 'E', 'CE', 'A1')
SUMS = (0.30, 0.60)
BLOCKS = ('TT', 'EE')
KEY = {'TT': 'Dl', 'EE': 'Dl_EE'}
BAR = 0.03                      # 69's refined joint bar at r7879
FLOOR = {'TT': 3.515263913511646e-06, 'EE': 5.307332502169082e-05}

TARGET = {
    ('W', 'TT', 0.30): 0.9951026561, ('W', 'TT', 0.60): 1.0562071519,
    ('W', 'EE', 0.30): 0.9599546392, ('W', 'EE', 0.60): 0.9403878391,
    ('C', 'TT', 0.30): 1.1311121927, ('C', 'TT', 0.60): 1.2639430128,
    ('C', 'EE', 0.30): 1.0123697443, ('C', 'EE', 0.60): 1.0436064977,
    ('E', 'TT', 0.30): 1.0546424534, ('E', 'TT', 0.60): 1.1390197499,
    ('E', 'EE', 0.30): 1.0006047992, ('E', 'EE', 0.60): 1.0201940348,
    ('CE', 'TT', 0.30): 1.0875896605, ('CE', 'TT', 0.60): 1.1895169477,
    ('CE', 'EE', 0.30): 1.0076871380, ('CE', 'EE', 0.60): 1.0342429157,
    ('A1', 'TT', 0.30): 0.9211487566, ('A1', 'TT', 0.60): 0.9078647914,
    ('A1', 'EE', 0.30): 0.9535035823, ('A1', 'EE', 0.60): 0.9277492001,
}


def leg_ratio(leg, s, blk):
    p = os.path.join(PARTS, 'lcdm_S%03d%s_pol.npz' % (int(round(s * 100)), leg))
    if not os.path.exists(p):
        return None, None
    ls = RL._npz(RL.LANDED_ZERO, 'ls').astype(int)
    d0 = RL._npz(RL.LANDED_ZERO, KEY[blk])
    ds = RL._npz(p, KEY[blk])
    m = (ls >= AC.L_LO) & (ls <= AC.L_HI)
    return ls[m].astype(float), (ds / d0 - 1.0)[m]


def main():
    print(__doc__)
    print('=' * 100)
    con = AC.control()
    out = {'control': con, 'legs': list(LEGS), 'bar': BAR, 'floors': FLOOR,
           'window': [AC.L_LO, AC.L_HI], 'legs_in_order_but_absent': []}
    print('\n  Ⓐ① control %s; tau %.3f; lmax %d; band %d-%d; 60\'s 41 multipoles'
          % (con, AC.TAU, AC.LMAX, AC.L_LO, AC.L_HI))
    print('\n  ⛔ FIVE legs banked (%s). 69\'s order names six; 60\'s own records name five.'
          % ', '.join(LEGS))

    CA = {}
    for s in (0.0,) + SUMS:
        CA[s], _, _ = AC.camb_one(con, s)
    l_dense = np.arange(2, AC.LMAX + 1, dtype=float)
    g = np.linspace(-0.08, 0.08, 3201)

    # ── the regression control, same instrument ──
    print('\n  Ⓐ①b THE REGRESSION CONTROL -- r7875\'s four landed amplitudes, re-derived')
    worst_reg, reg = 0.0, {}
    for blk in BLOCKS:
        for s in SUMS:
            ls = AC.bank_arr(AC.TAGS[0.0], 'ls')
            r_i = AC.bank_arr(AC.TAGS[s], KEY[blk]) / AC.bank_arr(AC.TAGS[0.0], KEY[blk]) - 1.0
            m = (ls >= AC.L_LO) & (ls <= AC.L_HI)
            rc = CA[s][2:AC.LMAX + 1, AC.COL[blk]] / CA[0.0][2:AC.LMAX + 1, AC.COL[blk]] - 1.0
            e0 = AC.fit_A_eps(ls[m].astype(float), r_i[m], l_dense, rc, g)[0]
            _, A, _ = AC.refine(ls[m].astype(float), r_i[m], l_dense, rc, e0)
            d = abs(A - RL.R7875_LANDED[(blk, s)])
            worst_reg = max(worst_reg, d)
            reg['%s|%.2f' % (blk, s)] = dict(A=float(A), diff=float(d))
    out['regression_worst'] = float(worst_reg)
    print('      worst %.3e   %s' % (worst_reg, 'PASSES' if worst_reg < 1e-9 else '⛔ FAILS'))
    if worst_reg >= 1e-9:
        out['legs_read'] = False
        io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
        return

    # ── Ⓑ② the twenty fits ──
    print('\n  Ⓑ② THE TWENTY FITS, against 60\'s own figures')
    fits = {}
    for leg in LEGS:
        for blk in BLOCKS:
            for s in SUMS:
                lo, r_i = leg_ratio(leg, s, blk)
                if lo is None:
                    out['legs_in_order_but_absent'].append('%s|%s|%.2f' % (leg, blk, s))
                    continue
                rc = CA[s][2:AC.LMAX + 1, AC.COL[blk]] / CA[0.0][2:AC.LMAX + 1, AC.COL[blk]] - 1.0
                e0 = AC.fit_A_eps(lo, r_i, l_dense, rc, g)[0]
                e, A, res = AC.refine(lo, r_i, l_dense, rc, e0)
                tgt = TARGET[(leg, blk, s)]
                d = abs(A - tgt)
                fits['%s|%s|%.2f' % (leg, blk, s)] = dict(
                    A=float(A), eps=float(e), resid=float(res), target_60=tgt,
                    diff_from_60=float(d), hits=bool(d < 0.005),
                    dist_from_unity=float(abs(A - 1.0)),
                    within_bar=bool(abs(A - 1.0) <= BAR), n=int(lo.size))
    out['fits'] = fits
    out['legs_read'] = True
    out['n_hits'] = sum(1 for v in fits.values() if v['hits'])
    out['worst_diff'] = float(max(v['diff_from_60'] for v in fits.values()))
    for leg in LEGS:
        row = []
        for blk in BLOCKS:
            for s in SUMS:
                v = fits.get('%s|%s|%.2f' % (leg, blk, s))
                row.append('%s%.2f %.7f (60 %.7f, |d| %.1e)%s'
                           % (blk, s, v['A'], v['target_60'], v['diff_from_60'],
                              '' if v['hits'] else ' ⛔'))
        print('      %-3s %s' % (leg, '  '.join(row[:2])))
        print('          %s' % '  '.join(row[2:]))
    print('      ⇒ %d of %d within 0.005; worst %.6e'
          % (out['n_hits'], len(fits), out['worst_diff']))

    # ── Ⓓ④ against 69's refined joint bar ──
    print('\n  Ⓓ④ AGAINST 69\'s REFINED BAR: TT and EE both within %.2f of unity' % BAR)
    bar = {}
    for leg in LEGS:
        ok = all(fits['%s|%s|%.2f' % (leg, b, s)]['within_bar']
                 for b in BLOCKS for s in SUMS)
        worst_blk = max(((b, s, fits['%s|%s|%.2f' % (leg, b, s)]['dist_from_unity'])
                         for b in BLOCKS for s in SUMS), key=lambda t: t[2])
        bar[leg] = dict(passes=bool(ok), worst_block=worst_blk[0],
                        worst_sum=worst_blk[1], worst_dist=float(worst_blk[2]))
        print('      %-3s %s -- worst is %s at %.2f, |A-1| = %.6f'
              % (leg, 'PASSES' if ok else 'fails', worst_blk[0], worst_blk[1], worst_blk[2]))
    out['bar'] = BAR
    out['against_bar'] = bar
    nearest = min(bar.items(), key=lambda kv: kv[1]['worst_dist'])
    out['nearest_leg'] = nearest[0]
    out['nearest_worst_dist'] = nearest[1]['worst_dist']
    out['any_passes_bar'] = bool(any(v['passes'] for v in bar.values()))
    print('      ⇒ %s; the nearest is %s, worst |A-1| = %.6f'
          % ('at least one passes' if out['any_passes_bar'] else 'NO leg passes the joint bar',
             nearest[0], nearest[1]['worst_dist']))

    # ── Ⓒ③ the separation floor, pair by pair ──
    print('\n  Ⓒ③ CAN THIS FITTER TELL THE LEGS APART? -- against my own floors')
    sep = {}
    for a, b in itertools.combinations(LEGS, 2):
        for blk in BLOCKS:
            for s in SUMS:
                ka, kb = '%s|%s|%.2f' % (a, blk, s), '%s|%s|%.2f' % (b, blk, s)
                if ka not in fits or kb not in fits:
                    continue
                mine = abs(fits[ka]['A'] - fits[kb]['A'])
                theirs = abs(TARGET[(a, blk, s)] - TARGET[(b, blk, s)])
                sep['%s-%s|%s|%.2f' % (a, b, blk, s)] = dict(
                    mine=float(mine), theirs=float(theirs), floor=FLOOR[blk],
                    resolvable=bool(mine > FLOOR[blk]))
    out['separation'] = sep
    unres = {k: v for k, v in sep.items() if not v['resolvable']}
    out['n_pairs'] = len(sep)
    out['n_unresolvable'] = len(unres)
    print('      %d leg-pair comparisons; %d fall BELOW my floor and confirm the bank reading, '
          'not the leg' % (len(sep), len(unres)))
    for k, v in sorted(unres.items())[:6]:
        print('          ⛔ %-18s mine %.3e vs floor %.3e' % (k, v['mine'], v['floor']))

    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
