#!/usr/bin/env python3
"""r7703+70 item 1 (usage: diag_ns3.py NS3 [KEY=VAL ...]; DIAG_OUT sets where the dump goes): run the receipt's own `_RUN` (read from its source) at a given NS3 on FROZEN (L), distances point,
with a dump appended: the stored E, the stored Phi/Theta0 at three k, the per-l Cd/Cc, and H.eta_end/eta_0/_EFINE."""
import importlib.util, os, sys, subprocess, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); BW = os.path.join(HERE, '..')
_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s); _s.loader.exec_module(rl)
ns = rl.engine(); CASES = {k: env for k, w, env in rl.CASES if w == 'ADJ'}
BG = (68.60, 0.2973); ns['R0'].setdefault(BG, ns['r0_of'](*BG))
n3 = int(sys.argv[1]); XTRA = dict(a.split('=', 1) for a in sys.argv[2:])
SCR = os.environ.get('DIAG_OUT', HERE)   # the dumps are ~16 MB each: written to scratch, not committed
out = os.path.join(SCR, f'diag_ns3_{n3}' + ''.join(f'_{k}{v}' for k, v in XTRA.items()) + '.npz')
DUMP = f"""
np.savez({out!r}, E=E, Phi=Y[:,:,2], Th0=Y[:,:,0], kk=kk, Cc=Cc, Cd=Cd, ls=ls, r=r, e_sw=e_sw,
         eta_end=H.eta_end, eta_0=H.eta_0, eta_rec=H.eta_rec, D2=Delta(2))
"""
# r7705+70: the harness now carries the magnitude guard, which stops a blow-up before this dump. DIAG_PRE=<rev> runs
# the harness as it stood at that revision (the guard's own positive control is in r7705_70_magnitude_guard).
_RUN = ns['_RUN']
if os.environ.get('DIAG_PRE'):
    import ast
    _src = subprocess.run(['git', 'show', os.environ['DIAG_PRE'] + ':receipts/P15_CR_cosmology/'
                           'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py'],
                          cwd=HERE, capture_output=True, text=True).stdout
    _RUN = next(ast.literal_eval(n.value) for n in ast.parse(_src).body if isinstance(n, ast.Assign)
                and any(getattr(t, 'id', None) == '_RUN' for t in n.targets))
run = _RUN + DUMP
env = dict(os.environ, BH0=f"{BG[0]}", BOM=f"{BG[1]}", BR0=f"{ns['R0'][BG]:.10f}", HIER_DIR=ns['HIER_DIR'])
for k in ('ZEND', 'ZDEC', 'NTAU', 'KLO', 'NLOW', 'NS3', 'HKCAP'): env.pop(k, None)
env.update({k: str(v) for k, v in dict(CASES['FROZEN_adjudicated_KLO_0_1'], NS3=n3, SPLITCLOCK='L', **XTRA).items()})
p = subprocess.run([sys.executable, '-c', run], env=env, capture_output=True, text=True)
print(p.stdout[-600:], p.stderr[-1500:])
