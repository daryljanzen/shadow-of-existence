#!/usr/bin/env python3
"""r7783+cc66: FAILABILITY of the opening-figures receipt, MEASURED and not asserted.

Scales the ONE-RATE arm's Dl by 1 + 2e-3 -- far smaller than the moves the receipt reports -- and
reports which of the eight gates go red.  A pin that does not move under this is not a pin.

⛔ The receipt's docstring claimed this measurement before this file existed.  That was a false
claim in a landed receipt, caught by `check_marker_transposition`'s sibling run at r7783+cc66.13;
the measurement below is the real one and the docstring is corrected to match it.
"""
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RD = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
RCPT = os.path.join(RD, 'P15_the_sections_opening_figures_on_the_one_rate_and_the_published_comb_'
                        'is_298_5_not_298_94.py')
SCALE = 1.0 + 2e-3
src = open(RCPT, encoding='utf-8').read()
# FIRST OCCURRENCE ONLY: these two literals also appear as the receipt's own rewrite targets.
for rl, new in (("HERE = os.path.dirname(os.path.abspath(__file__))", f'HERE = {RD!r}'),
                ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", f'ROOT = {ROOT!r}')):
    assert rl in src, f'the receipt has moved; this rewrites it by: {rl}'
    src = src.replace(rl, new, 1)
anchor = "    rec, one = _ns['_matched'](RECORD), _ns['_matched'](ONE_RATE)"
assert anchor in src, 'the receipt has moved; this probe reads it by that line'
hacked = src.replace(anchor, anchor + f"\none = dict(one, pk=one['pk'] * {SCALE!r}, "
                                      f"a4=one['a4'] * {SCALE!r}, a3=one['a3'] * {SCALE!r}, "
                                      f"p12=one['p12'] * {SCALE!r}, p13=one['p13'] * {SCALE!r})"
                                      f"   # r7783 failability probe")


def run(text, tag):
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, 'probe.py')
        open(p, 'w', encoding='utf-8').write(text)
        r = subprocess.run([sys.executable, '-I', p], capture_output=True, text=True, cwd=RD,
                           timeout=3600)
    v, n = {}, 0
    for ln in r.stdout.splitlines():
        m = re.match(r'\s*\[(PASS|FAIL)\]', ln)
        if m:
            n += 1
            v[n] = m.group(1)
    print(f'  {tag:28s} rc={r.returncode}  ' + ' '.join(f'{k}:{s[0]}' for k, s in sorted(v.items())))
    return r.returncode, v


print(__doc__)
rc0, v0 = run(src, 'unperturbed')
rc1, v1 = run(hacked, f'one-rate arm x {SCALE}')
moved = sorted(k for k in v0 if v0[k] == 'PASS' and v1.get(k) == 'FAIL')
held = sorted(k for k in v0 if v0[k] == 'PASS' and v1.get(k) == 'PASS')
print(f'\n  gates that go RED under the perturbation: {moved}')
print(f'  gates that hold: {held}')
ok = rc0 == 0 and rc1 != 0 and moved
print(f'\n  {"PASS" if ok else "FAIL"}  the pins are failable: unperturbed rc={rc0}, '
      f'perturbed rc={rc1}, {len(moved)} gate(s) move')
raise SystemExit(0 if ok else 1)
