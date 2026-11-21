"""** Ⓒ③ AND Ⓔ⑤: DOES THE INITIAL-CONDITION REPAIR MOVE THE BANDPOWERS AT ALL? **

Order `r7847` ② first half (the lensing shape drift) and the arm Ⓔ⑤ (the absolute normalisation).

`r7848` measured the shape systematic at the ordered carry: `chi^2` `16.389` on `8` degrees of
freedom, `2.049` per degree of freedom, with a monotone `+49.8` per cent drift, and held
`(A_cmb/T_CMB^2) e^{+2 tau} = 1.617967e-09` against the bandpowers' own preferred `1.471643e-09`,
a ratio of `0.909563`.

This revision's change to the lensing path is ONE thing: the growth's initial conditions now come
from the instrument's own perturbation solve rather than from a matter + Λ closed form.  ** So the
question Ⓒ③ and Ⓔ⑤ really ask is how far that moves the nine bandpowers, and the answer decides
whether the order's item ③ is worth six hours of grid and two of chains or is already settled. **

⌗ ** THE MEASUREMENT COMES BEFORE THE SPEND, WHICH IS THIS LINE'S OWN GUARD FROM r7848: when an
apparatus misses its control, measure whether the shortfall is a width or a centre before ordering
more data. **  Here: measure whether the repair moves the data vector by anything the data could
notice, before regenerating a grid on it.  The bandpowers' own fractional errors are `5.0` to
`17.6` per cent, so a change far inside that cannot move a limit.

Both spectra are built in ONE process with `phi_shape` memoised, because the instrument solve at
`eta_ref` costs `667` s and is the SAME solve for both growths -- only what is carried from it
differs.

Run: python3 shape_sensitivity.py          (writes shape_sensitivity.json)
"""
import functools
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)
sys.path.insert(0, _HERE)
sys.path.insert(0, _BTW)
import growth_kdep as GK                                                   # noqa: E402
import lensing_like as LL                                                  # noqa: E402
import phiphi as PP                                                        # noqa: E402
from growth_from_instrument import GrowthFromInstrument                     # noqa: E402

A = PP.A
ETAREF = float(os.environ.get('ETAREF', '4000'))
NKG = int(os.environ.get('NKG', '48'))

# ** ONE instrument solve for both growths: the shape at eta_ref does not depend on which growth
# carries it forward, and r7848's cost table (as this revision re-measured it) puts that solve at
# 667 s. **
PP.phi_shape = functools.lru_cache(maxsize=4)(PP.phi_shape)


def score(b):
    """`chi^2` at the vector's own best normalisation, and that normalisation"""
    a = float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b))
    r = LL.DATA - a * b
    return float(r @ LL.FISHER @ r), a


def drift(b):
    """the monotone drift against the data, as a percentage, the way r7848 measured it"""
    rat = (b / LL.DATA)
    rat = rat / rat[0]
    return float(100.0 * (rat[-1] - 1.0)), bool(np.all(np.diff(rat) <= 1e-12) or
                                                np.all(np.diff(rat) >= -1e-12))


def main():
    lb, cov, wins = PP.bandpowers()
    Lg = np.unique(np.concatenate([L for L, _ in wins]))
    ls = np.unique(np.round(np.logspace(np.log10(max(2, Lg.min())),
                                        np.log10(Lg.max()), 36)).astype(int))
    a_ref = float(A.a_of_eta(ETAREF))
    kk = np.logspace(np.log10(PP.KMIN), np.log10(PP.KMAX), NKG)
    err = np.sqrt(np.diag(cov))
    frac = err / LL.DATA

    print('\n  Ⓒ③/Ⓔ⑤: how far the initial-condition repair moves the nine bandpowers\n')
    print('  eta_ref = %g (z = %.2f); %d multipoles; %d wavenumbers in the growth'
          % (ETAREF, 1.0 / a_ref - 1.0, len(ls), NKG), flush=True)
    print('  the bandpowers\' own fractional errors run %.1f to %.1f per cent\n'
          % (100 * frac.min(), 100 * frac.max()), flush=True)

    out = {}
    for tag, g in (('quadrature_ics', GK.GrowthKDep(0.0, kk=kk, a_start=a_ref)),
                   ('instrument_ics', GrowthFromInstrument(0.0, kk=kk, etaref=ETAREF))):
        cl = PP.clpp(ls, 0.0, etaref=ETAREF, growth=g)
        b = PP.bin_through(ls, cl, wins)
        c2, amp = score(b)
        dr, mono = drift(b)
        out[tag] = dict(bandpowers=[float(v) for v in b], chi2=c2, chi2_per_dof=c2 / 8.0,
                        best_amplitude=amp, drift_pc=dr, drift_monotone=mono)
        print('  [%s] chi^2 %.6f on 8 dof (%.6f per dof); drift %+.4f per cent%s'
              % (tag, c2, c2 / 8.0, dr, '' if mono else '  (NOT monotone)'), flush=True)

    bq = np.array(out['quadrature_ics']['bandpowers'])
    bi = np.array(out['instrument_ics']['bandpowers'])
    rel = bi / bq - 1.0
    in_sigma = np.abs(bi - bq) / (err / LL.DATA * bq)   # the change in units of the bin's own error
    out['difference'] = dict(
        relative=[float(v) for v in rel],
        in_units_of_the_bins_error=[float(v) for v in in_sigma],
        worst_relative=float(np.max(np.abs(rel))),
        worst_in_units_of_the_bins_error=float(np.max(in_sigma)),
        chi2_change=out['instrument_ics']['chi2'] - out['quadrature_ics']['chi2'],
        amplitude_change_relative=(out['instrument_ics']['best_amplitude']
                                   / out['quadrature_ics']['best_amplitude'] - 1.0),
        fractional_error_pc=[float(100 * v) for v in frac])
    d = out['difference']
    print('\n  the repair moves the bandpowers by at most %.4e relative, which is %.4e of the '
          'bin\'s own error' % (d['worst_relative'], d['worst_in_units_of_the_bins_error']))
    print('  chi^2 moves by %+.6f and the best normalisation by %+.4e relative'
          % (d['chi2_change'], d['amplitude_change_relative']))
    settled = d['worst_in_units_of_the_bins_error'] < 0.1
    out['r7848'] = dict(chi2=16.389449912869935, chi2_per_dof=2.048681239108742,
                        drift_pc=49.81347923198254, amp_ratio=0.909563)
    out['verdict'] = (
        'the repair moves the data vector by %.3e of a bandpower error at worst, so it cannot move '
        'a limit: item 3 does not need a regenerated grid and a fresh chain to be answered, and '
        'this measurement is the answer' % d['worst_in_units_of_the_bins_error']) if settled else (
        'the repair moves the data vector by %.3e of a bandpower error, which the data CAN notice, '
        'so the grid and the chains are owed' % d['worst_in_units_of_the_bins_error'])
    out['grid_and_chains_owed'] = bool(not settled)
    print('\n  ⇒ %s\n' % out['verdict'])
    with io.open(os.path.join(_HERE, 'shape_sensitivity.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote shape_sensitivity.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
