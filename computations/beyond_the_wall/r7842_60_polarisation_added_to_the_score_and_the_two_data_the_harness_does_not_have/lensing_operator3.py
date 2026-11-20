"""r7842+60: THE LENSING OPERATOR FOR ALL THREE SPECTRA, FORMED AT EACH SUM.

On order r7841 (69) item ①.  r7838 formed `RATIO = C_l^lensed / C_l^unlensed` at each sum for TT
alone, because TT was all the harness scored.  TE and EE have their OWN lensing ratios -- lensing
smooths the E-mode acoustic peaks and the cross-spectrum differently from the temperature ones, and
TE's ratio is not even well defined where TE passes through zero -- so each spectrum gets its own,
formed at the same sums, in the same convention: the reference cosmology with the TOTAL
Omega_m h^2 held, so omega_cb falls by omega_nu.

** THE ONE PLACE A RATIO CANNOT BE USED, AND IT IS HANDLED RATHER THAN IGNORED. **  TE crosses zero
three times inside this instrument's reach, so C_l^lensed / C_l^unlensed is a ratio of two numbers
that both pass through zero at slightly displaced multipoles: it diverges, and the displacement is
physical rather than numerical.  So the TE operator is carried as an ADDITIVE correction -- which is
what the lensing literature does for TE, and for this reason.

** AND AN ADDITIVE CORRECTION HAS A UNIT PROBLEM THE MULTIPLICATIVE ONES DO NOT, SO IT IS CARRIED
AS A RATIO TO TT. **  The instrument's spectra have a FREE overall amplitude -- the score fits one
`A` -- so an additive term in CAMB's own micro-kelvin units cannot be added to them at all without
first fixing a scale between the two.  The correction is therefore stored as the DIMENSIONLESS

    c_TE(l, Sum) = [ C_TE^lensed - C_TE^unlensed ] / C_TT^unlensed

and applied in the model as `TE_instrument + c_TE * TT_instrument`, both in the INSTRUMENT's own
units, so the free amplitude cancels exactly and no external scale factor is needed.  `C_TT` is
positive everywhere, so nothing diverges.

Writes ratio_grid3.npz: the l axis, the grid in the sum, the TT and EE multiplicative ratios, and
the TE additive correction, with the reference columns.
rc=0 on success.  Run: python3 lensing_operator3.py            (numpy, camb)
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
import camb                                                                # noqa: E402

LMAX = 3000
H0, OMBH2, OM = 67.40, 0.02237, 0.3150
H = H0 / 100.0
OMH2 = OM * H ** 2
TAU, AS, NS = 0.054, 2.1e-9, 0.965
DIV = 93.14
GRID = np.round(np.arange(0.0, 0.6001, 0.03), 6)
OUT = os.path.join(HERE, 'ratio_grid3.npz')
OUTJ = os.path.join(HERE, 'lensing_operator3.json')


def spectra_at(sum_ev):
    """lensed and unlensed TT, EE and TE at the reference cosmology with the sum = sum_ev"""
    onuh2 = sum_ev / DIV
    omch2 = OMH2 - OMBH2 - onuh2
    kw = dict(H0=H0, ombh2=OMBH2, omch2=omch2, omk=0, tau=TAU, As=AS, ns=NS, lmax=LMAX)
    if sum_ev <= 0.0:
        p = camb.set_params(mnu=0.0, num_massive_neutrinos=0, **kw)
    else:
        p = camb.set_params(mnu=float(sum_ev), num_massive_neutrinos=3, **kw)
    cl = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=LMAX)
    # CAMB's column order is TT, EE, BB, TE
    le, un = cl['total'], cl['unlensed_scalar']
    return dict(tt_l=le[:, 0], tt_u=un[:, 0], ee_l=le[:, 1], ee_u=un[:, 1],
                te_l=le[:, 3], te_u=un[:, 3])


def main():
    rows = {}
    for s in GRID:
        rows[float(s)] = spectra_at(float(s))
        print(f'  operator at Sum = {float(s):.2f} eV: formed', flush=True)
    n = len(rows[0.0]['tt_l'])
    ls = np.arange(n, dtype=float)
    RTT = np.ones((len(GRID), n))
    REE = np.ones((len(GRID), n))
    DTE = np.zeros((len(GRID), n))
    for i, s in enumerate(GRID):
        r = rows[float(s)]
        m = r['tt_u'] > 0
        RTT[i][m] = r['tt_l'][m] / r['tt_u'][m]
        m = r['ee_u'] > 0
        REE[i][m] = r['ee_l'][m] / r['ee_u'][m]
        # ADDITIVE, because TE crosses zero -- and as a RATIO TO TT, so the
        # instrument's free amplitude cancels when it is applied
        _ttu = np.where(r['tt_u'] > 0, r['tt_u'], np.nan)
        DTE[i] = np.nan_to_num((r['te_l'] - r['te_u']) / _ttu, nan=0.0)
    rep = {}
    w = (ls >= 30) & (ls <= 2000)
    for i, s in enumerate(GRID):
        if abs(float(s) - 0.06) > 1e-9 and abs(float(s) - 0.12) > 1e-9 and float(s) != 0.6:
            continue
        dtt = RTT[i][w] / RTT[0][w] - 1.0
        dee = REE[i][w] / REE[0][w] - 1.0
        rep[f'{float(s):.2f}'] = dict(
            tt_max_pct=float(100.0 * np.max(np.abs(dtt))),
            tt_peak_l=int(ls[w][int(np.argmax(np.abs(dtt)))]),
            ee_max_pct=float(100.0 * np.max(np.abs(dee))),
            ee_peak_l=int(ls[w][int(np.argmax(np.abs(dee)))]))
        print('    Sum = %.2f eV: the TT operator moves %.4f per cent at l = %d, the EE operator '
              '%.4f per cent at l = %d'
              % (float(s), rep[f'{float(s):.2f}']['tt_max_pct'], rep[f'{float(s):.2f}']['tt_peak_l'],
                 rep[f'{float(s):.2f}']['ee_max_pct'], rep[f'{float(s):.2f}']['ee_peak_l']),
              flush=True)
    np.savez_compressed(OUT, ls=ls, grid=np.asarray(GRID, float), ratio_tt=RTT, ratio_ee=REE,
                        dte_over_tt=DTE, omh2=OMH2, ombh2=OMBH2, h0=H0, divisor=DIV)
    json.dump(dict(reference=dict(H0=H0, ombh2=OMBH2, omh2_total=OMH2, tau=TAU, As=AS, ns=NS,
                                  lmax=LMAX, divisor=DIV, model_lmax=1996),
                   te_form='additive and dimensionless: (C_TE_lensed - C_TE_unlensed) / C_TT_unlensed, '
                            'so the instrument\'s free amplitude cancels on application',
                   grid=[float(s) for s in GRID], response=rep), open(OUTJ, 'w'), indent=1)
    print(f'\n  wrote {os.path.relpath(OUT, HERE)} and {os.path.relpath(OUTJ, HERE)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
