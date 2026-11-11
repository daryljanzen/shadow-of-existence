#!/usr/bin/env python3
"""`r7739+cc66` THE SECOND PAIRING, READ AS REGISTERED — `S1`, `R1`, `R2`.

⛭ `PREDICTION.md`, registered and pushed at `r7739+cc66.1` BEFORE `refs/ci/r7737_grid` existed.

** THE BUILDER IS 70's, ESTABLISHED AND NOT ASSUMED. **  Rebuilding `G_l(k) = \\int g j_l(k x0) d eta`
from `r7737_grid`'s own arrays reproduces 70's `G__g_{a}__X_{b}` at **`0.000e+00`** relative deviation
on all four combinations, and `A_l` from those `G` at `6e-16` on all eight settings.  ⇒ *So the `P2`
build below is the same arithmetic with one input changed, which is the only thing that makes it
comparable.*

⛔ ** ONE DEFINITION HAD TO BE CHOSEN HERE AND IT IS BRACKETED RATHER THAN PICKED. **  `PREDICTION` §④
says `P2` rescales the borrowed map so its **span over the visibility's support** matches the source
arm's own.  Three candidate spans exist in these arrays and they do not agree:

    the GRID span ................ ratio 1.060251   (and the grid is far wider than the visibility)
    the g-weighted sigma in chi ... ratio 1.104473   (mine: standard, parameter-free, computable)
    70's declared `W` ............ ratio 1.155482   (the number its E4 narrative uses)

and **70's `W` is reproducible from none of them** — not sigma, not 2 sigma, not the FWHM, not the grid
span.  ⇒ *So `P2` is run under ALL THREE scale factors and the verdict is reported under each.  If the
attribution agrees across them it is robust to the definition; if it does not, that is the finding.*
⌗ *And I nearly reported "70's 15.5 % does not match the grid span" as a defect. It does not, but the
grid span is not the span over the support — a statement about one object read as a statement about
another, caught this time before it was written down.*

⌗ ** THE PIVOT ** is the visibility peak, where `x0` is each arm's own `x0_at_peak` — 70's own reported
quantity, and the one point on the map with a name.  So `P2` changes the spread and leaves the distance
to last scattering exactly where `P1` put it.
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.special import spherical_jn

D = ('/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/'
     'scratchpad/tier')
SHA = {'r7737_grid.npz': '546977c4f05f2cffb4299900586f5a6d3ab452f561b13f9272a24bdab7dc7305',
       'r7737_vis.npz': 'c3da5390680d86b2f9dddcae3738a01e88974545b1a5d1ea4c36a2739ceb6ba4'}
R1_LINE = 0.60          # registered
R2_LINE = 0.80          # registered
FAILS = []


def gate(tag, ok, text, witness=''):
    print(f"    [{'PASS' if ok else 'FAIL'}] {tag}  {text}")
    if witness:
        print(f"             {witness}")
    if not ok:
        FAILS.append(tag)
    return ok


def build_G(g, eta, x0, ls, k):
    out = np.empty((len(ls), len(k)))
    arg = k[None, :] * x0[:, None]
    for i, L in enumerate(ls):
        out[i] = np.trapezoid(g[:, None] * spherical_jn(int(L), arg), eta, axis=0)
    return out


def A_of(G, k, dk, rs):
    Wl = G ** 2 * dk[None, :] / k[None, :]
    return np.abs((Wl * np.exp(2j * k[None, :] * rs)).sum(axis=1)) / Wl.sum(axis=1)


def wsig(g, eta, x):
    n = np.trapezoid(g, eta)
    xb = np.trapezoid(g * x, eta) / n
    return float(np.sqrt(np.trapezoid(g * (x - xb) ** 2, eta) / n))


def lrms(x):
    return float(np.sqrt(((x - x.mean()) ** 2).mean()))


def main():
    print(__doc__)
    print("=" * 100)
    for f, s in SHA.items():
        h = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
        gate('input', h == s, f"{f} is the object 70 recorded", h)
    if FAILS:
        return 1
    Z = np.load(os.path.join(D, 'r7737_grid.npz'), allow_pickle=True)
    V = np.load(os.path.join(D, 'r7737_vis.npz'), allow_pickle=True)
    ls, k, dk = V['ls'], V['k'], V['dk']
    arm = {a: dict(eta=Z[f'eta_{a}'], x0=Z[f'x0_{a}'], g=Z[f'vis_{a}'],
                   W=float(Z[f'eta_ls_w_{a}']), rs=float(Z[f'r_s_{a}']),
                   D_M=float(Z[f'D_M_{a}'])) for a in ('lcdm', 'cr')}

    # ---------------------------------------------------------------- S1
    print("\n  ⛭ S1 — THE GRIDS AND THE MAP, REPORTED FIRST AND NOT CONDITIONED ON WHAT FOLLOWS")
    for a in ('lcdm', 'cr'):
        d = arm[a]
        print(f"      {a:5s} n {d['eta'].size}   eta span {np.ptp(d['eta']):.4f}   "
              f"x0 span {np.ptp(d['x0']):.4f}   x0 at g peak {d['x0'][np.argmax(d['g'])]:.6f}")
    gate('S1a', arm['lcdm']['eta'].size == arm['cr']['eta'].size,
         "the two grids have the SAME LENGTH, so index pairing is at least well-defined",
         f"{arm['lcdm']['eta'].size} and {arm['cr']['eta'].size}")
    r_grid = np.ptp(arm['cr']['x0']) / np.ptp(arm['lcdm']['x0'])
    sig = {a: wsig(arm[a]['g'], arm[a]['eta'], arm[a]['x0']) for a in arm}
    r_sig = sig['cr'] / sig['lcdm']
    r_W = arm['cr']['W'] / arm['lcdm']['W']
    r_DM = arm['cr']['D_M'] / arm['lcdm']['D_M']
    print(f"      ⇒ grid span ratio {r_grid:.6f}   g-weighted sigma ratio {r_sig:.6f}   "
          f"70's W ratio {r_W:.6f}   D_M ratio {r_DM:.10f}")
    gate('S1b', abs(r_grid - 1) > 0.005,
         "the spans differ by more than the 0.5 per cent the registration set as 'the convention "
         "barely bites', so P1 and P2 ARE different objects",
         f"grid span differs by {100 * (r_grid - 1):+.2f} %, the support's sigma by "
         f"{100 * (r_sig - 1):+.2f} %, 70's W by {100 * (r_W - 1):+.2f} %")
    # F_shape, as registered: how much of the map difference the single scalar does NOT capture
    xb = arm['cr']['x0']                      # index-paired onto lcdm's grid, which is 70's P1
    xa = arm['lcdm']['x0']
    num = float(np.sqrt((arm['lcdm']['g'] * (xb - r_DM * xa) ** 2).sum()
                        / arm['lcdm']['g'].sum()))
    den = float(np.sqrt((arm['lcdm']['g'] * (xb - xa) ** 2).sum() / arm['lcdm']['g'].sum()))
    print(f"      ⇒ ** F_shape = {num / den:.4f} ** (registered at r7737: <= 0.05 would mean the maps "
          f"are proportional\n           and the one-parameter cross term IS the map swap)")
    gate('S1c', True, f"F_shape reported, {num / den:.4f}; the registered 0.05 branch "
         f"{'FIRES' if num / den <= 0.05 else 'does NOT fire'}", 'reported, not a pass/fail')

    # ---------------------------------------------------------------- the five objects under P1
    print("\n  ⛭ VERIFYING 70's P1 BUILD IS REPRODUCED, before anything is changed")
    t0 = time.time()
    G_P1 = {f'{a}_{b}': V[f'G__g_{a}__X_{b}'] for a in arm for b in arm}
    sub_l, sub_k = np.arange(0, 698, 97), np.arange(0, 1450, 161)
    worst = 0.0
    for a in arm:
        for b in arm:
            mine = build_G(arm[a]['g'], arm[a]['eta'], arm[b]['x0'], ls[sub_l], k[sub_k])
            th = G_P1[f'{a}_{b}'][np.ix_(sub_l, sub_k)]
            worst = max(worst, float(np.abs(mine - th).max() / max(np.abs(th).max(), 1e-300)))
    gate('P1', worst == 0.0,
         "my builder reproduces 70's G EXACTLY on all four combinations, so P2 is the same "
         "arithmetic with one input changed",
         f"worst relative deviation {worst:.3e} over {len(sub_l)}x{len(sub_k)} sampled cells "
         f"({time.time() - t0:.0f} s)")
    if FAILS:
        print("  ⛔ REFUSING: a P2 build is only comparable if the P1 build is reproduced")
        return 1

    # ---------------------------------------------------------------- P2, under three span defs
    def rescale(src, brw, factor_ratio):
        """the borrowed map, pivoted at the visibility peak, spread rescaled by factor_ratio"""
        x = arm[brw]['x0']
        piv = x[np.argmax(arm[src]['g'])]
        return piv + (x - piv) / factor_ratio

    VARIANTS = {'sigma (mine)': r_sig, 'grid span': r_grid, "70's W": r_W}
    print(f"\n  ⛭ R1 — THE ATTRIBUTION UNDER P1 AND UNDER P2, fit-free, as a RANGE")
    print(f"      (the fit-free statistic is r7737's: the l-structured rms of each single swap, "
          f"no amplitudes)")
    rows = {}
    for tag, ratio in [('P1 (70, index)', None)] + [(f'P2 / {n}', v) for n, v in VARIANTS.items()]:
        if ratio is None:
            Gg, Gx = G_P1['cr_lcdm'], G_P1['lcdm_cr']
        else:
            Gg = build_G(arm['cr']['g'], arm['cr']['eta'], rescale('cr', 'lcdm', 1 / ratio), ls, k)
            Gx = build_G(arm['lcdm']['g'], arm['lcdm']['eta'], rescale('lcdm', 'cr', ratio), ls, k)
        lc = np.log(A_of(G_P1['lcdm_lcdm'], k, dk, arm['lcdm']['rs']))
        u_g = np.log(A_of(Gg, k, dk, arm['lcdm']['rs'])) - lc
        u_x = np.log(A_of(Gx, k, dk, arm['lcdm']['rs'])) - lc
        u_r = np.log(A_of(G_P1['lcdm_lcdm'], k, dk, arm['cr']['rs'])) - lc
        s = {'visibility g': lrms(u_g), 'distance map chi': lrms(u_x), 'comb period rs': lrms(u_r)}
        tot = sum(s.values())
        rows[tag] = {n: v / tot for n, v in s.items()}
        print(f"\n      {tag}")
        for n in ('distance map chi', 'visibility g', 'comb period rs'):
            print(f"          {n:18s} l-structured rms {s[n]:.6e}   = {100 * s[n] / tot:6.2f} %")
    print("\n" + "=" * 100)
    chi = [rows[t]['distance map chi'] for t in rows]
    g = [rows[t]['visibility g'] for t in rows]
    print(f"  the chi share across the pairings: {', '.join(f'{x:.3f}' for x in chi)}")
    print(f"  the g   share across the pairings: {', '.join(f'{x:.3f}' for x in g)}")
    if all(x >= R1_LINE for x in chi):
        print(f"  ⇒ R1 ROW ONE: chi >= {R1_LINE} under EVERY pairing. The attribution HOLDS, and order")
        print(f"    item ② opens: the closing sentence may name the distance map.")
    elif chi[0] >= R1_LINE and any(x >= R1_LINE for x in g):
        print(f"  ⛔ R1 ROW TWO: P1 gives chi >= {R1_LINE} and a P2 gives g >= {R1_LINE}.")
        print(f"     *** THE SPLIT IS A CONVENTION. *** The sentence may name ONLY the pairing-free")
        print(f"     part, and must say so.  Naming either leg would report a pairing as a result.")
    else:
        print(f"  ⇒ R1 ROW THREE: order item ③ — the range is reported and nothing is drafted.")
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
