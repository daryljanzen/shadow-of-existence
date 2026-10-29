#!/usr/bin/env python3
"""P7 frontier:realforms / P18 sec:frontier -- PO-94's quantum half, closed: the coupled theory's remaining data fall
inside the nine entries.  Its coupling is the scale (the regulator carries no cutoff, and the scale factors out of the
spectral sum exactly); its cubic and quartic vertices enter at exactly the inverse-square order where the boundary
coefficient already lives, bringing no new datum; its interaction counterterms are renormalisation data with the
scale (one-dimensional at fixed background, measured here on a general scale factor; two-dimensional once the scale
factor is quantized, imported from P10's anomaly result); and what stands outside, the completion of the tower's
definition, is a definition and not a freedom of the quantization.  With the free field complete (r7632) and the
coupled edge closed by finite form energy (cc66's r7631), every freedom the face could close is closed elsewhere,
and the quantum half rests as a rhyme at the level of the world while the placement of the scale stands.

WHAT IS CHECKED.  60's computation at r7634 (computations/beyond_the_wall/r7634_60_the_coupled_theorys_remaining_data_
against_the_nine/coupled.py, registered before it existed at 56e06b8a7) is run from source.  It has 22 checks; at the
head it was run on, 0 failed.  Three of its arms read the papers' OPEN statement of the half and the clause's wording,
which the landing this receipt supports replaced with the closure, so those three now fail and are asserted to fail,
the closure itself being pinned in P7.  Pinned against its output:
  * the quadratic invariants functionally independent on a general scale factor (rank 2) and of rank one on the
    admitted family, the control reproducing r7632;
  * the scale factoring out of every term of the spectral sum, the quotient's derivative identically zero;
  * the cubic's near-origin exponent exactly -2, a control term at -4/3;
  * the papers' own sentence that the completion is a different thing from a residual freedom, adjudicated;
  * the reachable negative did not arrive: no coupled datum lies outside the nine and is closed by the face alone.
COMPUTES: the Jacobian rank of the quadratic curvature invariants on a general and on the admitted scale factor, the
scale derivative of the spectral sum's terms, and the near-origin exponent of the cubic vertex in the geodesic
coordinate.
"""
import contextlib
import io
import os
import re
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7634_60_the_coupled_theorys_remaining_data_against_the_nine')
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
        runpy.run_path(os.path.join(D, 'coupled.py'), run_name='__main__')
except SystemExit as e:
    rc = e.code or 0
except AssertionError:
    rc = 1
finally:
    os.chdir(cwd)
out = buf.getvalue()

EXPECT = ('Ⓐ the clause is located at THIS head and unchanged',
          'Ⓐ and the open sentence now carries FOR THE COUPLED THEORY',
          'VERDICT: ⇒ THE CLAUSE FIRES FOR THE QUANTUM HALF ENTIRE')
_fails = re.findall(r'^\s*\[FAIL\] (.*)$', out, re.M)
if f'22 checks, {len(EXPECT)} failure(s).' not in out:
    print('  the computation reported:', rc)
    for ln in out.splitlines():
        if 'FAIL' in ln or 'checks,' in ln or 'Error' in ln:
            print('   |', ln[:200])
gate("60's computation runs from source: 22 checks, the 3 failures exactly the arms that read the now-closed open state",
     f'22 checks, {len(EXPECT)} failure(s).' in out and len(_fails) == len(EXPECT)
     and all(any(f.startswith(e) for e in EXPECT) for f in _fails))
gate("the quadratic invariants: rank 2 on a general scale factor, one direction on the admitted family",
     'their Jacobian in the two independent data has rank 2' in out and 'CONTROL REPRODUCES r7632' in out)
gate("the scale factors out of the spectral sum exactly, derivative identically zero",
     'factors out of the whole sum' in out and 'derivative identically zero' in out)
gate("the cubic's near-origin exponent exactly -2, the control at -4/3",
     'the exponent being -2' in out and 'it comes out at -4/3' in out)
gate("the papers' own sentence: the completion is a different thing from a residual freedom, adjudicated",
     'AND THE PAPERS THEMSELVES SAY IT IS NOT A FREEDOM' in out and 'Ⓔ ADJUDICATED' in out)
gate("the reachable negative did not arrive", 'THE REACHABLE NEGATIVE DID NOT ARRIVE' in out)
_p7 = ' '.join(open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'), encoding='utf-8').read().split())
gate("and the closure is in P7: every freedom the face could close is closed elsewhere, the half a rhyme",
     'So every freedom of the quantum theory the face could close is closed elsewhere' in _p7
     and 'the quantum half rests as a rhyme at the level of the world while the placement of the scale stands' in _p7)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
