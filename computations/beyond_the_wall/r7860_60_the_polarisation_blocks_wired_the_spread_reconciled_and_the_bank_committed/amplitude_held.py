# -*- coding: utf-8 -*-
"""r7860 (60) Ⓗ⑧ -- WHICH OF THIS SEAT'S THREE ABSOLUTE STATEMENTS ACTUALLY HOLDS THE AMPLITUDE.

⛭ `r7859` (69), on `cc66`'s measurement: in every scoring path they measured, the amplitude is
FITTED in closed form at the covariance-weighted optimum, so *"nothing fitted"* in this sector means
**no cosmological parameter fitted to the microwave data, not the amplitude held** — and doubling
every TT `D_\\ell` the bank hands them moved **zero** of their six verdicts.  ⇒ *The order asks this
seat to re-read its own three on that ground and say which, if any, actually holds the amplitude.*

⛔ **AND IT IS ANSWERED THE SAME WAY THEY ANSWERED IT, BY DOUBLING THE BANK AND RE-RUNNING** — not
by reading the source and deciding.  A doubled copy of the committed grid is built (exactly what the
switch does, measured exact elsewhere in this revision), each receipt is run against the normal bank
and against the doubled one, and the two verdicts are compared arm by arm.

  * a receipt whose verdict does NOT move lets the fit solve for the amplitude: its statement is
    about a SHAPE and the sweep was wrong to call it absolute;
  * a receipt whose verdict DOES move holds the amplitude, and its statement is genuinely absolute.

⌗ The comparison is on the PASS/FAIL pattern and the exit code, not on printed figures, because a
figure can move without a verdict moving and that is exactly the distinction being drawn.

    python3 amplitude_held.py
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
#: ⛔ FOUR dirnames: this file sits three directories below the repository root.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BANK = os.path.join(_BTW, 'bank', 'pol_grid')
MINE = [
    'receipts/P15_CR_cosmology/P15_more_information_made_the_control_worse_and_the_act_data_the_'
    'order_offered_was_already_banked_and_cannot_close_the_gap.py',
    'receipts/P15_CR_cosmology/P15_the_absolute_lensing_scale_is_two_factor_two_errors_that_'
    'cancelled_and_the_baryon_repair_broke_the_cancellation.py',
    'receipts/P15_CR_cosmology/P15_the_handover_belongs_late_not_early_and_an_independent_pipeline_'
    'already_installed_here_puts_the_lensing_fault_in_this_instrument.py',
]
BLOCKS = ('Dl', 'Dl_EE', 'Dl_TE')


def doubled_bank(dst):
    """every banked block times two -- what the switch does, applied to the grid itself"""
    os.makedirs(dst, exist_ok=True)
    n = 0
    for f in sorted(os.listdir(BANK)):
        if not f.endswith('.npz'):
            continue
        z = dict(np.load(os.path.join(BANK, f), allow_pickle=True))
        for k in BLOCKS:
            if k in z:
                z[k] = np.asarray(z[k], float) * 2.0
        np.savez(os.path.join(dst, f), **z)
        n += 1
    return n


def verdict(path, pol_dir):
    env = dict(os.environ)
    env['POL_DIR'] = pol_dir
    env['NODE'] = '60'
    r = subprocess.run([sys.executable, path], cwd=ROOT, env=env, capture_output=True)
    txt = r.stdout.decode()
    #: ⛔ ** TWO MARKER CONVENTIONS LIVE IN THIS CORPUS, and the first version of this comparator
    #:   only knew one. **  *`[PASS]`/`[FAIL]` is one; a bare tick or cross is the other, and the
    #:   lensing-scale receipt uses the second — so it came back `0 pass / 0 fail` and its verdict
    #:   comparison was VACUOUS while reporting `UNMOVED`.  Both are read now, and the whole
    #:   stdout is hashed beside them so that `unmoved` means the run did not differ AT ALL and not
    #:   merely that a pattern this comparator could parse did not.*
    marks = re.findall(r'\[(PASS|FAIL)\]|(\u2714)|(\u2718)', txt)
    flat = [m[0] or ('PASS' if m[1] else 'FAIL') for m in marks]
    import hashlib
    return dict(rc=int(r.returncode), n_pass=flat.count('PASS'), n_fail=flat.count('FAIL'),
                pattern=''.join('P' if m == 'PASS' else 'F' for m in flat),
                stdout_sha=hashlib.sha1(txt.encode('utf-8')).hexdigest()[:12],
                n_marks=len(flat))


print(__doc__)
print('=' * 100)
tmp = tempfile.mkdtemp(prefix='r7860_doubled_')
out = {}
try:
    n = doubled_bank(tmp)
    print('\n  a doubled copy of the committed grid: %d file(s)' % n)
    print('\n  Ⓗ⑧ EACH OF THIS SEAT\'S THREE, RUN AGAINST BOTH BANKS')
    print('  ' + '-' * 98)
    for path in MINE:
        a = verdict(path, BANK)
        b = verdict(path, tmp)
        moved = bool(a['rc'] != b['rc'] or a['pattern'] != b['pattern'])
        assert a['n_marks'] > 0, 'no verdict marks parsed: the comparison would be vacuous'
        name = os.path.basename(path)[:62]
        print('    %s' % name)
        print('      normal  rc=%d  %d pass / %d fail' % (a['rc'], a['n_pass'], a['n_fail']))
        print('      stdout differs at all: %s   (%d verdict mark(s) parsed)'
              % (a['stdout_sha'] != b['stdout_sha'], a['n_marks']))
        print('      doubled rc=%d  %d pass / %d fail   ⇒ verdict %s'
              % (b['rc'], b['n_pass'], b['n_fail'],
                 'MOVES -- it HOLDS the amplitude' if moved
                 else 'UNMOVED -- the fit solves for the amplitude'))
        out[os.path.basename(path)] = dict(normal=a, doubled=b, verdict_moves=moved,
                                           holds_the_amplitude=moved)
finally:
    shutil.rmtree(tmp, ignore_errors=True)

held = [k for k, v in out.items() if v['holds_the_amplitude']]
print('\n  ⇒ OF THIS SEAT\'S THREE, %d HOLD%s THE AMPLITUDE' % (len(held), '' if len(held) == 1
                                                               else ''))
for k in sorted(out):
    print('    %-8s %s' % ('HOLDS' if out[k]['holds_the_amplitude'] else 'does not', k[:78]))
if not held:
    print('\n    ** So the sweep at `r7858` was WRONG to call these three absolute, on the ground')
    print('       `r7859` names: they say "nothing fitted" about the COSMOLOGY and let the fit')
    print('       solve for the amplitude, exactly as `cc66`\'s six do. ⇒ This seat\'s three need')
    print('       no re-reading when the defaults change, and the sweep\'s phrase-matching is the')
    print('       thing that was too wide. **')
rec = dict(receipts=out, n_holding=len(held), holding=sorted(held),
           ground='r7859 (69), on cc66: "nothing fitted" means no cosmological parameter fitted, '
                  'not the amplitude held')
with io.open(os.path.join(_HERE, 'amplitude_held.json'), 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(rec, indent=1, sort_keys=True))
print('\n  wrote amplitude_held.json\n')
