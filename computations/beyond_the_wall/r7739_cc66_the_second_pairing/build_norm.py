#!/usr/bin/env python3
"""`r7739+cc66` THE SCALAR-ONLY MAP, which `R2`'s SUBSTITUTE needs and `R2` ITSELF CANNOT USE.

⛔ ** `R2` AS REGISTERED IS NOT COMPUTABLE FROM THE ARTEFACTS IN HAND, AND THIS FILE IS NOT IT. **
`R2` asks for Tier 1's `R_shape` and the normalisation's share of the distance leg **recomputed under
`P2`**.  Tier 1's distance leg is `u_map = log B[S_lcdm__X_cr] - log B[S_lcdm__X_lcdm]`, built from
`r7737_xmap`'s `Dlk__S_{a}__X_{b}`.  Borrowing one arm's `chi` map onto the other arm's SOURCE is a
pairing, and `70` did it by index, so rebuilding it under `P2` needs the transfer source `S_lcdm(eta)`
on `lcdm`'s own `eta` grid.  **No handed-over artefact carries it.**  `r7737_xmap` carries only the
OUTPUTS (`Dlk`, `P`, `Dl`); `r7737_grid` carries `eta`, `x0` and the VISIBILITY `vis_{arm}`, which is a
different object from the transfer source; and the `r7729` blob carries no `eta` or `x0` at all, which
is why `r7737`'s own `S1` was already recorded NOT COMPUTABLE for the same reason.
⇒ *So `R2` is reported NOT COMPUTABLE, with the one thing that would compute it: `70` re-running its
`xmap` build with the rescaled `chi` map. I do not approximate it and I do not quietly drop it.*

⛭ ** WHAT THIS BUILDS IS A DECLARED SUBSTITUTE ON A DIFFERENT OBJECT. **  The same split -- a pure
scalar normalisation against a shape remainder -- is computable on the ACCEPTANCE arm, where I do hold
every input.  The normalisation-only map is `x0_lcdm * xs` with `xs = D_M_cr / D_M_lcdm`: a pure scalar
multiply, which is `r7729`'s own definition of the normalisation term and needs no pivot.
⛔ *It answers `R2`'s QUESTION (is the normalisation's share pairing-robust) on the acceptance objects,
NOT `R2`. It is named separately in the verdict and never reported as `R2` discharged.*
"""
import os
import sys
import time

import numpy as np

import read_pairings as RP


def main():
    Z = np.load(os.path.join(RP.D, 'r7737_grid.npz'), allow_pickle=True)
    V = np.load(os.path.join(RP.D, 'r7737_vis.npz'), allow_pickle=True)
    ls, k = V['ls'], V['k']
    xs = float(Z['D_M_cr']) / float(Z['D_M_lcdm'])
    print(__doc__)
    print(f"  xs = D_M_cr / D_M_lcdm = {xs:.10f}")
    t0 = time.time()
    Gn = RP.build_G(Z['vis_lcdm'], Z['eta_lcdm'], xs * Z['x0_lcdm'], ls, k)
    print(f"  Gn built, {time.time() - t0:.0f} s", flush=True)
    out = os.path.join(RP.D, 'r7739_norm_only.npz')
    np.savez_compressed(out, Gn=Gn, xs=xs)
    print(f"  saved {out}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
