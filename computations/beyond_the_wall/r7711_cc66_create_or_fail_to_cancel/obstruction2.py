#!/usr/bin/env python3
"""`r7711+cc66` OBSTRUCTION 2: the cross-window projection, with its two-sided control run FIRST.

Builds each arm's projection kernel from its own banked geometry --
    G_l^K(k) = \\int v^K(eta) j_l(k x0^K(eta)) d eta
-- and forms a pseudo-spectrum by projecting a source's power through a kernel:
    Pseudo(S, K)_l = sum_k G_l^K(k)^2 S^S(k)^2 dk / k
on the SOURCE arm's k grid.  Four combinations: each arm's source through its own and the other's kernel.

⛔ THE CONTROL COMES FIRST AND DECIDES WHETHER ANYTHING BELOW IS EVIDENCE.  If swapping the kernel leaves
the pseudo-spectrum unmoved, the swap is an inert perturbation and no cross-reading from it separates
"creates" from "fails to cancel" -- which is `r7703`'s leg-B case, registered in advance at `r7711+cc66.0`.
"""
import json
import os
import sys
import time

import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7639_cc66_P15_repoint_paper'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7637_70_own_comb_statistic'))
import own_comb_kinds as OCK                                                 # noqa: E402

ACC = {'lcdm': 'r7041_accept_lcdm', 'cr': 'r7041_accept_cr_leafrec1'}
SRC = {'lcdm': 'r6911_source_lcdm_leafrec1', 'cr': 'r6911_source_cr_leafrec1'}
QLO, QHI = 0.80, 3.10


def geom(t):
    z = np.load(os.path.join(SP, ACC[t] + '.npz'), allow_pickle=True)
    ls = np.asarray(z['ls__fixed'], int)
    lA = float(z['l_A__fixed'])
    m = (ls / lA >= QLO) & (ls / lA <= QHI)
    return dict(ls=ls[m], l_A=lA, eta=np.asarray(z['eta__fixed'], float),
                x0=np.asarray(z['x0__fixed'], float), vis=np.asarray(z['vis__fixed'], float))


def source(t):
    z = np.load(os.path.join(SP, SRC[t] + '.npz'), allow_pickle=True)
    return (np.asarray(z['k'], float), np.asarray(z['S_i'], float) ** 2,
            float(z['r_s']), float(z['l_A']))


def pseudo(src_t, ker_t, G_cache):
    """Pseudo(S, K): the source's power through the kernel, on the source arm's k grid and the
    kernel arm's l list.  The abscissa is the KERNEL arm's q, because l is the kernel's index."""
    k, S2, rs, _ = source(src_t)
    g = geom(ker_t)
    key = (src_t, ker_t)
    if key not in G_cache:
        dk = np.gradient(k)
        out = np.empty(len(g['ls']))
        for i, l in enumerate(g['ls']):
            J = spherical_jn(int(l), k[None, :] * g['x0'][:, None])
            G = np.trapezoid(g['vis'][:, None] * J, g['eta'], axis=0)
            W = G ** 2 * dk / k
            out[i] = float(np.sum(W * S2))
        G_cache[key] = out
    return g['ls'] / g['l_A'], G_cache[key]


def slide(xa, ya, xc, yc, halves=(0.175, 0.25, 0.35)):
    """the band-RMS ratio of two pseudo-spectra, read exactly as the step is read"""
    st = OCK.own_state({'lcdm': (xc, yc), 'cr': (xa, ya)}, 'mean', 1.0)
    out = []
    for h in halves:
        cs = np.arange(0.85 + h, 3.0, 0.05)
        R = np.array([OCK._rms(st['ua'], st['oa'], c - h, c + h)
                      / OCK._rms(st['xc'], st['oc'], c - h, c + h) - 1.0 for c in cs])
        L, H = R[cs < 1.4], R[cs > 2.2]
        sd = float(np.sqrt((L.var(ddof=1) + H.var(ddof=1)) / 2))
        out.append(dict(half=h, lo=float(L.mean()), hi=float(H.mean()),
                        step=float(H.mean() - L.mean()), sd=sd,
                        in_sd=float(abs(H.mean() - L.mean()) / sd) if sd else float('nan')))
    return out


def main():
    t0 = time.time()
    C, res = {}, {}
    print("\n  ⛭ `r7711` building the four pseudo-spectra (source x kernel)")
    for s in ('lcdm', 'cr'):
        for kk in ('lcdm', 'cr'):
            t1 = time.time()
            q, y = pseudo(s, kk, C)
            res[f'{s}|{kk}'] = (q, y)
            print(f"      S={s:5s} through K={kk:5s}: {len(y)} l, "
                  f"range {y.min():.4g}..{y.max():.4g}   [{time.time() - t1:.1f} s]")

    # ⛔ THE CONTROL, FIRST: does swapping the kernel move the pseudo-spectrum AT ALL?
    print("\n  ⛔ `r7711` THE CONTROL -- swapping the kernel on a FIXED source must move something")
    ctl = {}
    for s in ('lcdm', 'cr'):
        qo, yo = res[f'{s}|{s}']
        other = 'cr' if s == 'lcdm' else 'lcdm'
        qx, yx = res[f'{s}|{other}']
        yi = np.interp(qo, qx, yx)
        rel = np.abs(yi / yo - 1.0)
        ctl[s] = dict(median=float(np.median(rel)), max=float(rel.max()),
                      identical=bool(np.array_equal(yo, yi)))
        print(f"      source {s:5s}: own kernel vs the other's -- median |move| "
              f"{100 * ctl[s]['median']:.3f}%, max {100 * ctl[s]['max']:.3f}%"
              + ("   ⛔ BYTE-IDENTICAL" if ctl[s]['identical'] else ""))
    live = all(c['median'] > 1e-6 for c in ctl.values())
    print(f"      ⇒ the kernel swap is {'LIVE' if live else 'INERT'} as a perturbation")

    # the readings
    print("\n  ⛭ `r7711` THE STEP IN EACH COMBINATION'S RATIO, read as the step is read")
    print("      ratio                               half     lo        hi       step     step/sd")
    rows = {}
    for name, (an, cn) in (("own x own  (cr|cr)/(lcdm|lcdm)", ('cr|cr', 'lcdm|lcdm')),
                           ("kernel swapped (cr|lcdm)/(lcdm|lcdm)", ('cr|lcdm', 'lcdm|lcdm')),
                           ("source swapped (lcdm|cr)/(lcdm|lcdm)", ('lcdm|cr', 'lcdm|lcdm'))):
        qa, ya = res[an]
        qc, yc = res[cn]
        rows[name] = slide(qa, ya, qc, yc)
        for r in rows[name]:
            print(f"      {name:35s} {r['half']:.3f}  {r['lo']:+.4f}  {r['hi']:+.4f}  "
                  f"{r['step']:+.4f}   {r['in_sd']:6.2f}")
    json.dump(dict(control=ctl, live=live,
                   rows={k: v for k, v in rows.items()}, wall_s=round(time.time() - t0, 1)),
              open(os.path.join(HERE, 'obstruction2.json'), 'w'), indent=1)
    print(f"\n  wall {time.time() - t0:.1f} s")
    return 0


if __name__ == '__main__':
    sys.exit(main())
