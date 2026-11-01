"""r7651+70 ①: solve SRCTAPER for the control so its band-summed window spread equals the ARM OF RECORD's, in each
arm's own r_s -- predict.py's own `amp`/`sig_all` and bisection, lifted unchanged; the banked eta profiles."""
import ast
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
SP = os.path.join(BW, 'spectra')
P = os.path.join(BW, 'r6959_directions', 'predict.py')
NF = 3.0
ns = {'np': np, 'NF': NF}
tree = ast.parse(open(P).read())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in ('cut', 'amp', 'sig_all')],
                        type_ignores=[]), P, 'exec'), ns)
sig_all = ns['sig_all']
L = np.load(os.path.join(SP, 'r6959_eta_lcdm.npz'))
C = np.load(os.path.join(SP, 'r6959_eta_cr_leafrec1.npz'))
C0 = np.load(os.path.join(SP, 'r6959_eta_cr.npz'))
old = np.load(os.path.join(SP, 'r6959_swap_lcdm.npz'))
s_l, s_c = sig_all(L), sig_all(C)
tgt_frac = s_c / float(C['r_s'])
tgt = tgt_frac * float(L['r_s'])
lo, hi = -0.5 / max(s_l, tgt) ** 2, 50.0 / max(s_l, tgt) ** 2
for _ in range(80):
    al = 0.5 * (lo + hi)
    if sig_all(L, taper=al) > tgt:
        lo = al
    else:
        hi = al
s0 = float(L['rs_leaf'][int(np.argmin(np.abs(L['eta'] - float(L['eta_ls']))))])
print(f"control spread {s_l / float(L['r_s']):.5f} of r_s; namesake arm {sig_all(C0) / float(C0['r_s']):.5f}; "
      f"arm of record {tgt_frac:.5f}")
print(f"banked SRCTAPER {float(old['taper']):.8g} at s0 {float(old['taper_s0']):.6f}; "
      f"re-solved SRCTAPER = {al:.10g} at s0 {s0:.6f} (same s0: {abs(s0 - float(old['taper_s0'])) < 1e-9})")
print(f"check: control at the new coefficient {sig_all(L, taper=al) / float(L['r_s']):.5f} of r_s")
json.dump(dict(alpha=al, s0=float(old['taper_s0']), target_frac=tgt_frac, sigma_lcdm=s_l, sigma_cr_leafrec1=s_c,
               alpha_banked=float(old['taper'])), open(os.path.join(HERE, 'taper.json'), 'w'), indent=1)
