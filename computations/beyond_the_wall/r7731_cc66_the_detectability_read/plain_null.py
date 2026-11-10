#!/usr/bin/env python3
"""`r7731+cc66.5` the SECONDARY null construction, which §3 registers and `four_cell.py` did not run.

⛔ `PREDICTION_detectability.md` §3 registers TWO null constructions -- PRIMARY (row-and-column
normalised) and SECONDARY (plain 2D phase randomisation) -- and says "both are reported; a disagreement
between them IS the verdict".  `four_cell.py` called the surrogate with `normalise=True` only, so it met
half of that.  ⌗ *Caught by re-reading my own §3 against what the script did, not by the result.*

⚠ Note the word "secondary" carries TWO axes in this registration: §3's secondary NULL CONSTRUCTION and
amendment 5's secondary BINNING.  They are independent, and this runs the plain null on BOTH binnings.
"""
import sys

import numpy as np

sys.path.insert(0, '.')
from four_cell import BLOB, BINS, ALPHA, N_NULL, SEED, binned, fit2, surrogate  # noqa: E402


def main():
    z = np.load(BLOB, allow_pickle=True)
    C = ('S_lcdm__K_lcdm', 'S_lcdm__K_cr', 'S_cr__K_lcdm', 'S_cr__K_cr')
    M = {c: z[f'P__{c}'][None, :] * z[f'Dlk__{c}'] ** 2 for c in C}
    print(f"\n  ⛭ `r7731+cc66.5` the SECONDARY (plain) null, {N_NULL} draws, both binnings\n")
    cells = {}
    for name, w in BINS.items():
        B = {c: binned(M[c], w) for c in C}
        dead = np.zeros(B[C[0]].shape, bool)
        for c in C:
            dead |= B[c] <= 0
        with np.errstate(divide='ignore'):
            lb = {c: np.where(dead, 0.0, np.log(np.where(B[c] > 0, B[c], 1.0))) for c in C}
        tk = lb['S_lcdm__K_cr'] - lb['S_lcdm__K_lcdm']
        ts = lb['S_cr__K_lcdm'] - lb['S_lcdm__K_lcdm']
        obs = lb['S_cr__K_cr'] - lb['S_lcdm__K_lcdm']
        W = np.where(dead, 0.0, B['S_lcdm__K_lcdm'] / B['S_lcdm__K_lcdm'].sum(axis=1, keepdims=True))
        a_ker, a_src = fit2(obs, tk, ts, W)
        resid = obs - (a_ker * tk + a_src * ts)
        rng = np.random.default_rng(SEED)
        nk, ns_ = np.empty(N_NULL), np.empty(N_NULL)
        for i in range(N_NULL):
            nk[i], ns_[i] = fit2(surrogate(resid, rng, False), tk, ts, W)   # ⛭ PLAIN: normalise=False
        lo_k, hi_k = np.quantile(nk, [ALPHA / 2, 1 - ALPHA / 2])
        lo_s, hi_s = np.quantile(ns_, [ALPHA / 2, 1 - ALPHA / 2])
        k_ = abs(a_ker) > max(abs(lo_k), abs(hi_k))
        s_ = abs(a_src) > max(abs(lo_s), abs(hi_s))
        v = ('the projection CREATES it' if k_ and not s_ else
             'the projection FAILS TO CANCEL it' if s_ and not k_ else
             'BOTH CONTRIBUTE' if k_ and s_ else 'NEITHER -- the plane does not decide')
        cells[name] = v
        print(f"    {name:10s} ({B[C[0]].shape[1]:3d} bins)  a_ker {a_ker:+.4f} vs null 99% "
              f"[{lo_k:+.4f}, {hi_k:+.4f}] | a_src {a_src:+.4f} vs [{lo_s:+.4f}, {hi_s:+.4f}]"
              f"\n                           =>  {v}")
    ok = len(set(cells.values())) == 1
    print(f"\n    [{'PASS' if ok else 'FAIL'}] the plain null agrees with itself across binnings")
    print(f"\n  ⇒ §3's rule: both null constructions are reported, and a disagreement between them IS\n"
          f"    the verdict.  The PRIMARY (normalised) null returned BOTH CONTRIBUTE on both binnings;\n"
          f"    the PLAIN null returns: {' / '.join(f'{k} {v}' for k, v in cells.items())}\n")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
