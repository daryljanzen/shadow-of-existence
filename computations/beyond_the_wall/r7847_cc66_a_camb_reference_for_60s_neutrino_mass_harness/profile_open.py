"""r7847+cc66: the SAME score, with the geometric degeneracy OPENED.  Order r7847 (69) item (3).

`score_reference.py` profiled tau only and held H0, Om, wb, ns at 60's control.  That is a
CONDITIONAL limit and it is TIGHT for exactly that reason: Sum m_nu is strongly degenerate with
H0 and Om, and holding them forbids the data from paying for a larger sum by moving the geometry.

** SO THE LIMIT THAT DECIDES THE REGISTERED CALL IS THIS ONE, NOT THAT ONE. **  Here tau, H0 and
Om are all free at each sum.  wb and ns stay at the control: the CMB pins both tightly and
neither is the direction Sum runs along.

Accuracy note: `lens_potential_accuracy` drops 4 -> 1 to make the 3-D profile affordable.  The
control chi^2 is re-reported at BOTH settings so the cost of that choice is visible rather than
assumed.
"""
import json, os, sys
import numpy as np
import camb
from scipy.optimize import minimize

_BTW = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_'
                                      'lensing_bandpowers'))
sys.path.insert(0, os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                                      'the_harness_does_not_have'))
import score_ttteee as SC                                                    # noqa: E402
import lensing_like as LL                                                    # noqa: E402

H0_0, OM_0, WB, NS, AS = 67.40, 0.3150, 0.0224, 0.965, 2.1e-9
LMAX = 2600
HERE = os.path.dirname(os.path.abspath(__file__))
SUMS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]


def score(sum_ev, h0, om, tau, acc=1):
    om_m = om * (h0 / 100.0) ** 2
    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=h0, ombh2=WB, omch2=max(om_m - WB - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=tau)
        p.InitPower.set_params(As=AS, ns=NS)
        p.set_for_lmax(LMAX, lens_potential_accuracy=acc)
        return p
    try:
        p = build(0.0)
        p = build(p.omnuh2)
        r = camb.get_results(p)
        cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['lensed_scalar'])['lensed_scalar']
        raw = r.get_lens_potential_cls(lmax=LMAX, raw_cl=True)[:, 0]
    except Exception:
        return 1e9, {}
    c2c, dof, amp, _ = SC.chi2_of(np.arange(cl.shape[0], dtype=float), cl[:, 0], cl[:, 3], cl[:, 1])
    bp = amp * LL.bandpowers_from(np.arange(raw.shape[0], dtype=float), raw)
    c2l = float(LL.chi2(bp)); c2t = float(LL.chi2_tau(tau))
    return float(c2c) + c2l + c2t, dict(chi2_cmb=float(c2c), chi2_lens=c2l, chi2_tau=c2t,
                                        amplitude=float(amp), H0=h0, Om=om, tau=tau)


def profile(sum_ev):
    def f(x):
        h0, om, tau = x
        if not (60.0 <= h0 <= 75.0 and 0.25 <= om <= 0.40 and 0.02 <= tau <= 0.12):
            return 1e9
        return score(sum_ev, h0, om, tau)[0]
    best = None
    for start in ((H0_0, OM_0, 0.054), (H0_0 - 1.5, OM_0 + 0.012, 0.060)):
        r = minimize(f, np.array(start), method='Nelder-Mead',
                     options=dict(xatol=2e-3, fatol=5e-3, maxfev=240))
        if best is None or r.fun < best.fun:
            best = r
    tot, det = score(sum_ev, *best.x)
    det.update(sum=float(sum_ev), total=float(tot), nfev=int(best.nfev))
    return det


def main():
    c_acc4 = score(0.0, H0_0, OM_0, 0.054, acc=4)[0]
    c_acc1 = score(0.0, H0_0, OM_0, 0.054, acc=1)[0]
    rows = [profile(s) for s in SUMS]
    t = np.array([r['total'] for r in rows]); s = np.array([r['sum'] for r in rows])
    dc = t - t.min(); i = int(np.argmin(t))
    hi_s, hi_d = s[i:], dc[i:]
    fine = np.linspace(hi_s[0], hi_s[-1], 20001); fd = np.interp(fine, hi_s, hi_d)
    k = np.where(fd > 2.71)[0]
    out = dict(control_total_acc4=c_acc4, control_total_acc1=c_acc1,
               accuracy_cost=c_acc4 - c_acc1, free='tau, H0, Om', held='wb, ns',
               scored_bins=613, rows=rows, sums=[float(v) for v in s],
               total=[float(v) for v in t], dchi2=[float(v) for v in dc],
               sum_at_min_eV=float(s[i]),
               limit95_meV=float(fine[k[0]] * 1000) if k.size else None)
    json.dump(out, open(os.path.join(HERE, 'profile_open.json'), 'w'), indent=2)
    print('control total chi2: acc=4 %.3f   acc=1 %.3f   (cost %.3f)' % (c_acc4, c_acc1, c_acc4 - c_acc1))
    print('%8s %10s %10s %8s %8s %8s %9s %6s'
          % ('Sum(eV)', 'chi2_cmb', 'chi2_lens', 'tau', 'H0', 'Om', 'd_chi2', 'nfev'))
    for r, d in zip(rows, dc):
        print('%8.3f %10.2f %10.3f %8.4f %8.3f %8.4f %9.3f %6d'
              % (r['sum'], r['chi2_cmb'], r['chi2_lens'], r['tau'], r['H0'], r['Om'], d, r['nfev']))
    print()
    print('minimum at %.1f meV ; 95%% limit = %s meV'
          % (out['sum_at_min_eV'] * 1000,
             ('%.1f' % out['limit95_meV']) if out['limit95_meV'] else 'ABOVE GRID'))


if __name__ == '__main__':
    main()
