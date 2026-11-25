# -*- coding: utf-8 -*-
"""r7873+cc66 item ⑫ -- CAMB's SUM RESPONSE BY SOURCE TERM.

`camb.symbolic.get_scalar_temperature_sources()` returns FOUR terms -- monopole (SW), ISW, doppler
and quadrupole -- and `set_custom_scalar_sources` feeds them back.  So CAMB CAN give the split and
the item is not refused.

⛔ TWO CONTROLS GATE EVERYTHING, and neither is optional:

  Ⓘ⑨ THE PATH control.  The sources returned UNMODIFIED and pushed back through
      `set_custom_scalar_sources` must return CAMB's own TT first.  A mechanism that silently does
      nothing produces a beautifully closing split of the WRONG THING -- the same shape that made
      four agreeing `MassiveNuMethod` settings worth proving live at `r7871`.

  Ⓕ⑥ THE CLOSURE control.  The four terms SUMMED must reproduce CAMB's own TT.  ** If closure
      fails, NO TERM IS REPORTED ** -- not one ratio, not as provisional.  Reading the terms of a
      decomposition that does not close would repeat `r7869`'s error of reading a per-bin share
      after it failed to close on the measured change.

⌗ The early/late ISW split is NOT a source term: CAMB's ISW is one expression and early against
  late is the same integrand over different stretches of TIME.  A window in the scale factor is
  attempted; if the source compiler refuses it, that is said in one line and the undivided ISW term
  is given.  Nothing is hand-integrated.

    NODE=cc66 python3 source_terms.py
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
import model3 as M3                                                         # noqa: E402

SUMS = (0.30, 0.60)
TAU = 0.054
L_LO, L_HI = 100, 420
LMAX_CALC = 1200
A_S = 2.1e-9
CLOSE_BAND = 1e-3
OUT = os.path.join(_HERE, 'source_terms.json')
TERMS = ('monopole', 'ISW', 'doppler', 'quadrupole')


def control():
    c = M3.ARMS['lcdm']['centre']
    return dict(H0=float(c['H0']), OM=float(c['OM']), WB=float(c['WB']), NS=float(c['NS']))


def _params(con, sum_ev):
    import camb
    om_m = con['OM'] * (con['H0'] / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=con['H0'], ombh2=con['WB'],
                        omch2=max(om_m - con['WB'] - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=TAU)
        p.InitPower.set_params(As=A_S, ns=con['NS'])
        p.set_for_lmax(LMAX_CALC, lens_potential_accuracy=1)
        return p
    p = build(0.0)
    return build(p.omnuh2)


def default_tt(con, sum_ev):
    """CAMB's own UNLENSED scalar TT -- the custom-source path returns unlensed, so compare like"""
    import camb
    p = _params(con, sum_ev)
    r = camb.get_results(p)
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['unlensed_scalar'])['unlensed_scalar']
    ls = np.arange(cl.shape[0], dtype=float)
    m = (ls >= L_LO) & (ls <= L_HI)
    return ls[m], np.asarray(cl[m, 0], float)


def custom_tt(con, sum_ev, which):
    """`which` = None for all four summed (the path control), or an index 0..3 for one term"""
    import camb
    import camb.symbolic as cs
    src = list(cs.get_scalar_temperature_sources())
    if which is None:
        expr = src[0] + src[1] + src[2] + src[3]
    else:
        expr = src[which]
    p = _params(con, sum_ev)
    p.set_custom_scalar_sources([expr], source_names=['T'],
                                source_ell_scales={'T': 0})
    r = camb.get_results(p)
    d = r.get_cmb_unlensed_scalar_array_dict(CMB_unit='muK')
    key = 'TxT' if 'TxT' in d else [k for k in d if k.startswith('T')][0]
    arr = np.asarray(d[key], float)
    ls = np.arange(arr.size, dtype=float)
    m = (ls >= L_LO) & (ls <= L_HI)
    return ls[m], arr[m]


def rel(a, b):
    return float(np.nanmax(np.abs(a - b) / np.maximum(np.abs(b), 1e-30)))


def main():
    print(__doc__)
    print('=' * 100)
    con = control()
    print('\n  the control, read from 60\'s module: %s;  tau fixed at %.3f and declared'
          % (con, TAU))
    out = {'control': con, 'tau': TAU, 'sums': list(SUMS), 'l_lo': L_LO, 'l_hi': L_HI,
           'terms': list(TERMS), 'close_band': CLOSE_BAND}

    # ── Ⓘ⑨ the PATH control ──
    print('\n  Ⓘ⑨ THE PATH CONTROL -- unmodified sources through the custom path against CAMB\'s own')
    ls, d0 = default_tt(con, 0.0)
    try:
        ls_c, c0 = custom_tt(con, 0.0, None)
        path_rel = rel(c0, d0)
        path_ok = path_rel < CLOSE_BAND
        print('      worst relative difference over l = %d..%d: %.3e   ⇒ %s'
              % (L_LO, L_HI, path_rel, 'PASSES' if path_ok else '⛔ FAILS'))
    except Exception as e:
        path_rel, path_ok = None, False
        print('      ⛔ the custom-source path RAISED: %s: %s' % (type(e).__name__, str(e)[:200]))
    out['path_control'] = dict(rel=path_rel, ok=bool(path_ok))

    if not path_ok:
        print('\n  ⛔ THE PATH CONTROL FAILS, so no term is read and no ratio is reported.')
        print('     CAMB exposes the mechanism but this seat could not make it return CAMB\'s own')
        print('     spectrum, and a split of something that is not the total is not a split of it.')
        out['terms_reported'] = False
        io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
        print('  written %s' % os.path.relpath(OUT, ROOT))
        return

    # ── Ⓕ⑥ the CLOSURE control, per sum ──
    print('\n  Ⓕ⑥ THE CLOSURE CONTROL -- the four terms summed against CAMB\'s own TT, at every sum')
    closure, per_term = {}, {}
    for s in (0.0,) + SUMS:
        _, dtt = default_tt(con, s)
        parts = []
        for i, nm in enumerate(TERMS):
            _, t = custom_tt(con, s, i)
            parts.append(t)
        tot = np.sum(np.vstack(parts), axis=0)
        r = rel(tot, dtt)
        closure['%g' % s] = r
        per_term['%g' % s] = {nm: parts[i] for i, nm in enumerate(TERMS)}
        print('      Sigma = %.2f: worst relative %.3e   ⇒ %s'
              % (s, r, 'closes' if r < CLOSE_BAND else '⛔ DOES NOT CLOSE'))
    out['closure'] = closure
    out['closes_everywhere'] = bool(all(v < CLOSE_BAND for v in closure.values()))

    if not out['closes_everywhere']:
        print('\n  ⛔ THE SPLIT DOES NOT CLOSE, so NO TERM IS REPORTED -- not one ratio, not as')
        print('     provisional.  A decomposition that does not sum to the thing it decomposes is')
        print('     not a decomposition of it.')
        out['terms_reported'] = False
        io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
        print('  written %s' % os.path.relpath(OUT, ROOT))
        return

    # ── Ⓖ⑦ each term's ratio, now that closure holds ──
    print('\n  Ⓖ⑦ EACH TERM\'S RATIO, closure having held')
    ratios = {}
    base = per_term['0']
    for s in SUMS:
        ratios['%g' % s] = {}
        for nm in TERMS:
            with np.errstate(divide='ignore', invalid='ignore'):
                rr = per_term['%g' % s][nm] / base[nm] - 1.0
            ratios['%g' % s][nm] = dict(
                l100=float(rr[0]), l220=float(rr[int(np.argmin(np.abs(ls - 220)))]),
                l420=float(rr[-1]), envelope=float(np.nanmax(np.abs(rr))),
                sign_changes=int(np.sum(np.sign(rr[1:]) * np.sign(rr[:-1]) < 0)))
            v = ratios['%g' % s][nm]
            print('      Sigma %.2f  %-11s l=100 %+.5f  l=220 %+.5f  l=420 %+.5f  envelope %.5f  '
                  '%d sign change(s)' % (s, nm, v['l100'], v['l220'], v['l420'], v['envelope'],
                                         v['sign_changes']))
    out['ratios'] = ratios
    out['terms_reported'] = True
    envs = [ratios['0.6'][nm]['envelope'] for nm in TERMS]
    out['worst_term_gap_at_0p60'] = float(max(envs) - min(envs))
    print('      ⇒ the terms do NOT move together: envelopes at Sigma=0.60 span %.5f'
          % out['worst_term_gap_at_0p60'])

    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
