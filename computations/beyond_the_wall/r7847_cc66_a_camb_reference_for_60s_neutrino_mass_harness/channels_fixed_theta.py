"""r7847+cc66: the channel split, with the GEOMETRIC channel isolated RIGOROUSLY.

Order r7847 (69) item (2).  `channels.py` modelled the geometric channel as an ell-rescaling by
d ln theta_*.  That is only first order, and the residual it leaves was large enough in TT to
decide a registered prediction -- so it is redone here WITHOUT a model of the geometry:

  ** H0 IS SOLVED AT EACH SUM SO THAT theta_* IS HELD TO 1e-13. **

The response at held theta_* is then the genuinely NON-GEOMETRIC one, and the difference from the
free-H0 run IS the geometry.  No interpolation, no analytic form: two real CAMB runs.

⌗ THE SHARES DO NOT PARTITION.  They are RMS ratios of channels that partially CANCEL, so they
need not sum to one, and the crude model's TE share exceeded one for exactly that reason.

⌗ AND WHAT `NON-GEOMETRIC` DOES NOT MEAN.  Holding theta_* removes the acoustic scale.  What is
left still mixes the early-time terms (the radiation-era Phi, the early ISW, the damping) with the
late-time ones (growth, the late ISW at low ell).  It is an upper bound on the radiation-era
channel 60 is ordered to carry, NOT a measurement of it alone.
"""
import json, os
import numpy as np
import camb
from scipy.optimize import brentq

H0, OM, WB, NS, TAU, AS = 67.40, 0.3150, 0.0224, 0.965, 0.054, 2.1e-9
OM_M = OM * (H0 / 100.0) ** 2
LMAX = 2600
STEP = 0.02
HERE = os.path.dirname(os.path.abspath(__file__))


def model(sum_ev, h0):
    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=h0, ombh2=WB, omch2=max(OM_M - WB - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=TAU)
        p.InitPower.set_params(As=AS, ns=NS)
        p.set_for_lmax(LMAX, lens_potential_accuracy=4)
        return p
    p = build(0.0)
    p = build(p.omnuh2)
    r = camb.get_results(p)
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK',
                                 spectra=['lensed_scalar', 'unlensed_scalar'])
    return cl, float(r.cosmomc_theta()), r.get_lens_potential_cls(lmax=LMAX)[:, 0]


def main():
    cl0, th0, pp0 = model(0.0, H0)
    cla, tha, ppa = model(STEP, H0)                        # free H0: geometry moves
    h_fix = brentq(lambda h: model(STEP, h)[1] - th0, H0 - 3.0, H0 + 3.0, xtol=1e-6)
    clb, thb, ppb = model(STEP, h_fix)                     # theta_* held: geometry frozen

    U0, Ua, Ub = (c['unlensed_scalar'] for c in (cl0, cla, clb))
    L0, La = cl0['lensed_scalar'], cla['lensed_scalar']
    out = {'control': dict(H0=H0, Om=OM, ombh2=WB, ns=NS, tau=TAU, om_m_held=OM_M),
           'convention': 'total omega_m held; omega_cb falls by omega_nu; 3 species, normal order',
           'step_eV': STEP, 'theta_0': th0,
           'H0_for_held_theta': h_fix,
           'theta_residual_when_held': (thb - th0) / th0,
           'dln_theta_dsum_per_eV': (tha - th0) / th0 / STEP, 'bands': {}}

    def rms(x, w):
        return float(np.sqrt(np.mean(np.asarray(x)[w] ** 2)))

    for idx, name, (a, b) in ((0, 'TT', (30, 2000)), (3, 'TE', (30, 1500)),
                              (1, 'EE', (30, 1500))):
        w = slice(a, b + 1)
        d_tot = (Ua[:, idx] - U0[:, idx]) / STEP
        d_non = (Ub[:, idx] - U0[:, idx]) / STEP
        d_len = (La[:, idx] - L0[:, idx]) / STEP
        out['bands'][name] = dict(
            band=[a, b], rms_unlensed_total=rms(d_tot, w),
            non_geometric_share=rms(d_non, w) / rms(d_tot, w),
            geometric_share=rms(d_tot - d_non, w) / rms(d_tot, w),
            lensing_smoothing_share_of_lensed=rms(d_len - d_tot, w) / rms(d_len, w))

    w = slice(8, 401)
    d_pp, d_pp_non = (ppa - pp0) / STEP, (ppb - pp0) / STEP
    out['bands']['PP'] = dict(
        band=[8, 400], rms_total=rms(d_pp, w),
        non_geometric_share=rms(d_pp_non, w) / rms(d_pp, w),
        geometric_share=rms(d_pp - d_pp_non, w) / rms(d_pp, w),
        dCl_dsum_at_L100=float(d_pp[100]),
        sign='negative = free-streaming suppression' if d_pp[100] < 0 else 'POSITIVE')
    json.dump(out, open(os.path.join(HERE, 'channels_fixed_theta.json'), 'w'), indent=2)
    np.savez_compressed(os.path.join(HERE, 'channels_fixed_theta.npz'),
                        unlensed_0=U0, unlensed_freeH0=Ua, unlensed_heldtheta=Ub,
                        lensed_0=L0, lensed_freeH0=La, pp_0=pp0, pp_freeH0=ppa,
                        pp_heldtheta=ppb, h_fix=h_fix, theta_0=th0, step=STEP)
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
