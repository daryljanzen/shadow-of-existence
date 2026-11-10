#!/usr/bin/env python3
"""`r7735+cc66` THE REGISTERED CONSEQUENCES OF SS1's CODE READING -- M1, M2, M3.

⛭ `PREDICTION.md` SS3, registered and pushed at `r7735+cc66.0` BEFORE this file existed.  Nothing here
is chosen after a result: M1's statistic, its interpolation, its licence in both directions, M2's two
closures and their tolerance, and M3's arithmetic are all in that commit.

⛔ ** THIS READS THE 32 MB BLOB, NOT THE COMMITTED BANK. **  M1 needs the UNBINNED `Dlk` on the ladder
and the ladder's own `k` nodes, neither of which `r7733`'s bank carries -- it banks the binned cells,
which is all `r7731`'s verdict needed.  The blob's sha256 is asserted below, so the input is pinned
even though it is not committed; `r7735` asks for a registration, a price and a routed request, NOT a
receipt, so no bank is minted here.  *If 69 later orders a receipt for this, the bank question returns
and the answer is the same as `r7733`'s: bank what the gates need and record the digest.*
"""
import hashlib
import json
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline

BLOB = ('/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/'
        'scratchpad/dlk/r7729_dlk_four.npz')
SRC_SHA256 = '3fbad4d34030cf0ee36e43ccbe30dc630039996d9a5cfa6316fd85917760ccb9'
CELLS = ('S_lcdm__K_lcdm', 'S_lcdm__K_cr', 'S_cr__K_lcdm', 'S_cr__K_cr')
WIDTH = 12            # the PRIMARY binning, amendment 5
M1_LICENCE = 0.10     # registered, in BOTH directions
TOL_ID = 1e-12        # registered for M2's closures
CHI_EXTENT = 15.5     # P15 l.1823ff, the arms' measured difference in per cent
FAILS = []


def gate(tag, ok, text, witness=''):
    print(f"    [{'PASS' if ok else 'FAIL'}] {tag}  {text}")
    if witness:
        print(f"             {witness}")
    if not ok:
        FAILS.append(tag)
    return ok


def wrms(X, W):
    return float(np.sqrt((W * X ** 2).sum() / W.sum()))


def main():
    print(__doc__)
    print("=" * 100)
    h = hashlib.sha256(open(BLOB, 'rb').read()).hexdigest()
    gate('input', h == SRC_SHA256, "the blob is the object 70 built, by its own sha256", h)
    if FAILS:
        print("  ⛔ REFUSING: nothing is computed on an input that is not the banked one")
        return 1
    z = np.load(BLOB, allow_pickle=True)
    meta = z['meta'].item()
    while isinstance(meta, str):          # the blob stores it JSON-encoded, and doubly so
        meta = json.loads(meta)
    # ⛔ NOT meta['grid'], which is a PROSE string naming the grid; the scalars live under
    #    meta['closure']['grid']['xs'] -- two keys spelled the same at different depths.
    xs = meta['closure']['grid']['xs']
    k = z['k']
    ls = z['ls']

    # ---------------------------------------------------------------- M2, first closure
    a, b = xs['S_lcdm__K_cr'], xs['S_cr__K_lcdm']
    gate('M2a', abs(a * b - 1.0) <= TOL_ID,
         "the two cross terms' scalars are EXACT INVERSES -- the signature of a one-parameter family",
         f"{a!r} * {b!r} = {a * b!r}  (departure {abs(a * b - 1.0):.3e}, tolerance {TOL_ID:.0e})")

    # ---------------------------------------------------------------- the binned arena, as r7733's
    M = {c: z[f'P__{c}'][None, :] * z[f'Dlk__{c}'] ** 2 for c in CELLS}
    nb = M[CELLS[0]].shape[1] // WIDTH
    B = {c: M[c][:, :nb * WIDTH].reshape(M[c].shape[0], nb, WIDTH).sum(axis=2) for c in CELLS}
    dead = np.zeros(B[CELLS[0]].shape, bool)
    for c in CELLS:
        dead |= B[c] <= 0
    lb = {c: np.where(dead, 0.0, np.log(np.where(B[c] > 0, B[c], 1.0))) for c in CELLS}
    t_ker = lb['S_lcdm__K_cr'] - lb['S_lcdm__K_lcdm']
    t_src = lb['S_cr__K_lcdm'] - lb['S_lcdm__K_lcdm']
    obs = lb['S_cr__K_cr'] - lb['S_lcdm__K_lcdm']
    t_ker_cr = lb['S_cr__K_lcdm'] - lb['S_cr__K_cr']
    W = B['S_lcdm__K_lcdm'] / B['S_lcdm__K_lcdm'].sum(axis=1, keepdims=True)
    W = np.where(dead, 0.0, W)

    # ---------------------------------------------------------------- M2, second closure
    lhs = obs - (t_ker + t_src)
    rhs = -(t_ker + t_ker_cr)
    scale = max(wrms(lhs, W), 1e-300)
    rel = wrms(lhs - rhs, W) / scale
    gate('M2b', rel <= TOL_ID,
         "the identity: the unit-coefficient residual IS minus the sum of the two source arms' "
         "kernel templates",
         f"relative departure {rel:.3e} (tolerance {TOL_ID:.0e});  so r7733's residual ratio "
         f"{wrms(lhs, W) / wrms(obs, W):.4f} IS the two templates' departure from exact antisymmetry")

    # ---------------------------------------------------------------- M1, the registered measurement
    # ⛭ the UNBINNED log of the diagonal, read at xs*k by cubic spline in log k, per l row.
    #   Registered: cubic spline in log k per l; cells whose shifted node leaves the ladder are
    #   DROPPED and COUNTED.
    XS = xs['S_lcdm__K_cr']
    D0 = np.abs(z['Dlk__S_lcdm__K_lcdm'])
    with np.errstate(divide='ignore'):
        lg0 = np.where(D0 > 0, 2.0 * np.log(np.where(D0 > 0, D0, 1.0)), np.nan)
    lk = np.log(k)
    inside = (XS * k >= k[0]) & (XS * k <= k[-1])
    shift = np.full(D0.shape, np.nan)
    for i in range(D0.shape[0]):
        row = lg0[i]
        good = np.isfinite(row)
        if good.sum() < 8:
            continue
        cs = CubicSpline(lk[good], row[good])
        tgt = inside & good
        shift[i, tgt] = cs(np.log(XS * k[tgt]))
    t_shift_un = shift - lg0                       # the predicted kernel template, unbinned
    # the measured one, unbinned, on the same cells
    Dx = np.abs(z['Dlk__S_lcdm__K_cr'])
    with np.errstate(divide='ignore'):
        t_ker_un = np.where((Dx > 0) & (D0 > 0),
                            2.0 * np.log(np.where(Dx > 0, Dx, 1.0)) - lg0, np.nan)
    live = np.isfinite(t_shift_un) & np.isfinite(t_ker_un)
    dropped = int((~live).sum())
    # the fit's own weights, spread back over the nodes of each bin (the weight is per bin)
    Wn = np.zeros(D0.shape)
    Wn[:, :nb * WIDTH] = np.repeat(W / WIDTH, WIDTH, axis=1)
    Wl = np.where(live, Wn, 0.0)
    num = wrms(np.where(live, t_ker_un - t_shift_un, 0.0), Wl)
    den = wrms(np.where(live, t_ker_un, 0.0), Wl)
    M1 = num / den
    print(f"\n    ⛭ M1   shift factor xs = {XS!r}")
    print(f"           live cells {int(live.sum())} of {live.size}  (dropped {dropped}: "
          f"{int((~inside).sum() * D0.shape[0])} outside the ladder after the shift, the rest "
          f"underflowed)")
    print(f"           wrms(t_ker) {den:.5f}   wrms(t_ker - t_shift) {num:.5f}   ⇒ M1 = {M1:.4f}")
    gate('M1', M1 <= M1_LICENCE,
         f"the kernel template IS a shift in wavenumber, to the registered {M1_LICENCE:.2f}",
         f"M1 = {M1:.4f} against the licence {M1_LICENCE:.2f}  ⇒ "
         f"{'the projection contribution is the DISTANCE acting through the l-k mapping' if M1 <= M1_LICENCE else 'the cross term carries MORE than a rescaling; SS4 must be re-derived'}")

    # ---------------------------------------------------------------- M3, the arithmetic
    moved = 100.0 * abs(XS - 1.0)
    print(f"\n    ⛭ M3   the kernel index moves the chi-extent by {moved:.3f} per cent;")
    print(f"           the arms' measured chi-extent difference is {CHI_EXTENT} per cent")
    print(f"           ⇒ a factor of {CHI_EXTENT / moved:.2f}: the cross term carries about "
          f"one {round(CHI_EXTENT / moved):d}th of the law's own named mechanism")

    print("\n" + "=" * 100)
    print(f"  {'OK' if not FAILS else '⛔'}  {4 - len(FAILS)} of 4 checks"
          + ("" if not FAILS else f";  FAILED: {', '.join(FAILS)}"))
    print("=" * 100)
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
