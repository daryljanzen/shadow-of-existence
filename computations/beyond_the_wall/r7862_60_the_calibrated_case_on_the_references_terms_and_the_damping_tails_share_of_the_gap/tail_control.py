# -*- coding: utf-8 -*-
"""Ⓒ③ᵈ -- ** NOT A REGISTERED ARM.  THE CONTROL Ⓒ③ LACKED, ADDED AFTER ITS CRITERION FAILED. **

⛔ *`Ⓒ③`'s registered criterion -- less than half of the `15.97` meV gap moves with the cut -- FAILED,
and it failed at the DEEPEST cut: `ell = 1200` drops `189` of `555` bandpowers and the limit loosens
by `36.66` meV, which is `-2.295` of the gap.  The criterion as registered has no control for
INFORMATION LOSS: a cut that removes a third of the data will move a limit whether or not the
multipoles it removed carried any residual at all.*

**So this file measures the control the registered leg should have carried, and it does not touch
`Ⓒ③`'s criterion or its numbers.**  For each registered cut, the SAME NUMBER of bandpowers is
dropped from the LOW-`ell` end of each block instead of the high end, and the limit is re-read. *If
the low-end cut moves the limit as far as the high-end cut did, the move is the data's volume and
not the damping tail's residual -- which is the question `r7861` item ② actually asks.*

⌗ *This is declared as added after the fact, in its own file, rather than folded back into `Ⓒ③` as
though it had been registered.  The registered arm stands as it was written and as it failed.*

    python3 tail_control.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import tail_share as TS                                                     # noqa: E402

PAIRS = ((1500, 90), (1200, 189), (1800, 36))     # the cuts Ⓒ③ ran and the counts each dropped


def narrow_low(mod, SC, M3, n_per_block):
    """drop the LOWEST-`ell` bandpowers of each block, `n_per_block` of them, consistently"""
    ok = mod.cmb.ok
    keep = np.ones(int(ok.sum()), bool)
    blk = SC.BLOCK[ok]
    lo = SC.BIN_LO[ok]
    for b in (0, 1, 2):
        idx = np.where(blk == b)[0]
        order = idx[np.argsort(lo[idx])]
        keep[order[:n_per_block]] = False
    newok = ok.copy()
    newok[ok] = keep
    base, g, h = mod.cmb.base, dict(mod.cmb.g), dict(mod.cmb.h)
    mod.cmb.base = lambda s, _o=base, _k=keep: np.asarray(_o(s), float)[_k]
    mod.cmb.g = {k: (lambda s, _o=g[k], _k=keep: np.asarray(_o(s), float)[_k]) for k in M3.KEYS4}
    mod.cmb.h = {k: (lambda s, _o=h[k], _k=keep: np.asarray(_o(s), float)[_k]) for k in M3.KEYS4}
    mod.cmb.ok = newok
    mod.cmb.nb = int(newok.sum())
    mod.cmb.F = SC.fisher_for(newok)
    mod.cmb.d = SC.X_DATA[newok]
    mod.cmb.pos = SC.POSITIVE[newok]
    return dict(bins_before=int(ok.sum()), bins_after=int(newok.sum()),
                dropped=int(ok.sum() - newok.sum()), per_block=int(n_per_block),
                ell_lo_after=int(SC.BIN_LO[newok].min()),
                ell_hi_after=int(SC.BIN_HI[newok].max()))


def main():
    print(__doc__)
    print('=' * 100)
    import model3 as M3
    import model6 as M6
    import score_ttteee as SC

    prev = json.load(io.open(os.path.join(_HERE, 'tail_share.json'), encoding='utf-8'))
    base_limit = prev['baseline']['limit_meV']
    gap = prev['gap_full_meV']
    sums = prev['baseline']['sums']
    out = dict(baseline_limit_meV=base_limit, gap_full_meV=gap, pairs=[list(p) for p in PAIRS],
               rows={})
    print('\n    the baseline this control differences against is Ⓒ③\'s own: %.2f meV, gap %.2f meV'
          % (base_limit, gap))

    for lcut, total in PAIRS:
        n = total // 3
        mod = M6.Model6('lcdm')
        raw = mod.amp_cmb
        mod.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0
        info = narrow_low(mod, SC, M3, n)
        hi = prev['cuts'][str(lcut)]
        print('\n    ** against the cut at ell = %d (%d dropped, limit %s meV, move %s) **'
              % (lcut, total,
                 ('%.2f' % hi['limit_meV']) if hi.get('limit_meV') is not None else 'none',
                 ('%+.2f' % hi['moved_meV']) if hi.get('moved_meV') is not None else 'none'))
        print('    the LOW-end control drops %d of %d (%d per block); bins now span %d to %d'
              % (info['dropped'], info['bins_before'], n,
                 info['ell_lo_after'], info['ell_hi_after']))
        res = TS.profile(mod, sums, 'THE LOW-END CONTROL for the cut at ell = %d' % lcut)
        res['info'] = info
        if res['limit_meV'] is not None:
            res['moved_meV'] = base_limit - res['limit_meV']
            res['share_of_gap'] = res['moved_meV'] / gap
            res['high_end_moved_meV'] = hi.get('moved_meV')
            res['ratio_to_high_end'] = (
                None if not hi.get('moved_meV') else res['moved_meV'] / hi['moved_meV'])
            # ⌗ *the comparison is which END costs more, and the verdict is worded as that
            #   rather than as a sameness: these two moves are not of the same order at all.*
            res['low_end_costs_more'] = bool(hi.get('moved_meV') is not None
                                             and abs(res['moved_meV']) > abs(hi['moved_meV']))
            print('    ⇒ the low-end control moves %+.2f meV against the high end\'s %+.2f'
                  % (res['moved_meV'], hi['moved_meV']))
            print('      %s' % (
                ('the SAME COUNT of bandpowers costs %.1f times more at the low end, so the '
                 'high-ell bandpowers carry little of this limit and the high-end move is the '
                 'DATA\'S VOLUME and not the tail\'s residual'
                 % abs(res['moved_meV'] / hi['moved_meV']))
                if res['low_end_costs_more'] else
                ('the high end costs AT LEAST as much as the low end, so the high-ell bandpowers '
                 'do carry this limit and the tail\'s residual is not ruled out')))
        out['rows'][str(lcut)] = res

    with io.open(os.path.join(_HERE, 'tail_control.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))
    print('')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
