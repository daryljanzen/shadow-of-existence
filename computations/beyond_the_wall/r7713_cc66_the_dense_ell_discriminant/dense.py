#!/usr/bin/env python3
"""`r7713+cc66` the dense-`l` discriminant, idempotent by construction.

Each of the four `Pseudo(source, kernel)` combinations is written to its own `.npz` as it completes and
SKIPPED if that file already exists, because this container restarts unpredictably and a three-hour job
that cannot resume may never finish.  Re-running after a restart continues rather than starting over.

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
    """one combination, written as it completes; a finished file is read and not recomputed"""
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f'pseudo__S_{src_t}__K_{ker_t}.npz')
    if os.path.exists(path):
        d = np.load(path)
        print(f"      S={src_t:5s} K={ker_t:5s}: already on disk, {len(d['y'])} l -- SKIPPED", flush=True)
        return d['q'], d['y']
    k, S2 = source(src_t)
    g = geom(ker_t)
    dk = np.gradient(k)
    y = np.empty(len(g['ls']))
    t0 = time.time()
    for i, l in enumerate(g['ls']):
        J = spherical_jn(int(l), k[None, :] * g['x0'][:, None])
        G = np.trapezoid(g['vis'][:, None] * J, g['eta'], axis=0)
        y[i] = float(np.sum(G ** 2 * dk / k * S2))
        if i and i % 100 == 0:
            print(f"        ... {i}/{len(g['ls'])} l, {time.time() - t0:.0f} s", flush=True)
    q = g['ls'] / g['l_A']
    np.savez(path, q=q, y=y, ls=g['ls'], l_A=g['l_A'],
             meta=json.dumps(dict(source=SRC[src_t], kernel=ACC[ker_t], n_l=len(y),
                                  wall_s=round(time.time() - t0, 1))))
    print(f"      S={src_t:5s} K={ker_t:5s}: {len(y)} l written  [{time.time() - t0:.0f} s]", flush=True)
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
