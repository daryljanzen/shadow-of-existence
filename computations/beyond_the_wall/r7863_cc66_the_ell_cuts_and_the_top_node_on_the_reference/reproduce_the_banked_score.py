"""r7863+cc66: WHY DOES r7853's SCORE NOT REPRODUCE AT ITS OWN RECORDED BEST FIT?

`cut_rescore.py`'s patch verification REFUSED the cut legs: with the mask keeping everything -- a
pure pass-through to the original `SC.chi2_of` -- the worst total moved 6.185e-03 from the banked
value.  The wrapper cannot be the cause, so the arm of record is not reproducing at the parameters
it recorded, and that has to be located before a single cut number is taken seriously.

** WHAT THIS SEPARATES. **  The total is four terms.  `chi2_bao` is the only one that goes through
`bao_min`, whose memo is keyed on ROUNDED parameters -- `round(h0, 4)`, `round(om, 5)` -- so a fresh
process can compute it where the banked run was served a NEIGHBOURING point's cached value.  If that
is the cause the departure is confined to the `rd_min` arm, because `rd_camb` never calls `bao_min`.
A departure on BOTH arms is something else: CAMB non-determinism, or the JSON's own precision.

Run: python3 -I reproduce_the_banked_score.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(HERE)
R7853 = os.path.join(_BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference')
assert os.path.isdir(R7853), R7853
sys.path.insert(0, R7853)
import profile_likeforlike as PL                                             # noqa: E402

TERMS = ('chi2_cmb', 'chi2_lens', 'chi2_tau', 'chi2_bao', 'rd_used', 'amplitude')


def main():
    rows = []
    print('  %-8s %5s %12s %12s %12s %12s %12s %12s'
          % ('mode', 'sum', 'd(total)', 'd(cmb)', 'd(lens)', 'd(tau)', 'd(bao)', 'd(rd)'))
    for mode in PL.MODES:
        for s in PL.SUMS:
            p = os.path.join(R7853, 'out5', '%s_%.3f.json' % (mode, s))
            if not os.path.exists(p):
                continue
            b = json.load(open(p))
            start = (b['H0'], b['Om'], b['ombh2'], b['ns'], b['tau'])
            tot, det = PL.score(s, *start, mode)
            d = {k: float(det[k]) - float(b[k]) for k in TERMS}
            d['total'] = tot - b['total']
            rows.append(dict(mode=mode, sum=s, **d))
            print('  %-8s %5.2f %12.3e %12.3e %12.3e %12.3e %12.3e %12.3e'
                  % (mode, s, d['total'], d['chi2_cmb'], d['chi2_lens'], d['chi2_tau'],
                     d['chi2_bao'], d['rd_used']), flush=True)
    worst = {}
    for k in ('total',) + TERMS:
        for m in PL.MODES:
            v = [abs(r[k]) for r in rows if r['mode'] == m]
            worst['%s|%s' % (k, m)] = max(v) if v else None
    out = dict(rows=rows, worst_abs_by_term_and_mode=worst)
    json.dump(out, open(os.path.join(HERE, 'reproduce_the_banked_score.json'), 'w'), indent=1)
    print('\n  worst |departure| by term, per arm:')
    for k in ('total',) + TERMS:
        print('    %-12s rd_camb %12.3e   rd_min %12.3e'
              % (k, worst['%s|rd_camb' % k] or 0.0, worst['%s|rd_min' % k] or 0.0))
    return 0


if __name__ == '__main__':
    sys.exit(main())
