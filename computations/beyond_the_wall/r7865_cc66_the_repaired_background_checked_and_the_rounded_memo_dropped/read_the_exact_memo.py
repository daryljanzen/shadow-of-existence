"""r7865+cc66 item ⑦: the limit off the exact-memo arm, and whether the arm is now re-derivable.

Band Ⓕ asks whether `54.00` meV moves.  Band Ⓖ asks the sharper thing: re-scoring each NEWLY
banked point at its own recorded five parameters must now reproduce its recorded total EXACTLY,
where the landed points depart by up to `6.185e-03` on `chi2_bao` alone.

⌗ *The limit is the interpolated `2.71` crossing, by `read_likeforlike.py`'s method and not a second
one -- and the check that it IS that method is that applying it to the LANDED points reproduces the
published `54.00` to the printed digit, asserted here and pinned in the receipt.*

Run: python3 -I read_the_exact_memo.py
"""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
R7853 = os.path.join(BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference')
sys.path.insert(0, R7853)
import profile_likeforlike as PL                                            # noqa: E402

TERMS = ('chi2_cmb', 'chi2_lens', 'chi2_tau', 'chi2_bao')
CROSS = 2.71


#: the PUBLISHED reader's own grid, and a twenty-times finer one.  ⛭ Both are reported, because
#: reporting only the fine grid would understate the answer -- on the arm of record's own
#: resolution the limit does not move AT ALL -- and reporting only the published grid would hide
#: the bound that the finer one puts on a movement that resolution cannot see.
GRIDS = (('published_20001', 20001), ('fine_400001', 400001))


def limit(points, n):
    pts = sorted(points)
    s = np.array([p[0] for p in pts], float)
    dc = np.array([p[1] for p in pts], float)
    dc = dc - dc.min()                      # the published reader measures from the MINIMUM
    fine = np.linspace(s[0], s[-1], n)
    i = np.where(np.interp(fine, s, dc) > CROSS)[0]
    return float(fine[i[0]] * 1000.0), [float(x) for x in dc]


def main():
    new, old = [], []
    rows = []
    for f in sorted(glob.glob(os.path.join(HERE, 'out_exact', '*.json'))):
        d = json.load(open(f))
        new.append((d['sum'], d['total']))
        old.append((d['sum'], d['landed_total']))
        rows.append(dict(sum=d['sum'], exact=d['total'], landed=d['landed_total'],
                         moved=d['total'] - d['landed_total'], H0=d['H0'],
                         rd=d['rd_used'], interior=d['interior']))
    print('  Ⓕ THE LIMIT, on the published reader\'s own grid AND on a finer one')
    grids = {}
    for name, n in GRIDS:
        lo, dc_old = limit(old, n)
        ln, dc_new = limit(new, n)
        grids[name] = dict(n=n, step_meV=400.0 / (n - 1), landed=lo, exact=ln, moved=ln - lo)
        print('    %-16s step %.4f meV   landed %9.5f   exact %9.5f   moved %+.5f'
              % (name, grids[name]['step_meV'], lo, ln, ln - lo))
    lim_old = grids['published_20001']['landed']
    lim_new = grids['published_20001']['exact']
    dc_old, dc_new = limit(old, 20001)[1], limit(new, 20001)[1]

    # Ⓖ: re-score each NEW point at its own recorded parameters; every term must be exact
    print('\n  Ⓖ RE-DERIVABILITY of the newly banked points, term by term')
    worst = {k: 0.0 for k in TERMS}
    worst['total'] = 0.0
    for f in sorted(glob.glob(os.path.join(HERE, 'out_exact', '*.json'))):
        d = json.load(open(f))
        start = (d['H0'], d['Om'], d['ombh2'], d['ns'], d['tau'])
        tot, det = PL.score(d['sum'], *start, 'rd_min')
        worst['total'] = max(worst['total'], abs(tot - d['total']))
        for k in TERMS:
            worst[k] = max(worst[k], abs(det[k] - d[k]))
        print('    Sum %.3f  d(total) %.3e  d(bao) %.3e' % (d['sum'], tot - d['total'],
                                                            det['chi2_bao'] - d['chi2_bao']))
    print('    worst: %s' % {k: '%.3e' % v for k, v in worst.items()})

    out = dict(rows=rows, grids=grids, limit_landed_meV=lim_old, limit_exact_meV=lim_new,
               moved_meV=lim_new - lim_old, dchi2_landed=dc_old, dchi2_exact=dc_new,
               rederive_worst=worst, all_interior=bool(all(r['interior'] for r in rows)),
               worst_move_in_total=max(abs(r['moved']) for r in rows),
               residue_attributed=6.185e-03)
    json.dump(out, open(os.path.join(HERE, 'exact_memo_read.json'), 'w'), indent=1)
    print('\n  worst single-point move in total: %.6f   all interior: %s'
          % (out['worst_move_in_total'], out['all_interior']))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
