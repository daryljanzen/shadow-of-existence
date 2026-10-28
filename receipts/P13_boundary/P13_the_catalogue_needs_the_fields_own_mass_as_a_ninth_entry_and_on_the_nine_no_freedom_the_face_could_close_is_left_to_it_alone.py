#!/usr/bin/env python3
"""P7 frontier:realforms / P18 sec:frontier -- PO-94's quantum half: every entry of the standard catalogue is scoped
by the papers' own sentences, the eight carry four real parameters, and the catalogue is not complete: the field's
own mass term (its mass and its coupling to curvature, which this background collapses to one combination) lies
outside all eight, and the face imposes no condition on it.  With it as a ninth entry, every freedom on the list
that the face could close is closed elsewhere, over the three enlargements tested; and the one place the papers
name the face as the only closer is the coupled tower's sub-threshold boundary condition.

WHAT IS CHECKED.  60's computation at r7630 (computations/beyond_the_wall/r7630_60_fixing_every_entrys_domain_and_
testing_whether_any_freedom_lies_outside_all_eight/domains.py, registered before it existed at becae87db) is run
from source: 46 checks, 0 failures.  Pinned against its output:
  * the voiding control does not void, and all 8 entries carry a located scoping sentence;
  * the extension's threshold gamma = 3/4 derived from the indicial equation, the extension one real parameter;
  * one reading covers the ordering family; the state control reproduces r7628;
  * the eight carry 4 real parameters in all;
  * the non-invariant states lie outside the state's domain and are closed by invariance, which has no Euclidean
    content;
  * the mass and curvature coupling map with rank one, and the face imposes zero equations on the combination;
  * at the patch's edge, in the coupled theory, the deficiency is a subspace, and no sentence carries a
    non-Euclidean closer to it.
COMPUTES: the indicial roots of the half-line operator over the ordering family, the spin-structure counts over
GF(2), the rank of the mass map, and the regular Euclidean branch's existence over the mass term.
"""
import contextlib
import io
import os
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7630_60_fixing_every_entrys_domain_and_testing_whether_any_freedom_lies_outside_all_eight')
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
        runpy.run_path(os.path.join(D, 'domains.py'), run_name='__main__')
except SystemExit as e:
    rc = e.code or 0
except AssertionError:
    rc = 1
finally:
    os.chdir(cwd)
out = buf.getvalue()

gate("60's computation runs from source: 46 checks, 0 failures", rc == 0 and '46 checks, 0 failure(s).' in out)
gate("the voiding control does not void; all 8 entries scoped by located sentences, 0 unscoped",
     'Ⓘ DOES NOT VOID' in out and '8 with a scoping sentence located verbatim and 0 unscoped' in out)
gate("the extension's threshold derived as gamma = 3/4, the extension one real parameter",
     'DERIVED as gamma = 3/4' in out and 'whose real dimension is ONE' in out)
gate("one reading covers the ordering family; the state control reproduces r7628",
     'ONE reading covers the whole family' in out and 'CONTROL REPRODUCES: both exclusion criteria are PHASE-BLIND' in out)
gate("the eight carry 4 real parameters in all", 'the eight entries carry 4 real parameters in all' in out)
gate("the non-invariant states: outside the state's domain, closed elsewhere by invariance",
     'INFINITE-dimensional' in out and 'Ⓕ CLOSED ELSEWHERE' in out)
gate("the mass term: rank one, zero equations from the face, outside all eight; the ninth entry the repair",
     'has rank ONE on this background' in out and 'Ⓖ ZERO EQUATIONS' in out
     and 'OUTSIDE all eight domains' in out and 'NINTH entry' in out)
gate("the coupled edge: a subspace, and no sentence carries a non-Euclidean closer to it",
     'the deficiency is a SUBSPACE rather than a line' in out
     and 'BUT NO sentence carries that closer to the coupled sub-threshold condition' in out)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
