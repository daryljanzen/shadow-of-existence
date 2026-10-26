#!/usr/bin/env python3
"""P13 sec:synthesis / sec:face-status -- PO-94's gauge half, the fourth of B59's five routes: the
spectral-triple route over the LEAF, where the corpus supplies its pieces, is closed, and it closes on the
LOCUS rather than on the real structure B61 expected; a triple over the FACE is left open.

WHAT IS CHECKED.  cc66's computation at r7613+cc66
(computations/beyond_the_wall/r7613_cc66_the_spectral_triple_route/spectral.py, registered before it
existed in PREDICTION.md there) is run from source; every one of its 22 checks must pass, and the
figures the row quotes are pinned against its output:
  * P14 supplies H and D over the LEAF, and the leaf is a compact ONE-dimensional domain; the space
    of two-forms over a one-dimensional base is ZERO-dimensional, counted by solving M + M^T = 0 and
    not by quoting a binomial, with the counter returning 1, 3 and 10 at p = 2, 3 and 5 as the
    control -- so a connection over the leaf has no object a field strength could be;
  * over the FACE the corpus states no piece and no obstruction to one: P13 sec:face-status says the
    round face carries no Dirac zero modes, which bears on massless content and not on whether a Dirac
    operator exists there -- the round five-sphere carries one -- so a triple over the face is open;
  * on the reading H = ker D the route closes twice over: P14's (3,0) chirality admits no
    grading-reversing J, the gap being 3 against 0 on a balanced space where the J is EXHIBITED, and
    every inner fluctuation a[D,b] vanishes, rank 0 against rank 11 on a circle triple;
  * the order-one condition does NOT close the route -- it holds vacuously, because D is zero on a
    kernel -- and that is reported as a pass that buys the route nothing;
  * and the checker is certified on a triple that IS one (the two-point bimodule: J^2 = 1, JD = DJ,
    order-one exact, and [D,a] non-zero so the arm is not vacuous), with the order-one expression
    shown able to FAIL on a generic non-commutative pair.
SCOPE.  Not an argument that no route exists: a triple over the face, C^inf(face) tensor M_3(C) with the
face's own Dirac operator, is not examined, and B59's composite/emergent route is untouched.  Not that a coupling follows (PO-5).  Not that B61 is weakened -- its
rows are read, not re-derived, except the grading, recomputed so nothing is inherited on trust.
"""
import contextlib
import io
import os
import re
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7613_cc66_the_spectral_triple_route',
                    'spectral.py')
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


gate(f"cc66's computation runs from source and every check it makes passes ({n_pass} pass, {n_fail} fail)",
     rc == 0 and n_pass == 22 and n_fail == 0 and 'ALL CHECKS PASS' in out)
gate('the pieces are READ from the papers and not recalled: P14 states that the leaf is compact with a '
     "finite analytical index, and that the wall kernel is (3,0); P13 sec:face-status states the face's "
     'obstruction in its own words',
     has(r'supplies D and its domain in its own words.*->\s+found in matter_sector_paper\.tex',
         r'ONE-CHIRALITY and gives both dimensions.*->\s+found in matter_sector_paper\.tex',
         r'FACE obstruction in its own words.*->\s+found in boundary_paper\.tex'))
gate('PINNED: the leaf is one-dimensional and carries ZERO independent two-forms, with the counter '
     'returning 1, 3 and 10 at p = 2, 3 and 5 so the zero is the leaf and not the counter',
     has(r'two-forms over the leaf \(p=1\) = 0\b', r'p=2 -> 1, p=3 -> 3, p=5 -> 10\b'))
gate('PINNED: the chirality gap on the kernel reading is 3, against 0 on a balanced space where the J '
     'is exhibited anti-commuting with the grading and squaring to +1',
     has(r'\|dim ker_\+ - dim ker_-\| = 3\b', r'gap = 0, \|\|Jgamma\+gammaJ\|\| = 0', r'\|\|J\^2-1\|\| = 0'))
gate('PINNED: the inner fluctuations over the kernel span rank 0, against rank 11 for the same '
     'expression on the circle triple, so the zero is the pieces and not the formula',
     has(r'rank of their span = 0\b', r"circle triple's fluctuation span = 11\b"))
gate('PINNED: the order-one condition holds VACUOUSLY on the kernel (defect 0) while the same '
     'expression is violated on a generic non-commutative pair, so the vacuous pass is a measurement',
     has(r'order-one defect = 0', r'violable there \('))
gate('the checker is certified on a triple that IS one: J^2 = +1, JD = DJ, the order-one defect 0 '
     'exactly, and [D,a] non-zero so that arm is not vacuous',
     has(r'\|\|JDJ\^-1 - D\|\| = 0', r'max \|\|\[\[D,a\],Jb\*J\^-1\]\|\| = 0',
         r'max \|\|\[D,a\]\|\| = 17\b'))
gate("and the circle comes back the OTHER way, plain conjugation ANTI-commuting with -i d/dtheta, so "
     'the checker distinguishes a real structure from something that merely looks like one',
     has(r'\|\|JDJ\^-1 - D\|\| = 26\.98\b', r'\|\|JDJ\^-1 \+ D\|\| = 0'))
gate('and the verdict is the pre-registered outcome 2 with the piece NAMED, the locus firing before '
     'the real structure is reached, and it is not that no route exists',
     has(r'CLOSED ON THE PIECES THE CORPUS SUPPLIES, AND IT CLOSES ON THE LOCUS',
         r"NOT \"NO ROUTE EXISTS\"", r'locus closes it; order-one passes vacuously'))

bad = [n for n, ok in CHECKS if not ok]
print(f'\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail')
for n in bad:
    print(f'    FAILED: {n}')
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
