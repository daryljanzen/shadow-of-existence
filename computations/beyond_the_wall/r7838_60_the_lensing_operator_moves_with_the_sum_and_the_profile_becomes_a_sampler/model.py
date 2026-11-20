"""r7838+60: THE 185-BIN MODEL WITH THE LENSING OPERATOR MOVING WITH THE SUM.

On order r7833 (69), item ①.  What changes against r7836, and nothing else does:

  * r7836 scored every trial point through ONE lensing operator, formed at `mnu = 0.06`.  Here the
    operator is formed at EACH sum (`lensing_operator.py`, holding the total Omega_m h^2 so that
    omega_cb falls by omega_nu -- the fit's own convention), and the model's base AND its four
    direction derivatives are all binned THROUGH the operator at that sum.
  * r7836 carried the sum as one +/-0.06 pair and expanded quadratically in it, which over a
    posterior reaching 0.3 eV is a quadratic extrapolated five steps out.  Here the arm's own
    spectrum is GENERATED at each grid sum (`gen_spectra.sh`) and the sum direction is interpolated
    inside the generated range.
  * Everything else is the borrowed harness, called and not reimplemented: `refit.binned`'s
    binning, `chi2_of_spectrum`'s covariance and data, the banked four-direction grids, the
    analytic amplitude solve, and `distances.chi2_bao` on the arm's own ruler with `r_d` minimised.

** WHY THE BINNED VECTORS ARE WHAT IS INTERPOLATED, not the spectra. **  The arms' spectra are a
DISCRETE physical ladder whose l axis need not be identical from run to run, and the fit consumes
only the 185 binned values.  So every spectrum is binned first, through the operator at its own
sum, and the interpolation across the sum is done on the binned vectors.  No l axis is ever
assumed to match another.

** NEGATIVE SUMS ARE AN ANALYTIC CONTINUATION, AND IT IS STATED. **  CAMB cannot form an operator
at a negative sum, and no instrument can carry negative neutrino density.  For Sum < 0 the operator
is continued LINEARLY through zero on its own slope there -- which is operationally what the
published negative effective mass means: density moved out of the neutrinos and into the clustering
matter.  The arms' own spectra at negative sums are GENERATED, not continued.

rc=0 on import.  Not a receipt: this is the instrument the sampler runs on.
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.interpolate import CubicSpline

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
sys.path.insert(0, os.path.join(BW, 'r7749_70_leafgeom_refit'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import refit as R                                                          # noqa: E402
import distances as DI                                                     # noqa: E402
import chi2_of_spectrum as CS                                              # noqa: E402
from scipy.optimize import minimize_scalar                                 # noqa: E402

OLD_DIR = os.environ.get('MNU_DIR', '/tmp/claude-0/mnu_grid')       # r7836's +/-0.06 pair
NEW_DIR = os.environ.get('MNU_DIR2', '/tmp/claude-0/mnu_grid2')     # this revision's grid
RATIO_NPZ = os.path.join(HERE, 'ratio_grid.npz')
STEP_MNU = 0.06                                   # kept only to name r7836's pair
KEYS4 = list(R.STEP)                              # H0, OM, WB, NS -- the banked directions

ARMS = {
    'cr': dict(grid=os.path.join(BW, 'r7093_directions', 'grid_oneclock_leafrec1'),
               centre=dict(R.CENTRE), pref='cr', E=DI.E_leaf),
    'lcdm': dict(grid=os.path.join(BW, 'refit_grid185'),
                 centre=dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965), pref='lcdm', E=DI.E_stack),
}
# the arm's own spectrum at each generated sum: (sum, path-relative name, which directory)
SPEC = {
    -0.12: (NEW_DIR, 'Sm12'),
    -0.06: (OLD_DIR, 'MNUm'),
    0.00: (NEW_DIR, 'S000'),
    0.06: (OLD_DIR, 'MNUp'),
    0.15: (NEW_DIR, 'S015'),
    0.30: (NEW_DIR, 'S030'),
}

_Z = np.load(RATIO_NPZ)
_LS_R, _SGRID, _RMAT = _Z['ls'], _Z['grid'], _Z['ratio']
_R0 = _RMAT[0]
_okr = _R0 > 0
# the operator's fractional shape against Sum = 0, splined per l across the generated sums
_FRAC = np.zeros_like(_RMAT)
_FRAC[:, _okr] = _RMAT[:, _okr] / _R0[_okr] - 1.0
_SPL = CubicSpline(_SGRID, _FRAC, axis=0)
_SLOPE0 = _SPL(0.0, 1)                                  # d(frac)/d(Sum) at zero, per l


def ratio_at(sum_ev):
    """the lensing operator at this sum; linear continuation of its own slope below zero."""
    f = _SPL(float(sum_ev)) if sum_ev >= 0.0 else _SLOPE0 * float(sum_ev)
    return _R0 * (1.0 + f)


def _spec(arm, sum_ev):
    d, tag = SPEC[sum_ev]
    p = os.path.join(d, f"{ARMS[arm]['pref']}_{tag}.npz")
    z = np.load(p)
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


def _bin_with(ratio, ls, Dl):
    """`refit.binned`, with the operator passed in rather than read from the module."""
    return CS.bin_spectrum(ls, Dl * np.interp(ls, _LS_R, ratio))


def _base_nodes(arm):
    """the binned base at each GENERATED sum, each through the operator AT THAT SUM."""
    sums = sorted(SPEC)
    rows = []
    for s in sums:
        ls, Dl = _spec(arm, s)
        rows.append(_bin_with(ratio_at(s), ls, Dl))
    return np.asarray(sums, float), np.asarray(rows)


def _dir_nodes(arm, ok):
    """the four banked directions' first and second differences, binned through the operator at
    each sum on the OPERATOR's own grid -- the directions themselves are held at Sum = 0, which is
    where they were generated, and that is stated rather than hidden."""
    a = ARMS[arm]
    pref = a['pref']
    raw = {}
    for k in KEYS4:
        for sgn in ('p', 'm'):
            z = np.load(os.path.join(a['grid'], f'{pref}_{k}{sgn}.npz'))
            raw[(k, sgn)] = (np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
    z = np.load(os.path.join(a['grid'], f'{pref}_base.npz'))
    raw['base'] = (np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
    g, h = {k: [] for k in KEYS4}, {k: [] for k in KEYS4}
    for s in _SGRID:
        rt = ratio_at(float(s))
        b = _bin_with(rt, *raw['base'])[ok]
        for k in KEYS4:
            mp = _bin_with(rt, *raw[(k, 'p')])[ok]
            mm = _bin_with(rt, *raw[(k, 'm')])[ok]
            g[k].append((mp - mm) / (2 * R.STEP[k]))
            h[k].append((mp - 2 * b + mm) / R.STEP[k] ** 2)
    return {k: CubicSpline(_SGRID, np.asarray(g[k]), axis=0) for k in KEYS4}, \
           {k: CubicSpline(_SGRID, np.asarray(h[k]), axis=0) for k in KEYS4}


class Model:
    """the binned model and its chi^2, as a function of the four offsets and the sum."""

    def __init__(self, arm):
        self.arm = arm
        s_nodes, rows = _base_nodes(arm)
        self.ok = np.isfinite(rows).all(axis=0)
        self.nb = int(self.ok.sum())
        self.base = CubicSpline(s_nodes, rows[:, self.ok], axis=0)
        self.s_lo, self.s_hi = float(s_nodes[0]), float(s_nodes[-1])
        self.g, self.h = _dir_nodes(arm, self.ok)
        F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(self.ok, self.ok)]),
                                   np.identity(self.nb))
        self.F = 0.5 * (F + F.T)
        self.d = CS.X_DATA[self.ok]
        self.sig = np.sqrt(np.diag(CS.COV_TT[np.ix_(self.ok, self.ok)]))
        self._bao = {}

    def binned(self, x4, sum_ev):
        s = float(np.clip(sum_ev, self.s_lo, self.s_hi))
        m = np.asarray(self.base(s), float).copy()
        for k, v in zip(KEYS4, x4):
            m = m + np.asarray(self.g[k](max(s, 0.0)), float) * v \
                  + 0.5 * np.asarray(self.h[k](max(s, 0.0)), float) * v * v
        return m

    def chi2_cmb(self, x4, sum_ev):
        m = self.binned(x4, sum_ev)
        if np.any(m <= 0) or not np.all(np.isfinite(m)):
            return 1e12
        A = float((m @ self.F @ self.d) / (m @ self.F @ m))
        r = self.d - A * m
        return float(r @ self.F @ r)

    def phys(self, x4, sum_ev):
        c = ARMS[self.arm]['centre']
        return dict(H0=c['H0'] + R.STEP['H0'] * x4[0], OM=c['OM'] + R.STEP['OM'] * x4[1],
                    WB=c['WB'] + R.STEP['WB'] * x4[2], NS=c['NS'] + R.STEP['NS'] * x4[3],
                    MNU=float(sum_ev))

    def chi2_bao(self, H0, OM):
        key = (round(H0, 4), round(OM, 5))
        if key not in self._bao:
            E = ARMS[self.arm]['E']
            r = minimize_scalar(lambda rd: DI.chi2_bao(H0, OM, rd, E), bounds=(120, 170),
                                method='bounded')
            self._bao[key] = (float(r.fun), float(r.x))
        return self._bao[key]

    def chi2(self, x5, bao=True):
        x4, s = x5[:4], float(x5[4])
        if not (self.s_lo <= s <= self.s_hi):
            return 1e12
        c = self.chi2_cmb(x4, s)
        if bao:
            p = self.phys(x4, s)
            c += self.chi2_bao(p['H0'], p['OM'])[0]
        return c

    def binned_exact(self, x4, sum_ev, ls, Dl):
        """the binned model built EXACTLY at this sum from a freshly generated spectrum, for the
        interpolation arm -- no node, no spline on the base."""
        rt = ratio_at(sum_ev)
        m = _bin_with(rt, ls, Dl)[self.ok]
        for k, v in zip(KEYS4, x4):
            m = m + np.asarray(self.g[k](max(sum_ev, 0.0)), float) * v \
                  + 0.5 * np.asarray(self.h[k](max(sum_ev, 0.0)), float) * v * v
        return m
