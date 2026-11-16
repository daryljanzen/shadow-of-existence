"""r7809+cc66: the re-pointed control at LSTEP=2, the sampling P15's FINE-GRID figures read.

⛔ ** WHY THIS RUN EXISTS, AND IT IS A CORRECTION TO THE ORDER'S PREMISE. **  `r7809` says to
re-derive the list "on the bank you have just run".  That bank --
`r7807_control_planck2018_L2000.npz` -- is `LSTEP=8`: `238` samples on `100 <= l <= 1996`, which is
the 185-bin configuration the published `0.918` is scored on, and it served that figure exactly.

** But the control bank P15's fine-grid figures actually read is `spectra/cc66_lcdm_L2000.npz`, and
that one is `LSTEP=2`: `950` samples on `100 <= l <= 1998`. **  A step-8 bank cannot stand in for a
step-2 one: interpolating onto the finer grid would change the measurement rather than re-derive it,
and a peak located by a parabola on a coarse grid is not the same estimator as one located on the
fine grid.  Reporting those figures off the step-8 bank would be a stencil wearing a run's clothes,
which is exactly the `r7805` lesson the registration named in advance.

⇒ So this launches the SAME point at the SAME form as `cc66_lcdm_L2000.npz`: `LSTEP=2`.
  Everything else is `r7807`'s run verbatim, so the only difference between the two banks is the
  sampling, and the only difference from `cc66_lcdm_L2000.npz` is the point -- which is what makes
  the comparison a re-derivation of the figure and not a new estimator.

⛔ And the caveat r7807 established carries unchanged: the instrument has NO NEUTRINO MASS, so this
is Planck's POINT in this instrument and not Planck's MODEL.

IDEMPOTENT: a finished `.npz` is skipped, so a container restart costs nothing.  A running solver is
detected by reading /proc/*/environ for ACOUSTIC_two_arm, never by a bare pgrep name test.

Run: python3 run_control_fine.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
INSTR = os.path.join(BW, 'ACOUSTIC_two_arm.py')
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

#: r7807's point verbatim; only LSTEP moves, from 8 to 2, to match cc66_lcdm_L2000.npz's form.
PLANCK = dict(ARM='lcdm', LH0='67.36', LOM='0.313773', WBH2='0.02237', NS='0.9649',
              HIER='1', LSTEP='2', LMAXL='2000')
STEM = 'r7809_control_planck2018_L2000_step2'


def already_running():
    """A running ACOUSTIC_two_arm for THIS stem, excluding this process's own ancestry."""
    mine = {os.getpid(), os.getppid()}
    for d in os.listdir('/proc'):
        if not d.isdigit() or int(d) in mine:
            continue
        try:
            with open(f'/proc/{d}/environ', 'rb') as f:
                env = f.read().decode('utf-8', 'replace')
        except (OSError, PermissionError):
            continue
        if 'ACOUSTIC_two_arm' in env and 'r7809_control' in env:
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
