"""Ⓘ⑨: whether ACT DR6 CMB-only would close the control's remainder -- MEASURED, before adding it.

`r7845` ③: *"ACT DR6 CMB-only only if the control needs it, and say so."*  `PREDICTION.md`'s Ⓘ⑨:
*"If Ⓖ⑦ fails, whether ACT DR6 would close the remainder is measured before it is added."*

Ⓖ⑦ FAILED on both halves, so this measurement is owed.

⌗ **THE DATA IS BANKED.**  `computations/planck_tt_likelihood/data/act_dr6_cmbonly/` holds the
ACT DR6.02 CMB-only SACC file verbatim and its extraction: 45 foreground-marginalised bandpowers
each in TT, TE and EE, effective ell 600.5..6125.5, the full 135x135 covariance, and per-bandpower
windows on ell 2..8501.  It was banked at `r7815+70.1`.  This is the SECOND consecutive revision in
which an order offered data conditionally and the data was already in the harness -- `r7844`'s Ⓗ⑧
found the lensing bandpowers the same way.  So this is not a question about access.  It is a
question about whether the thing would help, and that is measurable.

## What is measured

**1. The tightening the remainder requires.**  Taking the control's own posterior and shrinking its
width about its own centre, the factor `f` at which the 95 per cent upper limit reaches the
published `64.2` meV.  Hence the width an INDEPENDENT dataset would have to deliver on its own,
`sigma_req = sigma_ctrl / sqrt(f**2 - 1)`.

**2. The information ACT DR6 could contribute, as an UPPER BOUND.**  A Fisher matrix on ACT's
banked bandpowers and covariance, built with this instrument's OWN spectra, marginalised over the
four background directions, giving `sigma_ACT(Sum)`.  Every choice in it is deliberately generous
to ACT:

  * **only the bandpowers this instrument reaches are used** -- those whose window weight lies
    entirely at `ell <= 1996`, the top of the banked spectra.  Dropping the rest is not generosity;
    it is the instrument's limit.  But the kept sub-covariance is the correct marginal for a
    sub-vector of a Gaussian, so no information is invented.
  * **ACT's calibration and polarisation-efficiency nuisances are NOT included.**  They are not
    banked (`DR6-ACT-lite` is refused from this container, HTTP 403), and leaving a nuisance
    unmarginalised OVERSTATES the data's information.
  * **ACT is treated as independent of Planck**, although its footprint lies inside Planck's sky
    and the kept bandpowers sit at `ell 600..1996`, inside the band Planck already scores here.
    The shared sky is therefore double-counted, which again OVERSTATES the gain.
  * **two amplitude treatments are reported, not one.**  Shared with Planck (so ACT keeps its
    normalisation information: the larger Fisher) and free-and-marginalised (the smaller).  A
    disjunction beats a pin.

If even this over-generous bound falls short of `sigma_req`, then ACT DR6 cannot close the
remainder and is not added.  *Reachable negative: a bound comfortably BELOW `sigma_req`, which
would make adding it the right call and this receipt would say so.*

**3. Which remainder is at issue.**  Ⓖ⑦ failed on the limit AND on the effective mass's sign.
Shrinking a width at fixed centre moves a limit down but moves a central value NOWHERE, so the
third measurement is what shrinking by `f` does to the effective-mass disagreement.

rc=0 on import.  Not a receipt: this is the measurement the receipt will assert.
"""
import json
import os
import sys

import numpy as np
import scipy.linalg
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from scipy.stats import norm

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
R7842 = os.path.join(BW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_harness_'
                         'does_not_have')
sys.path.insert(0, R7842)
sys.path.insert(0, os.path.join(BW, 'r7749_70_leafgeom_refit'))
import refit as R                                                          # noqa: E402
import model3 as M3                                                        # noqa: E402
import score_ttteee as SC                                                  # noqa: E402

ACT_NPZ = os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'data', 'act_dr6_cmbonly',
                       'act_dr6_cmbonly.npz')
ARM = 'lcdm'                      # the CONTROL -- Ⓘ⑨ is about whether the CONTROL needs ACT
PUBLISHED_LIMIT_MEV = 64.2
PUBLISHED_MEFF_MEV = -101.0
LMAX_INSTRUMENT = 1996.0          # the banked spectra's own top multipole
LMIN_INSTRUMENT = 100.0
INSIDE = 0.999                    # a bandpower is usable only if this much of its weight is inside


# ----------------------------------------------------------------- the control's own posterior
def control_posterior():
    """the unbounded chain's sum samples, in eV, and the bounded chain's recorded limit"""
    rec = json.load(open(os.path.join(HERE, 'sampler6_lcdm.json')))
    z = np.load(os.path.join(HERE, 'chain6_lcdm_u.npz'))
    key = [k for k in z.files if 'chain' in k or 'out' in k or 'samp' in k]
    arr = z[key[0]] if key else z[z.files[0]]
    arr = np.asarray(arr, float)
    flat = arr.reshape(-1, arr.shape[-1])
    names = ('H0', 'OM', 'WB', 'NS', 'MNU', 'TAU')
    s = flat[:, names.index('MNU')]
    return s, rec


def limit_at_width(s, f, q=0.95):
    """the q-quantile of the sum, after the posterior is shrunk about its own mean by f and the
    non-negative part kept -- f = 1 must reproduce the bounded chain's limit"""
    mu = float(s.mean())
    t = mu + (s - mu) / float(f)
    t = t[t >= 0.0]
    if t.size < 100:
        return float('nan')
    return float(np.quantile(t, q))


def gaussian_limit(mu, sd, q=0.95):
    """the same thing in closed form, as a check on the empirical rescaling"""
    lo = norm.cdf(-mu / sd)
    return float(mu + sd * norm.ppf(lo + q * (1.0 - lo)))


# ----------------------------------------------------------------- ACT, as this instrument sees it
def act_usable():
    """the banked ACT data, and the index of the bandpowers whose windows lie inside the reach"""
    z = np.load(ACT_NPZ, allow_pickle=True)
    wl = np.asarray(z['win_ell'], float)
    inside = (wl >= LMIN_INSTRUMENT) & (wl <= LMAX_INSTRUMENT)
    specs, keep, frac = {}, [], {}
    for j, name in enumerate(('TT', 'TE', 'EE')):
        w = np.asarray(z[f'win_{name}'], float)
        fr = w[inside].sum(axis=0) / w.sum(axis=0)
        frac[name] = fr
        specs[name] = dict(ell=np.asarray(z[f'ell_{name}'], float),
                           Dl=np.asarray(z[f'Dl_{name}'], float), win=w)
        keep.append(np.where(fr >= INSIDE)[0] + 45 * j)
    return z, wl, specs, frac, np.concatenate(keep)


def bin_act(wl, win, ls, Dl):
    """this instrument's spectrum through one of ACT's bandpower windows

    The window is tabulated per multipole on `wl`; the instrument's spectrum is on its own coarse
    axis.  A cubic spline carries it onto `wl` INSIDE the reach, and the weight outside the reach is
    zero for every bandpower kept, so nothing is extrapolated.
    """
    spl = CubicSpline(ls, Dl)
    m = (wl >= LMIN_INSTRUMENT) & (wl <= LMAX_INSTRUMENT)
    v = np.zeros(len(wl))
    v[m] = spl(wl[m])
    return win.T @ v


def instrument_spectra(arm, tag):
    """(ls, Dtt, Dte, Dee) at one banked grid point, with the three operators applied at `sum_ev`"""
    return M3._load(arm, tag)


def act_model(arm, tag, sum_ev, wl, specs, keep):
    """the 135-vector of ACT bandpowers this instrument predicts, operators applied at `sum_ev`"""
    ls, tt, te, ee = instrument_spectra(arm, tag)
    rtt, ree, cte = M3.operators_at(sum_ev)
    itt = np.interp(ls, M3._LS_R, rtt)
    iee = np.interp(ls, M3._LS_R, ree)
    icte = np.interp(ls, M3._LS_R, cte)
    out = []
    for name, D in (('TT', tt * itt), ('TE', te + icte * tt), ('EE', ee * iee)):
        out.append(bin_act(wl, specs[name]['win'], ls, D))
    return np.concatenate(out)[keep]


def main():
    print('\n  Ⓘ⑨ -- whether ACT DR6 CMB-only would close the control'"'"'s remainder\n')
    s, rec = control_posterior()
    mu, sd = float(s.mean()), float(s.std(ddof=1))
    rec_lim = float(rec[f'{ARM}_bounded']['upper95_mev'])
    rec_mcse = float(rec[f'{ARM}_bounded']['upper95_mcse_mev'])
    l1 = limit_at_width(s, 1.0) * 1e3
    g1 = gaussian_limit(mu * 1e3, sd * 1e3)
    print(f'  the control: unbounded Sum = {mu*1e3:+.3f} +/- {sd*1e3:.3f} meV; the bounded '
          f"chain's limit {rec_lim:.3f} +/- {rec_mcse:.3f} meV")
    print(f'    the same width truncated at zero gives {l1:.3f} meV empirically and {g1:.3f} meV in '
          f'closed form -- {abs(l1 - rec_lim)/rec_lim*100:.2f} and '
          f'{abs(g1 - rec_lim)/rec_lim*100:.2f} per cent from the chain'"'"'s own limit')

    # 1. the tightening required
    fun = lambda f: limit_at_width(s, f) * 1e3 - PUBLISHED_LIMIT_MEV
    if fun(1.0) < 0:
        raise SystemExit('the control is already inside the published limit -- Ⓘ⑨ does not arise')
    f_req = float(brentq(fun, 1.0, 400.0, xtol=1e-6))
    sd_at_f = sd / f_req
    if f_req <= 1.0:
        raise SystemExit('f_req <= 1')
    sd_req = sd / np.sqrt(f_req ** 2 - 1.0)
    print(f'\n  1. to reach the published {PUBLISHED_LIMIT_MEV} meV the width must shrink by '
          f'f = {f_req:.4f}, to {sd_at_f*1e3:.3f} meV')
    print(f'     => an INDEPENDENT dataset would have to deliver sigma(Sum) = {sd_req*1e3:.3f} meV '
          f'on its own')

    # 2. ACT's own Fisher, over-generously
    z, wl, specs, frac, keep = act_usable()
    nk = {n: int((frac[n] >= INSIDE).sum()) for n in ('TT', 'TE', 'EE')}
    print(f"\n  2. of ACT's 135 bandpowers, {len(keep)} lie wholly inside ell "
          f'{LMIN_INSTRUMENT:.0f}..{LMAX_INSTRUMENT:.0f} '
          f'(TT {nk["TT"]}, TE {nk["TE"]}, EE {nk["EE"]} of 45 each)')
    e_in = np.concatenate([specs[n]['ell'][frac[n] >= INSIDE] for n in ('TT', 'TE', 'EE')])
    print(f'     their effective multipoles run {e_in.min():.1f}..{e_in.max():.1f}; the '
          f'{135-len(keep)} dropped ones carry weight past the instrument'"'"'s reach')

    cov = np.asarray(z['cov'], float)[np.ix_(keep, keep)]
    Fd = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(len(keep)))
    Fd = 0.5 * (Fd + Fd.T)

    sums = M3.available_sums()
    tags = M3._SUM_TAGS
    base = np.array([act_model(ARM, tags[sv], sv, wl, specs, keep) for sv in sums])
    spl = CubicSpline(np.asarray(sums, float), base, axis=0)
    m0 = spl(mu)
    dsum = spl(mu, 1)

    der = {'MNU': dsum}
    for k in M3.KEYS4:
        mp = act_model(ARM, f'{k}p', mu, wl, specs, keep)
        mm = act_model(ARM, f'{k}m', mu, wl, specs, keep)
        der[k] = (mp - mm) / (2.0 * R.STEP[k])
    names5 = list(M3.KEYS4) + ['MNU']

    # the amplitude Planck's own fit puts on this instrument at the posterior centre
    ls, tt, te, ee = instrument_spectra(ARM, tags[min(sums, key=lambda v: abs(v - mu))])
    rtt, ree, cte = M3.operators_at(mu)
    itt = np.interp(ls, M3._LS_R, rtt)
    iee = np.interp(ls, M3._LS_R, ree)
    icte = np.interp(ls, M3._LS_R, cte)
    _c2, _n, A_planck, _nb = SC.chi2_of(ls, tt * itt, te + icte * tt, ee * iee)
    print(f"     the amplitude Planck's own 555-bin fit puts on this instrument: {A_planck:.6e}")

    out = {}
    for label, extra in (('amplitude_shared_with_planck', False), ('amplitude_free', True)):
        cols = [A_planck * der[k] for k in names5]
        if extra:
            cols = cols + [m0]
        J = np.array(cols)
        F = J @ Fd @ J.T
        ev = np.linalg.eigvalsh(F)
        C = np.linalg.inv(F)
        i = names5.index('MNU')
        sig_marg = float(np.sqrt(C[i, i]))
        sig_cond = float(1.0 / np.sqrt(F[i, i]))
        out[label] = dict(sigma_sum_marginal_mev=sig_marg * 1e3,
                          sigma_sum_conditional_mev=sig_cond * 1e3,
                          fisher_min_eig=float(ev.min()), n_params=int(J.shape[0]),
                          closes=bool(sig_marg <= sd_req))
        print(f'     [{label}] sigma_ACT(Sum) marginal = {sig_marg*1e3:.1f} meV '
              f'(conditional {sig_cond*1e3:.2f} meV); needed {sd_req*1e3:.3f} meV -- '
              f'{"CLOSES" if sig_marg <= sd_req else "DOES NOT CLOSE"}, short by a factor '
              f'{sig_marg/sd_req:.2f}')

    # 2b. the limit ACT would actually buy, combined in the Fisher sense
    for label, v in out.items():
        sa = v['sigma_sum_marginal_mev'] / 1e3
        sc = 1.0 / np.sqrt(1.0 / sd ** 2 + 1.0 / sa ** 2)
        fc = sd / sc
        lim_c = limit_at_width(s, fc) * 1e3
        v['combined_sd_mev'] = sc * 1e3
        v['combined_f'] = fc
        v['combined_limit_mev'] = lim_c
        print(f'     [{label}] combining it with the control gives sigma = {sc*1e3:.3f} meV '
              f'(f = {fc:.4f}) and a limit of {lim_c:.3f} meV,')
        print(f'        against {rec_lim:.3f} meV without it and {PUBLISHED_LIMIT_MEV} published '
              f'-- it buys {rec_lim - lim_c:.2f} meV of the {rec_lim - PUBLISHED_LIMIT_MEV:.2f} '
              f'meV remainder, {(rec_lim - lim_c)/(rec_lim - PUBLISHED_LIMIT_MEV)*100:.1f} per cent')

    # 3. what shrinking does to the sign half
    d0 = abs(mu * 1e3 - PUBLISHED_MEFF_MEV) / (sd * 1e3)
    df = abs(mu * 1e3 - PUBLISHED_MEFF_MEV) / (sd_at_f * 1e3)
    print(f'\n  3. the effective mass sits at {mu*1e3:+.3f} meV against the published '
          f'{PUBLISHED_MEFF_MEV:+.1f}: {d0:.2f} sigma now, {df:.2f} sigma at f = {f_req:.4f}')
    print('     shrinking a width moves a limit and leaves a centre where it is, so the half of '
          'Ⓖ⑦ that failed on SIGN is made worse by exactly the operation that would mend the '
          'other half.')

    closes = any(v['closes'] for v in out.values())
    decision = ('ADD' if closes else 'DO NOT ADD')
    print(f'\n  => Ⓘ⑨: {decision}.  ACT DR6 CMB-only is banked and was not added, because an '
          f'over-generous upper bound on\n     its marginal information about the sum is a factor '
          f'{min(v["sigma_sum_marginal_mev"] for v in out.values())/(sd_req*1e3):.1f} short of what '
          f'closing the limit would take,\n     and closing the limit by width alone would push the '
          f'effective mass from {d0:.2f} to {df:.2f} sigma from the published value.')

    rec_out = dict(arm=ARM, published_limit_mev=PUBLISHED_LIMIT_MEV,
                   published_meff_mev=PUBLISHED_MEFF_MEV,
                   control_sum_mean_mev=mu * 1e3, control_sum_sd_mev=sd * 1e3,
                   control_limit_mev=rec_lim, control_limit_mcse_mev=rec_mcse,
                   limit_from_rescaling_f1_mev=l1, limit_closed_form_f1_mev=g1,
                   f_required=f_req, sd_at_f_required_mev=sd_at_f * 1e3,
                   sigma_required_of_an_independent_set_mev=sd_req * 1e3,
                   act_bandpowers_total=135, act_bandpowers_usable=int(len(keep)),
                   act_usable_per_spectrum=nk, act_usable_ell_min=float(e_in.min()),
                   act_usable_ell_max=float(e_in.max()), inside_threshold=INSIDE,
                   amplitude_planck=A_planck, fisher=out,
                   meff_sigma_now=d0, meff_sigma_at_f=df,
                   nuisances_included=False, planck_act_sky_overlap_included=False,
                   decision=decision)
    with open(os.path.join(HERE, 'act_dr6_decision.json'), 'w') as fh:
        json.dump(rec_out, fh, indent=1, sort_keys=True)
    print('\n  wrote act_dr6_decision.json\n')


if __name__ == '__main__':
    main()
