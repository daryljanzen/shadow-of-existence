#!/usr/bin/env python3
"""P15 sec:refit-bound, P7 frontier:scalar, P18 sec:frontier -- PO-87: AT THE FOURTH PEAK THE TWO ARMS DIFFER BY
ABOUT HALF THE SKY'S LOCATING SPREAD, MOST OF EACH ARM'S OFFSET FROM THE SKY IS COMMON TO BOTH, AND NO MEASUREMENT OF
THE TEMPERATURE SPECTRUM CAN SEPARATE THEM.

WHAT IS CHECKED.  70's measurement at r7629+70 (computations/beyond_the_wall/r7629_70_PO87_fourth_peak_act/, registered
before it ran at 18cb2dfd4) applies PO-47's locator unchanged to Planck plik_lite and to ACT DR6 CMB-only.  The ACT
bandpowers are an external SACC file, so this receipt reads the run's RECORDED output (measure.txt), as the r7625
receipt reads its fit records, and recomputes every quotient the papers print from the recorded pairs.  Pinned:
  * the sky's fourth peak spreads by 2.34 multipoles on Planck and 3.03 on ACT alone, ACT 0.77 times as precise;
  * the arm and the control differ by +1.31 on the fine grid, 0.56 of Planck's spread and 0.43 of ACT's, 0.71 of
    the combined bound;
  * the control carries 0.84 of the arm's offset from the sky (0.78 to 0.87);
  * on a full sky without noise the located peak spreads by 1.27 (W = 55) and 0.75 (W = 80), against the 0.65
    that would put 1.31 at two standard deviations.
INHERITED.  The bandpower covariances are the experiments' own; the locator is PO-47's, unchanged.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
T = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7629_70_PO87_fourth_peak_act', 'measure.txt'),
         encoding='utf-8').read()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def row(label):
    m = re.search(re.escape(label) + r'\s+([\d.]+)\s+([+-][\d.]+)\s+([\d.]+)\s+([+-][\d.]+)\s+([+-][\d.]+)\s+(\S+)', T)
    return None if m is None else [float(m.group(k)) for k in range(1, 6)] + [m.group(6)]


sky = {k: float(v) for k, v in re.findall(r'(Planck plik_lite|ACT DR6 CMB-only): l4 =\s+[\d.]+ .*?combined ([\d.]+)', T)}
gate("the sky's fourth peak spreads by 2.34 (Planck) and 3.03 (ACT alone)",
     sky.get('Planck plik_lite') == 2.34 and sky.get('ACT DR6 CMB-only') == 3.03)
ratio = re.search(r'ACT / Planck precision at the fourth peak: ([\d.]+)', T)
gate("ACT is 0.77 times as precise as Planck there, the recorded figure equal to the quotient 2.34/3.03",
     ratio is not None and float(ratio.group(1)) == 0.77 and round(2.34 / 3.03, 2) == 0.77)
BAND = re.search(r'Planck / fine.*?([\d.]+) \(([\d.]+) to ([\d.]+)\)', T)
P, A, C = row('Planck / fine'), row('ACT alone (P-ACT) / fine'), row('Planck+ACT (bound) / fine')
gate("the arm and the control differ by +1.31 at the fourth peak", P and A and C and P[1] == A[1] == C[1] == 1.31)
gate("1.31 is 0.56 of Planck's spread, 0.43 of ACT's and 0.71 of the combined bound, each recomputed",
     P[2] == round(1.31 / P[0], 2) == 0.56 and A[2] == round(1.31 / A[0], 2) == 0.43
     and C[2] == round(1.31 / C[0], 2) == 0.71)
gate("the control carries 0.84 of the arm's offset from the sky on Planck (6.67 of 7.98), 0.78 to 0.87",
     P[3] == 6.67 and P[4] == 7.98 and round(P[3] / P[4], 2) == 0.84
     and BAND is not None and abs(float(BAND.group(1)) - 0.84) < 0.005
     and abs(float(BAND.group(2)) - 0.78) < 0.005 and abs(float(BAND.group(3)) - 0.87) < 0.005)
fl = dict(re.findall(r'full sky, (W=\d+): sigma\(l4\) = ([\d.]+)', T))
need = re.search(r'separating \+1\.31 at 2 sigma needs sigma\(l4\) <= ([\d.]+)', T)
f55, f80 = float(fl.get('W=55', 'nan')), float(fl.get('W=80', 'nan'))
gate("full sky, no noise: 1.27 (W = 55) and 0.75 (W = 80), against the 0.65 that 2 sigma needs",
     abs(f55 - 1.27) < 0.005 and abs(f80 - 0.75) < 0.005 and need is not None and abs(float(need.group(1)) - 0.65) < 0.005
     and round(1.31 / 2, 3) == 0.655 and float(fl['W=80']) > 0.655)
gate("so even a full noise-free temperature sky puts the arms at most 1.74 sigma apart",
     re.search(r'W=80: sigma\(l4\) = 0\.75 .*would sit at 1\.74 sigma', T) is not None and abs(1.31 / 0.75 - 1.74) < 0.01)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
