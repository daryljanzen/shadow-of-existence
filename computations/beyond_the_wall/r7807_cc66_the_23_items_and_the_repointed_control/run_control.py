"""r7807+cc66 item ②: the control run at Planck 2018's PUBLISHED base-LCDM best fit.

69's order: run the control, NOT a stencil, at
    H0 67.36,  omega_b 0.02237,  omega_c 0.1200,  n_s 0.9649
and bank it WITH a `config` so it can never join an undecidable list.

The instrument takes Omega_m, not omega_c, so the point converts at ITS OWN h:
    Omega_m = (0.1200 + 0.02237) / 0.6736**2 = 0.313773
⛔ and the instrument carries NO NEUTRINO MASS -- a massless free-streaming hierarchy (LN, FNU,
DNEFF) and no `mnu` anywhere -- while Planck's published fit assumes sum m_nu = 0.06 eV.  So this is
Planck's POINT in this instrument, not Planck's MODEL.  Said here and in the receipt.

LMAXL=2000 / LSTEP=8 / HIER=1 matches the 185-bin configuration the published 0.918 is scored on.
POLSAVE is on for the EE and TE fourth-feature differences; r7807+cc66 gave it a `config` first.

IDEMPOTENT: a finished `.npz` is skipped, so a container restart costs nothing.  A running solver is
detected by reading /proc/*/environ for ACOUSTIC_two_arm, never by a bare pgrep name test.

Run: python3 run_control.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
INSTR = os.path.join(BW, 'ACOUSTIC_two_arm.py')
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

PLANCK = dict(ARM='lcdm', LH0='67.36', LOM='0.313773', WBH2='0.02237', NS='0.9649',
              HIER='1', LSTEP='8', LMAXL='2000')
STEM = 'r7807_control_planck2018_L2000'


def already_running():
    """A running ACOUSTIC_two_arm, excluding this process's own ancestry."""
    mine = {os.getpid(), os.getppid()}
    for d in os.listdir('/proc'):
        if not d.isdigit() or int(d) in mine:
            continue
        try:
            with open(f'/proc/{d}/environ', 'rb') as f:
                env = f.read().decode('utf-8', 'replace')
        except (OSError, PermissionError):
            continue
        if 'ACOUSTIC_two_arm' in env and 'r7807_control' in env:
            return int(d)
    return None


save = os.path.join(OUT, STEM + '.npz')
pols = os.path.join(OUT, STEM + '_pol.npz')
if os.path.exists(save) and os.path.exists(pols):
    print(f'  skip: both banks already exist\n    {save}\n    {pols}')
    sys.exit(0)
pid = already_running()
if pid:
    print(f'  skip: a run is already in flight at pid {pid}')
    sys.exit(0)

env = dict(os.environ, SAVE=save, POLSAVE=pols, **PLANCK)
assert 'mnu' not in env and 'MNU' not in env, 'the instrument takes no neutrino mass; see the docstring'
print('  switches: ' + ' '.join(f'{k}={v}' for k, v in sorted(PLANCK.items())))
print(f'  SAVE    {save}\n  POLSAVE {pols}\n')
r = subprocess.run([sys.executable, '-u', INSTR], env=env, cwd=BW)
print(f'\n  instrument rc={r.returncode}')
sys.exit(r.returncode)
