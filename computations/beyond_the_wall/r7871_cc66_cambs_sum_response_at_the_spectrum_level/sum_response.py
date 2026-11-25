# -*- coding: utf-8 -*-
"""r7871+cc66 item ⑩ -- CAMB's SUM RESPONSE AT THE SPECTRUM LEVEL, AT FIXED OTHER PARAMETERS.

`D_l(Sigma)/D_l(0) - 1` for TT, TE and EE, UNBINNED, on 60's multipole range, at 60's own control
cosmology, from CAMB.

⌗ 60's control is READ from their module at run time, not retyped: `model3.ARMS['lcdm']['centre']`.
  tau is NOT among the instrument's four parameters -- 60 profile it -- so it is fixed here and
  DECLARED, and Ⓒ③ measures whether the deliverable turns on that choice.

⚠ TE is a CROSS spectrum and changes sign, so a RATIO of TE is not a ratio of a positive quantity:
  near a zero crossing it diverges.  Both are reported -- the plain ratio and, for TE only, the
  difference normalised by the TT envelope -- and the arm that reads TE says which it is reading.

    NODE=cc66 python3 sum_response.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(_BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
sys.path.insert(0, os.path.join(_BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_'
                                      'the_damping_tails_share_of_the_gap'))
import tail_share as TS                                                     # noqa: E402,F401
import score_ttteee as SC                                                   # noqa: E402,F401
import model3 as M3                                                         # noqa: E402

SUMS = (0.06, 0.30, 0.60)
TAU = 0.054                      # DECLARED: 60 profile tau, so there is no control tau to read
TAU_PROBE = (0.044, 0.064)       # Ⓒ③
ACCS = (1, 3)                    # Ⓑ②
METHODS = ('Nu_best', 'Nu_int', 'Nu_trunc', 'Nu_approx')   # Ⓖ⑦
LMAX_CALC = 2600
L_LO, L_HI = 100, 1996           # 60's covered range, as r7869 measured it
A_S = 2.1e-9
OUT = os.path.join(_HERE, 'sum_response.json')
_cache = {}


def control():
    """60's own control, read from their module rather than retyped here"""
    c = M3.ARMS['lcdm']['centre']
    return dict(H0=float(c['H0']), OM=float(c['OM']), WB=float(c['WB']), NS=float(c['NS']))


def spectra(h0, om, wb, ns, tau, sum_ev, acc, method):
    key = (h0, om, wb, ns, tau, round(sum_ev, 10), acc, method)   # ⛔ the FULL tuple (r7867)
    if key in _cache:
        return _cache[key]
    import camb
    om_m = om * (h0 / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.MassiveNuMethod = method
        p.set_cosmology(H0=h0, ombh2=wb, omch2=max(om_m - wb - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=tau)
        p.InitPower.set_params(As=A_S, ns=ns)
        p.set_for_lmax(LMAX_CALC, lens_potential_accuracy=acc)
        return p
    p = build(0.0)
    p = build(p.omnuh2)
    r = camb.get_results(p)
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['lensed_scalar'])['lensed_scalar']
    ls = np.arange(cl.shape[0], dtype=float)
    m = (ls >= L_LO) & (ls <= L_HI)
    _cache[key] = dict(ls=ls[m], TT=cl[m, 0], EE=cl[m, 1], TE=cl[m, 3])
    return _cache[key]


def ratios(con, tau, acc, method):
    base = spectra(con['H0'], con['OM'], con['WB'], con['NS'], tau, 0.0, acc, method)
    out = {}
    for s in SUMS:
        here = spectra(con['H0'], con['OM'], con['WB'], con['NS'], tau, s, acc, method)
        r = {}
        for sp in ('TT', 'EE', 'TE'):
            with np.errstate(divide='ignore', invalid='ignore'):
                r[sp] = here[sp] / base[sp] - 1.0
        # TE read the other way too: difference over the TT envelope, finite through TE's zeros
        r['TE_over_TT'] = (here['TE'] - base['TE']) / np.abs(base['TT'])
        out['%g' % s] = r
    return base['ls'], out


def band_summary(ls, r):
    """a few reported reads, so the JSON is not only an array"""
    def at(sp, l):
        i = int(np.argmin(np.abs(ls - l)))
        return float(r[sp][i])
    return {sp: {'l%d' % l: at(sp, l) for l in (100, 220, 500, 1000, 1500, 1996)}
            for sp in ('TT', 'EE', 'TE', 'TE_over_TT')}


def main():
    print(__doc__)
    print('=' * 100)
    con = control()
    print('\n  Ⓐ① 60\'s CONTROL, read from their own module at run time:')
    print('      %s' % con)
    print('      tau FIXED HERE at %.3f and DECLARED -- 60 profile tau over their own range, so '
          'there is no control tau to read.' % TAU)
    out = {'control': con, 'tau': TAU, 'sums': list(SUMS), 'l_lo': L_LO, 'l_hi': L_HI,
           'lmax_calc': LMAX_CALC, 'A_s': A_S, 'methods_available': list(METHODS)}

    # ── the deliverable: standard treatment, acc=1 ──
    ls, r1 = ratios(con, TAU, 1, 'Nu_best')
    out['n_multipoles'] = int(ls.size)
    out['standard'] = {k: band_summary(ls, v) for k, v in r1.items()}
    print('\n  ⑩ THE DELIVERABLE -- D_l(Sigma)/D_l(0) - 1, unbinned on %d multipole(s) %d..%d'
          % (ls.size, int(ls[0]), int(ls[-1])))
    for s in SUMS:
        v = r1['%g' % s]
        print('      Sigma = %.2f eV' % s)
        for sp in ('TT', 'EE'):
            print('        %-3s  l=100 %+.5f   l=500 %+.5f   l=1000 %+.5f   l=1500 %+.5f   '
                  'l=1996 %+.5f' % ((sp,) + tuple(out['standard']['%g' % s][sp]['l%d' % l]
                                                  for l in (100, 500, 1000, 1500, 1996))))
        print('        TE (over |TT|)  l=100 %+.5f   l=500 %+.5f   l=1000 %+.5f   l=1500 %+.5f'
              % tuple(out['standard']['%g' % s]['TE_over_TT']['l%d' % l]
                      for l in (100, 500, 1000, 1500)))

    # ── Ⓑ② is the ratio readable: does it move with CAMB accuracy? ──
    _, r3 = ratios(con, TAU, 3, 'Nu_best')
    worst_acc = 0.0
    for s in SUMS:
        for sp in ('TT', 'EE'):
            d = float(np.nanmax(np.abs(r1['%g' % s][sp] - r3['%g' % s][sp])))
            worst_acc = max(worst_acc, d)
    out['accuracy_move_worst'] = worst_acc
    print('\n  Ⓑ② READABILITY -- worst move in any TT/EE ratio when lens_potential_accuracy 1 -> 3:'
          '  %.3e   (band: < 1e-3)' % worst_acc)

    # ── Ⓒ③ does it turn on my tau? ──
    worst_tau = 0.0
    for t in TAU_PROBE:
        _, rt = ratios(con, t, 1, 'Nu_best')
        for s in SUMS:
            for sp in ('TT', 'EE'):
                d = float(np.nanmax(np.abs(r1['%g' % s][sp] - rt['%g' % s][sp])))
                worst_tau = max(worst_tau, d)
    out['tau_move_worst'] = worst_tau
    print('  Ⓒ③ tau-INSENSITIVITY -- worst move over tau = %s:  %.3e   (band: < 5e-3)'
          % (list(TAU_PROBE), worst_tau))

    # ── Ⓓ④ Ⓔ⑤ Ⓕ⑥ sign, growth in Sigma, growth in l, and the TT-EE disagreement ──
    sign_ok, mono_ok = True, True
    for sp in ('TT', 'EE'):
        for s in SUMS:
            if not np.all(r1['%g' % s][sp] < 0):
                sign_ok = False
        for a, b in zip(SUMS, SUMS[1:]):
            if not np.all(np.abs(r1['%g' % b][sp]) > np.abs(r1['%g' % a][sp])):
                mono_ok = False
    tt_l = out['standard']['0.6']['TT']
    tt_grows = tt_l['l1996'] < tt_l['l100']
    tt_ee_gap = float(np.nanmax(np.abs(r1['0.6']['TT'][ls > 1000] - r1['0.6']['EE'][ls > 1000])))
    out.update(sign_all_negative=bool(sign_ok), monotone_in_sum=bool(mono_ok),
               tt_suppression_grows_with_l=bool(tt_grows), tt_ee_gap_at_0p60=tt_ee_gap)
    print('  Ⓓ④ every TT/EE ratio negative: %s;  |ratio| monotone in Sigma: %s' % (sign_ok, mono_ok))
    print('  Ⓔ⑤ TT suppression deeper at l=1996 than l=100 at Sigma=0.60: %s  (%+.5f vs %+.5f)'
          % (tt_grows, tt_l['l1996'], tt_l['l100']))
    print('  Ⓕ⑥ worst TT-EE disagreement above l=1000 at Sigma=0.60: %.5f' % tt_ee_gap)

    # ── Ⓖ⑦ the four treatments: a BOUND, not the instrument's treatment ──
    print('\n  Ⓖ⑦ THE PERTURBATION KNOB -- CAMB exposes MassiveNuMethod, and these are ITS OWN four')
    meth = {}
    for m in METHODS:
        _, rm = ratios(con, TAU, 1, m)
        meth[m] = band_summary(ls, rm)['TT']
        print('      %-10s TT at Sigma=0.60:  l=500 %+.5f  l=1000 %+.5f  l=1996 %+.5f'
              % (m, meth[m]['l500'], meth[m]['l1000'], meth[m]['l1996']))
    spread = 0.0
    for s in SUMS:
        for sp in ('TT', 'EE'):
            arrs = []
            for m in METHODS:
                _, rm = ratios(con, TAU, 1, m)
                arrs.append(rm['%g' % s][sp])
            A = np.vstack(arrs)
            spread = max(spread, float(np.nanmax(A.max(axis=0) - A.min(axis=0))))
    out['method_spread_worst'] = spread
    out['method_TT_at_0p60'] = meth
    out['bound_is_useful'] = bool(spread < tt_ee_gap)
    print('      ⇒ worst spread across the four treatments, any sum, TT or EE: %.3e' % spread)
    print('      ⇒ against the TT-EE disagreement %.5f  ⇒ the bound is %s'
          % (tt_ee_gap, 'USEFUL' if spread < tt_ee_gap else '⛔ USELESS, and said so'))

    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
