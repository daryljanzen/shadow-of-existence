#!/usr/bin/env python3
"""P15 sec:diffusion-scale -- PO-24: THE SAME COMPARISON ON A BASELINE TAKEN FROM THE SAME DATA AS THE TAIL.  The
off-tail baseline is refitted on l <= 800 from the same data as each tail arm, and the signature mock rebuilt on it.
The baseline barely moves, because ACT's higher n_s lives in its high-l spectra, the tail itself: the ACT-Planck
offset and the signature's shift lie in the same direction in the same multipoles, and a baseline from below l = 800
cannot separate them.  On the arm that does not count the shared sky twice -- ACT alone on the tail, Planck cut where
ACT measures (P-ACT) -- the test is undecided, and it names the precision still missing.

WHAT IS CHECKED.  70's fits at r7627+70 (computations/beyond_the_wall/r7627_70_PO24_same_data_baseline/, registered
before the fits at a94ef55) are read through 70's own decide.py, which applies the strict 2 sigma rule; this receipt
runs no likelihood.  Pinned:
  * the baselines on l <= 800: Planck alone 0.96095, Planck + ACT 0.9624 +/- 0.0062, the P-ACT cut 0.9592 +/- 0.00635;
  * ACT alone (P-ACT), l = 1000-2508: the predictions 2.93 sigma apart, the sky 1.52 sigma from no shift and 1.41
    from the signature -- undecided, sigma must shrink 1.31 times;
  * ACT alone (P-ACT), l = 700-1760: 2.41 sigma apart, the sky 0.69 and 1.72 -- undecided, 1.16 times missing;
  * Planck + ACT summed (the shared sky counted twice): the sky 2.36 (1000-2508) and 2.45 (700-1760) sigma from the
    signature and inside 1 sigma of no shift -- past the line, in the bounding arm.
INHERITED.  The six-parameter flat-LCDM fit is adopted as the standard instrument for reading a tilt off a window, as
in r7489 and r7625; the tilt is inherited boundary data in P15.
"""
import contextlib
import io
import os
import re
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7627_70_PO24_same_data_baseline')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


buf = io.StringIO()
cwd = os.getcwd()
try:
    os.chdir(D)
    with contextlib.redirect_stdout(buf):
        runpy.run_path(os.path.join(D, 'decide.py'), run_name='__main__')
finally:
    os.chdir(cwd)
out = buf.getvalue()
print(out)

b = re.search(r'Planck alone ([\d.]+)\s+sum ([\d.]+) \+/- ([\d.]+).*pcut ([\d.]+) \+/- ([\d.]+)', out)
rows = {(m.group(1), m.group(2)): [float(x) for x in m.group(3, 4, 5, 6, 7, 8, 9, 10)] + [m.group(11)]
        for m in re.finditer(r'^\s+(sum|pact)\s+(\d+_\d+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([+-][\d.]+)\s+([+-][\d.]+)'
                             r'\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+(.*)$', out, re.M)}
gate("baselines on l <= 800: Planck 0.96095, Planck + ACT 0.9624 +/- 0.0062, P-ACT 0.9592 +/- 0.00635",
     b is not None and abs(float(b.group(1)) - 0.96095) < 5e-6 and abs(float(b.group(2)) - 0.9624) < 5e-5
     and abs(float(b.group(3)) - 0.0062) < 5e-5 and abs(float(b.group(4)) - 0.9592) < 5e-5
     and abs(float(b.group(5)) - 0.00635) < 5e-6)
p1, p7 = rows.get(('pact', '1000_2508')), rows.get(('pact', '700_1760'))
s1, s7 = rows.get(('sum', '1000_2508')), rows.get(('sum', '700_1760'))
gate("ACT alone, 1000-2508: 2.93 sigma apart, sky 1.52 from no shift and 1.41 from the signature, 1.31 times missing",
     p1 and abs(p1[5] - 2.93) < 0.005 and abs(p1[6] - 1.52) < 0.005 and abs(p1[7] - 1.41) < 0.005
     and 'undecided' in p1[8] and re.search(r'shrink 1\.31x', p1[8]) is not None)
gate("ACT alone, 700-1760: 2.41 sigma apart, sky 0.69 and 1.72, 1.16 times missing",
     p7 and abs(p7[5] - 2.41) < 0.005 and abs(p7[6] - 0.69) < 0.005 and abs(p7[7] - 1.72) < 0.005
     and 'undecided' in p7[8] and re.search(r'shrink 1\.16x', p7[8]) is not None)
gate("Planck + ACT summed: the sky 2.36 and 2.45 sigma from the signature, inside 1 sigma of no shift",
     s1 and s7 and abs(s1[7] - 2.36) < 0.005 and abs(s7[7] - 2.45) < 0.005 and s1[6] < 1 and s7[6] < 1
     and 'AGAINST' in s1[8] and 'AGAINST' in s7[8])
gate("the decision belongs to the arm that does not double-count the sky, and there neither window reaches 2 sigma",
     p1[7] < 2 and p1[6] < 2 and p7[7] < 2 and p7[6] < 2)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
