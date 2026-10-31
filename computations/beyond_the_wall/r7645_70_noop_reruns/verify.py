"""r7645+70: the fresh no-op re-runs (LEAFREC=1 set) against r7643's banked `__*cr_leafrec1` keys and the screen's
`Dl__base`; zp_wblo (the control, LEAFREC=1) against the namesake `r6897_fields` wblo keys; item 2's key coverage.
Logs are copied beside this file (logs/) as the runs' provenance."""
import json
import os
import shutil
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank5')
fail, out = [], []
os.makedirs(os.path.join(HERE, 'logs'), exist_ok=True)


def rc(log):
    return next((int(l.split('rc=')[1]) for l in open(log) if l.startswith('__DONE__')), None)


def sw(log):
    return next((l.split(None, 1)[1].strip() for l in open(log) if l.startswith('__SWITCHES__ ')), '?')


base = np.load(os.path.join(SP, 'r6893_switch_screen_cr_leafrec1.npz'), allow_pickle=True)['Dl__base']
RUNS = {'r6897_noop_cr': ('r6897_noop', 'Dl__cr_leafrec1'), 'r6911_noop_cr': ('r6911_noop', 'Dl__noop_cr_leafrec1'),
        'r6911_xsonly_cr': ('r6911_noop', 'Dl__xsonly_cr_leafrec1'), 'r6915_noop_cr': ('r6915_noop', 'Dl__noop_cr_leafrec1'),
        'r6919_noop_cr': ('r6919_noop', 'Dl__noop_cr_leafrec1'), 'r6925_noop_cr': ('r6925_noop', 'Dl__noop_cr_leafrec1'),
        'r6929_unset_cr': ('r6929_noop', 'Dl__unset_cr_leafrec1'), 'r6929_zero_cr': ('r6929_noop', 'Dl__zero_cr_leafrec1')}
out.append(f"{'run':>18} {'rc':>3} {'LEAFREC set':>11} {'= r7643 key':>12} {'= screen base':>14}  switches")
for tag, (bank, key) in RUNS.items():
    log = f'{D}/{tag}.log'
    shutil.copy(log, os.path.join(HERE, 'logs', tag + '.log'))
    r, s = rc(log), sw(log)
    d = np.load(f'{D}/{tag}.npz', allow_pickle=True)
    cfg = json.loads(str(d['config']))
    old = np.load(os.path.join(SP, bank + '_leafrec1.npz'), allow_pickle=True)[key]
    eq_old, eq_base = np.array_equal(d['Dl'], old), np.array_equal(d['Dl'], base)
    out.append(f"{tag:>18} {r:>3} {str('LEAFREC=1' in s and cfg.get('LEAFREC') is True):>11} {str(eq_old):>12} "
               f"{str(eq_base):>14}  {s}")
    if r != 0 or not eq_old or not eq_base or 'LEAFREC=1' not in s:
        fail.append(f'{tag}: rc {r}, = r7643 {eq_old}, = base {eq_base}')

# the control's lower baryon density, against the namesake's fields
shutil.copy(f'{D}/zp_wblo.log', os.path.join(HERE, 'logs', 'zp_wblo.log'))
f = np.load(f'{D}/fields_wblo.npz', allow_pickle=True)
o = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
worst = 0.0
for k in f.files:
    if f'{k}__wblo' not in o.files:
        continue
    a, b = np.asarray(f[k]), np.asarray(o[f'{k}__wblo'])
    if a.dtype.kind in 'fc' and a.shape == b.shape:
        worst = max(worst, float(np.max(np.abs(a - b)) / max(np.max(np.abs(b)), 1e-300)))
    elif a.shape != b.shape or (a.dtype.kind not in 'fc' and not np.array_equal(a, b)):
        fail.append(f'wblo {k}: differs in shape/content')
out.append(f'zp_wblo (control, LEAFREC=1 set) against the namesake r6897_fields wblo: max relative |d| = {worst:.2e} '
           f'over {len([k for k in f.files if k + "__wblo" in o.files])} keys')
if worst > 1e-12:
    fail.append(f'wblo moves: {worst:.2e}')

# item 2: every key of r6919_geometry's cr arm carried under __cr_leafrec1
g = np.load(os.path.join(SP, 'r6919_geometry_leafrec1.npz'), allow_pickle=True)
need = [k.replace('__cr', '__cr_leafrec1') for k in g.files if k.endswith('__cr')]
miss = [k for k in need if k not in g.files]
out.append(f'r6919_geometry_leafrec1: {len(need) - len(miss)} of {len(need)} cr keys carried under __cr_leafrec1')
if miss:
    fail.append(f'r6919_geometry missing {miss}')
print('\n'.join(out))
print('\n'.join(['FAILS:'] + fail) if fail else 'every prediction holds')
sys.exit(1 if fail else 0)
