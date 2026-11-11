#!/usr/bin/env python3
"""`r7735+cc66` AMENDMENT 1's `M1b` AND `M4`, registered and pushed at `r7735+cc66.1` before this ran.

`M1b` -- the wavenumber shift at the BINNED resolution amendment 1 says SS3's words name.
`M4`  -- the MULTIPOLE shift, which holds the source still, unbinned and binned.

⛔ Licences are amendment 1's: `M1b <= 0.10`, `M4 <= 0.30`, and `M4 > 0.30` licenses NOTHING and
leaves the characterisation open pending Tier 1.  Neither number is moved after the run.
"""
import hashlib
import json
import sys

import numpy as np
from scipy.interpolate import CubicSpline

from which_term import BLOB, CELLS, SRC_SHA256, WIDTH, wrms

M1B_LICENCE = 0.10
M4_LICENCE = 0.30


def binned(X):
    n = X.shape[1] // WIDTH
    return X[:, :n * WIDTH].reshape(X.shape[0], n, WIDTH).sum(axis=2)


def main():
    print(__doc__)
    print("=" * 100)
    h = hashlib.sha256(open(BLOB, 'rb').read()).hexdigest()
    if h != SRC_SHA256:
        print(f"  ⛔ REFUSING: input sha256 {h} is not the banked object")
        return 1
    print(f"    input sha256 {h}  ✔")
    z = np.load(BLOB, allow_pickle=True)
    meta = z['meta'].item()
    while isinstance(meta, str):
        meta = json.loads(meta)
    XS = meta['closure']['grid']['xs']['S_lcdm__K_cr']
    k, ls = z['k'], z['ls']
    print(f"    xs = {XS!r};  ladder {k.size} nodes, window l {ls[0]}-{ls[-1]} ({ls.size})")

    P = z['P__S_lcdm__K_lcdm']
    D0 = np.abs(z['Dlk__S_lcdm__K_lcdm'])
    Dx = np.abs(z['Dlk__S_lcdm__K_cr'])
    M0 = P[None, :] * D0 ** 2
    Mx = P[None, :] * Dx ** 2

    # ---- the weights and the measured template, both binned exactly as r7733's fit forms them ----
    Bc = {c: binned(z[f'P__{c}'][None, :] * z[f'Dlk__{c}'] ** 2) for c in CELLS}
    dead = np.zeros(Bc[CELLS[0]].shape, bool)
    for c in CELLS:
        dead |= Bc[c] <= 0
    W = Bc['S_lcdm__K_lcdm'] / Bc['S_lcdm__K_lcdm'].sum(axis=1, keepdims=True)
    W = np.where(dead, 0.0, W)
    with np.errstate(divide='ignore'):
        lbx = np.where(dead, 0.0, np.log(np.where(Bc['S_lcdm__K_cr'] > 0,
                                                  Bc['S_lcdm__K_cr'], 1.0)))
        lb0 = np.where(dead, 0.0, np.log(np.where(Bc['S_lcdm__K_lcdm'] > 0,
                                                  Bc['S_lcdm__K_lcdm'], 1.0)))
    t_ker_b = lbx - lb0

    # the unbinned arena, as `which_term.py` built it
    with np.errstate(divide='ignore'):
        lg0 = np.where(D0 > 0, 2.0 * np.log(np.where(D0 > 0, D0, 1.0)), np.nan)
        t_ker_u = np.where((Dx > 0) & (D0 > 0),
                           2.0 * np.log(np.where(Dx > 0, Dx, 1.0)) - lg0, np.nan)
    nb = M0.shape[1] // WIDTH
    Wn = np.zeros(M0.shape)
    Wn[:, :nb * WIDTH] = np.repeat(W / WIDTH, WIDTH, axis=1)

    def report(tag, t_pred_u, M_pred, licence, note):
        live = np.isfinite(t_pred_u) & np.isfinite(t_ker_u)
        Wl = np.where(live, Wn, 0.0)
        num_u = wrms(np.where(live, t_ker_u - t_pred_u, 0.0), Wl)
        den_u = wrms(np.where(live, t_ker_u, 0.0), Wl)
        ok_b = M_pred is not None
        if ok_b:
            Bp = binned(np.where(np.isfinite(M_pred), M_pred, 0.0))
            bad = dead | (Bp <= 0)
            with np.errstate(divide='ignore'):
                t_pred_b = np.where(bad, 0.0, np.log(np.where(Bp > 0, Bp, 1.0)) - lb0)
            Wb = np.where(bad, 0.0, W)
            num_b, den_b = wrms(t_ker_b - t_pred_b, Wb), wrms(t_ker_b, Wb)
        print(f"\n    ⛭ {tag}   {note}")
        print(f"         unbinned  live {int(live.sum())} of {live.size};  "
              f"wrms(t_ker) {den_u:.5f}  wrms(diff) {num_u:.5f}  ⇒ {num_u / den_u:.4f}")
        if ok_b:
            print(f"         binned    live bins {int((Wb > 0).sum())} of {Wb.size};  "
                  f"wrms(t_ker) {den_b:.5f}  wrms(diff) {num_b:.5f}  ⇒ {num_b / den_b:.4f}")
        v = max(num_u / den_u, num_b / den_b) if ok_b else num_u / den_u
        print(f"         ⇒ against the registered licence {licence:.2f}: "
              f"{'WITHIN on both readings' if v <= licence else 'OVER'}")
        return (num_u / den_u, num_b / den_b if ok_b else None)

    # ---------------------------------------------------------------- M1b, the wavenumber shift
    lk = np.log(k)
    inside_k = (XS * k >= k[0]) & (XS * k <= k[-1])
    sh_lg = np.full(D0.shape, np.nan)
    sh_D2 = np.full(D0.shape, np.nan)
    for i in range(D0.shape[0]):
        good = np.isfinite(lg0[i])
        if good.sum() < 8:
            continue
        cs = CubicSpline(lk[good], lg0[i][good])
        tgt = inside_k & good
        sh_lg[i, tgt] = cs(np.log(XS * k[tgt]))
        sh_D2[i, tgt] = np.exp(sh_lg[i, tgt])
    M1b = report('M1 / M1b  (shift in WAVENUMBER)', sh_lg - lg0, P[None, :] * sh_D2, M1B_LICENCE,
                 'the model that moves the source as well as the Bessel factor')

    # ---------------------------------------------------------------- M4, the multipole shift
    lsf = ls.astype(float)
    tgt_l = lsf / XS
    inside_l = (tgt_l >= lsf[0]) & (tgt_l <= lsf[-1])
    sl_lg = np.full(D0.shape, np.nan)
    sl_D2 = np.full(D0.shape, np.nan)
    for j in range(D0.shape[1]):
        good = np.isfinite(lg0[:, j])
        if good.sum() < 8:
            continue
        cs = CubicSpline(lsf[good], lg0[good, j])
        tgt = inside_l & good
        sl_lg[tgt, j] = cs(tgt_l[tgt])
        sl_D2[tgt, j] = np.exp(sl_lg[tgt, j])
    print(f"\n    (multipole targets inside the window: {int(inside_l.sum())} of {ls.size}; "
          f"{int((~inside_l).sum())} rows dropped)")
    M4 = report('M4        (shift in MULTIPOLE)', sl_lg - lg0, P[None, :] * sl_D2, M4_LICENCE,
                'the model that holds the source still and moves only the Bessel factor')

    print("\n" + "=" * 100)
    v4 = max(M4[0], M4[1])
    if v4 <= M4_LICENCE:
        print("  ⇒ M4 WITHIN its licence: the kernel leg acts by sliding the kernel's")
        print("    multipole-wavenumber mapping against the source's comb -- the distance, nothing else.")
    else:
        print("  ⛔ M4 OVER its licence.  Amendment 1 registered that this licenses NOTHING:")
        print("     neither one-parameter picture describes the cross term on these arrays, and the")
        print("     CHARACTERISATION IS LEFT OPEN pending Tier 1.  §1, §4's price and the routing are")
        print("     untouched -- they rest on the code reading, not on M1 or M4.")
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
