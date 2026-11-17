#!/usr/bin/env python3
"""r7819 ⑥ (cc66): THE CONTROL ON THE FLUID PATH AT PLANCK'S PUBLISHED POINT.

P15 `l.857` prints *"Run on the flat-LambdaCDM arm it returns peaks at 220, 540 and
812 ... and a first-to-second height ratio of 2.1969 against a standard code's
2.200 -- agreement to 0.14%"*, and `l.877` says in as many words that this `0.14%`
belongs to the OTHER path from the one the cosmology's own number is taken in.

`r7813+70` measured the calibration through P15's matched locator on the
POLARISATION path: the instrument's 2.2026 against CAMB's 2.2123, 0.44%.  Its
receipt does not carry the fluid path, and `r7819` ⑥ hands that measurement here.

⛔ No fluid-path control at Planck's point exists: both `r7807` banks are `HIER=1`
(its launcher's own line 32), and the `_pol` suffix is the polarisation SAVE site,
not a second path.  So this runs it -- the same point and the same `LSTEP`/`LMAXL`
as `r7807`, with `HIER` UNSET, which is the only switch that moves.

Idempotent: it skips a finished bank, and refuses to start beside a running solver
read off `/proc/*/environ` rather than off a bare process-name test.
"""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
INSTR = os.path.join(BW, 'ACOUSTIC_two_arm.py')
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
STEM = 'r7819_control_planck2018_fluid_L2000'

#: r7807's point verbatim; HIER is the one switch that differs, and it is UNSET.
PLANCK = dict(ARM='lcdm', LH0='67.36', LOM='0.313773', WBH2='0.02237', NS='0.9649',
              LSTEP='8', LMAXL='2000')


def already_running():
    for d in glob.glob('/proc/[0-9]*/environ'):
        try:
            with open(d, 'rb') as f:
                env = f.read().decode('utf-8', 'replace')
        except OSError:
            continue
        if 'ACOUSTIC_two_arm' in env and STEM in env:
            return True
    return False


def main():
    save = os.path.join(OUT, STEM + '.npz')
    if os.path.exists(save):
        print(f'  skip -- {os.path.basename(save)} is already banked')
        return 0
    if already_running():
        print('  a solver for this stem is already running; not starting a second')
        return 0
    env = dict(os.environ, SAVE=save, **PLANCK)
    env.pop('HIER', None)                      # the fluid path is HIER UNSET, not HIER=0
    print(f'  === the control, FLUID path, Planck 2018 published point -> '
          f'{os.path.basename(save)}')
    rc = subprocess.call([sys.executable, '-u', INSTR], env=env, cwd=BW)
    print(f'  rc={rc};  banked={os.path.exists(save)}')
    return rc


if __name__ == '__main__':
    sys.exit(main())
