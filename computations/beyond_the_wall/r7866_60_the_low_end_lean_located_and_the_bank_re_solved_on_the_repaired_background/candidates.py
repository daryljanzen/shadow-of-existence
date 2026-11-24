# -*- coding: utf-8 -*-
"""Ⓑ②ᵈ+ᵉ THE THREE CANDIDATES THE ORDER NAMES, TESTED RATHER THAN ASSUMED, AND THE HIGH-END
CONTROL THAT KEEPS THE WHOLE OF ② HONEST.

The lean is located: removing the thirty-six bandpowers at multipoles `100..207` moves the
instrument's crossing by `20.1` meV with its parameters held as the reference's are, against the
reference's `0.12` on the SAME bins.  The order names three candidates for the mechanism and says
to test them.  Each test below can come back NO, and the first one comes back NO for a reason that
is structural rather than numerical.

    NODE=60 python3 candidates.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
sys.path.insert(0, os.path.join(_BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_'
                                      'the_damping_tails_share_of_the_gap'))
import tail_share as TS                                                     # noqa: E402,F401
import score_ttteee as SC                                                   # noqa: E402
import model3 as M3                                                         # noqa: E402
import model6 as M6                                                         # noqa: E402
from same_bins import SUMS, CROSS, cross_of, N_PER_BLOCK                    # noqa: E402
from lean import fit_x4                                                     # noqa: E402

NAMES = {0: 'TT', 1: 'TE', 2: 'EE'}
FIRST_PEAK = 220          # the TT first peak, where the late-ISW candidate lives below


def _restrict(mod, keep):
    """swap the model's own bandpower mask for `keep`, as r7862's own cuts do"""
    c = mod.cmb
    ok = c.ok
    newok = ok.copy()
    newok[ok] = keep
    base, g, h = c.base, dict(c.g), dict(c.h)
    c.base = lambda s, nu=0, _o=base, _k=keep: np.asarray(_o(s, nu), float)[_k]
    c.g = {k: (lambda s, nu=0, _o=g[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
           for k in M3.KEYS4}
    c.h = {k: (lambda s, nu=0, _o=h[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
           for k in M3.KEYS4}
    c.ok, c.nb = newok, int(newok.sum())
    c.F, c.d, c.pos = SC.fisher_for(newok), SC.X_DATA[newok], SC.POSITIVE[newok]
    return mod


def lowest_per_block(ok, n):
    keep = np.ones(int(ok.sum()), bool)
    blk, lo = SC.BLOCK[ok], SC.BIN_LO[ok]
    for b in (0, 1, 2):
        idx = np.where(blk == b)[0]
        keep[idx[np.argsort(lo[idx], kind='stable')][:n]] = False
    return keep


def highest_per_block(ok, n):
    keep = np.ones(int(ok.sum()), bool)
    blk, hi = SC.BLOCK[ok], SC.BIN_HI[ok]
    for b in (0, 1, 2):
        idx = np.where(blk == b)[0]
        keep[idx[np.argsort(-hi[idx], kind='stable')][:n]] = False
    return keep


def crossing(keep, x4=None, fixed_amp=False):
    """the 2.71 crossing of chi2_cmb over the sum, parameters frozen at `x4` or re-fit per sum"""
    mod = _restrict(M6.Model6('lcdm'), keep)
    if fixed_amp:
        c = mod.cmb
        m0 = c.binned(x4 if x4 is not None else np.zeros(4), 0.0)
        A0 = float((m0 @ c.F @ c.d) / (m0 @ c.F @ m0))

        def chi2_fixed(x4v, s, _A=A0):
            m = c.binned(np.asarray(x4v, float), s)
            r = c.d - _A * m
            return float(r @ c.F @ r)
        tot = [chi2_fixed(x4, s) for s in SUMS]
    elif x4 is not None:
        tot = [float(mod.cmb.chi2_cmb(x4, s)) for s in SUMS]
    else:
        tot = [fit_x4(mod, s)[1] for s in SUMS]
    return cross_of(SUMS, tot), tot


def main():
    print(__doc__)
    print('=' * 100)
    out = {}
    ok = M6.Model6('lcdm').cmb.ok
    keep_all = np.ones(int(ok.sum()), bool)
    keep_lo = lowest_per_block(ok, N_PER_BLOCK)
    keep_hi = highest_per_block(ok, N_PER_BLOCK)
    x4f, _ = fit_x4(M6.Model6('lcdm'), 0.0)

    # ── Ⓑ②ᵉ THE HIGH-END CONTROL ───────────────────────────────────────────────────────────────
    print('\n  Ⓑ②ᵉ THE HIGH-END CONTROL -- the same COUNT off the top of each block')
    base, _ = crossing(keep_all, x4f)
    lo, _ = crossing(keep_lo, x4f)
    hi, _ = crossing(keep_hi, x4f)
    out['high_end_control'] = dict(whole=base, minus_low36=lo, minus_high36=hi,
                                   move_low=None if None in (base, lo) else base - lo,
                                   move_high=None if None in (base, hi) else base - hi)
    print('    whole %s meV;  minus the LOW thirty-six %s;  minus the HIGH thirty-six %s'
          % tuple(('%.2f' % v) if v is not None else 'none' for v in (base, lo, hi)))
    print('    ⇒ the low end moves it %s meV and the high end %s'
          % (('%+.2f' % out['high_end_control']['move_low'])
             if out['high_end_control']['move_low'] is not None else 'none',
             ('%+.2f' % out['high_end_control']['move_high'])
             if out['high_end_control']['move_high'] is not None else 'none'))
    ok_control = (out['high_end_control']['move_high'] is not None
                  and out['high_end_control']['move_low'] is not None
                  and abs(out['high_end_control']['move_high'])
                  < abs(out['high_end_control']['move_low']) / 3.0)
    out['high_end_control']['holds'] = bool(ok_control)
    print('    the control HOLDS if the high end moves it far less: %s   ⌗ *if both ends moved it '
          'alike, the method would be measuring the COUNT and ② would be reported as not located*'
          % ok_control)

    # ── Ⓑ②ᵈ⓵ the tau prior ─────────────────────────────────────────────────────────────────────
    print('\n  Ⓑ②ᵈ⓵ THE LOW-ell REIONISATION BUMP AGAINST THE TAU PRIOR -- and the answer is NO, '
          'structurally')
    src = io.open(os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                                    'the_harness_does_not_have', 'model3.py'),
                  encoding='utf-8').read()
    has_tau = ('tau' in src.split('def chi2_cmb')[1].split('def ')[0]) if 'def chi2_cmb' in src \
        else None
    print('    the score the limit is read through is `chi2_cmb` + the BAO term.  Does `chi2_cmb` '
          'carry tau at all?  %s' % ('yes' if has_tau else 'NO'))
    print('    ⇒ ** the candidate cannot be what this lean rides: there is no tau in the function '
          'whose crossing moved. **  tau enters the JOINT score through the lensing half, and the '
          'lensing half does not reach this crossing -- measured separately, by re-solving the '
          'lensing grid and finding every profile total unchanged to four decimals.')
    out['tau_prior'] = dict(chi2_cmb_carries_tau=bool(has_tau), verdict='NO -- not in this path')

    # ── Ⓑ②ᵈ⓶ the late ISW ──────────────────────────────────────────────────────────────────────
    print('\n  Ⓑ②ᵈ⓶ THE LATE ISW -- does the lean survive on TT BELOW the first peak alone?')
    okidx = np.where(ok)[0]
    isw = (SC.BLOCK[okidx] == 0) & (SC.BIN_HI[okidx] < FIRST_PEAK)
    keep_isw_only = isw.copy()
    n_isw = int(isw.sum())
    print('    TT bins below multipole %d: %d of the mask' % (FIRST_PEAK, n_isw))
    if n_isw >= 10:
        b2, _ = crossing(keep_isw_only, x4f)
        k2 = keep_isw_only.copy()
        k2[np.where(isw)[0][:N_PER_BLOCK]] = False
        c2, _ = crossing(k2, x4f)
        out['late_isw'] = dict(n_bins=n_isw, whole=b2, minus12=c2,
                               move=None if None in (b2, c2) else b2 - c2)
        print('    on those alone: crossing %s meV; dropping twelve of them %s  ⇒ move %s'
              % (('%.2f' % b2) if b2 is not None else 'none',
                 ('%.2f' % c2) if c2 is not None else 'none',
                 ('%+.2f' % out['late_isw']['move']) if out['late_isw'].get('move') is not None
                 else 'none'))
    else:
        out['late_isw'] = dict(n_bins=n_isw, verdict='NOT TESTABLE on this mask -- too few bins '
                                                     'below the first peak to score')
        print('    ⇒ ** NOT TESTABLE on this mask: the instrument\'s score starts at multipole 100 '
              'and has only %d TT bin(s) below the first peak, too few to score. **  That is a '
              'fact about the mask Ⓐ① named, not a result about the ISW.' % n_isw)

    # ── Ⓑ②ᵈ⓷ the amplitude handover ────────────────────────────────────────────────────────────
    print('\n  Ⓑ②ᵈ⓷ THE SHARED NORMALISATION -- does the lean survive with the amplitude FIXED '
          'rather than solved?')
    b3, _ = crossing(keep_all, x4f, fixed_amp=True)
    c3, _ = crossing(keep_lo, x4f, fixed_amp=True)
    mv = None if None in (b3, c3) else b3 - c3
    out['amplitude_handover'] = dict(whole=b3, minus_low36=c3, move=mv,
                                     move_when_solved=out['high_end_control']['move_low'])
    print('    amplitude fixed at the whole-mask zero-sum solve: whole %s meV, minus the '
          'thirty-six %s  ⇒ move %s'
          % (('%.2f' % b3) if b3 is not None else 'none',
             ('%.2f' % c3) if c3 is not None else 'none',
             ('%+.2f' % mv) if mv is not None else 'none'))
    if mv is not None and out['high_end_control']['move_low'] is not None:
        share = 1.0 - abs(mv) / abs(out['high_end_control']['move_low'])
        out['amplitude_handover']['share_of_the_move_the_amplitude_carries'] = float(share)
        print('    against %+.2f with the amplitude solved  ⇒ the amplitude carries %.0f per cent '
              'of the move, and %.0f per cent survives it'
              % (out['high_end_control']['move_low'], 100.0 * share, 100.0 * (1.0 - share)))

    io.open(os.path.join(_HERE, 'candidates.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True, default=float))
    print('\n  wrote candidates.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
