"""r7651+70 ①: fold the eleven slices into spectra/r6959_swap_lcdm_leafrec1.npz by r6959_directions/bank.py's own
`fold` (lifted unchanged), in the namesake's form, plus `config`, `taper_target` and `manifest`.  An ADDITION:
the namesake and the other five tapered banks are not touched.  Gates: rc=0 on every slice, the slices tile,
the coefficient is on the switch line; the < 0.5% move is a reported prediction."""
import ast
import glob
import json
import os
import shutil
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
SP = os.path.join(BW, 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank7')
fail = []
B = os.path.join(BW, 'r6959_directions', 'bank.py')
ns = {'np': np, 'os': os, 're': __import__('re'), 'D': os.path.dirname(D), 'STEP': 250, 'NK': 2547}
tree = ast.parse(open(B).read())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'fold'],
                        type_ignores=[]), B, 'exec'), ns)
os.makedirs(os.path.join(HERE, 'logs_taper'), exist_ok=True)
for q in sorted(glob.glob(f'{D}/swap_lcdm_k*.log')):
    shutil.copy(q, os.path.join(HERE, 'logs_taper'))
    if not any(l.startswith('__DONE__ rc=0') for l in open(q)):
        fail.append(f'{os.path.basename(q)}: not rc=0')
out = ns['fold']('swap_lcdm', os.path.basename(D))
TJ = json.load(open(os.path.join(HERE, 'taper.json')))
cfg = np.load(f'{D}/swap_lcdm_k0.npz', allow_pickle=True)['config']
sw = next((l.split(None, 1)[1].strip() for l in open(f'{D}/swap_lcdm_k0.log') if l.startswith('__SWITCHES__ ')), '')
if f"SRCTAPER={'%.10g' % TJ['alpha']}" not in sw:
    fail.append(f'SRCTAPER not on the switch line: {sw}')
out.update(taper=float(TJ['alpha']), taper_s0=float(TJ['s0']), taper_all=0, taper_norm=0,
           taper_target=float(TJ['target_frac']), config=cfg)
man = dict(file='spectra/r6959_swap_lcdm_leafrec1.npz', namesake='spectra/r6959_swap_lcdm.npz',
           form="ADDITION (r7647 convention): a sibling of the namesake swap, its keys; the namesake and the other five "
                "tapered banks unchanged",
           arm='the CONTROL (LEAFREC does not reach it); the coefficient is what is for the arm of record',
           taper=TJ['alpha'], taper_banked=TJ['alpha_banked'], taper_s0=TJ['s0'],
           target=f"the arm of record's band-summed window spread {TJ['target_frac']:.6f} of its own r_s "
                  f"(sig_all(r6959_eta_cr_leafrec1)/r_s; the namesake targeted 0.06424)",
           switches=sw, held="r6959_directions/launch_b.sh's swap_lcdm verbatim (LSTEP=1 LMAXL=2000, eleven 250-mode "
                             "slices, its switch-line guard) at the re-solved SRCTAPER; folded by bank.py's own fold",
           reader='receipts/P15_CR_cosmology/P15_the_windows_phase_spread_is_nearly_equal_because_the_visibility_'
                  'widens_as_the_leaf_clock_slows.py')
out['manifest'] = np.array(json.dumps(man))
old = np.load(os.path.join(SP, 'r6959_swap_lcdm.npz'), allow_pickle=True)
miss = [k for k in old.files if k not in out]
if miss:
    fail.append(f'form: missing {miss}')
np.savez(os.path.join(SP, 'r6959_swap_lcdm_leafrec1.npz'), **out)
same = np.array_equal(old['ls'], out['ls'])
mv = float(np.max(np.abs(out['Dl'] - old['Dl'])) / np.max(np.abs(old['Dl']))) if same else float('nan')
un = np.load(os.path.join(SP, 'r6941_fine_lcdm.npz'))
mu = float(np.max(np.abs(out['Dl'] - un['Dl'])) / np.max(np.abs(un['Dl']))) if np.array_equal(un['ls'], out['ls']) else float('nan')
mo = float(np.max(np.abs(old['Dl'] - un['Dl'])) / np.max(np.abs(un['Dl']))) if np.array_equal(un['ls'], old['ls']) else float('nan')
print(f"{len(out['ls'])} multipoles; SRCTAPER {TJ['alpha']:.10g} (banked {TJ['alpha_banked']:.10g}); target {TJ['target_frac']:.5f}")
print(f"against the namesake swap: same ls {same}, max |dD_l| / peak = {mv:.3e}")
print(f"the taper's own effect (vs the untapered control r6941_fine_lcdm): new {mu:.3e}, namesake {mo:.3e} of peak")
# the registered PREDICTION (< 0.5% of peak) is reported, not gated: it MISSED (0.93%), and a missed prediction
# is a finding, not a fold defect -- the taper's own effect moves 4.20% -> 3.29% of peak with the coefficient
print(f"PREDICTION (registered < 0.5% of peak): {'HOLDS' if mv < 5e-3 else 'MISSED'} at {100 * mv:.2f}%")
print('\n'.join(['FAILS:'] + fail) if fail else 'all gates hold')
sys.exit(1 if fail else 0)
