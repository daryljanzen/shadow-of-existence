"""r7838+60: WHICH CONVENTION A LENSING FIGURE WAS MEASURED IN, AND WHY THE QUESTION IS NOT IDLE.

r7836 reported the omitted lensing signature as 0.372 per cent at Sum = 0.06 eV and 0.768 at 0.12,
"both peaking at l ~ 1980", and its receipt carries those as literals with the measurement kept
only in prose.  Rebuilding the operator here did NOT reproduce them: the fit's own convention gives
0.32 and 0.76 peaking at l ~ 2296 over the data's full reach.  So the figures are re-derived under
each convention that could have produced them, and the one that does is identified rather than
guessed at.

THREE THINGS CAN DIFFER, and each is a choice someone has to make:
  (a) WHAT IS HELD when the sum moves.  Holding the TOTAL Omega_m h^2 is what the fit does -- its
      Omega_m is the total, the distances see the total, and omega_cb falls by omega_nu.  Holding
      `omch2` instead, which is what a bare `camb.set_params(..., mnu=S)` does, RAISES the total
      with the sum, so the figure then carries an Omega_m shift as well as the neutrino's own
      free-streaming.
  (b) HOW THE SUM IS SPLIT.  `camb.set_params(mnu=S)` with nothing else said gives ONE massive
      species and two massless -- CAMB's default.  Three degenerate species is what Sum/93.14
      means and what the published analyses fit.
  (c) THE l WINDOW.  The arms' own spectra stop at l = 2000 (`LMAXL=2000`), so the 185 bins the fit
      scores end there; a figure measured out to the CAMB lmax of 3000 is measured where the fit
      cannot see.

Writes conventions.json.  rc=0 on success.  Run: python3 operator_conventions.py   (numpy, camb)
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
OMCH2_BARE = OMH2 - OMBH2            # what the borrowed harness passes, with mnu beside it
DIV = 93.14
OUT = os.path.join(HERE, 'conventions.json')


def ratio(sum_ev, hold_total, degenerate):
    onuh2 = sum_ev / DIV
    omch2 = (OMH2 - OMBH2 - onuh2) if hold_total else OMCH2_BARE
    kw = dict(H0=H0, ombh2=OMBH2, omch2=omch2, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=LMAX)
    if sum_ev <= 0.0:
        p = camb.set_params(mnu=0.0, num_massive_neutrinos=0, **kw)
    elif degenerate:
        p = camb.set_params(mnu=float(sum_ev), num_massive_neutrinos=3, **kw)
    else:
        p = camb.set_params(mnu=float(sum_ev), **kw)          # CAMB's default: one massive species
    cl = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=LMAX)
    le, un = cl['total'][:, 0], cl['unlensed_scalar'][:, 0]
    r = np.ones_like(le)
    r[un > 0] = le[un > 0] / un[un > 0]
    return r


def peak(r0, rs, lo, hi):
    ls = np.arange(len(r0), dtype=float)
    w = (ls >= lo) & (ls <= hi) & (r0 > 0)
    d = rs[w] / r0[w] - 1.0
    j = int(np.argmax(np.abs(d)))
    return float(100.0 * abs(d[j])), int(ls[w][j])


def main():
    out = {}
    for name, hold, deg in (('fit_convention_total_held_three_degenerate', True, True),
                            ('omch2_held_three_degenerate', False, True),
                            ('omch2_held_camb_default_split', False, False)):
        r0 = ratio(0.0, hold, deg)
        rows = {}
        for s in (0.06, 0.12):
            rs = ratio(s, hold, deg)
            for lo, hi in ((30, 2000), (30, 2508), (2, LMAX)):
                pct, l = peak(r0, rs, lo, hi)
                rows[f'{s:.2f}|{lo}-{hi}'] = dict(pct=pct, peak_l=l)
                print(f'  {name:46s} Sum={s:.2f} l={lo}-{hi}: {pct:.4f} per cent at l={l}',
                      flush=True)
        out[name] = rows
    json.dump(dict(reference=dict(H0=H0, ombh2=OMBH2, omh2_total=OMH2, omch2_bare=OMCH2_BARE,
                                  divisor=DIV, lmax=LMAX, model_lmax=2000),
                   conventions=out), open(OUT, 'w'), indent=1)
    print(f'\n  wrote {os.path.relpath(OUT, HERE)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
