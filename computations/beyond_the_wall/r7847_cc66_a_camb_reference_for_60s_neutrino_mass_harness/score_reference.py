"""r7847+cc66: the CAMB reference SCORED THROUGH 60's OWN MODULES.  Order r7847 (69) item (3).

Nothing here reimplements 60's likelihood.  `score_ttteee.chi2_of` is 60's CMB half -- plik_lite
2018 TT/TE/EE, their covariance, their closed-form single amplitude -- and `lensing_like` is their
lensing half, the nine Planck 2018 CONSERVATIVE bandpowers through their own window functions,
plus their tau prior (0.054 +/- 0.007).  Only the SPECTRA are mine.

** THE AMPLITUDE MECHANISM IS 60's AND IS KEPT. **  The CMB fit determines `A * exp(-2 tau)` in
closed form; `C_L^phiphi` scales with `A`, so the lensing prediction is `A x phiphi(CAMB)` and tau
cannot cancel out of it.  That is `model6`'s mechanism, stated in its own docstring.

⌗ TWO CONVENTION TRAPS, one of them 60's and one of them MINE, and they are mirror images.
`bandpowers_from` wants RAW `C_L^phiphi` and applies `[L(L+1)]^2/(2 pi)` itself.  60 first fed it
raw when it wanted scaled and caught `1.9e5` rising with L -- a MISSING L^4.  I first fed it
`get_lens_potential_cls`'s already-scaled output and got `2.2e7` rising with L -- a SURPLUS L^4.
The same guard caught both.  Feed `raw_cl=True`.

⌗ AND THE 555-BIN SUBSET CANNOT BE REPRODUCED HERE, which is stated rather than substituted:
60's mask is `isfinite` over its own solver's grid, and `POL_DIR`/`PPGRID` both default under
`/tmp`, so those grids are gone.  This scores the FULL 613 plik_lite bins.  That is MORE
information than 60's 555, so it biases the limit TIGHTER -- against this seat's own registered
call that the limit comes out loose.
"""
import json, os, sys
import numpy as np
import camb
from scipy.optimize import minimize_scalar

_BTW = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_'
                                      'lensing_bandpowers'))
sys.path.insert(0, os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                                      'the_harness_does_not_have'))
import score_ttteee as SC                                                    # noqa: E402
import lensing_like as LL                                                    # noqa: E402

H0, OM, WB, NS, AS = 67.40, 0.3150, 0.0224, 0.965, 2.1e-9
OM_M = OM * (H0 / 100.0) ** 2
LMAX = 2600
HERE = os.path.dirname(os.path.abspath(__file__))
SUMS = [0.0, 0.02, 0.05, 0.08, 0.12, 0.16, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
_CACHE = {}


def spectra(sum_ev, tau):
    key = (round(sum_ev, 6), round(tau, 6))
    if key in _CACHE:
        return _CACHE[key]

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=H0, ombh2=WB, omch2=max(OM_M - WB - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=tau)
        p.InitPower.set_params(As=AS, ns=NS)
        p.set_for_lmax(LMAX, lens_potential_accuracy=4)
        return p
    p = build(0.0)
    p = build(p.omnuh2)
    r = camb.get_results(p)
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['lensed_scalar'])['lensed_scalar']
    raw = r.get_lens_potential_cls(lmax=LMAX, raw_cl=True)[:, 0]
    _CACHE[key] = (cl, raw)
    return cl, raw


def total_chi2(sum_ev, tau, lensing=True, tau_prior=True):
    cl, raw = spectra(sum_ev, tau)
    c2c, dof, amp, _ = SC.chi2_of(np.arange(cl.shape[0], dtype=float),
                                  cl[:, 0], cl[:, 3], cl[:, 1])
    out = dict(chi2_cmb=float(c2c), dof_cmb=int(dof), amplitude=float(amp), chi2_lens=0.0,
               chi2_tau=0.0)
    if lensing:
        bp = amp * LL.bandpowers_from(np.arange(raw.shape[0], dtype=float), raw)
        out['chi2_lens'] = float(LL.chi2(bp))
        out['bandpowers'] = [float(v) for v in bp]
    if tau_prior:
        out['chi2_tau'] = float(LL.chi2_tau(tau))
    out['total'] = out['chi2_cmb'] + out['chi2_lens'] + out['chi2_tau']
    return out


def profile(sum_ev):
    """minimise the total over tau -- the one parameter the lensing term makes live"""
    f = minimize_scalar(lambda t: total_chi2(sum_ev, float(t))['total'],
                        bounds=(0.020, 0.120), method='bounded',
                        options=dict(xatol=2e-4))
    best = total_chi2(sum_ev, float(f.x))
    best['tau_hat'] = float(f.x)
    best['sum'] = float(sum_ev)
    return best


def main():
    rows = [profile(s) for s in SUMS]
    t = np.array([r['total'] for r in rows])
    s = np.array([r['sum'] for r in rows])
    dchi2 = t - t.min()
    out = dict(
        control=dict(H0=H0, Om=OM, ombh2=WB, ns=NS, As=AS, om_m_held=OM_M),
        scored_bins=int(rows[0]['dof_cmb']), nbandpowers=int(LL.NBP),
        tau_prior=dict(mean=LL.TAU_MEAN, sigma=LL.TAU_SIGMA),
        bin_subset_note='full 613 plik_lite bins; 60 own 555-bin mask is NOT reproducible here '
                        'because it is isfinite over grids that lived under /tmp',
        rows=rows, sums=[float(v) for v in s], total=[float(v) for v in t],
        dchi2=[float(v) for v in dchi2])
    # the 95 % one-sided limit on one parameter: Delta chi^2 = 2.71
    fine = np.linspace(s.min(), s.max(), 4001)
    # ** THE SCAN STARTS AT THE MINIMUM, NOT AT Sum = 0. **  The minimum of this profile is NOT at
    # Sum = 0 -- it sits near 0.05 eV -- so Sum = 0 is ITSELF above Delta chi^2 = 2.71 and a scan
    # from the bottom of the grid returns the first grid point, 0.0.  That is not a limit, and
    # because 0.0 is falsy it then reported itself as 'ABOVE THE GRID', which is the opposite of
    # what the grid says.  The upper limit is the first crossing ABOVE the minimum.
    i = int(np.argmin(t))
    hi_s, hi_d = s[i:], dchi2[i:]
    fine = np.linspace(float(hi_s[0]), float(hi_s[-1]), 20001)
    dfine = np.interp(fine, hi_s, hi_d)
    above = np.where(dfine > 2.71)[0]
    out['sum_at_min_eV'] = float(s[i])
    out['limit95_eV'] = float(fine[above[0]]) if above.size else None
    out['limit95_meV'] = (out['limit95_eV'] * 1000.0) if out['limit95_eV'] is not None else None
    json.dump(out, open(os.path.join(HERE, 'score_reference.json'), 'w'), indent=2)
    print('%8s %10s %10s %9s %8s %9s' % ('Sum(eV)', 'chi2_cmb', 'chi2_lens', 'chi2_tau',
                                         'tau_hat', 'd_chi2'))
    for r, d in zip(rows, dchi2):
        print('%8.3f %10.2f %10.3f %9.3f %8.4f %9.3f'
              % (r['sum'], r['chi2_cmb'], r['chi2_lens'], r['chi2_tau'], r['tau_hat'], d))
    print()
    print('  minimum at Sum = %.3f eV ; 95%% limit (Delta chi2 = 2.71) = %s meV'
          % (out['sum_at_min_eV'],
             ('%.1f' % out['limit95_meV']) if out['limit95_meV'] else 'ABOVE THE GRID'))


if __name__ == '__main__':
    main()
