#!/usr/bin/env python3
"""P15 sec:refit-bound, P7 frontier:scalar, P18 sec:frontier -- PO-87: THE FOURTH ACOUSTIC FEATURE IN POLARISATION.
ACT DR6 locates it more tightly in EE and TE than any experiment does in temperature; Planck and ACT place it apart
by about one and a half (EE) and two (TE) standard deviations of their combined spread; and the arm's own feature
moves by several multipoles with the rate recombination is solved on, so the comparison waits on the arm refitted
with recombination on the leaf rate and scored on both skies in all three spectra.

WHAT IS CHECKED.  70's measurement at r7631+70 (computations/beyond_the_wall/r7631_70_PO87_polarisation/, registered
before it ran at 3a049d4b8) adds an EE/TE save to the two-arm instrument (off by default, TT byte-identical to the
banked spectra) and applies PO-47's locator to the sky and to both arms.  The ACT bandpowers are an external SACC
file, so this receipt reads the run's RECORDED outputs (measure_leafrec1.txt, measure_r6941config.txt,
validate.txt), as the r7625 and r7629 receipts read theirs, and recomputes every quotient the papers print.  Pinned:
  * the instrument's control against CAMB at the fourth feature: -1.6 in TT and in EE, so the offset is common;
  * the sky's fourth feature, combined spread at W = 55: TT 2.35 (Planck) and 3.06 (ACT); EE 1.72 (ACT) against
    6.84 (Planck); TE 1.44 (ACT) against 2.43 (Planck);
  * the two skies' locations: EE 1001.2 and 990.6, 10.6 apart, 1.50 combined sigma; TE 1068.7 and 1074.2, 5.5
    apart, 1.95 combined sigma;
  * the arm's TT feature at 1129.58 with recombination on the stacking configuration and 1124.56 on the leaf
    rate, 5.0 multipoles, while the control does not move (1128.09 in both runs).
INHERITED.  The bandpower covariances are the experiments' own; the locator is PO-47's.
"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7631_70_PO87_polarisation')
L1 = open(os.path.join(D, 'measure_leafrec1.txt'), encoding='utf-8').read()
L0 = open(os.path.join(D, 'measure_r6941config.txt'), encoding='utf-8').read()
V = open(os.path.join(D, 'validate.txt'), encoding='utf-8').read()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def sky(text):
    out = {}
    for m in re.finditer(r'^\s+(TT|EE|TE)\s+(Planck|ACT)\s+([\d.]+)\s+[\d.]+\s+[\d.]+\s+[\d.]+\s+([\d.]+)\s+([\d.]+)', text, re.M):
        out[(m.group(1), m.group(2))] = (float(m.group(3)), float(m.group(4)))
    return out


def arms(text):
    return {m.group(1): (float(m.group(2)), float(m.group(3))) for m in
            re.finditer(r'^\s+(TT|EE|TE): CR\s+([\d.]+)\s+control\s+([\d.]+)', text, re.M)}


S1, S0 = sky(L1), sky(L0)
gate("the sky's numbers are the sky's: identical in the two runs", S1 == S0 and len(S1) == 6)
dV = {m.group(1): [float(x) for x in m.group(2).split()] for m in
      re.finditer(r'^\s*(TT|EE) instrument.*\n.*CAMB.*\n\s+diff\s+\[([^\]]+)\]', V, re.M)}
gate("the control against CAMB at the fourth feature: -1.6 in TT and in EE, a common offset",
     abs(dV['TT'][3] + 1.6) < 0.05 and abs(dV['EE'][3] + 1.6) < 0.05)
gate("combined spread at W = 55: TT 2.35 (Planck), 3.06 (ACT)",
     abs(S1[('TT', 'Planck')][1] - 2.35) < 0.005 and abs(S1[('TT', 'ACT')][1] - 3.06) < 0.005)
gate("EE 1.72 (ACT) against 6.84 (Planck); TE 1.44 (ACT) against 2.43 (Planck)",
     abs(S1[('EE', 'ACT')][1] - 1.72) < 0.005 and abs(S1[('EE', 'Planck')][1] - 6.84) < 0.005
     and abs(S1[('TE', 'ACT')][1] - 1.44) < 0.005 and abs(S1[('TE', 'Planck')][1] - 2.43) < 0.005)
dEE = S1[('EE', 'Planck')][0] - S1[('EE', 'ACT')][0]
dTE = S1[('TE', 'ACT')][0] - S1[('TE', 'Planck')][0]
zEE = dEE / math.hypot(S1[('EE', 'Planck')][1], S1[('EE', 'ACT')][1])
zTE = dTE / math.hypot(S1[('TE', 'Planck')][1], S1[('TE', 'ACT')][1])
gate(f"the skies apart: EE {dEE:.1f} ({zEE:.2f} combined sigma), TE {dTE:.1f} ({zTE:.2f})",
     abs(dEE - 10.6) < 0.05 and abs(zEE - 1.50) < 0.005 and abs(dTE - 5.5) < 0.05 and abs(zTE - 1.95) < 0.005)
A1, A0 = arms(L1), arms(L0)
gate("the arm's TT feature: 1129.58 and 1124.56, 5.0 apart, the control 1128.09 in both",
     abs(A0['TT'][0] - 1129.58) < 0.005 and abs(A1['TT'][0] - 1124.56) < 0.005
     and abs((A0['TT'][0] - A1['TT'][0]) - 5.02) < 0.005 and A0['TT'][1] == A1['TT'][1] == 1128.09)
gate("and the arm moves in all three spectra while the control does not",
     all(A0[k][1] == A1[k][1] for k in ('TT', 'EE', 'TE')) and all(abs(A0[k][0] - A1[k][0]) > 2 for k in ('TT', 'EE', 'TE')))

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
