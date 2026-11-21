#!/usr/bin/env python3
"""** THE GROWTH WHOSE INITIAL CONDITIONS ARE THE INSTRUMENT'S OWN STATE, NOT A CLOSED FORM'S. **

Order `r7847` ①, for items ② and ③ to be measured on.

`r7848`'s `GrowthKDep` solves the right equation and takes its initial conditions from
`L171x_lensing_potential.growth_over_a()` -- a matter + Λ closed form evaluated on a background
that carries radiation, which its own Ⓐ① measured wrong by about half a per cent in `D` by `z = 0`.
** That closed form is the LAST dependence the phi-phi path has on it, and this module removes it:
`delta_cb` and `d delta_cb / dN` at the start come from `ACOUSTIC_two_arm`'s own perturbation solve
at that same time, read off a single solve with three output times. **

⚠ ** AND THIS MODULE DOES NOT START EARLIER THAN `r7848` DID, WHICH IS THE OPPOSITE OF WHAT THE
ORDER ASKED FOR, BECAUSE THE MEASUREMENT SAID SO. **  `phi_carry.py` and `carry_isolate.py` measured
the carry against the instrument's own `Phi` from handovers at `z = 482`, `188`, `91.5` and `53.6`:
the residual is worse the EARLIER the handover and worse the longer the carry, and the Poisson
identity any growth-factor carry rests on holds on only `16`-`19` of `40` modes and only above
`k eta` of about `19`-`27`.  *The modes a growth factor can describe are the ones already deep
inside the horizon, and early on the lensing band is not.*  ⇒ So the handover stays at `eta_ref`,
where `r7848` had it, and what this revision changes is WHAT IS CARRIED FROM THERE.

Per-mode initial conditions are the point: `GrowthKDep`'s are one scalar pair for every `k`, because
a background quadrature has no `k` in it.  The instrument's state does, so these are arrays, and the
decaying mode the residual radiation era leaves behind is carried instead of discarded.

The normalisation per `k` is arbitrary and cancels: everything downstream uses
`ratio(k, a, a_ref) = g(k, a)/g(k, a_ref)`.

Used as a module:  `GrowthFromInstrument(mnu_ev, etaref=4000).ratio_fn(a_ref)`
Run as a script:   the reduction at zero sum and the suppression's shape, for comparison with
                   `r7848`'s same two readings.
"""
import io
import json
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)
sys.path.insert(0, _HERE)
sys.path.insert(0, _BTW)
import ACOUSTIC_two_arm as A                                               # noqa: E402
import growth_kdep as GK                                                  # noqa: E402

ETAREF = float(os.environ.get('ETAREF', '4000'))
NSTEP = int(os.environ.get('NSTEP', '400'))
DELTA = float(os.environ.get('DELTA', '8.0'))


class GrowthFromInstrument(GK.GrowthKDep):
    """`GrowthKDep` with the initial conditions read off the instrument instead of the quadrature"""

    def __init__(self, mnu_ev=0.0, n_species=3, kk=None, etaref=None, delta=DELTA):
        self.etaref = ETAREF if etaref is None else float(etaref)
        self.delta = float(delta)
        self._ic_cache = None
        super().__init__(mnu_ev=mnu_ev, n_species=n_species, kk=kk,
                         a_start=float(A.a_of_eta(self.etaref)))

    def _read_instrument(self):
        """ONE solve, three output times, so the derivative is a difference of the instrument's own
        output rather than a continuity equation written out here"""
        te = np.array([self.etaref - self.delta, self.etaref, self.etaref + self.delta], float)
        sol, nk, NV = A.evolve(self.kk, t_eval=te, e_end=float(te[-1]))
        assert sol.status == 0, f'the instrument solve did not finish: {sol.message}'
        Y = sol.y.T.reshape(len(te), nk, NV)
        wc = float(A.OCDM) / (float(A.OCDM) + float(A.OB))
        wb = 1.0 - wc
        d = wc * Y[:, :, 0] + wb * Y[:, :, NV - 1]
        N = np.log(np.array([float(A.a_of_eta(t)) for t in te]))
        self._ic_cache = (d[1], (d[2] - d[0]) / (N[2] - N[0]),
                          dict(phi_at_ref=[float(v) for v in Y[1, :, 6]],
                               weights=dict(cdm=wc, baryon=wb), eta_outputs=[float(t) for t in te]))
        return self._ic_cache

    def _ic(self):
        """unused by this class: the per-mode form below replaces it, and it is refused here so a
        later edit cannot silently fall back on the quadrature"""
        raise RuntimeError('GrowthFromInstrument takes per-mode initial conditions from the '
                           'instrument; the scalar quadrature form must not be used here')

    def _solve(self):
        if self._ic_cache is None:
            self._read_instrument()
        d0, dd0, _meta = self._ic_cache
        Ng = np.linspace(np.log(self.a_start), 0.0, NSTEP)
        rows = []
        for i, k in enumerate(self.kk):
            s = solve_ivp(self._rhs, (Ng[0], Ng[-1]), [float(d0[i]), float(dd0[i])], t_eval=Ng,
                          args=(float(k),), rtol=1e-11, atol=1e-16, method='Radau')
            assert s.success, f'the growth ODE failed at k = {k:.4g}: {s.message}'
            rows.append(s.y[0])
        self.N = Ng
        self.a = np.exp(Ng)
        self.D = np.asarray(rows)
        self.g = self.D / self.a[None, :]
        self._spl = [CubicSpline(Ng, self.g[i]) for i in range(len(self.kk))]

    def meta(self):
        if self._ic_cache is None:
            self._read_instrument()
        return self._ic_cache[2]


def main():
    kk = np.logspace(-4, 0, 40)
    print('\n  the growth with the instrument\'s own initial conditions, at eta_ref = %g (z = %.2f)'
          % (ETAREF, 1.0 / float(A.a_of_eta(ETAREF)) - 1.0), flush=True)
    g0 = GrowthFromInstrument(0.0, kk=kk)
    print('  built at zero sum over %d wavenumbers' % len(kk), flush=True)

    # Ⓓ④'s reading: the suppression of the POWER at a = 1, against the textbook -8 f_nu
    sum_ev = float(os.environ.get('SUM_EV', '0.06'))
    gm = GrowthFromInstrument(sum_ev, kk=kk)
    r0 = g0.ratio(kk, 1.0, g0.a_start).ravel()
    rm = gm.ratio(kk, 1.0, gm.a_start).ravel()
    supp = (rm / r0) ** 2 - 1.0                      # the POWER, which is the square
    f_nu = gm.f_nu
    textbook = -8.0 * f_nu
    out = dict(etaref=ETAREF, z_ref=1.0 / float(A.a_of_eta(ETAREF)) - 1.0, sum_ev=sum_ev,
               f_nu=f_nu, textbook=textbook,
               k=[float(v) for v in kk], suppression=[float(v) for v in supp],
               at_low_k=float(supp[0]), at_high_k=float(supp[-1]),
               ratio_to_textbook=float(supp[-1] / textbook),
               monotone_non_increasing=bool(np.all(np.diff(supp) <= 1e-12)),
               initial_conditions='from the instrument, per mode',
               meta=gm.meta())
    print('  suppression of the power at a = 1: %+.6f at k = %.1e, %+.6f at k = %.1e'
          % (supp[0], kk[0], supp[-1], kk[-1]))
    print('  against the textbook -8 f_nu = %+.6f: a ratio of %.6f (r7848 got 0.296012 from this '
          'same eta_ref)' % (textbook, out['ratio_to_textbook']))
    print('  monotone non-increasing in k: %s' % out['monotone_non_increasing'])
    with io.open(os.path.join(_HERE, 'growth_from_instrument.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote growth_from_instrument.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
