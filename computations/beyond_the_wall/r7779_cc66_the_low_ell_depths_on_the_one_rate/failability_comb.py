#!/usr/bin/env python3
"""r7779+cc66: FAILABILITY of the comb receipt's figure pin, MEASURED and not asserted.

Perturbs the LEAFGEOM=1 arm's multipole axis by a 1 + 3e-3 stretch -- a change far smaller than the
features the receipt reads, and one that moves ONLY the peak positions -- and reports which of the
nine gates go red.  A pin that does not move under this is not a pin.
"""
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_fitted_comb_moves_nine_times_less_than_the_scale_that_rules_it_'
                    'so_the_one_rate_takes_the_comb_from_299_1_to_298_94.py')
STRETCH = 1.0 + 3e-3
src = open(RCPT, encoding='utf-8').read()
# the copy runs from a scratch directory, so pin ROOT absolutely -- BOTH copies, so the baseline and
# the perturbed run differ in the perturbation and in nothing else.
_root_line = "ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))"
assert _root_line in src, 'the receipt has moved; this probe rewrites it by that line'
src = src.replace(_root_line, f'ROOT = {ROOT!r}')
anchor = 'S, L = arm(STACK), arm(LEAF)'
assert anchor in src, 'the receipt has moved; this probe reads it by that line'
hacked = src.replace(anchor, anchor + f"\nL['ls'] = L['ls'] * {STRETCH!r}   # r7779 failability probe")


def verdicts(text):
    out = {}
    for n, ln in enumerate(l for l in text.splitlines() if l.strip().startswith('[')):
        m = re.match(r'\s*\[(PASS|FAIL)\]', ln)
        if m:
            out[n + 1] = m.group(1)
    return out


def run(text, tag):
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, 'probe.py')
        open(p, 'w', encoding='utf-8').write(text)
        r = subprocess.run([sys.executable, '-I', p], capture_output=True, text=True, cwd=os.path.dirname(RCPT))
    v = verdicts(r.stdout)
    print(f'  {tag:28s} rc={r.returncode}  ' + ' '.join(f'{k}:{s[0]}' for k, s in sorted(v.items())))
    return r.returncode, v


print(__doc__)
rc0, v0 = run(src, 'unperturbed')
rc1, v1 = run(hacked, f'ls x {STRETCH}')
moved = sorted(k for k in v0 if v0[k] == 'PASS' and v1.get(k) == 'FAIL')
held = sorted(k for k in v0 if v0[k] == 'PASS' and v1.get(k) == 'PASS')
print(f'\n  gates that go RED under the perturbation: {moved}')
print(f'  gates that hold (they read configs, blobs and stored scalars, not peak positions): {held}')
ok = rc0 == 0 and rc1 != 0 and moved
print(f'\n  {"PASS" if ok else "FAIL"}  the pin is failable: '
      f'unperturbed rc={rc0}, perturbed rc={rc1}, {len(moved)} gate(s) move')
raise SystemExit(0 if ok else 1)
