"""r7739+70: the two x0(eta) arrays and the two eta grids, for refs/ci/r7737_grid (PREDICTION ⑥).

cc66 asked for them (r7739, 69) to compute S1 and to bound index pairing against a pairing that holds the
chi span fixed.  They come from GRIDSAVE, which is the same grid split.py paired on, and they need no solve.

Usage: gridref.py GRID_DIR XMAP_CLOSURE_JSON OUT_DIR

Each closure is a refusal: no blob is written unless all three pass.
  G1  eta + x0 == eta_0 bit for bit at every point, both arms
  G2  split.py's window rule (420 uniform points on [eta_LS - 6W, eta_LS + 6W)), both arms
  G3  x0 at the visibility's peak index == refs/ci/r7737_xmap's closure.json x0_at_peak, bit for bit, both arms
"""
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from split import window_rule  # noqa: E402  (the same assertion split.py paired under)

SCALARS = ('eta_ls', 'eta_ls_w', 'eta_0', 'D_M', 'r_s', 'l_A')


def main(gdir, xclose, odir):
    os.makedirs(odir, exist_ok=True)
    peak = json.load(open(xclose))['grid']['x0_at_peak']
    arr, rep = {}, {}
    for a in ('lcdm', 'cr'):
        g = np.load(os.path.join(gdir, f'grid_{a}.npz'))
        eta, x0, vis = np.asarray(g['eta']), np.asarray(g['x0']), np.asarray(g['vis'])
        g1 = bool(np.all(eta + x0 == float(g['eta_0'])))
        window_rule(eta, float(g['eta_ls']), float(g['eta_ls_w']), a)      # G2: exits on failure
        xp = float(x0[int(np.argmax(vis))])
        g3 = xp == float(peak[a])
        rep[a] = dict(G1_eta_plus_x0_is_eta_0=g1, G2_window_rule=True, G3_x0_at_peak=xp,
                      G3_xmap_x0_at_peak=float(peak[a]), G3_identical=g3, n=int(eta.size))
        print(f'  {a}: G1 {g1}   G2 True   G3 {xp!r} vs {float(peak[a])!r} -> {g3}   n={eta.size}')
        arr[f'eta_{a}'], arr[f'x0_{a}'], arr[f'vis_{a}'] = eta, x0, vis
        for s in SCALARS:
            arr[f'{s}_{a}'] = np.float64(g[s])
    ok = all(r['G1_eta_plus_x0_is_eta_0'] and r['G3_identical'] for r in rep.values())
    rep['ok'] = ok
    if not ok:
        json.dump(rep, open(os.path.join(odir, 'closure.json'), 'w'), indent=1)
        print('  ⛔ a closure failed -- REFUSING, no blob written')
        return 1
    blob = os.path.join(odir, 'r7737_grid.npz')
    np.savez(blob, **arr, meta=json.dumps(dict(order='r7739', pairing='grid index (PREDICTION ①)',
                                               closure={k: v for k, v in rep.items()})))
    rep['blob'] = dict(path='r7737_grid.npz', bytes=os.path.getsize(blob),
                       sha256=hashlib.sha256(open(blob, 'rb').read()).hexdigest())
    json.dump(rep, open(os.path.join(odir, 'closure.json'), 'w'), indent=1)
    print(f"  BUILT {blob} ({rep['blob']['bytes']} B, sha256 {rep['blob']['sha256'][:16]})")
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:4]))
