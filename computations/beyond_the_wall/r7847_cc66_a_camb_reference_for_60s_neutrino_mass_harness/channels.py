"""r7847+cc66: CAMB's decomposition of the response to Sum m_nu, at 60's control cosmology.

Order r7847 (69) items (1)-(2).  The convention is 69's and 60's: TOTAL omega_m HELD, so omega_cb
falls by omega_nu; three species, normal ordering.

** EVERY CHANNEL HERE IS A DIFFERENCE OF REAL CAMB RUNS, NOT AN ANALYTIC MODEL. **

  lensing smoothing   d(lensed) - d(unlensed)                 -- what lensing adds to the primary
  geometric           the theta_* shift, as an ell-rescaling  -- the background at fixed omega_m
  early (radiation)   d(unlensed) - geometric                 -- the residual: Phi in the rad era
  free-streaming      d(phiphi) - its geometric part          -- late-time growth suppression
"""
import json, os, sys
import numpy as np
import camb

H0, OM, WB, NS, TAU = 67.40, 0.3150, 0.0224, 0.965, 0.054
AS = 2.1e-9
LMAX = 2600
OM_M = OM * (H0 / 100.0) ** 2          # total omega_m, held at every sum
SUMS = [0.0, 0.02, 0.05, 0.10, 0.20, 0.30, 0.40, 0.60]
HERE = os.path.dirname(os.path.abspath(__file__))


def run(sum_ev):
    """one CAMB model at this sum, with total omega_m held"""
    def build(onu_guess):
        p = camb.CAMBparams()
        p.set_cosmology(H0=H0, ombh2=WB, omch2=max(OM_M - WB - onu_guess, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=TAU)
        p.InitPower.set_params(As=AS, ns=NS)
        p.set_for_lmax(LMAX, lens_potential_accuracy=4)
        return p
    p = build(0.0)
    p = build(p.omnuh2)                # omnuh2 depends only on mnu, so one pass fixes it
    r = camb.get_results(p)
    tot = p.ombh2 + p.omch2 + p.omnuh2
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK',
                                 spectra=['lensed_scalar', 'unlensed_scalar'])
    pp = r.get_lens_potential_cls(lmax=LMAX)[:, 0]
    th = r.cosmomc_theta()             # theta_* : the acoustic scale, the geometry in one number
    return dict(sum=sum_ev, omnuh2=float(p.omnuh2), omch2=float(p.omch2), om_m=float(tot),
                theta=float(th), lensed=cl['lensed_scalar'], unlensed=cl['unlensed_scalar'], pp=pp)


def ell_rescale(ls, spec, dlnl):
    """the GEOMETRIC channel: a pure shift of the acoustic scale is a rescaling of ell"""
    good = ls >= 2
    out = np.zeros_like(spec)
    out[good] = np.interp(ls[good] * (1.0 + dlnl), ls[good], spec[good])
    return out - spec


def main():
    models = [run(s) for s in SUMS]
    base = models[0]
    ls = np.arange(base['lensed'].shape[0], dtype=float)
    out = {'convention': 'total omega_m held; omega_cb falls by omega_nu; 3 species, normal order',
           'control': dict(H0=H0, Om=OM, ombh2=WB, ns=NS, tau=TAU, om_m_held=OM_M),
           'om_m_check': [m['om_m'] for m in models],
           'sums': SUMS, 'omnuh2': [m['omnuh2'] for m in models],
           'theta': [m['theta'] for m in models], 'channels': {}}

    # the derivative is taken over the FIRST interval, where 60's model6 linearises (Sum = 0)
    hi, lo = models[1], models[0]
    dS = hi['sum'] - lo['sum']
    dlnth = (hi['theta'] - lo['theta']) / lo['theta'] / dS      # d ln theta_* / dSum

    for idx, name in ((0, 'TT'), (1, 'EE'), (3, 'TE')):
        dlen = (hi['lensed'][:, idx] - lo['lensed'][:, idx]) / dS
        dunl = (hi['unlensed'][:, idx] - lo['unlensed'][:, idx]) / dS
        geo = ell_rescale(ls, lo['unlensed'][:, idx], dlnth * dS) / dS
        out['channels'][name] = dict(
            lensing_smoothing=dlen - dunl, geometric=geo, early=dunl - geo, total=dlen)

    dpp = (hi['pp'] - lo['pp']) / dS
    lpp = np.arange(lo['pp'].shape[0], dtype=float)
    geo_pp = ell_rescale(lpp, lo['pp'], dlnth * dS) / dS
    out['channels']['PP'] = dict(geometric=geo_pp, free_streaming=dpp - geo_pp, total=dpp)

    np.savez_compressed(os.path.join(HERE, 'channels.npz'),
                        ls=ls, lpp=lpp, dlnth_dsum=dlnth,
                        **{f'{k}_{c}': v for k, v in out['channels'].items()
                           for c, v in v.items()},
                        base_lensed=lo['lensed'], base_unlensed=lo['unlensed'], base_pp=lo['pp'],
                        sums=np.array(SUMS), theta=np.array(out['theta']),
                        omnuh2=np.array(out['omnuh2']),
                        all_lensed=np.array([m['lensed'] for m in models]),
                        all_unlensed=np.array([m['unlensed'] for m in models]),
                        all_pp=np.array([m['pp'] for m in models]))

    # ── the report: fractional share of each channel, in the band each spectrum is scored on ────
    rep = {'dlnth_dsum_per_eV': dlnth, 'om_m_held_exactly': bool(
        max(abs(m['om_m'] - OM_M) for m in models) < 1e-9), 'bands': {}}
    for name, band in (('TT', (30, 2000)), ('TE', (30, 1500)), ('EE', (30, 1500)),
                       ('PP', (8, 400))):
        ch = out['channels'][name]
        a, b = band
        w = (slice(a, b + 1))
        tot = np.sqrt(np.mean(ch['total'][w] ** 2))
        rep['bands'][name] = {'band': band, 'rms_total': float(tot)}
        for c, v in ch.items():
            if c == 'total':
                continue
            rep['bands'][name][c] = float(np.sqrt(np.mean(v[w] ** 2)) / tot) if tot else None
    json.dump(rep, open(os.path.join(HERE, 'channels.json'), 'w'), indent=2)
    print(json.dumps(rep, indent=2))


if __name__ == '__main__':
    main()
