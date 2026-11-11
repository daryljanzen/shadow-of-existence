#!/usr/bin/env python3
"""`r7739+cc66` `R2'` — THE DECLARED SUBSTITUTE, read under `P1` AND every `P2` span variant.

⛔ ** THIS IS NOT `R2`. **  `PREDICTION.md` Amendment 1 records `R2` as NOT COMPUTABLE from the handed-
over artefacts: it needs the transfer source `S_lcdm(eta)` to rebuild Tier 1's borrowed `chi` map under
`P2`, and no artefact carries it.  `R2'` is the SAME SPLIT -- a pure scalar normalisation against a shape
remainder -- on the ACCEPTANCE arm, where every input is in hand.  It licenses nothing about Tier 1's
`98.3` per cent and is never reported as `R2` discharged.

⛭ ** THE NUMERATOR IS PAIRING-FREE BY CONSTRUCTION, AND THAT IS THE POINT. **  The normalisation-only
map is `x0_lcdm * xs`, a pure scalar multiply of `lcdm`'s OWN map: nothing is borrowed, so no pairing
enters it.  ⇒ *So `R2'` moves across pairings ONLY through its denominator, the `chi` leg.  A spread of
`R2'` across the variants is therefore a statement about the `chi` leg alone, not about the
normalisation -- and that is exactly what makes the ratio readable here.*

⛭ The registered line is `0.80`, from Amendment 1:  `>= 0.80` under EVERY pairing confirms the reasoning
on these objects;  `< 0.80` under ANY pairing says it was wrong there, with the number and the pairing.
"""
import os
import sys

import numpy as np

import read_pairings as RP

VARIANT_FILES = {'grid span': 'r7739_P2_grid_span.npz',
                 'sigma (mine)': 'r7739_P2_sigma_(mine).npz',
                 "70's W": 'r7739_P2_70s_W.npz'}


def main():
    print(__doc__)
    print("=" * 100)
    Z = np.load(os.path.join(RP.D, 'r7737_grid.npz'), allow_pickle=True)
    V = np.load(os.path.join(RP.D, 'r7737_vis.npz'), allow_pickle=True)
    k, dk = V['k'], V['dk']
    rs_l, rs_c = float(Z['r_s_lcdm']), float(Z['r_s_cr'])
    nf = os.path.join(RP.D, 'r7739_norm_only.npz')
    if not os.path.exists(nf):
        print(f"  ⛔ {nf} absent -- `build_norm.py` has not finished. Nothing is reported.")
        return 1
    N = np.load(nf)
    Gn, xs = N['Gn'], float(N['xs'])
    print(f"\n  the scalar-only map used `x0_lcdm * xs`, xs = {xs:.10f}")

    lc = np.log(RP.A_of(V['G__g_lcdm__X_lcdm'], k, dk, rs_l))
    u_norm = np.log(RP.A_of(Gn, k, dk, rs_l)) - lc
    n_rms = RP.lrms(u_norm)
    print(f"  the normalisation leg, pairing-free: l-structured rms {n_rms:.6e}")

    legs = {'P1 (70, index)': np.log(RP.A_of(V['G__g_lcdm__X_cr'], k, dk, rs_l)) - lc}
    for name, f in VARIANT_FILES.items():
        p = os.path.join(RP.D, f)
        if os.path.exists(p):
            legs[f'P2 / {name}'] = np.log(RP.A_of(np.load(p)['Gx'], k, dk, rs_l)) - lc
        else:
            print(f"  ⌗ P2 / {name}: {f} absent, variant NOT read (absent, not passed)")

    print(f"\n  ⛭ `R2'` = lrms(normalisation) / lrms(chi leg), the registered line {RP.R2_LINE}")
    vals = {}
    for tag, u in legs.items():
        d = RP.lrms(u)
        vals[tag] = n_rms / d
        print(f"      {tag:22s} chi leg rms {d:.6e}   R2' {n_rms / d:.4f}   "
              f"{'>= line' if n_rms / d >= RP.R2_LINE else 'BELOW line'}")
    print("\n" + "=" * 100)
    if len(legs) < 4:
        print(f"  ⛔ only {len(legs)} of 4 pairings read; the verdict below is PARTIAL and says so.")
    if all(v >= RP.R2_LINE for v in vals.values()):
        print(f"  ⇒ `R2'` ROW ONE: >= {RP.R2_LINE} under every pairing READ. The normalisation dominates")
        print(f"    the chi leg ON THE ACCEPTANCE OBJECTS. This says NOTHING about Tier 1's 98.3 per cent.")
    else:
        lo = min(vals, key=vals.get)
        print(f"  ⛔ `R2'` ROW TWO: {vals[lo]:.4f} under {lo}, below {RP.R2_LINE}.")
        print(f"     The reasoning I declined to report at `r7739+cc66.0` was WRONG on these objects,")
        print(f"     and the number is {vals[lo]:.4f}. Said plainly, as the licence requires.")
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
