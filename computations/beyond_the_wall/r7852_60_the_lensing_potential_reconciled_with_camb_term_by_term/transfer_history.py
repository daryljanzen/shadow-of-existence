#!/usr/bin/env python3
"""** THE TRANSFER IS THE FAULT; WHEN DOES IT GO WRONG? **

`source_terms.py` located `99.8` per cent of the source difference -- and so about `98` per cent of
everything -- in the TRANSFER the instrument hands over at the carry start, not in the growth after
it.  Two readings pin that down further, and both come out of ONE solve with seven output times:

  ⓵ ** The instrument's super-horizon limit is already known to be RIGHT. **  `Phi(k -> 0)` at the
     handover is `-0.901020` against the analytic radiation-to-matter `-9/10`, so the initial
     conditions and the super-horizon evolution are correct to one part in a thousand.  ⇒ The error
     is in the `k` DEPENDENCE -- how much the instrument suppresses a mode that entered the horizon
     before equality -- and this file measures that suppression against CAMB at every output time.

  ⓶ ** Has it FROZEN by the handover? **  In matter domination `Phi` is constant, so if the
     instrument's `Phi(k, eta)` is still moving at `eta = 4000` the handover's lateness is itself a
     term, and if it is frozen the error is set in the radiation era and merely carried.  *That is
     the difference between a defect `r7850`'s ruling can reach and one it cannot.*

⚠ ONE solve, seven output times, so the suppression's history costs what one reading of it costs.

Run: python3 transfer_history.py        (writes transfer_history.json)
"""
import io
import json
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import terms as TT                                                           # noqa: E402

np = TT.np
A = TT.A
PP = TT.PP
NS, KMIN, KMAX, NKP = TT.NS, TT.KMIN, TT.KMAX, TT.NKP

ETAS = [float(v) for v in os.environ.get('ETAS', '500,914,1400,1893,2500,3200,4000').split(',')]
SUPERH = -0.9           # the analytic radiation-to-matter super-horizon value, not a fit


def main():
    t_all = time.time()
    kk = np.logspace(np.log10(KMIN), np.log10(KMAX), NKP)
    cache = os.path.join(_HERE, 'transfer_history_nkp%d.npz' % NKP)
    if os.path.exists(cache):
        z_ = np.load(cache)
        PhiT, etas = z_['PhiT'], [float(v) for v in z_['etas']]
        print('\n  read from cache: %d output time(s) on %d modes' % (len(etas), len(kk)),
              flush=True)
        t_solve = None
    else:
        print('\n  ONE solve, %d modes, %d output times to eta = %.0f' % (len(kk), len(ETAS),
                                                                         ETAS[-1]), flush=True)
        t0 = time.time()
        sol, nk, NV = A.evolve(kk, t_eval=np.array(ETAS, float), e_end=float(ETAS[-1]))
        assert sol.status == 0, 'the instrument solve did not finish: %s' % sol.message
        Y = sol.y.T.reshape(len(ETAS), nk, NV)
        PhiT = Y[:, :, 6]
        etas = list(ETAS)
        t_solve = round(time.time() - t0, 2)
        np.savez_compressed(cache, PhiT=PhiT, etas=np.array(etas), kk=kk)
        print('    %.1f s, cached' % t_solve, flush=True)

    r, cfg = TT.camb_results()
    Pw = TT.camb_weyl_power(r)

    kq = [1e-3, 5e-3, 1e-2, 2e-2, 5e-2, 1e-1, 3e-1, 1.0]
    idx = [int(np.argmin(np.abs(kk - q))) for q in kq]
    ipiv = int(np.argmin(np.abs(kk - 0.05)))

    print('\n  ⓶ HAS THE TRANSFER FROZEN?  Phi(k, eta) / Phi(k, eta = %.0f), on the instrument alone'
          % etas[-1])
    print('      k [/Mpc]  ' + '  '.join('%9.0f' % e for e in etas))
    frozen = {}
    for q, j in zip(kq, idx):
        row = [float(PhiT[i, j] / PhiT[-1, j]) for i in range(len(etas))]
        frozen['k%.4g' % kk[j]] = row
        print('      %8.5f  ' % kk[j] + '  '.join('%9.5f' % v for v in row))
    late = max(abs(frozen['k%.4g' % kk[j]][-2] - 1.0) for j in idx)
    print('    ⇒ the largest move over the LAST interval (eta %.0f -> %.0f) is %.3e'
          % (etas[-2], etas[-1], late), flush=True)

    print('\n  ⓵ THE SUPPRESSION AGAINST CAMB, at each output time, each normalised at k = %.4f'
          % kk[ipiv])
    print('      eta      z        ' + '  '.join('%9.4g' % q for q in kq))
    hist = {}
    for i, e in enumerate(etas):
        a = float(A.a_of_eta(e))
        z = 1.0 / a - 1.0
        d_i = (kk ** (NS - 1)) * PhiT[i] ** 2
        d_c = np.array([kk[j] ** 3 * Pw(z, kk[j]) / (2 * np.pi ** 2) for j in range(len(kk))])
        sh = (d_i / d_i[ipiv]) / (d_c / d_c[ipiv]) - 1.0
        hist['eta%.0f' % e] = dict(z=z, a=a,
                                   shape=[float(sh[j]) for j in idx],
                                   worst=float(sh[int(np.argmax(np.abs(sh)))]),
                                   worst_k=float(kk[int(np.argmax(np.abs(sh)))]))
        print('      %6.0f  %7.3f  ' % (e, z) + '  '.join('%+9.4f' % sh[j] for j in idx),
              flush=True)

    print('\n  ⓵ᵇ AND THE INSTRUMENT\'S OWN SUPPRESSION, absolute, against its super-horizon value')
    print('      eta      ' + '  '.join('%9.4g' % q for q in kq))
    absr = {}
    for i, e in enumerate(etas):
        row = [float(PhiT[i, j] / SUPERH) for j in idx]
        absr['eta%.0f' % e] = row
        print('      %6.0f   ' % e + '  '.join('%9.5f' % v for v in row))
    print('    ⌗ at k -> 0 the instrument reads Phi = %+.6f against the analytic %.1f -- so what '
          'moves below is the SUPPRESSION and not the normalisation'
          % (float(PhiT[-1, 0]), SUPERH), flush=True)

    out = dict(config=cfg, etas=etas, nkp=NKP, kmin=KMIN, kmax=KMAX, ns=NS,
               k_probed=[float(kk[j]) for j in idx], pivot_k=float(kk[ipiv]),
               superhorizon_analytic=SUPERH,
               phi_at_k_min=float(PhiT[-1, 0]),
               phi_over_superhorizon=absr,
               frozen_ratio_to_last=frozen,
               largest_move_over_last_interval=float(late),
               shape_against_camb=hist,
               solve_seconds=t_solve, nk_modes=int(len(kk)),
               switches={k: os.environ[k] for k in ('NK', 'NOPROJ', 'LN', 'HIER', 'ARM')
                         if k in os.environ},
               total_seconds=round(time.time() - t_all, 2))
    with io.open(os.path.join(_HERE, 'transfer_history.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote transfer_history.json  (%.1f s)\n' % out['total_seconds'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
