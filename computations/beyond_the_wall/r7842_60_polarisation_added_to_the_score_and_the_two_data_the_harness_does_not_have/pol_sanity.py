#!/usr/bin/env python3
"""** ARM Ⓐ①: THE INSTRUMENT'S POLARISATION OUTPUTS EXIST AND ARE WHAT THEIR OWN DOCSTRING SAYS. **

Registered: with `POLSAVE` on, both arms produce `C_TE` and `C_EE` on the same multipole axis as
`C_TT`; EE is positive everywhere it is scored, TE CHANGES SIGN, and EE's first acoustic maximum
falls between `l = 120` and `l = 160` where TT's falls between `l = 190` and `l = 250`.
*Reachable negative: a positive-definite TE, or an EE peak on top of TT's, either of which would
mean the E-mode kernel is not doing what its own docstring says.*

** WHY THE PEAK IS FOUND ON `D_l` AND NOT ON THE BANKED ARRAY WITHOUT THOUGHT. **  The instrument
banks `D_l = C_l * l(l+1)`, and the first EE maximum is a feature of `D_l`: hunting a maximum of
`C_l` instead finds the monotone fall of the plateau and reports `l = 100`, the bottom of the banked
range, which is not a peak at all.  The arm names acoustic maxima, so the quantity the acoustic
maxima live in is the one searched.

** AND THE PEAK IS REQUIRED TO BE INTERIOR. **  A maximum at either end of `l = 100`-`1996` is the
range running out, not a peak; it is reported as `None` rather than as the endpoint, so the arm
cannot be passed by an artefact of where the bank stops.

Writes `pol_sanity.json`.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
#: ⛔ ** THE BANK NO LONGER LIVES IN `/tmp`, AT `r7857`'s ORDER ③. **  *Three banks on this
#:   line were lost to a `/tmp` default -- the `555`-bin mask, the Phi bandpowers and this
#:   grid -- so what the scorers read is COMMITTED beside the instrument and this default
#:   points at it, computed from this file's own location rather than from an absolute path
#:   that would differ between containers.  The environment variable still overrides it.
_BANK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     'bank', 'pol_grid')
assert os.path.isdir(_BANK), _BANK      # two dirnames: this file sits one below `beyond_the_wall`
POL = os.environ.get('POL_DIR', _BANK)
ARMS = {'lcdm': 'lcdm', 'cr': 'cr'}


def first_max(ls, D, lo, hi):
    """the first interior local maximum of D over [lo, hi], or None if there is none inside"""
    m = (ls >= lo) & (ls <= hi)
    x, y = ls[m], D[m]
    for i in range(1, len(y) - 1):
        if y[i] >= y[i - 1] and y[i] >= y[i + 1]:
            return float(x[i])
    return None


def main():
    out = {}
    for arm, pref in sorted(ARMS.items()):
        p = os.path.join(POL, f'{pref}_S000.npz')
        if not os.path.exists(p):
            out[arm] = dict(present=False)
            print(f'  {arm}: not banked yet', flush=True)
            continue
        z = np.load(p, allow_pickle=True)
        keys = list(z.keys())
        ls = np.asarray(z['ls'], float)
        tt = np.asarray(z['Dl'], float)
        ee = np.asarray(z['Dl_EE'], float)
        te = np.asarray(z['Dl_TE'], float)
        scored = (ls >= 100) & (ls <= 1996)
        r = dict(
            present=True, keys=keys, multipoles=int(ls.size),
            axis_shared=bool(tt.shape == ee.shape == te.shape == ls.shape),
            l_range=[float(ls.min()), float(ls.max())],
            ee_min_on_scored=float(np.min(ee[scored])),
            ee_positive=bool(np.all(ee[scored] > 0)),
            te_min=float(np.min(te[scored])), te_max=float(np.max(te[scored])),
            te_changes_sign=bool(np.min(te[scored]) < 0 < np.max(te[scored])),
            te_sign_changes=int(np.sum(np.diff(np.sign(te[scored])) != 0)),
            ee_first_max=first_max(ls, ee, 100, 1996),
            tt_first_max=first_max(ls, tt, 100, 1996))
        r['ee_peak_in_band'] = bool(r['ee_first_max'] is not None
                                    and 120.0 <= r['ee_first_max'] <= 160.0)
        r['tt_peak_in_band'] = bool(r['tt_first_max'] is not None
                                    and 190.0 <= r['tt_first_max'] <= 250.0)
        r['ee_peak_below_tt'] = bool(r['ee_first_max'] is not None
                                     and r['tt_first_max'] is not None
                                     and r['ee_first_max'] < r['tt_first_max'])
        out[arm] = r
        print(f'  {arm}: {r["multipoles"]} multipoles, axis shared {r["axis_shared"]}', flush=True)
        print(f'     EE positive on the scored range: {r["ee_positive"]} '
              f'(minimum {r["ee_min_on_scored"]:.4g})', flush=True)
        print(f'     TE changes sign: {r["te_changes_sign"]} '
              f'({r["te_sign_changes"]} crossings, range {r["te_min"]:.4g} to '
              f'{r["te_max"]:.4g})', flush=True)
        print(f'     first maximum: EE at l = {r["ee_first_max"]}, TT at l = '
              f'{r["tt_first_max"]}  -- EE in 120-160: {r["ee_peak_in_band"]}, '
              f'TT in 190-250: {r["tt_peak_in_band"]}', flush=True)
    out['arms_present'] = sorted(a for a, v in out.items() if isinstance(v, dict)
                                 and v.get('present'))
    out['both_arms'] = bool(len(out['arms_present']) == 2)
    with open(os.path.join(HERE, 'pol_sanity.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f'  wrote pol_sanity.json  (arms present: {", ".join(out["arms_present"]) or "none"})',
          flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
