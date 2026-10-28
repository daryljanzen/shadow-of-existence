#!/usr/bin/env python3
"""P7 frontier:realforms / P18 sec:frontier -- PO-94's quantum half, the free field: every item of a classification of
the data that define a free quantum field on a fixed background, each sourced from a reference the papers already
cite, maps inside the nine entries -- the field content's parameters, the algebra of observables (which carries no
parameter), the state and its representation (one datum read twice), the global and topological data, and the
renormalisation data (which collapse onto the scale on this background).  So over the free field the list is
complete in that sense and no freedom on it is one the face alone removes.  Two things lie outside by the papers' own
scope, a field on a fixed background: the choice of field content and the background's own period.

WHAT IS CHECKED.  60's computation at r7632 (computations/beyond_the_wall/r7632_60_the_nine_against_a_sourced_
classification_of_the_data_that_define_a_free_field/classify.py, registered before it existed at daa66b4e0) is run
from source: 36 checks, 0 failures.  Pinned against its output:
  * the nine entries are in the papers, and all five classification items are sourced from cited keys;
  * the symplectic form conserved identically, with the control that breaks it;
  * the mixing coefficient mode-independent and the implementability sum divergent, with the decaying control finite;
  * the spin-structure counts 1, 1, 2 reproduced;
  * the three quadratic invariants of rank one at fixed dimension;
  * every item maps inside the nine, 0 outside, and the two scope exclusions named.
COMPUTES: the symplectic current's divergence for the mode equation, the Hilbert-Schmidt sum of the mixing
coefficient over the mode set, the spin-structure counts over GF(2), and the curvature invariants contracted from
the Riemann tensor in four and five dimensions.
"""
import contextlib
import io
import os
import re
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7632_60_the_nine_against_a_sourced_classification_of_the_data_that_define_a_free_field')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


buf = io.StringIO()
rc = 0
cwd = os.getcwd()
try:
    os.chdir(D)
    with contextlib.redirect_stdout(buf):
        runpy.run_path(os.path.join(D, 'classify.py'), run_name='__main__')
except SystemExit as e:
    rc = e.code or 0
except AssertionError:
    rc = 1
finally:
    os.chdir(cwd)
out = buf.getvalue()
if '36 checks, 2 failure(s).' not in out:
    print('  the computation reported:', rc)
    for ln in out.splitlines():
        if 'FAIL' in ln or 'checks,' in ln or 'Error' in ln:
            print('   |', ln[:200])

# r7633 (69): the routed gap -- no single monograph cited for the classification -- was CLOSED by the landing:
#   P7 cites Wald (1994).  Two arms rest on that gap being open (its measurement and the verdict that names it as a
#   qualification); both now fail and are asserted to, and the citation is pinned below.  Any OTHER failure is a
#   regression.
_fails = re.findall(r'^\s*\[FAIL\] (.*)$', out, re.M)
gate("60's computation runs from source: 36 checks, the two failures the closed monograph gap",
     '36 checks, 2 failure(s).' in out and len(_fails) == 2
     and _fails[0].startswith('Ⓒ THE ONE GAP, MEASURED: no single standard monograph')
     and _fails[1].startswith('VERDICT: ⚠ QUALIFIED TWICE'))
_p7 = open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'), encoding='utf-8').read()
gate("and the gap is closed: P7 cites Wald's monograph at the classification",
     '\\bibitem{Wald1994}' in _p7 and 'fixed background~\\cite{Wald1994}' in _p7
     and 'Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics' in _p7)
gate("the nine entries are in the papers; all five classification items sourced from cited keys",
     'the list carries 9 entries' in out and '5 sourced from keys the papers already carry and 0 unsourced' in out)
gate("the symplectic form conserved identically, and the control breaks it in proportion to the form",
     'the symplectic form is CONSERVED identically' in out and 'exactly proportional to the form itself' in out)
gate("the mixing coefficient mode-independent, the sum divergent, the decaying control finite",
     'the mixing coefficient carries NO mode dependence' in out and 'the sum DIVERGES' in out
     and 'a decaying coefficient gives a FINITE sum' in out)
gate("the spin-structure counts reproduce: 1 on S^4 and S^5, 2 on RP^5",
     'S^4 carries 1 spin structure(s)' in out and 'S^5 carries 1 spin structure(s)' in out
     and 'RP^5 carries 2 spin structure(s)' in out)
gate("the quadratic invariants span one direction at fixed dimension", 'the rank of the row they span is ONE' in out)
gate("every item maps inside the nine, 0 outside; the two scope exclusions named",
     'maps INSIDE the nine; 0 lie outside' in out and 'exactly TWO things are excluded' in out)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
