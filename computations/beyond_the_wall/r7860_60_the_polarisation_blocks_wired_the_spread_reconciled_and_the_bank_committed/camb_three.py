# -*- coding: utf-8 -*-
"""r7860 (60) Ⓑ② -- ALL THREE BLOCKS AGAINST CAMB, WITH `FOURPI` ON, TE BY ITS CORRELATION.

⛭ `r7857` (69) ruling ① directs that TE be checked **by the cross-correlation coefficient**
`r_l = TE / sqrt(TT x EE)` against CAMB's own, because that is invariant to a shared constant and
does not blow up where TE crosses zero.  So this file asks two different questions:

  * **Ⓑ②ᵃ** TT and EE by their ratio to CAMB -- a question about the NORMALISATION, which is what
    the two factors are;
  * **Ⓑ②ᵇ** TE by `r_l` -- a question about the SHAPE of the cross spectrum, which a factor of two
    cannot repair and cannot hide either.

⛔ `Ⓑ②ᵇ` can fail while `Ⓐ①` passes exactly, and that is the point of running it: a correlation
coefficient is blind to the constant this revision adds.

⌗ The input is the bank point RE-RUN with the switch set, at the bank's own configuration, not the
saved point multiplied by two: the multiplication is what `Ⓐ①` measured, and using it here would
make this arm read back that arm's own arithmetic.

    python3 camb_three.py        # rc=0 when both legs hold
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
#: ⛔ FOUR dirnames: this file sits three directories below the repository root.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
sys.path.insert(0, os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_'
                                      'lensing_bandpowers'))
sys.path.insert(0, os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                                      'the_harness_does_not_have'))
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

ON = os.environ.get('ONPOINT', '/tmp/claude-0/r7860/on.npz')
AS, K_PIVOT, SUM_REF = 2.1e-9, 0.05, 0.06
H0, OM, WB, TAU = 67.40, 0.3150, 0.0224, 0.054
TOL_RATIO, TOL_R = 0.03, 0.05


def main():
    if not os.path.exists(ON):
        print('\n  ⛔ the switch-on bank point is not on disk at %s -- nothing is claimed.\n' % ON)
        return 1
    import camb
    from camb import model as camb_model
    import model6 as M6
    import phiphi as PP

    z = np.load(ON, allow_pickle=True)
    lsb = np.asarray(z['ls'], float)
    ns = float(PP.NS)
    amp = (4.0 / 9.0) * AS * K_PIVOT ** (1.0 - ns)
    k = amp * M6.T_CMB_UK ** 2 * float(np.exp(-2.0 * TAU))
    tt_i = k * np.asarray(z['Dl'], float)
    ee_i = k * np.asarray(z['Dl_EE'], float)
    te_i = k * np.asarray(z['Dl_TE'], float)

    h = H0 / 100.0
    p = camb.set_params(H0=H0, ombh2=WB, omch2=(OM - WB / h ** 2) * h ** 2 - SUM_REF / 93.14,
                        mnu=SUM_REF, tau=TAU, ns=ns, As=AS, lmax=2600, WantTransfer=True)
    p.NonLinear = camb_model.NonLinear_none
    r = camb.get_results(p)
    tot = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['total'])['total']
    lsc = np.arange(tot.shape[0])
    tt_c = np.interp(lsb, lsc, np.nan_to_num(tot[:, 0]))
    ee_c = np.interp(lsb, lsc, np.nan_to_num(tot[:, 1]))
    te_c = np.interp(lsb, lsc, np.nan_to_num(tot[:, 3]))

    print(__doc__)
    print('=' * 100)
    print('\n  Ⓑ②ᵃ TT AND EE BY THEIR RATIO TO CAMB %s, over %d multipoles l %d .. %d'
          % (camb.__version__, len(lsb), int(lsb.min()), int(lsb.max())))
    print('  ' + '-' * 98)
    out, legs = {}, {}
    for name, a, b in (('TT', tt_i, tt_c), ('EE', ee_i, ee_c)):
        g = (np.abs(b) > 0) & np.isfinite(a) & np.isfinite(b)
        rat = a[g] / b[g]
        gm = float(np.exp(np.mean(np.log(np.abs(rat)))))
        d = dict(geometric_mean=gm, n=int(g.sum()), lo=float(rat.min()), hi=float(rat.max()),
                 worst_rel=float(np.max(np.abs(rat - gm)) / gm),
                 within=bool(abs(gm - 1.0) < TOL_RATIO))
        legs[name] = d
        print('    %-3s  n=%3d   geometric mean %.6f   range %.4f .. %.4f   within %.2f of one: %s'
              % (name, d['n'], gm, d['lo'], d['hi'], TOL_RATIO, d['within']))
    a_holds = bool(legs['TT']['within'] and legs['EE']['within'])
    print('\n    ** Ⓑ②ᵃ %s **' % ('HOLDS' if a_holds else 'FAILS, and the failure is the report'))
    out['ratios'] = legs
    out['B2a_holds'] = a_holds

    print('\n  Ⓑ②ᵇ TE BY ITS CORRELATION COEFFICIENT `r_l = TE / sqrt(TT x EE)`')
    print('  ' + '-' * 98)
    g = (tt_i > 0) & (ee_i > 0) & (tt_c > 0) & (ee_c > 0)
    r_i = te_i[g] / np.sqrt(tt_i[g] * ee_i[g])
    r_c = te_c[g] / np.sqrt(tt_c[g] * ee_c[g])
    dr = np.abs(r_i - r_c)
    med, worst = float(np.median(dr)), float(np.max(dr))
    b_holds = bool(med < TOL_R)
    print('    n=%3d   median |r_mine - r_camb| %.4f   worst %.4f   against a criterion of %.2f'
          % (int(g.sum()), med, worst, TOL_R))
    for i in (0, int(g.sum()) // 4, int(g.sum()) // 2, 3 * int(g.sum()) // 4, int(g.sum()) - 1):
        print('      l = %5d   r_mine %+.4f   r_camb %+.4f   diff %+.4f'
              % (int(lsb[g][i]), r_i[i], r_c[i], r_i[i] - r_c[i]))
    print('\n    ** Ⓑ②ᵇ %s **  *and it is blind to the constant `Ⓐ①` adds, by construction*'
          % ('HOLDS' if b_holds else 'FAILS, and the failure is the report'))
    out['correlation'] = dict(n=int(g.sum()), median_abs_diff=med, worst_abs_diff=worst,
                              criterion=TOL_R, holds=b_holds)
    out['B2b_holds'] = b_holds
    out['holds'] = bool(a_holds and b_holds)
    out['camb_version'] = camb.__version__
    out['point'] = os.path.basename(ON)
    with io.open(os.path.join(_HERE, 'camb_three.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  %s Ⓑ② %s\n' % ('✔' if out['holds'] else '⛔',
                              'holds' if out['holds'] else 'does NOT hold'))
    return 0 if out['holds'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
