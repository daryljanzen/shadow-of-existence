# -*- coding: utf-8 -*-
"""r7860 (60) Ⓓ④ -- THE BANK STOPS LIVING IN `/tmp`, AND THAT IS MEASURED, NOT READ OFF A DEFAULT.

⛭ `r7857` (69) ruling ③: three banks on this line were lost to `/tmp` defaults -- the `555`-bin
mask, the Phi bandpowers and the CMB grid -- so point the defaults into the repository, or commit
what `model3` and `model6` read, so the next seat can read the bank the control was scored on.

⛔ **WHAT WOULD NOT BE A MEASUREMENT.**  Reading the new default off the source and saying it points
into the repository.  So this runs a SUBPROCESS with `POL_DIR` and `PPGRID` stripped from its
environment, has it resolve and load what the scorers read, and prints the resolved path -- which
must be under the repository and must carry the files.

⌗ And a NEGATIVE CONTROL, because a loader that silently tolerated an empty directory would pass the
positive leg while establishing nothing: the same subprocess is run with the variable pointed at an
EMPTY directory and must FAIL.

    python3 bank_in_repo.py        # rc=0 when both legs hold
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
#: ⛔ FOUR dirnames: this file sits three directories below the repository root.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7842 = os.path.join(BW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_'
                         'harness_does_not_have')
R7846 = os.path.join(BW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')

PROBE = r'''
import json, os, sys
sys.path.insert(0, %r)
sys.path.insert(0, %r)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
import model3 as M3
import model6 as M6
mod = M6.Model6('lcdm')
chi2 = float(mod.cmb.chi2_cmb([0.0] * 4, 0.06))
print(json.dumps(dict(pol_dir=M3.POL_DIR, ppgrid=M6.GRID, chi2=chi2,
                      n_pol=len([f for f in os.listdir(M3.POL_DIR) if f.endswith('.npz')]),
                      n_pp=len(os.listdir(M6.GRID)),
                      pol_in_repo=os.path.abspath(M3.POL_DIR).startswith(%r),
                      pp_in_repo=os.path.abspath(M6.GRID).startswith(%r))))
''' % (R7846, R7842, os.path.abspath(ROOT), os.path.abspath(ROOT))


def run(extra=None):
    env = {k: v for k, v in os.environ.items() if k not in ('POL_DIR', 'PPGRID')}
    if extra:
        env.update(extra)
    return subprocess.run([sys.executable, '-c', PROBE], cwd=BW, env=env, capture_output=True)


print(__doc__)
print('=' * 100)
print('\n  Ⓓ④ WITH `POL_DIR` AND `PPGRID` STRIPPED FROM THE ENVIRONMENT')
print('  ' + '-' * 98)
r = run()
ok, info = False, {}
if r.returncode == 0:
    info = json.loads(r.stdout.decode().strip().splitlines()[-1])
    print('    resolved POL_DIR : %s' % os.path.relpath(info['pol_dir'], ROOT))
    print('    resolved PPGRID  : %s' % os.path.relpath(info['ppgrid'], ROOT))
    print('    files            : %d banked spectra, %d lensing files'
          % (info['n_pol'], info['n_pp']))
    print('    and it SCORES    : chi2 = %.4f at the control point' % info['chi2'])
    ok = bool(info['pol_in_repo'] and info['pp_in_repo'])
    print('    both under the repository: %s' % ok)
else:
    print('    ⛔ the probe failed with no environment set:')
    sys.stderr.write(r.stdout.decode()[-1500:] + r.stderr.decode()[-1500:])

print('\n  Ⓓ④ᵃ THE NEGATIVE CONTROL -- an EMPTY bank directory must FAIL')
print('  ' + '-' * 98)
tmp = tempfile.mkdtemp(prefix='r7860_empty_')
try:
    bad = run({'POL_DIR': tmp})
    failed = bad.returncode != 0
    print('    with POL_DIR at an empty directory the probe exits %d -- %s'
          % (bad.returncode, 'FAILS as it must' if failed else '⛔ PASSED, which it must not'))
finally:
    shutil.rmtree(tmp, ignore_errors=True)

holds = bool(ok and failed)
with io.open(os.path.join(_HERE, 'bank_in_repo.json'), 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(dict(holds=holds, resolved=info, empty_dir_fails=bool(failed)),
                        indent=1, sort_keys=True))
print('\n  %s Ⓓ④ %s' % ('✔' if holds else '⛔', 'holds' if holds else 'FAILS'))
sys.exit(0 if holds else 1)
