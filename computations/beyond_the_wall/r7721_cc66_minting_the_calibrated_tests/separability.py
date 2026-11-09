#!/usr/bin/env python3
"""`r7721+cc66.2` the `(l, k)` separability measurement, EXACTLY as pre-registered.

⛭ Registered in `PREDICTION_separability.md`, pushed in its own commit before this file existed.
Nothing here chooses a grid, a reading or a threshold: all three were fixed there.

The object: `M^{S,K}(l, k) = G_l^K(k)^2 (dk/k) S^2(k)`, whose `k`-collapse IS the banked spectrum.
The build is to KEEP it.  `G` is recomputed at the common grid's nodes and NEVER interpolated, because
interpolating `G` means interpolating the very object whose `(l, k)` structure is being measured.

⛔ The heavy part is the two `G` arrays and nothing else: by registered Gate 1 the kernel difference is
SOURCE-FREE, so this needs 2 kernel arrays rather than 4 combinations.  Checkpointed in BLOCKS of `l`,
because this container is reclaimed unpredictably and a checkpoint interval longer than the interval
between restarts is not a checkpoint (`r7713` lost a 34-minute combination learning that).
"""
import os
import sys
import time

import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7713_cc66_the_dense_ell_discriminant'))
import dense                                                     # noqa: E402  the banked instrument

OUT = os.path.join(HERE, 'sep')
BLOCK = 25
TOL_CONTROL = 1e-12          # registered: Gate 0, the same tolerance r7715's CI control runs under
TOL_GRID = 1e-3              # registered: Gate 2c, a convergence statement and NOT an identity
CORR_MAX = 0.70              # registered: Gate 3 threshold, fixed before any number existed
VIF_MAX = 2.0                # registered: the same statement -- at |corr| = 0.70 the VIF is 1.96
D1_CORR, D1_COND, D1_VIF = -0.9200, 5.03, 6.51                   # what closed the collapsed route


# ---------------------------------------------------------------- the registered grids


def kstar():
    """the COARSER arm's own nodes inside the overlap -- registered so NO ARM IS INTERPOLATED UP"""
    kl, _ = dense.source('lcdm')
    kc, _ = dense.source('cr')
    lo, hi = max(kl[0], kc[0]), min(kl[-1], kc[-1])
    return kc[(kc >= lo) & (kc <= hi)]


def s2_on_kstar(t):
    """`S^2` carried to `K*` by linear interpolation in `log k` of `log S^2` (registered)"""
    k, S2 = dense.source(t)
    ks = kstar()
    return np.exp(np.interp(np.log(ks), np.log(k), np.log(S2)))


def shared_ls():
    """reading (A): the shared INTEGER `l` range -- no interpolation anywhere in it"""
    return np.intersect1d(dense.geom('lcdm')['ls'], dense.geom('cr')['ls'])


def n_blocks():
    return (len(shared_ls()) + BLOCK - 1) // BLOCK


# ---------------------------------------------------------------- the heavy part, checkpointed


def g_block(ker_t, b):
    """`G_l^K` on `K*` for one block of `l`, written whole; a restart costs at most this block"""
    os.makedirs(OUT, exist_ok=True)
    bp = os.path.join(OUT, f'g__K_{ker_t}__B{BLOCK}__{b:03d}.npy')
    if os.path.exists(bp):
        return np.load(bp)
    g = dense.geom(ker_t)
    ks = kstar()
    sl = shared_ls()[b * BLOCK:(b + 1) * BLOCK]
    Gb = np.empty((len(sl), len(ks)))
    for i, l in enumerate(sl):
        J = spherical_jn(int(l), ks[None, :] * g['x0'][:, None])
        Gb[i] = np.trapezoid(g['vis'][:, None] * J, g['eta'], axis=0)
    np.save(bp, Gb)
    return Gb


def g_full(ker_t):
    """assembled only when every block is present; refuses on a partial grid and names what is missing"""
    miss = [b for b in range(n_blocks())
            if not os.path.exists(os.path.join(OUT, f'g__K_{ker_t}__B{BLOCK}__{b:03d}.npy'))]
    if miss:
        raise SystemExit(f"  ⛔ REFUSING: kernel {ker_t} is missing blocks {miss[:8]}"
                         f"{' ...' if len(miss) > 8 else ''} of {n_blocks()} -- run `--blocks` first")
    G = np.concatenate([np.load(os.path.join(OUT, f'g__K_{ker_t}__B{BLOCK}__{b:03d}.npy'))
                        for b in range(n_blocks())])
    assert G.shape == (len(shared_ls()), len(kstar())), G.shape
    return G


def build_blocks():
    t0 = time.time()
    nb = n_blocks()
    for ker_t in ('lcdm', 'cr'):
        for b in range(nb):
            bp = os.path.join(OUT, f'g__K_{ker_t}__B{BLOCK}__{b:03d}.npy')
            if os.path.exists(bp):
                continue
            g_block(ker_t, b)
            print(f"      K={ker_t:5s} block {b + 1}/{nb}  [{time.time() - t0:.0f} s this pass]",
                  flush=True)
    print(f"  all {2 * nb} blocks present; {time.time() - t0:.0f} s this pass", flush=True)


def how_far():
    nb = n_blocks()
    done = sum(os.path.exists(os.path.join(OUT, f'g__K_{t}__B{BLOCK}__{b:03d}.npy'))
               for t in ('lcdm', 'cr') for b in range(nb))
    return done, 2 * nb


if __name__ == '__main__':
    if '--blocks' in sys.argv:
        build_blocks()
    elif '--progress' in sys.argv:
        d, t = how_far()
        print(f"  {d} of {t} blocks")
    else:
        print(__doc__)
