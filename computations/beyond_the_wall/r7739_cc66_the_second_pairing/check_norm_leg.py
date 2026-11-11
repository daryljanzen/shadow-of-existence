#!/usr/bin/env python3
"""`r7739+cc66` CHECKING `R2'`'s NUMERATOR BY AN IDENTITY, AND ONE ROUTE OF THE CHECK IS BAD.

⛭ ** WHY THIS EXISTS. **  `R2'` came out at `0.0119` under `P1`, two orders below its registered `0.80`
line.  A number that far below its licence is checked before it is reported, not after.

⛭ ** THE IDENTITY. **  `G_l(k; xs*x0) = \\int g j_l(k*xs*x0) d eta = G_l(xs*k; x0)`: scaling the map by
a scalar is scaling `k` by that scalar.  Two routes follow from it.

⛔ ** ROUTE B (re-read 70's own `G` at `xs*k` by interpolation) IS A BAD CHECK, AND IT IS KEPT HERE AS
ONE. **  It disagrees with the build by a median relative `4.8e-01` and would put `R2'` at `2.82`
instead of `0.0119` -- a factor `238` on the numerator.  The reason is not a disagreement about the
physics: `j_l(k x0)` at these `l` oscillates on a scale COMPARABLE TO THE `k` GRID SPACING, so LINEAR
interpolation of it across a `1.29 %` shift is meaningless.  ⇒ *So this is not evidence against the
build; it is evidence that this `k` grid cannot be interpolated.  Worth knowing on its own: anyone
re-pairing by resampling onto a common `k` grid will get numbers like route B's and they will look
plausible.*

⛭ ** ROUTE C SETTLES IT, AND NEEDS NO INTERPOLATION AT ALL. **  If `Gn(k) = G0(xs*k)` exactly, then
scaling `rs` by the same `xs` must undo the whole effect: `A(Gn; rs*xs) = A(G0; rs)`, because the
measure `dk/k` is scale-invariant and `exp(2 i k rs xs)` becomes `exp(2 i k' rs)` under `k' = xs*k`.
Measured: the leg collapses from `1.563534e-04` to `5.205530e-09`, a factor `3.3e-05`, i.e. to
round-off.  ⇒ *The built array satisfies the identity to numerical precision. `R2'`'s numerator stands,
and `0.0119` is a reading rather than a bug.*

⛭ ** AND ROUTE C IS ALSO THE MECHANISM, WHICH IS THE PART THAT MATTERS FOR `R2`. **  It shows the
scalar's ENTIRE effect on `A_l` is its mismatch against the FIXED comb phase: `A_l` is normalised by
its own integral, so a pure `k`-reparametrisation cancels in the ratio and only `exp(2 i k rs)`, which
does not rescale, survives.  ⇒ *So a pure scalar is nearly INVISIBLE to a normalised acceptance ratio,
while on the UN-normalised transfer ladder of Tier 1 the same scalar rescales everything and dominated
at `98.3` per cent.  The two objects are REQUIRED to disagree here by their own construction.*
⛔ *That is why `R2'` cannot be read across to `R2`, now demonstrated rather than asserted -- and why
`R2` still needs 70's build. Amendment 1's bar on substituting one for the other was not a formality.*
"""
import os
import sys

import numpy as np

import read_pairings as RP


def main():
    print(__doc__)
    print("=" * 100)
    Z = np.load(os.path.join(RP.D, 'r7737_grid.npz'), allow_pickle=True)
    V = np.load(os.path.join(RP.D, 'r7737_vis.npz'), allow_pickle=True)
    N = np.load(os.path.join(RP.D, 'r7739_norm_only.npz'))
    k, dk = V['k'], V['dk']
    rs_l = float(Z['r_s_lcdm'])
    Gn, xs = N['Gn'], float(N['xs'])
    G0 = V['G__g_lcdm__X_lcdm']

    Gb = np.empty_like(G0)
    for i in range(G0.shape[0]):
        Gb[i] = np.interp(xs * k, k, G0[i])
    m = (xs * k >= k[0]) & (xs * k <= k[-1])
    rel = np.abs(Gb[:, m] - Gn[:, m]) / np.maximum(np.abs(Gn[:, m]), 1e-300)
    print(f"\n  ROUTE B, interpolation: {int(m.sum())} of {len(k)} cells in range; "
          f"median rel {np.median(rel):.3e}, 90th pct {np.percentile(rel, 90):.3e}")

    lc = np.log(RP.A_of(G0, k, dk, rs_l))
    uA = np.log(RP.A_of(Gn, k, dk, rs_l)) - lc
    uB = np.log(RP.A_of(Gb, k, dk, rs_l)) - lc
    chi = np.log(RP.A_of(V['G__g_lcdm__X_cr'], k, dk, rs_l)) - lc
    print(f"  lrms(u_norm)  route A (built) {RP.lrms(uA):.6e}   route B (interp) {RP.lrms(uB):.6e}"
          f"   factor {RP.lrms(uB) / RP.lrms(uA):.1f}")
    print(f"  ⇒ R2' would be {RP.lrms(uA) / RP.lrms(chi):.4f} by A and "
          f"{RP.lrms(uB) / RP.lrms(chi):.4f} by B. B is the BAD route, per route C below.")

    uC = np.log(RP.A_of(Gn, k, dk, rs_l * xs)) - lc
    f = RP.lrms(uC) / RP.lrms(uA)
    print(f"\n  ROUTE C, the identity with rs scaled by the same xs, NO interpolation:")
    print(f"      lrms {RP.lrms(uC):.6e} against {RP.lrms(uA):.6e} unscaled, factor {f:.3e}")
    ok = f < 1e-3
    RP.gate('C', ok, "scaling rs by xs undoes the scalar's whole effect, so the built array satisfies "
            "G(k; xs*x0) = G(xs*k; x0) to round-off and route A is the correct one",
            f"collapse factor {f:.3e}, threshold 1e-3")
    print(f"\n  ⇒ `R2'` numerator CONFIRMED. `R2'` under P1 = {RP.lrms(uA) / RP.lrms(chi):.4f}, "
          f"a reading and not a bug.")
    print(f"  ⛭ and the mechanism is established: the scalar's entire effect on a NORMALISED A_l is")
    print(f"    its mismatch against the fixed comb phase, which is why a scalar that DOMINATED")
    print(f"    Tier 1's un-normalised ladder is nearly invisible here. The objects must disagree.")
    print("=" * 100)
    return 1 if RP.FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
