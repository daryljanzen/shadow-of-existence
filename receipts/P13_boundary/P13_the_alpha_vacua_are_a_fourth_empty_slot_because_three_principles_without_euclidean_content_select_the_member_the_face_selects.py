#!/usr/bin/env python3
"""P13 sec:synthesis / P7 frontier:realforms / P18 sec:frontier -- PO-94's quantum half, a fourth slot: de Sitter's
alpha-vacua are a one-parameter family of invariant vacuum states with a dimensionless parameter and physically
distinct members; Euclidean regularity on the compact face selects Bunch-Davies, and three principles with no
Euclidean content select the same member, so the face's selection is not distinctive on this freedom either.

WHAT IS CHECKED.  60's computation at r7616 (computations/beyond_the_wall/r7616_60_whether_anything_but_the_face_
selects_bunch_davies/alphavacua.py, registered before it existed in PREDICTION.md there) is run from source; its arms
are read and the figures the papers quote are pinned against its output:
  * the corpus commits to the member (P11's "clean, unitary Bunch--Davies quantization") and names the family 0 times;
  * the family returns the Bunch-Davies function in its own limit, on the unit-Wronskian normalisation;
  * regularity at the antipode selects the member (the registered arm C, which read the antipodal singularity as a
    pole of non-zero residue everywhere, is a MISS asserted to stay one; its correction C' holds: the pole and a
    delta-function on the antipodal light cone form a pair of magnitude e^a, vanishing only in the limit);
  * the Hadamard condition selects it: singular support {1} for Bunch-Davies, {1, -1} for the family, the local
    parametrix's support being {1} alone;
  * the positive-energy flat limit selects it: |beta|^2 = e^{2a}/(1 - e^{2a}) with zero derivative in H;
  * the control sorts three cases apart (an overall phase selected by nothing, the Wronskian by the commutation
    relation, the family by the face and by three other principles), and the voiding control does not void.
SCOPE.  Four empty slots are four instances, not a demonstration over every freedom the face could close: the
terminal clause is not fired.  The placement of hbar's register on the face is not touched.
"""
import contextlib
import io
import os
import re
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7616_60_whether_anything_but_the_face_selects_bunch_davies', 'alphavacua.py')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


buf = io.StringIO()
rc = 0
cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(COMP))
    with contextlib.redirect_stdout(buf):
        runpy.run_path(COMP, run_name='__main__')
except (AssertionError, SystemExit) as e:
    rc = 1 if not isinstance(e, SystemExit) else (e.code or 0)
finally:
    os.chdir(cwd)
out = buf.getvalue()
arm = dict(re.findall(r"^\s+([A-H]'?): (HIT|MISS)\s*$", out, re.M))

gate("60's computation runs from source: arms A, B, C', D, E, G HIT and the registered C a MISS asserted to stay one "
     "(16 checks, the one failure being that arm)",
     rc == 0 and all(arm.get(a) == 'HIT' for a in ['A', 'B', "C'", 'D', 'E', 'G']) and arm.get('C') == 'MISS'
     and '16 checks, 1 failures' in out and "Ⓒ as registered" in out)
gate("the corpus commits to the member in P11 and names the family 0 times",
     'Bunch--Davies quantization" in [\'dynamics_paper\']' in out and "the family's names occur 0 times" in out)
gate("the family returns the Bunch-Davies function in its own limit, on the unit-Wronskian normalisation",
     'equals the Bunch-Davies function c/(1-Z)' in out and '|N|^2 (1 - |e^alpha|^2) = 1' in out)
gate("Hadamard: singular support {1} for Bunch-Davies and {1, -1} for the family",
     re.search(r'singular support of the Bunch-Davies function in Z : \{1\}', out) is not None
     and re.search(r'singular support of G_alpha in Z\s+: \{1, -1\}', out) is not None)
gate("the flat limit: |beta|^2 = e^{2a}/(1 - e^{2a}) with zero derivative in H",
     '|beta_alpha|^2 = exp(2*a)/(1 - exp(2*a))' in out and 'd|beta|^2 / dH = 0' in out)
gate("the control sorts three cases apart and the voiding control does not void",
     'Ⓖ HIT: the test sorts three cases apart' in out and 'Ⓗ does not void' in out)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
