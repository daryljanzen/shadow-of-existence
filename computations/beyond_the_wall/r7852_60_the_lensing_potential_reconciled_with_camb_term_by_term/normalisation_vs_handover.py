#!/usr/bin/env python3
"""** THE TWO READINGS ORDER THE HANDOVERS OPPOSITELY, AND THE LATE ONE IS RIGHT BY CANCELLATION. **

`handover_optimum.py` found the nine bandpowers' SHAPE best at the earliest affordable handover and
worst at the latest, by a factor `2.3`.  The joint fit says the opposite, and this file says why with
one number.

** The lensing side of the joint fit carries NO fitted amplitude. **  `phiphi.py`'s own header is
explicit: `CMB = AMP e^{-2 tau} shape_cmb` and `phiphi = AMP shape_phiphi`, one primordial
normalisation shared by both, which is the whole mechanism by which `tau` acquires reach.  ⇒ So the
joint fit tests the ABSOLUTE normalisation of the lensing prediction, not only its shape, and moving
the handover moves that normalisation.

Two monotone columns, in opposite directions, with no interior compromise:

  the SHAPE        best early   (0.89 per dof at eta = 400, 2.05 at eta = 4000)
  the ABSOLUTE     best late    (the preferred amplitude approaches the held one as eta rises)

⌗ ** AND THE CLOSURE THAT MAKES THIS A DIAGNOSIS RATHER THAN A TRADE-OFF. **  The instrument's `Phi`
decays spuriously through matter domination -- `transfer_history` measured the factor between two
handovers directly, on the instrument alone.  If the late handover's absolute normalisation is right
only because that spurious decay happens to cover the deficit, then

    the spurious decay in POWER between two handovers  ==  the ratio of their normalisation deficits

and the two are computed here from independent records and compared.  ** If they agree, the
instrument's absolute lensing normalisation at the landed handover is a CANCELLATION of two errors
and not a correctness. **  The reachable negative is that they disagree, in which case the
normalisation is right for some other reason and this file says so.

⚠ The held amplitude comes from the CMB fit and does NOT depend on which growth carries `Phi`, which
is why one held value serves every row.

Run: python3 normalisation_vs_handover.py        (writes normalisation_vs_handover.json)
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
R7850 = os.path.join(_BTW, 'r7850_60_phi_carried_through_the_radiation_era')

# ** read from r7846's own run record rather than retyped from a reply. **
HELD = json.load(io.open(os.path.join(R7846, 'lensing_informative.json'),
                         encoding='utf-8'))['amp_held']

PIVOT_K = 0.05          # the mode the shape comparison normalises at
DECAY_FROM, DECAY_TO = 500.0, 4000.0


def main():
    ho = json.load(io.open(os.path.join(_HERE, 'handover_optimum.json'), encoding='utf-8'))
    th = json.load(io.open(os.path.join(
        _HERE, 'transfer_history_eta500-914-1400-1893-2500-3200-4000.json'), encoding='utf-8'))

    print('\n  the held amplitude, from the CMB fit and independent of the growth: %.6e' % HELD)
    print('\n  THE TWO READINGS, over every banked handover')
    print('    eta       z        shape (per dof)   preferred amp    preferred/held   per cent low')
    rows = []
    for r_ in ho['rows']:
        ratio = r_['amplitude'] / HELD
        rows.append(dict(eta=r_['eta'], z=r_['z'], per_dof=r_['per_dof'],
                         preferred=r_['amplitude'], ratio=ratio,
                         per_cent_low=100.0 * (1.0 - ratio)))
        print('    %6.0f  %8.3f   %13.4f   %.6e   %12.6f   %10.2f'
              % (r_['eta'], r_['z'], r_['per_dof'], r_['amplitude'], ratio,
                 100.0 * (1.0 - ratio)))

    best_shape = min(rows, key=lambda r_: r_['per_dof'])
    best_abs = min(rows, key=lambda r_: abs(1.0 - r_['ratio']))
    shape_order = [r_['eta'] for r_ in sorted(rows, key=lambda r_: r_['per_dof'])]
    abs_order = [r_['eta'] for r_ in sorted(rows, key=lambda r_: abs(1.0 - r_['ratio']))]
    # ⚠ ** THE CLAIM IS MADE ONLY WHERE IT IS TRUE, and the first draft here overclaimed. **  The
    #   shape's best is NOT the absolute's worst over the whole range: below the shape's minimum
    #   BOTH readings are bad, so the earliest handovers are worst on both.  What is true, and is
    #   what the fork rests on, is that FROM the shape's minimum ONWARD the two are strictly
    #   monotone and in opposite directions.
    tail = [r_ for r_ in rows if r_['eta'] >= best_shape['eta']]
    shape_worsens = all(tail[i + 1]['per_dof'] > tail[i]['per_dof'] for i in range(len(tail) - 1))
    abs_improves = all(tail[i + 1]['ratio'] > tail[i]['ratio'] for i in range(len(tail) - 1))
    opposed_on_tail = bool(shape_worsens and abs_improves)
    abs_monotone_everywhere = all(rows[i + 1]['ratio'] > rows[i]['ratio']
                                  for i in range(len(rows) - 1))
    print('\n    the SHAPE is best at eta = %.0f (%.4f per dof); the ABSOLUTE is best at the '
          'LATEST probed, eta = %.0f (%.2f per cent low)'
          % (best_shape['eta'], best_shape['per_dof'], best_abs['eta'],
             best_abs['per_cent_low']))
    print('    the absolute improves monotonically over all %d handovers: %s'
          % (len(rows), abs_monotone_everywhere))
    print('    ⇒ from the shape\'s minimum onward the two readings are %s -- the shape worsens at '
          'every step (%s) while the absolute improves at every step (%s), over the %d handovers '
          'from eta = %.0f to eta = %.0f'
          % ('STRICTLY OPPOSED' if opposed_on_tail else 'not strictly opposed',
             shape_worsens, abs_improves, len(tail), tail[0]['eta'], tail[-1]['eta']))
    print('    ⌗ Below the shape\'s minimum BOTH are bad, so the earliest handovers are worst on '
          'both and there is no compromise to be had at that end either.', flush=True)

    # ── the closure
    kstr = 'k%.4g' % PIVOT_K
    if kstr not in th['frozen_ratio_to_last']:
        kstr = min(th['frozen_ratio_to_last'],
                   key=lambda s: abs(float(s[1:]) - PIVOT_K))
    etas = th['etas']
    i_from = etas.index(DECAY_FROM)
    phi_ratio = th['frozen_ratio_to_last'][kstr][i_from]        # Phi(eta_from)/Phi(eta_to)
    decay_power = phi_ratio ** 2
    r_from = next(r_ for r_ in rows if r_['eta'] == DECAY_FROM)['ratio']
    r_to = next(r_ for r_ in rows if r_['eta'] == DECAY_TO)['ratio']
    deficit_ratio = r_to / r_from
    rel = abs(decay_power / deficit_ratio - 1.0)
    print('\n  THE CLOSURE, from two independent records')
    print('    the instrument\'s own spurious decay at %s between eta = %.0f and %.0f:'
          % (kstr, DECAY_FROM, DECAY_TO))
    print('      Phi falls by a factor %.5f, so the POWER falls by %.5f' % (phi_ratio, decay_power))
    print('    the normalisation deficit it would have to cover:')
    print('      preferred/held goes %.6f -> %.6f, a factor %.5f' % (r_from, r_to, deficit_ratio))
    print('    ⇒ the two agree to %.2f per cent' % (100 * rel))
    verdict = ('the late handover\'s absolute normalisation is a CANCELLATION of two errors'
               if rel < 0.05 else
               'the two do not agree, so the normalisation is right for some other reason')
    print('    ** %s **' % verdict, flush=True)

    out = dict(held_amplitude=HELD, pivot_k=PIVOT_K, pivot_key_used=kstr,
               rows=rows,
               best_shape=dict(eta=best_shape['eta'], per_dof=best_shape['per_dof']),
               best_absolute=dict(eta=best_abs['eta'], per_cent_low=best_abs['per_cent_low']),
               shape_order_best_first=shape_order, absolute_order_best_first=abs_order,
               opposed_from_shape_minimum_onward=opposed_on_tail,
               shape_worsens_monotonically_after_its_minimum=bool(shape_worsens),
               absolute_improves_monotonically_after_it=bool(abs_improves),
               absolute_improves_monotonically_everywhere=bool(abs_monotone_everywhere),
               tail_etas=[r_['eta'] for r_ in tail],
               closure=dict(decay_from=DECAY_FROM, decay_to=DECAY_TO,
                            phi_ratio=phi_ratio, decay_in_power=decay_power,
                            normalisation_deficit_ratio=deficit_ratio,
                            relative_disagreement=rel, agrees_within_5_per_cent=bool(rel < 0.05),
                            verdict=verdict),
               note=('the lensing side of the joint fit carries no fitted amplitude, so the joint '
                     'fit tests the absolute normalisation and the nine-bandpower chi^2 with one '
                     'amplitude fitted tests only the shape'))
    with io.open(os.path.join(_HERE, 'normalisation_vs_handover.json'), 'w',
                 encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote normalisation_vs_handover.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
