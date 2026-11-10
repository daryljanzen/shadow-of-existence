#!/usr/bin/env python3
"""r7729+70: the four source x kernel transfers Delta_l(k) on the CR ladder, at every integer l in the window.

Usage: project4.py FIELDS_DIR OUT_DIR [--workers N]

FIELDS_DIR holds the per-k-slice `SRCFIELD` saves of one run per arm, `{lcdm,cr}_k{lo}.npz` (S(k, eta), eta, x0,
k, the batch-local P, and the run's own partial Cl), at the reported r6911 configuration.  This is `_project`'s
own line, `np.trapezoid(S * J, ee, axis=0)` with `J = j_l(k * XS * x0)`, applied four ways on ONE grid (69's
r7729 ruling (S1), as cc66 registered it at r7721):

  * the grid is the CR arm's own ladder nodes inside the k-overlap -- CR's physics, never interpolated;
  * the control's source is interpolated in k onto those nodes (cubic, per eta row; smooth in k);
  * each kernel is recomputed there: the cross terms use `SRCXS`'s definition, x0 -> XS * x0 with
    XS = D_M(kernel arm) / D_M(source arm);
  * P on the ladder is the SOURCE arm's k^(n_s - 1)/k times the ladder's own batch-local measure.

Closure controls, all registered in PREDICTION.md, and the build REFUSES on any failure:
  C1  each run's own D_l reproduces the banked r6911 leafrec1 D_l at the shared l          (<= 1e-10)
  C2  this projector on each arm's NATIVE grid reproduces that run's D_l at its l          (<= 1e-12)
  C3  (S_lcdm, K_lcdm) on the LADDER reproduces native lcdm D_l at EVERY l in the window   (<= 1e-3)
  C4  every retained array gives its own collapsed D_l by l(l+1) sum P Delta^2             (<= 1e-12)

Checkpointed in blocks of `BLOCK` l per combination, so a container restart costs at most one block.
"""
import glob
import hashlib
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
BANK = {'lcdm': 'r6911_source_lcdm_leafrec1', 'cr': 'r6911_source_cr_leafrec1'}
QLO, QHI = 0.80, 3.10
BLOCK = 25
COMBOS = (('cr', 'cr'), ('cr', 'lcdm'), ('lcdm', 'lcdm'), ('lcdm', 'cr'))   # (source, kernel)


def load_arm(fdir, arm):
    """the arm's fields, slices concatenated along k in slice order; the eta grid is one per run"""
    import re
    fs = sorted((p for p in glob.glob(os.path.join(fdir, f'{arm}_k*.npz'))
                 if re.fullmatch(rf'{arm}_k\d+\.npz', os.path.basename(p))),
                key=lambda p: int(os.path.basename(p)[len(arm) + 2:-4]))
    if not fs:
        raise SystemExit(f'no {arm} fields in {fdir}')
    zs = [np.load(f) for f in fs]
    eta = zs[0]['eta']
    for z in zs[1:]:
        assert np.array_equal(z['eta'], eta) and np.array_equal(z['x0'], zs[0]['x0']), 'eta grids differ'
    ls = zs[0]['ls']
    return dict(k=np.concatenate([z['k'] for z in zs]), P=np.concatenate([z['P'] for z in zs]),
                S=np.concatenate([z['S'] for z in zs], axis=1), eta=eta, x0=zs[0]['x0'],
                ls=ls, Cl=sum(z['Cl'] for z in zs), D_M=float(zs[0]['D_M']), l_A=float(zs[0]['l_A']),
                ns=float(zs[0]['ns']), r_s=float(zs[0]['r_s']), n_slices=len(zs),
                n_modes=int(zs[0]['n_modes']))


def transfer(S, ee, x0, k, l, xs=1.0):
    return np.trapezoid(S * spherical_jn(int(l), k[None, :] * (xs * x0)[:, None]), ee, axis=0)


# ---- worker state, set once per process ----------------------------------------------------------------
_W = {}


def _init(ctx):
    _W.update(ctx)


def _block(job):
    """one block of l for one combination, written whole"""
    name, b = job
    c = _W['combos'][name]
    out = os.path.join(_W['out'], f'blk__{name}__B{BLOCK}__{b:03d}.npy')
    if os.path.exists(out):
        return name, b, 'skip'
    ls = _W['ls'][b * BLOCK:(b + 1) * BLOCK]
    D = np.empty((len(ls), len(c['k'])))
    for i, l in enumerate(ls):
        D[i] = transfer(c['S'], c['eta'], c['x0'], c['k'], l, c['xs'])
    np.save(out + '.tmp.npy', D)
    os.replace(out + '.tmp.npy', out)
    return name, b, 'done'


def main(argv):
    fdir, odir = argv[0], argv[1]
    nw = int(argv[argv.index('--workers') + 1]) if '--workers' in argv else 4
    os.makedirs(odir, exist_ok=True)
    rep = {}
    A = {a: load_arm(fdir, a) for a in ('lcdm', 'cr')}

    # C1: the run against the bank
    for a, d in A.items():
        bk = np.load(os.path.join(SP, BANK[a] + '.npz'), allow_pickle=True)
        Dl = d['Cl'] * d['ls'] * (d['ls'] + 1)
        m = np.isin(bk['ls'], d['ls'])
        mm = np.isin(d['ls'], bk['ls'])
        r = float(np.max(np.abs(Dl[mm] / bk['Dl'][m] - 1)))
        rep[f'C1_{a}'] = dict(n_l=int(mm.sum()), max_rel=r, ok=r <= 1e-10, n_modes=d['n_modes'],
                              n_slices=d['n_slices'], nk_saved=len(d['k']))
        print(f'  C1 {a}: run D_l vs banked {BANK[a]} at {int(mm.sum())} l: max rel {r:.2e}', flush=True)

    # C2: the projector against the run, native grid, the run's own l
    for a, d in A.items():
        cl = np.array([np.sum(d['P'] * transfer(d['S'], d['eta'], d['x0'], d['k'], l) ** 2) for l in d['ls']])
        r = float(np.max(np.abs(cl / d['Cl'] - 1)))
        rep[f'C2_{a}'] = dict(max_rel=r, ok=r <= 1e-12)
        print(f'  C2 {a}: offline native projection vs the run at {len(d["ls"])} l: max rel {r:.2e}', flush=True)
    if not all(rep[f'C{i}_{a}']['ok'] for i in (1, 2) for a in A):
        json.dump(rep, open(os.path.join(odir, 'closure.json'), 'w'), indent=1)
        print('  ⛔ C1/C2 failed: REFUSING to build')
        return 1

    # the ladder grid, inside the overlap
    L, C = A['lcdm'], A['cr']
    lo, hi = max(L['k'].min(), C['k'].min()), min(L['k'].max(), C['k'].max())
    sel = (C['k'] >= lo) & (C['k'] <= hi)
    kg = C['k'][sel]
    dk_lad = (C['P'] / (C['k'] ** (C['ns'] - 1) / C['k']))[sel]        # CR's own batch-local measure
    S_l = CubicSpline(L['k'], L['S'], axis=1)(kg)                      # the control's source on the ladder
    srcs = {'cr': dict(S=C['S'][:, sel], eta=C['eta'], x0=C['x0'], D_M=C['D_M'], ns=C['ns']),
            'lcdm': dict(S=S_l, eta=L['eta'], x0=L['x0'], D_M=L['D_M'], ns=L['ns'])}
    combos = {}
    for s, kr in COMBOS:
        src = srcs[s]
        combos[f'S_{s}__K_{kr}'] = dict(S=src['S'], eta=src['eta'], x0=src['x0'], k=kg,
                                        xs=A[kr]['D_M'] / src['D_M'],
                                        P=kg ** (src['ns'] - 1) / kg * dk_lad)
    combos['native_lcdm'] = dict(S=L['S'], eta=L['eta'], x0=L['x0'], k=L['k'], xs=1.0, P=L['P'])
    lA = sorted([L['l_A'], C['l_A']])
    ls = np.arange(int(np.ceil(QLO * lA[0])), int(np.floor(QHI * lA[1])) + 1)
    nb = (len(ls) + BLOCK - 1) // BLOCK
    rep['grid'] = dict(n_ladder=len(kg), k_lo=float(kg[0]), k_hi=float(kg[-1]), n_l=len(ls), l_lo=int(ls[0]),
                       l_hi=int(ls[-1]), l_A=dict(lcdm=L['l_A'], cr=C['l_A']),
                       xs={n: c['xs'] for n, c in combos.items()},
                       nodes_per_bessel_period=float(2 * np.pi / max(L['D_M'], C['D_M']) / np.median(np.diff(kg))))
    print(f"  grid: {len(kg)} ladder nodes in k [{kg[0]:.5f}, {kg[-1]:.5f}], {len(ls)} l ({ls[0]}..{ls[-1]}), "
          f"{rep['grid']['nodes_per_bessel_period']:.2f} nodes per Bessel period", flush=True)

    jobs = [(n, b) for n in combos for b in range(nb)]
    t0 = time.time()
    with ProcessPoolExecutor(nw, initializer=_init, initargs=(dict(combos=combos, ls=ls, out=odir),)) as ex:
        for i, (n, b, st) in enumerate(ex.map(_block, jobs)):
            if st == 'done':
                print(f'    {n} block {b + 1}/{nb} [{time.time() - t0:.0f} s]', flush=True)

    D = {n: np.concatenate([np.load(os.path.join(odir, f'blk__{n}__B{BLOCK}__{b:03d}.npy')) for b in range(nb)])
         for n in combos}
    Dl = {n: ls * (ls + 1) * (combos[n]['P'][None, :] * D[n] ** 2).sum(axis=1) for n in combos}
    # C3: the ruling's control
    r3 = np.abs(Dl['S_lcdm__K_lcdm'] / Dl['native_lcdm'] - 1)
    rep['C3'] = dict(max_rel=float(r3.max()), worst_l=int(ls[int(np.argmax(r3))]),
                     n_over_1e3=int((r3 > 1e-3).sum()), ok=bool(r3.max() <= 1e-3))
    print(f"  C3 (S_lcdm,K_lcdm) on the ladder vs native lcdm, every l: max rel {r3.max():.2e} at l={rep['C3']['worst_l']}"
          f" ({rep['C3']['n_over_1e3']} l over 1e-3)", flush=True)
    # C4: the identity, recomputed independently in a different summation order
    r4 = max(float(np.max(np.abs(np.einsum('k,lk->l', combos[n]['P'], D[n] ** 2) * ls * (ls + 1) / Dl[n] - 1)))
             for n in combos)
    rep['C4'] = dict(max_rel=r4, ok=r4 <= 1e-12)
    rep['ok'] = all(rep[k]['ok'] for k in rep if k.startswith('C'))
    blob = os.path.join(odir, 'r7729_dlk_four.npz')
    if rep['ok']:
        np.savez(blob, ls=ls, k=kg, **{f'Dlk__{n}': D[n] for n in combos if n != 'native_lcdm'},
                 **{f'P__{n}': combos[n]['P'] for n in combos if n != 'native_lcdm'},
                 **{f'Dl__{n}': Dl[n] for n in combos}, k_native_lcdm=L['k'],
                 meta=json.dumps(dict(order='r7729', grid='CR ladder nodes in the k-overlap (S1)',
                                      lcdm_source='cubic spline in k per eta row', cross='x0 -> XS x0 (SRCXS)',
                                      combos=[f'S_{s}__K_{k}' for s, k in COMBOS], closure=rep)))
        rep['blob'] = dict(path=os.path.basename(blob), bytes=os.path.getsize(blob),
                           sha256=hashlib.sha256(open(blob, 'rb').read()).hexdigest())
        print(f"  BUILT {blob} ({rep['blob']['bytes'] / 1e6:.1f} MB, sha256 {rep['blob']['sha256'][:16]})")
    else:
        print('  ⛔ a closure control failed: REFUSING to write the blob')
    json.dump(rep, open(os.path.join(odir, 'closure.json'), 'w'), indent=1)
    return 0 if rep['ok'] else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
