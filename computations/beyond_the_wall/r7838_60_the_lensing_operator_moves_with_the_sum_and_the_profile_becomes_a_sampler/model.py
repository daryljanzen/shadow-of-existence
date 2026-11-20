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
from scipy.interpolate import CubicSpline, RectBivariateSpline

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
_SPEC_ALL = {
    -0.12: (NEW_DIR, 'Sm12'),
    -0.06: (OLD_DIR, 'MNUm'),
    0.00: (NEW_DIR, 'S000'),
    0.06: (OLD_DIR, 'MNUp'),
    0.15: (NEW_DIR, 'S015'),
    0.30: (NEW_DIR, 'S030'),
    0.45: (NEW_DIR, 'S045'),
    0.60: (NEW_DIR, 'S060'),
}
# only the nodes whose spectra exist FOR BOTH ARMS are used, so the two arms are always
# interpolated over the same range and a half-generated extension cannot quietly make them
# different instruments.
SPEC = {s: v for s, v in _SPEC_ALL.items()
        if all(os.path.exists(os.path.join(v[0], f'{pref}_{v[1]}.npz'))
               for pref in ('cr', 'lcdm'))}

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
        self._bao_spl = None
        self.rd_fixed = (float(os.environ['RD_FIXED']) if os.environ.get('RD_FIXED') else None)

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

    RD_BOUNDS = (100.0, 220.0)
    RD_BORROWED = (120.0, 170.0)      # what `r7836`'s fit used

    def bao_direct(self, H0, OM, bounds=None):
        """`distances.chi2_bao` on this arm's own ruler with `r_d` MINIMISED -- the honest call,
        about 5 ms, which is 48 times the cost of the whole CMB term.

        ** THE RULER'S BRACKET IS WIDENED, AND THAT IS A FINDING RATHER THAN A SETTING. **
        `r7836` minimised `r_d` inside `(120, 170)`.  Over the region this fit explores the
        minimising `r_d` LEAVES that interval -- it runs from about 120 at the high-`H0` edge to
        about 188 at the low one -- so across much of the region the bound was binding and the
        ruler was NOT being marginalised but pinned to an endpoint.  A bound that binds also puts
        a KINK in the surface, which is how this was noticed: an interpolation of the term that
        should have been smooth to a thousandth came out wrong by eleven.  The bracket here is
        `(100, 220)`, inside which the minimum is interior everywhere in the tabulated box, and
        `bao_truncation` reports what fraction of that box the borrowed bracket would have
        truncated.
        """
        b = self.RD_BOUNDS if bounds is None else tuple(bounds)
        key = (round(H0, 6), round(OM, 7), b)
        if key not in self._bao:
            E = ARMS[self.arm]['E']
            r = minimize_scalar(lambda rd: DI.chi2_bao(H0, OM, rd, E), bounds=b, method='bounded')
            self._bao[key] = (float(r.fun), float(r.x))
        return self._bao[key]

    def bao_truncation(self, half_steps=6, n=21):
        """over the tabulated box: the fraction of points where the BORROWED bracket binds, and the
        largest chi^2 it adds by binding."""
        c = ARMS[self.arm]['centre']
        lo, hi = self.RD_BORROWED
        bound, worst, tot = 0, 0.0, 0
        for a in np.linspace(c['H0'] - half_steps * R.STEP['H0'],
                             c['H0'] + half_steps * R.STEP['H0'], n):
            for b in np.linspace(c['OM'] - half_steps * R.STEP['OM'],
                                 c['OM'] + half_steps * R.STEP['OM'], n):
                free = self.bao_direct(float(a), float(b))
                pin = self.bao_direct(float(a), float(b), bounds=self.RD_BORROWED)
                tot += 1
                if pin[1] <= lo + 1e-4 or pin[1] >= hi - 1e-4:
                    bound += 1
                    worst = max(worst, pin[0] - free[0])
        return dict(points=tot, bound=bound, fraction=bound / float(tot), worst_chi2_added=worst)

    def _build_bao_spline(self, half_steps=6, n_h0=17, n_om=401):
        """the SAME minimised BAO term on a grid in (H0, Omega_m), splined.

        A sampler needs a million evaluations and the honest call costs 5 ms, so the term is
        tabulated once and interpolated.  The grid is deliberately ANISOTROPIC, and that is a
        measured fact about the term rather than a convenience: with `r_d` minimised, the control's
        BAO chi^2 is EXACTLY independent of `H0` -- identical to eight decimals across fourteen
        units of it, because the ruler rescales to absorb it -- and the arm of record's varies by
        only about `0.03` in chi^2 over the same span, while in `Omega_m` it moves by hundreds.  So
        the BAO term is effectively a function of `Omega_m` alone, which is also WHY the sum is so
        nearly degenerate with `Omega_m` in this fit: the only thing paying for a moved total is
        this one-dimensional term.  THE SUBSTITUTION IS CHECKED, not assumed: `bao_error`
        reports the largest disagreement against the honest call over points drawn inside the
        sampled region, and the sampler refuses to run if it is not far below the chi^2 resolution
        anything here is read at.
        """
        c = ARMS[self.arm]['centre']
        h0 = np.linspace(c['H0'] - half_steps * R.STEP['H0'], c['H0'] + half_steps * R.STEP['H0'],
                         n_h0)
        om = np.linspace(c['OM'] - half_steps * R.STEP['OM'], c['OM'] + half_steps * R.STEP['OM'],
                         n_om)
        Z = np.empty((n_h0, n_om))
        for i, a in enumerate(h0):
            for j, b in enumerate(om):
                Z[i, j] = self.bao_direct(float(a), float(b))[0]
        self._bao_lo = (float(h0[0]), float(om[0]))
        self._bao_hi = (float(h0[-1]), float(om[-1]))
        self._bao_spl = RectBivariateSpline(h0, om, Z, kx=3, ky=3, s=0)

    def bao_error(self, rng, m=200):
        """the largest |spline - honest| over m points drawn inside the tabulated region."""
        if self._bao_spl is None:
            self._build_bao_spline()
        lo, hi = self._bao_lo, self._bao_hi
        worst = 0.0
        for _ in range(m):
            a = lo[0] + (hi[0] - lo[0]) * rng.random()
            b = lo[1] + (hi[1] - lo[1]) * rng.random()
            worst = max(worst, abs(float(self._bao_spl(a, b)[0, 0]) - self.bao_direct(a, b)[0]))
        return float(worst)

    def chi2_bao(self, H0, OM):
        if self.rd_fixed is not None:
            # ** THE RULER HELD INSTEAD OF MARGINALISED. **  Not an alternative convention but a
            # MEASUREMENT of which missing lever costs this harness its constraining power: the
            # published analysis calibrates r_d against the microwave background's own baryon and
            # matter densities, while this harness lets r_d float free at every point, which is
            # what makes the BAO term a function of Omega_m alone.  Running the same fit with r_d
            # held says how much of the looseness that one choice accounts for.
            return (float(DI.chi2_bao(H0, OM, self.rd_fixed, ARMS[self.arm]['E'])), self.rd_fixed)
        if self._bao_spl is None:
            self._build_bao_spline()
        lo, hi = self._bao_lo, self._bao_hi
        if not (lo[0] <= H0 <= hi[0] and lo[1] <= OM <= hi[1]):
            return self.bao_direct(H0, OM)
        return (float(self._bao_spl(H0, OM)[0, 0]), float('nan'))

    def chi2(self, x5, bao=True):
        x4, s = x5[:4], float(x5[4])
        if not (self.s_lo <= s <= self.s_hi):
            return 1e12
        c = self.chi2_cmb(x4, s)
        if bao:
            p = self.phys(x4, s)
            c += self.chi2_bao(p['H0'], p['OM'])[0]
        return c


    def chi2_barrier(self, x5, lo=None):
        """the same chi^2 for a MINIMISER, with the infeasible region SLOPED instead of flat.

        A flat 1e12 penalty is a trap for a direction-set method: Powell walked into it and
        reported the plateau as a minimum.  The barrier keeps the infeasible region worse than
        anything feasible while still pointing back toward the feasible set.
        """
        x4, s = np.asarray(x5[:4], float), float(x5[4])
        slo = self.s_lo if lo is None else lo
        v = max(0.0, slo - s) + max(0.0, s - self.s_hi) + float(np.sum(np.maximum(0.0, np.abs(x4) - 6.0)))
        if v > 0:
            return 1e6 + 1e6 * v * v
        m = self.binned(x4, s)
        if not np.all(np.isfinite(m)):
            return 1e6
        neg = float(np.sum(np.maximum(0.0, -m) ** 2)) / max(float(np.mean(np.abs(m))) ** 2, 1e-300)
        if neg > 0:
            return 1e6 + 1e6 * neg
        A = float((m @ self.F @ self.d) / (m @ self.F @ m))
        r = self.d - A * m
        c = float(r @ self.F @ r)
        p = self.phys(x4, s)
        return c + self.chi2_bao(p['H0'], p['OM'])[0]

    def binned_exact(self, x4, sum_ev, ls, Dl):
        """the binned model built EXACTLY at this sum from a freshly generated spectrum, for the
        interpolation arm -- no node, no spline on the base."""
        rt = ratio_at(sum_ev)
        m = _bin_with(rt, ls, Dl)[self.ok]
        for k, v in zip(KEYS4, x4):
            m = m + np.asarray(self.g[k](max(sum_ev, 0.0)), float) * v \
                  + 0.5 * np.asarray(self.h[k](max(sum_ev, 0.0)), float) * v * v
        return m
