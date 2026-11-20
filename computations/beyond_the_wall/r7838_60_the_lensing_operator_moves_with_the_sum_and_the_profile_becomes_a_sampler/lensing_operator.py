"""r7838+60: THE LENSING OPERATOR THAT MOVES WITH THE SUM.

On order r7833 (69), item ①.  `r7749_70_leafgeom_refit/refit.py` forms

    RATIO = C_l^{lensed} / C_l^{unlensed}

ONCE, from a CAMB cosmology with `mnu = 0.06` hardcoded, and applies that one operator to every
spectrum at every trial point.  r7836 measured what that omits: the operator itself moves by 0.372
per cent at Sum = 0.06 eV and 0.768 at 0.12, peaking near l ~ 1980 -- the same order as the
omega_cb lever the harness kept, so the harness was confidently wrong rather than loose.

This file forms RATIO(Sum) instead, on a grid in the sum, at the reference cosmology, HOLDING THE
TOTAL Omega_m h^2 FIXED so that omega_cb falls by omega_nu.  That is the convention the fit uses
and the one ACOUSTIC_two_arm.py carries since r7836: the distances and the dark energy see the
total, the clustering matter the perturbations see is omega_cb = Omega_m h^2 - omega_nu.

  ** The borrowed harness's own cosmology is the reference, with ONE difference stated here: it
     passes omch2 = Om*h^2 - ombh2 WITH mnu=0.06 beside it, so its total is larger than Om*h^2 by
     omega_nu.  This file subtracts omega_nu, so that Sum is the only thing moving. **

Writes ratio_grid.npz: the l axis, the grid in the sum, RATIO on it, and the reference columns.
rc=0 on success.  Run: python3 lensing_operator.py            (numpy, camb)
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
import camb                                                                # noqa: E402

LMAX = 3000
H0 = 67.40
H = H0 / 100.0
OMBH2 = 0.02237
OM = 0.3150
OMH2 = OM * H ** 2                    # the TOTAL matter density, held fixed as the sum moves
TAU, AS, NS = 0.054, 2.1e-9, 0.965
NU_DIVISOR = 93.14                    # eV per unit omega_nu, the standard conversion
GRID = np.round(np.arange(0.0, 0.3001, 0.03), 6)
OUT = os.path.join(HERE, 'ratio_grid.npz')
OUTJ = os.path.join(HERE, 'lensing_operator.json')


def ratio_at(sum_ev):
    """C_l^lensed / C_l^unlensed at the reference cosmology with the sum = sum_ev, total omega_m held."""
    onuh2 = sum_ev / NU_DIVISOR
    omch2 = OMH2 - OMBH2 - onuh2
    if sum_ev <= 0.0:
        p = camb.set_params(H0=H0, ombh2=OMBH2, omch2=omch2, mnu=0.0, num_massive_neutrinos=0,
                            omk=0, tau=TAU, As=AS, ns=NS, lmax=LMAX)
    else:
        p = camb.set_params(H0=H0, ombh2=OMBH2, omch2=omch2, mnu=float(sum_ev),
                            num_massive_neutrinos=3, omk=0, tau=TAU, As=AS, ns=NS, lmax=LMAX)
    cl = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=LMAX)
    le, un = cl['total'][:, 0], cl['unlensed_scalar'][:, 0]
    r = np.ones_like(le)
    r[un > 0] = le[un > 0] / un[un > 0]
    return r


def main():
    rows = {}
    for s in GRID:
        rows[float(s)] = ratio_at(float(s))
        print(f'  RATIO at Sum = {float(s):.2f} eV: formed', flush=True)
    ls = np.arange(len(rows[0.0]), dtype=float)
    R = np.array([rows[float(s)] for s in GRID])
    r0 = rows[0.0]
    ok = (ls >= 2) & (ls <= LMAX) & (r0 > 0)
    rep = {}
    for s in GRID:
        d = np.zeros_like(r0)
        d[ok] = rows[float(s)][ok] / r0[ok] - 1.0
        j = int(np.argmax(np.abs(d)))
        rep[f'{float(s):.2f}'] = dict(max_abs_pct=float(100.0 * abs(d[j])), peak_l=int(ls[j]),
                                      signed_pct=float(100.0 * d[j]))
        print(f'    Sum = {float(s):.2f} eV: the operator moves by {100.0 * abs(d[j]):.4f} per cent, '
              f'peaking at l = {int(ls[j])}', flush=True)
    np.savez_compressed(OUT, ls=ls, grid=np.asarray(GRID, float), ratio=R,
                        omh2=OMH2, ombh2=OMBH2, h0=H0, divisor=NU_DIVISOR)
    json.dump(dict(reference=dict(H0=H0, ombh2=OMBH2, omh2_total=OMH2, tau=TAU, As=AS, ns=NS,
                                  lmax=LMAX, divisor=NU_DIVISOR),
                   grid=[float(s) for s in GRID], response=rep), open(OUTJ, 'w'), indent=1)
    print(f'\n  wrote {os.path.relpath(OUT, HERE)} and {os.path.relpath(OUTJ, HERE)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
