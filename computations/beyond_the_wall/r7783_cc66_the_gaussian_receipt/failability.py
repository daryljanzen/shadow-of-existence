#!/usr/bin/env python3
"""r7783+cc66: FAILABILITY of the Gaussian receipt, MEASURED and not asserted.

Perturbs the projection distance's MEASURED move by 1 + 1e-2 -- a one per cent change in the move
itself, so l_D shifts by 0.068 of a multipole instead of 6.788 -- and reports which of the seven
gates go red.  A pin that does not move under this is not a pin.

⛔ WHY NOT PERTURB `r`, WHICH WAS THIS PROBE'S FIRST KNOB: the receipt builds the joint-fit
receipt's declared INPUT line from `R_SIG` and `LD0` and refuses to run if that line is not found,
which is a GOOD coupling -- it asserts the published values -- but it makes either of them the wrong
knob: perturbing one makes the receipt exit FATAL before any fit, so no gate moves and the probe
measures nothing.  Measured: the first form of this probe did exactly that.
"""
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RD = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
RCPT = os.path.join(RD, 'P15_the_gaussian_residual_survives_on_the_one_rate_at_1_5238_chi2_per_bin_'
                        'and_the_arms_own_residual_runs_the_other_way.py')
SCALE = 1.0 + 1e-2
src = open(RCPT, encoding='utf-8').read()
# ⛔ FIRST OCCURRENCE ONLY.  A global replace also hits these same two literals where the receipt
#   carries them as its OWN rewrite TARGETS for the joint-fit source, which breaks that rewrite and
#   kills every gate from (4) on -- measured, the first form of this probe did exactly that.
for rl, new in (("HERE = os.path.dirname(os.path.abspath(__file__))", f'HERE = {RD!r}'),
                ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", f'ROOT = {ROOT!r}')):
    assert rl in src, f'the receipt has moved; this rewrites it by: {rl}'
    src = src.replace(rl, new, 1)
anchor = 'LD1 = LD0 * (1.0 + mv)'
assert anchor in src, 'the receipt has moved; this probe reads it by that line'
hacked = src.replace(anchor, f'LD1 = LD0 * (1.0 + mv * {SCALE!r})   # r7783 failability probe')


def run(text, tag):
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, 'probe.py')
        open(p, 'w', encoding='utf-8').write(text)
        r = subprocess.run([sys.executable, '-I', p], capture_output=True, text=True, cwd=RD,
                           timeout=1800)
    v, n = {}, 0
    for ln in r.stdout.splitlines():
        if re.match(r'\s*\[(PASS|FAIL)\]', ln):
            n += 1
            v[n] = re.match(r'\s*\[(PASS|FAIL)\]', ln).group(1)
    print(f'  {tag:24s} rc={r.returncode}  ' + ' '.join(f'{k}:{s[0]}' for k, s in sorted(v.items())))
    return r.returncode, v


print(__doc__)
rc0, v0 = run(src, 'unperturbed')
rc1, v1 = run(hacked, f'the distance move x {SCALE}')
moved = sorted(k for k in v0 if v0[k] == 'PASS' and v1.get(k) == 'FAIL')
held = sorted(k for k in v0 if v0[k] == 'PASS' and v1.get(k) == 'PASS')
print(f'\n  gates that go RED under the perturbation: {moved}')
print(f"  gates that hold (the paper's prose, the two receipts' source, the banked D_M, the arms): {held}")
ok = rc0 == 0 and rc1 != 0 and moved
print(f'\n  {"PASS" if ok else "FAIL"}  the pins are failable: unperturbed rc={rc0}, '
      f'perturbed rc={rc1}, {len(moved)} gate(s) move')
raise SystemExit(0 if ok else 1)
