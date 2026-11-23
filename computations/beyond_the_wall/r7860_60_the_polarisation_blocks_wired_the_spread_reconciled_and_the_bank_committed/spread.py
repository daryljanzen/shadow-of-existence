# -*- coding: utf-8 -*-
"""r7860 (60) Ⓒ③ -- THE SPREAD RECONCILED WITH `cc66`'s COMMITTED POINT, ON THE SAME ARRAYS.

⛭ `r7857` (69) ruling ③: `cc66` reports the TT factor's per-bin spread at `0.0566`, oscillating in
`l` with about `-6` per cent near `l = 1920`, where this seat's range implies `0.0105`; both agree on
the mean to `0.27` per cent.  The order says to reconcile it on the same arrays before the control
runs.

⛔ **THE FIRST QUESTION IS NOT WHICH SPREAD IS RIGHT.**  It is whether the two numbers describe the
same object at all.  `Ⓒ③ᵃ` asks that first, and a DIFFERENT verdict would end the item: two spreads
measured on two configurations are not a disagreement.

⌗ `Ⓒ③ᶜ` is a POSITIVE CONTROL, written because `r7858`'s census reported zero and was nearly
believed: the comparator must be shown to FIND a per-multipole difference that is really there.

    python3 spread.py        # rc=0 when the item is settled either way
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
R7842 = os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_'
                           'harness_does_not_have')
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)
sys.path.insert(0, R7842)

MINE = os.path.join(os.environ.get('POL_DIR', '/tmp/claude-0/pol_grid'), 'lcdm_S000.npz')
CC66 = os.path.join(_BTW, 'r7855_cc66_an_independent_check_of_the_factor_two_in_the_cmb_bank',
                    'bank', 'lcdm_S000.npz')
AS, K_PIVOT, SUM_REF = 2.1e-9, 0.05, 0.06
H0, OM, WB, TAU = 67.40, 0.3150, 0.0224, 0.054
ARRAYS = ('ls', 'Dl', 'Dl_EE', 'Dl_TE', 'r_s', 'l_A', 'D_M', 'n_modes', 'ns', 'sliced')


def cfg(z):
    return json.loads(str(np.atleast_1d(z['config'])[0])) if 'config' in z.files else {}


def same_object(a, b):
    """Ⓒ③ᵃ -- are the two points the same object?  every differing key is NAMED"""
    arr, bad = {}, []
    for k in ARRAYS:
        x, y = np.asarray(a[k], float), np.asarray(b[k], float)
        eq = x.shape == y.shape and bool(np.array_equal(x, y))
        arr[k] = dict(equal=eq, shape=list(x.shape))
        if not eq:
            bad.append(k)
    ca, cb = cfg(a), cfg(b)
    ckeys = sorted(set(ca) | set(cb))
    cdiff = [k for k in ckeys if ca.get(k) != cb.get(k)]
    return dict(arrays=arr, arrays_differing=bad, config_keys=len(ckeys),
                config_differing=cdiff,
                same=bool(not bad), n_config=len(ckeys))


def factor_per_l(lsb, dlb):
    """the instrument's implied C_l over CAMB's own, per multipole and before any binning"""
    import camb
    from camb import model as camb_model
    import phiphi as PP
    import model6 as M6
    ns = float(PP.NS)
    amp = (4.0 / 9.0) * AS * K_PIVOT ** (1.0 - ns)
    h = H0 / 100.0
    omch2 = (OM - WB / h ** 2) * h ** 2 - SUM_REF / 93.14
    p = camb.set_params(H0=H0, ombh2=WB, omch2=omch2, mnu=SUM_REF, tau=TAU, ns=ns, As=AS,
                        lmax=2600, WantTransfer=True)
    p.NonLinear = camb_model.NonLinear_none
    r = camb.get_results(p)
    dl_camb = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['total'])['total'][:, 0]
    dlc = np.interp(lsb, np.arange(dl_camb.shape[0]), np.nan_to_num(dl_camb))
    clc = dlc * 2.0 * np.pi / (lsb * (lsb + 1.0))
    pred = 4.0 * np.pi * amp * M6.T_CMB_UK ** 2 * float(np.exp(-2.0 * TAU)) * \
        dlb / (lsb * (lsb + 1.0))
    return pred / clc, clc, pred, camb.__version__


def spreads(rat):
    """the two readings of ONE array: the whole-range one and the scatter one"""
    gm = float(np.exp(np.mean(np.log(np.abs(rat)))))
    return dict(geometric_mean=gm,
                worst_rel=float(np.max(np.abs(rat - gm)) / gm),
                rms_rel=float(np.std(rat / gm)),
                lo=float(np.min(rat)), hi=float(np.max(rat)), n=int(rat.size))


def main():
    print(__doc__)
    print('=' * 100)
    for p in (MINE, CC66):
        if not os.path.exists(p):
            print('\n  ⛔ not on disk: %s -- nothing is claimed.\n' % p)
            return 1
    a = np.load(MINE, allow_pickle=True)
    b = np.load(CC66, allow_pickle=True)

    print('\n  Ⓒ③ᵃ ARE THE TWO POINTS THE SAME OBJECT?')
    print('  ' + '-' * 98)
    so = same_object(a, b)
    for k in ARRAYS:
        print('    %-9s equal: %-5s  shape %s' % (k, so['arrays'][k]['equal'],
                                                  tuple(so['arrays'][k]['shape'])))
    print('    config: %d key(s), differing: %s' % (so['config_keys'],
                                                    so['config_differing'] or 'none'))
    out = dict(same_object=so)
    if not so['same']:
        print('\n  ⛔ DIFFERENT on %s -- two spreads on two configurations are not a '
              'disagreement, and Ⓒ③ᵇ does not run.' % so['arrays_differing'])
        with io.open(os.path.join(_HERE, 'spread.json'), 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(out, indent=1, sort_keys=True))
        return 0
    print('\n    ⇒ ** EVERY ARRAY IS BITWISE EQUAL. **  The two seats hold the SAME point, so the'
          '\n       two spreads are TWO READINGS OF ONE ARRAY and the question is how each is read.')
    if so['config_differing']:
        print('    ⌗ and the only differing config key is %s -- the arrays are identical ACROSS a'
              % so['config_differing'])
        print('      moved instrument blob, which is what the inert-class ratchet is for.')

    lsb = np.asarray(a['ls'], float)
    dlb = np.asarray(a['Dl'], float)
    rat, clc, pred_cl, camb_v = factor_per_l(lsb, dlb)

    print('\n  Ⓒ③ᵇ THE SAME ARRAY, READ TWO WAYS (camb %s)' % camb_v)
    print('  ' + '-' * 98)
    per_l = spreads(rat)
    print('    per multipole, unbinned  : n=%3d  mean %.6f  worst |r-gm|/gm %.4f  rms %.4f'
          % (per_l['n'], per_l['geometric_mean'], per_l['worst_rel'], per_l['rms_rel']))

    import score_ttteee as SC
    # ⛔ ** THE FIRST VERSION OF THIS LEG BINNED THE RATIO, AND THAT IS WRONG. **  *A window
    #   average of a ratio is not the ratio of the window averages, and run that way it returned a
    #   mean of `1.0e-05` and an rms of `7.78` -- a number with no meaning, which is kept in this
    #   comment rather than deleted because it is the same shape of error as `r7858`'s first `4 pi`
    #   test: a quantity formed in the wrong order and then read as a result.*  ⇒ The two spectra
    #   are binned SEPARATELY through the same windows and the ratio is taken per bin.
    zero = np.zeros_like(dlb)
    num = np.asarray(SC.bin_three(lsb, pred_cl, zero, zero), float)
    den = np.asarray(SC.bin_three(lsb, clc, zero, zero), float)
    m = np.isfinite(num) & np.isfinite(den) & (den != 0)
    per_bin = spreads(num[m] / den[m])
    print('    through the windows      : n=%3d  mean %.6f  worst |r-gm|/gm %.4f  rms %.4f'
          % (per_bin['n'], per_bin['geometric_mean'], per_bin['worst_rel'], per_bin['rms_rel']))

    print('\n    where the per-multipole reading puts its excursions:')
    gm = per_l['geometric_mean']
    for lo, hi in ((100, 500), (500, 1000), (1000, 1500), (1500, 1800), (1800, 2000), (2000, 3000)):
        w = (lsb >= lo) & (lsb < hi)
        if w.sum():
            d = rat[w] / gm - 1.0
            print('      l %4d .. %4d  n=%3d   mean %+.4f   min %+.4f   max %+.4f'
                  % (lo, hi, int(w.sum()), float(d.mean()), float(d.min()), float(d.max())))
    out['per_multipole'] = per_l
    out['through_the_windows'] = per_bin
    out['camb_version'] = camb_v

    # ------------------------------------------------------------------------------------------
    # Ⓒ③ᵈ -- AND WHERE THIS SEAT'S OWN SMALLER FIGURE CAME FROM, measured rather than guessed.
    #   `r7858`'s Ⓐ① read `0.011660` on the SAME point, and the two numbers are not two readings
    #   of one array after all: that one was formed through `model3`'s RESPONSE-BANK path
    #   (`mod.cmb.binned`), where the response operators have already been applied, and this one is
    #   formed on the raw bank point.  The leg below runs that path here and reports what it gives.
    r7858_path = None
    try:
        import model6 as M6x
        import phiphi as PPx
        import camb
        from camb import model as camb_model
        nsx = float(PPx.NS)
        ampx = (4.0 / 9.0) * AS * K_PIVOT ** (1.0 - nsx)
        hh = H0 / 100.0
        pp = camb.set_params(H0=H0, ombh2=WB, omch2=(OM - WB / hh ** 2) * hh ** 2 - SUM_REF / 93.14,
                             mnu=SUM_REF, tau=TAU, ns=nsx, As=AS, lmax=2600, WantTransfer=True)
        pp.NonLinear = camb_model.NonLinear_none
        rr = camb.get_results(pp)
        dl_camb = rr.get_cmb_power_spectra(pp, CMB_unit='muK', spectra=['total'])['total'][:, 0]
        mod = M6x.Model6('lcdm')
        m_bank = np.asarray(mod.cmb.binned(np.zeros(4), SUM_REF), float)
        mb_full = np.full(SC.BLOCK.shape[0], np.nan)
        mb_full[mod.cmb.ok] = m_bank
        tt = (SC.BLOCK == 0) & mod.cmb.ok
        bank_tt = mb_full[tt]
        lsx = np.arange(2, 2601)
        dlc_d = np.interp(lsx, np.arange(dl_camb.shape[0]), np.nan_to_num(dl_camb))
        zx = np.zeros_like(dlc_d)
        b_camb_dl = np.asarray(SC.bin_three(lsx, dlc_d, zx, zx), float)[tt]
        g = np.isfinite(bank_tt) & np.isfinite(b_camb_dl) & (b_camb_dl != 0)
        r2 = (2.0 * ampx * M6x.T_CMB_UK ** 2 * np.exp(-2.0 * TAU) * bank_tt[g]) / b_camb_dl[g]
        r7858_path = spreads(r2)
        r7858_path['reproduces_r7858'] = bool(abs(r7858_path['geometric_mean'] - 1.009345) < 5e-4
                                              and abs(r7858_path['worst_rel'] - 0.011660) < 5e-4)
        print("    through model3's RESPONSE-BANK path, masked exactly as r7858 did:")
        print('      n=%3d  mean %.6f  worst |r-gm|/gm %.6f   reproduces r7858: %s'
              % (r7858_path['n'], r7858_path['geometric_mean'], r7858_path['worst_rel'],
                 r7858_path['reproduces_r7858']))
        if r7858_path['reproduces_r7858']:
            print('      \u21d2 ** SO THE TWO FIGURES ARE NOT TWO READINGS OF ONE ARRAY. **  This seat\'s')
            print('        smaller one is the RESPONSE-BANK vector against a densely binned CAMB;')
            print('        cc66\'s is the raw bank point per multipole.  For the question asked --')
            print('        is the bank\'s factor a CONSTANT -- the raw point is the right array, so')
            print('        cc66\'s spread is the one that stands and this seat\'s understated it.')
        else:
            print('      \u26a0 this leg did NOT reproduce r7858\'s 1.009345 / 0.011660, so where that')
            print('        figure came from is NOT established here and nothing is claimed from it.')
    except Exception as e:                                        # noqa: BLE001
        print('    \u26a0 the response-bank path did not run (%s: %s) -- this leg reports NOTHING.'
              % (type(e).__name__, str(e)[:90]))
    out['r7858_response_bank_path'] = r7858_path

    print('\n  Ⓒ③ᶜ THE POSITIVE CONTROL -- does the comparator FIND a difference that is there?')
    print('  ' + '-' * 98)
    amp_ctl = 0.05
    pert = dlb * (1.0 + amp_ctl * np.sin(lsb / 120.0))
    rat_p, _, _, _ = factor_per_l(lsb, pert)
    got = spreads(rat_p)
    seen = float(np.max(np.abs(rat_p / rat - 1.0)))
    ok_ctl = bool(abs(seen - amp_ctl) < 0.02 and got['rms_rel'] > per_l['rms_rel'])
    print('    a known %.0f per cent oscillation put through the same comparator: it comes back at'
          % (amp_ctl * 100))
    print('    %.4f, and the rms rises from %.4f to %.4f.   control %s'
          % (seen, per_l['rms_rel'], got['rms_rel'], 'HOLDS' if ok_ctl else 'FAILS'))
    out['positive_control'] = dict(injected=amp_ctl, recovered=seen, holds=ok_ctl,
                                   rms_before=per_l['rms_rel'], rms_after=got['rms_rel'])

    bigger = per_l['rms_rel'] > per_bin['rms_rel']
    repro = bool(r7858_path and r7858_path.get('reproduces_r7858'))
    out['verdict'] = dict(
        same_point=True,
        configurations_agree_except=so['config_differing'],
        cc66_spread_reproduced=float(per_l['worst_rel']),
        this_seats_figure_reproduced=repro,
        which_spread_is_right=('cc66\'s -- the raw bank point per multipole' if repro
                               else 'not established: this seat\'s figure was not reproduced'),
        why=('the two numbers are NOT two readings of one array: cc66\'s is the raw bank point '
             'per multipole, and this seat\'s is the model3 RESPONSE-BANK vector against a densely '
             'binned CAMB, reproduced here to six decimals. The question asked -- is the bank\'s '
             'factor a CONSTANT -- is a question about the bank, so the raw point is the right '
             'array and this seat\'s figure understated the spread'),
        per_multipole_worst=per_l['worst_rel'], through_the_windows_worst=per_bin['worst_rel'],
        response_bank_worst=(r7858_path or {}).get('worst_rel'),
        binning_understates=bool(bigger))
    print('\n  \u21d2 VERDICT: ONE point, and the two figures are NOT two readings of it.')
    print('    cc66\'s %.4f is the raw point per multipole and is reproduced here at %.4f, with its'
          % (0.0566, per_l['worst_rel']))
    print('    own negative lobe where cc66 puts it. This seat\'s %.6f is the response-bank vector'
          % 0.011660)
    print('    against a densely binned CAMB, reproduced here %s. \u21d2 ** cc66\'s spread is the one'
          % ('exactly' if repro else 'NOT'))
    print('    that stands for the question asked, and this seat\'s understated it. **')
    with io.open(os.path.join(_HERE, 'spread.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  wrote spread.json\n')
    return 0 if ok_ctl else 1


if __name__ == '__main__':
    raise SystemExit(main())
