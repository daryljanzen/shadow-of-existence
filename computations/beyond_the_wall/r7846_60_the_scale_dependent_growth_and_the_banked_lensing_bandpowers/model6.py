#!/usr/bin/env python3
"""** THE SIX-PARAMETER SCORE: 555 CMB BINS, NINE LENSING BANDPOWERS, AND `tau`. **

Order `r7845` ②-③.  `r7844`'s five-parameter model is reused WHOLE for the CMB half -- same bins,
same covariance, same analytic amplitude -- and two things are added: the nine banked lensing
bandpowers, scored with no amplitude fitted to them, and `tau`, which is what the lensing term makes
reachable.

    x = [H0, OM, WB, NS  (grid-step offsets),  Sum (eV),  tau]

** THE AMPLITUDE, WHICH IS THE WHOLE MECHANISM. **  Every mode of the instrument's solve starts at
`Phi = -1`, so the CMB spectra and the lensing potential share one primordial normalisation.  The
CMB fit determines `AMP * exp(-2 tau)` -- it is solved in closed form at each point, exactly as
`r7844` did -- and the lensing prediction is that same number times `exp(+2 tau) / T_CMB^2`.  So
nothing is fitted to the lensing data, and `tau` cannot cancel.  `r7846` measured the reach this
buys: `chi^2` moves by `355` across `tau = 0.02`-`0.20` where `r7844` measured `1.1e-12` without it.

⚠ ** THE ONE APPROXIMATION IN THE LENSING INTERPOLATION, NAMED. **  The `phi-phi` grid has its eight
sums at the arm's centre and its eight parameter directions at `Sum = 0`, so the parameter response
is carried as `Sum`-INDEPENDENT: `shape(x4, Sum) = base(Sum) * [1 + g.x + h.x^2/2]`.  The CMB half
does better than this -- `r7844`'s model takes its derivatives at every sum -- and the lensing half
cannot without eight more spectra per arm per sum.  *It is a separable approximation, it is stated
here rather than left for a reader to infer from the file layout, and the receipt reports it as a
limitation and not as a detail.*

⚠ ** AND THE SHAPE SYSTEMATIC THIS TERM CARRIES. **  Scored against the nine bandpowers with one
best-fit normalisation, this instrument's `phi-phi` gives `chi^2/dof = 2.05` with a MONOTONE
`49.8` per cent drift in the implied normalisation across `L = 28`-`377`.  That is a `50` per cent
systematic on a signal of about `5` per cent.  `r7846` measured that the sum still moves
`chi^2_lens` by `94.5` across the banked range, far more than the systematic costs -- so the term
is informative -- but **any limit from it is confounded with that drift and with `tau`, and the
receipt says so beside the number rather than after it.**
"""
import glob
import json
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_R44 = os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_harness_'
                          'does_not_have')
sys.path.insert(0, _HERE)
sys.path.insert(0, _R44)

import lensing_like as LL                                                # noqa: E402
import model3 as M3                                                      # noqa: E402

GRID = os.environ.get('PPGRID', '/tmp/claude-0/phiphi_grid_eta4000')
T_CMB_UK = 2.7255e6
KEYS4 = ('H0', 'OM', 'WB', 'NS')
TAU_LO, TAU_HI = 0.0, 0.40


def _load(arm):
    out = {}
    for p in sorted(glob.glob(os.path.join(GRID, f'{arm}_*.json'))):
        j = json.load(open(p))
        out[j['tag']] = np.asarray(j['bandpowers'], float)
    return out


class Model6:
    """the joint score: `r7844`'s CMB half unchanged, plus the lensing bandpowers and `tau`"""

    def __init__(self, arm, blocks=(0, 1, 2)):
        self.arm = arm
        self.cmb = M3.Model3(arm, blocks=blocks)
        g = _load(arm)
        tags = {'Sm12': -0.12, 'Sm06': -0.06, 'S000': 0.0, 'S006': 0.06,
                'S015': 0.15, 'S030': 0.30, 'S045': 0.45, 'S060': 0.60}
        have = {t: v for t, v in tags.items() if t in g}
        if len(have) < 4:
            raise RuntimeError(f'{arm}: only {len(have)} lensing sum point(s) in {GRID}')
        sums = sorted(have.values())
        rows = np.array([g[[t for t, s in have.items() if s == v][0]] for v in sums])
        self.pp_sums = np.asarray(sums, float)
        self.pp_base = CubicSpline(self.pp_sums, rows, axis=0)
        self.s_lo, self.s_hi = float(sums[0]), float(sums[-1])

        b0 = g['S000']
        self.pp_g, self.pp_h = {}, {}
        for k in KEYS4:
            if f'{k}p' in g and f'{k}m' in g:
                self.pp_g[k] = (g[f'{k}p'] - g[f'{k}m']) / 2.0 / b0
                self.pp_h[k] = (g[f'{k}p'] - 2.0 * b0 + g[f'{k}m']) / b0
            else:
                self.pp_g[k] = np.zeros_like(b0)
                self.pp_h[k] = np.zeros_like(b0)
        self.n_dirs = sum(1 for k in KEYS4 if f'{k}p' in g and f'{k}m' in g)

    # ── the lensing half ────────────────────────────────────────────────────────────────────────
    def pp_shape(self, x4, sum_ev):
        """the nine bandpowers' SHAPE at this point, in the instrument's own normalisation"""
        s = float(np.clip(sum_ev, self.s_lo, self.s_hi))
        base = self.pp_base(s)
        fac = np.ones_like(base)
        for j, k in enumerate(KEYS4):
            fac = fac + self.pp_g[k] * x4[j] + 0.5 * self.pp_h[k] * x4[j] ** 2
        return base * fac

    def amp_cmb(self, x4, sum_ev):
        """`AMP * exp(-2 tau)` as the CMB fit determines it, in closed form -- r7844's own solve"""
        m = self.cmb.binned(x4, sum_ev)
        F, d = self.cmb.F, self.cmb.d
        den = float(m @ F @ m)
        return (float(m @ F @ d) / den) if den > 0 else np.nan

    def pp_model(self, x4, sum_ev, tau):
        """the nine bandpowers PREDICTED, absolutely: the CMB's amplitude, undone of exp(-2 tau)"""
        a = self.amp_cmb(x4, sum_ev)
        if not np.isfinite(a):
            return None
        return (a / T_CMB_UK ** 2) * np.exp(2.0 * float(tau)) * self.pp_shape(x4, sum_ev)

    # ── the joint chi^2 ─────────────────────────────────────────────────────────────────────────
    def chi2(self, x6, bao=True, lensing=True, tau_prior=True):
        x6 = np.asarray(x6, float)
        x4, s, tau = x6[:4], float(x6[4]), float(x6[5])
        if not (TAU_LO <= tau <= TAU_HI):
            return 1e12
        c = self.cmb.chi2(np.concatenate([x4, [s]]), bao=bao)
        if c >= 1e11:
            return c
        if lensing:
            m = self.pp_model(x4, s, tau)
            if m is None:
                return 1e12
            c += LL.chi2(m)
        if tau_prior:
            c += LL.chi2_tau(tau)
        return float(c)

    def chi2_barrier(self, x6, lo=None):
        """the SLOPED infeasible region r7838 needed, carried to six parameters

        A flat penalty let Powell report a plateau as a minimum at r7838; the slope is what stops
        that, and any result landing on the barrier is discarded by the caller rather than reported.
        """
        x6 = np.asarray(x6, float)
        lo = self.cmb.s_lo if lo is None else lo
        v = 0.0
        v += max(0.0, lo - x6[4]) + max(0.0, x6[4] - self.s_hi)
        v += max(0.0, TAU_LO - x6[5]) + max(0.0, x6[5] - TAU_HI)
        v += float(np.sum(np.maximum(0.0, np.abs(x6[:4]) - 6.0)))
        if v > 0:
            return 1e6 + 1e6 * v * v
        return self.chi2(x6)

    def describe(self):
        return dict(arm=self.arm, cmb_bins=int(self.cmb.ok.sum()), lensing_bandpowers=int(LL.NBP),
                    lensing_sums=[float(v) for v in self.pp_sums],
                    lensing_directions=int(self.n_dirs),
                    parameter_response_is_sum_independent=True,
                    tau_range=[TAU_LO, TAU_HI],
                    tau_prior=dict(mean=LL.TAU_MEAN, sigma=LL.TAU_SIGMA))


if __name__ == '__main__':
    m = Model6(os.environ.get('ARM6', 'lcdm'))
    print(json.dumps(m.describe(), indent=1, sort_keys=True))
    x = np.array([0.0, 0.0, 0.0, 0.0, 0.0, LL.TAU_MEAN])
    print('\n  chi2 at the centre, Sum = 0, tau = %.3f: %.3f' % (LL.TAU_MEAN, m.chi2(x)))
    print('  CMB only                                : %.3f'
          % m.chi2(x, lensing=False, tau_prior=False))
    print('  + lensing                               : %.3f' % m.chi2(x, tau_prior=False))
    print('  + the tau prior                         : %.3f' % m.chi2(x))
