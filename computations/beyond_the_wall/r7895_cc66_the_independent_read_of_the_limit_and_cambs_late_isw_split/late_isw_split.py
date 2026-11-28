"""⑱③ — CAMB's late-ISW split: TT at ℓ=100–207, with and without the late-time ISW.

Order `r7895` (69) item ⑱③, at `Σ = 0, 0.06, 0.30, 0.60` eV on the reference's parameters.
`PREDICTION.md` Ⓔ⑤ registered, before this file existed, that the split would be computed from
**CAMB's own source terms and not by a hand-subtraction**, and that an inert leg pair would be
reported as inert rather than as a measurement.

** HOW THE SPLIT IS TAKEN. **  `camb.symbolic.get_scalar_temperature_sources()` returns the
temperature source in four terms: ⒜ `(Delta_g/4 + 2φ + η/2Kf_1)·visibility` (Sachs–Wolfe, at
recombination), ⒝ `2·exptau·dφ/dt` (**the ISW**, after recombination), ⒞ the Doppler term, ⒟ the
polarisation quadrupole.  Term ⒝ is the TOTAL ISW, early and late together, so dropping it does not
answer ⑱③.  The late part is isolated by multiplying ⒝ by a window in the scale factor that is `1`
early and `0` late — the source terms are CAMB's, the window only chooses WHEN term ⒝ contributes.

⛔ TWO CONTROLS, BOTH IN THE SAME RUN AS THE MEASUREMENT, because a small number at ℓ=100–207 is
worthless if the window never reached the compiled source:
  Ⓐ a leg whose window is `1` everywhere MUST equal the full leg.  *The first window written here
    was a sigmoid in `z`; `cs.z` is `z(t)` and the `exp` overflowed once compiled, and that leg came
    back indistinguishable from dropping the ISW entirely — a broken window reading as a measured
    split.  It was caught by this control, which is why the control is in the file.*
  Ⓑ the same no-late-ISW leg at ℓ=2–30, where the late ISW does live, MUST differ from full.

⌗ SCOPE.  The custom-source machinery returns UNLENSED scalar spectra, so this split is on unlensed
TT.  Lensing mixes multipoles and is not part of the source decomposition; the figure is not offered
as a lensed one.
"""
import importlib.util
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
R7871 = os.path.join(BTW, 'r7871_cc66_cambs_sum_response_at_the_spectrum_level')

SUMS = (0.0, 0.06, 0.30, 0.60)
L_LO, L_HI = 100, 207            #: the order's range
C_LO, C_HI = 2, 30               #: control Ⓑ: where the late ISW lives
ZCUT, NPOW = 30.0, 8             #: the early/late boundary, stated so 60 can match it
LMAX = 320
A_S = 2.1e-9
TAU = 0.054


def _reference():
    """60's own control parameters, imported from r7871 rather than retyped"""
    spec = importlib.util.spec_from_file_location(
        'cc66_sumresp', os.path.join(R7871, 'sum_response.py'))
    m = importlib.util.module_from_spec(spec)
    sys.modules['cc66_sumresp'] = m
    spec.loader.exec_module(m)
    return m.control()


def legs(h0, om, wb, ns, sum_ev):
    import camb
    import camb.symbolic as cs
    import sympy

    mono, isw, dopp, quad = cs.get_scalar_temperature_sources()
    full = mono + isw + dopp + quad
    a = cs.a
    acut = 1.0 / (1.0 + ZCUT)
    early = 1 / (1 + (a / acut) ** NPOW)        #: 1 early, 0 late -- polynomial, cannot overflow
    keepall = 1 / (1 + (a / 1.0e6) ** NPOW)     #: ~1 everywhere -- control Ⓐ
    exprs = [full, mono + dopp + quad, mono + dopp + quad + isw * early,
             mono + dopp + quad + isw * keepall]
    names = ['T', 'Tno', 'Tnl', 'Tkeep']

    om_m = om * (h0 / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=h0, ombh2=wb, omch2=max(om_m - wb - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=TAU)
        p.InitPower.set_params(As=A_S, ns=ns)
        p.set_for_lmax(LMAX, lens_potential_accuracy=0)
        return p
    p = build(0.0)
    p = build(p.omnuh2)                          #: r7871's two-pass build, so omnuh2 is the run's own
    p.set_custom_scalar_sources(exprs, source_names=names,
                                source_ell_scales={n: 0 for n in names})
    r = camb.get_results(p)
    d = r.get_cmb_unlensed_scalar_array_dict(lmax=LMAX, CMB_unit='muK', raw_cl=True)
    return {n: np.asarray(d['%sx%s' % (n, n)], float) for n in names}


def worst_rel(x, y, ls, lo, hi):
    m = (ls >= lo) & (ls <= hi)
    return float((np.abs(x[m] - y[m]) / np.abs(y[m])).max())


def main():
    ref = _reference()
    out = {'reference': ref, 'sums_eV': list(SUMS), 'band': [L_LO, L_HI],
           'control_band': [C_LO, C_HI], 'z_cut': ZCUT, 'window_power': NPOW,
           'window': '1/(1+(a/a_cut)^%d), 1 early and 0 late' % NPOW,
           'spectra': 'UNLENSED scalar TT from CAMB custom scalar sources',
           'terms': 'camb.symbolic.get_scalar_temperature_sources(): SW, ISW, Doppler, quadrupole',
           'per_sum': {}}

    for s in SUMS:
        L = legs(ref['H0'], ref['OM'], ref['WB'], ref['NS'], s)
        ls = np.arange(len(L['T']))
        row = {
            'control_A_window1_vs_full_in_band': worst_rel(L['Tkeep'], L['T'], ls, L_LO, L_HI),
            'no_total_isw_vs_full_in_band': worst_rel(L['Tno'], L['T'], ls, L_LO, L_HI),
            'no_late_isw_vs_full_in_band': worst_rel(L['Tnl'], L['T'], ls, L_LO, L_HI),
            'control_B_no_late_isw_vs_full_low_l': worst_rel(L['Tnl'], L['T'], ls, C_LO, C_HI),
            'no_total_isw_vs_full_low_l': worst_rel(L['Tno'], L['T'], ls, C_LO, C_HI),
        }
        row['control_A_holds'] = bool(row['control_A_window1_vs_full_in_band'] < 1e-10)
        row['control_B_holds'] = bool(row['control_B_no_late_isw_vs_full_low_l'] > 1e-3)
        row['late_over_total_in_band'] = (row['no_late_isw_vs_full_in_band']
                                          / row['no_total_isw_vs_full_in_band'])
        out['per_sum']['%.2f' % s] = row

    rows = out['per_sum']
    out['all_control_A_hold'] = all(r['control_A_holds'] for r in rows.values())
    out['all_control_B_hold'] = all(r['control_B_holds'] for r in rows.values())
    out['worst_late_in_band'] = max(r['no_late_isw_vs_full_in_band'] for r in rows.values())
    out['inert'] = not out['all_control_B_hold']

    json.dump(out, open(os.path.join(HERE, 'late_isw_split.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)

    print('\n  ⑱③ CAMB\'s LATE-ISW SPLIT, TT, UNLENSED, ON THE REFERENCE\'S PARAMETERS')
    print('     reference: H0=%(H0)s OM=%(OM)s WB=%(WB)s NS=%(NS)s' % ref)
    print('     early/late boundary z_cut = %.0f, window 1/(1+(a/a_cut)^%d)\n' % (ZCUT, NPOW))
    print('     %-6s %-14s %-14s %-14s %-14s' % ('Sigma', 'ctrl-A w==1', 'no TOTAL isw',
                                                 'no LATE isw', 'ctrl-B low-l'))
    for k in sorted(rows):
        r = rows[k]
        print('     %-6s %-14.3e %-14.6e %-14.6e %-14.6e' % (
            k, r['control_A_window1_vs_full_in_band'], r['no_total_isw_vs_full_in_band'],
            r['no_late_isw_vs_full_in_band'], r['control_B_no_late_isw_vs_full_low_l']))
    print()
    print('     control Ⓐ (window==1 equals full) holds at every sum: %s' % out['all_control_A_hold'])
    print('     control Ⓑ (the window acts at l=2-30)  holds at every sum: %s' % out['all_control_B_hold'])
    print('     worst late-ISW imprint in %d-%d: %.6e' % (L_LO, L_HI, out['worst_late_in_band']))
    print('     split inert? %s\n' % out['inert'])
    assert out['all_control_A_hold'], 'control A failed: the window did not reach the source'
    assert out['all_control_B_hold'], 'control B failed: the window is inert where the late ISW lives'


if __name__ == '__main__':
    main()
