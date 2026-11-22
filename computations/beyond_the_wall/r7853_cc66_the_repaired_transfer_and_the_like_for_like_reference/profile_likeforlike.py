"""r7853+cc66 item ⑤: THE LIKE-FOR-LIKE REFERENCE -- 60's subset AND 60's FREEDOMS.

Order r7853 (69) item ⑤.  r7849's reference scored 60's subset but HELD omega_b and n_s at the
control, where 60's model6 PROFILES them -- six parameters, x6 splitting into
x4 = (H0, OM, WB, NS), the sum and tau.  Fewer free parameters tightens a limit for free, which is
why r7849's own receipt called its factor against 60 an UPPER BOUND on their instrument's share and
explicitly NOT a measurement of it.  This frees the two and makes the comparison a measurement.

FREE HERE: H0, Om, omega_b, n_s, tau -- five, profiled at each sum, on both rulers.
  rd_camb -- r_d is CAMB's own drag-epoch sound horizon, so the absolute scale is CALIBRATED.
  rd_min  -- r_d minimised over (120, 170), as 60's model3.bao_direct does, so the scale is FREE.

** THE EFFECTIVE MASS IS AN EXTRAPOLATED VERTEX HERE, NOT 60's ESTIMATOR, AND THEY ARE DIFFERENT
THINGS. **  60's effective mass is the posterior MEAN of the sum over a chain whose lower bound is
negative (sampler6: `lo = 0.0 if bounded else mod.cmb.s_lo`), which their own growth solver can
evaluate.  CAMB CANNOT: its neutrino sector is parameterised by physical masses and has no
negative-sum construction, and inventing one would be this seat's invention rather than CAMB's and
would not be like-for-like.  So what is reported is the PARABOLIC VERTEX of Delta chi^2(sum) fitted
to the lowest points, as r7849 already did and pinned -- an extrapolation of the profile, not a
solve below zero, and not the same estimator as a posterior mean.

** WARM STARTS, AND THE CHECK THAT THEY DID NOT DECIDE THE ANSWER. **  Five free parameters at
2.5 s a call is ~9 hours from cold starts, so each sum starts from the previous sum's solution,
which are close.  That makes the result depend on the SCAN ORDER, so --cold re-runs a chosen point
from the control start and the receipt compares the two: if a warm-started minimum is higher than
a cold-started one, the warm path got stuck and the arm says so.

** IDEMPOTENT: one JSON per (mode, sum) under out5/, an existing file skipped. **  This container
restarts unpredictably; r7847's profile wrote nothing until it finished and would have lost it all.

Run: python3 -I profile_likeforlike.py                 (numpy, scipy, camb)
     python3 -I profile_likeforlike.py --cold rd_camb 0.10
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize, minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(_BTW, 'r7749_70_leafgeom_refit'))
sys.path.insert(0, os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_'
                                      'lensing_bandpowers'))
sys.path.insert(0, os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                                      'the_harness_does_not_have'))
import camb                                                                  # noqa: E402
import distances as DI                                                       # noqa: E402
import score_ttteee as SC                                                    # noqa: E402
import lensing_like as LL                                                    # noqa: E402

#: the control, which is also the cold start -- 60's gen_phiphi.sh lcdm arm
X0 = (67.40, 0.3150, 0.0224, 0.965, 0.054)
LMAX = 2600
ACC = 1
SUMS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
MODES = ('rd_camb', 'rd_min')
OUT = os.path.join(HERE, 'out5')
#: (H0, Om, omega_b, n_s, tau) -- wide enough that the optimum is interior, checked in the receipt
BOX = ((60.0, 75.0), (0.25, 0.40), (0.0200, 0.0250), (0.92, 1.01), (0.02, 0.12))

_RDMIN = {}


def bao_min(h0, om):
    """minimised-r_d BAO chi^2 depends ONLY on (H0, Om): E_stack has no sum dependence"""
    key = (round(h0, 4), round(om, 5))
    if key not in _RDMIN:
        r = minimize_scalar(lambda rd: DI.chi2_bao(h0, om, rd, DI.E_stack),
                            bounds=(120.0, 170.0), method='bounded')
        _RDMIN[key] = (float(r.fun), float(r.x))
    return _RDMIN[key]


def score(sum_ev, h0, om, wb, ns, tau, mode):
    om_m = om * (h0 / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=h0, ombh2=wb, omch2=max(om_m - wb - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=tau)
        p.InitPower.set_params(As=2.1e-9, ns=ns)
        p.set_for_lmax(LMAX, lens_potential_accuracy=ACC)
        return p
    try:
        p = build(0.0)
        p = build(p.omnuh2)
        r = camb.get_results(p)
        cl = r.get_cmb_power_spectra(p, CMB_unit='muK',
                                     spectra=['lensed_scalar'])['lensed_scalar']
        raw = r.get_lens_potential_cls(lmax=LMAX, raw_cl=True)[:, 0]
        rd_camb = float(r.get_derived_params()['rdrag'])
    except Exception:
        return 1e9, {}
    c2c, dof, amp, _ = SC.chi2_of(np.arange(cl.shape[0], dtype=float),
                                  cl[:, 0], cl[:, 3], cl[:, 1])
    bp = amp * LL.bandpowers_from(np.arange(raw.shape[0], dtype=float), raw)
    c2l = float(LL.chi2(bp))
    c2t = float(LL.chi2_tau(tau))
    if mode == 'rd_camb':
        rd_used = rd_camb
        c2b = float(DI.chi2_bao(h0, om, rd_used, DI.E_stack))
    elif mode == 'rd_min':
        c2b, rd_used = bao_min(h0, om)
    else:
        raise ValueError(mode)
    tot = float(c2c) + c2l + c2t + c2b
    return tot, dict(chi2_cmb=float(c2c), chi2_lens=c2l, chi2_tau=c2t, chi2_bao=c2b,
                     rd_used=float(rd_used), rd_camb=rd_camb, amplitude=float(amp),
                     H0=h0, Om=om, ombh2=wb, ns=ns, tau=tau, dof_cmb=int(dof))


def profile(sum_ev, mode, start):
    def f(x):
        if not all(lo <= v <= hi for v, (lo, hi) in zip(x, BOX)):
            return 1e9
        return score(sum_ev, *x, mode)[0]
    r = minimize(f, np.array(start, float), method='Nelder-Mead',
                 options=dict(xatol=1e-3, fatol=5e-3, maxfev=500))
    tot, det = score(sum_ev, *r.x, mode)
    det.update(sum=float(sum_ev), total=float(tot), nfev=int(r.nfev), mode=mode,
               start=[float(v) for v in start], free=['H0', 'Om', 'ombh2', 'ns', 'tau'])
    return det


def main():
    os.makedirs(OUT, exist_ok=True)
    if '--cold' in sys.argv:
        i = sys.argv.index('--cold')
        mode, s = sys.argv[i + 1], float(sys.argv[i + 2])
        det = profile(s, mode, X0)
        det['cold'] = True
        path = os.path.join(OUT, 'cold_%s_%.3f.json' % (mode, s))
        json.dump(det, open(path, 'w'), indent=1)
        print('  COLD %-8s Sum=%.3f: total %10.3f  nfev %d' % (mode, s, det['total'],
                                                               det['nfev']), flush=True)
        return 0
    done = skipped = 0
    for mode in MODES:
        warm = X0
        for s in SUMS:
            path = os.path.join(OUT, '%s_%.3f.json' % (mode, s))
            if os.path.exists(path):
                d = json.load(open(path))
                warm = (d['H0'], d['Om'], d['ombh2'], d['ns'], d['tau'])
                skipped += 1
                print('  skip (already done): %s' % os.path.basename(path), flush=True)
                continue
            det = profile(s, mode, warm)
            json.dump(det, open(path, 'w'), indent=1)
            warm = (det['H0'], det['Om'], det['ombh2'], det['ns'], det['tau'])
            done += 1
            print('  %-8s Sum=%.3f: total %10.3f  cmb %9.3f  lens %7.3f  bao %8.3f  '
                  'H0 %7.3f  Om %.4f  wb %.5f  ns %.4f  tau %.4f  rd %7.3f  nfev %d'
                  % (mode, s, det['total'], det['chi2_cmb'], det['chi2_lens'], det['chi2_bao'],
                     det['H0'], det['Om'], det['ombh2'], det['ns'], det['tau'],
                     det['rd_used'], det['nfev']), flush=True)
    print('\n  wrote %d, skipped %d, of %d expected' % (done, skipped, len(MODES) * len(SUMS)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
