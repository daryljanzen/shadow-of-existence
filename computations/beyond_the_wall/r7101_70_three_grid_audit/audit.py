"""r7101 (70) Q1 -- the audit of cc66's three-grid comparison, by the seat that did not produce it.
Pre-registered at PREDICTION.md beside this file.  Nothing is run through the transfer; every number is read
from the three banked grids through `r7091_70_fit_rigidity/rigidity.py`'s own definitions (imported, read-only),
and the receipt's nine headline numbers are additionally re-derived by running `rigidity.py` as a DRIVER.

  (1) LIKE-FOR-LIKE, from the artefacts: switches per step, ell sampling, controls byte-identical, rigidity.py
      as a subprocess, and the contrast coefficient c through `contrast_size.py`'s own model.
  (2) THE CEILING: k_max * D_M per arm from the logs; the three statistics re-fitted on data cut at ell_cut
      (sub-covariance, re-whitened, five directions re-projected -- a fit to fewer data, not a mask); and the
      share of the licensed-minus-forbidden chi^2 gap carried by the top bins.
  (3) THE OTHER WAY: per-band chi^2 on the full-range residual, the refit chi^2, low-frequency power, A0, peak
      ratios from the logs.

Usage:  python3 audit.py      (prints; the log beside it is this output)
"""
import contextlib
import hashlib
import io
import os
import re
import subprocess
import sys

import numpy as np
import scipy.linalg

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.abspath(os.path.join(HERE, '..'))
RIG = os.path.join(BW, 'r7091_70_fit_rigidity')
sys.argv = [sys.argv[0], '--mc', '1']
sys.path.insert(0, RIG)
with contextlib.redirect_stdout(io.StringIO()):
    import rigidity as R                                                    # noqa: E402

GRIDS = (('banked', os.path.join(BW, 'refit_grid185')),
         ('licensed', os.path.join(BW, 'r7095_directions', 'grid_licensed')),
         ('forbidden', os.path.join(BW, 'r7093_directions', 'grid_oneclock')))
TAGS = ['base'] + [f'{k}{s}' for k in R.STEP for s in 'pm']
RECEIPT = {('lcdm',): (186.007, 87, 8), 'banked': (278.795, 54, 33), 'licensed': (278.788, 54, 33),
           'forbidden': (184.989, 91, 8)}


def head(t):
    print('\n' + '=' * 100 + '\n  ' + t + '\n' + '=' * 100)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def sw(p):
    z = np.load(p, allow_pickle=False)
    if 'switches' not in z.files:
        return None
    d = dict(re.findall(r'(\w+)=(\S+)', str(z['switches'])))
    d.pop('SAVE', None)
    return d


# ===================================================================================================== (1)
head('(1) LIKE-FOR-LIKE, READ FROM THE ARTEFACTS')
ctrl = {t: {sha(os.path.join(g, f'lcdm_{t}.npz')) for _, g in GRIDS} for t in TAGS}
print(f'  control: {sum(len(v) == 1 for v in ctrl.values())} of {len(TAGS)} files byte-identical across all three grids')
for nm, g in GRIDS:
    ls = {tuple(np.load(os.path.join(g, f'{a}_{t}.npz'))['ls']) for a in ('lcdm', 'cr') for t in TAGS}
    print(f'  {nm:9s} ell samplings across its 18 files: {len(ls)} distinct; '
          f'{min(min(x) for x in ls)}..{max(max(x) for x in ls)}')
print('  switches, licensed against forbidden, per CR step (keys differing):')
diffs = set()
for t in TAGS:
    a = sw(os.path.join(GRIDS[1][1], f'cr_{t}.npz'))
    b = sw(os.path.join(GRIDS[2][1], f'cr_{t}.npz'))
    d = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    diffs.add(tuple(d))
    print(f'    cr_{t:5s} {d}')
print(f'  => {"ONE switch pair throughout: " + str(diffs) if len(diffs) == 1 else "MORE THAN ONE DIFFERENCE"}')
print('  the banked grid has no stamp; its launcher (refit_grid185/launch.sh) sets ZSTART=3e7 LEAFSCALES=1 and the'
      '\n  same parameter steps, and predates LEAFREC (so it ran at LEAFREC=0, the old behaviour).')

print('\n  rigidity.py run as a DRIVER on each grid (subprocess, --grid, --mc 2000), its own printed numbers:')
drv = {}
for nm, g in GRIDS:
    out = subprocess.run([sys.executable, os.path.join(RIG, 'rigidity.py'), '--mc', '2000', '--grid', g],
                         capture_output=True, text=True, cwd=RIG).stdout
    for arm, chi, cr in re.findall(r'^\s+(lcdm|cr)\s+rank.*?unreachable chi2 ([\d.]+) of.*?crossings (\d+)', out, re.M):
        drv[(nm, arm)] = (float(chi), int(cr))
    lr = re.findall(r'longest\s+data\s+([\d.]+)', out)
    lf = re.findall(r'lowfreq\s+data\s+([\d.]+)\s+noise\s+([\d.]+) \+-\s+([\d.]+)\s+([+-][\d.]+) sigma', out)
    for i, arm in enumerate(('lcdm', 'cr')):
        drv[(nm, arm)] += (int(float(lr[i])), tuple(float(v) for v in lf[i]))
    print(f'    {nm:9s} ' + '   '.join(f'{arm}: chi2 {drv[(nm, arm)][0]:.1f} crossings {drv[(nm, arm)][1]} '
                                       f'longest {drv[(nm, arm)][2]}' for arm in ('lcdm', 'cr')))


def reach(B, sel=None):
    """the receipt's reach exactly (rigidity.py's columns, W, QR projection, stats), optionally on the bins
    `sel` only: sub-covariance, its own Cholesky, the five directions re-projected on it"""
    cols = [B['m0'] * 0.02] + [B['g'][k] * R.STEP[k] for k in R.STEP]
    d = B['d']
    C, L = B['C'], B['L']
    if sel is not None:
        cols = [c[sel] for c in cols]
        d = d[sel]
        C = C[np.ix_(sel, sel)]
        L = np.linalg.cholesky(C)
    Wf = lambda v: scipy.linalg.solve_triangular(L, v, lower=True)       # noqa: E731
    Jw = np.column_stack([Wf(c) for c in cols])
    dw = Wf(d)
    Q, _ = np.linalg.qr(Jw)
    rw = dw - Q @ (Q.T @ dw)
    st = R.stats((L @ rw) / np.sqrt(np.diag(C)))
    return float(rw @ rw), st, rw, (L @ rw) / np.sqrt(np.diag(C)), len(d)


BB, V = {}, {}
for nm, g in GRIDS:
    R.GRID = g
    for arm in ('lcdm', 'cr'):
        with contextlib.redirect_stdout(io.StringIO()):
            BB[(nm, arm)] = R.build(arm)
        V[(nm, arm)] = reach(BB[(nm, arm)])
print('\n  the same through the imported definitions (the receipt\'s own route), and the receipt\'s literals:')
for nm, _ in GRIDS:
    for arm in ('lcdm', 'cr'):
        c, st, *_ = V[(nm, arm)]
        lit = RECEIPT[('lcdm',)] if arm == 'lcdm' else RECEIPT[nm]
        ok = abs(c - lit[0]) < 6e-4 and st['crossings'] == lit[1] and st['longest'] == lit[2] \
            and abs(drv[(nm, arm)][0] - c) < 0.06 and drv[(nm, arm)][1] == st['crossings'] \
            and drv[(nm, arm)][2] == st['longest']
        print(f'    {nm:9s} {arm:4s} chi2 {c:10.4f} (receipt {lit[0]:8.3f})  crossings {st["crossings"]:3d} '
              f'({lit[1]})  longest {st["longest"]:3d} ({lit[2]})   {"REPRODUCED" if ok else "** DIFFERS **"}')

print('\n  the contrast coefficient c (contrast_size.py\'s model: five directions + contrast template, GLS):')
CC = {}
for nm, _ in GRIDS:
    for arm in ('lcdm', 'cr'):
        B = BB[(nm, arm)]
        cols = [B['m0'] * 0.02] + [B['g'][k] * R.STEP[k] for k in R.STEP] + [B['contrast']]
        Jw = np.column_stack([R.W(B, c) for c in cols])
        x, *_ = np.linalg.lstsq(Jw, R.W(B, B['d'] - B['m0']), rcond=None)
        e = np.sqrt(np.diag(np.linalg.inv(Jw.T @ Jw)))
        CC[(nm, arm)] = (x[-1], e[-1])
        print(f'    {nm:9s} {arm:4s} c = {x[-1]:+.4f} +- {e[-1]:.4f}   ({x[-1] / e[-1]:+.2f} sigma)')

# ===================================================================================================== (2)
head('(2) THE CEILING')
for nm, g in GRIDS[1:]:
    t = open(os.path.join(g, 'cr_base.log')).read()
    km = re.search(r'k_max = (\d+)/D_M against a reported l_max = (\d+) -> ratio ([\d.]+)', t)
    ld = re.search(r'l_D = (\d+)', t)
    print(f'  {nm:9s} projection reach k_max*D_M = {km.group(1)} at l_max {km.group(2)} (ratio {km.group(3)}); '
          f'D_M {float(np.load(os.path.join(g, "cr_base.npz"))["D_M"]):.1f};  l_D = {ld.group(1)}  '
          f'-> l_max/l_D = {2000 / int(ld.group(1)):.3f}')
print('  => k_max is held as a multiple of 1/D_M, so the projection reaches the same multipole on every arm;')
print('     the coupling "k_max fixed, D_M smaller" is not what the instrument does.')

hi = (R.CS.BIN_HI)[BB[('banked', 'cr')]['ok']]
lo = (R.CS.BIN_LO)[BB[('banked', 'cr')]['ok']]
print(f'\n  bins used: {len(hi)}, ell {lo.min():.0f}..{hi.max():.0f}  (plik_lite bins above the spectra\'s 1996 are dropped)')
CUTS = [850, 1000, 1200, 1400, 1600, 1800, 1900, int(hi.max())]
print(f'\n  the three statistics re-fitted on ell <= cut  (chi2 / n-5  crossings  longest), and the arm gap:')
print(f'    {"cut":>5s} {"n":>4s}  ' + '  '.join(f'{f"{nm} {arm}":>26s}' for nm, _ in GRIDS for arm in ('cr',))
      + f'  {"control":>24s}   {"lic-forb dchi2":>14s}')
CUT = {}
for cut in CUTS:
    sel = hi <= cut
    row = {}
    for nm, _ in GRIDS:
        for arm in ('lcdm', 'cr'):
            c, st, _, _, n = reach(BB[(nm, arm)], sel)
            row[(nm, arm)] = (c, st['crossings'], st['longest'], n)
    CUT[cut] = row
    n = row[('banked', 'cr')][3]
    print(f'    {cut:5d} {n:4d}  ' + '  '.join(
        f'{row[(nm, "cr")][0]:8.1f}/{n - 5:<4d} {row[(nm, "cr")][1]:4d} {row[(nm, "cr")][2]:4d}  ' for nm, _ in GRIDS)
        + f'{row[("banked", "lcdm")][0]:8.1f} {row[("banked", "lcdm")][1]:4d} {row[("banked", "lcdm")][2]:4d}    '
        f'{row[("licensed", "cr")][0] - row[("forbidden", "cr")][0]:+10.1f}')

# where in ell the full-range gap sits: the full-range whitened residual is in the Cholesky basis, which is
# ordered by bin and lower-triangular, so its squared components accumulate in ell order
print('\n  the full-range gap, accumulated in ell (whitened residual, Cholesky ordered by bin):')
rl = V[('licensed', 'cr')][2] ** 2
rf = V[('forbidden', 'cr')][2] ** 2
rc = V[('banked', 'lcdm')][2] ** 2
gap = rl.sum() - rf.sum()
BANDS = [(0, 500), (500, 850), (850, 1200), (1200, 1500), (1500, 1800), (1800, 2000)]
print(f'    {"band":>12s} {"n":>4s} {"licensed":>9s} {"forbidden":>10s} {"control":>8s} {"lic-forb":>9s} {"share of gap":>13s}')
for a, b in BANDS:
    m = (hi > a) & (hi <= b)
    print(f'    {f"({a},{b}]":>12s} {m.sum():4d} {rl[m].sum():9.1f} {rf[m].sum():10.1f} {rc[m].sum():8.1f} '
          f'{rl[m].sum() - rf[m].sum():+9.1f} {100 * (rl[m].sum() - rf[m].sum()) / gap:12.1f}%')

# ===================================================================================================== (3)
head('(3) DOES ANYTHING IN THE BANKED SET POINT THE OTHER WAY')
print(f'    {"":10s} {"A0":>8s} {"refit chi2":>11s} {"lowfreq (driver)":>26s}')
for nm, _ in GRIDS:
    B = BB[(nm, 'cr')]
    with contextlib.redirect_stdout(io.StringIO()):
        x, A, mfit, c0, c1 = R.bestfit(B)
    lf = drv[(nm, 'cr')][3]
    print(f'    {nm:10s} {B["A0"]:8.4f} {c1:11.1f}   {lf[0]:.3f} vs noise {lf[1]:.3f}+-{lf[2]:.3f} ({lf[3]:+.1f}s)')
B = BB[('banked', 'lcdm')]
with contextlib.redirect_stdout(io.StringIO()):
    _, _, _, _, c1 = R.bestfit(B)
lf = drv[('banked', 'lcdm')][3]
print(f'    {"control":10s} {B["A0"]:8.4f} {c1:11.1f}   {lf[0]:.3f} vs noise {lf[1]:.3f}+-{lf[2]:.3f} ({lf[3]:+.1f}s)')
print('\n  peak structure printed by the instrument at each arm\'s base (line-of-sight, hierarchy):')
for nm, g in GRIDS[1:]:
    t = open(os.path.join(g, 'cr_base.log')).read()
    print(f'    {nm:9s} ' + re.search(r'peaks at l = .*', t).group(0) + '   '
          + re.search(r'l_1/l_A = .*', t).group(0).strip())
print('  (the control\'s base has no log banked beside the grids; its peak ratios are not compared here)')
