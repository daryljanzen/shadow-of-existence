#!/usr/bin/env python3
"""** Ⓐ①/Ⓑ②: WHICH OF THE THREE QUANTITIES BREAKS THE CANCELLATION. **

`r7852` measured the potential falling by `5.3` to `53.9` per cent between two handovers where it
should hold flat.  `PREDICTION.md` declares that the equation's FORM is not the cause and registers
no answer.  The cancellation it rests on is

    k^2 Phi / (3 Hc)  ==  -(Hc / 2) sum_i Om_i d_i          (sub-horizon, quasi-static)

between three quantities: the RATE `Hc` the perturbation equations use, the FRACTIONS `Om_i` their
source is normalised against, and the CONTRASTS `d_i`.  ** One solve prices all three. **

  Ⓑ②  the rate against the source: `Hc^2` against `H0^2 a^2 sum_i Om_i`, which is the Friedmann
       relation the source's form assumes.  ⚠ The registered expectation is that this is BROKEN.

  Ⓐ①ᵃ the quasi-static balance itself: how far the solved `Phi` sits from `-(3/2) Hc^2 sum/k^2`.
       Sub-horizon the homogeneous decay rate is `k^2/(3 Hc)` per unit conformal time, which is fast
       against the expansion, so a sub-horizon mode should TRACK that relation tightly and a drift
       of fifty per cent cannot come from the potential's own equation.

  Ⓐ①ᵇ the growth exponent `dln d / dln a`, which is `1` in matter domination.  ** If the contrasts
       are not growing linearly, `Hc^2 d / k^2` is not constant and the potential is RIGHT to move. **

  Ⓐ①ᶜ and the three factors of `Hc^2 d / k^2` separately, so that whichever moves is named rather
       than inferred from the product.

⚠ Each reading is reported for every probed mode; nothing is averaged over `k`, because `r7852`'s
whole finding was that the error is `k`-dependent.

Run: python3 locate.py          (writes locate.json; ONE solve, cached)
"""
import io
import json
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
sys.path.insert(0, _BTW)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

import ACOUSTIC_two_arm as A                                                 # noqa: E402

ETAS = [float(v) for v in os.environ.get(
    'ETAS', '500,700,914,1200,1400,1893,2500,3200,4000').split(',')]
KK = np.array([float(v) for v in os.environ.get(
    'KPROBE', '2e-4,1e-3,5e-3,1e-2,2e-2,5e-2,1e-1,3e-1,1.0').split(',')])
NS = float(os.environ.get('NS', '0.965'))


def main():
    t_all = time.time()
    tag = '-'.join('%g' % e for e in ETAS) + '_k' + '-'.join('%g' % k for k in KK)
    cache = os.path.join(_HERE, 'locate_state.npz')
    if os.path.exists(cache):
        z = np.load(cache)
        if z['tag'].item() == tag:
            Y, etas = z['Y'], [float(v) for v in z['etas']]
            print('\n  state read from its cache (%d time(s), %d mode(s))' % (len(etas), len(KK)),
                  flush=True)
            t_solve = None
        else:
            raise SystemExit('the cache is for a different configuration: %s' % z['tag'].item())
    else:
        print('\n  ONE solve: %d mode(s), %d output time(s) to eta = %.0f'
              % (len(KK), len(ETAS), ETAS[-1]), flush=True)
        t0 = time.time()
        sol, nk, NV = A.evolve(KK, t_eval=np.array(ETAS, float), e_end=float(ETAS[-1]))
        assert sol.status == 0, 'the solve did not finish: %s' % sol.message
        Y = sol.y.T.reshape(len(ETAS), nk, NV)
        etas = list(ETAS)
        t_solve = round(time.time() - t0, 2)
        np.savez_compressed(cache, Y=Y, etas=np.array(etas), kk=KK, tag=np.array(tag))
        print('    %.1f s, cached' % t_solve, flush=True)

    NV = Y.shape[2]
    I_DB = NV - 1
    dc, dg, dn, Ph, db = (Y[:, :, 0], Y[:, :, 2], Y[:, :, 4], Y[:, :, 6], Y[:, :, I_DB])

    a = np.array([float(A.a_of_eta(e)) for e in etas])
    Hc = np.array([float(A.Hl_of(e) if A.LEAFPERT else A.Hc_of(e)) for e in etas])
    Og = np.array([float(A.Og_of(e)) for e in etas])
    On = np.array([float(A.On_of(e)) for e in etas])
    Oc = np.array([float(A.Oc_of(e)) for e in etas])
    Ob = np.array([float(A.Ob_of(e)) for e in etas])
    Gf = np.array([float(A.Gf_of(e)) for e in etas])

    # ── Ⓑ② the rate against the source's own normalisation
    H0c = float(A.H0) / float(A.C)
    rt = float(A.OR) / a ** 4 + float(A.OM) / a ** 3 + float(A.OL)
    fried = np.abs(Hc ** 2 / (H0c ** 2 * a ** 2 * rt) - 1.0)
    print('\n  Ⓑ② THE RATE AGAINST THE SOURCE  (LEAFPERT = %s, GSRC factor %.6f..%.6f)'
          % (A.LEAFPERT, Gf.min(), Gf.max()))
    print('      eta        a            |Hc^2/(H0^2 a^2 sum Om) - 1|      sum Om_i')
    sumom = Og + On + Oc + Ob
    for i, e in enumerate(etas):
        print('      %6.0f  %.6e   %.6e                 %.8f' % (e, a[i], fried[i], sumom[i]))
    print('    ⇒ worst %.3e over the interval.  ** %s **'
          % (fried.max(),
             'the rate IS consistent with its source, so Ⓑ② FAILS AS REGISTERED'
             if fried.max() < 1e-06 else
             'the rate is NOT consistent, as registered'), flush=True)

    # ── the quasi-static balance, per mode
    src = Gf[:, None] * (Og[:, None] * dg + On[:, None] * dn
                         + Oc[:, None] * dc + Ob[:, None] * db)
    phi_qs = -1.5 * (Hc[:, None] ** 2) * src / (KK[None, :] ** 2)
    print('\n  Ⓐ①ᵃ THE QUASI-STATIC BALANCE -- solved Phi over the Poisson value, per mode')
    print('      eta    ' + '  '.join('%9.3g' % k for k in KK))
    for i, e in enumerate(etas):
        print('      %6.0f ' % e + '  '.join('%9.4f' % v for v in (Ph[i] / phi_qs[i])))
    print('    ⌗ sub-horizon this should be 1: the homogeneous decay rate k^2/(3 Hc) is fast '
          'against the expansion, so the mode tracks the relation.')
    print('      horizon test, k/Hc at the last time: ' + '  '.join('%7.2f' % (k / Hc[-1])
                                                                    for k in KK), flush=True)

    # ── the growth exponent, per mode
    lna = np.log(a)
    print('\n  Ⓐ①ᵇ THE GROWTH EXPONENT dln(d_cb)/dln(a), which is 1 in matter domination')
    wc = float(A.OCDM) / (float(A.OCDM) + float(A.OB))
    wb = 1.0 - wc
    dcb = wc * dc + wb * db
    print('      eta interval      ' + '  '.join('%9.3g' % k for k in KK))
    grow = {}
    for i in range(len(etas) - 1):
        ex = (np.log(np.abs(dcb[i + 1])) - np.log(np.abs(dcb[i]))) / (lna[i + 1] - lna[i])
        grow['%g-%g' % (etas[i], etas[i + 1])] = [float(v) for v in ex]
        print('      %6.0f -> %6.0f  ' % (etas[i], etas[i + 1])
              + '  '.join('%9.4f' % v for v in ex))
    print('    ⌗ a contrast that is not growing linearly makes Hc^2 d / k^2 move, and then the '
          'potential is RIGHT to move with it.', flush=True)

    # ── the three factors of the product, separately
    print('\n  Ⓐ①ᶜ THE PRODUCT\'S FACTORS, each over its value at the last time')
    print('      quantity        ' + '  '.join('%9.3g' % k for k in KK))
    print('      Hc^2            ' + '  '.join('%9.4f' % (Hc[0] ** 2 / Hc[-1] ** 2) for _ in KK))
    print('      d_cb            ' + '  '.join('%9.4f' % v for v in (dcb[0] / dcb[-1])))
    print('      Hc^2 d_cb       ' + '  '.join('%9.4f' % v for v in
                                               (Hc[0] ** 2 * dcb[0]) / (Hc[-1] ** 2 * dcb[-1])))
    print('      Phi             ' + '  '.join('%9.4f' % v for v in (Ph[0] / Ph[-1])))
    print('      sum Om_i d_i    ' + '  '.join('%9.4f' % v for v in (src[0] / src[-1])))
    print('      Hc^2 sum        ' + '  '.join('%9.4f' % v for v in
                                               (Hc[0] ** 2 * src[0]) / (Hc[-1] ** 2 * src[-1])))
    print('    ⌗ the row that is NOT 1 is the one that moves; Phi follows Hc^2 sum, so if that '
          'row moves the potential is tracking it correctly.', flush=True)

    out = dict(etas=etas, k=[float(v) for v in KK], a=[float(v) for v in a],
               Hc=[float(v) for v in Hc], leafpert=bool(A.LEAFPERT),
               Gf=[float(v) for v in Gf],
               omegas=dict(Og=[float(v) for v in Og], On=[float(v) for v in On],
                           Oc=[float(v) for v in Oc], Ob=[float(v) for v in Ob],
                           sum=[float(v) for v in sumom]),
               friedmann_residual=[float(v) for v in fried],
               friedmann_worst=float(fried.max()),
               rate_is_consistent=bool(fried.max() < 1e-06),
               phi_over_quasistatic=[[float(v) for v in row] for row in (Ph / phi_qs)],
               k_over_Hc_at_last=[float(k / Hc[-1]) for k in KK],
               growth_exponent=grow,
               factors=dict(
                   Hc2_first_over_last=float(Hc[0] ** 2 / Hc[-1] ** 2),
                   dcb=[float(v) for v in (dcb[0] / dcb[-1])],
                   Hc2_dcb=[float(v) for v in (Hc[0] ** 2 * dcb[0]) / (Hc[-1] ** 2 * dcb[-1])],
                   Phi=[float(v) for v in (Ph[0] / Ph[-1])],
                   src=[float(v) for v in (src[0] / src[-1])],
                   Hc2_src=[float(v) for v in (Hc[0] ** 2 * src[0]) / (Hc[-1] ** 2 * src[-1])]),
               switches={k: os.environ[k] for k in ('NK', 'NOPROJ', 'ARM', 'HIER', 'LN')
                         if k in os.environ},
               solve_seconds=t_solve, total_seconds=round(time.time() - t_all, 2))
    with io.open(os.path.join(_HERE, 'locate.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote locate.json  (%.1f s)\n' % out['total_seconds'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
