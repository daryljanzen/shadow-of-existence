#!/usr/bin/env python3
"""r7783+cc66: FAILABILITY of the low-ell depths receipt, MEASURED and not asserted.

Perturbs the ONE-RATE arm-A leg by a 1 + 2e-3 scaling -- far smaller than the moves the receipt
reports -- and reports which of the eight gates go red.  A pin that does not move under this is not
a pin.
"""
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RD = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
RCPT = os.path.join(RD, 'P15_the_printed_low_multipole_depths_are_the_arm_of_records_and_on_the_one_'
                        'rate_they_are_0_490_0_435_0_359_0_668.py')
SCALE = 1.0 + 2e-3
src = open(RCPT, encoding='utf-8').read()
for _rl, _new in (("HERE = os.path.dirname(os.path.abspath(__file__))", f'HERE = {RD!r}'),
                  ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", f'ROOT = {ROOT!r}')):
    assert _rl in src, f'the receipt has moved; this rewrites it by: {_rl}'
    src = src.replace(_rl, _new)
anchor = "tex = open(TEX, encoding='utf-8').read()"
assert anchor in src, 'the receipt has moved; this probe reads it by that line'
hacked = src.replace(anchor, anchor + f"\nA_1 = A_1 * {SCALE!r}   # r7783 failability probe")


def run(text, tag):
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, 'probe.py')
        open(p, 'w', encoding='utf-8').write(text)
        r = subprocess.run([sys.executable, '-I', p], capture_output=True, text=True, cwd=RD)
    v = {}
    n = 0
    for ln in r.stdout.splitlines():
        m = re.match(r'\s*\[(PASS|FAIL)\]', ln)
        if m:
            n += 1
            v[n] = m.group(1)
    print(f'  {tag:26s} rc={r.returncode}  ' + ' '.join(f'{k}:{s[0]}' for k, s in sorted(v.items())))
    return r.returncode, v


print(__doc__)
rc0, v0 = run(src, 'unperturbed')
rc1, v1 = run(hacked, f'one-rate armA x {SCALE}')
moved = sorted(k for k in v0 if v0[k] == 'PASS' and v1.get(k) == 'FAIL')
held = sorted(k for k in v0 if v0[k] == 'PASS' and v1.get(k) == 'PASS')
print(f'\n  gates that go RED under the perturbation: {moved}')
print(f'  gates that hold (the (L) legs, the paper\'s text, the refit point, the blobs): {held}')
ok = rc0 == 0 and rc1 != 0 and moved
print(f'\n  {"PASS" if ok else "FAIL"}  the pins are failable: unperturbed rc={rc0}, '
      f'perturbed rc={rc1}, {len(moved)} gate(s) move')
raise SystemExit(0 if ok else 1)
