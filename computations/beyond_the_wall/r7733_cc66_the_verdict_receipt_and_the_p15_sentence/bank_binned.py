#!/usr/bin/env python3
"""`r7733+cc66` BANK THE BINNED OBJECT THE VERDICT RESTS ON, so the receipt needs no mutable ref.

** WHY A BANK AND NOT A FETCH. **  70's arrays live at `refs/ci/r7729_dlk`, and `.github/workflows/dlk.yml`
line 85 pushes that ref with `git push -f`.  ⇒ ** The ref is FORCE-PUSHABLE, so it is not an immutable
input **, and a receipt pinned to it would be pinned to something that can change underneath it without
any commit in this repository recording that it did.  The receipt reads this bank instead.

** WHAT IS BANKED, and it is not a digest of the answer. **  The whole computation downstream of the
binning -- the templates, the fit, both nulls, the power -- reads ONLY the four binned cells.  So the
four cells are banked AT BOTH REGISTERED BINNINGS and nothing else is pre-computed: the receipt forms
its own logs, its own templates, its own weights and its own mask.  ⛔ The log transform in particular
is NOT applied here, because the receipt's templates are differences of logs and banking them would be
banking the answer's own inputs.

** AND THE BANK CARRIES ITS OWN CLOSURE, three ways, so the receipt can fail on the bank itself:
  * `T12`/`T23` are the TRUNCATED TAIL sums -- `1450 = 120*12 + 10 = 63*23 + 1` -- so
    `B.sum(axis=1) + T` must return `Mtot` at both binnings, to `1e-13` relative and measured at
    `8e-16`, which is summation reassociation and NOT an identity held exactly; a bin boundary off by
    one node breaks it by of order a whole node's contribution instead;
  * `Mtot` against `Dl`:  `l(l+1) * Mtot == Dl`, 70's own C4 identity recomputed, and THIS one does
    hold exactly -- departure `0.000e+00` on all four cells;
  * `SRC_SHA256` is the sha256 of the 32,508,096-byte source file, recorded here and asserted by the
    receipt against the figure 70's `closure.json` carries.

SOURCE: `refs/ci/r7729_dlk:r7729_dlk_four.npz`, fetched per `.github/workflows/dlk.yml` line 86.
  sha256 3fbad4d34030cf0ee36e43ccbe30dc630039996d9a5cfa6316fd85917760ccb9  (32508096 bytes)
"""
import hashlib
import os
import sys

import numpy as np

CELLS = ('S_lcdm__K_lcdm', 'S_lcdm__K_cr', 'S_cr__K_lcdm', 'S_cr__K_cr')
SRC_SHA256 = '3fbad4d34030cf0ee36e43ccbe30dc630039996d9a5cfa6316fd85917760ccb9'
SRC_BYTES = 32508096
WIDTHS = {'12': 12, '23': 23}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r7733_binned.npz')


def main(src):
    h = hashlib.sha256(open(src, 'rb').read()).hexdigest()
    n = os.path.getsize(src)
    print(f"  source {src}\n    sha256 {h}\n    bytes  {n}")
    if h != SRC_SHA256 or n != SRC_BYTES:
        print(f"  ⛔ REFUSING: this is not the banked object ({SRC_SHA256}, {SRC_BYTES} bytes)")
        return 1

    z = np.load(src, allow_pickle=True)
    M = {c: z[f'P__{c}'][None, :] * z[f'Dlk__{c}'] ** 2 for c in CELLS}
    ls = z['ls']
    d = {'ls': ls, 'k_nodes': np.array([z['k'].shape[0]]),
         'src_sha256': np.array([SRC_SHA256]), 'src_bytes': np.array([SRC_BYTES])}
    for c in CELLS:
        d[f'Mtot__{c}'] = M[c].sum(axis=1)
        d[f'Dl__{c}'] = z[f'Dl__{c}']
        for tag, w in WIDTHS.items():
            nb = M[c].shape[1] // w
            d[f'B{tag}__{c}'] = M[c][:, :nb * w].reshape(M[c].shape[0], nb, w).sum(axis=2)
            d[f'T{tag}__{c}'] = M[c][:, nb * w:].sum(axis=1)

    # the three closures, HERE as well as in the receipt, so a bad bank is never written
    bad = []
    for c in CELLS:
        for tag in WIDTHS:
            r = np.abs(d[f'B{tag}__{c}'].sum(axis=1) + d[f'T{tag}__{c}'] - d[f'Mtot__{c}'])
            rel = float((r / np.abs(d[f'Mtot__{c}'])).max())
            print(f"    {c:17s} B{tag}+T vs Mtot   max rel {rel:.3e}")
            if rel > 1e-13:
                bad.append(f'{c}/B{tag}')
        rel = float((np.abs(ls * (ls + 1) * d[f'Mtot__{c}'] - d[f'Dl__{c}'])
                     / np.abs(d[f'Dl__{c}'])).max())
        print(f"    {c:17s} l(l+1)*Mtot vs Dl   max rel {rel:.3e}")
        if rel > 1e-13:
            bad.append(f'{c}/Dl')
    if bad:
        print(f"  ⛔ REFUSING to write the bank: {', '.join(bad)}")
        return 1

    np.savez_compressed(OUT, **d)
    print(f"\n  banked {OUT}  ({os.path.getsize(OUT)} bytes)")
    print(f"    sha256 {hashlib.sha256(open(OUT, 'rb').read()).hexdigest()}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
