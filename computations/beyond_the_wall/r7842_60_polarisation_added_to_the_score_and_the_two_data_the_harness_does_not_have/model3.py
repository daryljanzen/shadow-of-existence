"""r7842+60: THE 555-BIN MODEL -- TT, TE AND EE, WITH EVERY OPERATOR MOVING WITH THE SUM.

On order r7841 (69), items ① and ④.  This is r7838's `model.py` with the score widened from one
spectrum to three.  What is kept, unchanged and deliberately:

  * the sum direction is INTERPOLATED on GENERATED nodes, never extrapolated from one pair;
  * the binned vectors are what is interpolated across the sum, not the spectra, because the arms'
    multipole axis is a discrete physical ladder and the fit consumes only the binned values;
  * negative sums are the operator's LINEAR CONTINUATION through zero, which is what the published
    negative effective mass means, while the arms' own spectra at negative sums are GENERATED;
  * the BAO term is `distances.chi2_bao` on the arm's own ruler with `r_d` minimised over the
    WIDENED bracket r7838 established, inside which the minimum is interior everywhere in the box;
  * the BAO term is tabulated on an anisotropic grid and the substitution is CHECKED, because with
    `r_d` minimised that term is a function of `Omega_m` alone.

What is new:

  * three spectra per point, scored through `score_ttteee` with ONE amplitude across them;
  * one operator per spectrum, each formed at the trial sum: multiplicative for TT and EE,
    and for TE an ADDITIVE correction carried as a ratio to TT so the free amplitude cancels;
  * the four banked directions now carry all three spectra, which is why every point had to be
    regenerated with `POLSAVE` on.

rc=0 on import.  Not a receipt: this is the instrument the sampler runs on.
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.interpolate import CubicSpline, RectBivariateSpline
from scipy.optimize import minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(BW, 'r7749_70_leafgeom_refit'))
import refit as R                                                          # noqa: E402
import distances as DI                                                     # noqa: E402
import score_ttteee as SC                                                  # noqa: E402

POL_DIR = os.environ.get('POL_DIR', '/tmp/claude-0/pol_grid')
RATIO_NPZ = os.path.join(HERE, 'ratio_grid3.npz')
KEYS4 = list(R.STEP)                               # H0, OM, WB, NS
BLOCKS = tuple(int(b) for b in os.environ.get('BLOCKS', '0,1,2').split(','))

ARMS = {
    'cr': dict(centre=dict(R.CENTRE), pref='cr', E=DI.E_leaf),
    'lcdm': dict(centre=dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965), pref='lcdm', E=DI.E_stack),
}
_SUM_TAGS = {-0.12: 'Sm12', -0.06: 'Sm06', 0.00: 'S000', 0.06: 'S006',
             0.15: 'S015', 0.30: 'S030', 0.45: 'S045', 0.60: 'S060'}


# ** WHOSE SPECTRA HAVE TO EXIST BEFORE A SUM IS A NODE. **  By default BOTH arms', so that a
#   half-finished generation can never leave the two arms interpolated over different ranges, which
#   would make them two instruments rather than one comparison.  `SUM_ARMS` narrows it to one arm,
#   and it is narrowed for exactly one purpose: the CONTROL is scored first, as the order requires,
#   while the arm of record's own points are still generating.  ⌗ *Any run that COMPARES the two
#   must leave this at its default, and the receipt asserts that the comparison was made on the
#   same node set.*
SUM_ARMS = tuple(a for a in os.environ.get('SUM_ARMS', 'cr,lcdm').split(',') if a)


def available_sums(arms=None):
    """the sums whose spectra exist for every arm in `arms` (both, unless narrowed on purpose)"""
    need = tuple(arms) if arms else SUM_ARMS
    return sorted(s for s, t in _SUM_TAGS.items()
                  if all(os.path.exists(os.path.join(POL_DIR, f'{p}_{t}.npz')) for p in need))


def directions_ready(arm):
    return all(os.path.exists(os.path.join(POL_DIR, f"{ARMS[arm]['pref']}_{k}{s}.npz"))
               for k in KEYS4 for s in ('p', 'm'))


_Z = np.load(RATIO_NPZ)
_LS_R, _SG = _Z['ls'], _Z['grid']
_RTT, _REE, _DTE = _Z['ratio_tt'], _Z['ratio_ee'], _Z['dte_over_tt']
# each operator's response against Sum = 0, splined per multipole across the generated sums; the
# zero-sum operator itself is the reference the response multiplies
_R0TT, _R0EE = _RTT[0], _REE[0]
_FTT = np.zeros_like(_RTT)
_FEE = np.zeros_like(_REE)
_mtt, _mee = _R0TT > 0, _R0EE > 0
_FTT[:, _mtt] = _RTT[:, _mtt] / _R0TT[_mtt] - 1.0
_FEE[:, _mee] = _REE[:, _mee] / _R0EE[_mee] - 1.0
_SPL_TT = CubicSpline(_SG, _FTT, axis=0)
_SPL_EE = CubicSpline(_SG, _FEE, axis=0)
_SPL_TE = CubicSpline(_SG, _DTE, axis=0)
_SL_TT, _SL_EE = _SPL_TT(0.0, 1), _SPL_EE(0.0, 1)
_DTE0 = _DTE[0]


def operators_at(sum_ev):
    """(RATIO_TT, RATIO_EE, c_TE) at this sum; below zero each is its own linear continuation"""
    s = float(sum_ev)
    if s >= 0.0:
        return (_R0TT * (1.0 + _SPL_TT(s)), _R0EE * (1.0 + _SPL_EE(s)), _SPL_TE(s))
    return (_R0TT * (1.0 + _SL_TT * s), _R0EE * (1.0 + _SL_EE * s),
            _DTE0 + (_SPL_TE(0.0, 1)) * s)


def _load(arm, tag):
    z = np.load(os.path.join(POL_DIR, f"{ARMS[arm]['pref']}_{tag}.npz"), allow_pickle=True)
    return (np.asarray(z['ls'], float), np.asarray(z['Dl'], float),
            np.asarray(z['Dl_TE'], float), np.asarray(z['Dl_EE'], float))


def _bin_through(ops, ls, tt, te, ee):
    """apply the three operators on the spectrum's own axis and bin the result

    ** TE's correction is a RATIO TO TT and is applied as such **, so the instrument's own TT
    carries it and the free amplitude cancels.
    """
    rtt, ree, cte = ops
    itt = np.interp(ls, _LS_R, rtt)
    iee = np.interp(ls, _LS_R, ree)
    icte = np.interp(ls, _LS_R, cte)
    return SC.bin_three(ls, tt * itt, te + icte * tt, ee * iee)


class Model3:
    """the 555-bin model and its chi^2, as a function of the four offsets and the sum"""

    def __init__(self, arm, blocks=BLOCKS):
        self.arm, self.blocks = arm, tuple(blocks)
        sums = available_sums()
        if len(sums) < 4:
            raise SystemExit(f'only {len(sums)} sum node(s) present for both arms -- not enough')
        if not directions_ready(arm):
            raise SystemExit(f'{arm}: the four directions are not all generated yet')
        rows = []
        for s in sums:
            rows.append(_bin_through(operators_at(s), *_load(arm, _SUM_TAGS[s])))
        rows = np.asarray(rows)
        self.ok = (np.isfinite(rows).all(axis=0) & np.isin(SC.BLOCK, list(self.blocks)))
        self.nb = int(self.ok.sum())
        self.s_lo, self.s_hi = float(sums[0]), float(sums[-1])
        self.base = CubicSpline(np.asarray(sums, float), rows[:, self.ok], axis=0)
        # the four banked directions, binned through the operators at each OPERATOR-grid sum; the
        # directions themselves are at zero sum, which is where they were generated, and that is
        # stated rather than hidden
        raw = {k: {sg: _load(arm, f'{k}{sg}') for sg in ('p', 'm')} for k in KEYS4}
        b0 = {k: None for k in KEYS4}
        g, h = {k: [] for k in KEYS4}, {k: [] for k in KEYS4}
        base0 = _load(arm, _SUM_TAGS[0.00])
        for s in _SG:
            ops = operators_at(float(s))
            b = _bin_through(ops, *base0)[self.ok]
            for k in KEYS4:
                mp = _bin_through(ops, *raw[k]['p'])[self.ok]
                mm = _bin_through(ops, *raw[k]['m'])[self.ok]
                g[k].append((mp - mm) / (2 * R.STEP[k]))
                h[k].append((mp - 2 * b + mm) / R.STEP[k] ** 2)
            b0[k] = b
        self.g = {k: CubicSpline(_SG, np.asarray(g[k]), axis=0) for k in KEYS4}
        self.h = {k: CubicSpline(_SG, np.asarray(h[k]), axis=0) for k in KEYS4}
        self.F = SC.fisher_for(self.ok)
        self.d = SC.X_DATA[self.ok]
        self.pos = SC.POSITIVE[self.ok]
        self._bao, self._bao_spl = {}, None

    # ── the ruler, exactly as r7838 left it ─────────────────────────────────────────────────────
    RD_BOUNDS = (100.0, 220.0)
    RD_BORROWED = (120.0, 170.0)

    def bao_direct(self, H0, OM, bounds=None):
        b = self.RD_BOUNDS if bounds is None else tuple(bounds)
        key = (round(H0, 6), round(OM, 7), b)
        if key not in self._bao:
            r = minimize_scalar(lambda rd: DI.chi2_bao(H0, OM, rd, ARMS[self.arm]['E']),
                                bounds=b, method='bounded')
            self._bao[key] = (float(r.fun), float(r.x))
        return self._bao[key]

    def _build_bao_spline(self, half_steps=6, n_h0=17, n_om=401):
        c = ARMS[self.arm]['centre']
        h0 = np.linspace(c['H0'] - half_steps * R.STEP['H0'],
                         c['H0'] + half_steps * R.STEP['H0'], n_h0)
        om = np.linspace(c['OM'] - half_steps * R.STEP['OM'],
                         c['OM'] + half_steps * R.STEP['OM'], n_om)
        Z = np.empty((n_h0, n_om))
        for i, a in enumerate(h0):
            for j, b in enumerate(om):
                Z[i, j] = self.bao_direct(float(a), float(b))[0]
        self._bao_lo = (float(h0[0]), float(om[0]))
        self._bao_hi = (float(h0[-1]), float(om[-1]))
        self._bao_spl = RectBivariateSpline(h0, om, Z, kx=3, ky=3, s=0)

    def bao_error(self, rng, m=200):
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
        if self._bao_spl is None:
            self._build_bao_spline()
        lo, hi = self._bao_lo, self._bao_hi
        if not (lo[0] <= H0 <= hi[0] and lo[1] <= OM <= hi[1]):
            return self.bao_direct(H0, OM)
        return (float(self._bao_spl(H0, OM)[0, 0]), float('nan'))

    # ── the score ───────────────────────────────────────────────────────────────────────────────
    def binned(self, x4, sum_ev):
        s = float(np.clip(sum_ev, self.s_lo, self.s_hi))
        m = np.asarray(self.base(s), float).copy()
        for k, v in zip(KEYS4, x4):
            m = m + np.asarray(self.g[k](max(s, 0.0)), float) * v \
                  + 0.5 * np.asarray(self.h[k](max(s, 0.0)), float) * v * v
        return m

    def chi2_cmb(self, x4, sum_ev):
        m = self.binned(x4, sum_ev)
        if not np.all(np.isfinite(m)) or np.any(m[self.pos] <= 0):
            return 1e12
        A = float((m @ self.F @ self.d) / (m @ self.F @ m))
        r = self.d - A * m
        return float(r @ self.F @ r)

    def phys(self, x4, sum_ev):
        c = ARMS[self.arm]['centre']
        return dict(H0=c['H0'] + R.STEP['H0'] * x4[0], OM=c['OM'] + R.STEP['OM'] * x4[1],
                    WB=c['WB'] + R.STEP['WB'] * x4[2], NS=c['NS'] + R.STEP['NS'] * x4[3],
                    MNU=float(sum_ev))

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
        """the same chi^2 with the infeasible region SLOPED, for a minimiser -- r7838's own fix,
        after Powell reported a flat penalty plateau as a minimum."""
        x4, s = np.asarray(x5[:4], float), float(x5[4])
        slo = self.s_lo if lo is None else lo
        v = max(0.0, slo - s) + max(0.0, s - self.s_hi) \
            + float(np.sum(np.maximum(0.0, np.abs(x4) - 6.0)))
        if v > 0:
            return 1e6 + 1e6 * v * v
        m = self.binned(x4, s)
        if not np.all(np.isfinite(m)):
            return 1e6
        neg = float(np.sum(np.maximum(0.0, -m[self.pos]) ** 2)) \
            / max(float(np.mean(np.abs(m))) ** 2, 1e-300)
        if neg > 0:
            return 1e6 + 1e6 * neg
        A = float((m @ self.F @ self.d) / (m @ self.F @ m))
        r = self.d - A * m
        p = self.phys(x4, s)
        return float(r @ self.F @ r) + self.chi2_bao(p['H0'], p['OM'])[0]
