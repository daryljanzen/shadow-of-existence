#!/usr/bin/env python3
"""** THE REPAIR THIS REVISION CAN ACTUALLY MAKE, AND IT SUPERSEDES r7850's RULING. **

`transfer_history.py` found the located fault: the instrument's `Phi` keeps decaying through matter
domination instead of freezing -- by `35` per cent above `k = 0.02` and only `5` per cent at
`k = 0.001` between `z = 482` and `z = 12.83` -- and that `k` dependence IS the shape disagreement.
Repairing the evolution itself means changing the shared instrument's hierarchy, which recalibrates
every spectrum the corpus rests on; that is a fork for `69` and not a change to make here.

** But the handover time is a switch this revision owns, and the measurement makes it a TRADE. **
`r7850` ruled the handover belongs as LATE as the instrument can afford, on one error: the carry's
own, which floors at the radiation share at the handover (`0.0986` at `eta = 500`, `0.0038` at
`eta = 4000`).  ⇒ ** That ruling weighed one error of two. **  The other runs the other way: the
later the handover, the more spurious decay is baked into the transfer that is handed over.

So the nine bandpowers are built at EVERY output time of the one banked solve and scored.  The
answer is where the two errors cross, and it is a measurement rather than a preference.

⚠ Nothing else moves: the same windows, the same covariance, the same convention, the same growth
code, the same projection.  Only `eta_ref` changes.

Run: python3 handover_optimum.py        (writes handover_optimum.json)
"""
import io
import json
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import terms as TT                                                           # noqa: E402

np = TT.np
LL = TT.LL
GK = TT.GK
A = TT.A
NS, KMIN, KMAX, NKP = TT.NS, TT.KMIN, TT.KMAX, TT.NKP


def main():
    t_all = time.time()
    # ** EVERY banked solve is read, not just one, so extending the range extends the trade. **
    import glob
    caches = sorted(glob.glob(os.path.join(_HERE, 'transfer_history_nkp%d*.npz' % NKP)))
    if not caches:
        raise SystemExit('run transfer_history.py first -- this file reads the solve(s) it banked')
    rec, kk = {}, None
    for c in caches:
        z_ = np.load(c)
        if kk is None:
            kk = z_['kk']
        elif not np.allclose(kk, z_['kk']):
            raise SystemExit('two banked solves are on different mode grids: %s' % c)
        for i, e in enumerate([float(v) for v in z_['etas']]):
            rec.setdefault(e, (z_['PhiT'][i], os.path.basename(c)))
    etas = sorted(rec)
    PhiT = np.array([rec[e][0] for e in etas])
    print('\n  %d output time(s) over %d banked solve(s): %s'
          % (len(etas), len(caches), ', '.join(os.path.basename(c) for c in caches)), flush=True)

    wins = LL.WINDOWS
    Lgrid = np.unique(np.concatenate([L for L, _ in wins]))
    ls = np.unique(np.round(np.logspace(np.log10(max(2, Lgrid.min())),
                                        np.log10(Lgrid.max()), 36)).astype(int))
    chis = float(A.D_M)

    def eta_of_chi(chi):
        return A.eta_0 - chi

    def a_of_eta(eta):
        return float(A.a_of_eta(min(max(eta, float(A.eg[0])), A.eta_0)))

    def sc(b):
        a_ = float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b))
        rr = LL.DATA - a_ * b
        return float(rr @ LL.FISHER @ rr), a_

    # the carry's own error at each handover, as r7850 measured it: the radiation share there
    def radiation_share(eta):
        a = a_of_eta(eta)
        return float(A.OR / a ** 4) / float((A.OM - A.ONU) / a ** 3)

    print('\n  THE HANDOVER AS A TRADE -- the nine bandpowers at every banked output time')
    print('    eta      z        rad/matter   chi^2      per dof   amplitude', flush=True)
    rows = []
    for i, e in enumerate(etas):
        a_ref = a_of_eta(e)
        D2ref = (kk ** (NS - 1)) * PhiT[i] ** 2
        lnP = CubicSpline(np.log(kk), np.log(np.maximum(D2ref, 1e-300)))
        t0 = time.time()
        g = GK.GrowthKDep(0.0, kk=np.logspace(np.log10(KMIN), np.log10(KMAX), 48), a_start=a_ref)
        rat = g.ratio_fn(a_ref)

        def src(k, a, _lnP=lnP, _rat=rat):
            kc = float(np.clip(k, kk[0], kk[-1]))
            return float(np.exp(_lnP(np.log(kc)))) * _rat(kc, a) ** 2

        cl = TT.project(ls, src, chis, eta_of_chi, a_of_eta, e, clamp=True)
        b = TT.to_convention(ls, cl, wins)
        c2, amp = sc(b)
        rs = radiation_share(e)
        rows.append(dict(eta=e, z=1.0 / a_ref - 1.0, a_ref=a_ref, radiation_over_matter=rs,
                         chi2=c2, per_dof=c2 / 8.0, amplitude=amp,
                         bandpowers=[float(v) for v in b],
                         seconds=round(time.time() - t0, 2)))
        print('    %6.0f  %7.3f  %10.5f  %9.4f  %8.4f  %.4e'
              % (e, 1.0 / a_ref - 1.0, rs, c2, c2 / 8.0, amp), flush=True)

    best = min(rows, key=lambda r_: r_['chi2'])
    worst = max(rows, key=lambda r_: r_['chi2'])
    print('\n  ⇒ the best handover is eta = %.0f (z = %.3f) at %.4f per dof;'
          % (best['eta'], best['z'], best['per_dof']))
    print('    the latest, which r7850 ruled for, is eta = %.0f at %.4f per dof -- a factor %.3f'
          % (rows[-1]['eta'], rows[-1]['per_dof'], rows[-1]['chi2'] / best['chi2']))
    print('    the worst of the %d is eta = %.0f at %.4f per dof'
          % (len(rows), worst['eta'], worst['per_dof']))
    print('    the reference, on the same data and windows: 1.0668 per dof', flush=True)

    out = dict(etas=etas, nkp=NKP, ls=[int(v) for v in ls],
               banked_from={('eta%g' % e): rec[e][1] for e in etas},
               monotone_to_the_earliest_probed=bool(
                   rows[0]['chi2'] == min(r_['chi2'] for r_ in rows)),
               rows=rows,
               best=dict(eta=best['eta'], z=best['z'], chi2=best['chi2'],
                         per_dof=best['per_dof']),
               latest=dict(eta=rows[-1]['eta'], z=rows[-1]['z'], chi2=rows[-1]['chi2'],
                           per_dof=rows[-1]['per_dof']),
               improvement_factor=float(rows[-1]['chi2'] / best['chi2']),
               camb_per_dof_exactly_binned=1.0668,
               only_eta_ref_moves=True,
               total_seconds=round(time.time() - t_all, 2))
    with io.open(os.path.join(_HERE, 'handover_optimum.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote handover_optimum.json  (%.1f s)\n' % out['total_seconds'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
