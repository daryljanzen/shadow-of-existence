"""r7737+70 -- PO-87's last step, both tiers, as registered in PREDICTION.md.

  python3 split.py xmap FIELDS_DIR OUT_DIR [--workers N]     Tier 1: the other arm's distance MAP
  python3 split.py vis  GRID_DIR   OUT_DIR [--workers N]     Tier 2: the visibility exchange

THE PAIRING (declared, PREDICTION ①): x0 = eta_0 - eta on both arms, so a map swap is a choice of which
eta_B goes with which eta_A.  Both arms build their line-of-sight grid by ONE rule (420 points uniform on
eta_ls +/- 6W, 140 to ETA_END), so grid index i is the same position relative to each arm's own last
scattering.  `paired()` asserts that rule on both grids and returns x0_B read at the same index: no
interpolation is involved, and the window's chi span is exchanged with it (W_B / W_A).

Every closure is a refusal: no blob is written unless all pass.
"""
import json
import os
import sys
import time
import hashlib
from concurrent.futures import ProcessPoolExecutor

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7729_70_dlk_build'))
import project4 as P4                                    # noqa: E402  (load_arm, transfer, BANK, QLO, QHI)

BLOCK = 25
NWIN = 420                                               # the instrument's int(NLOSF * NLOS) = int(0.75 * 560)
C1_BAR = float(os.environ.get('C1_BAR', '1e-10'))


def window_rule(eta, eta_ls, w, tag):
    """the instrument's grid rule, asserted: eta_ls +/- 6W uniform over the first NWIN points, unclipped"""
    lo, hi = eta_ls - 6.0 * w, eta_ls + 6.0 * w
    ok = (abs(eta[0] - lo) <= 1e-9 * hi and abs(eta[NWIN] - hi) <= 1e-9 * hi
          and np.allclose(np.diff(eta[:NWIN]), (hi - lo) / NWIN, rtol=1e-9, atol=0))
    if not ok:
        raise SystemExit(f'⛔ {tag}: the eta grid does not follow the declared rule, so index pairing is not '
                         f'the declared pairing -- REFUSING')


def paired(x0_other):
    """x0_B at the same grid index (PREDICTION ①).  A copy, so the identity closure exercises this path."""
    return np.array(x0_other, dtype=float, copy=True)


# ---- workers ------------------------------------------------------------------------------------------
_W = {}


def _init(ctx):
    _W.update(ctx)


def _block(job):
    name, b = job
    c = _W['combos'][name]
    out = os.path.join(_W['out'], f'blk__{name}__B{BLOCK}__{b:03d}.npy')
    if os.path.exists(out):
        return name, b, 'skip'
    ls = _W['ls'][b * BLOCK:(b + 1) * BLOCK]
    F = np.empty((len(ls), len(c['k'])))
    for i, l in enumerate(ls):
        J = spherical_jn(int(l), c['k'][None, :] * c['x0'][:, None])
        F[i] = np.trapezoid(c['W'] * J, c['eta'], axis=0)      # W is S (Tier 1) or g[:, None] (Tier 2)
    np.save(out + '.tmp.npy', F)
    os.replace(out + '.tmp.npy', out)
    return name, b, 'done'


def run_blocks(combos, ls, odir, nw):
    nb = (len(ls) + BLOCK - 1) // BLOCK
    jobs = [(n, b) for n in combos for b in range(nb)]
    t0 = time.time()
    with ProcessPoolExecutor(nw, initializer=_init, initargs=(dict(combos=combos, ls=ls, out=odir),)) as ex:
        for n, b, st in ex.map(_block, jobs):
            if st == 'done':
                print(f'    {n} block {b + 1}/{nb} [{time.time() - t0:.0f} s]', flush=True)
    return {n: np.concatenate([np.load(os.path.join(odir, f'blk__{n}__B{BLOCK}__{b:03d}.npy'))
                               for b in range(nb)]) for n in combos}


def window_ls(lA_lcdm, lA_cr):
    lA = sorted([lA_lcdm, lA_cr])
    return np.arange(int(np.ceil(P4.QLO * lA[0])), int(np.floor(P4.QHI * lA[1])) + 1)


def finish(rep, odir, blob, arrays):
    ok = all(v.get('ok', True) for k, v in rep.items() if isinstance(v, dict) and k.startswith(('C', 'T2')))
    rep['ok'] = bool(ok)
    if ok:
        np.savez(blob, **arrays, meta=json.dumps(dict(order='r7737', closure=rep)))
        rep['blob'] = dict(path=os.path.basename(blob), bytes=os.path.getsize(blob),
                           sha256=hashlib.sha256(open(blob, 'rb').read()).hexdigest())
        print(f"  BUILT {blob} ({rep['blob']['bytes'] / 1e6:.1f} MB, sha256 {rep['blob']['sha256'][:16]})")
    else:
        print('  ⛔ a closure failed: REFUSING to write the blob')
    json.dump(rep, open(os.path.join(odir, 'closure.json'), 'w'), indent=1)
    return 0 if ok else 1


# ======================================================================================== Tier 1
def xmap(fdir, odir, nw):
    A = {a: P4.load_arm(fdir, a) for a in ('lcdm', 'cr')}
    gdir = os.environ.get('GRID_DIR') or SystemExit('set GRID_DIR: the declared pairing is asserted on GRIDSAVE grids')
    if isinstance(gdir, SystemExit):
        raise gdir
    G = {a: np.load(os.path.join(gdir, f'grid_{a}.npz')) for a in A}
    for a in A:                                              # the GRIDSAVE grid IS the field grid, bit for bit
        if not (np.array_equal(G[a]['eta'], A[a]['eta']) and np.array_equal(G[a]['x0'], A[a]['x0'])):
            raise SystemExit(f'⛔ {a}: GRIDSAVE grid differs from the SRCFIELD grid -- REFUSING')
    rep = {'C1_bar': C1_BAR}
    for a, d in A.items():                                   # C1, C2 exactly as r7729
        bk = np.load(os.path.join(P4.SP, P4.BANK[a] + '.npz'))
        m = np.isin(bk['ls'], d['ls'])
        Dl = d['Cl'] * d['ls'] * (d['ls'] + 1)
        mm = np.isin(d['ls'], bk['ls'])
        r = float(np.max(np.abs(Dl[mm] / bk['Dl'][m] - 1)))
        rep[f'C1_{a}'] = dict(max_rel=r, bar=C1_BAR, ok=r <= C1_BAR)
        cl = np.array([np.sum(d['P'] * P4.transfer(d['S'], d['eta'], d['x0'], d['k'], l) ** 2) for l in d['ls']])
        r2 = float(np.max(np.abs(cl / d['Cl'] - 1)))
        rep[f'C2_{a}'] = dict(max_rel=r2, ok=r2 <= 1e-12)
        print(f'  C1 {a} {r:.2e} (bar {C1_BAR:g})   C2 {a} {r2:.2e}', flush=True)
    if not all(rep[f'C{i}_{a}']['ok'] for i in (1, 2) for a in A):
        return finish(rep, odir, None, {})
    if True:                                                 # the declared rule, on the grids actually used
        for a in A:
            window_rule(A[a]['eta'], float(G[a]['eta_ls']), float(G[a]['eta_ls_w']), a)
    L, C = A['lcdm'], A['cr']
    assert len(L['eta']) == len(C['eta']), 'grids differ in length: index pairing undefined'
    lo, hi = max(L['k'].min(), C['k'].min()), min(L['k'].max(), C['k'].max())
    sel = (C['k'] >= lo) & (C['k'] <= hi)
    kg = C['k'][sel]
    dk_lad = (C['P'] / (C['k'] ** (C['ns'] - 1) / C['k']))[sel]
    src = {'cr': dict(S=C['S'][:, sel], eta=C['eta'], x0=C['x0'], ns=C['ns']),
           'lcdm': dict(S=CubicSpline(L['k'], L['S'], axis=1)(kg), eta=L['eta'], x0=L['x0'], ns=L['ns'])}
    combos = {}
    for s in ('cr', 'lcdm'):
        for x in ('cr', 'lcdm'):
            x0 = src[s]['x0'] if x == s else paired(A[x]['x0'])
            combos[f'S_{s}__X_{x}'] = dict(W=src[s]['S'], eta=src[s]['eta'], x0=x0, k=kg,
                                           P=kg ** (src[s]['ns'] - 1) / kg * dk_lad)
    combos['native_lcdm'] = dict(W=L['S'], eta=L['eta'], x0=L['x0'], k=L['k'], P=L['P'])
    ls = window_ls(L['l_A'], C['l_A'])
    rep['grid'] = dict(n_ladder=len(kg), k_lo=float(kg[0]), k_hi=float(kg[-1]), n_l=len(ls),
                       l_lo=int(ls[0]), l_hi=int(ls[-1]), pairing='grid index (PREDICTION ①)',
                       x0_at_peak={a: float(A[a]['x0'][int(np.argmax(G[a]['vis']))]) for a in A} )
    D = run_blocks(combos, ls, odir, nw)
    Dl = {n: ls * (ls + 1) * (combos[n]['P'][None, :] * D[n] ** 2).sum(axis=1) for n in combos}
    r3 = np.abs(Dl['S_lcdm__X_lcdm'] / Dl['native_lcdm'] - 1)
    rep['C3'] = dict(max_rel=float(r3.max()), worst_l=int(ls[int(np.argmax(r3))]), ok=bool(r3.max() <= 1e-3))
    r4 = max(float(np.max(np.abs(ls * (ls + 1) * (combos[n]['P'] * D[n] ** 2).sum(1) / Dl[n] - 1))) for n in combos)
    rep['C4'] = dict(max_rel=r4, ok=r4 <= 1e-12)
    # C5: the hybrid path with x0_B := x0_A returns the diagonal bit for bit
    c5 = []
    for s in ('cr', 'lcdm'):
        c = combos[f'S_{s}__X_{s}']
        for i in (0, len(ls) // 2, len(ls) - 1):
            l = ls[i]
            h = np.trapezoid(c['W'] * spherical_jn(int(l), kg[None, :] * paired(src[s]['x0'])[:, None]), c['eta'], axis=0)
            c5.append(bool(np.array_equal(h, D[f'S_{s}__X_{s}'][i])))
    rep['C5'] = dict(checked=len(c5), identical=int(sum(c5)), ok=all(c5))
    for k in ('C3', 'C4', 'C5'):
        print(f'  {k}: {rep[k]}', flush=True)
    arr = dict(ls=ls, k=kg, k_native_lcdm=L['k'],
               **{f'Dlk__{n}': D[n] for n in combos if n != 'native_lcdm'},
               **{f'P__{n}': combos[n]['P'] for n in combos if n != 'native_lcdm'},
               **{f'Dl__{n}': Dl[n] for n in combos})
    return finish(rep, odir, os.path.join(odir, 'r7737_xmap.npz'), arr)


# ======================================================================================== Tier 2
def acceptance(Gm, k, dk, rs):
    """A_l and the acceptance width -- `r7041_directions/acceptance_convergence.py::acceptance`, on given G"""
    W = Gm ** 2 * (dk / k)[None, :]
    s = W.sum(1)
    A = np.abs((W * np.exp(2j * k * rs)[None, :]).sum(1)) / s
    kb = (W * k).sum(1) / s
    wd = 2 * np.sqrt(np.maximum((W * (k[None, :] - kb[:, None]) ** 2).sum(1) / s, 0.0))
    return A, wd


def vis(gdir, odir, nw):
    G = {a: np.load(os.path.join(gdir, f'grid_{a}.npz')) for a in ('lcdm', 'cr')}
    for a in G:
        window_rule(G[a]['eta'], float(G[a]['eta_ls']), float(G[a]['eta_ls_w']), a)
    L, C = G['lcdm'], G['cr']
    assert len(L['eta']) == len(C['eta']), 'grids differ in length: index pairing undefined'
    lo, hi = max(L['k'].min(), C['k'].min()), min(L['k'].max(), C['k'].max())
    sel = (C['k'] >= lo) & (C['k'] <= hi)
    kg, dkg = C['k'][sel], C['dk'][sel]
    rep = {'T2_C3': {a: float(np.trapezoid(G[a]['vis'], G[a]['eta'])) for a in G}}
    combos = {}
    for g in ('cr', 'lcdm'):
        for x in ('cr', 'lcdm'):
            x0 = G[g]['x0'] if x == g else paired(G[x]['x0'])
            combos[f'g_{g}__X_{x}'] = dict(W=np.asarray(G[g]['vis'], float)[:, None], eta=G[g]['eta'], x0=x0, k=kg)
    combos['native_lcdm'] = dict(W=np.asarray(L['vis'], float)[:, None], eta=L['eta'], x0=L['x0'], k=L['k'])
    combos['native_cr'] = dict(W=np.asarray(C['vis'], float)[:, None], eta=C['eta'], x0=C['x0'], k=C['k'])
    ls = window_ls(float(L['l_A']), float(C['l_A']))
    Gm = run_blocks(combos, ls, odir, nw)
    rs = {a: float(G[a]['r_s']) for a in G}
    Acc = {}
    for n in combos:
        if n.startswith('native'):
            a = n.split('_')[1]
            Acc[n] = acceptance(Gm[n], G[a]['k'], G[a]['dk'], rs[a])
        else:
            for r in rs:
                Acc[f'{n}__rs_{r}'] = acceptance(Gm[n], kg, dkg, rs[r])
    a1 = np.abs(Acc['g_lcdm__X_lcdm__rs_lcdm'][0] / Acc['native_lcdm'][0] - 1)
    rep['T2_C1_lcdm'] = dict(max_rel=float(a1.max()), worst_l=int(ls[int(np.argmax(a1))]), ok=bool(a1.max() <= 1e-3))
    gid = Gm['native_cr'][:, sel]
    rep['T2_C1_cr'] = dict(G_identical=bool(np.array_equal(gid, Gm['g_cr__X_cr'])),
                           max_rel_A=float(np.max(np.abs(Acc['g_cr__X_cr__rs_cr'][0] / Acc['native_cr'][0] - 1))),
                           ok=bool(np.array_equal(gid, Gm['g_cr__X_cr'])))
    c2 = []
    for g in ('cr', 'lcdm'):
        c = combos[f'g_{g}__X_{g}']
        for i in (0, len(ls) // 2, len(ls) - 1):
            h = np.trapezoid(c['W'] * spherical_jn(int(ls[i]), kg[None, :] * paired(G[g]['x0'])[:, None]), c['eta'], axis=0)
            c2.append(bool(np.array_equal(h, Gm[f'g_{g}__X_{g}'][i])))
    rep['T2_C2'] = dict(checked=len(c2), identical=int(sum(c2)), ok=all(c2))
    for k in ('T2_C1_lcdm', 'T2_C1_cr', 'T2_C2', 'T2_C3'):
        print(f'  {k}: {rep[k]}', flush=True)
    rep['l_A'] = {a: float(G[a]['l_A']) for a in G}
    rep['r_s'] = rs
    rep['W'] = {a: float(G[a]['eta_ls_w']) for a in G}
    arr = dict(ls=ls, k=kg, dk=dkg, k_native_lcdm=L['k'], k_native_cr=C['k'],
               **{f'G__{n}': Gm[n] for n in combos},
               **{f'A__{n}': v[0] for n, v in Acc.items()}, **{f'width__{n}': v[1] for n, v in Acc.items()})
    return finish(rep, odir, os.path.join(odir, 'r7737_vis.npz'), arr)


if __name__ == '__main__':
    mode, src, out = sys.argv[1:4]
    nw = int(sys.argv[sys.argv.index('--workers') + 1]) if '--workers' in sys.argv else 4
    os.makedirs(out, exist_ok=True)
    sys.exit({'xmap': xmap, 'vis': vis}[mode](src, out, nw))
