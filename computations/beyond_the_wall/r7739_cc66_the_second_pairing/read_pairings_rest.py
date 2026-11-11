#!/usr/bin/env python3
"""`r7739+cc66` THE REMAINING TWO `P2` SPAN VARIANTS, one per process.

⛭ ** WHY THIS FILE EXISTS, AND IT IS NOT A SECOND INSTRUMENT. **  `read_pairings.py` runs `P1` and all
three `P2` span variants in one process.  Each `P2` variant costs TWO full `G` builds at ~30 min each,
so three variants do not fit in one background window: the first run was cut after `P2 / sigma (mine)`
had printed.  ⇒ *This file imports `read_pairings`'s OWN `build_G`, `A_of`, `lrms` and `rescale`
arithmetic unchanged and runs ONE named variant, so the two remaining variants go in parallel on
separate cores.  The arithmetic is identical by import, not by copy.*

⛔ ** `grid span` IS RUN FIRST AND IT IS THE ONE THAT MATTERS. **  The three ratios are 1.060251 (grid),
1.104473 (sigma), 1.155482 (70's `W`), and a LARGER ratio moves MORE of the reading onto `g`.  `sigma`
already gives `g` 72.52 %, so 70's `W`, being larger, cannot fall below it.  The `grid span` is the
SMALLEST and therefore the only variant that could put `g` back under the registered `0.60` line.
⇒ *If `grid span` also gives `g >= 0.60` the convention finding holds across the whole bracket; if it
does not, the reading is span-dependent ON TOP OF pairing-dependent, and that is a different finding.*
⌗ *That monotone expectation is stated so it can be WRONG. It is not a substitute for either run.*

⛭ Each variant also SAVES its two `G` arrays, because `R2` (Tier 1 re-read under `P2`) needs the same
objects and rebuilding them would cost another half hour per variant for arithmetic already done.
"""
import os
import sys
import time

import numpy as np

import read_pairings as RP


def main():
    key = sys.argv[1]
    print(__doc__)
    Z = np.load(os.path.join(RP.D, 'r7737_grid.npz'), allow_pickle=True)
    V = np.load(os.path.join(RP.D, 'r7737_vis.npz'), allow_pickle=True)
    ls, k, dk = V['ls'], V['k'], V['dk']
    arm = {a: dict(eta=Z[f'eta_{a}'], x0=Z[f'x0_{a}'], g=Z[f'vis_{a}'],
                   W=float(Z[f'eta_ls_w_{a}']), rs=float(Z[f'r_s_{a}']),
                   D_M=float(Z[f'D_M_{a}'])) for a in ('lcdm', 'cr')}

    # the three ratios, recomputed here from the same arrays rather than pasted in as figures
    ratios = {'grid span': float(np.ptp(arm['cr']['x0']) / np.ptp(arm['lcdm']['x0'])),
              'sigma (mine)': (RP.wsig(arm['cr']['g'], arm['cr']['eta'], arm['cr']['x0'])
                               / RP.wsig(arm['lcdm']['g'], arm['lcdm']['eta'], arm['lcdm']['x0'])),
              "70's W": arm['cr']['W'] / arm['lcdm']['W']}
    if key not in ratios:
        print(f"  ⛔ unknown variant {key!r}; known: {sorted(ratios)}")
        return 2
    ratio = ratios[key]
    print(f"\n  ⛭ P2 / {key}   ratio {ratio:.6f}")

    def rescale(src, brw, factor_ratio):
        x = arm[brw]['x0']
        piv = x[np.argmax(arm[src]['g'])]
        return piv + (x - piv) / factor_ratio

    t0 = time.time()
    Gg = RP.build_G(arm['cr']['g'], arm['cr']['eta'], rescale('cr', 'lcdm', 1 / ratio), ls, k)
    print(f"      Gg built, {time.time() - t0:.0f} s", flush=True)
    Gx = RP.build_G(arm['lcdm']['g'], arm['lcdm']['eta'], rescale('lcdm', 'cr', ratio), ls, k)
    print(f"      Gx built, {time.time() - t0:.0f} s total", flush=True)

    out = os.path.join(RP.D, f"r7739_P2_{key.replace(' ', '_').replace(chr(39), '')}.npz")
    np.savez_compressed(out, Gg=Gg, Gx=Gx, ratio=ratio)
    print(f"      saved {out}")

    G_P1 = {f'{a}_{b}': V[f'G__g_{a}__X_{b}'] for a in arm for b in arm}
    lc = np.log(RP.A_of(G_P1['lcdm_lcdm'], k, dk, arm['lcdm']['rs']))
    u_g = np.log(RP.A_of(Gg, k, dk, arm['lcdm']['rs'])) - lc
    u_x = np.log(RP.A_of(Gx, k, dk, arm['lcdm']['rs'])) - lc
    u_r = np.log(RP.A_of(G_P1['lcdm_lcdm'], k, dk, arm['cr']['rs'])) - lc
    s = {'visibility g': RP.lrms(u_g), 'distance map chi': RP.lrms(u_x), 'comb period rs': RP.lrms(u_r)}
    tot = sum(s.values())
    print(f"\n      P2 / {key}")
    for n in ('distance map chi', 'visibility g', 'comb period rs'):
        print(f"          {n:18s} l-structured rms {s[n]:.6e}   = {100 * s[n] / tot:6.2f} %")
    print(f"\n      SHARES {key}: chi {s['distance map chi'] / tot:.4f}  "
          f"g {s['visibility g'] / tot:.4f}  rs {s['comb period rs'] / tot:.4f}")
    print(f"      the registered {RP.R1_LINE} line on g: "
          f"{'g >= line' if s['visibility g'] / tot >= RP.R1_LINE else 'g BELOW line'}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
