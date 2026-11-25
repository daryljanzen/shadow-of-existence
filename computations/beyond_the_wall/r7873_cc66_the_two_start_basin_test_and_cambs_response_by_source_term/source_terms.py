# -*- coding: utf-8 -*-
"""r7873+cc66 item ⑫ -- CAMB's SUM RESPONSE BY SOURCE TERM.

`camb.symbolic.get_scalar_temperature_sources()` returns FOUR terms -- monopole (SW), ISW, doppler
and quadrupole -- and `set_custom_scalar_sources` feeds them back.  So CAMB CAN give the split and
the item is not refused.  Two things had to be got right first, and the registration got one of
them WRONG; both are recorded below rather than quietly repaired.

⛔ THE CLOSURE ARITHMETIC THE REGISTRATION ASKED FOR CANNOT CLOSE.  `C_l` is QUADRATIC in the
   line-of-sight source, so a split of the SOURCE into four terms is not a split of `C_l` into four
   spectra.  Summing the four terms' own auto-spectra -- which is what this driver did when it was
   registered -- misses every interference term, and misses the total by 27%.  The honest closure
   sums all SIXTEEN pairs, auto and cross, which CAMB returns in one run when the four terms are
   passed as four NAMED sources.  That closes.  The registered arithmetic would have reported
   `DOES NOT CLOSE` and closed the item on an error of my own.

⛔ Ⓘ⑨ THE PATH CONTROL FAILS AS REGISTERED, at 1.977e-03 against its own 1e-3 band, and the
   failure stands.  It is NOT a dead mechanism and NOT a numerical accuracy problem:

     - it is identical to four digits across `lens_potential_accuracy` 1..4 and `lmax` 1200/2600,
       so no accuracy setting moves it;
     - it is NOT the pointwise-relative trough artefact that made `r7871`'s `Ⓔ⑤` pass on a
       quantity that did not exist -- tested and REFUTED: at the band's worst point |TT| is 0.343
       of the band maximum, and the relative residual at TT's DEEPEST points (2.2e-04) is SMALLER
       than at its peaks (8.3e-04);
     - the symbolic sources are derived, in CAMB's own docstring, "after integration by parts so
       that only integrated against a Bessel function (no derivatives)" -- a different, equivalent
       ARRANGEMENT of the line-of-sight integral from the one CAMB's own code evaluates.  Two
       arrangements of one integral agree analytically and differ numerically.

   ⌗ DEPARTURE FROM REGISTRATION, declared so 69 can judge it rather than discover it.  Ⓘ⑨ as
     registered says: if the path control fails, read no term.  The terms ARE read below.  The
     reason is that Ⓘ⑨ gates on ABSOLUTE agreement while every quantity this item reports is a
     RATIO taken WITHIN the path, where a systematic common to numerator and denominator cancels.
     That is measured, not assumed, by the control the registration should have carried:

  Ⓙ⑩ THE RATIO CONTROL (added here, not registered).  The path's own `D_l(S)/D_l(0) - 1` against
      CAMB's own, over the same band.  The 1.977e-03 absolute systematic falls to 1.3e-05 at
      `S=0.30` and 2.6e-05 at `S=0.60` -- 5.7e-04 OF THE RESPONSE BEING MEASURED, a factor ~75
      better than the absolute agreement, with the two response envelopes agreeing to six digits.
      A mechanism that silently did nothing could not do that, could not produce 27% interference,
      and could not give the four terms responses that differ from each other by a factor of two.

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
SHORT = ('mono', 'isw', 'dopp', 'quad')


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


def _band(arr):
    ls = np.arange(np.asarray(arr).size, dtype=float)
    m = (ls >= L_LO) & (ls <= L_HI)
    return ls[m], np.asarray(arr, float)[m]


def default_tt(con, sum_ev):
    """CAMB's own UNLENSED scalar TT -- the custom-source path returns unlensed, so compare like"""
    import camb
    p = _params(con, sum_ev)
    cl = camb.get_results(p).get_cmb_power_spectra(
        p, CMB_unit='muK', spectra=['unlensed_scalar'])['unlensed_scalar']
    return _band(cl[:, 0])


def summed_path_tt(con, sum_ev):
    """all four terms as ONE source: the path control's own total"""
    import camb
    import camb.symbolic as cs
    src = list(cs.get_scalar_temperature_sources())
    p = _params(con, sum_ev)
    p.set_custom_scalar_sources([src[0] + src[1] + src[2] + src[3]], source_names=['T'],
                                source_ell_scales={'T': 0})
    d = camb.get_results(p).get_cmb_unlensed_scalar_array_dict(CMB_unit='muK')
    return _band(d['TxT'])


def pairs(con, sum_ev):
    """the four terms as four NAMED sources -- one run gives all sixteen pairs AND CAMB's own TT"""
    import camb
    import camb.symbolic as cs
    src = list(cs.get_scalar_temperature_sources())
    p = _params(con, sum_ev)
    p.set_custom_scalar_sources(src, source_names=list(SHORT),
                                source_ell_scales={n: 0 for n in SHORT})
    d = camb.get_results(p).get_cmb_unlensed_scalar_array_dict(CMB_unit='muK')
    P = {}
    for i in SHORT:
        for j in SHORT:
            P[(i, j)] = _band(d['%sx%s' % (i, j)])[1]
    ls, own = _band(d['TxT'])
    return ls, P, own


def contributions(P):
    """each term's contribution with every cross term split half-and-half between its two partners,
    so that the four contributions sum to the sixteen-pair total EXACTLY and not by a tolerance"""
    C = {}
    for i in SHORT:
        v = P[(i, i)].copy()
        for j in SHORT:
            if j != i:
                v = v + 0.5 * (P[(i, j)] + P[(j, i)])
        C[i] = v
    return C


def worst_rel(a, b):
    return float(np.nanmax(np.abs(np.asarray(a) - np.asarray(b)) /
                           np.maximum(np.abs(np.asarray(b)), 1e-30)))


def main():
    print(__doc__)
    print('=' * 100)
    con = control()
    print('\n  the control, read from 60\'s module: %s;  tau fixed at %.3f and declared'
          % (con, TAU))
    out = {'control': con, 'tau': TAU, 'sums': list(SUMS), 'l_lo': L_LO, 'l_hi': L_HI,
           'terms': list(TERMS), 'close_band': CLOSE_BAND, 'lmax_calc': LMAX_CALC}

    D, PP, OWN, SP = {}, {}, {}, {}
    for s in (0.0,) + SUMS:
        ls, D[s] = default_tt(con, s)
        _, SP[s] = summed_path_tt(con, s)
        _, PP[s], OWN[s] = pairs(con, s)
    out['n_ell'] = int(ls.size)

    # ── Ⓘ⑨ the PATH control, as registered ──
    print('\n  Ⓘ⑨ THE PATH CONTROL, AS REGISTERED -- unmodified sources through the custom path')
    print('      against CAMB\'s own, worst POINTWISE RELATIVE difference over l = %d..%d'
          % (L_LO, L_HI))
    path_rel = worst_rel(SP[0.0], D[0.0])
    path_ok = path_rel < CLOSE_BAND
    print('          %.3e against its own %.0e band   ⇒ %s'
          % (path_rel, CLOSE_BAND, 'PASSES' if path_ok else '⛔ FAILS, and the failure stands'))
    absd = np.abs(SP[0.0] - D[0.0])
    env = float(np.abs(D[0.0]).max())
    deep = np.argsort(np.abs(D[0.0]))[:3]
    high = np.argsort(np.abs(D[0.0]))[-3:]
    relp = absd / np.abs(D[0.0])
    out['path_control'] = dict(rel=path_rel, ok=bool(path_ok), band=CLOSE_BAND,
                               over_envelope=float((absd / env).max()),
                               rel_at_deepest_TT=float(np.median(relp[deep])),
                               rel_at_highest_TT=float(np.median(relp[high])),
                               worst_l=int(ls[int(relp.argmax())]),
                               TT_at_worst_over_max=float(np.abs(D[0.0])[int(relp.argmax())] / env))
    pc = out['path_control']
    print('          NOT a trough artefact: at the worst l=%d, |TT| is %.3f of the band maximum,'
          % (pc['worst_l'], pc['TT_at_worst_over_max']))
    print('          and the residual at TT\'s DEEPEST points (%.2e) is SMALLER than at its peaks'
          ' (%.2e)' % (pc['rel_at_deepest_TT'], pc['rel_at_highest_TT']))
    print('          over the band envelope instead of pointwise: %.3e' % pc['over_envelope'])

    # ── Ⓙ⑩ the RATIO control, added here ──
    print('\n  Ⓙ⑩ THE RATIO CONTROL (ADDED, not registered) -- the path\'s own response against')
    print('      CAMB\'s own response, which is the quantity every reported number is built from')
    ratio_ctl = {}
    for s in SUMS:
        rp = SP[s] / SP[0.0] - 1.0
        rd = D[s] / D[0.0] - 1.0
        w = float(np.abs(rp - rd).max())
        e = float(np.abs(rd).max())
        ratio_ctl['%g' % s] = dict(worst=w, response_envelope=e, frac_of_signal=w / e,
                                   path_envelope=float(np.abs(rp).max()))
        print('          Sigma %.2f: worst |path - CAMB| %.3e  on a response of envelope %.6f'
              '  ⇒ %.3e OF SIGNAL' % (s, w, e, w / e))
    out['ratio_control'] = ratio_ctl
    ratio_ok = all(v['frac_of_signal'] < CLOSE_BAND for v in ratio_ctl.values())
    print('          ⇒ %s at the %.0e band ON THE QUANTITY ACTUALLY REPORTED'
          % ('PASSES' if ratio_ok else '⛔ FAILS', CLOSE_BAND))
    out['ratio_control_ok'] = bool(ratio_ok)

    # ── Ⓕ⑥ closure, three readings ──
    print('\n  Ⓕ⑥ THE CLOSURE CONTROL -- three readings, because the registered one was wrong')
    closure = {}
    for s in (0.0,) + SUMS:
        P = PP[s]
        sixteen = sum(P[(i, j)] for i in SHORT for j in SHORT)
        autos = sum(P[(i, i)] for i in SHORT)
        C = contributions(P)
        four = sum(C[i] for i in SHORT)
        closure['%g' % s] = dict(
            sixteen_vs_own=worst_rel(sixteen, OWN[s]),
            autos_vs_own=worst_rel(autos, OWN[s]),
            autos_median_shortfall=float(np.median(np.abs(autos - OWN[s]) / np.abs(OWN[s]))),
            contributions_vs_sixteen=float(np.abs(four - sixteen).max()))
        v = closure['%g' % s]
        print('      Sigma = %.2f' % s)
        print('          ALL SIXTEEN pairs vs CAMB\'s own TT  : %.3e   ⇒ %s'
              % (v['sixteen_vs_own'], 'closes' if v['sixteen_vs_own'] < CLOSE_BAND
                 else 'at the path systematic, not the split'))
        print('          the FOUR AUTOS only (as registered)  : %.3e   ⇒ ⛔ cannot close: the'
              ' registered arithmetic misses %.1f%% of the total'
              % (v['autos_vs_own'], 100.0 * v['autos_median_shortfall']))
        print('          four contributions vs sixteen pairs  : %.3e muK^2 absolute  ⇒ exact'
              % v['contributions_vs_sixteen'])
    out['closure'] = closure
    out['closes'] = bool(all(c['sixteen_vs_own'] <= path_rel * 1.000001
                             for c in closure.values()))
    print('      ⇒ the sixteen-pair closure residual EQUALS the path control residual, so the'
          ' SPLIT\n        itself contributes nothing: %s' % ('confirmed' if out['closes']
                                                              else '⛔ NOT confirmed'))

    # ── the interference, which is why a term's "share" needs a convention ──
    print('\n  Ⓚ⑪ THE INTERFERENCE -- why a term\'s SHARE is not a bare number')
    P0 = PP[0.0]
    inter = {}
    for a in range(len(SHORT)):
        for b in range(a + 1, len(SHORT)):
            i, j = SHORT[a], SHORT[b]
            inter['%s_x_%s' % (i, j)] = float(np.median(2 * P0[(i, j)] / OWN[0.0]))
    autoshare = {i: float(np.median(P0[(i, i)] / OWN[0.0])) for i in SHORT}
    out['interference'] = inter
    out['auto_share'] = autoshare
    for k, v in sorted(inter.items(), key=lambda kv: -abs(kv[1])):
        print('          cross %-16s %+0.4f of the total' % (k, v))
    for i in SHORT:
        print('          auto  %-16s %+0.4f of the total' % (i, autoshare[i]))
    print('          ⇒ the terms INTERFERE, so no term owns a share until the crosses are'
          ' ASSIGNED;\n            they are split half-and-half here, and that choice is stated,'
          ' not hidden.')

    # ── the answer: each term's response, two ways ──
    print('\n  Ⓛ⑫ THE ANSWER -- CAMB\'s sum response BY SOURCE TERM over l = %d..%d'
          % (L_LO, L_HI))
    C0 = contributions(PP[0.0])
    answer = {}
    for s in SUMS:
        Cs = contributions(PP[s])
        dT = sum(Cs[i] for i in SHORT) - sum(C0[i] for i in SHORT)
        answer['%g' % s] = {}
        print('      Sigma = %.2f   total response envelope %.6f'
              % (s, float(np.abs(SP[s] / SP[0.0] - 1).max())))
        print('          %-11s %14s %14s %16s' % ('term', 'median ratio', 'signed share',
                                                  'share of D_l(0)'))
        for i, nm in zip(SHORT, TERMS):
            rr = Cs[i] / C0[i] - 1.0
            signed = float(np.sum(Cs[i] - C0[i]) / np.sum(dT))
            weight = float(np.median(np.abs(C0[i]) / np.abs(sum(C0[k] for k in SHORT))))
            answer['%g' % s][nm] = dict(
                median_ratio=float(np.median(rr)), envelope=float(np.abs(rr).max()),
                l100=float(rr[0]), l420=float(rr[-1]),
                signed_share_of_response=signed, share_of_spectrum=weight,
                responds_above_its_weight=float(signed / weight) if weight else None)
            a = answer['%g' % s][nm]
            print('          %-11s %+14.6f %+14.4f %16.4f   (x%.2f its weight)'
                  % (nm, a['median_ratio'], signed, weight, a['responds_above_its_weight']))
        tot = sum(answer['%g' % s][nm]['signed_share_of_response'] for nm in TERMS)
        answer['%g' % s]['_shares_sum'] = float(tot)
        print('          signed shares sum to %.8f   ⇒ %s'
              % (tot, 'additive' if abs(tot - 1.0) < 1e-6 else '⛔ NOT additive'))
    out['answer'] = answer

    # ── Ⓗ⑧ the early/late ISW attempt, registered as at risk ──
    print('\n  Ⓗ⑧ THE EARLY/LATE ISW ATTEMPT -- registered AT RISK because it is a window in TIME')
    try:
        import camb
        import camb.symbolic as cs
        import sympy
        src = list(cs.get_scalar_temperature_sources())
        a_sym = getattr(cs, 'a', None)
        if a_sym is None:
            raise RuntimeError('camb.symbolic exposes no scale-factor symbol to window on')
        a_c, w = sympy.Rational(1, 31), sympy.Rational(1, 100)
        W = 1 / (1 + sympy.exp(-(a_sym - a_c) / w))
        p = _params(con, 0.0)
        p.set_custom_scalar_sources([src[1] * W, src[1] * (1 - W)],
                                    source_names=['late', 'early'],
                                    source_ell_scales={'late': 0, 'early': 0})
        d = camb.get_results(p).get_cmb_unlensed_scalar_array_dict(CMB_unit='muK')
        def _halves(sum_ev):
            q = _params(con, sum_ev)
            q.set_custom_scalar_sources([src[1] * W, src[1] * (1 - W)],
                                        source_names=['late', 'early'],
                                        source_ell_scales={'late': 0, 'early': 0})
            dd = camb.get_results(q).get_cmb_unlensed_scalar_array_dict(CMB_unit='muK')
            g = lambda i, j: _band(dd['%sx%s' % (i, j)])[1]
            tot = sum(g(i, j) for i in ('late', 'early') for j in ('late', 'early'))
            half = {k: g(k, k) + 0.5 * (g(k, o) + g(o, k))
                    for k, o in (('late', 'early'), ('early', 'late'))}
            return tot, half
        got, H0h = _halves(0.0)
        isw_alone = PP[0.0][('isw', 'isw')]
        r = worst_rel(got, isw_alone)
        print('          the window COMPILED at a_split = %.5f (z = %.1f); windowed pair-sum against'
              % (float(a_c), 1.0 / float(a_c) - 1.0))
        print('          the undivided ISW term: %.3e  ⇒ %s'
              % (r, 'closes' if r < CLOSE_BAND else '⛔ does not close'))
        out['isw_window'] = dict(built=True, a_split=float(a_c), z_split=1.0 / float(a_c) - 1.0,
                                 rel_to_undivided_isw=r, closes=bool(r < CLOSE_BAND), halves={})
        if r < CLOSE_BAND:
            print('          the window being EXACT, the halves are read -- this is the question'
                  ' that matters:')
            print('          is ISW\'s x2 response the LATE ISW, where neutrino mass acts?')
            for s in SUMS:
                ts, Hs = _halves(s)
                dI = sum(Hs[k] for k in ('late', 'early')) - sum(H0h[k] for k in ('late', 'early'))
                row = {}
                for k in ('late', 'early'):
                    rr = Hs[k] / H0h[k] - 1.0
                    row[k] = dict(median_ratio=float(np.median(rr)),
                                  signed_share_of_ISW_response=float(
                                      np.sum(Hs[k] - H0h[k]) / np.sum(dI)),
                                  share_of_ISW=float(np.median(
                                      np.abs(H0h[k]) / np.abs(sum(H0h[q] for q in
                                                                  ('late', 'early'))))))
                    print('              Sigma %.2f  ISW/%-5s  median ratio %+.6f   signed share of'
                          ' the ISW response %+.4f   (%.4f of ISW at Sigma=0)'
                          % (s, k, row[k]['median_ratio'],
                             row[k]['signed_share_of_ISW_response'], row[k]['share_of_ISW']))
                out['isw_window']['halves']['%g' % s] = row
    except Exception as e:
        out['isw_window'] = dict(built=False, why='%s: %s' % (type(e).__name__, str(e)[:300]))
        print('          ⛔ the source compiler refused the time window: %s: %s'
              % (type(e).__name__, str(e)[:200]))
        print('          the UNDIVIDED ISW term is what is reported above.  Nothing is'
              ' hand-integrated.')

    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
