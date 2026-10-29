#!/usr/bin/env python3
"""P15 sec:refit-bound, P7 frontier:scalar, P18 sec:frontier -- PO-87: ON THE ARM OF RECORD THE FOURTH ACOUSTIC FEATURE
IS THE CONTROL'S TO UNDER A MULTIPOLE, IN TEMPERATURE AND IN BOTH POLARISATION SPECTRA.  The arm of record is the
two-arm instrument's ruled configuration, recombination solved on the leaf rate, refitted there by the procedure the
185-bin refit used.  On it the arm and the control differ at the fourth feature by less than what the two skies
together resolve in every spectrum, so the fourth peak's offset from the sky is the two models' common one.

WHAT IS CHECKED.  70's refit at r7633+70 (computations/beyond_the_wall/r7633_70_leafrec_refit/, registered before the
refit at 21f3e35b4).  The ACT bandpowers are an external file, so this receipt reads the run's RECORDED outputs
(refit_leafrec1.txt, verify_chi2.txt, score_refit.txt), as the r7625, r7629 and r7631 receipts read theirs, and
recomputes every quotient the papers print.  Pinned:
  * the refitted point H0 68.5707, Omega_m 0.291246, omega_b 0.021643, n_s 1.015066, and its verified chi^2 297.7 on
    185 bins (452.9 at the unrefitted point, 292.4 off the leaf rate, the control 186.5);
  * the arm-control differences 0.69 (TT), 0.92 (EE), -0.21 (TE), each below the combined skies' spread 1.87, 1.67,
    1.24, recomputed as 0.37, 0.55, 0.17 of it;
  * the joint score over the three spectra, 0.09 sigma at W = 55 and 0.28 at W = 80 on the combined skies.
INHERITED.  The bandpower covariances are the experiments' own; the locator is PO-47's.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7633_70_leafrec_refit')
F = open(os.path.join(D, 'refit_leafrec1.txt'), encoding='utf-8').read()
V = open(os.path.join(D, 'verify_chi2.txt'), encoding='utf-8').read()
S = open(os.path.join(D, 'score_refit.txt'), encoding='utf-8').read()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


b = re.search(r'BEST H0=([\d.]+) OM=([\d.]+) WB=([\d.]+) NS=([\d.]+)', F)
gate("the refitted point: H0 68.5707, Omega_m 0.291246, omega_b 0.021643, n_s 1.015066",
     b is not None and abs(float(b.group(1)) - 68.5707) < 5e-5 and abs(float(b.group(2)) - 0.291246) < 5e-7
     and abs(float(b.group(3)) - 0.021643) < 5e-7 and abs(float(b.group(4)) - 1.015066) < 5e-7)
chi = {k: float(v) for k, v in re.findall(r'(at r6941 point|refitted \(verify run\)|r6941 \(banked verify\)|control \(banked verify\))[^:]*: chi2\s+([\d.]+)', V)}
gate("chi^2 on 185 bins: 297.7 refitted, 452.9 unrefitted, 292.4 off the leaf rate, 186.5 the control",
     abs(chi.get('refitted (verify run)', 0) - 297.7) < 0.05 and abs(chi.get('at r6941 point', 0) - 452.9) < 0.05
     and abs(chi.get('r6941 (banked verify)', 0) - 292.4) < 0.05 and abs(chi.get('control (banked verify)', 0) - 186.5) < 0.05)
d = {m.group(1): float(m.group(2)) for m in re.finditer(r'^\s+(TT|EE|TE): CR\s+[\d.]+\s+control\s+[\d.]+\s+arm - control ([+-][\d.]+)', S, re.M)}
bnd = {m.group(1): (float(m.group(2)), float(m.group(3))) for m in
       re.finditer(r'^\s+(TT|EE|TE)\s+P\+A bnd\s+([\d.]+)\s+[+-][\d.]+\s+([+-]?[\d.]+)', S, re.M)}
gate("arm-control at the fourth feature: +0.69 (TT), +0.92 (EE), -0.21 (TE)",
     abs(d.get('TT', 9) - 0.69) < 0.005 and abs(d.get('EE', 9) - 0.92) < 0.005 and abs(d.get('TE', 9) + 0.21) < 0.005)
gate("each below the combined skies' spread 1.87, 1.67, 1.24: 0.37, 0.55, 0.17 of it, recomputed",
     all(k in bnd for k in ('TT', 'EE', 'TE'))
     and abs(bnd['TT'][0] - 1.87) < 0.005 and abs(bnd['EE'][0] - 1.67) < 0.005 and abs(bnd['TE'][0] - 1.24) < 0.005
     and all(abs(abs(d[k]) / bnd[k][0] - abs(bnd[k][1])) < 0.006 for k in ('TT', 'EE', 'TE'))
     and all(abs(d[k]) < bnd[k][0] for k in ('TT', 'EE', 'TE')))
j = {m.group(1): float(m.group(2)) for m in re.finditer(r'combined (W=\d+): arms apart chi2\s+[\d.]+ \(3 dof\) = ([\d.]+) sigma', S)}
gate("jointly over the three spectra on the combined skies: 0.09 sigma (W = 55), 0.28 (W = 80)",
     abs(j.get('W=55', 9) - 0.09) < 0.005 and abs(j.get('W=80', 9) - 0.28) < 0.005)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
