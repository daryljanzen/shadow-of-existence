"""r7838+60: WHAT THE MOVING OPERATOR CHANGES, AND WHICH WAY -- measured, before the fit is read.

r7836 reported its control's 95 per cent limit as too TIGHT by a factor 2.42 and named the frozen
lensing operator as the cause, reasoning that a fit which keeps the omega_cb lever and drops the
lensing signature reports a limit that is too tight.  That reasoning has a direction in it, and a
direction is checkable.  This file checks it: the same 185-bin chi^2 at each generated sum, once
with the operator formed AT that sum and once with it frozen where the borrowed harness freezes it,
at the grid centre so that nothing else moves.

  ** If freezing the operator LOWERS chi^2 at large sums, the frozen harness prefers large sums
     MORE than the honest one does, and its limit is too LOOSE on that account -- the opposite of
     what r7836 named.  Then whatever made r7836's limit too tight is somewhere else. **

Also written: the leave-one-out interpolation error of the sum direction, and the off-grid check
against a spectrum generated at a sum that is no node, which is what the registration names.

Writes operator_effect.json.  rc=0 on success.  Run: python3 operator_effect.py   (numpy, scipy)
"""
import json
import os
import sys

import numpy as np
import scipy.linalg
from scipy.interpolate import CubicSpline

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as M                                                          # noqa: E402
import chi2_of_spectrum as CS                                              # noqa: E402

FROZEN_AT = 0.06                     # where `r7749_70_leafgeom_refit/refit.py` freezes it
OFFGRID = 0.21                       # a sum that is no node of the model's own grid
OUT = os.path.join(HERE, 'operator_effect.json')


def rows_for(arm, ratio_fn):
    sums = sorted(M.SPEC)
    out = []
    for s in sums:
        ls, Dl = M._spec(arm, s)
        out.append(M._bin_with(ratio_fn(s), ls, Dl))
    return np.asarray(sums, float), np.asarray(out)


def main():
    res = {}
    rfix = M.ratio_at(FROZEN_AT)
    for arm in ('lcdm', 'cr'):
        try:
            sums, A = rows_for(arm, M.ratio_at)
            _, B = rows_for(arm, lambda s: rfix)
        except FileNotFoundError as e:
            print(f'  {arm}: not all spectra present yet ({e.filename}) -- skipped', flush=True)
            continue
        ok = np.isfinite(A).all(axis=0) & np.isfinite(B).all(axis=0)
        F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(ok, ok)]),
                                   np.identity(int(ok.sum())))
        F = 0.5 * (F + F.T)
        d = CS.X_DATA[ok]
        sig = np.sqrt(np.diag(CS.COV_TT[np.ix_(ok, ok)]))

        def chi2(m):
            a = float((m @ F @ d) / (m @ F @ m))
            r = d - a * m
            return float(r @ F @ r)

        per_sum = {}
        for i, s in enumerate(sums):
            cm, cf = chi2(A[i][ok]), chi2(B[i][ok])
            b2 = B[i][ok] * float((A[i][ok] @ B[i][ok]) / (B[i][ok] @ B[i][ok]))
            per_sum[f'{s:+.2f}'] = dict(moving=cm, frozen=cf, difference=cm - cf,
                                        shape_pct=float(100.0 * np.max(np.abs(A[i][ok] / b2 - 1.0))))
            print(f'    {arm} Sum={s:+.2f}: chi2 moving {cm:.3f}, frozen {cf:.3f}, '
                  f'difference {cm - cf:+.3f}   (shape {per_sum[f"{s:+.2f}"]["shape_pct"]:.4f} '
                  f'per cent)', flush=True)
        # the leave-one-out error of the interpolation the sampler rides
        R = A[:, ok]
        loo = {}
        for j in range(1, len(sums) - 1):
            keep = [i for i in range(len(sums)) if i != j]
            sp = CubicSpline(sums[keep], R[keep], axis=0)
            e = np.abs(np.asarray(sp(sums[j]), float) - R[j]) / sig
            loo[f'{sums[j]:+.2f}'] = dict(max_over_sigma=float(e.max()),
                                          median_over_sigma=float(np.median(e)))
        # the off-grid check, which is what the registration names literally
        off = None
        p = os.path.join(M.NEW_DIR, f"{M.ARMS[arm]['pref']}_S021.npz")
        if os.path.exists(p):
            z = np.load(p)
            exact = M._bin_with(M.ratio_at(OFFGRID), np.asarray(z['ls'], float),
                                np.asarray(z['Dl'], float))[ok]
            sp = CubicSpline(sums, R, axis=0)
            e = np.abs(np.asarray(sp(OFFGRID), float) - exact) / sig
            off = dict(sum_ev=OFFGRID, max_over_sigma=float(e.max()),
                       median_over_sigma=float(np.median(e)))
            print(f'    {arm} OFF-GRID at Sum={OFFGRID}: max |interpolated - rebuilt| / sigma = '
                  f'{e.max():.6f}', flush=True)
        else:
            print(f'    {arm} OFF-GRID at Sum={OFFGRID}: spectrum not generated yet', flush=True)
        res[arm] = dict(frozen_at=FROZEN_AT, bins=int(ok.sum()), per_sum=per_sum,
                        leave_one_out=loo, off_grid=off)
    old = json.load(open(OUT)) if os.path.exists(OUT) else {}
    old.update(res)
    json.dump(old, open(OUT, 'w'), indent=1)
    print(f'\n  wrote {os.path.relpath(OUT, HERE)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
