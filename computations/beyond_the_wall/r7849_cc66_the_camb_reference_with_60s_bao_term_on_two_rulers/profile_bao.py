"""r7849+cc66: THE SAME CAMB REFERENCE, WITH 60's BAO TERM, ON TWO TREATMENTS OF THE RULER.

Order r7849 (69) items ① and ②.  r7847's reference scored the CMB half and the lensing half and
NO BAO, against a 60 control and a published figure that BOTH carry DESI DR2.  That made the
headline comparison not like for like and the "subset, not instrument" verdict is withdrawn.

** THE BAO TERM IS 60's OWN, NOT A REIMPLEMENTATION. **  distances.chi2_bao, DESI DR2's 13
measurements (six anisotropic pairs and one isotropic), on distances.E_stack -- the radiation-free
flat-LCDM rate that ARMS['lcdm'], 60's CONTROL arm, uses.

** AND E_stack CARRIES NO SUM DEPENDENCE AT ALL. **  E_stack(z, Om, h) = sqrt(Om (1+z)^3 + 1 - Om):
it does not even use h.  So the BAO term CANNOT constrain the sum directly.  Its whole effect must
run through pinning the geometry the sum trades against -- which r7847's opened profile showed
plainly, H0 running 67.95 -> 64.18 and Om 0.308 -> 0.358 as the sum grew.  The H0 and Om columns
written here are therefore the mechanistic check (Ⓖ), not decoration.

TWO RULERS, which is item ②:
  rd_camb -- r_d is CAMB's own sound horizon at the drag epoch at each point (derived 'rdrag'),
             as the published analysis does.  The absolute distance scale is then CALIBRATED.
  rd_min  -- r_d is minimised over (120, 170) at each point, as 60's model3.bao_direct does.
             The absolute scale is then FREE and BAO constrains only the shape.
⌗ At the control these already differ: chi2_bao is 31.63 at CAMB's rdrag = 147.06 Mpc against
  14.56 at a minimised 148.66 Mpc, so the calibrated arm is a materially stronger constraint.

** IDEMPOTENT BY DESIGN, because r7847's profile_open.py wrote NOTHING until it finished and a
timeout would have lost all of it. **  One JSON per (mode, sum) under out/; an existing file is
skipped, so a restart re-runs only what is missing.

Accuracy and grid match r7847's opened profile exactly (LMAX 2600, lens_potential_accuracy 1,
the same eight sums, the same two starts) so the two are comparable term by term.
Run: python3 -I profile_bao.py            (numpy, scipy, camb)
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

H0_0, OM_0, WB, NS, AS = 67.40, 0.3150, 0.0224, 0.965, 2.1e-9
LMAX = 2600
SUMS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
MODES = ('rd_camb', 'rd_min')
OUT = os.path.join(HERE, 'out')

# the minimised-r_d BAO chi^2 depends ONLY on (H0, Om) -- E_stack has no sum dependence and r_d is
# free -- so it is cached, exactly the reason 60 spline it rather than re-minimise
_RDMIN = {}


def bao_min(h0, om):
    key = (round(h0, 4), round(om, 5))
    if key not in _RDMIN:
        r = minimize_scalar(lambda rd: DI.chi2_bao(h0, om, rd, DI.E_stack),
                            bounds=(120.0, 170.0), method='bounded')
        _RDMIN[key] = (float(r.fun), float(r.x))
    return _RDMIN[key]


def score(sum_ev, h0, om, tau, mode, acc=1):
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
        cl = r.get_cmb_power_spectra(p, CMB_unit='muK',
                                     spectra=['lensed_scalar'])['lensed_scalar']
        raw = r.get_lens_potential_cls(lmax=LMAX, raw_cl=True)[:, 0]
        rd_camb = float(r.get_derived_params()['rdrag'])
    except Exception:
        return 1e9, {}
    c2c, dof, amp, _ = SC.chi2_of(np.arange(cl.shape[0], dtype=float), cl[:, 0], cl[:, 3], cl[:, 1])
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
                     H0=h0, Om=om, tau=tau, dof_cmb=int(dof))


def profile(sum_ev, mode):
    def f(x):
        h0, om, tau = x
        if not (60.0 <= h0 <= 75.0 and 0.25 <= om <= 0.40 and 0.02 <= tau <= 0.12):
            return 1e9
        return score(sum_ev, h0, om, tau, mode)[0]
    best = None
    for start in ((H0_0, OM_0, 0.054), (H0_0 - 1.5, OM_0 + 0.012, 0.060)):
        r = minimize(f, np.array(start), method='Nelder-Mead',
                     options=dict(xatol=2e-3, fatol=5e-3, maxfev=240))
        if best is None or r.fun < best.fun:
            best = r
    tot, det = score(sum_ev, *best.x, mode)
    det.update(sum=float(sum_ev), total=float(tot), nfev=int(best.nfev), mode=mode)
    return det


def main():
    os.makedirs(OUT, exist_ok=True)
    done = skipped = 0
    for mode in MODES:
        for s in SUMS:
            path = os.path.join(OUT, '%s_%.3f.json' % (mode, s))
            if os.path.exists(path):
                skipped += 1
                print('  skip (already done): %s' % os.path.basename(path), flush=True)
                continue
            det = profile(s, mode)
            json.dump(det, open(path, 'w'), indent=1)
            done += 1
            print('  %-8s Sum=%.3f: total %10.3f  cmb %9.3f  lens %7.3f  bao %8.3f  '
                  'tau %.4f  H0 %7.3f  Om %.4f  rd %7.3f  nfev %d'
                  % (mode, s, det['total'], det['chi2_cmb'], det['chi2_lens'], det['chi2_bao'],
                     det['tau'], det['H0'], det['Om'], det['rd_used'], det['nfev']), flush=True)
    print('\n  wrote %d, skipped %d, of %d expected' % (done, skipped, len(MODES) * len(SUMS)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
