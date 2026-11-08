#!/usr/bin/env python3
"""`r7713+cc66` the dense-`l` discriminant, idempotent in BLOCKS of `l`.

⛔ **The first form of this file checkpointed per COMBINATION and that granularity was too coarse.**  The
container restarted (`up 0 min`, confirmed from `/proc/uptime`, not inferred) after `100` of `693` `l`,
about five minutes into a thirty-four minute combination, and the whole combination was lost because
nothing had been written.  ⇒ A checkpoint interval longer than the interval between restarts is not a
checkpoint.  Blocks of `BLOCK` `l` are now written as they finish and skipped on a re-run, so a restart
costs at most one block, and the combination file is assembled from the blocks once they are all present.

`Pseudo(S,K)_l = sum_k G_l^K(k)^2 S(k)^2 dk / k`, with `G_l^K(k) = \\int v^K j_l(k x0^K) d eta` built from
the banked geometry, on the SOURCE arm's `k` grid and EVERY integer `l` with `q = l / l_A^K` in
[0.80, 3.10].
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
OUT = os.path.join(HERE, 'pseudo')
ACC = {'lcdm': 'r7041_accept_lcdm', 'cr': 'r7041_accept_cr_leafrec1'}
SRC = {'lcdm': 'r6911_source_lcdm_leafrec1', 'cr': 'r6911_source_cr_leafrec1'}
QLO, QHI = 0.80, 3.10
# ⛔ 50 was TOO COARSE FOR THE TOP OF THE BAND, by this file's own criterion.  The per-`l` cost RISES
#    with order -- 152 s per 50 `l` near the bottom of the window, 386 s near the top, measured -- so a
#    50-`l` block at high `l` cost up to 46 per cent of the observed window between container recycles,
#    and the whole of it was lost each time.  25 halves the in-flight loss without touching the
#    computation, the grid, or any registered threshold.  ⌗ The block FILENAME now carries the block
#    size, so blocks written at one size can never be read as blocks of another.
BLOCK = 25


def geom(t):
    z = np.load(os.path.join(SP, ACC[t] + '.npz'), allow_pickle=True)
    lA = float(z['l_A__fixed'])
    ls = np.arange(int(np.ceil(QLO * lA)), int(np.floor(QHI * lA)) + 1)
    return dict(ls=ls, l_A=lA, eta=np.asarray(z['eta__fixed'], float),
                x0=np.asarray(z['x0__fixed'], float), vis=np.asarray(z['vis__fixed'], float))


def source(t):
    z = np.load(os.path.join(SP, SRC[t] + '.npz'), allow_pickle=True)
    return np.asarray(z['k'], float), np.asarray(z['S_i'], float) ** 2


def build(src_t, ker_t):
    """one combination, checkpointed in BLOCKS of `l`; finished blocks are read and not recomputed"""
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f'pseudo__S_{src_t}__K_{ker_t}.npz')
    if os.path.exists(path):
        d = np.load(path)
        print(f"      S={src_t:5s} K={ker_t:5s}: already assembled, {len(d['y'])} l -- SKIPPED", flush=True)
        return d['q'], d['y']
    k, S2 = source(src_t)
    g = geom(ker_t)
    dk = np.gradient(k)
    nb = (len(g['ls']) + BLOCK - 1) // BLOCK
    t0 = time.time()
    for b in range(nb):
        bp = os.path.join(OUT, f'block__S_{src_t}__K_{ker_t}__B{BLOCK}__{b:03d}.npy')
        if os.path.exists(bp):
            continue
        sl = g['ls'][b * BLOCK:(b + 1) * BLOCK]
        yb = np.empty(len(sl))
        for i, l in enumerate(sl):
            J = spherical_jn(int(l), k[None, :] * g['x0'][:, None])
            G = np.trapezoid(g['vis'][:, None] * J, g['eta'], axis=0)
            yb[i] = float(np.sum(G ** 2 * dk / k * S2))
        np.save(bp, yb)                      # written whole; a restart costs at most this block
        print(f"        S={src_t:5s} K={ker_t:5s} block {b + 1}/{nb} ({len(sl)} l) "
              f"[{time.time() - t0:.0f} s in this pass]", flush=True)
    y = np.concatenate([np.load(os.path.join(OUT, f'block__S_{src_t}__K_{ker_t}__B{BLOCK}__{b:03d}.npy'))
                        for b in range(nb)])
    assert len(y) == len(g['ls']), (len(y), len(g['ls']))
    q = g['ls'] / g['l_A']
    np.savez(path, q=q, y=y, ls=g['ls'], l_A=g['l_A'],
             meta=json.dumps(dict(source=SRC[src_t], kernel=ACC[ker_t], n_l=len(y), block=BLOCK)))
    print(f"      S={src_t:5s} K={ker_t:5s}: {len(y)} l ASSEMBLED from {nb} blocks", flush=True)
    return q, y


def main():
    t0 = time.time()
    print("\n  ⛭ `r7713` the four pseudo-spectra on EVERY integer l in q in [0.80, 3.10]", flush=True)
    res = {}
    for s in ('lcdm', 'cr'):
        for kk in ('lcdm', 'cr'):
            res[f'{s}|{kk}'] = build(s, kk)
    print(f"\n  all four present; {time.time() - t0:.0f} s in this pass", flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
