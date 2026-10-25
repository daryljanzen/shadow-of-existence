#!/usr/bin/env python3
"""P13 sec:synthesis / P7 frontier:realforms / P18 sec:frontier -- PO-94's gauge half: the three routes to a field
strength on the compact face outside isometry that the construction offers directly are each closed by a computed
reason, and the result is not that no route exists.

WHAT IS CHECKED.  cc66's computation at r7611+cc66 (computations/beyond_the_wall/r7611_cc66_the_gauge_halfs_
discharge_clause/routes.py, registered before it existed in PREDICTION.md there) is run from source; every one of
its 20 checks must pass, and the figures the papers quote are pinned against its output:
  * the curvature test sees a field strength that is there and is normalised (the monopole connection on S^2,
    first Chern number 1), and the corpus's own branch-point bundle comes back flat with the holonomy group of
    order 27, P14's own;
  * the dynamics-induced connection: a connection preserving a real metric is antisymmetric, 3 free components
    against su(3)'s 8 (reality, 5 of 8 parameters dying); its Berry member needs a state varying over a base, and
    a Berry connection on a family that does not vary has zero curvature, the control on one that does returning
    a non-zero one;
  * the horizon's thermal state: the datum is beta = 2 pi alpha, a function of alpha alone, and the space of
    two-forms over a one-parameter base is zero-dimensional (1 and 3 at p = 2 and 3, the control);
  * the wall-sourced field strength: the flat connection has no deformations, H^1(G, su(3)) = 0 on the order-27
    group, the same machinery returning 2 on the infinite cyclic group (the control);
  * and the verdict asserts the result is not that no route exists, the spectral-triple route being unexamined.
SCOPE.  Not an argument that no route exists: a composite or emergent connection and a spectral triple are not
among the three and are not examined.  The structural identification of colour's algebra on the compact face is
not touched.
"""
import contextlib
import io
import os
import re
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7611_cc66_the_gauge_halfs_discharge_clause',
                    'routes.py')
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

n_pass = len(re.findall(r'^\s+\[PASS\]', out, re.M))
n_fail = len(re.findall(r'^\s+\[FAIL\]', out, re.M))


def has(*pats):
    return all(re.search(p, out) for p in pats)


gate(f"cc66's computation runs from source and every check it makes passes ({n_pass} pass, 0 fail)",
     rc == 0 and n_pass == 20 and n_fail == 0 and 'ALL CHECKS PASS' in out)
gate("the curvature test is normalised on a field strength that is there (monopole, c_1 = 1), and the corpus's "
     "branch-point bundle comes back flat with holonomy group of order 27",
     has(r'->\s+c_1 = 1\b', r'\|G\| = 27 against', r'canonical connection vanishes IDENTICALLY.*->\s+F = 0'))
gate("reality: a metric connection has 3 free components against su(3)'s 8, and 5 of su(3)'s 8 parameters die "
     "under the reality condition",
     has(r"3 free components, not 8\s+->\s+free \['A_10', 'A_20', 'A_21'\]", r'kills 5 of 8 parameters'))
gate("and a Berry curvature needs a varying state: zero on a family that does not vary, non-zero on one that does",
     has(r'does not vary over the base has curvature identically zero\s+->\s+F = 0', r'->\s+F = -sin\(2\*s1\)'))
gate("dimension: the thermal datum is beta = 2 pi alpha alone, and two-forms over a one-parameter base number 0 "
     "(1 and 3 at p = 2 and 3)",
     has(r"free symbols \['alpha'\]", r'p=1 -> 0\s+p=2 -> 1\s+p=3 -> 3'))
gate("rigidity: H^1(G, su(3)) = 0 on the order-27 group, 2 on the infinite cyclic control",
     has(r'dim Z\^1 = 8\s+dim B\^1 = 8\s+dim H\^1 = 0', r'dim H\^1\(Z, su\(3\)\) = 2'))
gate("and the verdict is not that no route exists: the spectral-triple route is open and not among the three",
     has(r'the result is NOT that no route exists', r'spectral-triple route is open, unexamined'))

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
